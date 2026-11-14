#!/usr/bin/env python3
"""Correção da segunda passada — fila de reserva 1 (ampliação da amostra de buscas).
Confere, nos dados, os achados de docs/fds-2026-11-13/_runs/verificacao2_reserva1.md antes de aplicá-los a
docs/mercado/serp_sp_ampliacao.md. Biblioteca padrão; SÓ LEITURA: não grava nada, não importa nem roda
monta_ampliacao.py nem gera_palavras_chave.py (eles regravam artefatos), não importa os scripts do revisor.
Uso: python3 /home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/corr2res1_contas.py"""
import sys
sys.dont_write_bytecode = True
import csv, glob, json, os, re, unicodedata, collections, statistics

RAIZ = '/home/ancastelo/pessoal/SEO_Project'
D = os.path.join(RAIZ, 'data')
C = collections.Counter
P = print


def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


def le_jsonl(padrao):
    out = []
    for f in sorted(glob.glob(os.path.join(D, 'serp_raw', padrao))):
        with open(f, encoding='utf-8') as fh:
            for n, l in enumerate(fh, 1):
                if l.strip():
                    o = json.loads(l); o['_arq'] = os.path.basename(f); o['_linha'] = n; out.append(o)
    return out


def le_csv(nome):
    """devolve as linhas com '_linha' = número da linha no arquivo (cabeçalho = 1)"""
    with open(os.path.join(D, nome), encoding='utf-8', newline='') as fh:
        rows = list(csv.DictReader(fh))
    for n, r in enumerate(rows, 2):
        r['_linha'] = n
    return rows


BRUTO = le_jsonl('ampliacao_*.jsonl')      # as 40 buscas da ampliação
REP2 = le_jsonl('repeticao_02.jsonl')      # as 5 repetições da ampliação
LOTES = le_jsonl('lote_*.jsonl')           # item 4
REP1 = le_jsonl('repeticao_01.jsonl')      # repetições do item 4
CSVA = le_csv('serp_sp_ampliacao.csv')
CSV4 = le_csv('serp_sp.csv')
CONS = le_csv('serp_consultas_ampliacao.csv')
DOM = {r['dominio']: r for r in le_csv('serp_dominios.csv')}
PK = le_csv('palavras_chave.csv')
GRUPO = {r['id']: r['grupo'] for r in CONS}
BID = {o['id']: o for o in BRUTO}

# ---------- regra de tipo de página (a do documento: pelo endereço) ----------
LOCAIS_ITEM4 = ['zona-leste', 'zona-norte', 'zona-oeste', 'zona-sul', 'centro', 'moema', 'pinheiros', 'vila-mariana', 'tatuape', 'santana',
                'lapa', 'itaim-bibi', 'santo-amaro', 'mooca', 'perdizes', 'santa-cecilia', 'higienopolis', 'butanta', 'ipiranga', 'penha',
                'jabaquara', 'itaquera', 'campo-limpo', 'bela-vista', 'vila-madalena', 'osasco', 'jardim-paulista', 'barra-funda',
                'analia-franco']
LOCAIS_NOVOS = ['brooklin', 'morumbi', 'saude', 'campo-belo', 'campo_belo', 'interlagos', 'capao-redondo', 'vila-prudente', 'sao-miguel',
                'sapopemba', 'guaianases', 'guaianazes', 'tucuruvi', 'pirituba', 'freguesia', 'casa-verde', 'vila-maria',
                'vila-leopoldina', 'jaguare', 'liberdade', 'consolacao', 'aclimacao']
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com', 'tiktok.com', 'linkedin.com')


def tipo(host, path, locais):
    p = sem_acento(path)
    if host.endswith('.gov.br') or host in ('gov.br', 'puspc.usp.br'): return 'governo/universidade'
    if host in SOCIAL: return 'rede social/fórum'
    if p in ('', '/'): return 'página inicial'
    if any(x in p for x in ('/blog', '/artigo', '/noticias', '/tag/')): return 'blog/artigo'
    if any(l in p for l in locais): return 'página interna por local'
    return 'página interna (serviço/outro)'


LOCAL, SERV = 'página interna por local', 'página interna (serviço/outro)'
AMPLA = LOCAIS_ITEM4 + LOCAIS_NOVOS

# orgânico a partir do BRUTO
ORG = []
for o in BRUTO:
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | ')
        host, _, path = u.partition('/')
        ORG.append(dict(id=o['id'], g=GRUPO[o['id']], pos=i, dom=host, path='/' + path, tit=t.strip(), tipo=tipo(host, '/' + path, AMPLA),
                        arq=o['_arq'], linha_bruto=o['_linha'], idx=i - 1))
