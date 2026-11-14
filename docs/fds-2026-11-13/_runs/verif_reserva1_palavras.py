#!/usr/bin/env python3
"""Verificação da reserva 1 — mapa de palavras-chave (data/palavras_chave.csv) e contagens citadas em
serp_sp_ampliacao.md (seção 8), serp_sp.md (seção 10) e plano_conteudo_90d.md (coluna "Termos em K"). Só leitura."""
import csv, os, sys, random, collections, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verif_reserva1_base import RAIZ, D, RAW, CONSULTAS, sem_acento

P = print
C = collections.Counter
K = list(csv.DictReader(open(os.path.join(D, 'palavras_chave.csv'), encoding='utf-8')))
P('colunas:', list(K[0].keys()))
P('total', len(K), '| termos distintos', len({r['termo'] for r in K}), '| distintos sem acento/caixa', len({sem_acento(r['termo']) for r in K}))
dup = [t for t, n in C(sem_acento(r['termo']) for r in K).items() if n > 1]
P('duplicados (sem acento):', dup[:20])
P('termo com espaço duplo, ponta ou maiúscula:', [r['termo'] for r in K if r['termo'] != ' '.join(r['termo'].split()) or r['termo'] != r['termo'].lower()][:10])
P('volume:', C(r['volume'] for r in K))
P('intenção:', C(r['intencao'] for r in K).most_common())
P('tipo_local:', C(r['tipo_local'] for r in K).most_common())
P('praga:', C(r['praga'] for r in K).most_common())
P('público:', C(r['publico'] for r in K).most_common())
P('origem:', C(r['origem_do_termo'] for r in K).most_common())
P('situação:', C(r['situacao_na_coleta'] for r in K).most_common())
P('locais distintos por tipo:', {t: len({r['local'] for r in K if r['tipo_local'] == t}) for t in ('cidade', 'zona', 'bairro', 'sem local')})
P('bairros:', sorted({r['local'] for r in K if r['tipo_local'] == 'bairro'}))
P('zonas:', sorted({r['local'] for r in K if r['tipo_local'] == 'zona'}))
ger = [r for r in K if r['origem_do_termo'] == 'combinação gerada']
P('geradas:', len(ger), '| da coleta:', len(K) - len(ger), '| ids de coleta distintos:', len({r['id_na_coleta'] for r in K if r['id_na_coleta']}))
P('grade teórica: 18 x 46 x 3 =', 18 * 46 * 3, '+ confiança 3 x 46 =', 3 * 46, '+ público 5 x 6 =', 30, '+ 21 informativos =', 18 * 46 * 3 + 138 + 30 + 21, '| coincidem com consulta coletada:', 18 * 46 * 3 + 138 + 30 + 21 - len(ger))
P('pares (praga) nas geradas com local:', len({r['praga'] for r in ger if r['tipo_local'] != 'sem local'}), sorted({r['praga'] for r in ger}))
# serviços: quantos moldes de serviço distintos
serv = C()
for r in ger:
    if r['intencao'] == 'contratar' and r['publico'] == 'residencial/geral' and r['tipo_local'] == 'cidade':
        serv[r['termo'].replace(' são paulo', '')] += 1
P('serviços (geradas, contratar, cidade):', len(serv), sorted(serv))

P('\n== as 40 linhas da coleta de 14/11')
k14 = [r for r in K if r['origem_do_termo'] == 'consulta da coleta de 14/11/2026']
P('linhas:', len(k14), '| todas coletadas:', all(r['situacao_na_coleta'] == 'coletado' for r in k14), '| ids:', sorted(r['id_na_coleta'] for r in k14) == sorted(c['id'] for c in CONSULTAS))
cons = {c['id']: c['termo'] for c in CONSULTAS}
P('termo != termo do plano:', [(r['id_na_coleta'], r['termo'], cons[r['id_na_coleta']]) for r in k14 if r['termo'] != cons[r['id_na_coleta']].lower()])
for r in k14:
    P('  ', r['id_na_coleta'], '|', r['termo'], '|', r['praga'], '|', r['tipo_local'], '|', r['local'], '|', r['intencao'], '|', r['publico'])
k13 = [r for r in K if r['origem_do_termo'] == 'consulta da coleta de 13/11/2026']
P('linhas da coleta de 13/11:', len(k13), C(r['situacao_na_coleta'] for r in k13))

