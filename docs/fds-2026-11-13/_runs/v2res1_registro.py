#!/usr/bin/env python3
"""Segunda passada da reserva 1 — registro: bruto x CSV x registro .md x consultas; intervalos; contagem de buscas. Só leitura."""
import sys, os, re, collections, statistics
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2res1_comum import *

print('== contagem ==')
print('bruto ampliacao:', len(BRUTO), collections.Counter(o['_arq'] for o in BRUTO))
print('repeticao_02:', len(REP2), '| lotes item 4:', len(LOTES), '| repeticao_01:', len(REP1))
print('consultas planejadas:', len(CONS), collections.Counter(r['grupo'] for r in CONS))
print('ids unicos no bruto:', len({o['id'] for o in BRUTO}), '| ids do CSV:', len({r['id'] for r in CSVA}), '| linhas CSV:', len(CSVA))

# registro .md
reg = {}
for l in open(os.path.join(RAIZ, 'docs/mercado/serp_sp_ampliacao_registro.md'), encoding='utf-8'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 16 and re.fullmatch(r'[IJK]\d\d', c[0]):
        reg[c[0]] = c
print('linhas do registro .md:', len(reg))

print('== bruto x consultas x CSV x registro (termo, hora, local, logado, IA, contagens, pixels) ==')
falhas = 0
cons = {r['id']: r for r in CONS}
for o in BRUTO:
    i = o['id']; pr = []
    if cons[i]['termo'] != o['q']: pr.append(f"termo consultas={cons[i]['termo']!r} bruto={o['q']!r}")
    L = [r for r in CSVA if r['id'] == i]
    for campo, val in (('termo', o['q']), ('hora_navegacao', o['nv']), ('logado', 'sim' if o['lg'] else 'não'),
                       ('local_exibido', o['loc'] or 'não exibido'), ('visao_geral_ia', 'sim' if o['aio'] else 'não'),
                       ('data', '2026-11-14'), ('grupo', cons[i]['grupo'])):
        vs = {r[campo] for r in L}
        if vs != {val}: pr.append(f'CSV {campo}: {vs} != {val!r}')
    n_ad = sum(1 for r in L if r['superficie'] == 'anúncio'); n_org = sum(1 for r in L if r['superficie'] == 'orgânico')
    n_mp = sum(1 for r in L if r['superficie'] == 'mapa (bloco Empresas)'); n_pt = sum(1 for r in L if r['superficie'] == 'mapa (patrocinado)')
    pk = pack_do_bruto(o)
    if (n_ad, n_org, n_mp, n_pt) != (len(o['ads']), len(o['org']), sum(1 for p in pk if not p[0]), sum(1 for p in pk if p[0])):
        pr.append('contagem de linhas do CSV difere do bruto')
    # conteúdo orgânico
    ob = org_do_bruto(o); oc = [(int(r['posicao']), r['dominio'], r['caminho'], r['titulo_ou_nome']) for r in L if r['superficie'] == 'orgânico']
    if ob != oc: pr.append('orgânico do CSV difere do bruto')
    mb = [(p[1], p[2], p[3]) for p in pk if not p[0]]; mc = [(r['titulo_ou_nome'], r['nota'], r['avaliacoes']) for r in L if r['superficie'] == 'mapa (bloco Empresas)']
    if mb != mc: pr.append('bloco de mapa do CSV difere do bruto')
    ab = [h if (h and h != 'google.com') else 'não identificado' for h in o['ads']]; ac = [r['dominio'] for r in L if r['superficie'] == 'anúncio']
    if ab != ac: pr.append('anúncios do CSV diferem do bruto')
    # registro
    c = reg.get(i)
    if not c: pr.append('sem linha no registro')
    else:
        y = o['y']; px = lambda k: '—' if y.get(k) is None else str(y[k])
        npat = sum(1 for p in pk if p[0])
        esperado = [i, cons[i]['grupo_descricao'], o['q'], o['nv'], 'sim' if o['lg'] else 'não', o['loc'] or '—', 'sim' if o['aio'] else 'não',
                    str(len(o['ads'])), f"{len(pk) - npat}{' + 1' if npat else ''}", str(len(o['org'])), ordem(y), px('aio'), px('ad'), px('pack'), px('org'), o['_arq']]
        for a, b, nome in zip(c, esperado, 'id grupo termo hora logado local IA anuncios perfis organicos ordem IApx adpx mapapx orgpx lote'.split()):
            if a != b: pr.append(f'registro {nome}: {a!r} != {b!r}')
        if npat > 1: pr.append(f'{npat} patrocinados no bloco; o registro mostra "+ 1"')
    # coerência interna do bruto
    y = o['y']
    if bool(o['aio']) != (y.get('aio') is not None): pr.append('aio x y.aio incoerente')
    if bool(o['ads']) != (y.get('ad') is not None): pr.append('ads x y.ad incoerente')
    if bool(o['pack']) != (y.get('pack') is not None): pr.append('pack x y.pack incoerente')
    if bool(o['org']) != (y.get('org') is not None): pr.append('org x y.org incoerente')
    if y.get('h') != 945: pr.append(f"altura da janela {y.get('h')}")
    if seg(o['t']) < seg(o['nv']): pr.append('t antes de nv')
    if pr: falhas += 1; print(i, pr)
print('buscas com alguma divergência:', falhas, 'de', len(BRUTO))

print('== intervalos (hora da navegação, nv) ==')
B = sorted(BRUTO, key=lambda o: seg(o['nv']))
print('ordem do arquivo == ordem da hora:', [o['id'] for o in B] == [o['id'] for o in BRUTO])
iv = [(seg(b['nv']) - seg(a['nv']), a['id'], b['id']) for a, b in zip(B, B[1:])]
v = [x[0] for x in iv]
print('janela', B[0]['nv'], 'a', B[-1]['nv'], '| min', min(v), 'mediana', statistics.median(v), 'max', max(v), '| < 20 s:', sum(1 for x in v if x < 20))
print('menores:', sorted(iv)[:3], '| maiores:', sorted(iv)[-4:])
dl = [seg(o['t']) - seg(o['nv']) for o in BRUTO]
print('t - nv (segundos entre navegação e leitura): min', min(dl), 'max', max(dl), collections.Counter(dl).most_common())
# intervalo t(anterior) -> nv(seguinte)
iv2 = [seg(b['nv']) - seg(a['t']) for a, b in zip(B, B[1:])]
print('fim da leitura anterior -> navegação seguinte: min', min(iv2), 'max', max(iv2))
R = sorted(REP2, key=lambda o: seg(o['nv']))
ivr = [seg(b['nv']) - seg(a['nv']) for a, b in zip(R, R[1:])]
print('repetições:', [(o['id'], o['nv'], o['t']) for o in R], 'intervalos', ivr)
print('última da ampliação -> primeira repetição (s):', seg(R[0]['nv']) - seg(B[-1]['nv']))
print('t - nv nas repetições:', [seg(o['t']) - seg(o['nv']) for o in R])
r1 = sorted(REP1, key=lambda o: seg(o['nv']))
print('última busca de 13/11 no bruto (repeticao_01):', r1[-1]['id'], r1[-1]['nv'], '-> primeira de 14/11', B[0]['nv'], '=', 86400 - seg(r1[-1]['nv']) + seg(B[0]['nv']), 's')
print('logado:', sum(o['lg'] for o in BRUTO), '| local:', collections.Counter(o['loc'] or 'não exibido' for o in BRUTO))
print('local por id:', [(o['id'], o['loc']) for o in BRUTO if o['loc']])
print('minutos entre 1ª vez e repetição:')
bid = {o['id']: o for o in BRUTO}
for o in R:
    a = bid[o['id'][:-1]]
    print(' ', o['id'], a['nv'], '->', o['nv'], round((seg(o['nv']) - seg(a['nv'])) / 60, 1), 'min | termo igual:', a['q'] == o['q'])
print('total na rodada pelos brutos: lotes', len(LOTES), '+ rep1', len(REP1), '+ ampliacao', len(BRUTO), '+ rep2', len(REP2), '=', len(LOTES) + len(REP1) + len(BRUTO) + len(REP2))
