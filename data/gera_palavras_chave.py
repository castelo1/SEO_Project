#!/usr/bin/env python3
"""Gera data/palavras_chave.csv: combinações praga × local × intenção para São Paulo.
São COMBINAÇÕES GERADAS (hipóteses de termo), não demanda observada: o volume de busca não foi medido.
Marca quais termos foram de fato buscados ao vivo em 13/11/2026 (data/serp_consultas.csv + data/serp_raw/lote_*.jsonl)
e em 14/11/2026 (ampliação da fila de reserva 1: data/serp_consultas_ampliacao.csv + data/serp_raw/ampliacao_*.jsonl).
Em 14/11/2026 a grade ganhou 20 bairros e 4 pragas (moscas, lacraias, marimbondos, brocas de madeira).
Uso: python3 data/gera_palavras_chave.py"""
import csv, glob, json, os
BASE = os.path.dirname(os.path.abspath(__file__))
# (praga, nome do serviço como o mercado escreve — visto nos títulos da coleta de 13/11/2026)
SERVICOS = [('geral', 'dedetização'), ('geral', 'dedetizadora'), ('baratas', 'dedetização de baratas'), ('ratos', 'desratização'),
            ('cupim', 'descupinização'), ('formigas', 'dedetização de formigas'), ('pulgas', 'dedetização de pulgas'),
            ('percevejo', 'dedetização de percevejo de cama'), ('escorpião', 'controle de escorpião'),
            ('pombos', 'controle de pombos'), ('mosquito', 'controle de mosquitos'), ('carrapatos', 'dedetização de carrapatos'),
            ('aranhas', 'dedetização de aranhas'), ('traças', 'dedetização de traças'),
            # acrescentadas em 14/11/2026 (reserva 1)
            ('moscas', 'dedetização de moscas'), ('lacraias', 'dedetização de lacraias'), ('marimbondos', 'remoção de marimbondos'),
            ('brocas', 'tratamento de broca de madeira')]
LOCAIS = [('cidade', 'são paulo'), ('zona', 'zona leste'), ('zona', 'zona norte'), ('zona', 'zona oeste'), ('zona', 'zona sul'),
          ('zona', 'centro de são paulo')] + [('bairro', b) for b in
          ['moema', 'pinheiros', 'vila mariana', 'tatuapé', 'santana', 'lapa', 'itaim bibi', 'santo amaro', 'mooca', 'perdizes',
           'santa cecília', 'higienópolis', 'butantã', 'ipiranga', 'penha', 'jabaquara', 'itaquera', 'campo limpo', 'bela vista',
           'vila madalena',
           # 20 bairros acrescentados em 14/11/2026 (reserva 1)
           'brooklin', 'morumbi', 'saúde', 'campo belo', 'interlagos', 'capão redondo', 'vila prudente', 'são miguel paulista',
           'sapopemba', 'guaianases', 'tucuruvi', 'pirituba', 'freguesia do ó', 'casa verde', 'vila maria', 'vila leopoldina',
           'jaguaré', 'liberdade', 'consolação', 'aclimação']]
INTENCOES_LOCAIS = [('contratar', '{s} {l}'), ('urgência', '{s} 24 horas {l}'), ('preço', 'preço {s} {l}')]
INFORMATIVAS = {'baratas': ['como acabar com baratas em apartamento', 'barata de esgoto como eliminar'],
                'ratos': ['como acabar com ratos em casa', 'rato no forro o que fazer'],
                'cupim': ['como saber se tem cupim', 'cupim de madeira seca tratamento'],
                'formigas': ['como acabar com formigas na cozinha'], 'pulgas': ['como acabar com pulgas em casa'],
                'percevejo': ['como identificar percevejo de cama', 'picada de percevejo de cama'],
                'escorpião': ['apareceu escorpião em casa o que fazer'], 'pombos': ['como espantar pombos do telhado'],
                'mosquito': ['como acabar com mosquito da dengue em casa'], 'carrapatos': ['como acabar com carrapatos no quintal'],
                'aranhas': ['aranha marrom em casa o que fazer'], 'traças': ['como acabar com traças no guarda roupa'],
                'geral': ['quanto tempo dura dedetização', 'dedetização é segura para pets', 'dedetização vale a pena',
                          'tabela de preço dedetização', 'como saber se dedetizadora é licenciada',
                          'de quanto em quanto tempo dedetizar apartamento', 'dedetização condomínio é obrigatória']}
CONFIANCA = ['dedetizadora confiável {l}', 'dedetizadora com licença vigilância sanitária {l}', 'melhor dedetizadora {l}']
PUBLICO = [('restaurante', 'dedetização para restaurante {l}'), ('condomínio', 'dedetização para condomínio {l}'),
           ('apartamento', 'dedetização de apartamento {l}'), ('empresa', 'controle de pragas para empresas {l}'),
           ('escola', 'dedetização para escola {l}')]
