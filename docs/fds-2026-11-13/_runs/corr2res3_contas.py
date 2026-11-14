#!/usr/bin/env python3
"""Segunda passada, correção da reserva 3 (plano de conteúdo de 90 dias).
Reconta, SÓ DE LEITURA, todo número que docs/plano_conteudo_90d.md escreve ou mantém:
  parte 1 - mapa de palavras-chave (data/palavras_chave.csv): filtros da coluna "Termos em K" e cobertura;
  parte 2 - a mesma cobertura nas versões antigas do mapa (git show, leitura), para explicar 168 x 167;
  parte 3 - números de busca (data/serp_sp.csv, data/serp_sp_ampliacao.csv e brutos em data/serp_raw/);
  parte 4 - leitura das dez páginas, colunas da planilha de medição, protótipo.
Biblioteca padrão. Não grava nada. Rodar com: python3 -B corr2res3_contas.py"""
import csv, json, os, io, glob, time, hashlib, collections, subprocess, itertools

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
C = collections.Counter
GUIA = ['baratas', 'ratos', 'cupim', 'percevejo', 'pombos', 'escorpião']
P5 = GUIA[:5]


def info(rel):
    p = os.path.join(RAIZ, rel)
    return f"{rel} | gravado {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(os.path.getmtime(p)))} | sha256 {hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]}"


def filtro(L):
    def f(**kw):
        return [r for r in L if all((r[k] in v) if isinstance(v, (set, list, tuple)) else (r[k] == v) for k, v in kw.items())]
    return f