CSV_ORG = [r for r in CSVA if r['superficie'] == 'orgânico']
assert len(ORG) == len(CSV_ORG) == 352, (len(ORG), len(CSV_ORG))
for a, b in zip(ORG, CSV_ORG):
    assert (a['id'], str(a['pos']), a['dom'], a['path'], a['tipo']) == (b['id'], b['posicao'], b['dominio'], b['caminho'], b['tipo_pagina']), (a, b)
    a['linha_csv'] = b['_linha']
P('base: 40 buscas?', len(BRUTO), '| orgânicos bruto = CSV, linha a linha (domínio, caminho, tipo):', len(ORG), '| linhas do CSV:', len(CSVA),
  dict(C(r['superficie'] for r in CSVA)))


def top3_todos_local(ids, troca=()):
    """nº de buscas cujos três primeiros são todos 'por local'; troca = {(id, pos)} reclassificados como local"""
    n = 0
    for i in ids:
        t3 = [x for x in ORG if x['id'] == i and x['pos'] <= 3]
        if len(t3) == 3 and all(x['tipo'] == LOCAL or (x['id'], x['pos']) in troca for x in t3): n += 1
    return n


IDS = {g: [o['id'] for o in BRUTO if GRUPO[o['id']] == g] for g in 'IJK'}

P('\n===== ACHADO 1: caminho cortado em 50 caracteres =====')
P('onde o corte acontece: coletor.js, função fx2, "x.pathname.slice(0,50)" — o corte é do coletor; o bruto já vem cortado')
P('comprimento máximo do caminho no CSV:', max(len(x['path']) for x in ORG), '| orgânicos com caminho de exatamente 50:', sum(1 for x in ORG if len(x['path']) == 50))
cort = [x for x in ORG if len(x['path']) == 50]
P('caminhos de 50 por tipo atribuído:', dict(C(x['tipo'] for x in cort)))
P('caminhos de 50 classificados como serviço, grupos I e J (id, posição, linha do CSV, bruto arquivo:linha[índice em org], endereço | título):')
for x in cort:
    if x['tipo'] == SERV and x['g'] in 'IJ':
        P(f"   {x['id']} {x['pos']}º | CSV linha {x['linha_csv']} | {x['arq']}:{x['linha_bruto']} org[{x['idx']}] | {x['dom']}{x['path']} | {x['tit']}")
P('caminhos de 50 classificados como serviço ENTRE OS TRÊS PRIMEIROS (todos os grupos):')
for x in cort:
    if x['tipo'] == SERV and x['pos'] <= 3:
        P(f"   {x['id']} {x['pos']}º | CSV linha {x['linha_csv']} | {x['arq']}:{x['linha_bruto']} org[{x['idx']}] | {x['dom']}{x['path']} | {x['tit']} | termo: {BID[x['id']]['q']}")
P('J10, três primeiros:', [(x['pos'], x['dom'] + x['path'], x['tipo']) for x in ORG if x['id'] == 'J10' and x['pos'] <= 3])
P('mesmo endereço em outras buscas:', [(x['id'], x['pos'], x['linha_csv']) for x in ORG if x['dom'] == 'pacprag.com.br' and x['path'].startswith('/dedetizacao-de-baratas-e-insetos')])
P('o sufixo cortado "-em-sao" é prefixo de quais nomes? da lista de locais:', [l for l in AMPLA if l.startswith('sao')], '| e também de "sao-paulo" (cidade, fora da lista)')
for g in 'IJ':
    P(f'grupo {g}: três primeiros todos por local, pela regra:', top3_todos_local(IDS[g]), 'de', len(IDS[g]))
ij = IDS['I'] + IDS['J']
P('I + J, pela regra:', top3_todos_local(ij), 'de', len(ij), '| se J10 3º contasse como local:', top3_todos_local(ij, {('J10', 3)}), 'de', len(ij),
  '| só J:', top3_todos_local(IDS['J'], {('J10', 3)}), 'de', len(IDS['J']))
P('I: buscas fora:', [i for i in IDS['I'] if not top3_todos_local([i])], '| J: buscas dentro:', [i for i in IDS['J'] if top3_todos_local([i])])
t3 = [x for x in ORG if x['pos'] <= 3]
P('três primeiros das 40 buscas:', len(t3), dict(C(x['tipo'] for x in t3)))
c2 = C(LOCAL if (x['id'], x['pos']) == ('J10', 3) else x['tipo'] for x in t3)
P('  se J10 3º contasse como local:', dict(c2))
for g in 'IJK':
    L = [x for x in ORG if x['g'] == g]; n = sum(1 for x in L if x['tipo'] == LOCAL)
    P(f'grupo {g}: por local {n} de {len(L)} = {100 * n / len(L):.1f}%')