PRAGA_CHAVES = [('baratas', ['barata']), ('ratos', ['desratiza', 'rato']), ('cupim', ['cupim', 'descupiniza']), ('formigas', ['formiga']),
                ('pulgas', ['pulga']), ('percevejo', ['percevejo']), ('escorpião', ['escorpi']), ('pombos', ['pombo']),
                ('mosquito', ['mosquito', 'dengue', 'fumacê']), ('carrapatos', ['carrapato']), ('aranhas', ['aranha']), ('traças', ['traça']),
                ('morcegos', ['morcego']), ('moscas', ['mosca']), ('lacraias', ['lacraia']), ('marimbondos', ['marimbondo']),
                ('brocas', ['broca'])]
PUBLICO_CHAVES = [('restaurante', ['restaurante', 'bares', 'lanchonete']), ('condomínio', ['condomínio']), ('apartamento', ['apartamento']),
                  ('escola', ['escola']), ('empresa', ['empresas', 'comercial', 'indústria'])]
INTENCAO_GRUPO = {'A': 'contratar', 'B': 'contratar', 'C': 'contratar', 'D': 'contratar', 'E': 'contratar', 'F': 'contratar'}
def intencao_gh(t):
    if any(k in t for k in ('urgente', '24h', '24 horas', 'hoje', 'emergencial', 'aberta agora')): return 'urgência'
    if any(k in t for k in ('preço', 'orçamento', 'quanto custa')): return 'preço'
    if any(k in t for k in ('confiável', 'licen', 'melhor dedetizadora')): return 'confiança'
    return 'informativa'
coletados = {}
CONSULTAS = [dict(r, dia='13/11/2026') for r in csv.DictReader(open(os.path.join(BASE, 'serp_consultas.csv'), encoding='utf-8'))] + \
            [dict(r, dia='14/11/2026') for r in csv.DictReader(open(os.path.join(BASE, 'serp_consultas_ampliacao.csv'), encoding='utf-8'))]
for r in CONSULTAS: coletados[r['termo'].lower()] = [r['id'], 'planejado', r['dia']]
for f in glob.glob(os.path.join(BASE, 'serp_raw', 'lote_*.jsonl')) + glob.glob(os.path.join(BASE, 'serp_raw', 'ampliacao_*.jsonl')):
    for l in open(f, encoding='utf-8'):
        o = json.loads(l); coletados.setdefault(o['q'].lower(), [o['id'], '', ''])[1] = 'coletado'
linhas, vistos = [], set()
def add(termo, praga, tipo_local, local, intencao, publico, origem='combinação gerada'):
    t = ' '.join(termo.split())
    if t in vistos: return
    vistos.add(t); c = coletados.get(t)
    linhas.append(dict(termo=t, praga=praga, tipo_local=tipo_local, local=local, intencao=intencao, publico=publico,
                       volume='não medido', origem_do_termo=('consulta da coleta de ' + c[2]) if c else origem,
                       id_na_coleta=c[0] if c else '', situacao_na_coleta=c[1] if c else 'não buscado'))
for r in CONSULTAS:
    t = r['termo'].lower()   # as 129 consultas das duas coletas (89 + 40) entram primeiro, como foram escritas; praga, local e público inferidos do texto
    praga = next((p for p, chaves in PRAGA_CHAVES if any(k in t for k in chaves)), 'geral')
    tipo, local = next(((tp, l) for tp, l in sorted(LOCAIS, key=lambda x: (x[0] == 'cidade', -len(x[1]))) if l in t or (l == 'são paulo' and (t.endswith(' sp') or ' sp ' in t))), ('sem local', ''))
    if tipo == 'sem local' and 'penha' in t: tipo, local = 'bairro', 'penha'
    pub = next((p for p, chaves in PUBLICO_CHAVES if any(k in t for k in chaves)), 'residencial/geral')
    add(t, praga, tipo, local, intencao_gh(t) if (r['grupo'] in 'GH' or intencao_gh(t) != 'informativa') else 'contratar', pub)
for praga, s in SERVICOS:
    for tipo, l in LOCAIS:
        for intencao, molde in INTENCOES_LOCAIS: add(molde.format(s=s, l=l), praga, tipo, l, intencao, 'residencial/geral')
for tipo, l in LOCAIS:
    for molde in CONFIANCA: add(molde.format(l=l), 'geral', tipo, l, 'confiança', 'residencial/geral')
    if tipo != 'bairro':
        for pub, molde in PUBLICO: add(molde.format(l=l), 'geral', tipo, l, 'contratar', pub)
for praga, termos in INFORMATIVAS.items():
    for t in termos: add(t, praga, 'sem local', '', 'informativa', 'residencial/geral')
campos = ['termo', 'praga', 'tipo_local', 'local', 'intencao', 'publico', 'volume', 'origem_do_termo', 'id_na_coleta', 'situacao_na_coleta']
with open(os.path.join(BASE, 'palavras_chave.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader(); w.writerows(linhas)
import collections
print('termos', len(linhas), collections.Counter(l['situacao_na_coleta'] for l in linhas), collections.Counter(l['intencao'] for l in linhas).most_common(12))
