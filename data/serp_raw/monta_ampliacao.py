#!/usr/bin/env python3
"""Fila de reserva, tarefa 1 (ampliação da amostra de buscas, 14/11/2026).
Lê data/serp_consultas_ampliacao.csv e os lotes brutos data/serp_raw/ampliacao_*.jsonl e grava:
  - data/serp_sp_ampliacao.csv (uma linha por resultado visto, mesmas colunas de data/serp_sp.csv)
  - docs/mercado/serp_sp_ampliacao_registro.md (uma linha por busca: termo, hora, logado, local, camadas e posição vertical)
Só transforma o que foi coletado; não busca nada e não toca nos arquivos do item 4.
Compara com a amostra principal (grupos A a G de data/serp_sp.csv) e imprime as contas usadas em
docs/mercado/serp_sp_ampliacao.md. Uso: python3 data/serp_raw/monta_ampliacao.py"""
import csv, glob, json, re, unicodedata, collections, os, statistics
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(BASE)
DATA = '2026-11-14'
def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
# locais do script do item 4 + os 20 bairros novos (com as grafias vistas nos endereços)
LOCAIS = ['zona-leste', 'zona-norte', 'zona-oeste', 'zona-sul', 'centro', 'moema', 'pinheiros', 'vila-mariana', 'tatuape', 'santana', 'lapa',
          'itaim-bibi', 'santo-amaro', 'mooca', 'perdizes', 'santa-cecilia', 'higienopolis', 'butanta', 'ipiranga', 'penha', 'jabaquara',
          'itaquera', 'campo-limpo', 'bela-vista', 'vila-madalena', 'osasco', 'jardim-paulista', 'barra-funda', 'analia-franco',
          'brooklin', 'morumbi', 'saude', 'campo-belo', 'campo_belo', 'interlagos', 'capao-redondo', 'vila-prudente', 'sao-miguel',
          'sapopemba', 'guaianases', 'guaianazes', 'tucuruvi', 'pirituba', 'freguesia', 'casa-verde', 'vila-maria', 'vila-leopoldina',
          'jaguare', 'liberdade', 'consolacao', 'aclimacao']
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'tiktok.com', 'linkedin.com')
def tipo_pagina(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'governo/universidade'
    if host in SOCIAL: return 'rede social/fórum'
    if p in ('', '/'): return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog/artigo'
    if any(l in p for l in LOCAIS): return 'página interna por local'
    return 'página interna (serviço/outro)'
consultas = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, 'serp_consultas_ampliacao.csv'), encoding='utf-8'))}
recs = []
for f in sorted(glob.glob(os.path.join(BASE, 'serp_raw', 'ampliacao_*.jsonl'))):
    for l in open(f, encoding='utf-8'):
        if l.strip():
            o = json.loads(l); o['arquivo'] = os.path.basename(f); recs.append(o)
TEL = re.compile(r'\(?\d{2}\)?[\s-]?9?\d{4}[-\s]?\d{4}|0800')
for o in recs:
    assert not TEL.search(json.dumps(o, ensure_ascii=False)), ('telefone no bruto', o['id'])
    assert o['id'] in consultas and consultas[o['id']]['termo'].lower() == o['q'].lower(), ('termo', o['id'], o['q'])