tres = {('I05', 6), ('I08', 4), ('J10', 3)}
for g in 'IJ':
    L = [x for x in ORG if x['g'] == g]; n = sum(1 for x in L if x['tipo'] == LOCAL); m = sum(1 for x in L if (x['id'], x['pos']) in tres)
    P(f'  efeito dos três caminhos citados (I05 6º, I08 4º, J10 3º) no grupo {g}: {n} -> {n + m} de {len(L)} = {100 * n / len(L):.1f}% -> {100 * (n + m) / len(L):.1f}%')


def comeco_de_local(path):
    """o fim do caminho cortado é o começo (3 letras ou mais, nome incompleto) de um nome da lista de locais?"""
    p = sem_acento(path)
    return sorted({l for l in AMPLA for k in range(3, len(l)) if p.endswith(l[:k])})


P('TESTE MECÂNICO: caminhos de 50 classificados como serviço cujo final é o começo de um nome da lista de locais (todos os grupos):')
sus = [x for x in cort if x['tipo'] == SERV and comeco_de_local(x['path'])]
for x in sus:
    P(f"   {x['id']} {x['pos']}º | CSV linha {x['linha_csv']} | {x['arq']}:{x['linha_bruto']} org[{x['idx']}] | {x['dom']}{x['path']} | começo de: {comeco_de_local(x['path'])} | termo: {BID[x['id']]['q']}")
SUS = {(x['id'], x['pos']) for x in sus}
P('  desses, entre os três primeiros:', sorted(k for k in SUS if k[1] <= 3))
c3 = C(LOCAL if (x['id'], x['pos']) in SUS else x['tipo'] for x in t3)
P('  três primeiros das 40 se TODOS esses contassem como local:', dict(c3))
P('  I + J com os três primeiros todos por local, se todos esses contassem:', top3_todos_local(ij, SUS), 'de', len(ij), '| J:', top3_todos_local(IDS['J'], SUS), '| I:', top3_todos_local(IDS['I'], SUS),
  '| K:', top3_todos_local(IDS['K'], SUS), 'de', len(IDS['K']), '(pela regra:', top3_todos_local(IDS['K']), ')')
for g in 'IJK':
    L = [x for x in ORG if x['g'] == g]; n = sum(1 for x in L if x['tipo'] == LOCAL); m = sum(1 for x in L if (x['id'], x['pos']) in SUS)
    P(f'  grupo {g}: por local {n} -> {n + m} de {len(L)} = {100 * n / len(L):.1f}% -> {100 * (n + m) / len(L):.1f}% | serviço {sum(1 for x in L if x["tipo"] == SERV)} -> {sum(1 for x in L if x["tipo"] == SERV) - m}'
      f' = {100 * sum(1 for x in L if x["tipo"] == SERV) / len(L):.1f}% -> {100 * (sum(1 for x in L if x["tipo"] == SERV) - m) / len(L):.1f}%')
# Leitura, um a um, do que o teste mecânico trouxe (endereços e termos acima; nenhuma página foi aberta):
#   I03 7º  "...clinicas-e-hospitai"      -> falso positivo do teste ("hospitais"; "itai" só coincide com o começo de "itaim-bibi")
#   I17 9º  "...DEDETIZADORA-JAGU"        -> página de consulta de empresas; "JAGU..." é parte do nome de uma empresa, não página de bairro
#   I05 6º  "...-pragas-em-int"           -> busca de Interlagos: tem cara de página do bairro
#   K10 2º  "...-no-jardim-paulist"       -> falta uma letra para "jardim-paulista", que está na lista: tem cara de página por local
#   I08 4º e J10 3º (mesmo endereço) "...-rasteiros-em-sao" -> pode ser "sao-miguel" (as duas buscas são de São Miguel Paulista) ou
#            "sao-paulo" (cidade, que a regra não conta como local): ambíguo
CARA = {('I05', 6), ('K10', 2), ('I08', 4), ('J10', 3)}
assert CARA <= SUS
P('CENÁRIO "os quatro com cara de página por local contam como local" (I05 6º, K10 2º, I08 4º, J10 3º; os dois últimos são ambíguos):')
c4 = C(LOCAL if (x['id'], x['pos']) in CARA else x['tipo'] for x in t3)
P('  três primeiros das 40:', dict(c4))
P('  I + J com os três primeiros todos por local:', top3_todos_local(ij, CARA), 'de', len(ij), '| J:', top3_todos_local(IDS['J'], CARA), 'de 10 | I:', top3_todos_local(IDS['I'], CARA), 'de 20')
for g in 'IJK':
    L = [x for x in ORG if x['g'] == g]; n = sum(1 for x in L if x['tipo'] == LOCAL); m = sum(1 for x in L if (x['id'], x['pos']) in CARA); sv = sum(1 for x in L if x['tipo'] == SERV)
    P(f'  grupo {g}: por local {n} -> {n + m} de {len(L)} = {100 * n / len(L):.1f}% -> {100 * (n + m) / len(L):.1f}% | serviço {sv} -> {sv - m} = {100 * sv / len(L):.1f}% -> {100 * (sv - m) / len(L):.1f}%')


