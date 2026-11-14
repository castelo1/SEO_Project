#!/usr/bin/env python3
"""Segunda passada da reserva 1 — recalcula os números do documento a partir do BRUTO (jsonl) e, em paralelo, do CSV. Só leitura."""
import sys, os, re, collections, statistics
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2res1_comum import *
C = collections.Counter
P = print

# ---- regra de tipo de página, reescrita a partir da descrição (lista de locais copiada do script, conferida à parte) ----
LOCAIS = ['zona-leste', 'zona-norte', 'zona-oeste', 'zona-sul', 'centro', 'moema', 'pinheiros', 'vila-mariana', 'tatuape', 'santana', 'lapa',
          'itaim-bibi', 'santo-amaro', 'mooca', 'perdizes', 'santa-cecilia', 'higienopolis', 'butanta', 'ipiranga', 'penha', 'jabaquara',
          'itaquera', 'campo-limpo', 'bela-vista', 'vila-madalena', 'osasco', 'jardim-paulista', 'barra-funda', 'analia-franco',
          'brooklin', 'morumbi', 'saude', 'campo-belo', 'campo_belo', 'interlagos', 'capao-redondo', 'vila-prudente', 'sao-miguel',
          'sapopemba', 'guaianases', 'guaianazes', 'tucuruvi', 'pirituba', 'freguesia', 'casa-verde', 'vila-maria', 'vila-leopoldina',
          'jaguare', 'liberdade', 'consolacao', 'aclimacao']
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'tiktok.com', 'linkedin.com')
def tipo(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'gov'
    if host in SOCIAL: return 'social'
    if p in ('', '/'): return 'inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog'
    if any(l in p for l in LOCAIS): return 'local'
    return 'servico'
MAPA_TIPO = {'governo/universidade': 'gov', 'rede social/fórum': 'social', 'página inicial': 'inicial', 'blog/artigo': 'blog',
             'página interna por local': 'local', 'página interna (serviço/outro)': 'servico'}

# ---- orgânico a partir do bruto ----
ORG = []   # dict(id, grupo, pos, dom, path, tit, tipo)
for o in BRUTO:
    for pos, host, path, t in org_do_bruto(o):
        ORG.append(dict(id=o['id'], g=GRUPO[o['id']], pos=pos, dom=host, path=path, tit=t, tipo=tipo(host, path)))
# o tipo do CSV bate com o meu?
csv_org = [r for r in CSVA if r['superficie'] == 'orgânico']
dif = [(a['id'], a['pos'], a['tipo'], b['tipo_pagina']) for a, b in zip(ORG, csv_org) if a['tipo'] != MAPA_TIPO[b['tipo_pagina']]]
P('tipo de página: bruto x CSV divergentes:', dif)
P('linhas CSV por superfície:', C(r['superficie'] for r in CSVA), 'total', len(CSVA))

def grupo(g): return [x for x in ORG if g == '*' or x['g'] == g]
def buscas(g): return [o for o in BRUTO if g == '*' or GRUPO[o['id']] == g]

P('\n== cabeçalho ==')
P('orgânicos', len(ORG), '| por grupo', C(x['g'] for x in ORG))
# item 4
P('item 4: buscas A-G', len({r['id'] for r in CSV4 if r['grupo'] != 'H'}), '| todas', len({r['id'] for r in CSV4}),
  '| horas A-G', min(r['hora_navegacao'] for r in CSV4 if r['grupo'] != 'H'), max(r['hora_navegacao'] for r in CSV4 if r['grupo'] != 'H'),
  '| datas', C(r['data'] for r in CSV4))

P('\n== resumo 1 ==')
for g in 'IJK':
    L = grupo(g); c = C(x['tipo'] for x in L)
    P(g, len(L), {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in c.most_common()})
def top3_local(g):
    n = 0; ids = []
    for o in buscas(g):
        t3 = [x for x in ORG if x['id'] == o['id'] and x['pos'] <= 3]
        if len(t3) == 3 and all(x['tipo'] == 'local' for x in t3): n += 1; ids.append(o['id'])
    return n, ids
for g in 'IJK*': P('três primeiros todos por local, grupo', g, top3_local(g)[0], 'de', len(buscas(g)))
P('I: buscas em que NÃO:', [o['id'] for o in buscas('I') if o['id'] not in top3_local('I')[1]])
# grupos do item 4 (tipo do CSV do item 4)
for g in 'DEB':
    L = [r for r in CSV4 if r['grupo'] == g and r['superficie'] == 'orgânico']; c = C(MAPA_TIPO.get(r['tipo_pagina'], r['tipo_pagina']) for r in L)
    P('item 4 grupo', g, len(L), {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in c.most_common()})
    # recalculo com a regra (lista ampliada) para ver se muda
    c2 = C(tipo(r['dominio'], r['caminho']) for r in L)
    P('   recalculado com a lista ampliada:', {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in c2.most_common()})

P('\n== resumo 2 ==')
LI = grupo('I')
nb = C();
for i in {x['id'] for x in LI}:
    for d in {x['dom'] for x in LI if x['id'] == i}: nb[d] += 1
P('domínios do grupo I por nº de buscas:', nb.most_common(14))
P('em 5 ou mais buscas:', len([d for d, n in nb.items() if n >= 5]), sorted([(n, d) for d, n in nb.items() if n >= 5], reverse=True))
P('1ª posição grupo I:', C(x['dom'] for x in LI if x['pos'] == 1).most_common())
P('domínios distintos no grupo I:', len(nb))
domD = {r['dominio'] for r in CSV4 if r['grupo'] == 'D' and r['superficie'] == 'orgânico'}
domDE = {r['dominio'] for r in CSV4 if r['grupo'] in 'DE' and r['superficie'] == 'orgânico'}
P('já vistos no grupo D:', len(set(nb) & domD), '| em D ou E:', len(set(nb) & domDE))
nbD = C()
for i in {r['id'] for r in CSV4 if r['grupo'] == 'D'}:
    for d in {r['dominio'] for r in CSV4 if r['id'] == i and r['superficie'] == 'orgânico'}: nbD[d] += 1
d5 = {d for d, n in nbD.items() if n >= 5}
P('grupo D: domínios em 5 ou mais das 20:', len(d5), '| dos', len([d for d, n in nb.items() if n >= 5]), 'do grupo I, estão lá:', len({d for d, n in nb.items() if n >= 5} & d5),
  sorted({d for d, n in nb.items() if n >= 5} & d5))

P('\n== resumo 3 (grupo K) ==')
LK = grupo('K')
gov = [x for x in ORG if x['tipo'] == 'gov']
P('governo: resultados', len(gov), '| buscas', len({x['id'] for x in gov}), [(x['id'], x['pos'], x['dom']) for x in gov])
P('governo no K: buscas', len({x['id'] for x in gov if x['g'] == 'K'}), '| 1º em', [x['id'] for x in gov if x['pos'] == 1])
for g in 'IJK*':
    R = buscas(g)
    P(g, 'buscas', len(R), '| IA', sum(o['aio'] for o in R), '| bloco', sum(tem_bloco(o) for o in R), '| anúncio de texto', sum(1 for o in R if o['ads']),
      '| patrocinado', sum(tem_pat(o) for o in R), '| sem anúncio nenhum', sum(1 for o in R if not o['ads'] and not tem_pat(o)))
P('sem IA:', [o['q'] for o in BRUTO if not o['aio']]); P('sem bloco:', [(o['id'], o['q']) for o in BRUTO if not tem_bloco(o)])
P('bloco com patrocinado mas sem perfil orgânico?', [o['id'] for o in BRUTO if tem_pat(o) and not tem_bloco(o)])
for g, n in (('*', 79),):
    ids = {r['id'] for r in CSV4 if r['grupo'] != 'H'}
    def tem(i, f): return any(f(r) for r in CSV4 if r['id'] == i)
    P('item 4 A-G:', len(ids), 'IA', sum(tem(i, lambda r: r['visao_geral_ia'] == 'sim') for i in ids), 'bloco', sum(tem(i, lambda r: r['superficie'] == 'mapa (bloco Empresas)') for i in ids),
      'anúncio', sum(tem(i, lambda r: r['superficie'] == 'anúncio') for i in ids), 'patrocinado', sum(tem(i, lambda r: r['superficie'] == 'mapa (patrocinado)') for i in ids),
      'sem anúncio nenhum', sum(not tem(i, lambda r: r['superficie'] in ('anúncio', 'mapa (patrocinado)')) for i in ids))
    idsD = {r['id'] for r in CSV4 if r['grupo'] == 'D'}
    P('item 4 grupo D:', len(idsD), 'IA', sum(tem(i, lambda r: r['visao_geral_ia'] == 'sim') for i in idsD), 'bloco', sum(tem(i, lambda r: r['superficie'] == 'mapa (bloco Empresas)') for i in idsD),
      'anúncio', sum(tem(i, lambda r: r['superficie'] == 'anúncio') for i in idsD), 'patrocinado', sum(tem(i, lambda r: r['superficie'] == 'mapa (patrocinado)') for i in idsD))

P('\n== resumo 4 (ordem na página) ==')
for g in 'IJK*':
    R = buscas(g); ys = [o['y'] for o in R]
    P(g, 'ordens:', C(ordem(y) for y in ys).most_common())
    P('  primeira camada:', C(ordem(y).split(' > ')[0] for y in ys).most_common(), '| IA primeira entre as com IA:', sum(1 for y in ys if y['aio'] is not None and ordem(y).startswith('IA')), 'de', sum(1 for y in ys if y['aio'] is not None))
    P('  mapa antes do orgânico:', sum(1 for y in ys if y['pack'] is not None and y['pack'] < y['org']), 'de', sum(1 for y in ys if y['pack'] is not None),
      '| anúncio depois do orgânico:', sum(1 for y in ys if y['ad'] is not None and y['ad'] > y['org']), 'de', sum(1 for y in ys if y['ad'] is not None))
    P('  1º orgânico abaixo da 1ª tela (>= 945):', sum(1 for y in ys if y['org'] >= 945), 'de', len(ys), '| abaixo de 2 telas (>= 1890):', sum(1 for y in ys if y['org'] >= 1890),
      '| na 1ª tela:', sum(1 for y in ys if y['org'] < 945))
    for k in ('aio', 'pack', 'org', 'ad'):
        v = [y[k] for y in ys if y[k] is not None]
        if v: P(f'  {NOME[k]}: n={len(v)} mediana={statistics.median(v)} mín={min(v)} máx={max(v)} na 1ª tela={sum(1 for x in v if x < 945)}')
    # patrocinado acima do orgânico: o patrocinado está dentro do bloco; "acima" = bloco acima do 1º orgânico
    pt = [o for o in R if tem_pat(o)]
    P('  buscas com patrocinado:', len(pt), '| com bloco acima do 1º orgânico:', sum(1 for o in pt if o['y']['pack'] is not None and o['y']['pack'] < o['y']['org']))
P('posição do patrocinado dentro do bloco (índice na lista pack):', C((next(i for i, p in enumerate(o['pack']) if p.startswith('Patrocinado')), len(o['pack'])) for o in BRUTO if tem_pat(o)).most_common())

P('\n== resumo 5 (classe na 1ª posição) ==')
def classe(x):
    if x['dom'] in DOM: return DOM[x['dom']]['classe'] or 'não lido'
    if x['tipo'] == 'gov': return 'governo_universidade'
    if x['tipo'] == 'social': return 'rede_social_forum'
    return 'novo (não lido)'
P('valores de classe no serp_dominios.csv:', C(r['classe'] for r in DOM.values()).most_common())
for g in 'IJK*':
    L = grupo(g)
    P(g, 'todas:', C(classe(x) for x in L).most_common())
    P('   top3:', C(classe(x) for x in L if x['pos'] <= 3).most_common())
    P('   1ª:', C(classe(x) for x in L if x['pos'] == 1).most_common())
# item 4: licença na primeira posição por grupo
p1 = [r for r in CSV4 if r['superficie'] == 'orgânico' and r['posicao'] == '1']
for gs in ('D', 'E', 'B', 'ACFG', 'ABCDEFG', 'H', 'A', 'C', 'F', 'G'):
    L = [r for r in p1 if r['grupo'] in gs]
    P('item 4 grupo(s)', gs, ': 1ª posição com classe empresa_com_numero_de_licenca:', sum(1 for r in L if DOM.get(r['dominio'], {}).get('classe') == 'empresa_com_numero_de_licenca'), 'de', len(L))
P('quem são os 1ºs lugares do grupo I por classe:', sorted(C((x['dom'], classe(x)) for x in grupo('I') if x['pos'] == 1).items(), key=lambda z: -z[1]))
P('1º lugar K com licença:', [(x['id'], x['dom']) for x in grupo('K') if x['pos'] == 1 and classe(x) == 'empresa_com_numero_de_licenca'])

P('\n== resumo 6 (anunciante) ==')
ads = C(h if h and h != 'google.com' else 'não identificado' for o in BRUTO for h in o['ads'])
P('anúncios de texto:', sum(ads.values()), ads.most_common(), '| buscas com anúncio', sum(1 for o in BRUTO if o['ads']))
P('buscas com brasiltechs.com em anúncio de texto:', sum(1 for o in BRUTO if 'brasiltechs.com' in o['ads']))
pats = C(p[1] for o in BRUTO for p in pack_do_bruto(o) if p[0])
P('patrocinados:', pats.most_common(), '| buscas', sum(tem_pat(o) for o in BRUTO))
pats4 = C(r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (patrocinado)')
P('patrocinados no item 4:', pats4.most_common(5))

P('\n== resumo 7 (domínios novos) ==')
dom4 = {r['dominio'] for r in CSV4 if r['superficie'] == 'orgânico'}
P('buscas no item 4:', len({r['id'] for r in CSV4}))
for g in 'IJK*':
    L = grupo(g); ds = {x['dom'] for x in L}; nv = ds - dom4
    P(g, 'domínios', len(ds), '| novos', len(nv), '| resultados deles', pct(sum(1 for x in L if x['dom'] in nv), len(L)))
P('domínios distintos nas duas coletas (orgânico):', len(dom4 | {x['dom'] for x in ORG}), '| item 4 sozinho', len(dom4))
perf4_todos = {r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (bloco Empresas)'}
perf4_AG = {r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] != 'H'}
MP = [dict(id=o['id'], g=GRUPO[o['id']], nome=p[1], nota=p[2], av=p[3]) for o in BRUTO for p in pack_do_bruto(o) if not p[0]]
perfA = {m['nome'] for m in MP}
P('perfis distintos nas duas coletas (bloco):', len(perf4_todos | perfA), '| item 4 (89):', len(perf4_todos), '| A-G:', len(perf4_AG), '| ampliação:', len(perfA))
P('domínios novos (lista):', sorted({x['dom'] for x in ORG} - dom4))
novos = {x['dom'] for x in ORG} - dom4
P('novos por tipo:', C(x['tipo'] for x in ORG if x['dom'] in novos), '| novos gov:', sorted({x['dom'] for x in ORG if x['dom'] in novos and x['tipo'] == 'gov'}))

P('\n== seção 5 ==')
t3 = [x for x in ORG if x['pos'] <= 3]
P('top3: n', len(t3), C(x['tipo'] for x in t3).most_common())
IJ = [o['id'] for o in BRUTO if GRUPO[o['id']] in 'IJ']
P('I+J três primeiros todos por local:', top3_local('I')[0] + top3_local('J')[0], 'de', len(IJ))
dc = C(x['dom'] for x in ORG); P('352?', len(ORG), '| domínios', len(dc))
P('mais frequentes (resultados, top3):', [(d, n, sum(1 for x in t3 if x['dom'] == d)) for d, n in dc.most_common(12)])
P('1ª posição (40):', C(x['dom'] for x in ORG if x['pos'] == 1).most_common(10))
top10_4 = C(r['dominio'] for r in CSV4 if r['superficie'] == 'orgânico' and r['grupo'] != 'H').most_common(12)
P('10 mais frequentes da amostra principal -> aqui:', [(d, n, dc.get(d, 0)) for d, n in top10_4])
top10_4h = C(r['dominio'] for r in CSV4 if r['superficie'] == 'orgânico').most_common(12)
P('  (com o grupo H):', [(d, n, dc.get(d, 0)) for d, n in top10_4h])
dk = C(x['dom'] for x in LK); P('grupo K mais frequentes:', dk.most_common(4), '| tipos do uniprag no K:', C(x['tipo'] for x in LK if x['dom'] == 'uniprag.com.br'), [x['path'] for x in LK if x['dom'] == 'uniprag.com.br'])
P('K: domínios', len(dk), 'novos', len(set(dk) - dom4), 'resultados de novos', pct(sum(1 for x in LK if x['dom'] not in dom4), len(LK)))
# domínio com nome exato do bairro
P('ohub:', sorted({(x['id'], x['pos']) for x in ORG if x['dom'] == 'ohub.com.br'}))
P('listazn / encontravilamaria:', [(x['id'], x['pos'], x['dom']) for x in ORG if x['dom'] in ('listazn.com.br', 'encontravilamaria.com.br')], '| listazn no item 4:', 'listazn.com.br' in dom4, '| encontravilamaria no item 4:', 'encontravilamaria.com.br' in dom4)
P('gov no item 4 (grupos, termo, pos):', sorted({(r['id'], r['termo'], r['posicao'], r['dominio']) for r in CSV4 if r['superficie'] == 'orgânico' and MAPA_TIPO.get(r['tipo_pagina']) == 'gov'}))

P('\n== seção 5.1: bairro buscado no caminho (grupo I) ==')
BAIRRO = {'I01': ['brooklin'], 'I02': ['morumbi'], 'I03': ['saude'], 'I04': ['campo-belo', 'campo_belo', 'campobelo'], 'I05': ['interlagos'], 'I06': ['capao-redondo', 'capaoredondo'],
          'I07': ['vila-prudente', 'vilaprudente'], 'I08': ['sao-miguel', 'saomiguel'], 'I09': ['sapopemba'], 'I10': ['guaianases', 'guaianazes'], 'I11': ['tucuruvi'], 'I12': ['pirituba'],
          'I13': ['freguesia'], 'I14': ['casa-verde', 'casaverde'], 'I15': ['vila-maria', 'vilamaria'], 'I16': ['vila-leopoldina', 'vilaleopoldina'], 'I17': ['jaguare'],
          'I18': ['liberdade'], 'I19': ['consolacao'], 'I20': ['aclimacao']}
loc = [x for x in LI if x['tipo'] == 'local']
com = [x for x in loc if any(b in sem_acento(x['path']) for b in BAIRRO[x['id']])]
P('páginas por local no I:', len(loc), '| com o bairro buscado no caminho:', len(com), '| outras:', [(x['id'], x['pos'], x['dom'] + x['path']) for x in loc if x not in com])
P('domínio com nome do bairro:', [(x['id'], x['pos'], x['dom']) for x in LI if any(b.replace('-', '') in x['dom'].replace('-', '') for b in BAIRRO[x['id']])])
P('caminhos com 50+ caracteres classificados como serviço em I/J:', [(x['id'], x['pos'], x['dom'] + x['path']) for x in ORG if x['g'] in 'IJ' and x['tipo'] == 'servico' and len(x['path']) >= 50])
P('J05 6º:', [(x['dom'] + x['path'], x['tipo']) for x in ORG if x['id'] == 'J05' and x['pos'] == 6])
P('tamanho máximo de caminho:', max(len(x['path']) for x in ORG), '| de título:', max(len(x['tit']) for x in ORG))

P('\n== seção 6 (mapa) ==')
P('linhas', len(MP), '| perfis distintos', len(perfA), '| buscas com bloco', len({m['id'] for m in MP}), '| novos vs A-G:', len(perfA - perf4_AG), '| novos vs 89:', len(perfA - perf4_todos))
P('mais frequentes:', C(m['nome'] for m in MP).most_common(5))
P('Ddtizz:', C((m['nome'], m['nota'], m['av']) for m in MP if 'ddtizz' in m['nome'].lower()))
MI = [m for m in MP if m['g'] == 'I']; pI = {m['nome'] for m in MI}
perfD = {r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] == 'D'}
P('grupo I: buscas com bloco', len({m['id'] for m in MI}), 'linhas', len(MI), 'perfis', len(pI), '| já vistos no grupo D:', len(pI & perfD), '| em D ou E:', len(pI & {r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] in 'DE'}))
notas = [float(m['nota'].replace(',', '.')) for m in MP if m['nota']]
P('notas lidas', len(notas), 'mediana', statistics.median(notas), 'mín', min(notas), '| >= 4,8:', pct(sum(1 for n in notas if n >= 4.8), len(notas)), '| sem nota:', [m for m in MP if not m['nota']])
def av_por_perfil(M):
    av = {}
    for m in M:
        if m['av'].isdigit(): av[m['nome']] = int(m['av'])
    return av
