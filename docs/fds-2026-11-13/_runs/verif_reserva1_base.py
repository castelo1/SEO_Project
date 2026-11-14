#!/usr/bin/env python3
"""Verificação independente da reserva 1 — módulo base (só leitura).
Carrega os brutos (.jsonl) e os CSV e remonta, por conta própria, as linhas por resultado.
Não grava nada. Usado pelos outros verif_reserva1_*.py."""
import csv, json, os, re, unicodedata, collections, statistics

RAIZ = '/home/ancastelo/pessoal/SEO_Project'
D = os.path.join(RAIZ, 'data')
RAW = os.path.join(D, 'serp_raw')


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


def seg(h):
    a, b, c = map(int, h.split(':'))
    return a * 3600 + b * 60 + c


def le_jsonl(nome):
    out = []
    for l in open(os.path.join(RAW, nome), encoding='utf-8'):
        if l.strip():
            o = json.loads(l)
            o['arquivo'] = nome
            out.append(o)
    return out


def le_csv(caminho):
    return list(csv.DictReader(open(caminho, encoding='utf-8')))


CONSULTAS = le_csv(os.path.join(D, 'serp_consultas_ampliacao.csv'))
CONS = {r['id']: r for r in CONSULTAS}
RECS = []
for n in ('ampliacao_01.jsonl', 'ampliacao_02.jsonl', 'ampliacao_03.jsonl', 'ampliacao_04.jsonl'):
    RECS += le_jsonl(n)
REP = le_jsonl('repeticao_02.jsonl')
CSV_AMP = le_csv(os.path.join(D, 'serp_sp_ampliacao.csv'))
CSV_PRI = le_csv(os.path.join(D, 'serp_sp.csv'))
DOMS = {r['dominio']: r for r in le_csv(os.path.join(D, 'serp_dominios.csv'))}

# lista de locais: a mesma que o texto declara (locais do item 4 + 20 bairros novos), copiada de monta_ampliacao.py
LOCAIS = ['zona-leste', 'zona-norte', 'zona-oeste', 'zona-sul', 'centro', 'moema', 'pinheiros', 'vila-mariana', 'tatuape', 'santana', 'lapa',
          'itaim-bibi', 'santo-amaro', 'mooca', 'perdizes', 'santa-cecilia', 'higienopolis', 'butanta', 'ipiranga', 'penha', 'jabaquara',
          'itaquera', 'campo-limpo', 'bela-vista', 'vila-madalena', 'osasco', 'jardim-paulista', 'barra-funda', 'analia-franco',
          'brooklin', 'morumbi', 'saude', 'campo-belo', 'campo_belo', 'interlagos', 'capao-redondo', 'vila-prudente', 'sao-miguel',
          'sapopemba', 'guaianases', 'guaianazes', 'tucuruvi', 'pirituba', 'freguesia', 'casa-verde', 'vila-maria', 'vila-leopoldina',
          'jaguare', 'liberdade', 'consolacao', 'aclimacao']
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'tiktok.com', 'linkedin.com')


def tipo_pagina(host, path):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'):
        return 'governo/universidade'
    if host in SOCIAL:
        return 'rede social/fórum'
    if p in ('', '/'):
        return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')):
        return 'blog/artigo'
    if any(l in p for l in LOCAIS):
        return 'página interna por local'
    return 'página interna (serviço/outro)'


def org_de(o):
    """lista de dicts (pos, dominio, caminho, titulo, tipo) do orgânico de um registro bruto"""
    out = []
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | ')
        host, _, path = u.partition('/')
        out.append(dict(id=o['id'], grupo=o['id'][0], pos=i, dominio=host, caminho='/' + path, titulo=t.strip(),
                        tipo=tipo_pagina(host, '/' + path)))
    return out


def pack_de(o):
    """(perfis orgânicos do bloco, perfis patrocinados); cada perfil = (nome, nota, avaliacoes)"""
    org, pat = [], []
    for s in o['pack']:
        p = s.startswith('Patrocinado ')
        nome = s[len('Patrocinado '):] if p else s
        m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
        t = ((m.group(1) if m else nome).strip(), m.group(2) if m else '', m.group(3).replace('.', '') if m else '')
        (pat if p else org).append(t)
    return org, pat


ORG = [l for o in RECS for l in org_de(o)]
GRUPO = lambda o: o['id'][0]
pct = lambda a, b: round(100 * a / b) if b else None