def corte_suspeito(path, locais=None):
    """versão proposta para o monta_ampliacao.py (só diagnóstico): caminho de 50 caracteres cujo último pedaço, depois de
    '-' ou '/', é o começo incompleto (3 letras ou mais) de um nome da lista de locais"""
    p = sem_acento(path)
    if len(path) != 50: return ''
    for l in (locais or AMPLA):
        for k in range(3, len(l)):
            if p.endswith('-' + l[:k]) or p.endswith('/' + l[:k]): return l
    return ''


P('TESTE PROPOSTO PARA O SCRIPT (pedaço final alinhado a "-" ou "/"):',
  [(x['id'], x['pos'], corte_suspeito(x['path'])) for x in ORG if x['tipo'] == SERV and corte_suspeito(x['path'])])
P('  caminhos de 50 classificados como POR LOCAL (o corte não os tirou da regra):', sum(1 for x in cort if x['tipo'] == LOCAL))
BAIRRO = {'I01': ['brooklin'], 'I02': ['morumbi'], 'I03': ['saude'], 'I04': ['campo-belo', 'campo_belo', 'campobelo'], 'I05': ['interlagos'],
          'I06': ['capao-redondo', 'capaoredondo'], 'I07': ['vila-prudente', 'vilaprudente'], 'I08': ['sao-miguel', 'saomiguel'], 'I09': ['sapopemba'],
          'I10': ['guaianases', 'guaianazes'], 'I11': ['tucuruvi'], 'I12': ['pirituba'], 'I13': ['freguesia'], 'I14': ['casa-verde', 'casaverde'],
          'I15': ['vila-maria', 'vilamaria'], 'I16': ['vila-leopoldina', 'vilaleopoldina'], 'I17': ['jaguare'], 'I18': ['liberdade'],
          'I19': ['consolacao'], 'I20': ['aclimacao']}
locI = [x for x in ORG if x['g'] == 'I' and x['tipo'] == LOCAL]
comB = [x for x in locI if any(b in sem_acento(x['path']) for b in BAIRRO[x['id']])]
P('grupo I: páginas por local', len(locI), '| com o bairro buscado no caminho', len(comB), '| outras', len(locI) - len(comB))

P('\n===== ACHADO 2: nome de perfil não separado da nota ("1,1 mil") =====')
RX_SCRIPT = re.compile(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)')                      # a do monta_ampliacao.py, linha 55
RX_NOVA = re.compile(r'^(.*?)\s(\d,\d)(?:\((\d[\d.]*)\)|\(([^)]*)\)|$)')   # a do monta_csv.py (item 4), linha 37, desde 14/11 02:21:
#   separa o nome e a nota; a contagem abreviada ("1,1 mil") fica fora do campo de avaliações (aqui guardada à parte, no grupo 4)


def avalia(txt):
    """'1.234' -> 1234; '1,1 mil' -> 1100 (arredondado pelo Google: de 1.050 a 1.149)"""
    t = txt.strip()
    if t.endswith('mil'): return int(round(float(t[:-3].strip().replace('.', '').replace(',', '.')) * 1000))
    return int(t.replace('.', ''))


def separa(s, rx):
    pat = s.startswith('Patrocinado ')
    nome = s[len('Patrocinado '):] if pat else s
    m = rx.search(nome)
    if not m: return pat, nome.strip(), '', ''
    g = m.groups() + (None,)
    return pat, m.group(1).strip(), m.group(2), (g[2] or g[3] or '')   # g[3] = contagem abreviada, quando houver


MP = []   # linhas do bloco (sem patrocinado), a partir do bruto
for o in BRUTO:
    for k, s in enumerate(o['pack']):
        pat, nome_s, nota_s, av_s = separa(s, RX_SCRIPT)
        _, nome_n, nota_n, av_n = separa(s, RX_NOVA)
        MP.append(dict(id=o['id'], g=GRUPO[o['id']], pat=pat, nome_script=nome_s, nota_script=nota_s, av_script=av_s.replace('.', ''),
                       nome=nome_n, nota=nota_n, av=av_n, arq=o['_arq'], linha_bruto=o['_linha'], idx=k, cru=s))
CSV_MP = [r for r in CSVA if r['superficie'].startswith('mapa')]
assert len(MP) == len(CSV_MP)
for a, b in zip(MP, CSV_MP):
    assert (a['nome_script'], a['nota_script'], a['av_script']) == (b['titulo_ou_nome'], b['nota'], b['avaliacoes']), (a, b)
    a['linha_csv'] = b['_linha']
