#!/usr/bin/env python3
"""Verificação da reserva 1 — recalcula, a partir dos .jsonl e dos CSV, os números das seções 1, 3, 4, 5, 6, 7 e 11
de docs/mercado/serp_sp_ampliacao.md e os números do item 4 que o texto cita. Só leitura."""
import re, os, sys, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verif_reserva1_base import *

P = print
C = collections.Counter
tem_bloco = lambda o: any(not p.startswith('Patrocinado') for p in o['pack'])
tem_pat = lambda o: any(p.startswith('Patrocinado') for p in o['pack'])

P('=== SEÇÃO 3: camadas por grupo')
for g in 'IJK*':
    R = [o for o in RECS if g == '*' or GRUPO(o) == g]
    P(g, 'buscas', len(R), '| IA', sum(o['aio'] for o in R), pct(sum(o['aio'] for o in R), len(R)), '| bloco', sum(map(tem_bloco, R)), pct(sum(map(tem_bloco, R)), len(R)),
      '| anúncio', sum(1 for o in R if o['ads']), pct(sum(1 for o in R if o['ads']), len(R)), '| patrocinado', sum(map(tem_pat, R)), pct(sum(map(tem_pat, R)), len(R)),
      '| sem anúncio nenhum', sum(1 for o in R if not o['ads'] and not tem_pat(o)))
P('sem IA:', [o['q'] for o in RECS if not o['aio']])
P('sem bloco:', [(o['id'], o['q']) for o in RECS if not tem_bloco(o)])
P('patrocinado sem bloco orgânico?', [o['id'] for o in RECS if tem_pat(o) and not tem_bloco(o)])
P('aio=1 mas y.aio nulo, ou o contrário:', [o['id'] for o in RECS if bool(o['aio']) != (o['y'].get('aio') is not None)])
P('bloco x y.pack divergente:', [o['id'] for o in RECS if tem_bloco(o) != (o['y'].get('pack') is not None)], '| ads x y.ad:', [o['id'] for o in RECS if bool(o['ads']) != (o['y'].get('ad') is not None)])

P('\n--- item 4 (amostra principal, A a G), a partir de serp_sp.csv')
pri = [r for r in CSV_PRI if r['grupo'] != 'H']
bus = collections.defaultdict(list)
for r in pri:
    bus[r['id']].append(r)
P('buscas A-G', len(bus), '| linhas', len(pri), '| total com H', len(CSV_PRI), len({r['id'] for r in CSV_PRI}))
ia = sum(1 for rs in bus.values() if rs[0]['visao_geral_ia'] == 'sim')
bl = sum(1 for rs in bus.values() if any(r['superficie'] == 'mapa (bloco Empresas)' for r in rs))
ad = sum(1 for rs in bus.values() if any(r['superficie'] == 'anúncio' for r in rs))
pt = sum(1 for rs in bus.values() if any(r['superficie'] == 'mapa (patrocinado)' for r in rs))
sem = sum(1 for rs in bus.values() if not any(r['superficie'] in ('anúncio', 'mapa (patrocinado)') for r in rs))
P('IA', ia, pct(ia, 79), '| bloco', bl, pct(bl, 79), '| anúncio', ad, pct(ad, 79), '| patrocinado', pt, pct(pt, 79), '| sem anúncio nenhum', sem)
hp = sorted(r['hora_navegacao'] for r in pri)
P('janela A-G:', hp[0], hp[-1])
orgp = [r for r in pri if r['superficie'] == 'orgânico']
P('orgânicos A-G', len(orgp), '| domínios', len({r['dominio'] for r in orgp}))
for g in 'BDE':
    L = [r for r in orgp if r['grupo'] == g]
    c = C(r['tipo_pagina'] for r in L)
    P(' ', g, len(L), {k: pct(v, len(L)) for k, v in c.most_common()})

P('\n=== SEÇÃO 5.1: tipo de página por grupo (%)')
ordem_t = ['página interna por local', 'página interna (serviço/outro)', 'página inicial', 'blog/artigo', 'governo/universidade', 'rede social/fórum']
for g in 'IJK':
    L = [l for l in ORG if l['grupo'] == g]
    c = C(l['tipo'] for l in L)
    P(g, len(L), [(t, c[t], pct(c[t], len(L))) for t in ordem_t], '| soma %', sum(pct(c[t], len(L)) for t in ordem_t))
