#!/usr/bin/env python3
"""Monta data/serp_sp.csv (uma linha por resultado visto) a partir dos lotes brutos em data/serp_raw/lote_*.jsonl.
Só transforma o que foi coletado; não busca nada. Uso: python3 data/serp_raw/monta_csv.py"""
import csv, glob, json, re, unicodedata, collections, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
consultas = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, 'serp_consultas.csv'), encoding='utf-8'))}
def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
LOCAIS = ['zona-leste','zona-norte','zona-oeste','zona-sul','centro','moema','pinheiros','vila-mariana','tatuape','santana','lapa',
          'itaim-bibi','santo-amaro','mooca','perdizes','santa-cecilia','higienopolis','butanta','ipiranga','penha','jabaquara',
          'itaquera','campo-limpo','bela-vista','vila-madalena','osasco','jardim-paulista','barra-funda','analia-franco']
SOCIAL = ('instagram.com','facebook.com','reddit.com','youtube.com','tiktok.com','linkedin.com')
def tipo_pagina(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('puspc.usp.br',): return 'governo/universidade'
    if host in SOCIAL: return 'rede social/fórum'
    if p in ('', '/'): return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog/artigo'
    if any(l in p for l in LOCAIS): return 'página interna por local'
    return 'página interna (serviço/outro)'
linhas = []
for f in sorted(glob.glob(os.path.join(BASE, 'serp_raw', 'lote_*.jsonl'))):
    for l in open(f, encoding='utf-8'):
        o = json.loads(l); c = consultas.get(o['id'], {})
        base = dict(id=o['id'], grupo=c.get('grupo', o['id'][0]), termo=o['q'], data='2026-11-13', hora_navegacao=o['nv'],
                    logado='sim' if o['lg'] else 'não', local_exibido=o['loc'] or 'não exibido',
                    visao_geral_ia='sim' if o['aio'] else 'não')
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
                               nota=m.group(2) if m else '', avaliacoes=m.group(3).replace('.', '') if m else '',
                               tipo_pagina='perfil de empresa'))
        for i, s in enumerate(o['org'], 1):
            u, _, t = s.partition(' | ')
            host, _, path = u.partition('/')
            linhas.append(dict(base, superficie='orgânico', posicao=i, dominio=host, caminho='/' + path, titulo_ou_nome=t.strip(),
                               nota='', avaliacoes='', tipo_pagina=tipo_pagina(host, '/' + path)))
campos = ['id','grupo','termo','data','hora_navegacao','logado','local_exibido','visao_geral_ia','superficie','posicao','dominio',
          'caminho','titulo_ou_nome','nota','avaliacoes','tipo_pagina']
with open(os.path.join(BASE, 'serp_sp.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader(); w.writerows(linhas)
org = [l for l in linhas if l['superficie'] == 'orgânico']
dom = collections.Counter(); top3 = collections.Counter(); cons = collections.defaultdict(set)
for l in org:
    dom[l['dominio']] += 1; cons[l['dominio']].add(l['id'])
    if l['posicao'] <= 3: top3[l['dominio']] += 1
with open(os.path.join(BASE, 'serp_dominios.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['dominio','resultados_organicos','consultas_em_que_aparece','vezes_no_top3','classe','base_da_classe'])
    for d, n in dom.most_common(): w.writerow([d, n, len(cons[d]), top3[d], '', ''])
print('linhas', len(linhas), '| orgânicos', len(org), '| domínios', len(dom), '| consultas', len({l['id'] for l in linhas}))
print('tipo de página (orgânico):', collections.Counter(l['tipo_pagina'] for l in org).most_common())
print('top 45 domínios (resultados, consultas, top3):')
for d, n in dom.most_common(45): print(f'  {d}: {n}, {len(cons[d])}, {top3[d]}')
pk = collections.Counter(l['titulo_ou_nome'] for l in linhas if l['superficie'] == 'mapa (bloco Empresas)')
print('perfis distintos no bloco Empresas:', len(pk)); print(pk.most_common(25))
ad = collections.Counter(l['dominio'] for l in linhas if l['superficie'] == 'anúncio'); print('anúncios:', ad.most_common())
print('mapa patrocinado:', collections.Counter(l['titulo_ou_nome'] for l in linhas if l['superficie']=='mapa (patrocinado)').most_common(3))