P('linhas de mapa bruto = CSV (nome, nota, avaliações pela regra do script):', len(MP), '| bloco:', sum(1 for m in MP if not m['pat']), '| patrocinado:', sum(1 for m in MP if m['pat']))
for m in MP:
    if not m['nota_script']:
        P(f"  sem nota separada pelo script: {m['id']} | CSV linha {m['linha_csv']} | {m['arq']}:{m['linha_bruto']} pack[{m['idx']}] | bruto: {m['cru']!r}")
        P(f"     com a expressão nova: nome={m['nome']!r} nota={m['nota']!r} avaliações={m['av']!r} -> {avalia(m['av']) if m['av'] else None}")
P('linhas em que a expressão nova muda o resultado do script:', sum(1 for m in MP if (m['nome'], m['nota']) != (m['nome_script'], m['nota_script'])),
  '| linhas ainda sem nota com a expressão nova:', [m['cru'] for m in MP if not m['nota']])
# item 4: o CSV foi regravado em 14/11 às 02:21 com o monta_csv.py corrigido (nome e nota separados; contagem abreviada fica vazia).
# Leio a coluna de nome como está gravada agora.
P4 = [dict(g=r['grupo'], id=r['id'], nome_script=r['titulo_ou_nome'], nome=r['titulo_ou_nome'], av=r['avaliacoes'], linha=r['_linha'], nota=r['nota'])
      for r in CSV4 if r['superficie'] == 'mapa (bloco Empresas)']
for m in P4:
    if m['nome'].startswith('EccoClean') or not m['nota']:
        P(f"  item 4, serp_sp.csv linha {m['linha']} ({m['id']}): nome={m['nome']!r} nota={m['nota']!r} avaliações={m['av']!r}")
A = [m for m in MP if not m['pat']]
for rot, chave in (('pela coluna de nome (como o script grava)', 'nome_script'), ('pelo perfil (nome separado com a expressão nova)', 'nome')):
    pa = {m[chave] for m in A}; p4t = {m[chave] for m in P4}; p4ag = {m[chave] for m in P4 if m['g'] != 'H'}
    pI = {m[chave] for m in A if m['g'] == 'I'}; pD = {m[chave] for m in P4 if m['g'] == 'D'}
    P(f'{rot}:')
    P('   perfis distintos na ampliação:', len(pa), '| no item 4 (89 buscas):', len(p4t), '| no item 4 (A a G):', len(p4ag))
    P('   distintos nas 129 buscas das duas coletas:', len(pa | p4t))
    P('   da ampliação, não vistos na amostra principal (A a G):', len(pa - p4ag), '| não vistos nas 89:', len(pa - p4t))
    P('   grupo I: buscas com bloco', len({m['id'] for m in A if m['g'] == 'I'}), '| linhas', sum(1 for m in A if m['g'] == 'I'), '| perfis', len(pI), '| já vistos no grupo D:', len(pI & pD))
P('perfil que explica a diferença (nome gravado no CSV da ampliação -> nome separado):', sorted((m['nome_script'], m['nome']) for m in A if m['nome_script'] != m['nome']),
  '| está no item 4 com o nome separado?', sorted({(p['id'], p['linha']) for m in A if m['nome_script'] != m['nome'] for p in P4 if p['nome'] == m['nome']}))
# outras quase-coincidências entre as duas coletas (só para ver se há mais nomes que não casam por sobra de texto)
na = sorted({m['nome'] for m in A}); n4 = sorted({m['nome'] for m in P4})
quase = [(a, b) for a in na for b in n4 if a != b and (sem_acento(a) == sem_acento(b) or a.startswith(b + ' ') or b.startswith(a + ' '))]
P('outros nomes da ampliação que quase casam com nome do item 4 (prefixo ou só caixa/acento):', quase)
quase_int = [(a, b) for a in na for b in na if a < b and (sem_acento(a) == sem_acento(b) or b.startswith(a + ' '))]
P('idem, dentro da ampliação:', quase_int)
P('mais frequentes no bloco:', C(m['nome'] for m in A).most_common(4))
P('pares (nota, avaliações) do perfil "Ddtizz":', sorted({(m['nota'], m['av']) for m in A if m['nome'] == 'Ddtizz'}))
notas = [float(m['nota_script'].replace(',', '.')) for m in A if m['nota_script']]
P('nota (script): linhas lidas', len(notas), 'de', len(A), '| mediana', statistics.median(notas), '| mín', min(notas), '| 4,8 ou mais:', sum(1 for n in notas if n >= 4.8), f'= {100 * sum(1 for n in notas if n >= 4.8) / len(notas):.1f}%')
notas2 = [float(m['nota'].replace(',', '.')) for m in A if m['nota']]
P('nota (com a linha do "1,1 mil"): linhas', len(notas2), '| 4,8 ou mais:', sum(1 for n in notas2 if n >= 4.8), f'= {100 * sum(1 for n in notas2 if n >= 4.8) / len(notas2):.1f}%')


