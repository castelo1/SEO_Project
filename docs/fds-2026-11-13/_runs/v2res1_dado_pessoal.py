#!/usr/bin/env python3
"""Segunda passada da reserva 1 — dado pessoal e regras de coleta nos brutos, nos CSV e nos textos. Só leitura."""
import sys, os, re, collections, json
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2res1_comum import *
ARQS = ['data/serp_raw/ampliacao_01.jsonl', 'data/serp_raw/ampliacao_02.jsonl', 'data/serp_raw/ampliacao_03.jsonl', 'data/serp_raw/ampliacao_04.jsonl',
        'data/serp_raw/repeticao_02.jsonl', 'data/serp_sp_ampliacao.csv', 'data/serp_consultas_ampliacao.csv', 'data/palavras_chave.csv',
        'docs/mercado/serp_sp_ampliacao.md', 'docs/mercado/serp_sp_ampliacao_registro.md', 'data/serp_raw/monta_ampliacao.py', 'data/gera_palavras_chave.py',
        'data/serp_raw/coletor.js']
PADROES = {
    'telefone (DDD + 8 ou 9 dígitos)': re.compile(r'(?<!\d)\(?\d{2}\)?[\s.-]?9?\d{4}[\s.-]?\d{4}(?!\d)'),
    '0800/4004/3003': re.compile(r'(?<!\d)(0800|4004|3003)[\s-]?\d{3}'),
    'sequência de 8+ dígitos': re.compile(r'\d{8,}'),
    'e-mail': re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'),
    'CPF': re.compile(r'(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)'),
    'CNPJ': re.compile(r'(?<!\d)\d{2}\.?\d{3}\.?\d{3}/\d{4}-?\d{2}(?!\d)'),
    'sinal de clique em anúncio': re.compile(r'aclk|gclid|adurl|googleadservices|/pagead/|gad_source|wbraid|gbraid', re.I),
    'identificador de publicação de rede social': re.compile(r'(instagram\.com/(p|reel|reels|tv)/\w+|facebook\.com/[^ |"]*(posts|photos|videos|permalink|story)[^ |"]*|fbid=|youtube\.com/watch|youtu\.be/|tiktok\.com/@[^ |"]+/video|reddit\.com/r/[^ |"]+/comments/\w+|linkedin\.com/(posts|pulse|in)/[^ |"]+)', re.I),
    'whatsapp/wa.me': re.compile(r'wa\.me|api\.whatsapp|whatsapp\.com/send', re.I),
    'texto com cara de avaliação': re.compile(r'recomendo|atendimento (excelente|ótimo|otimo|péssimo)|profissionais (excelentes|ótimos)|"[^"]{40,}"', re.I),
}
for a in ARQS:
    p = os.path.join(RAIZ, a)
    if not os.path.exists(p): print('NÃO EXISTE', a); continue
    txt = open(p, encoding='utf-8').read()
    for nome, rx in PADROES.items():
        ach = [(txt.count('\n', 0, m.start()) + 1, m.group(0)[:70]) for m in rx.finditer(txt)]
        if ach: print(f'{a} | {nome}: {len(ach)} -> {ach[:12]}')
print('\n== [tel] nos brutos e no CSV ==')
for a in ARQS[:6]:
    txt = open(os.path.join(RAIZ, a), encoding='utf-8').read(); print(a, txt.count('[tel]'), '| [id]/omitido:', len(re.findall(r'\[[^\]]{2,20}\]', txt)), collections.Counter(re.findall(r'\[[^\]"]{2,24}\]', txt)).most_common(6))
print('\n== resultados de rede social no orgânico (bruto) ==')
for o in BRUTO + REP2:
    for pos, host, path, t in org_do_bruto(o):
        if any(s in host for s in ('instagram', 'facebook', 'reddit', 'youtube', 'tiktok', 'linkedin', 'twitter', 'x.com', 'threads')):
            print(o['id'], pos, host + path, '|', repr(t))
print('\n== nomes de perfil no bloco (todos, para leitura humana: nome de pessoa física?) ==')
nomes = collections.Counter(p[1] for o in BRUTO + REP2 for p in pack_do_bruto(o))
print(sorted(nomes))
print('\n== sufixo das linhas de perfil depois da nota (endereço? anos de atividade?) ==')
suf = collections.Counter()
for o in BRUTO + REP2:
    for s in o['pack']:
        m = re.search(r'\d,\d\([^)]*\)\s*(.*)$', s); suf[m.group(1) if m else '(sem nota) ' + s] += 1
print(suf.most_common())
print('\n== títulos orgânicos com palavras de pessoa (sr., dr., nome próprio + sobrenome?) — lista dos títulos que não contêm palavra do ramo ==')
ramo = ('dedetiz', 'praga', 'cupim', 'descupin', 'desratiz', 'rato', 'barata', 'pombo', 'mosquito', 'escorpi', 'formiga', 'pulga', 'percevejo', 'traça', 'mosca', 'lacraia',
        'marimbondo', 'broca', 'fumacê', 'fumace', 'inset', 'dengue', 'vespa', 'abelha', 'desentup', 'controle')
for o in BRUTO:
    for pos, host, path, t in org_do_bruto(o):
        if not any(k in t.lower() for k in ramo): print(o['id'], pos, host + path, '|', repr(t))
