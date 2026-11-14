#!/usr/bin/env python3
"""Segunda passada da reserva 3: confere, só de leitura, os números de busca que docs/plano_conteudo_90d.md cita,
contra data/serp_sp.csv e os brutos em data/serp_raw/. Biblioteca padrão. Não grava nada."""
import csv, json, os, collections, glob, subprocess, io, time
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
C = collections.Counter
p = os.path.join(RAIZ, 'data', 'serp_sp.csv')
print('serp_sp.csv mtime', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(p))))
S = list(csv.DictReader(open(p, encoding='utf-8')))
print('linhas', len(S), '| superficies', C(r['superficie'] for r in S))
org = [r for r in S if r['superficie'].startswith('org')]
print('orgânicos', len(org), '| A-G', sum(r['grupo'] != 'H' for r in org), '| H', sum(r['grupo'] == 'H' for r in org))

print('\n== Grupo F (plano L80: 13 buscas, 117 resultados, 68% serviço ou outra, 1% por local)')
F = [r for r in org if r['grupo'] == 'F']
print('   buscas', len({r['id'] for r in F}), 'resultados', len(F))
for k, v in C(r['tipo_pagina'] for r in F).most_common(): print(f'   {k}: {v} ({100*v/len(F):.1f}%)')

print('\n== Escorpião (plano L77: 12 de 16 resultados de órgãos públicos e do Butantan)')
E = [r for r in org if 'escorpi' in r['termo']]
print('   buscas', sorted({(r['id'], r['termo']) for r in E}), 'resultados', len(E))
print('   por tipo', C(r['tipo_pagina'] for r in E)); print('   domínios', C(r['dominio'] for r in E).most_common())

print('\n== Grupo H')
for i in ['H%02d' % n for n in range(1, 11)]:
    rs = [r for r in S if r['id'] == i]
    o = sorted([r for r in rs if r['superficie'].startswith('org')], key=lambda r: int(r['posicao']))
    print(f"   {i} {rs[0]['termo']!r} | IA {rs[0]['visao_geral_ia']} | superficies {dict(C(r['superficie'] for r in rs))}")
    print('        orgânicos 1-3:', [(r['posicao'], r['dominio'], r['tipo_pagina']) for r in o[:3]])
print('   anúncios (linhas de anúncio de texto) em H01+H02+H03:', sum(1 for r in S if r['id'] in ('H01', 'H02', 'H03') and r['superficie'].startswith('an')))
for i in ('H04', 'H05', 'H10'):
    o = [r for r in org if r['id'] == i]
    print('   ', i, 'primeiro:', [(r['dominio'], r['caminho'][:40]) for r in o if r['posicao'] == '1'], '| marketplaces:', sorted({r['dominio'] for r in o if r['dominio'] in ('triider.com.br', 'ohub.com.br', 'pedegas.com', 'getninjas.com.br', 'coteibem.com.br')}))
print('   H03 sivisa:', [(r['posicao'], r['dominio']) for r in org if r['id'] == 'H03' and ('sivisa' in r['dominio'] or 'gov' in r['dominio'])])

print('\n== Cupim B04 e B04r (plano L72): perfis do bloco de mapa nos brutos')
for arq in sorted(glob.glob(os.path.join(RAIZ, 'data', 'serp_raw', '*.jsonl'))):
    for l in open(arq, encoding='utf-8'):
        try: o = json.loads(l)
        except Exception: continue
        if o.get('id') in ('B04', 'B04r'):
            print('   ', os.path.basename(arq), o.get('id'), repr(o.get('q')), '| chaves:', sorted(o.keys()))
            for k, v in o.items():
                if isinstance(v, list) and v and k not in ('org', 'organicos'):
                    print('       ', k, ':')
                    for x in v: print('           ', (json.dumps(x, ensure_ascii=False)[:150]))
print('   no CSV, B04:', [(r['superficie'], r['posicao'], r['titulo_ou_nome'][:60]) for r in S if r['id'] == 'B04' and not r['superficie'].startswith('org')])

print('\n== Protótipo: "[A ESCREVER]" (plano L81)')
for arq in glob.glob(os.path.join(RAIZ, 'prototipo', '**', '*.html'), recursive=True):
    t = open(arq, encoding='utf-8').read()
    if 'A ESCREVER' in t: print('   ', arq, 'ocorrências:', t.count('A ESCREVER'))
print('   página-modelo existe:', os.path.exists(os.path.join(RAIZ, 'prototipo', 'zona-oeste', 'baratas', 'index.html')))

print('\n== Mapa antigo (plano L88-91: 168 de 1.260, 13%) — versões de data/palavras_chave.csv no git (leitura)')
try:
    log = subprocess.run(['git', '-C', RAIZ, 'log', '--format=%h %ad', '--date=format:%d/%m %H:%M', '--', 'data/palavras_chave.csv'], capture_output=True, text=True).stdout.strip().splitlines()
    GUIA = {'baratas', 'ratos', 'cupim', 'percevejo', 'pombos', 'escorpião'}
    for ln in log:
        h = ln.split()[0]
        txt = subprocess.run(['git', '-C', RAIZ, 'show', h + ':data/palavras_chave.csv'], capture_output=True, text=True).stdout
        L = list(csv.DictReader(io.StringIO(txt)))
        def f(**kw): return [r for r in L if all((r[k] in v) if isinstance(v, (set, list, tuple)) else (r[k] == v) for k, v in kw.items())]
        def cob(reg, pragas, com_melhor=True, com_inicio=True, com_gerais=True):
            s = set(); a = lambda rs: s.update(r['termo'] for r in rs)
            if com_inicio: a(f(tipo_local='cidade', praga='geral', intencao='contratar', publico='residencial/geral'))
            a([r for r in f(intencao='confiança') if com_melhor or 'melhor dedetizadora' not in r['termo']])
            for g in GUIA: a(f(praga=g, intencao='informativa')); a(f(praga=g, tipo_local='cidade', intencao='contratar'))
            a(f(tipo_local='zona', local=reg, intencao='contratar'))
            for g in pragas: a(f(praga=g, tipo_local='zona', local=reg, intencao=['contratar', 'preço']))
            a(f(intencao='preço', tipo_local='cidade')); a([r for r in L if r.get('id_na_coleta') == 'H05'])
            a(f(publico='condomínio')); a(f(publico='restaurante'))
            if com_gerais: a([r for r in f(intencao='informativa') if r['praga'] == 'geral'])
            return len(s)
        P5 = ['baratas', 'ratos', 'cupim', 'percevejo', 'pombos']
        print(f"   {ln}: {len(L)} termos | intencao {dict(C(r['intencao'] for r in L))} | cobertura zona oeste, 5 T3: {cob('zona oeste', P5)}; 1 T3: {cob('zona oeste', P5[:1])}; 5 T3 sem 'melhor': {cob('zona oeste', P5, com_melhor=False)}; 5 T3 sem início: {cob('zona oeste', P5, com_inicio=False)}; 5 T3 sem gerais: {cob('zona oeste', P5, com_gerais=False)}")
except Exception as e:
    print('   git indisponível:', e)
