#!/usr/bin/env python3
"""Verificador independente do item 4 — só leitura. Refaz as contas de docs/mercado/serp_sp.md a partir dos .jsonl e CSV.
Não grava nada. Uso: python3 verif_item4_contas.py [bloco]"""
import csv, glob, json, os, re, sys, statistics, collections, unicodedata
R = '/home/ancastelo/pessoal/SEO_Project'
D = R + '/data'
C = collections.Counter
def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
def seg(h):
    a, b, c = h.split(':'); return int(a) * 3600 + int(b) * 60 + int(c)
recs = []
for f in sorted(glob.glob(D + '/serp_raw/lote_*.jsonl')):
    for l in open(f, encoding='utf-8'):
        if l.strip():
            o = json.loads(l); o['arq'] = os.path.basename(f); recs.append(o)
rep = [json.loads(l) for l in open(D + '/serp_raw/repeticao_01.jsonl', encoding='utf-8') if l.strip()]
cons = list(csv.DictReader(open(D + '/serp_consultas.csv', encoding='utf-8')))
rows = list(csv.DictReader(open(D + '/serp_sp.csv', encoding='utf-8')))
doms = list(csv.DictReader(open(D + '/serp_dominios.csv', encoding='utf-8')))
kw = list(csv.DictReader(open(D + '/palavras_chave.csv', encoding='utf-8')))
byid = {o['id']: o for o in recs}
main = [o for o in recs if o['id'][0] != 'H']
H = [o for o in recs if o['id'][0] == 'H']
def P(*a): print(*a)
def pct(a, b): return f'{a}/{b}={100*a/b:.1f}%'

def bloco_basico():
    P('== BASICO ==')
    P('registros jsonl', len(recs), 'ids distintos', len(byid), '| main', len(main), '| H', len(H), '| rep', len(rep))
    P('por arquivo', C(o['arq'] for o in recs))
    P('consultas planejadas', len(cons), C(c['grupo'] for c in cons))
    P('feitas por grupo', sorted(C(o['id'][0] for o in recs).items()))
    P('ids planejados sem registro', [c['id'] for c in cons if c['id'] not in byid], '| registros fora do plano', [i for i in byid if i not in {c['id'] for c in cons}])
    dif = [(c['id'], c['termo'], byid[c['id']]['q']) for c in cons if c['id'] in byid and c['termo'].lower() != byid[c['id']]['q'].lower()]
    P('termo planejado != q:', dif)
    P('csv linhas', len(rows), '| A-G', sum(1 for r in rows if r['grupo'] != 'H'), '| H', sum(1 for r in rows if r['grupo'] == 'H'))
    P('csv superficies', C(r['superficie'] for r in rows))
    # csv x jsonl: linhas esperadas
    esp = sum(len(o['ads']) + len(o['pack']) + len(o['org']) for o in recs)
    P('linhas esperadas a partir dos jsonl', esp)
    # csv consistente com jsonl por id
    bad = []
    for o in recs:
        rr = [r for r in rows if r['id'] == o['id']]
        if len(rr) != len(o['ads']) + len(o['pack']) + len(o['org']): bad.append((o['id'], 'n'))
        for r in rr:
            if r['termo'] != o['q'] or r['hora_navegacao'] != o['nv'] or r['logado'] != ('sim' if o['lg'] else 'não') or r['local_exibido'] != (o['loc'] or 'não exibido') or r['visao_geral_ia'] != ('sim' if o['aio'] else 'não'):
                bad.append((o['id'], 'campo')); break
        og = [r for r in rr if r['superficie'] == 'orgânico']
        for r, s in zip(og, o['org']):
            u, _, t = s.partition(' | '); host, _, path = u.partition('/')
            if r['dominio'] != host or r['caminho'] != '/' + path: bad.append((o['id'], 'org', r['dominio'], host)); break
    P('csv x jsonl divergencias', bad)
    P('logado', C(o['lg'] for o in recs), '| rep', C(o['lg'] for o in rep))
    P('loc main', C(o['loc'] for o in main)); P('loc H', C(o['loc'] for o in H))

def bloco_registro():
    P('== REGISTRO x JSONL ==')
    txt = open(R + '/docs/mercado/serp_sp_registro.md', encoding='utf-8').read().splitlines()
    lin = [l for l in txt if re.match(r'^\| [A-H]\d\d ', l)]
    P('linhas de busca no registro', len(lin))
    falhas = []; vistos = set()
    for l in lin:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        i, grupo, termo, hora, lg, loc, ia, nads, pk, norg, lote = c
        o = byid.get(i); vistos.add(i)
        if not o: falhas.append((i, 'sem jsonl')); continue
        pat = sum(1 for p in o['pack'] if p.startswith('Patrocinado'))
        esperado = [o['q'], o['nv'], 'sim' if o['lg'] else 'não', o['loc'] or '—', 'sim' if o['aio'] else 'não', str(len(o['ads'])), f"{len(o['pack'])-pat}{' + 1' if pat else ''}", str(len(o['org'])), o['arq']]
        if [termo, hora, lg, loc, ia, nads, pk, norg, lote] != esperado: falhas.append((i, [termo, hora, lg, loc, ia, nads, pk, norg, lote], esperado))
        if pat > 1: falhas.append((i, 'mais de um patrocinado', pat))
    P('ids no registro', len(vistos), '| faltam', [i for i in byid if i not in vistos])
    P('falhas', falhas)
    P('ultima linha:', txt[-1])
    P('campos vazios: q', [o['id'] for o in recs if not o['q']], 'nv', [o['id'] for o in recs if not re.match(r'^\d\d:\d\d:\d\d$', o['nv'])])

