#!/usr/bin/env python3
"""Verificação da reserva 1 — registro, plano, intervalos, CSV × brutos (só leitura)."""
import re, os, sys, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verif_reserva1_base import *

P = print
P('== plano x brutos')
ids_plano = [r['id'] for r in CONSULTAS]
ids_raw = [o['id'] for o in RECS]
P('planejadas', len(ids_plano), '| brutos', len(ids_raw), '| ids distintos nos brutos', len(set(ids_raw)))
P('planejada sem bruto:', sorted(set(ids_plano) - set(ids_raw)), '| bruto fora do plano:', sorted(set(ids_raw) - set(ids_plano)))
P('termo do plano != termo lido (q):', [(o['id'], CONS[o['id']]['termo'], o['q']) for o in RECS if o['id'] in CONS and CONS[o['id']]['termo'] != o['q']])
P('por arquivo:', collections.Counter(o['arquivo'] for o in RECS))
P('por grupo (plano):', collections.Counter(r['grupo'] for r in CONSULTAS))

P('\n== registro .md x brutos')
reg = {}
for l in open(os.path.join(RAIZ, 'docs/mercado/serp_sp_ampliacao_registro.md'), encoding='utf-8'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 16 and re.match(r'^[IJK]\d\d$', c[0]):
        reg[c[0]] = c
P('linhas de busca no registro:', len(reg), '| ids fora do plano:', sorted(set(reg) - set(ids_plano)), '| plano sem registro:', sorted(set(ids_plano) - set(reg)))
erros = []
nome = {'aio': 'IA', 'ad': 'anúncio', 'pack': 'mapa', 'org': 'orgânico'}
for o in RECS:
    c = reg[o['id']]
    po, pp = pack_de(o)
    y = o['y']
    ordem = ' > '.join(nome[k] for v, k in sorted((v, k) for k, v in y.items() if k in nome and v is not None))
    px = lambda k: '—' if y.get(k) is None else str(y[k])
    esperado = [o['id'], CONS[o['id']]['grupo_descricao'], o['q'], o['nv'], 'sim' if o['lg'] else 'não', o['loc'] or '—', 'sim' if o['aio'] else 'não',
                str(len(o['ads'])), f"{len(po)}{' + 1' if pp else ''}", str(len(o['org'])), ordem, px('aio'), px('ad'), px('pack'), px('org'), o['arquivo']]
    for i, (a, b) in enumerate(zip(c, esperado)):
        if a != b:
            erros.append((o['id'], i, a, b))
    if len(pp) > 1:
        erros.append((o['id'], 'mais de um patrocinado', len(pp)))
P('divergências registro x bruto:', erros or 'nenhuma (16 colunas x 40 linhas)')

P('\n== CSV x brutos')
porid = collections.defaultdict(list)
for r in CSV_AMP:
    porid[r['id']].append(r)
P('linhas CSV', len(CSV_AMP), '| superfícies', dict(collections.Counter(r['superficie'] for r in CSV_AMP)), '| ids', len(porid))
e2 = []
for o in RECS:
    rs = porid[o['id']]
    po, pp = pack_de(o)
    for r in rs:
        if (r['termo'], r['hora_navegacao'], r['logado'], r['local_exibido'], r['visao_geral_ia'], r['grupo'], r['data']) != \
           (o['q'], o['nv'], 'sim' if o['lg'] else 'não', o['loc'] or 'não exibido', 'sim' if o['aio'] else 'não', o['id'][0], '2026-11-14'):
            e2.append((o['id'], 'cabecalho', r))
    n = collections.Counter(r['superficie'] for r in rs)
    if (n['anúncio'], n['mapa (bloco Empresas)'], n['mapa (patrocinado)'], n['orgânico']) != (len(o['ads']), len(po), len(pp), len(o['org'])):
        e2.append((o['id'], 'contagem', dict(n)))
    mo = org_de(o)
    co = [r for r in rs if r['superficie'] == 'orgânico']
    for a, b in zip(mo, co):
        if (str(a['pos']), a['dominio'], a['caminho'], a['titulo'], a['tipo']) != (b['posicao'], b['dominio'], b['caminho'], b['titulo_ou_nome'], b['tipo_pagina']):
            e2.append((o['id'], 'org', a, b))
    cm = [(r['titulo_ou_nome'], r['nota'], r['avaliacoes']) for r in rs if r['superficie'] == 'mapa (bloco Empresas)']
    if cm != po:
        e2.append((o['id'], 'mapa', cm, po))
    ca = [r['dominio'] for r in rs if r['superficie'] == 'anúncio']
    if ca != [h if (h and h != 'google.com') else 'não identificado' for h in o['ads']]:
        e2.append((o['id'], 'ads', ca, o['ads']))
P('divergências CSV x bruto:', e2 or 'nenhuma')
P('colunas iguais às de serp_sp.csv:', list(CSV_AMP[0].keys()) == list(CSV_PRI[0].keys()))

P('\n== intervalos (nv), 40 buscas')
hs = [(seg(o['nv']), o['id']) for o in RECS]
P('ordem dos brutos = ordem cronológica:', hs == sorted(hs))
hs.sort()
iv = [(b[0] - a[0], a[1], b[1]) for a, b in zip(hs, hs[1:])]
v = [x[0] for x in iv]
P('primeira', RECS[0]['nv'], 'última', max(o['nv'] for o in RECS), '| n intervalos', len(v), '| min', min(v), 'mediana', statistics.median(v), 'max', max(v), '| <20s:', [x for x in iv if x[0] < 20])
P('menores:', sorted(iv)[:3], '| maiores:', sorted(iv)[-3:])
P('t - nv (segundos entre navegação e coleta): min', min(seg(o['t']) - seg(o['nv']) for o in RECS), 'max', max(seg(o['t']) - seg(o['nv']) for o in RECS))
P('logado:', sum(o['lg'] for o in RECS), 'de', len(RECS), '| local:', dict(collections.Counter(o['loc'] or 'nenhuma' for o in RECS)))
P('altura da janela (h):', collections.Counter(o['y'].get('h') for o in RECS), '| y com erro:', [o['id'] for o in RECS if 'erro' in o['y']])

P('\n== repetições')
hr = [(seg(o['nv']), o['id']) for o in REP]
P([(o['id'], o['q'], o['nv'], o['t'], o['lg'], o['loc']) for o in REP])
ivr = [b[0] - a[0] for a, b in zip(hr, hr[1:])]
P('intervalos entre repetições:', ivr, '| da última das 40 (', hs[-1], ') à 1ª repetição:', hr[0][0] - hs[-1][0], 's')
todas = sorted(hs + hr)
ivt = [b[0] - a[0] for a, b in zip(todas, todas[1:])]
P('45 buscas em sequência: min', min(ivt), 'max', max(ivt), '| <20s:', sum(1 for x in ivt if x < 20))
P('total de buscas desta tarefa:', len(RECS) + len(REP))
# buscas do item 4, para o total da rodada
import glob
n4 = sum(1 for f in glob.glob(os.path.join(RAW, 'lote_*.jsonl')) for l in open(f, encoding='utf-8') if l.strip())
nr1 = sum(1 for l in open(os.path.join(RAW, 'repeticao_01.jsonl'), encoding='utf-8') if l.strip())
P('registros brutos do item 4: lotes', n4, '| repeticao_01', nr1, '| soma com esta tarefa (só registros válidos):', n4 + nr1 + len(RECS) + len(REP))
