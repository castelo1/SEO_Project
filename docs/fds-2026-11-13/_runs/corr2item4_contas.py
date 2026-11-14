#!/usr/bin/env python3
"""Corretor da segunda passada do item 4 — recalcula, SÓ LEITURA, os números que entram em
/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md por conta dos achados de verificacao2_item4.md.
Não grava nada. Biblioteca padrão. Uso: python3 -B corr2item4_contas.py
Fonte: data/serp_raw/lote_*.jsonl e repeticao_01.jsonl (brutos), data/serp_dominios.csv,
data/serp_dominios_classe_parte{1,2}.csv, data/palavras_chave.csv, data/serp_sp.csv (só para o achado 11)."""
import csv, glob, json, os, re, statistics, unicodedata, collections

RAIZ = '/home/ancastelo/pessoal/SEO_Project'
DATA = os.path.join(RAIZ, 'data'); RAW = os.path.join(DATA, 'serp_raw')


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


def seg(h):
    a, b, c = h.split(':'); return int(a) * 3600 + int(b) * 60 + int(c)


recs = []
for f in sorted(glob.glob(os.path.join(RAW, 'lote_*.jsonl'))):
    for n, l in enumerate(open(f, encoding='utf-8'), 1):
        o = json.loads(l); o['arq'] = os.path.basename(f); o['lin'] = n; recs.append(o)
AG = [o for o in recs if o['id'][0] != 'H']; H = [o for o in recs if o['id'][0] == 'H']
print('registros', len(recs), '| A a G', len(AG), '| H', len(H))


def org(o):
    out = []
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | '); host, _, path = u.partition('/')
        out.append((i, host, '/' + path, t.strip()))
    return out


# mesma regra de data/serp_raw/monta_csv.py (copiada para não importar nem executar o script do projeto)
LOCAIS = ['zona-leste', 'zona-norte', 'zona-oeste', 'zona-sul', 'centro', 'moema', 'pinheiros', 'vila-mariana', 'tatuape', 'santana',
          'lapa', 'itaim-bibi', 'santo-amaro', 'mooca', 'perdizes', 'santa-cecilia', 'higienopolis', 'butanta', 'ipiranga', 'penha',
          'jabaquara', 'itaquera', 'campo-limpo', 'bela-vista', 'vila-madalena', 'osasco', 'jardim-paulista', 'barra-funda',
          'analia-franco']
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'tiktok.com', 'linkedin.com')


