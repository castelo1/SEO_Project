#!/usr/bin/env python3
"""Segunda passada da reserva 1 — mapa de termos (data/palavras_chave.csv). Só leitura; não roda gera_palavras_chave.py (ele grava)."""
import sys, os, re, collections, random
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2res1_comum import *
C = collections.Counter
PK = le_csv('palavras_chave.csv')
print('linhas', len(PK), '| colunas', list(PK[0].keys()))
t = [r['termo'] for r in PK]
print('duplicado exato:', [k for k, v in C(t).items() if v > 1])
norm = lambda s: ' '.join(sem_acento(s).split())
dn = collections.defaultdict(list)
for x in t: dn[norm(x)].append(x)
print('duplicado sem acento/caixa/espaço:', [v for v in dn.values() if len(v) > 1])
print('termo vazio ou com espaço duplo/ponta:', [x for x in t if not x or x != ' '.join(x.split())])
print('volume:', C(r['volume'] for r in PK))
print('intencao:', C(r['intencao'] for r in PK).most_common())
print('tipo_local:', C(r['tipo_local'] for r in PK).most_common())
print('praga:', C(r['praga'] for r in PK).most_common())
print('publico:', C(r['publico'] for r in PK).most_common())
print('situacao:', C(r['situacao_na_coleta'] for r in PK), '| origem:', C(r['origem_do_termo'] for r in PK))
print('locais distintos por tipo:', {k: len({r['local'] for r in PK if r['tipo_local'] == k}) for k in ('cidade', 'zona', 'bairro', 'sem local')})
print('bairros:', sorted({r['local'] for r in PK if r['tipo_local'] == 'bairro'}))
print('pragas x serviço nas combinações geradas:', len({r['praga'] for r in PK if r['origem_do_termo'] == 'combinação gerada'}))
# termos coletados marcados
cons = {r['termo'].lower(): r['id'] for r in CONS4 + CONS}
print('consultas das duas coletas:', len(CONS4), '+', len(CONS), '=', len(CONS4) + len(CONS), '| termos distintos (minúsculas):', len(cons))
brutos = {o['q'].lower(): o['id'] for o in LOTES + BRUTO}
pk = {r['termo']: r for r in PK}
falta = [q for q in brutos if q not in pk]; print('termos buscados (bruto) ausentes do mapa:', falta)
errado = [(q, i, pk[q]['id_na_coleta'], pk[q]['situacao_na_coleta']) for q, i in brutos.items() if q in pk and (pk[q]['id_na_coleta'] != i or pk[q]['situacao_na_coleta'] != 'coletado')]
print('termos buscados com id ou situação errados no mapa:', errado)
print('marcados como coletado sem estar no bruto:', [r['termo'] for r in PK if r['situacao_na_coleta'] == 'coletado' and r['termo'] not in brutos])
print('coletados:', sum(1 for r in PK if r['situacao_na_coleta'] == 'coletado'), '| da ampliação (I, J, K):', sum(1 for r in PK if r['id_na_coleta'][:1] in 'IJK' and r['id_na_coleta']),
      '| origem 14/11:', sum(1 for r in PK if '14/11' in r['origem_do_termo']))
print('ordem das datas na origem x id:', C((r['origem_do_termo'], r['id_na_coleta'][:1]) for r in PK if r['id_na_coleta']).most_common())
# conta esperada da grade
print('grade esperada: 18 x 46 x 3 =', 18 * 46 * 3, '+ confiança 3 x 46 =', 3 * 46, '+ público 5 x 6 =', 30, '+ informativas 21 -> total', 18 * 46 * 3 + 138 + 30 + 21,
      '| geradas no arquivo:', sum(1 for r in PK if r['origem_do_termo'] == 'combinação gerada'))
print('informativas sem local:', sum(1 for r in PK if r['intencao'] == 'informativa'), '| sem local:', [(r['termo'], r['intencao'], r['id_na_coleta']) for r in PK if r['tipo_local'] == 'sem local' and r['intencao'] != 'informativa'])
print('\n== as 40 consultas da ampliação no mapa ==')
for r in PK:
    if r['id_na_coleta'][:1] in ('I', 'J', 'K'): print(r['id_na_coleta'], '|', r['termo'], '|', r['praga'], '|', r['tipo_local'], '|', r['local'], '|', r['intencao'], '|', r['publico'], '|', r['situacao_na_coleta'])
print('\n== coerência mecânica das combinações geradas (local contido no termo; praga coerente) ==')
ruins = []
CH = {'baratas': ['barata'], 'ratos': ['desratiza', 'rato'], 'cupim': ['cupim', 'descupiniza'], 'formigas': ['formiga'], 'pulgas': ['pulga'], 'percevejo': ['percevejo'],
      'escorpião': ['escorpi'], 'pombos': ['pombo'], 'mosquito': ['mosquito', 'dengue', 'fumacê'], 'carrapatos': ['carrapato'], 'aranhas': ['aranha'], 'traças': ['traça'],
      'morcegos': ['morcego'], 'moscas': ['mosca'], 'lacraias': ['lacraia'], 'marimbondos': ['marimbondo'], 'brocas': ['broca']}
for r in PK:
    tt = r['termo']
    if r['local'] and r['local'] not in tt and not (r['local'] == 'são paulo' and (tt.endswith(' sp') or ' sp ' in tt)): ruins.append(('local fora do termo', tt, r['local']))
    if r['tipo_local'] == 'sem local' and r['local']: ruins.append(('sem local com local', tt))
    pr = [p for p, ks in CH.items() if any(k in tt for k in ks)]
    if r['praga'] == 'geral' and pr: ruins.append(('geral com praga no termo', tt, pr))
    if r['praga'] != 'geral' and r['praga'] not in pr: ruins.append(('praga não está no termo', tt, r['praga'], pr))
    if len(pr) > 1: ruins.append(('mais de uma praga no termo', tt, r['praga'], pr))
    i = r['intencao']
    urg = any(k in tt for k in ('urgente', '24h', '24 horas', 'hoje', 'emergencial', 'aberta agora')); pre = any(k in tt for k in ('preço', 'orçamento', 'quanto custa'))
    if (i == 'urgência') != urg and not (urg and i != 'urgência' and False): ruins.append(('urgência incoerente', tt, i))
    if i == 'preço' and not pre: ruins.append(('preço sem palavra de preço', tt))
    if pre and i not in ('preço', 'urgência'): ruins.append(('palavra de preço com outra intenção', tt, i))
print(len(ruins)); [print('  ', x) for x in ruins[:60]]
print('\n== sorteio de 15 linhas (random.seed(20261114); random.sample(range(len(PK)), 15)) ==')
random.seed(20261114)
for n in sorted(random.sample(range(len(PK)), 15)):
    r = PK[n]; print(f"linha {n + 2} | {r['termo']} | praga={r['praga']} | {r['tipo_local']}={r['local']} | intenção={r['intencao']} | público={r['publico']} | volume={r['volume']} | {r['origem_do_termo']} | {r['id_na_coleta']} | {r['situacao_na_coleta']}")
