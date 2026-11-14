#!/usr/bin/env python3
"""Verificação da reserva 1 — conferências extras (só leitura): comparações iguais com iguais com o item 4,
candidatos a classificação errada de tipo de página, linhas de rede social, nomes dos perfis, dados de terceiros."""
import re, os, sys, json, collections, statistics, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verif_reserva1_base import *

P = print
C = collections.Counter
pri = [r for r in CSV_PRI if r['grupo'] != 'H']
orgp = [r for r in pri if r['superficie'] == 'orgânico']
LIC = 'empresa_com_numero_de_licenca'
cl = lambda d: DOMS.get(d, {}).get('classe', 'novo')

P('=== iguais com iguais: 1ª posição com licença, por grupo')
for g in 'ABCDEFG':
    p1 = [r for r in orgp if r['grupo'] == g and r['posicao'] == '1']
    n = sum(1 for r in p1 if cl(r['dominio']) == LIC)
    P(' item 4, grupo', g, ':', n, 'de', len(p1), pct(n, len(p1)), '%', dict(C(r['dominio'] for r in p1 if cl(r['dominio']) == LIC)))
for g in 'IJK':
    p1 = [l for l in ORG if l['grupo'] == g and l['pos'] == 1]
    n = sum(1 for l in p1 if cl(l['dominio']) == LIC)
    P(' ampliação, grupo', g, ':', n, 'de', len(p1), pct(n, len(p1)), '%', dict(C(l['dominio'] for l in p1 if cl(l['dominio']) == LIC)))
P(' item 4, D+E+B:', sum(1 for r in orgp if r['grupo'] in 'DEB' and r['posicao'] == '1' and cl(r['dominio']) == LIC), 'de', sum(1 for r in orgp if r['grupo'] in 'DEB' and r['posicao'] == '1'))

P('\n=== iguais com iguais: camadas D x I, E x J, B x K (item 4, serp_sp.csv)')
bus = collections.defaultdict(list)
for r in pri:
    bus[r['id']].append(r)
for g in 'DEB':
    B = [rs for rs in bus.values() if rs[0]['grupo'] == g]
    P(' ', g, len(B), 'IA', sum(1 for rs in B if rs[0]['visao_geral_ia'] == 'sim'), '| bloco', sum(1 for rs in B if any(r['superficie'] == 'mapa (bloco Empresas)' for r in rs)),
      '| anúncio', sum(1 for rs in B if any(r['superficie'] == 'anúncio' for r in rs)), '| patrocinado', sum(1 for rs in B if any(r['superficie'] == 'mapa (patrocinado)' for r in rs)))

P('\n=== iguais com iguais: avaliações por perfil')
def med_av(rows, nome='titulo_ou_nome'):
    av = {}
    for r in rows:
        if r['avaliacoes'].isdigit():
            av[r[nome]] = int(r['avaliacoes'])
    return len(av), (statistics.median(av.values()) if av else None)
for g in ('D', 'E', 'DE', 'ABFG', 'ABCDEFG'):
    P(' item 4, grupo', g, ': perfis com número lido, mediana =', med_av([r for r in pri if r['superficie'] == 'mapa (bloco Empresas)' and r['grupo'] in g]))
amp_m = [r for r in CSV_AMP if r['superficie'] == 'mapa (bloco Empresas)']
for g in ('I', 'J', 'K', 'IJ', 'IJK'):
    P(' ampliação, grupo', g, ':', med_av([r for r in amp_m if r['grupo'] in g]))

P('\n=== governo no item 4, por busca (para a frase "mais quatro pragas")')
gv = collections.defaultdict(list)
for r in orgp:
    if r['tipo_pagina'] == 'governo/universidade':
        gv[(r['id'], r['termo'])].append(int(r['posicao']))
for k, v in sorted(gv.items()):
    P(' ', k, v)

P('\n=== tipo de página: candidatos a classificação errada')
P('-- "por local" no grupo K (termo com a cidade):', [(l['id'], l['dominio'] + l['caminho']) for l in ORG if l['grupo'] == 'K' and l['tipo'] == 'página interna por local'])
amb = ('centro', 'saude', 'lapa', 'penha', 'liberdade', 'freguesia', 'santana', 'consolacao', 'osasco')
P('-- "por local" só por causa de palavra ambígua (' + ', '.join(amb) + '):')
for l in ORG:
    if l['tipo'] == 'página interna por local':
        p = sem_acento(l['caminho'])
        hits = [x for x in LOCAIS if x in p]
        if all(h in amb for h in hits):
            P('   ', l['id'], CONS[l['id']]['termo'], '|', l['dominio'] + l['caminho'], hits)
P('-- "serviço/outro" em I e J cujo caminho tem cara de local (bairro sem hífen, cidade vizinha, "sao-paulo", "sp"):')
for l in ORG:
    if l['grupo'] in 'IJ' and l['tipo'] == 'página interna (serviço/outro)':
        P('   ', l['id'], CONS[l['id']]['termo'], '|', l['dominio'] + l['caminho'])
