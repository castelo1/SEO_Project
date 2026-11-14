#!/usr/bin/env python3
"""Segunda passada do item 4 — confere o registro (89 buscas) entre .jsonl, CSV e registro.md. SÓ LEITURA."""
import sys, os, re, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2item4_comum import *

recs = lotes(); cons = consultas(); rows = serp_csv()
print('registros nos lotes:', len(recs), '| ids distintos:', len({o['id'] for o in recs}), '| consultas planejadas:', len(cons))
print('por lote:', collections.Counter(o['arquivo'] for o in recs))
byid = {o['id']: o for o in recs}
cid = {c['id']: c for c in cons}
print('ids planejados sem registro:', [c['id'] for c in cons if c['id'] not in byid])
print('ids com registro fora do plano:', [i for i in byid if i not in cid])
dif = [(i, cid[i]['termo'], byid[i]['q']) for i in byid if cid[i]['termo'] != byid[i]['q']]
print('termo planejado != título lido (exato):', dif)
print('grupos planejados:', collections.Counter(c['grupo'] for c in cons))

# CSV x jsonl
csvid = collections.defaultdict(list)
for r in rows: csvid[r['id']].append(r)
print('linhas CSV:', len(rows), '| ids no CSV:', len(csvid), '| linhas A-G:', sum(1 for r in rows if r['grupo'] != 'H'), '| H:', sum(1 for r in rows if r['grupo'] == 'H'))
erros = 0
for i, o in byid.items():
    rs = csvid.get(i, [])
    esperado = len(o['ads']) + len(o['pack']) + len(o['org'])
    if len(rs) != esperado: print('  N LINHAS DIFERE', i, len(rs), esperado); erros += 1
    for r in rs:
        if r['termo'] != o['q'] or r['hora_navegacao'] != o['nv'] or r['logado'] != ('sim' if o['lg'] else 'não') or \
           r['local_exibido'] != (o['loc'] or 'não exibido') or r['visao_geral_ia'] != ('sim' if o['aio'] else 'não') or r['data'] != '2026-11-13' or r['grupo'] != i[0]:
            print('  CAMPO DIFERE', i, r); erros += 1; break
    # orgânico: domínio, caminho, título, tipo
    ro = [r for r in rs if r['superficie'] == 'orgânico']
    for (p, h, pa, t), r in zip(org_de(o), ro):
        if str(p) != r['posicao'] or h != r['dominio'] or pa != r['caminho'] or t != r['titulo_ou_nome'] or tipo_pagina(h, pa) != r['tipo_pagina']:
            print('  ORG DIFERE', i, p, h, pa, t, '|', r['posicao'], r['dominio'], r['caminho'], r['titulo_ou_nome'], r['tipo_pagina']); erros += 1
    rp = [r for r in rs if r['superficie'].startswith('mapa')]
    for pk, r in zip(pack_de(o), rp):
        if pk['nome'] != r['titulo_ou_nome'] or pk['nota'] != r['nota'] or pk['aval'] != r['avaliacoes'] or (pk['pat'] != (r['superficie'] == 'mapa (patrocinado)')):
            print('  MAPA DIFERE', i, pk, r); erros += 1
    ra = [r for r in rs if r['superficie'] == 'anúncio']
    for h, r in zip(o['ads'], ra):
        e = h if (h and h != 'google.com') else 'não identificado'
        if e != r['dominio']: print('  AD DIFERE', i, h, r['dominio']); erros += 1
print('divergências CSV x jsonl:', erros)