t3 = [l for l in ORG if l['pos'] <= 3]
P('top3 (', len(t3), '):', C(l['tipo'] for l in t3).most_common())
def todos3local(o):
    L = [l for l in ORG if l['id'] == o['id'] and l['pos'] <= 3]
    return len(L) == 3 and all(l['tipo'] == 'página interna por local' for l in L)
for g in ('I', 'J', 'K', 'IJ'):
    R = [o for o in RECS if GRUPO(o) in g]
    P('três primeiros todos por local, grupo', g, ':', sum(map(todos3local, R)), 'de', len(R))
# domínio com o nome exato do bairro
bairros = {'I01': 'brooklin', 'I02': 'morumbi', 'I03': 'saude', 'I04': 'campobelo', 'I05': 'interlagos', 'I06': 'capaoredondo', 'I07': 'vilaprudente',
           'I08': 'saomiguel', 'I09': 'sapopemba', 'I10': 'guaiana', 'I11': 'tucuruvi', 'I12': 'pirituba', 'I13': 'freguesia', 'I14': 'casaverde',
           'I15': 'vilamaria', 'I16': 'vilaleopoldina', 'I17': 'jaguare', 'I18': 'liberdade', 'I19': 'consolacao', 'I20': 'aclimacao'}
P('domínio com nome do bairro (grupo I):', [(l['id'], l['pos'], l['dominio']) for l in ORG if l['id'] in bairros and bairros[l['id']] in l['dominio'].replace('-', '')])
P('domínio com nome de bairro em J/K:', [(l['id'], l['pos'], l['dominio']) for l in ORG if l['grupo'] in 'JK' and any(b in l['dominio'].replace('-', '') for b in bairros.values())])

P('\n=== SEÇÃO 1 e 5.2: concentração')
dc = C(l['dominio'] for l in ORG)
P('orgânicos', len(ORG), '| domínios', len(dc))
P('mais frequentes (resultados, top3):', [(d, n, sum(1 for l in t3 if l['dominio'] == d)) for d, n in dc.most_common(12)])
P('1ª posição (40):', C(l['dominio'] for l in ORG if l['pos'] == 1).most_common())
I = [l for l in ORG if l['grupo'] == 'I']
dI = collections.defaultdict(set)
for l in I:
    dI[l['dominio']].add(l['id'])
P('grupo I: resultados', len(I), '| domínios', len(dI))
c5 = sorted(((len(v), d) for d, v in dI.items() if len(v) >= 5), reverse=True)
P('grupo I, domínios em 5+ buscas:', len(c5), c5)
P('grupo I, 1ª posição:', C(l['dominio'] for l in I if l['pos'] == 1).most_common())
# item 4: domínios nas buscas de bairro (grupo D) e os 13 em 5+
dD = collections.defaultdict(set)
for r in orgp:
    if r['grupo'] == 'D':
        dD[r['dominio']].add(r['id'])
