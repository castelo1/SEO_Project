#!/usr/bin/env python3
"""Segunda passada do item 4 — recalcula, a partir dos .jsonl, os números de serp_sp.md. SÓ LEITURA."""
import sys, os, re, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2item4_comum import *
C = collections.Counter
recs = lotes(); AG = [o for o in recs if o['id'][0] != 'H']; H = [o for o in recs if o['id'][0] == 'H']
def pct(a, b): return f'{a}/{b}={100*a/b:.1f}%'
def has_pack(o): return any(not p['pat'] for p in pack_de(o))
def has_pat(o): return any(p['pat'] for p in pack_de(o))

print('=== SEÇÃO 3 / S1.1: camadas ===')
for g in 'ABCDEFG':
    G = [o for o in AG if o['id'][0] == g]
    print(g, len(G), 'aio', sum(o['aio'] for o in G), 'pack', sum(has_pack(o) for o in G), 'ads', sum(bool(o['ads']) for o in G), 'pat', sum(has_pat(o) for o in G))
print('TOTAL', len(AG), 'aio', pct(sum(o['aio'] for o in AG), 79), 'pack', pct(sum(has_pack(o) for o in AG), 79), 'ads', pct(sum(bool(o['ads']) for o in AG), 79), 'pat', pct(sum(has_pat(o) for o in AG), 79))
print('pack vazio mas com patrocinado?', [o['id'] for o in AG if has_pat(o) and not has_pack(o)])
print('sem anúncio nenhum (nem texto nem patrocinado):', sum(1 for o in AG if not o['ads'] and not has_pat(o)), '| sem anúncio de texto:', sum(1 for o in AG if not o['ads']))
print('sem aio:', [(o['id'], o['q']) for o in AG if not o['aio']])
print('sem pack:', [(o['id'], o['q']) for o in AG if not has_pack(o)])
print('tamanho do pack (não patrocinado):', C(sum(1 for p in pack_de(o) if not p['pat']) for o in AG))

print('\n=== SEÇÃO 4.1 / S1.2: orgânico ===')
ORG = [(o['id'],) + x for o in AG for x in org_de(o)]   # id,pos,host,path,titulo
dom = C(x[2] for x in ORG); cons = collections.defaultdict(set); top3 = C(); p1 = C()
for i, p, h, pa, t in ORG:
    cons[h].add(i)
    if p <= 3: top3[h] += 1
    if p == 1: p1[h] += 1
n = len(ORG); print('resultados', n, 'domínios', len(dom), 'orgânicos por busca', C(len(o['org']) for o in AG))
mc = dom.most_common()
for k in (3, 5, 10, 20): print(f'top {k}:', pct(sum(v for _, v in mc[:k]), n))
print('domínios com 1 aparição:', sum(1 for v in dom.values() if v == 1), '| com 2:', sum(1 for v in dom.values() if v == 2), '| com 3+:', sum(1 for v in dom.values() if v >= 3))
print('1ª posição:', p1.most_common(9), '| total', sum(p1.values()))
print('dez mais frequentes:', [(d, v, len(cons[d]), top3[d]) for d, v in mc[:12]])
for g in 'ABCDEFG':
    dg = C(x[2] for x in ORG if x[0][0] == g); tot = sum(dg.values()); ac = 0; k = 0
    for d, v in dg.most_common():
        ac += v; k += 1
        if ac >= tot / 2: break
    print(f'  grupo {g}: {tot} resultados, {len(dg)} domínios, {k} somam metade (acumulado {ac})')

print('\n=== SEÇÃO 4.2: tipo de página ===')
tp = lambda x: tipo_pagina(x[2], x[3])
ordem = ['página interna por local', 'página interna (serviço/outro)', 'página inicial', 'blog/artigo', 'governo/universidade', 'rede social/fórum']
for g in 'ABCDEFG':
    xs = [x for x in ORG if x[0][0] == g]; c = C(tp(x) for x in xs)
    print(f'  {g} ({len(xs)}):', [f'{100*c[t]/len(xs):.1f}' for t in ordem], [c[t] for t in ordem])