def av_perfil(M, chave_nome, chave_av, conv):
    av = {}
    for m in M:
        if m[chave_av] and (conv is avalia or m[chave_av].isdigit()): av[m[chave_nome]] = conv(m[chave_av])
    return av


for rot, M in (('40 buscas', A), ('grupo I', [m for m in A if m['g'] == 'I'])):
    a1 = av_perfil(M, 'nome_script', 'av_script', int); a2 = av_perfil(M, 'nome', 'av', avalia)
    P(f'avaliações por perfil, {rot}: script -> lidos {len(a1)}, mediana {statistics.median(a1.values())}, de {min(a1.values())} a {max(a1.values())}'
      f' | com o perfil do "1,1 mil" (qualquer valor acima do máximo dá a mesma mediana) -> lidos {len(a2)}, mediana {statistics.median(a2.values())}, máximo exibido "1,1 mil"')
for rot, gs in (('item 4, A a G', 'ABCDEFG'), ('item 4, grupo D', 'D')):
    M = [m for m in P4 if m['g'] in gs]
    a1 = {m['nome']: int(m['av']) for m in M if m['av'].isdigit()}
    P(f'avaliações por perfil, {rot} (CSV do item 4 como está): perfis {len({m["nome"] for m in M})}, lidos {len(a1)}, mediana {statistics.median(a1.values())}')

P('\n===== ACHADO 3: licença na primeira posição (piso) =====')


def classe(x):
    if x['dom'] in DOM: return DOM[x['dom']]['classe'] or 'não lido'
    if x['tipo'] == 'governo/universidade': return 'governo (pelo domínio)'
    if x['tipo'] == 'rede social/fórum': return 'rede social'
    return 'novo (não lido)'


LIC = 'empresa_com_numero_de_licenca'
for g in 'IJK':
    p1 = [x for x in ORG if x['g'] == g and x['pos'] == 1]
    P(f'grupo {g}: 1ª posição por classe:', dict(C(classe(x) for x in p1)), '| com licença:', sum(1 for x in p1 if classe(x) == LIC), 'de', len(p1),
      '| sites com licença na 1ª:', dict(C(x['dom'] for x in p1 if classe(x) == LIC)))
P('as 40 primeiras posições por classe:', dict(C(classe(x) for x in ORG if x['pos'] == 1)))
P('grupo K, 1ª posição (id, domínio, classe):', [(x['id'], x['dom'], classe(x)) for x in ORG if x['g'] == 'K' and x['pos'] == 1])
p14 = [r for r in CSV4 if r['superficie'] == 'orgânico' and r['posicao'] == '1']
for gs in ('D', 'E', 'B', 'ACFG', 'ABCDEFG'):
    L = [r for r in p14 if r['grupo'] in gs]
    P(f'item 4, grupo(s) {gs}: licença na 1ª posição', sum(1 for r in L if DOM.get(r['dominio'], {}).get('classe') == LIC), 'de', len(L),
      '| sites:', dict(C(r['dominio'] for r in L if DOM.get(r['dominio'], {}).get('classe') == LIC)))

P('\n===== ACHADO 4: duas listas de locais na tabela da seção 5.1 =====')
for g in 'DEB':
    L = [r for r in CSV4 if r['grupo'] == g and r['superficie'] == 'orgânico']
    gravado = C(r['tipo_pagina'] for r in L)
    antiga = C(tipo(r['dominio'], r['caminho'], LOCAIS_ITEM4) for r in L)
    ampla = C(tipo(r['dominio'], r['caminho'], AMPLA) for r in L)
    P(f'grupo {g} ({len(L)} orgânicos): gravado = regra com a lista de 13/11?', gravado == antiga)
    P('   lista de 13/11:', {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in antiga.most_common()})
    P('   lista ampliada:', {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in ampla.most_common()})
    for r in L:
        if tipo(r['dominio'], r['caminho'], LOCAIS_ITEM4) != tipo(r['dominio'], r['caminho'], AMPLA):
            P(f"   muda: serp_sp.csv linha {r['_linha']} | {r['id']} {r['posicao']}º | {r['dominio']}{r['caminho']} | {r['tipo_pagina']} -> {tipo(r['dominio'], r['caminho'], AMPLA)}")
todos4 = [r for r in CSV4 if r['superficie'] == 'orgânico']
P('em todo o item 4 (89 buscas), resultados que mudariam de tipo com a lista ampliada:', sum(1 for r in todos4 if tipo(r['dominio'], r['caminho'], LOCAIS_ITEM4) != tipo(r['dominio'], r['caminho'], AMPLA)),
  dict(C(r['grupo'] for r in todos4 if tipo(r['dominio'], r['caminho'], LOCAIS_ITEM4) != tipo(r['dominio'], r['caminho'], AMPLA))))