def bloco_intervalos():
    P('== INTERVALOS ==')
    todos = sorted([(seg(o['nv']), o['id']) for o in recs] + [(seg(o['nv']), 'R-' + o['id']) for o in rep])
    P('primeira', min(o['nv'] for o in recs), 'ultima lotes', max(o['nv'] for o in recs), 'rep', [(o['id'], o['nv'], o['t']) for o in rep])
    j1 = [x for x in todos if x[0] < seg('22:00:00')]; j2 = [x for x in todos if x[0] >= seg('22:00:00')]
    for nome, j in (('janela1', j1), ('janela2', j2)):
        iv = [(j[k + 1][0] - j[k][0], j[k][1], j[k + 1][1]) for k in range(len(j) - 1)]
        v = [x[0] for x in iv]
        P(nome, 'n buscas', len(j), 'de', j[0], 'a', j[-1], '| n intervalos', len(v), '| mediana', statistics.median(v), 'min', min(v), 'max', max(v))
        P('   abaixo de 20s:', [x for x in iv if x[0] < 20]); P('   iguais a 20:', [x for x in iv if x[0] == 20])
        P('   maiores:', sorted(iv, reverse=True)[:5]); P('   menores:', sorted(iv)[:6])
    # ordem por id == ordem por hora?
    ordem_hora = [x[1] for x in j1]
    P('ordem por hora == ordem do plano?', ordem_hora == [c['id'] for c in cons if c['grupo'] != 'H'])
    if ordem_hora != [c['id'] for c in cons if c['grupo'] != 'H']: P('   ordem por hora:', ordem_hora)
    P('buscas entre 21:17 e 23:17:', [(o['id'], o['nv']) for o in recs + rep if seg('21:17:00') <= seg(o['nv']) <= seg('23:17:59')])
    P('H:', [(o['id'], o['nv']) for o in H])
    # t - nv
    P('t-nv (s) main: min', min(seg(o['t']) - seg(o['nv']) for o in main), 'max', max(seg(o['t']) - seg(o['nv']) for o in main))
    P('duracao coleta continua antes das 21:16: ultimas pausas >60s na janela 1:', [(x, a, b) for x, a, b in [(j1[k + 1][0] - j1[k][0], j1[k][1], j1[k + 1][1]) for k in range(len(j1) - 1)] if x > 60])

def camadas(o):
    pat = any(p.startswith('Patrocinado') for p in o['pack'])
    npk = sum(1 for p in o['pack'] if not p.startswith('Patrocinado'))
    return dict(aio=bool(o['aio']), pack=npk > 0, ads=len(o['ads']) > 0, pat=pat)

def bloco_camadas():
    P('== CAMADAS (secao 3) ==')
    for g in 'ABCDEFG':
        gg = [o for o in main if o['id'][0] == g]; cs = [camadas(o) for o in gg]
        P(g, len(gg), 'aio', sum(c['aio'] for c in cs), 'pack', sum(c['pack'] for c in cs), 'ads', sum(c['ads'] for c in cs), 'pat', sum(c['pat'] for c in cs))
    cs = [camadas(o) for o in main]
    P('total', len(main), 'aio', pct(sum(c['aio'] for c in cs), 79), 'pack', pct(sum(c['pack'] for c in cs), 79), 'ads', pct(sum(c['ads'] for c in cs), 79), 'pat', pct(sum(c['pat'] for c in cs), 79))
    P('sem anuncio nenhum (nem texto nem pat):', sum(1 for c in cs if not c['ads'] and not c['pat']), '| sem anuncio de texto', sum(1 for c in cs if not c['ads']))
    P('pat sem bloco?', [o['id'] for o in main if camadas(o)['pat'] and not camadas(o)['pack']])
    P('sem aio:', [(o['id'], o['q']) for o in main if not o['aio']])
    P('sem pack:', [(o['id'], o['q']) for o in main if not camadas(o)['pack']])
    P('pack com so patrocinado ou tamanhos', C(sum(1 for p in o['pack'] if not p.startswith('Patrocinado')) for o in main))

LOCAIS = ['zona-leste','zona-norte','zona-oeste','zona-sul','centro','moema','pinheiros','vila-mariana','tatuape','santana','lapa',
          'itaim-bibi','santo-amaro','mooca','perdizes','santa-cecilia','higienopolis','butanta','ipiranga','penha','jabaquara',
          'itaquera','campo-limpo','bela-vista','vila-madalena','osasco','jardim-paulista','barra-funda','analia-franco']