assert len({o['id'] for o in recs}) == len(recs), 'id repetido'
linhas = []
for o in recs:
    c = consultas[o['id']]
    base = dict(id=o['id'], grupo=c['grupo'], termo=o['q'], data=DATA, hora_navegacao=o['nv'], logado='sim' if o['lg'] else 'não',
                local_exibido=o['loc'] or 'não exibido', visao_geral_ia='sim' if o['aio'] else 'não')
    for i, h in enumerate(o['ads'], 1):
        ok = h and h != 'google.com'
        linhas.append(dict(base, superficie='anúncio', posicao=i, dominio=h if ok else 'não identificado', caminho='',
                           titulo_ou_nome='', nota='', avaliacoes='', tipo_pagina='anúncio de texto'))
    pos = 0
    for s in o['pack']:
        pat = s.startswith('Patrocinado ')
        nome = s[len('Patrocinado '):] if pat else s
        m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
        if not pat: pos += 1
        linhas.append(dict(base, superficie='mapa (patrocinado)' if pat else 'mapa (bloco Empresas)', posicao='' if pat else pos,
                           dominio='', caminho='', titulo_ou_nome=(m.group(1) if m else nome).strip(),
                           nota=m.group(2) if m else '', avaliacoes=m.group(3).replace('.', '') if m else '', tipo_pagina='perfil de empresa'))
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | ')
        host, _, path = u.partition('/')
        linhas.append(dict(base, superficie='orgânico', posicao=i, dominio=host, caminho='/' + path, titulo_ou_nome=t.strip(),
                           nota='', avaliacoes='', tipo_pagina=tipo_pagina(host, '/' + path)))
campos = ['id', 'grupo', 'termo', 'data', 'hora_navegacao', 'logado', 'local_exibido', 'visao_geral_ia', 'superficie', 'posicao', 'dominio',
          'caminho', 'titulo_ou_nome', 'nota', 'avaliacoes', 'tipo_pagina']
