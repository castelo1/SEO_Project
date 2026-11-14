#!/usr/bin/env python3
"""Segunda passada da reserva 3: recontagem, só de leitura, de todas as contagens de termos que
docs/plano_conteudo_90d.md cita, contra data/palavras_chave.csv. Biblioteca padrão. Não grava nada."""
import csv, os, collections, hashlib, time
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
K = os.path.join(RAIZ, 'data', 'palavras_chave.csv')
L = list(csv.DictReader(open(K, encoding='utf-8')))
C = collections.Counter
print('arquivo', K)
print('mtime', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(K))), 'sha256', hashlib.sha256(open(K, 'rb').read()).hexdigest()[:16])
print('linhas (termos)', len(L), '| termos distintos', len({r['termo'] for r in L}))
print('colunas', list(L[0].keys()))
print('volume', C(r['volume'] for r in L))
print('intencao', C(r['intencao'] for r in L).most_common())
print('tipo_local', C(r['tipo_local'] for r in L).most_common())
print('publico', C(r['publico'] for r in L).most_common())
print('praga', C(r['praga'] for r in L).most_common())
print('situacao_na_coleta', C(r['situacao_na_coleta'] for r in L).most_common())

def f(**kw):
    return [r for r in L if all((r[k] in v) if isinstance(v, (set, list, tuple)) else (r[k] == v) for k, v in kw.items())]
def mostra(rot, rs, lim=30):
    print(f'\n== {rot}: {len(rs)}')
    for r in rs[:lim]:
        print('   ', r['termo'], '|', r['praga'], r['tipo_local'], r['local'], r['intencao'], r['publico'], '|', r['id_na_coleta'], r['situacao_na_coleta'])

