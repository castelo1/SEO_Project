#!/usr/bin/env python3
# Segunda passada, reserva 2 - so leitura.
# (1) mede a pagina-modelo e as outras paginas do prototipo; (2) confere a tabela das dez e a de min/mediana/max contra o .jsonl.
import json, re, os, statistics, subprocess
from html.parser import HTMLParser
BASE='/home/ancastelo/pessoal/SEO_Project/'

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.stack=[]; s.inbody=False; s.skip=0
        s.txt_body_noscript=[]; s.txt_body_noscript_nostyle=[]; s.txt_all=[]
        s.title=''; s.intitle=False; s.desc=None; s.canon=None
        s.links=[]; s.h=dict(h1=0,h2=0,h3=0); s.htxt=[]; s.curh=None
        s.imgs=0; s.forms=0; s.iframes=0; s.ld=[]; s.inld=False; s.lang=None; s.viewport=False
        s.inscript=False; s.instyle=False
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=='html': s.lang=a.get('lang')
        if t=='body': s.inbody=True
        if t=='title': s.intitle=True
        if t=='meta' and a.get('name')=='description': s.desc=a.get('content','')
        if t=='meta' and a.get('name')=='viewport': s.viewport=True
        if t=='link' and a.get('rel')=='canonical': s.canon=a.get('href')
        if t=='a': s.links.append(a.get('href'))
        if t in s.h: s.h[t]+=1; s.curh=[t,'']
        if t=='img': s.imgs+=1
        if t=='form': s.forms+=1
        if t=='iframe': s.iframes+=1
        if t=='script':
            s.inscript=True
            if a.get('type')=='application/ld+json': s.inld=True; s.ld.append('')
        if t=='style': s.instyle=True
    def handle_endtag(s,t):
        if t=='title': s.intitle=False
        if t=='script': s.inscript=False; s.inld=False
        if t=='style': s.instyle=False
        if t in s.h and s.curh: s.htxt.append(tuple(s.curh)); s.curh=None
        if t=='body': s.inbody=False
    def handle_data(s,d):
        if s.intitle: s.title+=d
        if s.inld: s.ld[-1]+=d
        if s.curh: s.curh[1]+=d
        if s.inbody:
            if not s.inscript:
                s.txt_body_noscript.append(d)
                if not s.instyle: s.txt_body_noscript_nostyle.append(d)

def mede(rel):
    raw=open(BASE+rel,'rb').read()
    p=P(); p.feed(raw.decode('utf-8'))
    t=' '.join(p.txt_body_noscript_nostyle)
    w_split=len(t.split())
    w_alnum=len([x for x in t.split() if re.search(r'\w',x)])
    w_re=len(re.findall(r"[0-9A-Za-zÀ-ÿ]+(?:[-'’][0-9A-Za-zÀ-ÿ]+)*",t))
    # variante: sem separador entre nos de texto (junta "Zona Oeste" + "(nao prototipada)" como o navegador faria com innerText? nao exatamente)
    t2=''.join(p.txt_body_noscript_nostyle); w_join=len(t2.split())
    links=p.links
    ext=[l for l in links if l and re.match(r'https?://',l)]
    anc=[l for l in links if l and l.startswith('#')]
    wa=[l for l in links if l and ('wa.me' in l or 'whatsapp' in l.lower())]
    botoes=len(re.findall(r'class="botao"',raw.decode('utf-8')))
    tipos=[]
    for b in p.ld:
        try: tipos+=re.findall(r'"@type"\s*:\s*"([^"]+)"',b)
        except Exception as e: tipos.append('erro')
    print('\n==',rel)
    print(' bytes',len(raw),'| KB(/1000) %.2f | KB(/1024) %.2f'%(len(raw)/1000,len(raw)/1024))
    print(' palavras: split com espaco entre nos =',w_split,'| so tokens com letra/numero =',w_alnum,'| regex de palavra =',w_re,'| nos colados =',w_join)
    print(' title [%d]: %s'%(len(p.title),p.title))
    print(' meta descricao [%d]: %s'%(len(p.desc) if p.desc is not None else -1,p.desc))
    print(' <a> ao todo',len(links),'| externos',len(ext),'| ancora na pagina',len(anc),'| whatsapp no href',len(wa),'| class=botao',botoes)
    print(' hrefs:',links)
    print(' h1,h2,h3',p.h,'| imgs',p.imgs,'| forms',p.forms,'| iframes',p.iframes)
    print(' h2:',[x[1] for x in p.htxt if x[0]=='h2'])
    print(' ld tipos',sorted(set(tipos)),'| lang',p.lang,'| viewport',p.viewport,'| canonical',p.canon)
    return p