def partes_cobertura(L, regiao, pragas_t3):
    """Devolve a lista ordenada (rótulo, linhas) dos filtros da seção 3 do plano."""
    f = filtro(L)
    conf = f(intencao='confiança')
    partes = [
        ('início (cidade, geral, contratar, residencial/geral)', f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral')),
        ('confiança', conf),
    ]
    for p in GUIA:
        partes.append((f'guia {p}: informativa', f(praga=p, intencao='informativa')))
        partes.append((f'guia {p}: cidade + contratar', f(praga=p, tipo_local='cidade', intencao='contratar')))
    partes.append((f'região {regiao}: zona + contratar', f(tipo_local='zona', local=regiao, intencao='contratar')))
    for p in pragas_t3:
        partes.append((f'T3 {p} x {regiao}: contratar e preço', f(praga=p, tipo_local='zona', local=regiao, intencao=['contratar', 'preço'])))
    partes.append(('preço + cidade', f(intencao='preço', tipo_local='cidade')))
    partes.append(('H05', [r for r in L if r.get('id_na_coleta') == 'H05']))
    partes.append(('público condomínio', f(publico='condomínio')))
    partes.append(('público restaurante', f(publico='restaurante')))
    partes.append(('informativas gerais (seção 4 do plano)', [r for r in f(intencao='informativa') if r['praga'] == 'geral']))
    return partes


def uniao(partes, fora=()):
    s = set()
    for rot, rs in partes:
        if any(rot.startswith(x) for x in fora):
            continue
        s.update(r['termo'] for r in rs)
    return s


# ---------------------------------------------------------------- parte 1
print('=' * 100)
print('PARTE 1 - MAPA DE PALAVRAS-CHAVE')
print(info('data/palavras_chave.csv'))
L = list(csv.DictReader(open(os.path.join(RAIZ, 'data', 'palavras_chave.csv'), encoding='utf-8')))
f = filtro(L)
print('linhas', len(L), '| termos distintos', len({r['termo'] for r in L}))
print('colunas', list(L[0].keys()))
print('volume', dict(C(r['volume'] for r in L)))
print('situacao_na_coleta', dict(C(r['situacao_na_coleta'] for r in L)))
print('origem_do_termo', dict(C(r['origem_do_termo'] for r in L)))
print('intencao', C(r['intencao'] for r in L).most_common())
print('tipo_local', C(r['tipo_local'] for r in L).most_common())
print('publico', C(r['publico'] for r in L).most_common())

print('\n-- início:', len(f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral')),
      [r['id_na_coleta'] for r in f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral')])
conf = f(intencao='confiança')
molde = lambda t: ('com licença' if 'com licença' in t else 'confiável' if 'confiável' in t else 'melhor' if t.startswith('melhor dedetizadora') else 'como saber' if t.startswith('como saber') else 'OUTRO')
print('-- confiança:', len(conf), dict(C(molde(r['termo']) for r in conf)), '| por tipo_local', dict(C(r['tipo_local'] for r in conf)))
print('   molde x tipo_local:', sorted(C((molde(r['termo']), r['tipo_local']) for r in conf).items()))
print('   coletados:', sorted((r['id_na_coleta'], r['termo']) for r in conf if r['id_na_coleta']))
for p in GUIA:
    a, b = f(praga=p, intencao='informativa'), f(praga=p, tipo_local='cidade', intencao='contratar')
    print(f'-- guia {p}: informativa {len(a)} {[r["termo"] for r in a]} | cidade+contratar {len(b)} {[(r["id_na_coleta"], r["termo"]) for r in b]}')
print('-- zona + contratar, por região:')
for z in sorted({r['local'] for r in L if r['tipo_local'] == 'zona'}):
    rs = f(tipo_local='zona', local=z, intencao='contratar')
    print('    ', z, len(rs), '| publico', dict(C(r['publico'] for r in rs)), '| praga=geral', sum(r['praga'] == 'geral' for r in rs))
tab = collections.defaultdict(C)
for r in L:
    if r['tipo_local'] == 'zona' and r['intencao'] in ('contratar', 'preço') and r['praga'] != 'geral':
        tab[(r['praga'], r['local'])][r['intencao']] += 1
print('-- praga x região (contratar, preço):', dict(C((v['contratar'], v['preço']) for v in tab.values())), '| pares', len(tab))
pc = f(intencao='preço', tipo_local='cidade')
print('-- preço + cidade:', len(pc), '| gerais', sum(r['praga'] == 'geral' for r in pc), '| de praga', sum(r['praga'] != 'geral' for r in pc),
      '| de praga sem guia', sum(r['praga'] not in GUIA + ['geral'] for r in pc), sorted({r['praga'] for r in pc if r['praga'] not in GUIA + ['geral']}))
print('   coletados no filtro:', sorted((r['id_na_coleta'], r['termo']) for r in pc if r['id_na_coleta']))
print('   H05:', [(r['termo'], r['tipo_local'], r['intencao']) for r in L if r['id_na_coleta'] == 'H05'])
for p in ('condomínio', 'restaurante'):
    rs = f(publico=p)
    print(f'-- publico={p}:', len(rs), dict(C((r['tipo_local'], r['intencao']) for r in rs)), '| coletados', sorted(r['id_na_coleta'] for r in rs if r['id_na_coleta']))
print('-- urgência', len(f(intencao='urgência')), '| bairro', len(f(tipo_local='bairro')))
inf = f(intencao='informativa')
print('-- informativas', len(inf), '| coletadas', sorted(r['id_na_coleta'] for r in inf if r['id_na_coleta']), '| por praga', C(r['praga'] for r in inf).most_common())
print('   de praga sem guia:', [(r['praga'], r['termo']) for r in inf if r['praga'] not in GUIA + ['geral']])
print('   gerais:', [r['termo'] for r in inf if r['praga'] == 'geral'])
print('   nos seis guias:', sum(r['praga'] in GUIA for r in inf))
print('-- K06, K07, K09, K10 no mapa:', [(r['id_na_coleta'], r['termo'], r['praga'], r['tipo_local'], r['intencao'], r['publico']) for r in L if r['id_na_coleta'] in ('K06', 'K07', 'K09', 'K10')])
print('-- pombos sem K10: cidade + contratar =', len([r for r in f(praga='pombos', tipo_local='cidade', intencao='contratar') if r['id_na_coleta'] != 'K10']))

print('\n-- COBERTURA (união dos filtros da seção 3 e das informativas gerais da seção 4), mapa de hoje')
for reg in ('zona oeste', 'zona leste', 'zona norte', 'zona sul', 'centro de são paulo'):
    for n, ps in ((1, P5[:1]), (5, P5)):
        u = uniao(partes_cobertura(L, reg, ps))
        print(f'    região={reg!r}, {n} T3: {len(u)} de {len(L)} = {100 * len(u) / len(L):.2f}%')
print('   as cinco pragas de T3 importam? (zona oeste, todas as 6 escolhas de 5 entre os 6 guias):',
      sorted({len(uniao(partes_cobertura(L, 'zona oeste', list(c)))) for c in itertools.combinations(GUIA, 5)}))
print('   e cada escolha de 1 praga:', sorted({len(uniao(partes_cobertura(L, 'zona oeste', [p]))) for p in GUIA}))
pt = partes_cobertura(L, 'zona oeste', P5)
u5 = uniao(pt)
print('   soma simples dos filtros (com repetição):', sum(len(rs) for _, rs in pt), '| união:', len(u5))
rep = C(t for _, rs in pt for t in {r['termo'] for r in rs})
print('   termos em mais de um filtro:', [(t, [rot for rot, rs in pt if any(r['termo'] == t for r in rs)]) for t, n in rep.items() if n > 1])
melhor = {r['termo'] for r in conf if molde(r['termo']) == 'melhor'}
ini = {r['termo'] for r in f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral')}
print('   dentro da união, o plano NÃO tenta ranquear: "melhor"', len(melhor & u5), '+ início', len(ini & u5), '=', len((melhor | ini) & u5))
outros_conf = [r for r in conf if molde(r['termo']) != 'melhor']
print('   confiança fora "melhor":', len(outros_conf), dict(C(r['tipo_local'] for r in outros_conf)))
fora = [r for r in L if r['termo'] not in u5]
print('   SEM PÁGINA (5 T3, zona oeste):', len(fora), '| confere', len(u5) + len(fora), '=', len(L))
urg = [r for r in fora if r['intencao'] == 'urgência']
bai = [r for r in fora if r['intencao'] != 'urgência' and r['tipo_local'] == 'bairro']
out = [r for r in fora if r['intencao'] != 'urgência' and r['tipo_local'] != 'bairro']
print('      urgência', len(urg), '(todas as de urgência estão fora?', len(urg) == len(f(intencao='urgência')), ')')
print('      bairro, fora urgência', len(bai), dict(C(r['intencao'] for r in bai)))
print('      demais', len(out), '| por tipo_local', dict(C(r['tipo_local'] for r in out)))
print('         zona (regiões sem licenciada + sobra da região)', dict(C(r['local'] for r in out if r['tipo_local'] == 'zona')))
print('         zona oeste fora da união, fora urgência:', dict(C((r['intencao'], 'geral' if r['praga'] == 'geral' else 'praga T3' if r['praga'] in P5 else 'outra praga') for r in out if r['local'] == 'zona oeste')))
print('         quatro regiões sem licenciada:', sum(1 for r in out if r['tipo_local'] == 'zona' and r['local'] != 'zona oeste'))
print('         cidade', len([r for r in out if r['tipo_local'] == 'cidade']), dict(C((r['intencao'], r['publico'], 'sem guia' if r['praga'] not in GUIA + ['geral'] else 'geral' if r['praga'] == 'geral' else 'com guia') for r in out if r['tipo_local'] == 'cidade')))
print('         sem local', [(r['termo'], r['praga'], r['intencao']) for r in out if r['tipo_local'] == 'sem local'])
print('   bairro: total', len(f(tipo_local='bairro')), '| dentro da união (só confiança)', len([r for r in L if r['tipo_local'] == 'bairro' and r['termo'] in u5]),
      '| fora', len([r for r in fora if r['tipo_local'] == 'bairro']))
k10 = {r['termo'] for r in L if r['id_na_coleta'] == 'K10'}
print('   sem o K10 (classificação discutível): 5 T3', len(u5 - k10), '| 1 T3', len(uniao(partes_cobertura(L, 'zona oeste', P5[:1])) - k10),
      '| K10 está em que filtros:', [rot for rot, rs in pt if any(r['termo'] in k10 for r in rs)])
u1 = uniao(partes_cobertura(L, 'zona oeste', P5[:1]))
print('   coletados dentro da união (5 T3, zona oeste):', sum(1 for r in L if r['termo'] in u5 and r['situacao_na_coleta'] == 'coletado'), 'de', len(u5),
      '| (1 T3):', sum(1 for r in L if r['termo'] in u1 and r['situacao_na_coleta'] == 'coletado'), 'de', len(u1))

# ---------------------------------------------------------------- parte 2
print('\n' + '=' * 100)
print('PARTE 2 - A MESMA COBERTURA NAS VERSÕES ANTIGAS DO MAPA (git show; leitura)')
try:
    log = subprocess.run(['git', '-C', RAIZ, 'log', '--format=%h %ad', '--date=format:%d/%m/%Y %H:%M:%S', '--', 'data/palavras_chave.csv'],
                         capture_output=True, text=True).stdout.strip().splitlines()
    for ln in log:
        h = ln.split()[0]
        txt = subprocess.run(['git', '-C', RAIZ, 'show', h + ':data/palavras_chave.csv'], capture_output=True, text=True).stdout
        A = list(csv.DictReader(io.StringIO(txt)))
        fa = filtro(A)
        print(f'\n-- commit {ln}: {len(A)} linhas, {len({r["termo"] for r in A})} termos distintos | intencao {dict(C(r["intencao"] for r in A))}')
        regs = sorted({r['local'] for r in A if r['tipo_local'] == 'zona'})
        for reg in regs:
            pa = partes_cobertura(A, reg, P5)
            p1 = partes_cobertura(A, reg, P5[:1])
            print(f'     {reg!r}: 5 T3 união {len(uniao(pa))} | soma simples {sum(len(rs) for _, rs in pa)} | 1 T3 união {len(uniao(p1))}'
                  f' | 5 T3 sem H05 {len(uniao(pa, fora=("H05",)))} | sem informativas gerais {len(uniao(pa, fora=("informativas gerais",)))}'
                  f' | sem início {len(uniao(pa, fora=("início",)))}')
        pa = partes_cobertura(A, 'zona oeste', P5)
        print('     tamanho de cada filtro (zona oeste, 5 T3):', [(rot, len(rs)) for rot, rs in pa])
        rep = C(t for _, rs in pa for t in {r['termo'] for r in rs})
        print('     termos em mais de um filtro:', [(t, [rot for rot, rs in pa if any(r['termo'] == t for r in rs)]) for t, n in rep.items() if n > 1])
        # variantes que dariam 168: informativas todas (não só gerais e de guia); T3 com 6 pragas; público todo
        s = uniao(pa)
        v1 = s | {r['termo'] for r in fa(intencao='informativa')}
        v2 = uniao(partes_cobertura(A, 'zona oeste', GUIA))
        print(f'     variantes (zona oeste): com TODAS as informativas {len(v1)} | com 6 T3 {len(v2)} | 100*168/{len(A)} = {100 * 168 / len(A):.1f}% | 100*{len(s)}/{len(A)} = {100 * len(s) / len(A):.1f}%')
except Exception as e:
    print('git indisponível:', e)

# ---------------------------------------------------------------- parte 3
print('\n' + '=' * 100)
print('PARTE 3 - NÚMEROS DE BUSCA')
print(info('data/serp_sp.csv'))
S = list(csv.DictReader(open(os.path.join(RAIZ, 'data', 'serp_sp.csv'), encoding='utf-8')))
org = [r for r in S if r['superficie'] == 'orgânico']
ids = {}
for r in S:
    ids.setdefault(r['id'], r)
print('buscas', len(ids), '| por grupo', sorted(C(r['grupo'] for r in ids.values()).items()), '| datas', dict(C(r['data'] for r in ids.values())), '| logado', dict(C(r['logado'] for r in ids.values())))
for nome, sel in (('A a G', lambda r: r['grupo'] != 'H'), ('H', lambda r: r['grupo'] == 'H')):
    hs = sorted(r['hora_navegacao'] for r in ids.values() if sel(r))
    print(f'   grupos {nome}: {len(hs)} buscas, das {hs[0]} às {hs[-1]}')
print('   superfícies', dict(C(r['superficie'] for r in S)))

print('\n-- grupo H')
cls = {r['dominio']: r['classe'] for r in csv.DictReader(open(os.path.join(RAIZ, 'data', 'serp_dominios.csv'), encoding='utf-8'))}
for i in ['H%02d' % n for n in range(1, 11)]:
    rs = [r for r in S if r['id'] == i]
    o = sorted([r for r in rs if r['superficie'] == 'orgânico'], key=lambda r: int(r['posicao']))
    print(f"   {i} {rs[0]['termo']!r} | IA {rs[0]['visao_geral_ia']} | anúncios de texto {sum(r['superficie'] == 'anúncio' for r in rs)} | bloco {sum(r['superficie'].startswith('mapa (bloco') for r in rs)} | orgânicos {len(o)}")
    print('        1º a 3º:', [(r['posicao'], r['dominio'], r['caminho'][:45], cls.get(r['dominio'], 'sem classe no item 4')) for r in o[:3]])
conf3 = [r for r in org if r['id'] in ('H01', 'H02', 'H03')]
print('   H01+H02+H03: orgânicos', len(conf3), '| por classe do item 4:', C(cls.get(r['dominio'], 'sem classe (domínio novo)') for r in conf3).most_common())
print('   anúncios de texto: H01', sum(r['id'] == 'H01' and r['superficie'] == 'anúncio' for r in S), '| H02', sum(r['id'] == 'H02' and r['superficie'] == 'anúncio' for r in S), '| H03', sum(r['id'] == 'H03' and r['superficie'] == 'anúncio' for r in S))
for i in ('H04', 'H05', 'H10'):
    o = [r for r in org if r['id'] == i]
    print('   ', i, '1º:', [(r['dominio'], r['caminho']) for r in o if r['posicao'] == '1'], '| triider:', [r['posicao'] for r in o if r['dominio'] == 'triider.com.br'])
print('   informativas H06-H09, 1º resultado:', [(r['id'], r['dominio'], cls.get(r['dominio'], 'sem classe')) for r in org if r['id'] in ('H06', 'H07', 'H08', 'H09') and r['posicao'] == '1'])
print('   resumo de IA no grupo H:', dict(C(r['visao_geral_ia'] for r in ids.values() if r['grupo'] == 'H')))

print('\n-- grupo F')
F = [r for r in org if r['grupo'] == 'F']
print('   buscas', len({r['id'] for r in F}), '| resultados', len(F), '|', [(k, v, f'{100 * v / len(F):.1f}%') for k, v in C(r['tipo_pagina'] for r in F).most_common()])
print('-- escorpião')
E = [r for r in org if 'escorpi' in r['termo']]
print('   buscas', sorted({(r['id'], r['termo']) for r in E}), '| resultados', len(E), '| por tipo', dict(C(r['tipo_pagina'] for r in E)))
print('   domínios governo/universidade:', C(r['dominio'] for r in E if r['tipo_pagina'] == 'governo/universidade').most_common())
print('-- ratos, na amostra principal (B02): governo em', [(r['posicao'], r['dominio']) for r in org if r['id'] == 'B02' and r['tipo_pagina'] == 'governo/universidade'])
print('-- pombos, na amostra principal (B09):', [(r['posicao'], r['dominio'], r['tipo_pagina']) for r in org if r['id'] == 'B09'][:4])

print('\n-- cupim B04 e B04r (brutos)')
for arq in ('lote_02.jsonl', 'repeticao_01.jsonl'):
    for l in open(os.path.join(RAIZ, 'data', 'serp_raw', arq), encoding='utf-8'):
        try:
            o = json.loads(l)
        except Exception:
            continue
        if o.get('id') in ('B04', 'B04r'):
            print('   ', arq, o['id'], repr(o.get('q')), o.get('nv'))
            for x in o.get('pack', []):
                print('         ', x[:70], '| patrocinado' if x.startswith('Patrocinado') else '', '| tem cupim' if 'cupim' in x.lower() or 'cupins' in x.lower() else '')

print('\n-- ampliação (S2): CSV e brutos')
print(info('data/serp_sp_ampliacao.csv'))
S2 = list(csv.DictReader(open(os.path.join(RAIZ, 'data', 'serp_sp_ampliacao.csv'), encoding='utf-8')))
ids2 = {}
for r in S2:
    ids2.setdefault(r['id'], r)
hs = sorted(r['hora_navegacao'] for r in ids2.values())
print('   buscas', len(ids2), '| por grupo', sorted(C(r['grupo'] for r in ids2.values()).items()), '| datas', dict(C(r['data'] for r in ids2.values())), '| das', hs[0], 'às', hs[-1], '| logado', dict(C(r['logado'] for r in ids2.values())))
o2 = [r for r in S2 if r['superficie'] == 'orgânico']
for i in ('K06', 'K07', 'K09', 'K10'):
    o = sorted([r for r in o2 if r['id'] == i], key=lambda r: int(r['posicao']))
    print(f"   {i} {ids2[i]['termo']!r}: 1º a 3º {[(r['posicao'], r['dominio'], r['tipo_pagina']) for r in o[:3]]} | governo em {[(r['posicao'], r['dominio']) for r in o if r['tipo_pagina'] == 'governo/universidade']}")
K = {i: sorted([r for r in o2 if r['id'] == i], key=lambda r: int(r['posicao'])) for i in ids2 if ids2[i]['grupo'] == 'K'}
print('   grupo K: buscas', len(K), '| governo em 1º em', sorted(i for i, o in K.items() if o and o[0]['tipo_pagina'] == 'governo/universidade'),
      '| governo em qualquer posição em', sorted(i for i, o in K.items() if any(r['tipo_pagina'] == 'governo/universidade' for r in o)))
bruto = {}
for arq in sorted(glob.glob(os.path.join(RAIZ, 'data', 'serp_raw', 'ampliacao_0*.jsonl'))):
    for l in open(arq, encoding='utf-8'):
        try:
            o = json.loads(l)
        except Exception:
            continue
        bruto[o['id']] = (os.path.basename(arq), o)
print('   brutos: buscas', len(bruto), '| logado', dict(C(o['lg'] for _, o in bruto.values())))
for i in ('K06', 'K09', 'K10'):
    arq, o = bruto[i]
    print(f"   bruto {arq} {i} {o['q']!r} {o['nv']}: 1º orgânico = {o['org'][0].split(' | ')[0][:70]}")

# ---------------------------------------------------------------- parte 4
print('\n' + '=' * 100)
print('PARTE 4 - DEZ PÁGINAS, PLANILHA, PROTÓTIPO, CONTAS DE DIAS')
P = [json.loads(l) for l in open(os.path.join(RAIZ, 'data', 'paginas_top10.jsonl'), encoding='utf-8') if l.strip()]
print('paginas_top10.jsonl: páginas', len(P), '| com hq > 0:', sum(1 for p in P if p.get('hq', 0) > 0))
cab = next(csv.reader(open(os.path.join(RAIZ, 'data', 'medicao_modelo.csv'), encoding='utf-8')))
print('medicao_modelo.csv: colunas', len(cab))
for c in ('impressoes', 'cliques_na_busca', 'posicao_media', 'impressoes_em_ia', 'visitas_googlebot', 'visitas_bingbot', 'visitas_oai_searchbot', 'visitas_chatgpt_user', 'leads_toque_no_botao', 'leads_validos', 'orcamentos', 'servicos_fechados'):
    print(f'   {c}: {"existe" if c in cab else "NÃO EXISTE"}')
print('   colunas visitas_*:', [c for c in cab if c.startswith('visitas_')])
for rel in ('prototipo/zona-oeste/baratas/index.html', 'prototipo/para-empresas/restaurantes/index.html', 'prototipo/para-empresas/condominios/index.html'):
    p = os.path.join(RAIZ, rel)
    if os.path.exists(p):
        ls = open(p, encoding='utf-8').read().splitlines()
        print('  ', rel, '| existe |', len(ls), 'linhas | "[A ESCREVER]" nas linhas', [n for n, l in enumerate(ls, 1) if 'A ESCREVER' in l])
    else:
        print('  ', rel, '| NÃO EXISTE')
print('ritmo: 90/7 =', round(90 / 7, 2), 'semanas | 19 páginas:', round(19 / (90 / 7), 2), '| 23 páginas:', round(23 / (90 / 7), 2), 'por semana')
print('páginas: 7 + 6 + 1 + 1 + (1 a 5) + 1 + 2 =', 7 + 6 + 1 + 1 + 1 + 1 + 2, 'a', 7 + 6 + 1 + 1 + 5 + 1 + 2)