d13 = {d for d, v in dD.items() if len(v) >= 5}
P('item 4, grupo D: domínios', len(dD), '| em 5+ buscas:', len(d13), sorted((len(dD[d]), d) for d in d13))
P('dos', len(c5), 'de I em 5+, quantos estão nos', len(d13), 'de D em 5+:', len({d for _, d in c5} & d13), sorted({d for _, d in c5} & d13))
P('dos', len(dI), 'domínios de I, já vistos no grupo D:', len(set(dI) & set(dD)))
dDE = {r['dominio'] for r in orgp if r['grupo'] in 'DE'}
P('  ... já vistos em D ou E:', len(set(dI) & dDE), '| já vistos em A-G:', len(set(dI) & {r['dominio'] for r in orgp}), '| já vistos em A-H:', len(set(dI) & {r['dominio'] for r in CSV_PRI if r['superficie'] == 'orgânico'}))
top10p = C(r['dominio'] for r in orgp).most_common(10)
P('10 mais frequentes da amostra principal -> resultados aqui:', [(d, dc.get(d, 0)) for d, _ in top10p])
K = [l for l in ORG if l['grupo'] == 'K']
dK = C(l['dominio'] for l in K)
P('grupo K: resultados', len(K), 'domínios', len(dK), '| mais frequentes:', dK.most_common(4))
P('uniprag em K, tipos:', C(l['tipo'] for l in K if l['dominio'] == 'uniprag.com.br'), [l['caminho'] for l in K if l['dominio'] == 'uniprag.com.br'])
# domínios novos
ant89 = {r['dominio'] for r in CSV_PRI if r['superficie'] == 'orgânico'}
novos = [d for d in dc if d not in ant89]
P('domínios novos (fora das 89 buscas):', len(novos), 'de', len(dc), '| resultados', sum(dc[d] for d in novos), pct(sum(dc[d] for d in novos), len(ORG)))
nK = [d for d in dK if d not in ant89]
P('  em K:', len(nK), 'de', len(dK), '| resultados', sum(dK[d] for d in nK), pct(sum(dK[d] for d in nK), len(K)))
P('  novos:', sorted(novos))
P('distintos no orgânico nas 129 buscas:', len(ant89 | set(dc)), '(item 4, 89 buscas:', len(ant89), ')')
perf89 = {r['titulo_ou_nome'] for r in CSV_PRI if r['superficie'] == 'mapa (bloco Empresas)'}
perfAG = {r['titulo_ou_nome'] for r in pri if r['superficie'] == 'mapa (bloco Empresas)'}
MAPA = [(o['id'], GRUPO(o), n, nota, av) for o in RECS for n, nota, av in pack_de(o)[0]]
perfN = {m[2] for m in MAPA}
P('perfis distintos no bloco nas 129 buscas:', len(perf89 | perfN), '| só A-G + ampliação:', len(perfAG | perfN), '| item 4 (89):', len(perf89), '(A-G:', len(perfAG), ')')
# governo
gov = [l for l in ORG if l['tipo'] == 'governo/universidade']
P('governo:', len(gov), 'resultados em', len({l['id'] for l in gov}), 'buscas:', [(l['id'], CONS[l['id']]['termo'], l['pos'], l['dominio']) for l in gov])
P('  em K:', len({l['id'] for l in gov if l['grupo'] == 'K'}), 'de 10 buscas | 1º em:', [l['id'] for l in gov if l['pos'] == 1])
P('ohub:', sorted({l['id'] for l in ORG if l['dominio'] == 'ohub.com.br'}))
outros_dir = ('triider', 'reclameaqui', 'coteibem', 'pedegas', 'pestwase', 'listazn', 'getninjas', 'habitissimo', 'cronoshare', 'guiamais', 'apontador', 'telelistas')
P('outros marketplaces/diretórios:', [(l['id'], l['dominio']) for l in ORG if any(x in l['dominio'] for x in outros_dir)])
P('diretório por classe do item 4:', [(l['id'], l['dominio']) for l in ORG if DOMS.get(l['dominio'], {}).get('classe', '').startswith('diret')])

P('\n=== SEÇÃO 5.3: classe')
P('classes existentes em serp_dominios.csv:', C(r['classe'] for r in DOMS.values()))
def classe(l):
    if l['dominio'] in DOMS:
        return DOMS[l['dominio']]['classe'] or 'não lido (item 4)'
    if l['tipo'] == 'governo/universidade':
        return 'governo (domínio novo)'
    if l['tipo'] == 'rede social/fórum':
        return 'rede social (domínio novo)'
    return 'novo, não lido'
for nome, L in (('todos', ORG), ('top3', t3), ('1ª', [l for l in ORG if l['pos'] == 1]), ('1ª grupo I', [l for l in I if l['pos'] == 1])):
    P(nome, len(L), C(classe(l) for l in L).most_common())
P('1ª posição, domínio e classe:', [(l['id'], l['dominio'], classe(l)) for l in ORG if l['pos'] == 1])
P('domínios vistos aqui que não estão em serp_dominios.csv mas estão nas 89 (grupo H):', sorted({l['dominio'] for l in ORG if l['dominio'] not in DOMS and l['dominio'] in ant89}))
P('domínios novos por tipo:', C(l['tipo'] for l in ORG if l['dominio'] not in ant89))
# item 4: 1ª posição por classe
p1 = [r for r in orgp if r['posicao'] == '1']
P('item 4: 1ª posição com licença:', sum(1 for r in p1 if DOMS.get(r['dominio'], {}).get('classe') == 'empresa_com_numero_de_licenca'), 'de', len(p1))

