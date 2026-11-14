#!/usr/bin/env python3
# Segunda passada, reserva 2 - so leitura. Confere o criterio de escolha das dez paginas contra data/serp_sp.csv.
import csv, json, sys
from collections import Counter, defaultdict
BASE='/home/ancastelo/pessoal/SEO_Project/'
rows=list(csv.DictReader(open(BASE+'data/serp_sp.csv',encoding='utf-8')))
org=[r for r in rows if r['superficie']=='orgânico']
ids=sorted(set(r['id'] for r in rows))
print('linhas',len(rows),'organicos',len(org),'buscas (ids distintos)',len(ids),'buscas com organico',len(set(r['id'] for r in org)))
print('grupos:',Counter(r['grupo'] for r in org))
print('ids por grupo:',{g:len(set(r['id'] for r in rows if r['grupo']==g)) for g in sorted(set(r['grupo'] for r in rows))})
print('horas: min',min(r['hora_navegacao'] for r in rows),'max',max(r['hora_navegacao'] for r in rows))
def conta(sub):
    top3=defaultdict(set); top1=defaultdict(set); tipos=defaultdict(set)
    for r in sub:
        p=int(r['posicao']) if r['posicao'] else 99
        k=(r['dominio'],r['caminho'])
        tipos[k].add(r['tipo_pagina'])
        if p<=3: top3[k].add(r['id'])
        if p==1: top1[k].add(r['id'])
    return top3,top1,tipos
dez=[json.loads(l) for l in open(BASE+'data/paginas_top10.jsonl')]
for nome,sub in (('TODO O ARQUIVO',org),):
    top3,top1,tipos=conta(sub)
    print('\n==',nome,'== paginas distintas no top3:',len(top3))
    rank=sorted(top3.items(),key=lambda kv:-len(kv[1]))
    for k,v in rank[:40]:
        print(len(v),len(top1.get(k,())),k[0]+k[1],'|',';'.join(sorted(tipos[k])))
    c=Counter(len(v) for v in top3.values())
    print('distribuicao de aparicoes no top3:',sorted(c.items(),reverse=True))
    print('\nas dez:')
    for i,d in enumerate(dez,1):
        k=(d['host'],d['path'])
        print(i,k[0]+k[1],'top3=',len(top3.get(k,())),'top1=',len(top1.get(k,())), 'ids',sorted(top3.get(k,())))
    # variantes de caminho (com/sem barra)
    for i,d in enumerate(dez,1):
        var=[(k,len(v)) for k,v in top3.items() if k[0]==d['host']]
        print('  host',d['host'],var)

# --- recorte sem o grupo H (o documento diz 709 organicos de 79 buscas; hoje o arquivo tem 795 de 89) ---
semH=[r for r in org if r['grupo']!='H']
print('\n\n=== SEM O GRUPO H === organicos',len(semH),'buscas',len(set(r['id'] for r in semH)))
print('horas do grupo H:',sorted(set((r['id'],r['hora_navegacao'],r['termo']) for r in rows if r['grupo']=='H')))
print('horas sem H: min',min(r['hora_navegacao'] for r in rows if r['grupo']!='H'),'max',max(r['hora_navegacao'] for r in rows if r['grupo']!='H'))
top3,top1,tipos=conta(semH)
rank=sorted(top3.items(),key=lambda kv:-len(kv[1]))
for k,v in rank:
    if len(v)>=2: print(len(v),len(top1.get(k,())),k[0]+k[1],'|',';'.join(sorted(tipos[k])))
c=Counter(len(v) for v in top3.values())
print('distribuicao:',sorted(c.items(),reverse=True))
print('as dez (sem H):')
for i,d in enumerate(dez,1):
    k=(d['host'],d['path'])
    print(i,k[0]+k[1],'top3=',len(top3.get(k,())),'top1=',len(top1.get(k,())))
emp=[k for k,v in top3.items() if len(v)==2]
print('empatadas com 2:',len(emp))
print('sites distintos nas dez:',len(set(d['host'] for d in dez)), Counter(d['host'] for d in dez))
