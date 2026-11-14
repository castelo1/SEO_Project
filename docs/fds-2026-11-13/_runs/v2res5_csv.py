#!/usr/bin/env python3
# Segunda passada, reserva 5 - so leitura. Confere data/medicao_modelo.csv e as definicoes de docs/medicao_modelo.md.
import csv, re, io, datetime
BASE='/home/ancastelo/pessoal/SEO_Project/'
raw=open(BASE+'data/medicao_modelo.csv','rb').read()
print('bytes',len(raw),'| BOM',raw[:3]==b'\xef\xbb\xbf','| CRLF',b'\r\n' in raw,'| termina com \\n',raw.endswith(b'\n'),'| linhas fisicas',raw.count(b'\n'))
txt=raw.decode('utf-8')
rows=list(csv.reader(io.StringIO(txt)))
print('linhas logicas',len(rows),'| campos por linha',[len(r) for r in rows])
cab=rows[0]
print('cabecalho unico?',len(cab)==len(set(cab)),'| vazios no cabecalho',[c for c in cab if not c.strip()],'| so minusculas/ascii/_ ?',all(re.fullmatch(r'[a-z0-9_]+',c) for c in cab))
md=open(BASE+'docs/medicao_modelo.md',encoding='utf-8').read()
tab=md.split('## Colunas')[1].split('## Contas')[0]
defs=[]; linhas_def=[]
for ln in tab.split('\n'):
    if ln.startswith('| `'):
        c=[x.strip() for x in ln.strip().strip('|').split('|')]
        nomes=re.findall(r'`([a-z0-9_]+)`',c[0])
        defs+=nomes; linhas_def.append((nomes,c))
print('colunas no CSV',len(cab),'| colunas definidas no .md',len(defs))
print('no CSV sem definicao:',[c for c in cab if c not in defs])
print('definidas sem coluna no CSV:',[d for d in defs if d not in cab])
print('mesma ordem?',cab==defs)
print('\n--- por definicao: tem "o que e", "de onde vem", "quem preenche", "base"? ---')
for nomes,c in linhas_def:
    falta=[n for n,v in zip(['o que e','de onde vem','quem preenche','base'],c[1:5]) if v in ('','—','-')]
    freq=bool(re.search(r'período|periodo|mensal|28 dias|mês|semana',c[1]+c[2],re.I))
    print(','.join(nomes),'| quem:',c[3],'| de onde:',c[2][:60],'| lacunas:',falta,'| fala de periodicidade na linha:',freq)
# colunas citadas no .md fora da tabela existem?
cit=set(re.findall(r'`([a-z_]+)`',md))
print('\nnomes entre crases no .md que nao sao coluna:',sorted(x for x in cit if x not in cab and '_' in x))
print('\n--- linhas de exemplo ---')
for r in rows[1:]:
    d=dict(zip(cab,r))
    i0=datetime.date.fromisoformat(d['periodo_inicio']); i1=datetime.date.fromisoformat(d['periodo_fim'])
    print('exemplo=',d['exemplo'],'| periodo',d['periodo_inicio'],d['periodo_fim'],'dias inclusive',(i1-i0).days+1,'| pagina',d['pagina'],d['tipo_pagina'],'| licenciada',repr(d['licenciada']))
    print('   marcado EXEMPLO na observacao?', 'EXEMPLO' in d['observacao'],'| licenciada com EXEMPLO?',('EXEMPLO' in d['licenciada']) if d['licenciada'] else 'vazia')
    imp=d['impressoes']; cl=d['cliques_na_busca']; t=d['taxa_de_clique']
    if imp not in ('','0'): print('   taxa esperada',int(cl)/int(imp),'declarada',t)
    else: print('   impressoes =',repr(imp),'-> taxa deve ser vazia: ',t=='','| posicao_media vazia:',d['posicao_media']=='')
    print('   buscas a mao',repr(d['buscas_conferidas_a_mao']),'-> posicao_na_tela vazia:',d['posicao_na_tela_mediana']=='')
    lv=d['leads_vendidos']; p=d['preco_combinado_reais']; rc=d['receita_reais']
    print('   leads_vendidos',repr(lv),'preco',repr(p),'receita',repr(rc),'forma',repr(d['forma_de_cobranca']),'| coerente:', (rc=='' and lv=='') or (lv!='' and p!='' and rc!='' and float(rc)==float(lv)*float(p)))
    print('   validos',repr(d['leads_validos']),'orcamentos',repr(d['orcamentos']),'fechados',repr(d['servicos_fechados']),'toques',repr(d['leads_toque_no_botao']),'formulario',repr(d['leads_pedido_formulario']))
    nz=[k for k,v in d.items() if re.fullmatch(r'[0-9.]+',v) and float(v)!=0]
    print('   colunas numericas diferentes de zero:',nz)