P('-- página por local que NÃO é do bairro buscado (grupo I):')
chave = {'I01': ['brooklin'], 'I02': ['morumbi'], 'I03': ['saude'], 'I04': ['campo-belo', 'campo_belo', 'campobelo'], 'I05': ['interlagos'], 'I06': ['capao-redondo', 'capaoredondo'],
         'I07': ['vila-prudente', 'vilaprudente'], 'I08': ['sao-miguel', 'saomiguel'], 'I09': ['sapopemba'], 'I10': ['guaianases', 'guaianazes'], 'I11': ['tucuruvi'], 'I12': ['pirituba'],
         'I13': ['freguesia'], 'I14': ['casa-verde', 'casaverde'], 'I15': ['vila-maria', 'vilamaria'], 'I16': ['vila-leopoldina', 'vilaleopoldina'], 'I17': ['jaguare'],
         'I18': ['liberdade'], 'I19': ['consolacao'], 'I20': ['aclimacao']}
n_ok = n_out = 0
for l in ORG:
    if l['grupo'] == 'I' and l['tipo'] == 'página interna por local':
        p = sem_acento(l['caminho'])
        if any(k in p for k in chave[l['id']]):
            n_ok += 1
        else:
            n_out += 1
            P('   ', l['id'], CONS[l['id']]['termo'], '|', l['dominio'] + l['caminho'], '(cortado em 50)' if len(l['caminho']) >= 50 else '')
P('   grupo I: páginas "por local" com o bairro buscado no caminho:', n_ok, '| com outro local (ou caminho cortado):', n_out)

P('\n=== linhas de rede social / fórum (o que ficou gravado)')
for l in ORG:
    if l['tipo'] == 'rede social/fórum':
        P('  ', l['id'], l['pos'], l['dominio'] + l['caminho'], '|', repr(l['titulo']))
P('-- títulos vazios ou com marca de omissão:', [(l['id'], l['pos'], l['dominio'] + l['caminho'], l['titulo']) for l in ORG if not l['titulo'] or 'omitid' in l['titulo'].lower() or 'omitid' in l['caminho'].lower()])

P('\n=== perfis do bloco (nomes de empresa; procurar nome de pessoa física)')
nomes = sorted({n for o in RECS + REP for n, _, _ in pack_de(o)[0] + pack_de(o)[1]})
for n in nomes:
    P('  ', n)
P('-- linhas brutas do bloco com endereço ou texto além de nome/nota/cidade:')
for o in RECS + REP:
    for s in o['pack']:
        resto = re.sub(r'^(Patrocinado )?.*?\d,\d\([\d., mil]+\)\s*', '', s)
        if re.search(r'\d{2,}|Rua|Av\.|Avenida|R\.', resto):
            P('  ', o['id'], '|', s)

P('\n=== dados de terceiros: expressões sobre todos os arquivos da tarefa')
ARQ = ['docs/mercado/serp_sp_ampliacao.md', 'docs/mercado/serp_sp_ampliacao_registro.md', 'data/serp_consultas_ampliacao.csv', 'data/serp_sp_ampliacao.csv',
       'data/serp_raw/ampliacao_01.jsonl', 'data/serp_raw/ampliacao_02.jsonl', 'data/serp_raw/ampliacao_03.jsonl', 'data/serp_raw/ampliacao_04.jsonl',
       'data/serp_raw/repeticao_02.jsonl', 'data/serp_raw/monta_ampliacao.py', 'data/serp_raw/coletor.js', 'data/palavras_chave.csv', 'data/gera_palavras_chave.py',
       'docs/plano_conteudo_90d.md']
EXP = {'telefone': r'\(?\d{2}\)?[\s-]?9?\d{4}[-\s]?\d{4}', '0800': r'0800', 'e-mail': r'[\w.+-]+@[\w-]+\.[\w.-]+', 'CPF': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
       'CNPJ': r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', '11+ dígitos': r'(?<!\d)\d{10,14}(?!\d)', 'whatsapp/wa.me': r'wa\.me|api\.whatsapp|whatsapp\.com/send',
       'tel solto 4-4': r'(?<!\d)9?\d{4}-\d{4}(?!\d)', '@usuario': r'(?<![\w.])@[A-Za-z0-9_.]{3,}'}
for a in ARQ:
    t = open(os.path.join(RAIZ, a), encoding='utf-8').read()
    for nome, e in EXP.items():
        hits = [(m.group(0), t[max(0, m.start() - 45):m.end() + 25].replace('\n', ' ')) for m in re.finditer(e, t)]
        if hits:
            P(' ', a, '|', nome, '|', len(hits), 'ocorrência(s):')
            for h in hits[:8]:
                P('      ', h)
    P(' ', a, '| [tel]:', t.count('[tel]'), '| "omitido":', len(re.findall(r'omitid', t)))
P('-- títulos orgânicos com resto de telefone (dígitos depois de [tel] ou parêntese aberto no fim):')
for o in RECS + REP:
    for s in o['org']:
        if re.search(r'\[tel\]\s?\d|\(\d{0,2}\)?\s?\d{0,8}$|\d{4,}', s.split(' | ', 1)[1]):
            P('  ', o['id'], '|', s)
P('-- caminhos com 4+ dígitos seguidos:')
for o in RECS + REP:
    for s in o['org']:
        u = s.split(' | ', 1)[0]
        if re.search(r'\d{4,}', u):
            P('  ', o['id'], '|', u)