# registro.md x jsonl
reg = {}
for l in open(os.path.join(RAIZ, 'docs/mercado/serp_sp_registro.md'), encoding='utf-8'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 11 and re.match(r'^[A-H]\d\d$', c[0]): reg[c[0]] = c
print('linhas no registro.md:', len(reg))
e2 = 0
for i, o in byid.items():
    c = reg.get(i)
    if not c: print('  SEM LINHA NO REGISTRO', i); e2 += 1; continue
    pat = sum(1 for p in o['pack'] if p.startswith('Patrocinado'))
    esp = [i, cid[i]['grupo_descricao'], o['q'], o['nv'], 'sim' if o['lg'] else 'não', o['loc'] or '—', 'sim' if o['aio'] else 'não', str(len(o['ads'])),
           f"{len(o['pack']) - pat}{' + 1' if pat else ''}", str(len(o['org'])), o['arquivo']]
    if esp != c: print('  REGISTRO DIFERE', esp, c); e2 += 1
print('divergências registro.md x jsonl:', e2)

# logado, local
print('logado:', collections.Counter(o['lg'] for o in recs))
ag = [o for o in recs if o['id'][0] != 'H']; h = [o for o in recs if o['id'][0] == 'H']
print('local A-G:', collections.Counter(o['loc'] or '(nenhum)' for o in ag))
print('local H:', collections.Counter(o['loc'] or '(nenhum)' for o in h))

# intervalos por nv
ordem = sorted(recs, key=lambda o: seg(o['nv']))
print('primeira nv', ordem[0]['id'], ordem[0]['nv'], '| última A-G', max(ag, key=lambda o: seg(o['nv']))['nv'], max(ag, key=lambda o: seg(o['t']))['t'],
      '| H:', min(h, key=lambda o: seg(o['nv']))['nv'], max(h, key=lambda o: seg(o['nv']))['nv'], max(h, key=lambda o: seg(o['t']))['t'])
print('ordem por nv == ordem do arquivo?', [o['id'] for o in ordem] == [o['id'] for o in recs])
agord = sorted(ag, key=lambda o: seg(o['nv']))
ints = [(agord[k]['id'], agord[k + 1]['id'], seg(agord[k + 1]['nv']) - seg(agord[k]['nv'])) for k in range(len(agord) - 1)]
d = [x[2] for x in ints]
print('A-G: n intervalos', len(d), 'mediana', statistics.median(d), 'min', min(d), 'max', max(d))
print('A-G abaixo de 20 s:', [x for x in ints if x[2] < 20])
print('A-G intervalos >= 60 s:', [x for x in ints if x[2] >= 60])
rep = repeticao()
seq2 = sorted(h + rep, key=lambda o: seg(o['nv']))
i2 = [(seq2[k]['id'], seq2[k + 1]['id'], seg(seq2[k + 1]['nv']) - seg(seq2[k]['nv'])) for k in range(len(seq2) - 1)]
print('2ª janela (H + repetições): n', len(i2), 'min', min(x[2] for x in i2), 'max', max(x[2] for x in i2), 'mediana', statistics.median([x[2] for x in i2]))
print('2ª janela detalhes:', i2)
todos = sorted(recs + rep, key=lambda o: seg(o['nv']))
print('buscas com nv entre 21:16:00 e 23:18:00:', [(o['id'], o['nv']) for o in todos if seg('21:16:00') < seg(o['nv']) < seg('23:18:00')])
print('última nv antes da pausa:', [(o['id'], o['nv'], o['t']) for o in agord[-2:]], '| primeira depois:', [(o['id'], o['nv']) for o in seq2[:2]])
print('repetições:', [(o['id'], o['q'], o['nv'], o['t'], o['lg'], o['loc']) for o in rep])
# nv vs t: tempo dentro de cada busca; t(k) <= nv(k+1)?
neg = [(todos[k]['id'], todos[k]['t'], todos[k + 1]['id'], todos[k + 1]['nv']) for k in range(len(todos) - 1) if seg(todos[k]['t']) > seg(todos[k + 1]['nv'])]
print('casos em que a leitura (t) de uma busca é posterior à navegação da seguinte:', neg)
# pausas longas
print('pausa longa mais recente antes de 21:16 (intervalo >= 60 s):', [x for x in ints if x[2] >= 60][-1])
# chaves presentes
print('chaves por lote:', {a: sorted(set().union(*[set(o.keys()) for o in recs if o['arquivo'] == a])) for a in sorted({o['arquivo'] for o in recs})})
