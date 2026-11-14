#!/usr/bin/env python3
"""Gera docs/mercado/serp_sp_registro.md: o registro de cada busca ao vivo (termo, hora, logado, local exibido) e o que apareceu.
Uso: python3 data/serp_raw/monta_registro.py"""
import csv, glob, json, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.dirname(BASE)
cons = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, 'serp_consultas.csv'), encoding='utf-8'))}
recs = {}
for f in sorted(glob.glob(os.path.join(BASE, 'serp_raw', 'lote_*.jsonl'))):
    for l in open(f, encoding='utf-8'):
        o = json.loads(l); o['arquivo'] = os.path.basename(f); recs[o['id']] = o
out = ['# Registro das buscas ao vivo — anexo de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`', '',
       'Gerado por `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_registro.py` a partir dos lotes brutos em',
       '`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/`. Todas as buscas: Google (www.google.com), 13/11/2026, horário de Brasília,',
       'navegador pessoal do owner, parâmetros `hl=pt-BR&gl=br&pws=0`. "Local exibido" é o que o Google mostrou no bloco de mapa;',
       '"—" = a página não mostrou local. "IA" = havia "Visão geral criada por IA". Orgânicos = resultados com título na 1ª página.', '',
       '| id | grupo | termo (lido do título da página) | hora da navegação | logado | local exibido | IA | anúncios de texto | perfis no bloco "Empresas" (+ patrocinado) | orgânicos | lote |',
       '|---|---|---|---|---|---|---|---|---|---|---|']
for i, c in cons.items():
    o = recs.get(i)
    if not o:
        out.append(f"| {i} | {c['grupo_descricao']} | {c['termo']} | **não buscado** | — | — | — | — | — | — | — |"); continue
    pat = sum(1 for p in o['pack'] if p.startswith('Patrocinado'))
    out.append(f"| {i} | {c['grupo_descricao']} | {o['q']} | {o['nv']} | {'sim' if o['lg'] else 'não'} | {o['loc'] or '—'} | {'sim' if o['aio'] else 'não'} | {len(o['ads'])} | {len(o['pack']) - pat}{' + 1' if pat else ''} | {len(o['org'])} | {o['arquivo']} |")
out += ['', f"Total: {len(recs)} buscas com registro, de {len(cons)} planejadas."]
os.makedirs(os.path.join(RAIZ, 'docs', 'mercado'), exist_ok=True)
open(os.path.join(RAIZ, 'docs', 'mercado', 'serp_sp_registro.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
dif = [(i, cons[i]['termo'], recs[i]['q']) for i in recs if cons[i]['termo'].lower() != recs[i]['q'].lower()]
print('registros', len(recs), '| termo planejado ≠ título lido:', dif)