P('\n== sorteio de 15 linhas (random.seed(2026111401); random.sample(range(len(K)), 15))')
random.seed(2026111401)
for i in sorted(random.sample(range(len(K)), 15)):
    r = K[i]
    P('  linha', i + 2, '|', r['termo'], '|', r['praga'], '|', r['tipo_local'], '|', r['local'], '|', r['intencao'], '|', r['publico'], '|', r['origem_do_termo'], '|', r['situacao_na_coleta'])

P('\n== classificação: conferência por regra independente')
BAIRROS = sorted({r['local'] for r in K if r['tipo_local'] == 'bairro'})
err = []
for r in K:
    t = r['termo']
    # local declarado tem de estar no termo (ou "sp" para a cidade)
    if r['tipo_local'] != 'sem local':
        ok = r['local'] in t or (r['local'] == 'são paulo' and (t.endswith(' sp') or ' sp ' in t))
        if not ok:
            err.append(('local fora do termo', t, r['local']))
    # outro bairro mais longo presente no termo
    for b in BAIRROS:
        if b in t and b != r['local'] and len(b) > len(r['local']) and r['tipo_local'] == 'bairro':
            err.append(('bairro mais longo no termo', t, r['local'], b))
    if r['tipo_local'] == 'sem local' and any(b in t for b in BAIRROS + ['são paulo', 'zona ', ' sp']):
        err.append(('sem local mas com local no termo', t))
    if r['tipo_local'] in ('cidade', 'zona') and any(b in t for b in BAIRROS):
        err.append(('cidade/zona mas com bairro no termo', t, [b for b in BAIRROS if b in t]))
    # intenção
    urg = any(k in t for k in ('urgente', '24h', '24 horas', 'hoje', 'emergencial', 'aberta agora'))
    pre = any(k in t for k in ('preço', 'orçamento', 'quanto custa'))
    if urg and r['intencao'] != 'urgência':
        err.append(('urgência no termo', t, r['intencao']))
    if pre and not urg and r['intencao'] != 'preço':
        err.append(('preço no termo', t, r['intencao']))
    if r['intencao'] == 'urgência' and not urg:
        err.append(('urgência sem marca', t))
    if r['intencao'] == 'preço' and not pre:
        err.append(('preço sem marca', t))
    if r['intencao'] == 'informativa' and r['tipo_local'] != 'sem local':
        err.append(('informativa com local', t, r['local']))
P('achados da regra:', len(err))
for e in err[:60]:
    P('  ', e)
P('-- praga x termo: termos cuja praga declarada não aparece (por radical) no termo, ou praga "geral" com nome de praga')
RAD = {'baratas': ['barata'], 'ratos': ['rato', 'desratiza'], 'cupim': ['cupim', 'descupiniza'], 'formigas': ['formiga'], 'pulgas': ['pulga'], 'percevejo': ['percevejo'],
       'escorpião': ['escorpi'], 'pombos': ['pombo'], 'mosquito': ['mosquito', 'dengue', 'fumacê'], 'carrapatos': ['carrapato'], 'aranhas': ['aranha'], 'traças': ['traça'],
       'morcegos': ['morcego'], 'moscas': ['mosca'], 'lacraias': ['lacraia'], 'marimbondos': ['marimbondo'], 'brocas': ['broca']}
e2 = []
for r in K:
    t = r['termo']
    if r['praga'] == 'geral':
        h = [p for p, ks in RAD.items() if any(k in t for k in ks)]
        if h:
            e2.append(('geral com praga', t, h))
    elif not any(k in t for k in RAD.get(r['praga'], ['<<<'])):
        e2.append(('praga fora do termo', t, r['praga']))
    else:
        h = [p for p, ks in RAD.items() if any(k in t for k in ks) and p != r['praga']]
        if h:
            e2.append(('duas pragas no termo', t, r['praga'], h))
P('achados:', len(e2))
for e in e2[:40]:
    P('  ', e)