for rel in ('prototipo/zona-oeste/baratas/index.html','prototipo/index.html','prototipo/para-empresas/restaurantes/index.html','prototipo/privacidade/index.html'):
    if os.path.exists(BASE+rel): mede(rel)

# --- tabela das dez contra o jsonl ---
dez=[json.loads(l) for l in open(BASE+'data/paginas_top10.jsonl')]
md=open(BASE+'docs/mercado/paginas_top10.md',encoding='utf-8').read().split('\n')
def cls(ld):
    t=set(re.split(r'[,+]',ld)); out=[]
    if 'BreadcrumbList' in t: out.append('trilha')
    if t&{'Organization','Corporation'}: out.append('organização')
    if t&{'LocalBusiness','ProfessionalService','PestControl'}: out.append('negócio local')
    if t&{'AggregateRating','aggregateRating'}: out.append('nota agregada')
    if 'FAQPage' in t: out.append('perguntas')
    if t&{'Article','TechArticle'}: out.append('artigo')
    if 'Service' in t: out.append('serviço')
    if 'Product' in t: out.append('produto')
    return out
sn=lambda b:'sim' if b else 'não'
falhas=0; conf=0
print('\n=== TABELA DAS DEZ (secao 3) ===')
for ln in md:
    m=re.match(r'\| (\d+) \| `([^`]+)` \|',ln)
    if not m: continue
    c=[x.strip() for x in ln.strip().strip('|').split('|')]
    i=int(c[0]); d=dez[i-1]
    esperado=[d['host']+d['path'], d['words'], d['htmlKB'], d['internos'], d['h2']+d['h3'], d['wa'], d['bairros'], sorted(cls(d['ld'])), sn(d['lic']), sn(d['h24']), sn(d['garantia'])]
    lido=[c[1].strip('`'), int(c[3]), int(c[4]), int(c[5]), int(c[6]), int(c[7]), int(c[8]), sorted(x.strip() for x in c[9].split(',')), c[10], c[11], c[12]]
    for nome,e,l in zip(['pagina','palavras','KB','internos','h2+h3','wa','bairros','ld','lic','24h','garantia'],esperado,lido):
        conf+=1
        if e!=l: falhas+=1; print('  DIVERGE linha',i,nome,'doc=',l,'jsonl=',e)
    print(i,'ok' if esperado==lido else 'DIVERGE',lido[:7],lido[7])
print('valores conferidos',conf,'divergencias',falhas)

print('\n=== MIN / MEDIANA / MAX (secao 4) ===')
for nome,k in (('palavras','words'),('KB','htmlKB'),('internos','internos'),('h2','h2'),('title','titleLen'),('desc','descLen'),('wa','wa'),('imgs','imgs')):
    v=[d[k] for d in dez]; print(nome,min(v),statistics.median(v),max(v),sorted(v))
print('\n=== CONTAGENS (secao 4) ===')
cnt=lambda f:sum(1 for d in dez if f(d))
print('trilha',cnt(lambda d:'trilha' in cls(d['ld'])),'| canonSelf',cnt(lambda d:d['canonSelf']),'| viewport',cnt(lambda d:d['viewport']),'| lang pt-BR',cnt(lambda d:d['lang']=='pt-BR'),'| wa>=1',cnt(lambda d:d['wa']>=1))
print('organizacao',cnt(lambda d:'organização' in cls(d['ld'])),'| negocio local',cnt(lambda d:'negócio local' in cls(d['ld'])),'| nota',cnt(lambda d:'nota agregada' in cls(d['ld'])),'| perguntas',cnt(lambda d:'perguntas' in cls(d['ld'])))
print('24h',cnt(lambda d:d['h24']),'| garantia',cnt(lambda d:d['garantia']),'| lic',cnt(lambda d:d['lic']),'| cnpj',cnt(lambda d:d['cnpj']))
print('forms>0',cnt(lambda d:d['forms']>0),'| mapa',cnt(lambda d:d['mapa']),'| iframes>0',cnt(lambda d:d['iframes']>0),'| hq>0',cnt(lambda d:d['hq']>0),'| seguro',cnt(lambda d:'seguro' in d['vedados']),'| estrelas',cnt(lambda d:d['estrelas']),'| depo',cnt(lambda d:d['depo']))
print('h1==0:',[i+1 for i,d in enumerate(dez) if d['h1']==0],'h1>1:',[i+1 for i,d in enumerate(dez) if d['h1']>1])
print('titleLen declarado x len(title gravado):',[(d['titleLen'],len(d['title'])) for d in dez])
print('campos por linha:',sorted(set(len(d) for d in dez)))