with open(os.path.join(BASE, 'serp_sp_ampliacao.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader(); w.writerows(linhas)

# registro por busca, com a posição vertical (pixels a partir do topo da página; janela de y['h'] pixels de altura)
def camada_ordem(y):
    ks = [(v, k) for k, v in y.items() if k in ('aio', 'ad', 'pack', 'org') and v is not None]
    nome = {'aio': 'IA', 'ad': 'anúncio', 'pack': 'mapa', 'org': 'orgânico'}
    return ' > '.join(nome[k] for v, k in sorted(ks))
out = ['# Registro das buscas da ampliação — anexo de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`', '',
       'Gerado por `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py` a partir dos lotes brutos',
       '`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/ampliacao_*.jsonl`. Todas as buscas: Google (www.google.com), 14/11/2026 (sábado, madrugada),',
       'horário de Brasília, navegador pessoal do owner, parâmetros `hl=pt-BR&gl=br&pws=0`. "Local exibido" é o que o Google mostrou no bloco de mapa;',
       '"—" = a página não mostrou local. "Ordem na página" = ordem, de cima para baixo, do rótulo do resumo de IA, do primeiro anúncio de texto,',
       'do título do bloco "Empresas" e do primeiro resultado orgânico; os números são a distância do topo da página em pixels (janela de 945 pixels de altura).', '',
       '| id | grupo | termo (lido do título da página) | hora da navegação | logado | local exibido | IA | anúncios de texto | perfis no bloco (+ patrocinado) | orgânicos | ordem na página | IA (px) | 1º anúncio (px) | mapa (px) | 1º orgânico (px) | lote |',
       '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
rid = {o['id']: o for o in recs}
for i, c in consultas.items():
    o = rid.get(i)
    if not o:
        out.append(f"| {i} | {c['grupo_descricao']} | {c['termo']} | **não buscado** |" + ' — |' * 12); continue
    pat = sum(1 for p in o['pack'] if p.startswith('Patrocinado')); y = o.get('y', {})
    px = lambda k: '—' if y.get(k) is None else str(y[k])
    out.append(f"| {i} | {c['grupo_descricao']} | {o['q']} | {o['nv']} | {'sim' if o['lg'] else 'não'} | {o['loc'] or '—'} | {'sim' if o['aio'] else 'não'} | {len(o['ads'])} | "
               f"{len(o['pack']) - pat}{' + 1' if pat else ''} | {len(o['org'])} | {camada_ordem(y)} | {px('aio')} | {px('ad')} | {px('pack')} | {px('org')} | {o['arquivo']} |")
out += ['', f"Total: {len(recs)} buscas com registro, de {len(consultas)} planejadas."]
open(os.path.join(RAIZ, 'docs', 'mercado', 'serp_sp_ampliacao_registro.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

# ---------- contas ----------
P = print
pct = lambda a, b: f'{a} de {b} ({round(100 * a / b)}%)' if b else '0'
def seg(h): a, b, c = map(int, h.split(':')); return a * 3600 + b * 60 + c
P('buscas', len(recs), 'de', len(consultas), '| linhas', len(linhas), collections.Counter(l['superficie'] for l in linhas))
hs = sorted(seg(o['nv']) for o in recs); iv = [b - a for a, b in zip(hs, hs[1:])]
if iv: P('janela', min(o['nv'] for o in recs), 'a', max(o['nv'] for o in recs), '| intervalos: min', min(iv), 'mediana', statistics.median(iv), 'max', max(iv), '| abaixo de 20 s:', sum(1 for x in iv if x < 20))
P('logado', sum(o['lg'] for o in recs), '| local', collections.Counter(o['loc'] or 'não exibido' for o in recs))
principal = [r for r in csv.DictReader(open(os.path.join(BASE, 'serp_sp.csv'), encoding='utf-8')) if r['grupo'] not in ('H',)]
dom_ant = {r['dominio'] for r in csv.DictReader(open(os.path.join(BASE, 'serp_sp.csv'), encoding='utf-8')) if r['superficie'] == 'orgânico'}
dom_princ = collections.Counter(r['dominio'] for r in principal if r['superficie'] == 'orgânico')
perf_ant = {r['titulo_ou_nome'] for r in principal if r['superficie'] == 'mapa (bloco Empresas)'}
classes = {r['dominio']: r for r in csv.DictReader(open(os.path.join(BASE, 'serp_dominios.csv'), encoding='utf-8'))}
for g in sorted({c['grupo'] for c in consultas.values()}) + ['todos']:
    R = [o for o in recs if g == 'todos' or consultas[o['id']]['grupo'] == g]
    if not R: continue
    L = [l for l in linhas if g == 'todos' or l['grupo'] == g]
    org = [l for l in L if l['superficie'] == 'orgânico']
    P(f'--- grupo {g}: {len(R)} buscas')
    P('  IA', sum(o['aio'] for o in R), '| bloco', sum(1 for o in R if any(not p.startswith('Patrocinado') for p in o['pack'])),
      '| anúncio de texto', sum(1 for o in R if o['ads']), '| patrocinado no bloco', sum(1 for o in R if any(p.startswith('Patrocinado') for p in o['pack'])),
      '| sem anúncio nenhum', sum(1 for o in R if not o['ads'] and not any(p.startswith('Patrocinado') for p in o['pack'])))
    P('  sem IA:', [o['q'] for o in R if not o['aio']], '| sem bloco:', [o['q'] for o in R if not any(not p.startswith('Patrocinado') for p in o['pack'])])
    P('  orgânicos', len(org), '| domínios', len({l['dominio'] for l in org}), '| tipo:', [(k, pct(v, len(org))) for k, v in collections.Counter(l['tipo_pagina'] for l in org).most_common()])
    t3 = [l for l in org if l['posicao'] <= 3]
    P('  top3 tipo:', collections.Counter(l['tipo_pagina'] for l in t3).most_common())
    P('  buscas com os 3 primeiros todos por local:', sum(1 for o in R if len(o['org']) >= 3 and all(l['tipo_pagina'] == 'página interna por local' for l in org if l['id'] == o['id'] and l['posicao'] <= 3)))
    dc = collections.Counter(l['dominio'] for l in org)
    P('  domínios mais frequentes (resultados, top3):', [(d, n, sum(1 for l in t3 if l['dominio'] == d)) for d, n in dc.most_common(15)])
    P('  1ª posição:', collections.Counter(l['dominio'] for l in org if l['posicao'] == 1).most_common(8))
    novos = [d for d in dc if d not in dom_ant]
    P('  domínios novos (não vistos nas 89 buscas do item 4):', len(novos), 'de', len(dc), '| resultados deles:', pct(sum(dc[d] for d in novos), len(org)))
    P('   ', sorted(novos))
    cl = collections.Counter((classes[l['dominio']]['classe'] or 'não lido') if l['dominio'] in classes else ('novo (não lido)') for l in org)
    P('  classe (a do item 4, onde havia):', cl.most_common())
    P('  dos 10 domínios mais frequentes da amostra principal, presentes aqui:', [(d, dc.get(d, 0)) for d, _ in dom_princ.most_common(10)])
    mp = [l for l in L if l['superficie'] == 'mapa (bloco Empresas)']
    pc = collections.Counter(l['titulo_ou_nome'] for l in mp)
    P('  mapa: linhas', len(mp), '| perfis distintos', len(pc), '| novos (não vistos na amostra principal)', sum(1 for p in pc if p not in perf_ant), '| mais frequentes:', pc.most_common(8))
    notas = [float(l['nota'].replace(',', '.')) for l in mp if l['nota']]
    if notas: P('  nota: lidas', len(notas), 'mediana', statistics.median(notas), 'mín', min(notas), '| 4,8 ou mais:', pct(sum(1 for n in notas if n >= 4.8), len(notas)))
    av = {}
    for l in mp:
        if l['avaliacoes'].isdigit(): av[l['titulo_ou_nome']] = int(l['avaliacoes'])
    if av: P('  avaliações por perfil: lidos', len(av), 'mediana', statistics.median(av.values()), 'mín', min(av.values()), 'máx', max(av.values()))
    ad = collections.Counter(l['dominio'] for l in L if l['superficie'] == 'anúncio')
    P('  anúncios de texto:', sum(ad.values()), ad.most_common(), '| buscas com brasiltechs.com:', sum(1 for o in R if 'brasiltechs.com' in o['ads']))
    P('  patrocinado no bloco:', collections.Counter(l['titulo_ou_nome'] for l in L if l['superficie'] == 'mapa (patrocinado)').most_common(3))
    # posição vertical
    ys = [o['y'] for o in R if o.get('y') and 'erro' not in o['y']]
    P('  ordem na página:', collections.Counter(camada_ordem(y) for y in ys).most_common())
    prim = collections.Counter(camada_ordem(y).split(' > ')[0] for y in ys); P('  primeira camada:', prim.most_common())
    for k, nome in (('aio', 'IA'), ('ad', 'anúncio'), ('pack', 'mapa'), ('org', 'orgânico')):
        v = [y[k] for y in ys if y.get(k) is not None]
        if v: P(f'  {nome}: n={len(v)} mediana={statistics.median(v)} mín={min(v)} máx={max(v)} | dentro da primeira tela (< altura da janela): {sum(1 for y in ys if y.get(k) is not None and y[k] < y["h"])}')
    P('  1º orgânico abaixo da primeira tela:', sum(1 for y in ys if y.get('org') is not None and y['org'] >= y['h']), 'de', len(ys),
      '| abaixo de duas telas:', sum(1 for y in ys if y.get('org') is not None and y['org'] >= 2 * y['h']))
    P('  anúncio de texto acima do 1º orgânico:', sum(1 for y in ys if y.get('ad') is not None and y.get('org') is not None and y['ad'] < y['org']), 'de', sum(1 for y in ys if y.get('ad') is not None),
      '| mapa acima do 1º orgânico:', sum(1 for y in ys if y.get('pack') is not None and y.get('org') is not None and y['pack'] < y['org']), 'de', sum(1 for y in ys if y.get('pack') is not None),
      '| IA acima do 1º orgânico:', sum(1 for y in ys if y.get('aio') is not None and y.get('org') is not None and y['aio'] < y['org']), 'de', sum(1 for y in ys if y.get('aio') is not None))