print('  todos:', C(tp(x) for x in ORG))
t3 = [x for x in ORG if x[1] <= 3]; print('  top3 (n=%d):' % len(t3), C(tp(x) for x in t3))
DE = [o for o in AG if o['id'][0] in 'DE']
print('  buscas D+E:', len(DE), '| top3 todos por local:', sum(1 for o in DE if len(org_de(o)) >= 3 and all(tipo_pagina(h, pa) == 'página interna por local' for p, h, pa, t in org_de(o)[:3])))
print('  idem só D:', sum(1 for o in DE if o['id'][0] == 'D' and all(tipo_pagina(h, pa) == 'página interna por local' for p, h, pa, t in org_de(o)[:3])))
xsDE = [x for x in ORG if x[0][0] in 'DE']; print('  % por local em D+E:', pct(sum(1 for x in xsDE if tp(x) == 'página interna por local'), len(xsDE)))
loc = [x for x in ORG if tp(x) == 'página interna por local']
umn = [x for x in loc if len([s for s in x[3].split('/') if s]) == 1]
print('  páginas por local:', len(loc), pct(len(loc), n), '| de um nível só:', len(umn))
D = [x for x in ORG if x[0][0] == 'D']; dD = collections.defaultdict(set)
for x in D: dD[x[2]].add(x[0])
tr = sorted([(len(v), d) for d, v in dD.items() if len(v) >= 5], reverse=True); print('  domínios em 5+ das 20 buscas D:', len(tr), tr)
r13 = [x for x in D if x[2] in {d for _, d in tr}]; print('  resultados desses domínios em D:', len(r13), '| por local:', sum(1 for x in r13 if tp(x) == 'página interna por local'))
print('  exceções:', [(x[0], x[2], x[3]) for x in r13 if tp(x) != 'página interna por local'])
print('  domínios com nome de bairro:', [(d, v) for d, v in dom.items() if re.search(r'dedetizadora(em|na|no|zona)', d)])
for d in ('rentokil.com', 'orkinbrasil.com.br', 'orkinsp.com.br'): print('  ', d, C(x[0][0] for x in ORG if x[2] == d))

print('\n=== SEÇÃO 4.3: títulos ===')
def conta(xs, f): return sum(1 for x in xs if f(sem_acento(x[4])))
regras = {'telefone [tel] (ou "[t" no fim)': lambda t: '[tel' in t or t.endswith('[t') or t.endswith('[te') or t.endswith('['),
          'telefone só "[tel" completo': lambda t: '[tel' in t,
          '24 horas/24h (inclui "24 h")': lambda t: bool(re.search(r'24\s?h', t)),
          'preço / a partir de (inclui "prec")': lambda t: 'prec' in t or 'a partir de' in t,
          'melhor': lambda t: 'melhor' in t, 'orçamento': lambda t: 'orcamento' in t}
for k, f in regras.items(): print(f'  {k}: todos {pct(conta(ORG, f), n)} | top3 {pct(conta(t3, f), len(t3))}')
print('  comprimento máx. do título por lote:', {a: max(len(x[3]) for o in recs if o['arquivo'] == a for x in org_de(o)) for a in sorted({o['arquivo'] for o in recs})})
print('  títulos > 34 no lote 3:', [(o['id'], len(x[3])) for o in recs if o['arquivo'] == 'lote_03.jsonl' for x in org_de(o) if len(x[3]) > 34])
print('  caminho máx (com barra inicial):', max(len(x[3]) for x in ORG))

