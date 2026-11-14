#!/usr/bin/env python3
"""Segunda passada do item 4 — varre os arquivos do item atrás de telefone, e-mail, CPF/CNPJ e sinais de clique/contato. SÓ LEITURA.
Não imprime o dado achado por inteiro quando for telefone/CNPJ: mostra o arquivo, a linha e um trecho mascarado."""
import re, os, glob, json, sys
RAIZ = '/home/ancastelo/pessoal/SEO_Project'
arqs = ['docs/mercado/serp_sp.md', 'docs/mercado/serp_sp_registro.md', 'docs/mercado/serp_sp_dominios.md', 'docs/mercado/_notas_dominios_parte1.md',
        'docs/mercado/_notas_dominios_parte2.md', 'data/serp_sp.csv', 'data/serp_dominios.csv', 'data/serp_consultas.csv', 'data/serp_dominios_classe_parte1.csv',
        'data/serp_dominios_classe_parte2.csv', 'data/palavras_chave.csv', 'data/gera_palavras_chave.py', 'data/serp_raw/coletor.js', 'data/serp_raw/monta_csv.py',
        'data/serp_raw/junta_classes.py', 'data/serp_raw/monta_registro.py', 'data/serp_raw/repeticao_01.jsonl'] + [f'data/serp_raw/lote_0{i}.jsonl' for i in range(1, 9)]
PADROES = {
    'telefone (regex do pedido)': r'\(?\d{2}\)?[\s-]?9?\d{4}[-\s]?\d{4}',
    '0800': r'0800',
    'e-mail': r'[\w.+-]+@[\w-]+\.[\w.-]+',
    'CNPJ': r'\d{2}\.?\d{3}\.?\d{3}/\d{4}-?\d{2}',
    'CPF': r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b',
    'wa.me / api.whatsapp / tel:': r'wa\.me|api\.whatsapp|whatsapp\.com/send|tel:\+?\d',
    'sequência de 10+ dígitos': r'(?<![\d-])\d{10,13}(?![\d-])',
    'aspas de avaliação (estrelas, "avaliou", "recomendo")': r'recomendo|avaliou|⭐|★|excelente atendimento|ótimo atendimento|otimo servi',
    'clique em anúncio / aclk / gclid': r'aclk|gclid|googleadservices|/pagead/',
}
def mask(s): return re.sub(r'\d', '#', s)
tot = {}
for a in arqs:
    p = os.path.join(RAIZ, a)
    if not os.path.exists(p): print('NÃO EXISTE', a); continue
    for n, l in enumerate(open(p, encoding='utf-8'), 1):
        for nome, pat in PADROES.items():
            for m in re.finditer(pat, l, flags=re.I):
                tot.setdefault((nome, a), []).append((n, m.start(), m.group(0), l[max(0, m.start() - 45):m.end() + 25].replace('\n', ' ')))
for (nome, a), v in sorted(tot.items()):
    print(f'\n## {nome} — {a}: {len(v)} ocorrência(s)')
    lim = 400 if '--tudo' in sys.argv else 12
    for n, c, g, ctx in v[:lim]:
        print(f'   linha {n}: «{ctx if "--claro" in sys.argv else mask(ctx)}»')
# o que o texto declara ter mascarado
c_tel = 0; c_omit = 0
for f in sorted(glob.glob(os.path.join(RAIZ, 'data/serp_raw/lote_*.jsonl'))) + [os.path.join(RAIZ, 'data/serp_raw/repeticao_01.jsonl')]:
    t = open(f, encoding='utf-8').read(); c_tel += t.count('[tel'); c_omit += t.count('omitid')
print('\n"[tel" nos brutos:', c_tel, '| "omitid" nos brutos:', c_omit)
t = open(os.path.join(RAIZ, 'data/serp_sp.csv'), encoding='utf-8').read(); print('"[tel" no CSV:', t.count('[tel'), '| "omitid" no CSV:', t.count('omitid'))