P('\n=== SEÇÃO 4: posição vertical')
nm = {'aio': 'IA', 'ad': 'anúncio', 'pack': 'mapa', 'org': 'orgânico'}
def ordem(y):
    return ' > '.join(nm[k] for v, k in sorted((v, k) for k, v in y.items() if k in nm and v is not None))
P('ordens:', C(ordem(o['y']) for o in RECS).most_common())
P('empates de posição dentro da mesma busca:', [(o['id'], o['y']) for o in RECS if len({v for k, v in o['y'].items() if k in nm and v is not None}) < sum(1 for k, v in o['y'].items() if k in nm and v is not None)])
P('valores 0 ou negativos (elemento oculto?):', [(o['id'], o['y']) for o in RECS if any(v is not None and v <= 0 for k, v in o['y'].items() if k in nm)])
for g in 'IJK*':
    R = [o for o in RECS if g == '*' or GRUPO(o) == g]
    P('grupo', g, len(R), 'buscas')
    P('  ordens:', C(ordem(o['y']) for o in R).most_common())
    P('  1ª camada:', C(ordem(o['y']).split(' > ')[0] for o in R).most_common())
    for k in ('aio', 'pack', 'org', 'ad'):
        v = [o['y'][k] for o in R if o['y'].get(k) is not None]
        if v:
            P(f'  {nm[k]}: n={len(v)} mediana={statistics.median(v)} mín={min(v)} máx={max(v)} | <945: {sum(1 for x in v if x < 945)} | >=945: {sum(1 for x in v if x >= 945)} | >=1890: {sum(1 for x in v if x >= 1890)}')
    y = [o['y'] for o in R]
    P('  mapa antes do orgânico:', sum(1 for a in y if a.get('pack') is not None and a['pack'] < a['org']), 'de', sum(1 for a in y if a.get('pack') is not None),
      '| anúncio depois do orgânico:', sum(1 for a in y if a.get('ad') is not None and a['ad'] > a['org']), 'de', sum(1 for a in y if a.get('ad') is not None),
      '| IA é 1ª camada:', sum(1 for o in R if ordem(o['y']).startswith('IA')), 'de', sum(o['aio'] for o in R),
      '| orgânico antes do mapa:', sum(1 for a in y if a.get('pack') is not None and a['org'] < a['pack']))
P('valores distintos de y.org:', sorted(C(o['y']['org'] for o in RECS).items()))
P('valores distintos de y.aio:', sorted(C(o['y'].get('aio') for o in RECS if o['y'].get('aio') is not None).items()))
P('valores distintos de y.pack:', sorted(C(o['y'].get('pack') for o in RECS if o['y'].get('pack') is not None).items()))

P('\n=== SEÇÃO 6: bloco de mapa')
pc = C(m[2] for m in MAPA)
P('linhas', len(MAPA), '| perfis distintos', len(pc), '| buscas com bloco', len({m[0] for m in MAPA}), '| novos (fora de A-G):', sum(1 for p in pc if p not in perfAG), '| novos (fora de A-H):', sum(1 for p in pc if p not in perf89))
P('mais frequentes:', pc.most_common(6))
MI = [m for m in MAPA if m[1] == 'I']
pI = {m[2] for m in MI}
perfD = {r['titulo_ou_nome'] for r in pri if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] == 'D'}
perfDE = {r['titulo_ou_nome'] for r in pri if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] in 'DE'}
P('grupo I: buscas com bloco', len({m[0] for m in MI}), '| linhas', len(MI), '| perfis distintos', len(pI), '| já vistos em D:', len(pI & perfD), '| em D ou E:', len(pI & perfDE), '| em A-G:', len(pI & perfAG))
P('item 4, grupo D: perfis distintos', len(perfD))
notas = [float(m[3].replace(',', '.')) for m in MAPA if m[3]]
P('nota: lidas', len(notas), 'de', len(MAPA), '| mediana', statistics.median(notas), 'mín', min(notas), '| >=4,8:', sum(1 for n in notas if n >= 4.8), pct(sum(1 for n in notas if n >= 4.8), len(notas)))
P('linha sem nota:', [m for m in MAPA if not m[3]])
av = {}
for m in MAPA:
    if m[4].isdigit():
        av[m[2]] = int(m[4])
