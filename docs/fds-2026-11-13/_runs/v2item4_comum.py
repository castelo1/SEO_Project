#!/usr/bin/env python3
"""Segunda passada do item 4 — funções comuns, SÓ LEITURA. Não grava nenhum arquivo."""
import csv, glob, json, os, re, unicodedata, collections, statistics
RAIZ = '/home/ancastelo/pessoal/SEO_Project'
DATA = os.path.join(RAIZ, 'data'); RAW = os.path.join(DATA, 'serp_raw')

def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

def lotes():
    recs = []
    for f in sorted(glob.glob(os.path.join(RAW, 'lote_*.jsonl'))):
        for n, l in enumerate(open(f, encoding='utf-8'), 1):
            o = json.loads(l); o['arquivo'] = os.path.basename(f); o['linha'] = n; recs.append(o)
    return recs

def repeticao():
    return [json.loads(l) for l in open(os.path.join(RAW, 'repeticao_01.jsonl'), encoding='utf-8')]

def consultas():
    return list(csv.DictReader(open(os.path.join(DATA, 'serp_consultas.csv'), encoding='utf-8')))

def serp_csv():
    return list(csv.DictReader(open(os.path.join(DATA, 'serp_sp.csv'), encoding='utf-8')))

def dominios_csv():
    return list(csv.DictReader(open(os.path.join(DATA, 'serp_dominios.csv'), encoding='utf-8')))

def seg(h):
    a, b, c = h.split(':'); return int(a) * 3600 + int(b) * 60 + int(c)

def org_de(o):
    """lista de (pos, host, path, titulo) do bruto"""
    out = []
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | ')
        host, _, path = u.partition('/')
        out.append((i, host, '/' + path, t.strip()))
    return out

LOCAIS = ['zona-leste','zona-norte','zona-oeste','zona-sul','centro','moema','pinheiros','vila-mariana','tatuape','santana','lapa',
          'itaim-bibi','santo-amaro','mooca','perdizes','santa-cecilia','higienopolis','butanta','ipiranga','penha','jabaquara',
          'itaquera','campo-limpo','bela-vista','vila-madalena','osasco','jardim-paulista','barra-funda','analia-franco']
SOCIAL = ('instagram.com','facebook.com','reddit.com','youtube.com','tiktok.com','linkedin.com')
def tipo_pagina(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'governo/universidade'
    if host in SOCIAL: return 'rede social/fórum'
    if p in ('', '/'): return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog/artigo'
    if any(l in p for l in LOCAIS): return 'página interna por local'
    return 'página interna (serviço/outro)'

def pack_de(o):
    """lista de dicts: pat, pos, nome, nota, aval, bruto"""
    out = []; pos = 0
    for s in o['pack']:
        pat = s.startswith('Patrocinado ')
        nome = s[len('Patrocinado '):] if pat else s
        m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
        if not pat: pos += 1
        out.append(dict(pat=pat, pos=None if pat else pos, nome=(m.group(1) if m else nome).strip(),
                        nota=m.group(2) if m else '', aval=m.group(3).replace('.', '') if m else '', bruto=s))
    return out
