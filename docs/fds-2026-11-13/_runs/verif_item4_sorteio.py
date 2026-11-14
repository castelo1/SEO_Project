#!/usr/bin/env python3
"""Verificador item 4 — numera as frases com número de docs/mercado/serp_sp.md a partir da seção 2 (linha 60 em diante;
a seção 1 é conferida inteira à parte). Só leitura; imprime 'n<TAB>linha<TAB>frase'.
Unidade: linha de tabela (cada uma) ou frase de parágrafo/item de lista (parágrafo juntado; corte em '. ', '; ' ou ': ' antes de maiúscula, aspas ou negrito).
Entra a frase que tem algarismo depois de retirar trechos entre crases (caminhos), remissões 'seção N' e datas."""
import re, sys
L = open('/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md', encoding='utf-8').read().split('\n')
blocos = []; cur = None
for n, l in enumerate(L, 1):
    if n < 60: continue
    s = l.rstrip()
    if not s.strip() or s.startswith('#'): cur = None; continue
    if s.startswith('|'):
        cur = None
        if not re.match(r'^\|[-| ]+\|$', s): blocos.append([n, s])
        continue
    if re.match(r'^\s*(-|\d+\.)\s', s) or cur is None: cur = [n, s.strip()]; blocos.append(cur)
    else: cur[1] += ' ' + s.strip()
fr = []
for n, b in blocos:
    b = b if b.startswith('|') else re.sub(r'^\s*(-|\d+\.)\s+', '', b)   # tira o marcador de lista (senão '1.' vira frase)
    partes = [b] if b.startswith('|') else re.split(r'(?<=[.;:])\s+(?=[A-ZÀ-Ú"“*(])', b)
    for p in partes:
        limpo = re.sub(r'`[^`]*`', '', p); limpo = re.sub(r'se[cç][aã]o \(?[\d.]+\)?|se[cç][oõ]es [\d a.e]+|\d\d/\d\d(/\d{4})?|item \d+|fila de reserva \d|^\s*\d+\.\s', '', limpo)
        if re.search(r'\d', limpo): fr.append((n, p))
for i, (n, p) in enumerate(fr, 1): print(f'{i}\t{n}\t{p}')