def tipo(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'governo'
    if host in SOCIAL: return 'social'
    if p in ('', '/'): return 'inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog'
    if any(l in p for l in LOCAIS): return 'local'
    return 'servico'


RE_PACK = re.compile(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)')   # a expressão de monta_csv.py


def pack(o):
    out = []
    for i, s in enumerate(o['pack']):
        pat = s.startswith('Patrocinado '); nome = s[len('Patrocinado '):] if pat else s
        m = RE_PACK.search(nome)
        out.append(dict(pat=pat, nome=(m.group(1) if m else nome).strip(), nota=m.group(2) if m else '',
                        aval=m.group(3).replace('.', '') if m else '', bruto=s, idx=i))
    return out


print('\n== ACHADO 1: rótulo de local ==')
compack = [o for o in AG if any(not p['pat'] for p in pack(o))]
print('buscas com bloco', len(compack), '| com rótulo de local', sum(1 for o in AG if o['loc']),
      '| rótulo e bloco', sum(1 for o in compack if o['loc']), '| rótulo sem bloco', sum(1 for o in AG if o['loc'] and o not in compack))
print('rótulos:', collections.Counter(o['loc'] or 'nenhum' for o in AG))
def tem_cidade(q):
    q = sem_acento(q); return 'sao paulo' in q or re.search(r'\bsp\b', q) is not None
sp = [o for o in AG if o['loc'] == 'São Paulo, SP']; os_ = [o for o in AG if o['loc'] == 'Osasco, SP']
print('"São Paulo, SP":', len(sp), '| com cidade no termo', sum(tem_cidade(o['q']) for o in sp))
print('"Osasco, SP":', len(os_), '| com cidade no termo', sum(tem_cidade(o['q']) for o in os_), '| sem', sum(not tem_cidade(o['q']) for o in os_))
for o in os_: print('   ', o['id'], o['q'])
print('buscas com cidade no termo:', sum(tem_cidade(o['q']) for o in AG), '| delas com bloco', sum(1 for o in compack if tem_cidade(o['q'])),
      '| com bloco e sem rótulo', [(o['id'], o['q']) for o in compack if tem_cidade(o['q']) and not o['loc']])
print('buscas sem cidade no termo, com bloco:', sum(1 for o in compack if not tem_cidade(o['q'])),
      '| rótulos nelas:', collections.Counter(o['loc'] or 'nenhum' for o in compack if not tem_cidade(o['q'])))

print('\n== ACHADOS 2, 11, 17: bloco de mapa ==')
linhas = [(o, p) for o in AG for p in pack(o) if not p['pat']]
print('linhas', len(linhas), '| com nota e número lidos', sum(1 for _, p in linhas if p['nota']))
for o, p in linhas:
    if not p['nota']: print('   NÃO LIDA:', o['id'], o['arq'], 'linha', o['lin'], 'pack[%d]' % p['idx'], '|', len(p['bruto']), 'caracteres |', repr(p['bruto']))
notas = [float(p['nota'].replace(',', '.')) for _, p in linhas if p['nota']]
print('nota: mediana', statistics.median(notas), 'mínima', min(notas), '| >= 4,8:', sum(n >= 4.8 for n in notas), 'de', len(notas),
      '= %.1f%%' % (100 * sum(n >= 4.8 for n in notas) / len(notas)), '| sobre 202: %.1f%%' % (100 * sum(n >= 4.8 for n in notas) / len(linhas)))
por = collections.defaultdict(list)
for _, p in linhas:
    if p['aval']: por[p['nome']].append(int(p['aval']))
av = sorted(statistics.median(v) for v in por.values())
q = statistics.quantiles(av, n=4)
print('perfis com número', len(av), '| mediana', statistics.median(av), '| quartis', q, '| mínimo', min(av), 'máximo', max(av),
      '| até 42:', sum(a <= 42 for a in av), '| mais de 313:', sum(a > 313 for a in av), '| menos de 10:', sum(a < 10 for a in av))
pat = [o for o in AG if any(p['pat'] for p in pack(o))]
print('patrocinado em', len(pat), 'buscas | todas com bloco?', all(o in compack for o in pat), '| %.0f%% de %d' % (100 * len(pat) / len(compack), len(compack)))
print('tamanho do bloco (perfis não patrocinados):', collections.Counter(sum(1 for p in pack(o) if not p['pat']) for o in compack))

print('\n== ACHADO 3: domínios com página de local ==')
dom_local = collections.defaultdict(int); dom_all = collections.Counter()
for o in AG:
    for i, h, p, t in org(o):
        dom_all[h] += 1
        if tipo(h, p) == 'local': dom_local[h] += 1
print('domínios', len(dom_all), '| resultados', sum(dom_all.values()), '| páginas por local', sum(dom_local.values()), '| domínios com página por local', len(dom_local))
dcsv = {r['dominio']: r for r in csv.DictReader(open(os.path.join(DATA, 'serp_dominios.csv'), encoding='utf-8'))}
print('   desses, por classe:', collections.Counter(dcsv[d]['classe'] for d in dom_local))
cls = {}
for f in ('serp_dominios_classe_parte1.csv', 'serp_dominios_classe_parte2.csv'):
    for r in csv.DictReader(open(os.path.join(DATA, f), encoding='utf-8')): cls[r['dominio'].strip()] = r
SERV = ('empresa_identificada_sem_numero_de_licenca', 'empresa_com_numero_de_licenca', 'marca_sem_identificacao_vista', 'rede_ou_dominio_satelite')
serv = [d for d in dcsv if dcsv[d]['classe'] in SERV]
sim = lambda d, c: cls[d][c].strip().lower() == 'sim'
print('sites de serviço lidos', len(serv), '| páginas por localidade', sum(sim(d, 'paginas_por_bairro') for d in serv),
      '| WhatsApp', sum(sim(d, 'botao_whatsapp') for d in serv), '| número de licença', sum(sim(d, 'licenca_exibida') for d in serv))

print('\n== ACHADO 6: só entre os primeiros colocados ==')
for nome, corte in (('1ª posição', 1), ('três primeiros', 3)):
    ds = {h for o in AG for i, h, p, t in org(o) if i <= corte}
    s = [d for d in ds if d in serv]
    print(f'{nome}: {len(ds)} domínios | por classe {dict(collections.Counter(dcsv[d]["classe"] for d in ds))}')
    print(f'   sites de serviço lidos {len(s)} | localidade {sum(sim(d, "paginas_por_bairro") for d in s)} | WhatsApp {sum(sim(d, "botao_whatsapp") for d in s)} | licença {sum(sim(d, "licenca_exibida") for d in s)}')
    print('   sem páginas por localidade:', sorted(d for d in s if not sim(d, 'paginas_por_bairro')))
    print('   com número de licença:', sorted(d for d in s if sim(d, 'licenca_exibida')))
    # ponderado por resultado (cada resultado conta)
    res = [(h) for o in AG for i, h, p, t in org(o) if i <= corte]
    rs = [h for h in res if h in serv]
    print(f'   por resultado: {len(res)} resultados, {len(rs)} de sites de serviço lidos | localidade {sum(sim(h, "paginas_por_bairro") for h in rs)} | WhatsApp {sum(sim(h, "botao_whatsapp") for h in rs)} | licença {sum(sim(h, "licenca_exibida") for h in rs)}')
for a, b in ((15, 19), (50, 67), (33, 44), (5, 19), (12, 67), (9, 44)): print('   %d/%d = %.1f%%' % (a, b, 100 * a / b))

print('\n== ACHADO 7: cupimax e ratomax ==')
for d in ('cupimax.com.br', 'ratomax.com.br'):
    r = dcsv[d]; print('  ', d, r['resultados_organicos'], 'resultados |', r['vezes_no_top3'], 'entre os três primeiros | classe', r['classe'],
                       '| 1ª posição', sum(1 for o in AG for i, h, p, t in org(o) if i == 1 and h == d))
for c in ('rede_ou_dominio_satelite', 'marca_sem_identificacao_vista'):
    ds = [d for d in dcsv if dcsv[d]['classe'] == c]
    print('  ', c, len(ds), 'domínios', sum(int(dcsv[d]['resultados_organicos']) for d in ds), 'resultados', sum(int(dcsv[d]['vezes_no_top3']) for d in ds), 'top3')

print('\n== ACHADO 8: domínios não lidos com cara de lista ou guia ==')
ALVO = ('comerciosaopaulo.com.br', 'znimovel.com.br', 'encontrasantacecilia.com.br', 'catalogohospitalar.com.br', 'g1.globo.com',
        'coteibem.com.br', 'listazn.com.br', 'pestwase.com', 'triider.com.br', 'reclameaqui.com.br', 'pedegas.com', 'ohub.com.br')
for o in AG:
    for i, h, p, t in org(o):
        if h in ALVO and h != 'ohub.com.br': print('  ', o['id'], 'posição', i, h, p, '|', t, '| classe', dcsv[h]['classe'])
dire = sum(int(r['resultados_organicos']) for r in dcsv.values() if r['classe'] == 'diretorio_marketplace')
extra = sum(dom_all[d] for d in ('coteibem.com.br', 'listazn.com.br', 'comerciosaopaulo.com.br', 'znimovel.com.br', 'encontrasantacecilia.com.br', 'catalogohospitalar.com.br'))
print('   diretório (classe lida):', dire, '= %.1f%%' % (100 * dire / 709), '| com os 6 não lidos:', dire + extra, '= %.1f%%' % (100 * (dire + extra) / 709))

print('\n== ACHADO 10: termos informativos ==')
pk = list(csv.DictReader(open(os.path.join(DATA, 'palavras_chave.csv'), encoding='utf-8')))
inf = [r for r in pk if r['intencao'].startswith('informa')]
print('termos', len(pk), '| informativos', len(inf), '| por origem', collections.Counter(r['origem_do_termo'] for r in inf),
      '| ids da coleta', [r['id_na_coleta'] for r in inf if r['id_na_coleta']], '| tipo_local', collections.Counter(r['tipo_local'] for r in inf))
print('por tipo de local:', collections.Counter(r['tipo_local'] for r in pk))
print('por intenção:', collections.Counter(r['intencao'] for r in pk))
print('por origem:', collections.Counter(r['origem_do_termo'] for r in pk))

print('\n== ACHADO 11: linhas do CSV com o nome contaminado ==')
with open(os.path.join(DATA, 'serp_sp.csv'), encoding='utf-8', newline='') as fh:
    for n, row in enumerate(csv.reader(fh), 1):
        if n > 1 and row[8].startswith('mapa') and (not row[13] or re.search(r'\d,\d', row[12])):
            print('   CSV linha', n, '|', row[0], '| superfície', row[8], '| posição', row[9], '| nome', repr(row[12]), '| nota', repr(row[13]), '| aval', repr(row[14]))
RE_NOVA = re.compile(r'^(.*?)\s(\d,\d)(?:\(([^)]*)\)?)?')   # troca proposta: nota obrigatória, número entre parênteses opcional
for o, p in linhas:
    if not p['nota']:
        m = RE_NOVA.search(p['bruto'])
        print('   com a expressão proposta:', o['id'], '->', (m.group(1), m.group(2), m.group(3)) if m else 'sem casamento (nome fica inteiro)')
# a expressão proposta não pode mudar nenhuma das linhas hoje lidas
dif = 0
for o in recs:
    for p in pack(o):
        if p['nota']:
            nome = p['bruto'][len('Patrocinado '):] if p['pat'] else p['bruto']
            m = RE_NOVA.search(nome); g3 = (m.group(3) or '')
            av = g3.replace('.', '') if re.fullmatch(r'\d[\d.]*', g3) else ''
            if (m.group(1).strip(), m.group(2), av) != (p['nome'], p['nota'], p['aval']): dif += 1
print('   linhas hoje lidas que mudariam com a expressão proposta:', dif, '(nos 89 registros, patrocinados incluídos)')

print('\n== ACHADO 12: repetição e bairro ==')
rep = [json.loads(l) for l in open(os.path.join(RAW, 'repeticao_01.jsonl'), encoding='utf-8')]
byid = {o['id']: o for o in recs}
for r in rep:
    rid = r.get('id') or r.get('rid'); base = byid.get(rid[:3]) if rid else None
    print('  ', rid, r['nv'], '| 1ª vez', base['nv'] if base else '?', '| %.2f h' % ((seg(r['nv']) - seg(base['nv'])) / 3600) if base else '')
for g in ('D', 'E', 'DE'):
    rs = [(h, p) for o in AG if o['id'][0] in g for i, h, p, t in org(o)]
    loc = sum(tipo(h, p) == 'local' for h, p in rs)
    print('   grupo', g, ':', sum(1 for o in AG if o['id'][0] in g), 'buscas |', loc, 'de', len(rs), '= %.1f%%' % (100 * loc / len(rs)))
tres = [o for o in AG if o['id'][0] in 'DE' and all(tipo(h, p) == 'local' for i, h, p, t in org(o) if i <= 3)]
print('   buscas D+E com os três primeiros por local:', len(tres), 'de', sum(1 for o in AG if o['id'][0] in 'DE'),
      '| só D:', sum(1 for o in tres if o['id'][0] == 'D'), '| só E:', sum(1 for o in tres if o['id'][0] == 'E'))

print('\n== ACHADO 13: pausas ==')
ordem = sorted(AG, key=lambda o: seg(o['nv']))
print('   primeira', ordem[0]['id'], ordem[0]['nv'], '| última', ordem[-1]['id'], ordem[-1]['nv'], 'lida às', ordem[-1]['t'])
for a, b in zip(ordem, ordem[1:]):
    d = seg(b['nv']) - seg(a['nv'])
    if d >= 60 or d < 20: print('   %s (%s) -> %s (%s): %d s' % (a['id'], a['nv'], b['id'], b['nv'], d))
ivs = [seg(b['nv']) - seg(a['nv']) for a, b in zip(ordem, ordem[1:])]
print('   intervalos', len(ivs), '| mediana', statistics.median(ivs), '| mínimo', min(ivs), '| máximo', max(ivs))
print('   H01', byid['H01']['nv'], '| minutos entre 20:26 e 21:16:', (seg('21:16:00') - seg(ordem[0]['nv'])) / 60)

print('\n== ACHADO 19: grupo H, buscas de confiança ==')
for i in ('H01', 'H02', 'H03'):
    o = byid[i]; print('  ', i, '| anúncios', len(o['ads']), '| orgânicos', len(o['org']), '| 1º', org(o)[0][1], dcsv.get(org(o)[0][1], {}).get('classe', 'domínio novo'))
c = collections.Counter()
for i in ('H01', 'H02', 'H03'):
    for pos, h, p, t in org(byid[i]):
        k = dcsv[h]['classe'] if h in dcsv else ('governo_universidade' if h.endswith('.gov.br') or h == 'gov.br' else ('rede_social_forum' if h in SOCIAL else 'domínio novo, não lido'))
        c[k] += 1
print('   28 resultados por classe:', dict(c))
print('   dedetizadoras já classificadas (4 classes de serviço):', sum(v for k, v in c.items() if k in SERV))
