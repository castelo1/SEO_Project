#!/usr/bin/env python3
"""Segunda passada do item 4 — confere data/palavras_chave.csv. SÓ LEITURA. Semente do sorteio de 15 linhas: 'v2item4-palavras-20261114'."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2item4_comum import *
C = collections.Counter
rows = list(csv.DictReader(open(os.path.join(DATA, 'palavras_chave.csv'), encoding='utf-8')))
print('linhas', len(rows), '| colunas', list(rows[0].keys()))
print('termos distintos', len({r['termo'] for r in rows}), '| distintos sem acento/caixa', len({sem_acento(r['termo']) for r in rows}))
dup = [t for t, n in C(sem_acento(r['termo']) for r in rows).items() if n > 1]; print('duplicados (sem acento):', dup[:10])
print('volume:', C(r['volume'] for r in rows))
print('intenção:', C(r['intencao'] for r in rows).most_common())
print('tipo_local:', C(r['tipo_local'] for r in rows).most_common())
print('praga:', C(r['praga'] for r in rows).most_common())
print('publico:', C(r['publico'] for r in rows).most_common())
print('origem:', C(r['origem_do_termo'] for r in rows).most_common())
print('situação:', C(r['situacao_na_coleta'] for r in rows).most_common())
print('locais distintos por tipo:', {t: len({r['local'] for r in rows if r['tipo_local'] == t}) for t in C(r['tipo_local'] for r in rows)})
print('locais bairro:', sorted({r['local'] for r in rows if r['tipo_local'] == 'bairro'}))
print('locais zona/cidade:', sorted({(r['tipo_local'], r['local']) for r in rows if r['tipo_local'] in ('zona', 'cidade', 'sem local')}))
ger = [r for r in rows if r['origem_do_termo'] == 'combinação gerada']
print('geradas:', len(ger), '| por intenção', C(r['intencao'] for r in ger).most_common(), '| por tipo_local', C(r['tipo_local'] for r in ger).most_common())
print('  grade cheia 18 x 46 x 3 =', 18 * 46 * 3, '| confiança 46 x 3 =', 46 * 3, '| público 6 x 5 =', 30, '| informativas no gerador = 23')
col = [r for r in rows if r['origem_do_termo'].startswith('consulta da coleta')]
print('consultas da coleta:', len(col), C(r['origem_do_termo'] for r in col), '| situação', C(r['situacao_na_coleta'] for r in col))
c13 = [r for r in col if '13/11' in r['origem_do_termo']]
cons = {c['id']: c for c in consultas()}; lot = {o['id']: o for o in lotes()}
print('13/11: linhas', len(c13), '| ids', len({r['id_na_coleta'] for r in c13}), '| todos nos lotes?', all(r['id_na_coleta'] in lot for r in c13), '| termo == q do lote?', all(lot[r['id_na_coleta']]['q'].lower() == r['termo'] for r in c13))
print('ids da coleta ausentes do mapa:', [i for i in lot if i not in {r['id_na_coleta'] for r in c13}])
print('\n--- as 89 linhas de 13/11 (id | termo | praga | tipo_local | local | intenção | público) ---')
for r in c13: print(' ', r['id_na_coleta'], '|', r['termo'], '|', r['praga'], '|', r['tipo_local'], '|', r['local'], '|', r['intencao'], '|', r['publico'])
print('\n--- sorteio de 15 linhas (semente v2item4-palavras-20261114) ---')
rnd = random.Random('v2item4-palavras-20261114')
for k in sorted(rnd.sample(range(len(rows)), 15)):
    r = rows[k]; print(f'  linha {k + 2}:', r['termo'], '|', r['praga'], '|', r['tipo_local'], '|', r['local'], '|', r['intencao'], '|', r['publico'], '|', r['volume'], '|', r['origem_do_termo'], '|', r['id_na_coleta'], '|', r['situacao_na_coleta'])
# coerência mecânica de todas as geradas
PR = {'dedetização de baratas': 'baratas', 'desratização': 'ratos', 'descupinização': 'cupim', 'dedetização de formigas': 'formigas', 'dedetização de pulgas': 'pulgas',
      'dedetização de percevejo de cama': 'percevejo', 'controle de escorpião': 'escorpião', 'controle de pombos': 'pombos', 'controle de mosquitos': 'mosquito',
      'dedetização de carrapatos': 'carrapatos', 'dedetização de aranhas': 'aranhas', 'dedetização de traças': 'traças', 'dedetização de moscas': 'moscas',
      'dedetização de lacraias': 'lacraias', 'remoção de marimbondos': 'marimbondos', 'tratamento de broca de madeira': 'brocas'}
ruim = []
for r in ger:
    t = r['termo']
    if r['local'] and not t.endswith(r['local']): ruim.append(('local', t, r['local']))
    esp = next((p for s, p in sorted(PR.items(), key=lambda x: -len(x[0])) if s in t), 'geral')
    if r['intencao'] != 'informativa' and esp != r['praga']: ruim.append(('praga', t, r['praga'], esp))
    i = 'urgência' if '24 horas' in t else 'preço' if t.startswith('preço ') else 'confiança' if any(k in t for k in ('confiável', 'com licença', 'melhor dedetizadora')) else 'informativa' if not r['local'] else 'contratar'
    if i != r['intencao']: ruim.append(('intenção', t, r['intencao'], i))
print('\ngeradas incoerentes (regra mecânica):', len(ruim), ruim[:10])
# termos gerados que duplicam, em sentido, uma consulta da coleta
print('informativas:', [(r['termo'], r['origem_do_termo'][:8], r['praga']) for r in rows if r['intencao'] == 'informativa'])