for g in 'IJK':
    L = [x for x in ORG if x['g'] == g]
    P(f'grupo {g} ({len(L)}):', {k: f'{v} ({100 * v / len(L):.1f}%)' for k, v in C(x['tipo'] for x in L).most_common()})

P('\n===== ACHADO 5: posição do perfil patrocinado =====')
pt = [o for o in BRUTO if any(p.startswith('Patrocinado') for p in o['pack'])]
P('buscas com perfil patrocinado:', len(pt), '| bloco (título "Empresas") acima do 1º orgânico:', sum(1 for o in pt if o['y']['pack'] is not None and o['y']['pack'] < o['y']['org']),
  '| no grupo I:', sum(1 for o in pt if GRUPO[o['id']] == 'I' and o['y']['pack'] < o['y']['org']), 'de', sum(1 for o in pt if GRUPO[o['id']] == 'I'))
P('o coletor mede: y.pack = topo do título "Empresas" (coletor.js, fx2: "pack: yOf(emp)"); não há medida da linha patrocinada')
P('lugar da linha patrocinada na lista do bloco (índice, tamanho):', dict(C((next(i for i, p in enumerate(o['pack']) if p.startswith('Patrocinado')), len(o['pack'])) for o in pt)))

P('\n===== ACHADO 9: linhas de perfil patrocinado =====')
P('linhas:', sum(1 for m in MP if m['pat']), '| perfis distintos:', dict(C(m['nome'] for m in MP if m['pat'])), '| buscas:', len({m['id'] for m in MP if m['pat']}))
P('patrocinado no item 4:', dict(C(r['titulo_ou_nome'] for r in CSV4 if r['superficie'] == 'mapa (patrocinado)')))

P('\n===== ACHADO 10: variantes quase iguais no mapa de termos =====')
PREP = {'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas', 'para', 'pra', 'e', 'a', 'o'}


def chave(t):
    w = sem_acento(t).split()
    w = [x for x in w if x not in PREP]
    s = ' '.join(w).replace('sao paulo', 'sp')
    return ' '.join(sorted(s.split()))


P('termos:', len(PK), '| duplicado exato:', [k for k, v in C(r['termo'] for r in PK).items() if v > 1],
  '| duplicado sem acento/caixa/espaço:', [k for k, v in C(' '.join(sem_acento(r['termo']).split()) for r in PK).items() if v > 1])
gr = collections.defaultdict(list)
for r in PK: gr[chave(r['termo'])].append(r)
pares = [v for v in gr.values() if len(v) > 1]
P('grupos de variantes (sem preposição, sem ordem, "sp" = "são paulo"):', len(pares), '| tamanhos:', dict(C(len(v) for v in pares)))
um_buscado = 0
for v in pares:
    sit = [r['situacao_na_coleta'] for r in v]
    if sit.count('coletado') == 1: um_buscado += 1
    P('   ' + ' × '.join(f"linha {r['_linha']} \"{r['termo']}\" [{r['id_na_coleta'] or '—'}, {r['situacao_na_coleta']}]" for r in v))
P('grupos em que exatamente uma variante foi buscada:', um_buscado, '| com as duas buscadas:', sum(1 for v in pares if [r['situacao_na_coleta'] for r in v].count('coletado') >= 2),
  '| com nenhuma:', sum(1 for v in pares if 'coletado' not in [r['situacao_na_coleta'] for r in v]))
P('por intenção:', dict(C(r['intencao'] for r in PK)), '| por tipo de local:', dict(C(r['tipo_local'] for r in PK)), '| volume:', dict(C(r['volume'] for r in PK)))

P('\n===== ACHADO 11: registro das 5 repetições (repeticao_02.jsonl) =====')
NOME = {'aio': 'IA', 'ad': 'anúncio', 'pack': 'mapa', 'org': 'orgânico'}


def ordem(y):
    return ' > '.join(NOME[k] for v, k in sorted((v, k) for k, v in y.items() if k in NOME and v is not None))


def seg(h):
    a, b, c = map(int, h.split(':')); return a * 3600 + b * 60 + c


def px(y, k):
    return '—' if y.get(k) is None else str(y[k])