P('-- bairros com nome de palavra comum: termos em que o nome do bairro aparece e o tipo NÃO é bairro, e termos de coleta com esses nomes')
for b in ('saúde', 'liberdade', 'consolação', 'aclimação', 'lapa', 'penha', 'santana', 'bela vista', 'centro'):
    fora = [r['termo'] for r in K if b in r['termo'] and not (r['tipo_local'] == 'bairro' and r['local'] == b) and not (b == 'centro' and r['local'] == 'centro de são paulo')]
    P('  ', b, ': linhas com o nome', sum(1 for r in K if b in r['termo']), '| classificadas noutro local:', fora[:8])

P('\n== contagens citadas no plano de conteúdo (coluna "Termos em K")')
f = lambda **kw: [r for r in K if all(r[k] == v for k, v in kw.items())]
P('cidade, geral, contratar, residencial/geral:', len(f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral')), '(plano: 6)')
cf = f(intencao='confiança')
P('confiança:', len(cf), '(plano: 140) |', C('com licença' if 'com licença' in r['termo'] else 'confiável' if 'confiável' in r['termo'] else 'melhor' if 'melhor' in r['termo'] else r['termo'] for r in cf).most_common(),
  '| por tipo_local:', C(r['tipo_local'] for r in cf).most_common(), '| coletados:', sorted(r['id_na_coleta'] for r in cf if r['id_na_coleta']))
for p, inf, cc in (('baratas', 2, 1), ('ratos', 2, 2), ('cupim', 2, 3), ('percevejo', 2, 1), ('pombos', 1, 2), ('escorpião', 1, 1)):
    a = f(praga=p, intencao='informativa'); b = f(praga=p, tipo_local='cidade', intencao='contratar')
    P(f'  {p}: informativa {len(a)} (plano: {inf}) | cidade+contratar {len(b)} (plano: {cc})', '' if (len(a), len(b)) == (inf, cc) else '<<< DIVERGE', [r['termo'] for r in b])
for z in sorted({r['local'] for r in K if r['tipo_local'] == 'zona'}):
    a = f(tipo_local='zona', local=z, intencao='contratar')
    P(f'  zona "{z}", contratar: {len(a)} (plano: 24; 23 no centro) | de público condomínio/restaurante: {sum(1 for r in a if r["publico"] in ("condomínio", "restaurante"))} | por praga contratar+preço:',
      sorted(C(r['praga'] for r in f(tipo_local='zona', local=z) if r['intencao'] in ('contratar', 'preço') and r['praga'] != 'geral').items()))
pc = f(intencao='preço', tipo_local='cidade')
P('preço + cidade:', len(pc), '(plano: 22) | gerais:', sum(1 for r in pc if r['praga'] == 'geral'), '(6) | de praga:', sum(1 for r in pc if r['praga'] != 'geral'), '(16) | pragas:', sorted(C(r['praga'] for r in pc if r['praga'] != 'geral').items()),
  '| coletados:', sorted(r['id_na_coleta'] for r in pc if r['id_na_coleta']))
sem_guia = ('formigas', 'pulgas', 'mosquito', 'carrapatos', 'aranhas', 'traças', 'moscas', 'lacraias', 'marimbondos', 'brocas')
P('  de pragas sem guia:', sum(1 for r in pc if r['praga'] in sem_guia), '(plano: 10)')
P('  H05:', [(r['termo'], r['tipo_local'], r['intencao']) for r in K if r['id_na_coleta'] == 'H05'])
P('público condomínio:', len(f(publico='condomínio')), '(plano: 9) | restaurante:', len(f(publico='restaurante')), '(plano: 9)')
P('urgência:', len(f(intencao='urgência')), '(plano: 835) | bairro:', len(f(tipo_local='bairro')), '(plano: 2.289)')
inf = f(intencao='informativa')
P('informativos:', len(inf), '(21) | coletados:', sorted(r['id_na_coleta'] for r in inf if r['id_na_coleta']), '| por praga:', C(r['praga'] for r in inf).most_common())
P('  informativos de formigas, pulgas, mosquito, carrapatos, aranhas e traças:', sum(1 for r in inf if r['praga'] in ('formigas', 'pulgas', 'mosquito', 'carrapatos', 'aranhas', 'traças')), '(plano: 6)')
P('  informativos de moscas, lacraias, marimbondos, brocas, morcegos:', sum(1 for r in inf if r['praga'] in ('moscas', 'lacraias', 'marimbondos', 'brocas', 'morcegos')))