P('avaliações por perfil: lidos', len(av), 'mediana', statistics.median(av.values()), 'mín', min(av.values()), 'máx', max(av.values()))
avI = {m[2]: int(m[4]) for m in MI if m[4].isdigit()}
P('  só grupo I: lidos', len(avI), 'mediana', statistics.median(avI.values()))
avN = {p: v for p, v in av.items() if p not in perfAG}
avV = {p: v for p, v in av.items() if p in perfAG}
P('  perfis novos (fora de A-G): n', len(avN), 'mediana', statistics.median(avN.values()), '| perfis já vistos: n', len(avV), 'mediana', statistics.median(avV.values()))
avp = {}
for r in pri:
    if r['superficie'] == 'mapa (bloco Empresas)' and r['avaliacoes'].isdigit():
        avp[r['titulo_ou_nome']] = int(r['avaliacoes'])
P('  item 4 (A-G): lidos', len(avp), 'mediana', statistics.median(avp.values()), 'máx', max(avp.values()))
P('perfil com mais de um valor de avaliações na ampliação:', [(p, sorted({m[4] for m in MAPA if m[2] == p})) for p in pc if len({m[4] for m in MAPA if m[2] == p}) > 1])
P('nome de perfil com cara de diretório:', [p for p in pc if re.search(r'ohub|triider|getninjas|guia|lista', p, re.I)])

P('\n=== SEÇÃO 7: anúncios')
ads = [(o['id'], h if (h and h != 'google.com') else 'não identificado') for o in RECS for h in o['ads']]
ac = C(h for _, h in ads)
P('anúncios', len(ads), 'em', len({i for i, _ in ads}), 'buscas |', ac.most_common())
P('buscas com brasiltechs.com:', len({i for i, h in ads if h == 'brasiltechs.com'}), '| valores brutos distintos dos não identificados:', C(h for o in RECS for h in o['ads'] if not h or h == 'google.com'))
pat = [(o['id'], n) for o in RECS for n, _, _ in pack_de(o)[1]]
P('perfil patrocinado:', len(pat), 'linhas em', len({i for i, _ in pat}), 'buscas |', C(n for _, n in pat))
P('item 4, patrocinado:', C(r['titulo_ou_nome'] for r in pri if r['superficie'] == 'mapa (patrocinado)'))
ap = collections.defaultdict(set)
for r in pri:
    if r['superficie'] == 'anúncio':
        ap[r['dominio']].add(r['id'])
P('item 4, brasiltechs em buscas:', len(ap['brasiltechs.com']), 'de 79')

P('\n=== SEÇÃO 11: repetições')
por = {o['id']: o for o in RECS}
for r in REP:
    a = por[r['id'][:-1]]
    da, dr = [l['dominio'] for l in org_de(a)], [l['dominio'] for l in org_de(r)]
    ua, ur = [x.split(' | ')[0] for x in a['org']], [x.split(' | ')[0] for x in r['org']]
    pa, pr = [n for n, _, _ in pack_de(a)[0]], [n for n, _, _ in pack_de(r)[0]]
    P(r['id'], '|', r['q'] == a['q'], '| 1ª', a['nv'][:5], '2ª', r['nv'][:5], '| minutos depois:', round((seg(r['nv']) - seg(a['nv'])) / 60, 1),
      '| mesmo 1º:', da[0] == dr[0], '| n domínios', len(da), len(dr), '| mesma ordem de domínios:', da == dr, '| mesmas URLs na ordem:', ua == ur,
      '| perfis em comum:', len(set(pa) & set(pr)), 'de', len(pa), '(mesma ordem:', pa == pr, ') | local:', repr(a['loc']), repr(r['loc']),
      '| anúncios', len(a['ads']), '->', len(r['ads']), '| patrocinado', len(pack_de(a)[1]), '->', len(pack_de(r)[1]), '| y 1ª', a['y'], '| y 2ª', r['y'],
      '| ordem', ordem(a['y']), '->', ordem(r['y']), '| aio', a['aio'], r['aio'], '| lg', r['lg'])