ant = None
for r in REP2:
    a = BID[r['id'][:-1]]
    pat = sum(1 for p in r['pack'] if p.startswith('Patrocinado'))
    ua = [s.partition(' | ')[0] for s in a['org']]; ur = [s.partition(' | ')[0] for s in r['org']]
    pa = [separa(p, RX_NOVA)[1] for p in a['pack'] if not p.startswith('Patrocinado')]; pr = [separa(p, RX_NOVA)[1] for p in r['pack'] if not p.startswith('Patrocinado')]
    P(f"{r['id']} | {r['_arq']}:{r['_linha']} | termo {r['q']!r} (= 1ª vez: {r['q'] == a['q']}) | navegação {r['nv']} | leitura {r['t']} | logado {r['lg']} | local {r['loc']!r} (1ª vez {a['loc']!r}) | IA {r['aio']} | "
      f"anúncios {len(a['ads'])} -> {len(r['ads'])} | bloco {len(r['pack']) - pat}{' + 1' if pat else ''} (1ª vez {len(a['pack']) - sum(1 for p in a['pack'] if p.startswith('Patrocinado'))}"
      f"{' + 1' if any(p.startswith('Patrocinado') for p in a['pack']) else ''}) | orgânicos {len(ur)} | ordem {ordem(r['y'])} (= 1ª vez: {ordem(r['y']) == ordem(a['y'])})")
    P(f"      px IA {px(a['y'], 'aio')} -> {px(r['y'], 'aio')} | 1º anúncio {px(a['y'], 'ad')} -> {px(r['y'], 'ad')} | mapa {px(a['y'], 'pack')} -> {px(r['y'], 'pack')} | 1º orgânico {px(a['y'], 'org')} -> {px(r['y'], 'org')} | janela {r['y'].get('h')}"
      f" | 1ª vez às {a['nv']} ({(seg(r['nv']) - seg(a['nv'])) / 60:.1f} min antes) | mesmo 1º: {ua[0] == ur[0]} | mesmos endereços na ordem: {ua == ur} ({len(ua)}, {len(ur)}) | perfis em comum: {len(set(pa) & set(pr))} de {len(pa)}"
      f" | desde a repetição anterior: {'—' if ant is None else seg(r['nv']) - ant} s")
    ant = seg(r['nv'])
P('última das 40:', max(o['nv'] for o in BRUTO), '| primeira repetição:', REP2[0]['nv'], '| intervalo:', seg(REP2[0]['nv']) - max(seg(o['nv']) for o in BRUTO), 's')

P('\n===== ACHADO 13: precisão (uniprag no grupo K; domínio com o nome do bairro) =====')
P('grupo K, domínios mais frequentes:', C(x['dom'] for x in ORG if x['g'] == 'K').most_common(3))
for x in ORG:
    if x['g'] == 'K' and x['dom'] == 'uniprag.com.br': P(f"   {x['id']} {x['pos']}º | {x['path']} | {x['tipo']}")
for x in ORG:
    if x['g'] == 'I' and any(b.replace('-', '').replace('_', '') in x['dom'].replace('-', '') for b in BAIRRO[x['id']]):
        P(f"   nome do bairro no domínio: {x['id']} {x['pos']}º | {x['dom']} | {BID[x['id']]['q']}")

P('\n===== ACHADO 14: buscas com bruto =====')
P('lote_*:', len(LOTES), '| repeticao_01:', len(REP1), '| ampliacao_*:', len(BRUTO), '| repeticao_02:', len(REP2), '| soma:', len(LOTES) + len(REP1) + len(BRUTO) + len(REP2))

P('\n===== números do resumo que NÃO deveriam mudar (conferência) =====')
ys = [o['y'] for o in BRUTO]
P('resumo de IA: primeira camada em', sum(1 for y in ys if y['aio'] is not None and all(y[k] is None or y['aio'] <= y[k] for k in ('ad', 'pack', 'org'))), 'de', sum(1 for y in ys if y['aio'] is not None),
  '| acima do 1º orgânico em', sum(1 for y in ys if y['aio'] is not None and y['aio'] < y['org']), '| bloco antes do orgânico:', sum(1 for y in ys if y['pack'] is not None and y['pack'] < y['org']), 'de', sum(1 for y in ys if y['pack'] is not None),
  '| anúncio depois do orgânico:', sum(1 for y in ys if y['ad'] is not None and y['ad'] > y['org']), 'de', sum(1 for y in ys if y['ad'] is not None), '| orgânico abaixo da 1ª tela:', sum(1 for y in ys if y['org'] >= y['h']), 'de', len(ys))
dom4 = {r['dominio'] for r in CSV4 if r['superficie'] == 'orgânico'}
domA = {x['dom'] for x in ORG}
P('buscas do item 4:', len({r['id'] for r in CSV4}), '| domínios do item 4:', len(dom4), '| da ampliação:', len(domA), '| novos:', len(domA - dom4),
  '| resultados dos novos:', sum(1 for x in ORG if x['dom'] not in dom4), f"= {100 * sum(1 for x in ORG if x['dom'] not in dom4) / len(ORG):.1f}%", '| distintos nas duas coletas:', len(dom4 | domA))
P('linhas do CSV:', len(CSVA), dict(C(r['superficie'] for r in CSVA)))