av = av_por_perfil(MP); P('avaliações por perfil: lidos', len(av), 'mediana', statistics.median(av.values()), 'mín', min(av.values()), 'máx', max(av.values()))
avI = av_por_perfil(MI); P('  grupo I: lidos', len(avI), 'mediana', statistics.median(avI.values()))
def av4(gs):
    av = {}
    for r in CSV4:
        if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] in gs and r['avaliacoes'].isdigit(): av[r['titulo_ou_nome']] = int(r['avaliacoes'])
    return av
a = av4('ABCDEFG'); P('  item 4 A-G: lidos', len(a), 'mediana', statistics.median(a.values()), '| perfis distintos A-G', len(perf4_AG))
a = av4('D'); P('  item 4 D: lidos', len(a), 'mediana', statistics.median(a.values()))
# perfis com mais de um valor de avaliações (a mediana "por perfil" fica com o último)
multi = collections.defaultdict(set)
for m in MP: multi[m['nome']].add((m['nota'], m['av']))
P('perfis com mais de um par (nota, avaliações):', {k: v for k, v in multi.items() if len(v) > 1})

P('\n== seção 11 (repetições) ==')
bid = {o['id']: o for o in BRUTO}
for r in REP2:
    a = bid[r['id'][:-1]]
    ua = [s.partition(' | ')[0] for s in a['org']]; ur = [s.partition(' | ')[0] for s in r['org']]
    pa = {p[1] for p in pack_do_bruto(a) if not p[0]}; pr = {p[1] for p in pack_do_bruto(r) if not p[0]}
    P(r['id'], a['nv'][:5], r['nv'][:5], '| 1º igual:', ua[0] == ur[0], '| mesmos endereços na ordem:', ua == ur, len(ua), len(ur), '| perfis em comum:', len(pa & pr), 'de', len(pa), len(pr),
      '| mesma ordem dos perfis:', [p[1] for p in pack_do_bruto(a) if not p[0]] == [p[1] for p in pack_do_bruto(r) if not p[0]],
      '| local:', repr(a['loc']), repr(r['loc']), '| anúncios:', len(a['ads']), '->', len(r['ads']), '| y:', a['y'], '->', r['y'], '| ordem igual:', ordem(a['y']) == ordem(r['y']),
      '| pat:', tem_pat(a), tem_pat(r), '| IA:', a['aio'], r['aio'])