SOCIAL = ('instagram.com','facebook.com','reddit.com','youtube.com','tiktok.com','linkedin.com')
def tipo_pagina(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'governo/universidade'
    if host in SOCIAL: return 'rede social/fórum'
    if p in ('', '/'): return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog/artigo'
    if any(l in p for l in LOCAIS): return 'página interna por local'
    return 'página interna (serviço/outro)'
def orgs(lst):
    out = []
    for o in lst:
        for i, s in enumerate(o['org'], 1):
            u, _, t = s.partition(' | '); host, _, path = u.partition('/')
            out.append(dict(id=o['id'], g=o['id'][0], pos=i, dom=host, path='/' + path, tit=t.strip(), tipo=tipo_pagina(host, '/' + path)))
    return out
OM = orgs(main); OH = orgs(H)

def bloco_organico():
    P('== ORGANICO (secao 4) ==')
    dom = C(r['dom'] for r in OM); n = len(OM)
    P('resultados', n, 'dominios', len(dom), '| por busca n org', C(len(o['org']) for o in main))
    mc = dom.most_common()
    for k in (5, 10, 20): P(' top', k, pct(sum(v for _, v in mc[:k]), n))
    P(' empates na fronteira: 5o/6o', mc[4], mc[5], '10o/11o', mc[9], mc[10], '20o/21o', mc[19], mc[20])
    P(' dominios com 1 aparicao', sum(1 for v in dom.values() if v == 1), '| com 1 ou 2', sum(1 for v in dom.values() if v <= 2))
    P(' primeira posicao', C(r['dom'] for r in OM if r['pos'] == 1).most_common(9))
    cons_ = collections.defaultdict(set); t3 = C()
    for r in OM:
        cons_[r['dom']].add(r['id'])
        if r['pos'] <= 3: t3[r['dom']] += 1
    P(' top10 (res, buscas, top3):', [(d, v, len(cons_[d]), t3[d]) for d, v in mc[:11]])
    for g in 'ABCDEFG':
        gd = C(r['dom'] for r in OM if r['g'] == g); tot = sum(gd.values()); acc = 0; k = 0
        for d, v in gd.most_common():
            acc += v; k += 1
            if acc >= tot / 2: break
        P('  grupo', g, 'res', tot, 'dominios', len(gd), 'metade com', k, f'(acum {acc}; {k}/{len(gd)}={k/len(gd):.2f})')
    P('-- 4.2 tipo')
    tipos = ['página interna por local', 'página interna (serviço/outro)', 'página inicial', 'blog/artigo', 'governo/universidade', 'rede social/fórum']
    for g in 'ABCDEFG':
        gt = C(r['tipo'] for r in OM if r['g'] == g); tot = sum(gt.values())
        P('  ', g, tot, [f'{100*gt[t]/tot:.1f}' for t in tipos], [gt[t] for t in tipos])
    P('  tipo total', C(r['tipo'] for r in OM))
    P('  csv tipo_pagina confere com recalculo?', C(r['tipo_pagina'] for r in rows if r['superficie'] == 'orgânico' and r['grupo'] != 'H') == C({k: v for k, v in C(r['tipo'] for r in OM).items()}))
    top3 = [r for r in OM if r['pos'] <= 3]
    P('  top3 n', len(top3), C(r['tipo'] for r in top3))
    DE = [o for o in main if o['id'][0] in 'DE']
    allloc = [o['id'] for o in DE if len(o['org']) >= 3 and all(r['tipo'] == 'página interna por local' for r in OM if r['id'] == o['id'] and r['pos'] <= 3)]
    P('  buscas D+E', len(DE), 'com 3 primeiros todos por local', len(allloc))
    de_res = [r for r in OM if r['g'] in 'DE']
    P('  % local em D+E juntos', pct(sum(1 for r in de_res if r['tipo'] == 'página interna por local'), len(de_res)), '| so D', pct(sum(1 for r in OM if r['g'] == 'D' and r['tipo'] == 'página interna por local'), sum(1 for r in OM if r['g'] == 'D')))
    loc = [r for r in OM if r['tipo'] == 'página interna por local']
    um = [r for r in loc if len([x for x in r['path'].split('/') if x]) == 1]
    P('  paginas por local', len(loc), 'um nivel', len(um))
    dD = collections.defaultdict(set)
    for r in OM:
        if r['g'] == 'D': dD[r['dom']].add(r['id'])
    P('  dominios em 5+ das 20 buscas D:', sorted([(len(v), d) for d, v in dD.items() if len(v) >= 5], reverse=True))
    # cada vez com a pagina daquele bairro?
    P('  dominios com nome de bairro:', [(d, v) for d, v in dom.items() if re.search(r'dedetizadora(em|na|no|zona)', d)])
    P('  rentokil/orkin:', [(d, v, sorted({r["g"] for r in OM if r["dom"] == d})) for d, v in dom.items() if 'rentokil' in d or 'orkin' in d])
    P('-- 4.3 titulos')
    def cnt(f): return sum(1 for r in OM if f(r['tit'])), sum(1 for r in top3 if f(r['tit']))
    for nome, f in (('tel', lambda t: '[tel]' in t), ('24', lambda t: re.search(r'24\s?horas|24\s?h\b|24hs', t.lower()) is not None), ('preco', lambda t: 'preço' in t.lower() or 'a partir de' in t.lower()),
                    ('melhor', lambda t: 'melhor' in t.lower()), ('orcamento', lambda t: 'orçamento' in t.lower())):
        a, b = cnt(f); P('  ', nome, a, f'{100*a/n:.1f}%', b, f'{100*b/len(top3):.1f}%')
    P('-- 4.4')
    oh = [r for r in OM if r['dom'] == 'ohub.com.br']
    P('  ohub', len(oh), 'buscas', len({r['id'] for r in oh}), 'pos', sorted(r['pos'] for r in oh), 'mediana', statistics.median(r['pos'] for r in oh), 'paths', sorted({r['path'] for r in oh})[:6])
    for d in ('triider.com.br', 'reclameaqui.com.br', 'coteibem.com.br', 'pedegas.com', 'pestwase.com', 'listazn.com.br', 'getninjas.com.br', 'habitissimo.com.br', 'instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'sivisa.saude.sp.gov.br'):
        P('  ', d, dom[d], [(r['id'], byid[r['id']]['q']) for r in OM if r['dom'] == d][:3])
    P('  getninjas/habitissimo qualquer:', [d for d in dom if 'ninja' in d or 'habitis' in d])
    P('  social total', sum(1 for r in OM if r['tipo'] == 'rede social/fórum'))
    gov = [r for r in OM if r['tipo'] == 'governo/universidade']
    P('  gov', len(gov), C(byid[r['id']]['q'] for r in gov))
    P('  gov dominios', C(r['dom'] for r in gov))
    esc = [o for o in main if 'escorpi' in o['q']]
    P('  escorpiao', [(o['id'], o['q'], len(o['org']), sum(1 for r in OM if r['id'] == o['id'] and (r['tipo'] == 'governo/universidade' or 'butantan' in r['dom'])), [r['dom'] for r in OM if r['id'] == o['id']], len(o['pack'])) for o in esc])
    P('  outros sites de lista possiveis:', [d for d in dom if any(x in d for x in ('lista', 'guia', 'cotei', 'orcamento', 'melhores', 'apontador', 'telelista', 'solutudo', 'cronoshare', 'habitissimo'))])

def parse_pack(s):
    pat = s.startswith('Patrocinado ')
    nome = s[len('Patrocinado '):] if pat else s
    m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
    return dict(pat=pat, nome=(m.group(1) if m else nome).strip(), nota=float(m.group(2).replace(',', '.')) if m else None, av=int(m.group(3).replace('.', '')) if m else None, raw=s)

def bloco_mapa():
    P('== MAPA (secao 5) ==')
    L = [dict(parse_pack(s), id=o['id'], g=o['id'][0]) for o in main for s in o['pack']]
    np_ = [l for l in L if not l['pat']]
    P('linhas nao patrocinadas', len(np_), 'perfis distintos', len({l['nome'] for l in np_}), 'buscas com bloco', len({l['id'] for l in np_}))
    P('  distintos ignorando caixa', len({l['nome'].lower() for l in np_}))
    mc = C(l['nome'] for l in np_).most_common(8); P('  top', mc, '| top3', pct(sum(v for _, v in mc[:3]), len(np_)))
    P('  buscas por perfil (distintas)', [(n, len({l['id'] for l in np_ if l['nome'] == n})) for n, _ in mc[:6]])
    P('  ARMOR cidade', C(re.search(r'·\s*([^·]*?) - SP', l['raw']).group(1) if re.search(r'·\s*([^·]*?) - SP', l['raw']) else '-' for l in np_ if l['nome'].startswith('ARMOR')))
    D_ = [l for l in np_ if l['g'] == 'D']
    P('  grupo D: buscas com bloco', len({l['id'] for l in D_}), 'perfis distintos', len({l['nome'] for l in D_}), 'lideres', [(n, len({l['id'] for l in D_ if l['nome'] == n})) for n, _ in C(l['nome'] for l in D_).most_common(5)])
    DE_ = [l for l in np_ if l['g'] in 'DE']
    P('  grupos D+E: buscas com bloco', len({l['id'] for l in DE_}), 'perfis distintos', len({l['nome'] for l in DE_}))
    for g in 'ABFG':
        gg = [l for l in np_ if l['g'] == g]; P('   grupo', g, C(l['nome'] for l in gg).most_common(5))
    def cidade(raw):
        m = re.findall(r'([A-ZÀ-Ú][\wÀ-ú ]+?) - SP', raw); return m[-1].strip() if m else ''
    P('  cidade exibida', C(cidade(l['raw']) for l in np_))
    cn = [l for l in np_ if l['nota'] is not None]
    notas = [l['nota'] for l in cn]
    P('  linhas com nota', len(cn), 'mediana', statistics.median(notas), 'min', min(notas), '>=4.8', pct(sum(1 for x in notas if x >= 4.8), len(notas)), '| sem nota:', [l['raw'] for l in np_ if l['nota'] is None])
    por = {}
    for l in cn: por.setdefault(l['nome'], set()).add(l['av'])
    P('  perfis com numero lido', len(por), '| perfis com mais de um valor de avaliacoes', sum(1 for v in por.values() if len(v) > 1))
    for regra in ('max', 'min', 'primeiro'):
        if regra == 'primeiro':
            vals = []; seen = set()
            for l in cn:
                if l['nome'] not in seen: seen.add(l['nome']); vals.append(l['av'])
        else: vals = [(max if regra == 'max' else min)(v) for v in por.values()]
        q = statistics.quantiles(vals, n=4, method='inclusive')
        P('   ', regra, 'mediana', statistics.median(vals), 'q1,q3 incl', q[0], q[2], 'q excl', statistics.quantiles(vals, n=4)[0], statistics.quantiles(vals, n=4)[2], 'max', max(vals))
    P('  "1,1 mil":', [l['raw'] for l in np_ if 'mil' in l['raw']][:3])
    anos = [int(m.group(1)) for l in np_ for m in [re.search(r'(?:Mais de )?(\d+)\s?a(?:nos no mercado)?\b', l['raw'][len(l['nome']):])] if m]
    P('  anos no mercado: linhas', len(anos), 'min', min(anos), 'max', max(anos))
    nomes = sorted({l['nome'] for l in np_})
    serv = [n for n in nomes if re.search(r'dedetiza|controle de pragas|cupim|descupiniza|desratiza|pragas|desentup|dedet', sem_acento(n))]
    serv2 = [n for n in nomes if re.search(r'dedetizadora|dedetizacao|controle de pragas|cupim', sem_acento(n))]
    P('  nomes com palavra de servico (largo)', len(serv), '(estreito: dedetizadora/dedetizacao/controle de pragas/cupim)', len(serv2), 'de', len(nomes))
    P('  nomes SEM (estreito):', [n for n in nomes if n not in serv2])
    locn = [n for n in nomes if re.search(r'zona |24\s?h|sao paulo|\bsp\b|vila |moema|pinheiros|tatuape|santana|lapa|itaim|santo amaro|mooca|perdizes|higienopolis|butanta|ipiranga|penha|jabaquara|itaquera|campo limpo|bela vista|osasco|centro', sem_acento(n))]
    P('  nomes com local ou 24h (minha regra larga)', len(locn), locn)
    pats = [l for l in L if l['pat']]
    P('  patrocinados: linhas', len(pats), 'buscas', len({l['id'] for l in pats}), C((l['nome'], l['nota'], l['av']) for l in pats))

def bloco_ads():
    P('== ANUNCIOS (secao 6) ==')
    ads = [(o['id'], a) for o in main for a in o['ads']]
    P('anuncios', len(ads), 'em buscas', len({i for i, _ in ads}))
    P('  por dominio (anuncios)', C(a for _, a in ads).most_common())
    P('  por dominio (buscas)', [(d, len({i for i, a in ads if a == d})) for d in C(a for _, a in ads)])
    P('  sem anuncio nenhum', sum(1 for o in main if not o['ads'] and not any(p.startswith('Patrocinado') for p in o['pack'])))
    P('  brasiltechs texto OU google?', len({i for i, a in ads if a == 'brasiltechs.com'}))

def bloco_classes():
    P('== CLASSES (secao 7) ==')
    dom = C(r['dom'] for r in OM); t3 = C(r['dom'] for r in OM if r['pos'] <= 3); p1 = C(r['dom'] for r in OM if r['pos'] == 1)
    cons_ = collections.defaultdict(set)
    for r in OM: cons_[r['dom']].add(r['id'])
    P('serp_dominios.csv linhas', len(doms), '| dominios iguais ao recalculo?', {d['dominio'] for d in doms} == set(dom))
    bad = [d['dominio'] for d in doms if int(d['resultados_organicos']) != dom[d['dominio']] or int(d['consultas_em_que_aparece']) != len(cons_[d['dominio']]) or int(d['vezes_no_top3']) != t3[d['dominio']]]
    P('  contagens divergentes no csv de dominios', bad)
    ag = collections.defaultdict(lambda: [0, 0, 0, 0])
    for d in doms:
        c = d['classe']; n = d['dominio']; ag[c][0] += 1; ag[c][1] += dom[n]; ag[c][2] += t3[n]; ag[c][3] += p1[n]
    for c, v in sorted(ag.items(), key=lambda kv: -kv[1][1]): P('  ', c, v, f'{100*v[1]/709:.1f}% {100*v[2]/237:.1f}% {100*v[3]/79:.1f}%')
    P('  soma', [sum(v[k] for v in ag.values()) for k in range(4)])
    lidos = [d for d in doms if d['base_da_classe'].startswith('leitura')]
    P('  lidos (base leitura)', len(lidos), 'resultados', sum(dom[d['dominio']] for d in lidos), pct(sum(dom[d['dominio']] for d in lidos), 709))
    mc = dom.most_common()
    P('  os 77 mais frequentes == lidos?', {d for d, _ in mc[:77]} == {d['dominio'] for d in lidos}, '| freq do 77o e 78o', mc[76], mc[77], '| lidos com freq<=2:', [(d['dominio'], dom[d['dominio']]) for d in lidos if dom[d['dominio']] <= 2][:10], '| nao lidos com freq>=3:', [(d['dominio'], dom[d['dominio']], d['classe']) for d in doms if not d['base_da_classe'].startswith('leitura') and dom[d['dominio']] >= 3])
    P('  nao_classificado: freq', C(dom[d['dominio']] for d in doms if d['classe'] == 'nao_classificado'))
    serv = [d for d in lidos if d['classe_do_subagente'] not in ('nao_abriu', 'diretorio_marketplace', 'outro')]
    P('  sites de servico lidos', len(serv), 'licenca sim', sum(1 for d in serv if d['licenca_exibida'].strip().lower() == 'sim'), 'cnpj sim', sum(1 for d in serv if d['cnpj_exibido'].strip().lower() == 'sim'), C(d['licenca_exibida'] for d in serv))
    P('  classe x licenca_exibida', C((d['classe'], d['licenca_exibida']) for d in lidos))
    P('  licenca sim fora da classe com_numero:', [(d['dominio'], d['classe'], d['classe_do_subagente']) for d in doms if d['licenca_exibida'].strip().lower() == 'sim' and d['classe'] != 'empresa_com_numero_de_licenca'])
    P('  classe com_numero:', [(d['dominio'], dom[d['dominio']], p1[d['dominio']]) for d in doms if d['classe'] == 'empresa_com_numero_de_licenca'])
    P('  nao_abriu:', [d['dominio'] for d in doms if d['classe'] == 'nao_abriu'], '| outro:', [d['dominio'] for d in doms if d['classe'] == 'outro'], '| diretorio:', [d['dominio'] for d in doms if d['classe'] == 'diretorio_marketplace'])
    four = sum(ag[c][1] for c in ('empresa_com_numero_de_licenca', 'empresa_identificada_sem_numero_de_licenca', 'marca_sem_identificacao_vista', 'rede_ou_dominio_satelite'))
    P('  7.3.1 soma 4 classes', pct(four, 709), '| empresas identificadas (com+sem)', pct(ag['empresa_com_numero_de_licenca'][1] + ag['empresa_identificada_sem_numero_de_licenca'][1], 709), '| marca+satelite', ag['marca_sem_identificacao_vista'][0] + ag['rede_ou_dominio_satelite'][0], pct(ag['marca_sem_identificacao_vista'][1] + ag['rede_ou_dominio_satelite'][1], 709))
    # partes brutas
    cls = {}
    for f in sorted(glob.glob(D + '/serp_dominios_classe_parte*.csv')):
        for r in csv.DictReader(open(f, encoding='utf-8')): r['parte'] = f[-5]; cls[r['dominio'].strip()] = r
    P('  partes: total', len(cls), C(r['parte'] for r in cls.values()), '| fora do organico', [d for d in cls if d not in dom])
    sv = [d for d in cls if d in dom and cls[d]['classe'] not in ('nao_abriu', 'diretorio_marketplace', 'outro')]
    P('  servico lidos (partes)', len(sv), 'bairro sim', sum(1 for d in sv if cls[d]['paginas_por_bairro'].strip().lower() == 'sim'), 'whatsapp sim', sum(1 for d in sv if cls[d]['botao_whatsapp'].strip().lower() == 'sim'))
    P('  horas de leitura min/max', min(re.findall(r'\d\d:\d\d', ' '.join(r['hora_leitura'] for r in cls.values()))), max(re.findall(r'\d\d:\d\d', ' '.join(r['hora_leitura'] for r in cls.values()))))
    P('  "licenciada/legalizada" sem numero (campo tipo_de_licenca_citada nao vazio e licenca != sim):', sum(1 for d in sv if cls[d]['licenca_exibida'].strip().lower() != 'sim' and re.search(r'licenciad|legalizad|certificad', (cls[d]['tipo_de_licenca_citada'] + ' ' + cls[d]['observacao']).lower())))
    P('  71 sites lidos? (lidos menos nao_abriu)', len([d for d in cls if d in dom and cls[d]['classe'] != 'nao_abriu']), '| 24 horas em obs:', sum(1 for d in cls if d in dom and cls[d]['classe'] != 'nao_abriu' and re.search(r'24\s?h', (cls[d]['observacao'] + cls[d]['nome_exibido']).lower())))
    P('  desentupidora parte1:', sum(1 for d in cls if cls[d]['parte'] == '1' and 'desentup' in (' '.join(cls[d].values())).lower()), 'de', sum(1 for d in cls if cls[d]['parte'] == '1'))

def bloco_H():
    P('== GRUPO H (secao 12) ==')
    dm = C(r['dom'] for r in OM); clsd = {d['dominio']: d['classe'] for d in doms}
    for o in H:
        pat = sum(1 for p in o['pack'] if p.startswith('Patrocinado'))
        P(' ', o['id'], o['q'], '| nv', o['nv'], 'aio', o['aio'], 'ads', len(o['ads']), 'pack', len(o['pack']) - pat, '+', pat, 'org', len(o['org']), 'loc', o['loc'] or '-', '| 1o:', o['org'][0])
    P(' aio', sum(o['aio'] for o in H), 'pack', sum(1 for o in H if any(not p.startswith('Patrocinado') for p in o['pack'])), 'ads em', sum(1 for o in H if o['ads']), 'sem anuncio nenhum', sum(1 for o in H if not o['ads'] and not any(p.startswith('Patrocinado') for p in o['pack'])))
    ads = [a for o in H for a in o['ads']]; P(' anuncios', len(ads), C(ads).most_common())
    dh = C(r['dom'] for r in OH)
    novos = [d for d in dh if d not in dm]
    P(' organico', len(OH), 'dominios', len(dh), '| novos', len(novos), 'resultados de novos', sum(dh[d] for d in novos), pct(sum(dh[d] for d in novos), len(OH)))
    P(' tipo', C(r['tipo'] for r in OH).most_common()); P(' tipo no csv', C(r['tipo_pagina'] for r in rows if r['grupo'] == 'H' and r['superficie'] == 'orgânico').most_common())
    P(' main: local', sum(1 for r in OM if r['tipo'] == 'página interna por local'), pct(sum(1 for r in OM if r['tipo'] == 'página interna por local'), 709), '| H local', pct(sum(1 for r in OH if r['tipo'] == 'página interna por local'), len(OH)))
    def clH(d):
        if d in clsd and clsd[d] != 'nao_classificado': return clsd[d]
        if d.endswith('.gov.br') or d in ('gov.br', 'puspc.usp.br'): return 'governo_universidade'
        if d in SOCIAL: return 'rede_social_forum'
        if d in clsd: return 'nao_classificado(ja visto)'
        return 'novo_nao_lido'
    P(' classe', C(clH(r['dom']) for r in OH).most_common())
    P(' novos por classe:', C(clH(d) for d in novos), '| novos gov/social:', [d for d in novos if clH(d) != 'novo_nao_lido'])
    for nome, ids in (('confianca', ('H01', 'H02', 'H03')), ('preco', ('H04', 'H05', 'H10')), ('info', ('H06', 'H07', 'H08', 'H09'))):
        rr = [r for r in OH if r['id'] in ids]
        P('  ', nome, 'res', len(rr), 'anuncios', sum(len(byid[i]['ads']) for i in ids), C(clH(r['dom']) for r in rr).most_common())
        P('     gov:', [(r['id'], r['pos'], r['dom'], r['path'][:40]) for r in rr if clH(r['dom']) == 'governo_universidade'], '| dir:', [(r['id'], r['pos'], r['dom']) for r in rr if clH(r['dom']) == 'diretorio_marketplace'], '| social', [(r['id'], r['dom']) for r in rr if clH(r['dom']) == 'rede_social_forum'])
        P('     novos:', [(r['id'], r['pos'], r['dom']) for r in rr if clH(r['dom']) == 'novo_nao_lido'])
    s = [r for r in OH if r['dom'] == 'dedetizadora.srv.br']; P(' srv.br', len(s), 'buscas', len({r['id'] for r in s}), [(r['id'], r['pos'], r['path'], r['tit']) for r in s])
    for i in ('H02', 'H03', 'H04', 'H05', 'H10', 'H06', 'H07', 'H08', 'H09'):
        P('  --', i, byid[i]['q'])
        for r in OH:
            if r['id'] == i: P('      ', r['pos'], r['dom'] + r['path'], '|', r['tit'], '|', clH(r['dom']))
    P(' loc H', C(o['loc'] for o in H), '| H packs', [(o['id'], o['pack']) for o in H if o['pack']])
    P(' csv H linhas', sum(1 for r in rows if r['grupo'] == 'H'), C(r['superficie'] for r in rows if r['grupo'] == 'H'))

def bloco_rep():
    P('== REPETICOES (secao 13) ==')
    for o2 in rep:
        o1 = byid[o2['id'].rstrip('r')]
        d1 = [s.partition(' | ')[0].partition('/')[0] for s in o1['org']]; d2 = [s.partition(' | ')[0].partition('/')[0] for s in o2['org']]
        u1 = [s.partition(' | ')[0] for s in o1['org']]; u2 = [s.partition(' | ')[0] for s in o2['org']]
        p1 = [parse_pack(s) for s in o1['pack']]; p2 = [parse_pack(s) for s in o2['pack']]
        n1 = {p['nome'] for p in p1 if not p['pat']}; n2 = {p['nome'] for p in p2 if not p['pat']}
        P(' ', o2['id'], o2['q'], '| q igual', o1['q'] == o2['q'], '|', o1['nv'], '->', o2['nv'], f"(+{(seg(o2['nv'])-seg(o1['nv']))/3600:.2f} h)", '| lg', o1['lg'], o2['lg'])
        P('     1o igual (url)', u1[0] == u2[0], '(dominio)', d1[0] == d2[0], '| top3 dominios iguais em ordem', d1[:3] == d2[:3], 'como conjunto', set(d1[:3]) == set(d2[:3]))
        P('     dominios: 1a', len(d1), 'distintos', len(set(d1)), '| 2a', len(d2), 'distintos', len(set(d2)), '| em comum', len(set(d1) & set(d2)), '| urls em comum', len(set(u1) & set(u2)))
        P('     mapa em comum', len(n1 & n2), 'de', len(n1), len(n2), '| pat', sum(p['pat'] for p in p1), sum(p['pat'] for p in p2), '| loc', o1['loc'], '/', o2['loc'], '| ads', len(o1['ads']), '->', len(o2['ads']), o1['ads'], o2['ads'], '| aio', o1['aio'], o2['aio'])
    P(' rep ids em serp_sp.csv com hora da repeticao?', [r['id'] for r in rows if r['hora_navegacao'] in {o['nv'] for o in rep}][:3])
    P(' rep horas', [(o['id'], o['nv']) for o in rep])

def bloco_kw():
    P('== PALAVRAS-CHAVE (secao 10) ==')
    P('linhas', len(kw), 'colunas', list(kw[0].keys()))
    P(' volume', C(r['volume'] for r in kw)); P(' intencao', C(r['intencao'] for r in kw)); P(' origem', C(r['origem_do_termo'] for r in kw)); P(' situacao', C(r['situacao_na_coleta'] for r in kw))
    P(' praga', len(C(r['praga'] for r in kw)), C(r['praga'] for r in kw)); P(' tipo_local', C(r['tipo_local'] for r in kw)); P(' locais', len(C(r['local'] for r in kw)), C(r['local'] for r in kw).most_common(40)); P(' publico', C(r['publico'] for r in kw))
    t = C(r['termo'] for r in kw); P(' duplicados exatos', [(k, v) for k, v in t.items() if v > 1][:10], '| ignorando caixa/espacos', sum(1 for v in C(' '.join(r['termo'].lower().split()) for r in kw).values() if v > 1), '| ignorando acento', [(k, v) for k, v in C(sem_acento(' '.join(r['termo'].split())) for r in kw).items() if v > 1][:10])
    col = [r for r in kw if r['situacao_na_coleta'] == 'coletado']
    P(' coletados', len(col), '| ids', len({r['id_na_coleta'] for r in col}), '| termo == q do jsonl', sum(1 for r in col if byid.get(r['id_na_coleta'], {}).get('q', '').lower() == r['termo'].lower()), '| id vazio nos nao coletados', all(not r['id_na_coleta'] for r in kw if r['situacao_na_coleta'] != 'coletado'))
    P(' informativos sem local', sum(1 for r in kw if r['intencao'] == 'informativa'), C((r['tipo_local'], r['origem_do_termo'][:8]) for r in kw if r['intencao'] == 'informativa'))
    P(' vazios', {k: sum(1 for r in kw if not r[k].strip()) for k in kw[0]})
    P(' intencao x origem', C((r['intencao'], r['origem_do_termo'][:8]) for r in kw))

def bloco_tel():
    P('== TELEFONE ==')
    pat = re.compile(r'\(?\d{2}\)?\s?9?\d{4}[-\s]?\d{4}|0800')
    arqs = [D + '/serp_sp.csv', D + '/serp_dominios.csv', D + '/serp_consultas.csv', D + '/palavras_chave.csv', D + '/serp_dominios_classe_parte1.csv', D + '/serp_dominios_classe_parte2.csv',
            R + '/docs/mercado/serp_sp.md', R + '/docs/mercado/serp_sp_registro.md', R + '/docs/mercado/serp_sp_dominios.md', R + '/docs/mercado/_notas_dominios_parte1.md', R + '/docs/mercado/_notas_dominios_parte2.md'] + sorted(glob.glob(D + '/serp_raw/*'))
    for a in arqs:
        hits = []
        for n, l in enumerate(open(a, encoding='utf-8'), 1):
            for m in pat.finditer(l): hits.append((n, m.group(0), l[max(0, m.start() - 25):m.end() + 15].replace('\n', ' ')))
        P(' ', a.replace(R, ''), len(hits)); [P('      ', h) for h in hits[:12]]
    P(' [tel] ocorrencias em jsonl', sum(l.count('[tel]') for f in glob.glob(D + '/serp_raw/*.jsonl') for l in open(f, encoding='utf-8')))

B = dict(basico=bloco_basico, registro=bloco_registro, intervalos=bloco_intervalos, camadas=bloco_camadas, organico=bloco_organico, mapa=bloco_mapa, ads=bloco_ads, classes=bloco_classes, H=bloco_H, rep=bloco_rep, kw=bloco_kw, tel=bloco_tel)
for b in (sys.argv[1:] or list(B)): B[b]()