mostra('Início: cidade, geral, contratar, residencial/geral (plano: 6)', f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral'))
conf = f(intencao='confiança')
mostra('T8: intencao=confiança (plano: 140)', conf, 0)
print('   por começo do termo:', C(('com licença' if 'com licença' in r['termo'] else 'confiável' if 'confiável' in r['termo'] else 'melhor' if r['termo'].startswith('melhor dedetizadora') else 'como saber' if r['termo'].startswith('como saber') else 'OUTRO: ' + r['termo']) for r in conf))
print('   por tipo_local:', C(r['tipo_local'] for r in conf))
print('   coletados:', [(r['id_na_coleta'], r['termo'], r['tipo_local'], r['situacao_na_coleta']) for r in conf if r['id_na_coleta']])
print('   confiança que não se encaixa nos 3 moldes + H03:', [r['termo'] for r in conf if not any(k in r['termo'] for k in ('com licença vigilância sanitária', 'dedetizadora confiável', 'melhor dedetizadora', 'como saber se dedetizadora'))])
for p, inf_plano, cc_plano in [('baratas', 2, 1), ('ratos', 2, 2), ('cupim', 2, 3), ('percevejo', 2, 1), ('pombos', 1, 2), ('escorpião', 1, 1)]:
    mostra(f'Guia {p}: informativa (plano: {inf_plano})', f(praga=p, intencao='informativa'))
    mostra(f'Guia {p}: cidade + contratar (plano: {cc_plano})', f(praga=p, tipo_local='cidade', intencao='contratar'))
    mostra(f'   (extra) {p}: informativa OU sem local, qualquer intenção', [r for r in L if r['praga'] == p and r['tipo_local'] == 'sem local'])
print('\n== T7/T4: zona + local + contratar (plano: 24 por região; 23 no centro)')
for z in sorted({r['local'] for r in L if r['tipo_local'] == 'zona'}):
    rs = f(tipo_local='zona', local=z, intencao='contratar')
    print('   ', z, len(rs), '| publico:', dict(C(r['publico'] for r in rs)), '| pragas:', len({r['praga'] for r in rs}), '| praga=geral:', sum(r['praga'] == 'geral' for r in rs))
    for r in rs:
        if r['publico'] != 'residencial/geral' or r['praga'] == 'geral': print('        ', r['termo'], '|', r['praga'], r['publico'], r['id_na_coleta'])
print('\n== T3: praga + zona + local + (contratar, preço) (plano: 2 por praga e região: 1 de contratar, 1 de preço)')
tab = collections.defaultdict(C)
for r in L:
    if r['tipo_local'] == 'zona' and r['intencao'] in ('contratar', 'preço') and r['praga'] != 'geral':
        tab[(r['praga'], r['local'])][r['intencao']] += 1
print('    distribuição de (contratar, preço) por par praga × região:', C((v['contratar'], v['preço']) for v in tab.values()))
for k, v in sorted(tab.items()):
    if (v['contratar'], v['preço']) != (1, 1): print('    fora do 1+1:', k, dict(v), [r['termo'] for r in L if r['tipo_local'] == 'zona' and r['praga'] == k[0] and r['local'] == k[1] and r['intencao'] in ('contratar', 'preço')])
print('    só as 6 pragas com guia:', {k: dict(v) for k, v in sorted(tab.items()) if k[0] in ('baratas', 'ratos', 'cupim', 'percevejo', 'pombos', 'escorpião') and (v['contratar'], v['preço']) != (1, 1)} or 'todas 1+1')
pc = f(intencao='preço', tipo_local='cidade')
mostra('T9: preço + cidade (plano: 22; 6 gerais, 16 de praga, 10 de pragas sem guia)', pc, 40)
print('   por praga:', C(r['praga'] for r in pc).most_common())
GUIA = {'baratas', 'ratos', 'cupim', 'percevejo', 'pombos', 'escorpião'}
print('   gerais:', sum(r['praga'] == 'geral' for r in pc), '| de praga:', sum(r['praga'] != 'geral' for r in pc), '| de praga sem guia:', sum(r['praga'] not in GUIA | {'geral'} for r in pc), sorted({r['praga'] for r in pc if r['praga'] not in GUIA | {'geral'}}))
print('   coletados no filtro:', [(r['id_na_coleta'], r['termo'], r['situacao_na_coleta']) for r in pc if r['id_na_coleta']])
print('   H05:', [(r['termo'], r['tipo_local'], r['intencao'], r['situacao_na_coleta']) for r in L if r['id_na_coleta'] == 'H05'])
print('   preço fora de cidade/zona/bairro:', [(r['termo'], r['tipo_local'], r['id_na_coleta']) for r in f(intencao='preço') if r['tipo_local'] == 'sem local'])
for p in ('condomínio', 'restaurante'):
    rs = f(publico=p)
    mostra(f'T6: publico={p} (plano: 9)', rs)
    print('   por tipo_local/intencao:', C((r['tipo_local'], r['intencao']) for r in rs))
print('\n== urgência (plano: 835):', len(f(intencao='urgência')), '| bairro (plano: 2.289):', len(f(tipo_local='bairro')))
print('   urgência por tipo_local:', C(r['tipo_local'] for r in f(intencao='urgência')))
inf = f(intencao='informativa')
mostra('informativas (plano: 21; 4 coletadas no grupo H)', inf, 40)
print('   coletadas:', [(r['id_na_coleta'], r['termo'], r['situacao_na_coleta']) for r in inf if r['id_na_coleta']])
print('   por praga:', C(r['praga'] for r in inf).most_common())
print('   pragas sem guia (plano: formigas, pulgas, mosquito, carrapatos, aranhas, traças = 6 termos):', [(r['praga'], r['termo']) for r in inf if r['praga'] not in GUIA | {'geral'}])
print('   gerais:', [r['termo'] for r in inf if r['praga'] == 'geral'])
# cobertura: união dos filtros do plano, com uma licenciada numa região e de 1 a 5 páginas T3
def cobertura(regiao, pragas_t3):
    s = set()
    def a(rs): s.update(r['termo'] for r in rs)
    a(f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral'))
    a(conf)
    for p in GUIA: a(f(praga=p, intencao='informativa')); a(f(praga=p, tipo_local='cidade', intencao='contratar'))
    a(f(tipo_local='zona', local=regiao, intencao='contratar'))
    for p in pragas_t3: a(f(praga=p, tipo_local='zona', local=regiao, intencao=['contratar', 'preço']))
    a(pc); a([r for r in L if r['id_na_coleta'] == 'H05'])
    a(f(publico='condomínio')); a(f(publico='restaurante'))
    a([r for r in inf if r['praga'] == 'geral'])
    return len(s)
for reg in ('zona oeste', 'centro de são paulo'):
    for n, ps in ((1, ['baratas']), (5, ['baratas', 'ratos', 'cupim', 'percevejo', 'pombos'])):
        c = cobertura(reg, ps); print(f'\n== cobertura (união dos filtros da seção 3, mapa de hoje) região={reg}, {n} T3: {c} de {len(L)} = {100*c/len(L):.1f}%')
c2 = cobertura('zona oeste', ['baratas', 'ratos', 'cupim', 'percevejo', 'pombos']) - len({r['termo'] for r in conf if 'melhor dedetizadora' in r['termo']})
print('   idem, 5 T3, sem os de "melhor":', c2, f'{100*c2/len(L):.1f}%')
print('\n== situação: coletado', sum(r['situacao_na_coleta'] == 'coletado' for r in L), '| ids de grupo H:', sorted(r['id_na_coleta'] for r in L if r['id_na_coleta'].startswith('H')))
