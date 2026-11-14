#!/usr/bin/env python3
"""Segunda passada da reserva 1 — carga comum (só leitura). Não importa nem roda monta_ampliacao.py (ele grava arquivos).
Reimplementa, de forma independente, a transformação bruto -> linhas, para comparar com data/serp_sp_ampliacao.csv."""
import csv, glob, json, os, re, unicodedata, collections, statistics
RAIZ = '/home/ancastelo/pessoal/SEO_Project'
D = os.path.join(RAIZ, 'data')

def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

def le_jsonl(padrao):
    out = []
    for f in sorted(glob.glob(os.path.join(D, 'serp_raw', padrao))):
        for n, l in enumerate(open(f, encoding='utf-8'), 1):
            if l.strip():
                o = json.loads(l); o['_arq'] = os.path.basename(f); o['_linha'] = n; out.append(o)
    return out

def le_csv(nome):
    return list(csv.DictReader(open(os.path.join(D, nome), encoding='utf-8')))

BRUTO = le_jsonl('ampliacao_*.jsonl')
REP2 = le_jsonl('repeticao_02.jsonl')
LOTES = le_jsonl('lote_*.jsonl')
REP1 = le_jsonl('repeticao_01.jsonl')
CSVA = le_csv('serp_sp_ampliacao.csv')
CONS = le_csv('serp_consultas_ampliacao.csv')
CSV4 = le_csv('serp_sp.csv')
CONS4 = le_csv('serp_consultas.csv')
DOM = {r['dominio']: r for r in le_csv('serp_dominios.csv')}
GRUPO = {r['id']: r['grupo'] for r in CONS}

def seg(h):
    a, b, c = map(int, h.split(':')); return a * 3600 + b * 60 + c

def org_do_bruto(o):
    """lista de (posicao, host, caminho, titulo) a partir do bruto"""
    r = []
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | ')
        host, _, path = u.partition('/')
        r.append((i, host, '/' + path, t.strip()))
    return r

def pack_do_bruto(o):
    """lista de (patrocinado?, nome, nota, avaliacoes)"""
    r = []
    for s in o['pack']:
        pat = s.startswith('Patrocinado ')
        nome = s[len('Patrocinado '):] if pat else s
        m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
        r.append((pat, (m.group(1) if m else nome).strip(), m.group(2) if m else '', m.group(3).replace('.', '') if m else ''))
    return r

def tem_bloco(o):
    return any(not p.startswith('Patrocinado') for p in o['pack'])

def tem_pat(o):
    return any(p.startswith('Patrocinado') for p in o['pack'])

NOME = {'aio': 'IA', 'ad': 'anúncio', 'pack': 'mapa', 'org': 'orgânico'}
def ordem(y):
    ks = sorted((v, k) for k, v in y.items() if k in NOME and v is not None)
    return ' > '.join(NOME[k] for v, k in ks)

def pct(a, b):
    return f'{a}/{b} = {100 * a / b:.1f}%' if b else '0'
