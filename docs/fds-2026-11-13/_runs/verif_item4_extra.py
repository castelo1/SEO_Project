#!/usr/bin/env python3
"""Verificador item 4 — contas complementares, só leitura (títulos 4.3, 'anos no mercado', nomes de perfil, claims menores)."""
import csv, glob, json, os, re, sys, statistics, collections, unicodedata
R = '/home/ancastelo/pessoal/SEO_Project'; D = R + '/data'; C = collections.Counter
def sa(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
recs = []
for f in sorted(glob.glob(D + '/serp_raw/lote_*.jsonl')):
    for l in open(f, encoding='utf-8'):
        if l.strip(): o = json.loads(l); o['arq'] = os.path.basename(f); recs.append(o)
main = [o for o in recs if o['id'][0] != 'H']
O = []
for o in main:
    for i, s in enumerate(o['org'], 1):
        u, _, t = s.partition(' | '); h, _, p = u.partition('/'); O.append(dict(id=o['id'], pos=i, dom=h, path='/' + p, tit=t, arq=o['arq']))
T3 = [r for r in O if r['pos'] <= 3]
print('titulos: comprimento max por lote', {a: max(len(r['tit']) for r in O if r['arq'] == a) for a in sorted({r['arq'] for r in O})})
print('caminho: comprimento max', max(len(r['path']) for r in O))
def show(nome, f):
    a = sum(1 for r in O if f(r)); b = sum(1 for r in T3 if f(r)); print(f'  {nome}: todos {a} ({100*a/len(O):.1f}%) | top3 {b} ({100*b/len(T3):.1f}%)')
print('-- telefone')
show('[tel] no titulo', lambda r: '[tel]' in r['tit'])
show('[tel] ou resto de mascara cortada no fim ([, [t, [te, [tel)', lambda r: '[tel]' in r['tit'] or re.search(r'\[(t(e(l)?)?)?$', r['tit']) is not None)
show('[tel] ou digitos tipo (11) / 11 9', lambda r: '[tel]' in r['tit'] or re.search(r'\(\d{2}\)|\b\d{4}[- ]\d{4}\b|\(?\d{2}\)?\s?9?\d{3,4}', r['tit']) is not None)
show('[tel] no titulo ou caminho', lambda r: '[tel]' in r['tit'] + r['path'])
print('   titulos com resto de numero sem [tel]:', [r['tit'] for r in O if '[tel]' not in r['tit'] and re.search(r'\(\d{2}|\d{4,}|\[', r['tit'])][:40])
print('-- 24 horas')
show('24 horas|24h|24hs|24 hrs (titulo)', lambda r: re.search(r'24\s?(horas|hrs|hs|h)\b', r['tit'].lower()) is not None)
show('24 (qualquer, titulo)', lambda r: re.search(r'\b24\b|24h', r['tit'].lower()) is not None)
show('24 horas|24h (titulo ou caminho)', lambda r: re.search(r'24[\s-]?(horas|hrs|hs|h)\b', (r['tit'] + ' ' + r['path']).lower()) is not None)
show('24 (qualquer, titulo ou caminho)', lambda r: '24' in (r['tit'] + ' ' + r['path']))
print('-- preco')
show('preço|a partir de (titulo)', lambda r: re.search(r'preço|a partir de', r['tit'].lower()) is not None)
show('preco s/ acento|a partir de (titulo)', lambda r: re.search(r'preco|a partir de', sa(r['tit'])) is not None)
show('preco|a partir de|R$ (titulo)', lambda r: re.search(r'preco|a partir de|r\$', sa(r['tit'])) is not None)
show('preco|a partir de (titulo ou caminho)', lambda r: re.search(r'preco|a partir de|a-partir-de', sa(r['tit'] + ' ' + r['path'])) is not None)
show('preco|a partir|valor|custa (titulo)', lambda r: re.search(r'preco|a partir|valor|custa', sa(r['tit'])) is not None)
print('-- melhor / orcamento')
show('melhor', lambda r: 'melhor' in r['tit'].lower()); show('orçamento', lambda r: 'orçamento' in r['tit'].lower()); show('orcamento s/acento', lambda r: 'orcamento' in sa(r['tit']))
# com csv
rows = [r for r in csv.DictReader(open(D + '/serp_sp.csv', encoding='utf-8')) if r['superficie'] == 'orgânico' and r['grupo'] != 'H']
print('csv: [tel] em titulo', sum(1 for r in rows if '[tel]' in r['titulo_ou_nome']), '| 24', sum(1 for r in rows if re.search(r'24\s?(horas|h)\b', r['titulo_ou_nome'].lower())))
print('== anos no mercado')
L = [(o['id'], o['arq'], s) for o in main for s in o['pack'] if not s.startswith('Patrocinado')]
a1 = [(i, s) for i, a, s in L if re.search(r'anos? no mercado', s)]
a2 = [(i, s) for i, a, s in L if re.search(r'\b\d+a\b', s)]
print(' linhas', len(L), '| com "anos no mercado"', len(a1), '| com "Na"', len(a2), '| uniao', len({(i, s) for i, s in a1 + a2}))
print(' por lote: linhas', C(a for _, a, _ in L)); print(' por lote com anos', C(a for i, a, s in L if re.search(r'anos? no mercado|\b\d+a\b', s)))
an = [int(m.group(1)) for i, a, s in L for m in [re.search(r'(\d+) anos? no mercado|\b(\d+)a\b', s)] if m for m in [re.match(r'(\d+)', m.group(1) or m.group(2))]]
print(' n', len(an), 'min', min(an), 'max', max(an))
print(' exemplos sem anos:', [s for i, a, s in L if not re.search(r'anos? no mercado|\b\d+a\b', s)][:12])
print('== nomes de perfil')
def nome(s):
    m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', s); return (m.group(1) if m else s).strip()
N = sorted({nome(s) for _, _, s in L}); print(' distintos', len(N))
for n in N: print('   ', n)
for rot, rx in (('dedetiz|controle de pragas|cupi', r'dedetiz|controle de pragas|cupi'), ('+pragas', r'dedetiz|pragas|cupi'), ('+pragas+desentup+insect+pest+pombos', r'dedetiz|pragas|cupi|desentup|insect|pest|pombo|prag'), ('dedetiz|prag|cupi', r'dedetiz|prag|cupi'), ('dedetiz|prag|cupi|ddt|dd', r'dedetiz|prag|cupi|pombo'), ('dedet|controle|cupi|pragas|pest control', r'dedet|controle|cupi|pragas|pest control')):
    print(' servico', rot, sum(1 for n in N if re.search(rx, sa(n))))
loc = [n for n in N if re.search(r'zona (norte|sul|leste|oeste)|24\s?h|\bsp\b|sao paulo|vila mariana|butanta|osasco|santana|moema|pinheiros|tatuape|lapa|mooca|penha|ipiranga|centro', sa(n))]
print(' local ou 24h', len(loc)); [print('    ', n) for n in loc]
print('== 13 dominios em 5+ buscas D: cada vez com pagina do bairro?')
LOCAIS = ['zona-leste','zona-norte','zona-oeste','zona-sul','centro','moema','pinheiros','vila-mariana','tatuape','santana','lapa','itaim-bibi','santo-amaro','mooca','perdizes','santa-cecilia','higienopolis','butanta','ipiranga','penha','jabaquara','itaquera','campo-limpo','bela-vista','vila-madalena','osasco','jardim-paulista','barra-funda','analia-franco']
q = {o['id']: o['q'] for o in main}
for d in ['protecpragas.com.br','lunardedetizadora.com.br','keikodedetizadora.com.br','dedetizadora.srv.br','primordialdedetizacao.com.br','dedetizadoraddpilar.com.br','biodesin.com.br','zet-tecdedetizadora.com.br','ohub.com.br','hidrosampa.com.br','ambientalepragas.com.br','grupoexpansao.com','etoprag.com.br']:
    rr = [r for r in O if r['dom'] == d and r['id'][0] == 'D']
    def bairro_ok(r):
        b = sa(q[r['id']]).replace('dedetizadora ', '').replace('dedetizacao ', '').strip().replace(' ', '-'); return b in sa(r['path'])
    print('  ', d, len(rr), 'com bairro da busca no caminho', sum(bairro_ok(r) for r in rr), [(q[r['id']], r['path']) for r in rr if not bairro_ok(r)][:4])
print('== rentokil por grupo', C(r['id'][0] for r in O if r['dom'] == 'rentokil.com'))
print('== D10/D11/D17/D18 e ultimos', [(o['id'], o['nv'], o['t']) for o in main if o['id'] in ('D10', 'D11', 'D16', 'D17', 'D18', 'D19', 'G05', 'G06')])
print('== D05 santana', [s for s in next(o for o in main if o['id'] == 'D05')['org']])
print('== variantes 4.3 (procura da regra que da os numeros do texto: tel 54/20; 24h 71/28; preco 30/13)')
for rot, f in (("'[t' no titulo", lambda r: '[t' in r['tit']), ("'[te' no titulo", lambda r: '[te' in r['tit']), ("'[tel' no titulo", lambda r: '[tel' in r['tit']), ("termina em '[' ou tem '[t'", lambda r: '[t' in r['tit'] or r['tit'].rstrip().endswith('[')),
               ('24 h (prefixo, pega cortado)', lambda r: re.search(r'24\s?h', r['tit'].lower()) is not None), ('24 hora|24h', lambda r: re.search(r'24 hora|24h', r['tit'].lower()) is not None), ('"24" em qualquer lugar', lambda r: '24' in r['tit']),
               ('24 seguido de h/H ou fim', lambda r: re.search(r'24\s?(h|$)', r['tit'].lower()) is not None),
               ('preç|a partir', lambda r: re.search(r'preç|a partir', r['tit'].lower()) is not None), ('preç|a partir|r\\$', lambda r: re.search(r'preç|a partir|r\$', r['tit'].lower()) is not None),
               ('preç|a partir|custa', lambda r: re.search(r'preç|a partir|custa', r['tit'].lower()) is not None), ('preç|a partir|valor', lambda r: re.search(r'preç|a partir|valor', r['tit'].lower()) is not None),
               ('preç|a partir|barat', lambda r: re.search(r'preç|a partir|barat[oa]\b', r['tit'].lower()) is not None), ('preç|partir|custa|valor|r\\$', lambda r: re.search(r'preç|partir|custa|valor|r\$', r['tit'].lower()) is not None)):
    show(rot, f)
print(' titulos com preç/a partir:', sorted(C(r['tit'] for r in O if re.search(r'preç|a partir', r['tit'].lower())).items()))
print(' titulos com custa/valor/R$ sem preç:', sorted(C(r['tit'] for r in O if re.search(r'custa|valor|r\$', r['tit'].lower()) and not re.search(r'preç|a partir', r['tit'].lower())).items()))
print(' titulos com 24 que nao casam 24 horas/24h:', sorted(C(r['tit'] for r in O if '24' in r['tit'] and not re.search(r'24\s?(horas|hrs|hs|h)\b', r['tit'].lower())).items()))