print('\n=== SEÇÃO 4.4 ===')
oh = [x for x in ORG if x[2] == 'ohub.com.br']; print('  ohub:', len(oh), 'resultados,', len({x[0] for x in oh}), 'buscas, posições', sorted(x[1] for x in oh), 'mediana', statistics.median(x[1] for x in oh), '| caminhos', C(x[3][:40] for x in oh).most_common(4))
for d in ('triider.com.br', 'reclameaqui.com.br', 'coteibem.com.br', 'pedegas.com', 'pestwase.com', 'listazn.com.br', 'getninjas.com.br', 'habitissimo.com.br', 'instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'sivisa.saude.sp.gov.br'):
    print('  ', d, dom.get(d, 0), [(x[0], x[1]) for x in ORG if x[2] == d])
print('  getninjas/habitissimo em qualquer domínio:', [d for d in dom if 'ninja' in d or 'habitiss' in d])
gov = [x for x in ORG if tp(x) == 'governo/universidade']; print('  governo/univ:', len(gov), C(x[0] for x in gov), '| domínios', len({x[2] for x in gov}))
soc = [x for x in ORG if tp(x) == 'rede social/fórum']; print('  rede social:', len(soc), C(x[2] for x in soc), [(x[0]) for x in soc])
qs = {o['id']: o['q'] for o in recs}
print('  buscas com governo:', [(i, qs[i], c) for i, c in C(x[0] for x in gov).items()])
esc = [o for o in AG if 'escorpi' in o['q']]; print('  escorpião:', [(o['id'], o['q'], len(o['org']), sum(1 for x in org_de(o) if tipo_pagina(x[1], x[2]) == 'governo/universidade'), has_pack(o), [x[1] for x in org_de(o)]) for o in esc])

print('\n=== SEÇÃO 5: mapa ===')
PK = [(o['id'], p) for o in AG for p in pack_de(o) if not p['pat']]
nomes = C(p['nome'] for _, p in PK); print('  linhas', len(PK), 'perfis distintos', len(nomes), '| buscas com bloco', len({i for i, _ in PK}))
print('  mais frequentes:', nomes.most_common(8), '| top3 share', pct(sum(v for _, v in nomes.most_common(3)), len(PK)))
print('  buscas em que cada um aparece:', [(nm, len({i for i, p in PK if p['nome'] == nm})) for nm, _ in nomes.most_common(6)])
print('  cidade exibida do ARMOR:', C(re.findall(r'(Osasco|São Paulo|Embu das Artes) - SP', p['bruto'])[0] if re.findall(r'(Osasco|São Paulo|Embu das Artes) - SP', p['bruto']) else '-' for _, p in PK if p['nome'].startswith('ARMOR')))
PD = [(i, p) for i, p in PK if i[0] == 'D']; print('  grupo D: buscas com bloco', len({i for i, _ in PD}), 'linhas', len(PD), 'perfis distintos', len({p['nome'] for _, p in PD}), '| líderes', C(p['nome'] for _, p in PD).most_common(5))
PDE = [(i, p) for i, p in PK if i[0] in 'DE']; print('  grupos D+E: buscas com bloco', len({i for i, _ in PDE}), 'perfis distintos', len({p['nome'] for _, p in PDE}))
for g in 'ABCDEFG': print('   ', g, C(p['nome'] for i, p in PK if i[0] == g).most_common(4))
def cidade(b):
    m = re.search(r'([A-ZÀ-Ú][\wÀ-ú ]+?) - SP', b); return m.group(1).strip() if m else ''
cid = C()
for _, p in PK:
    m = re.findall(r'(São Paulo|Osasco|Embu das Artes|[A-ZÀ-Ú][a-zà-ú]+(?: [A-ZÀ-Ú]?[a-zà-ú]+)*) - SP', p['bruto'])
    cid[m[-1] if m else '(sem)'] += 1
print('  cidade exibida:', cid.most_common())
lidas = [p for _, p in PK if p['nota']]; print('  linhas com nota lida:', len(lidas), '| sem:', [(i, p['bruto']) for i, p in PK if not p['nota']])
notas = [float(p['nota'].replace(',', '.')) for p in lidas]; print('  nota mediana', statistics.median(notas), 'mín', min(notas), '| >=4,8:', pct(sum(1 for x in notas if x >= 4.8), len(notas)), '| sobre 202:', pct(sum(1 for x in notas if x >= 4.8), len(PK)))
pa = {}
for _, p in PK:
    if p['aval']: pa.setdefault(p['nome'], set()).add(int(p['aval']))
print('  perfis com número lido:', len(pa), '| com mais de um valor:', {k: v for k, v in pa.items() if len(v) > 1})
av = sorted(max(v) for v in pa.values()); q = statistics.quantiles(av, n=4, method='inclusive')
print('  avaliações por perfil: mediana', statistics.median(av), 'quartis (inclusive)', q, 'exclusive', statistics.quantiles(av, n=4), 'máx', max(av), '| <=42:', sum(1 for x in av if x <= 42), '| >313:', sum(1 for x in av if x > 313))
print('  "mil" nos brutos:', [(i, p['bruto']) for i, p in PK if ' mil' in p['bruto']])
an1 = [(i, p) for i, p in PK if re.search(r'Mais de \d+ anos? no mercado', p['bruto'])]; an2 = [(i, p) for i, p in PK if re.search(r'(?<![\d,(])\b\d{1,2}a\b', p['bruto']) and not re.search(r'Mais de \d+ anos? no mercado', p['bruto'])]
lot = {o['id']: o['arquivo'] for o in recs}
print('  "anos no mercado": por extenso', len(an1), C(lot[i] for i, _ in an1), '| abreviado', len(an2), C(lot[i] for i, _ in an2), '| total', len(an1) + len(an2))
anos = [int(x) for _, p in an1 for x in re.findall(r'Mais de (\d+) anos?', p['bruto'])] + [int(x) for _, p in an2 for x in re.findall(r'(?<![\d,(])\b(\d{1,2})a\b', p['bruto'])]
print('  anos: mín', min(anos), 'máx', max(anos), '| "Há/anos" outras formas:', [(i, p['bruto']) for i, p in PK if 'ano' in p['bruto'] and not re.search(r'Mais de \d+ anos? no mercado', p['bruto'])][:5])
print('  comprimento máx. da linha do pack por lote:', {a: max([len(s) for o in recs if o['arquivo'] == a for s in o['pack']] or [0]) for a in sorted({o['arquivo'] for o in recs})})
sv = [nm for nm in nomes if any(k in sem_acento(nm) for k in ('dedetiz', 'pragas', 'cupi'))]; print('  nomes com palavra de serviço:', len(sv), 'de', len(nomes), '| sem:', [nm for nm in nomes if nm not in sv])
B20 = ['moema','pinheiros','vila mariana','tatuape','santana','lapa','itaim bibi','santo amaro','mooca','perdizes','santa cecilia','higienopolis','butanta','ipiranga','penha','jabaquara','itaquera','campo limpo','bela vista','vila madalena']
def regra_local(nm):
    s = sem_acento(nm)
    return bool(re.search(r'zona (norte|sul|leste|oeste)', s) or '24h' in s or 'sao paulo' in s or re.search(r'\bsp\b', s) or re.search(r'\bvila ', s) or 'osasco' in s or any(b in s for b in B20))
lc = [nm for nm in nomes if regra_local(nm)]; print('  nomes com local/24h (regra):', len(lc), lc)
print('  categorias vistas (lotes 1-2):', C(m for _, p in PK for m in re.findall(r'· ([A-ZÀ-Ú][^·]*?)(?: Mais de| ·|$)', p['bruto'])).most_common(8))
print('  "pássaros":', [(i, p['bruto']) for i, p in PK if 'ssaro' in p['bruto']])
print('  nomes de perfis parecidos com domínio:', {k: [d for d in dom if k in d] for k in ('primordial', 'lunar', 'heloin', 'sanitech', 'armor', 'sjg')})

print('\n=== SEÇÃO 6: anúncios ===')
ADS = [(o['id'], h) for o in AG for h in o['ads']]; print('  anúncios', len(ADS), 'em', len({i for i, _ in ADS}), 'buscas')
ca = C(h for _, h in ADS); print('  por domínio (anúncios):', ca.most_common()); print('  por domínio (buscas):', [(d, len({i for i, h in ADS if h == d})) for d, _ in ca.most_common()])
PAT = [(o['id'], p) for o in AG for p in pack_de(o) if p['pat']]; print('  patrocinado: buscas', len({i for i, _ in PAT}), 'linhas', len(PAT), C((p['nome'], p['nota'], p['aval']) for _, p in PAT))
print('  nº de anúncios por busca:', C(len(o['ads']) for o in AG))
print('  brasiltechs texto OU patrocinado:', len({i for i, h in ADS if h == 'brasiltechs.com'} | {i for i, _ in PAT}))

print('\n=== SEÇÃO 12: grupo H ===')
for o in H:
    og = org_de(o); print('  ', o['id'], o['q'], '| aio', o['aio'], '| ads', len(o['ads']), o['ads'], '| pack', sum(1 for p in pack_de(o) if not p['pat']), '+', sum(1 for p in pack_de(o) if p['pat']), '| org', len(og), '| 1º', og[0][1], og[0][2], '| loc', o['loc'])
adsH = [h for o in H for h in o['ads']]; print('  anúncios H:', len(adsH), C(adsH), '| buscas com anúncio', sum(bool(o['ads']) for o in H), '| sem nenhum anúncio (texto nem patrocinado):', sum(1 for o in H if not o['ads'] and not has_pat(o)))
OH = [(o['id'],) + x for o in H for x in org_de(o)]; dh = C(x[2] for x in OH); novos = [d for d in dh if d not in dom]
print('  resultados', len(OH), 'domínios', len(dh), '| novos', len(novos), 'com', sum(dh[d] for d in novos), 'resultados', pct(sum(dh[d] for d in novos), len(OH)))
print('  tipo de página H:', C(tp(x) for x in OH).most_common())
dc = {r['dominio']: r for r in dominios_csv()}
def classeH(d):
    if d in dc: return dc[d]['classe']
    if d.endswith('.gov.br') or d in ('gov.br', 'puspc.usp.br'): return 'governo_universidade'
    if d in SOCIAL: return 'rede_social_forum'
    return 'NOVO'
print('  classe H:', C(classeH(x[2]) for x in OH).most_common())
for nome, ids in (('Confiança', ('H01', 'H02', 'H03')), ('Preço', ('H04', 'H05', 'H10')), ('Informativa', ('H06', 'H07', 'H08', 'H09'))):
    xs = [x for x in OH if x[0] in ids]; print(f'  {nome}: {len(xs)} resultados | classes', C(classeH(x[2]) for x in xs).most_common(), '| anúncios', sum(len(o['ads']) for o in H if o['id'] in ids))
    print('     governo:', [(x[0], x[1], x[2]) for x in xs if classeH(x[2]) == 'governo_universidade'], '| diretório:', [(x[0], x[1], x[2]) for x in xs if classeH(x[2]) == 'diretorio_marketplace'], '| social:', [(x[0], x[1], x[2]) for x in xs if classeH(x[2]) == 'rede_social_forum'])
print('  novos domínios:', sorted(novos))
print('  novos que são gov/social:', [d for d in novos if classeH(d) != 'NOVO'])
srv = [x for x in OH if x[2] == 'dedetizadora.srv.br']; print('  dedetizadora.srv.br em H:', len(srv), 'resultados,', len({x[0] for x in srv}), 'buscas', [(x[0], x[1], x[3], x[4]) for x in srv])
for i in ('H02', 'H03', 'H04', 'H05', 'H10', 'H06', 'H07', 'H08', 'H09', 'H01'):
    print('  ', i, [(x[1], x[2], x[3][:45], x[4]) for x in OH if x[0] == i])

print('\n=== SEÇÃO 13: repetição ===')
rep = repeticao(); by = {o['id']: o for o in recs}
for r in rep:
    o = by[r['id'][:3]]; a = org_de(o); b = org_de(r)
    da = [x[1] for x in a]; db = [x[1] for x in b]
    pa_ = [p['nome'] for p in pack_de(o) if not p['pat']]; pb = [p['nome'] for p in pack_de(r) if not p['pat']]
    print('  ', r['id'], r['q'], o['nv'], '->', r['nv'], f"dif {(seg(r['nv']) - seg(o['nv'])) / 3600:.2f} h", '| mesmo 1º (domínio+caminho):', a[0][1:3] == b[0][1:3], '| top3 domínios iguais (ordem):', da[:3] == db[:3], '(conjunto):', set(da[:3]) == set(db[:3]),
          '| domínios em comum', len(set(da) & set(db)), 'de', len(set(da)), '/', len(set(db)), 'n org', len(a), len(b), '| perfis em comum', len(set(pa_) & set(pb)), 'de', len(pa_), len(pb), '| loc', o['loc'], '/', r['loc'], '| ads', len(o['ads']), '->', len(r['ads']), '| aio', o['aio'], r['aio'])
