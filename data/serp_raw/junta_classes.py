#!/usr/bin/env python3
"""Junta a classificação dos domínios (data/serp_dominios_classe_parte*.csv, feita por leitura das páginas) à tabela de
frequência (data/serp_dominios.csv) e gera docs/mercado/serp_sp_dominios.md. Uso: python3 data/serp_raw/junta_classes.py"""
import csv, glob, os, collections
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RAIZ = os.path.dirname(BASE)
rows = list(csv.DictReader(open(os.path.join(BASE, 'serp_sp.csv'), encoding='utf-8')))
org = [r for r in rows if r['superficie'] == 'orgânico']
cls = {}
for f in sorted(glob.glob(os.path.join(BASE, 'serp_dominios_classe_parte*.csv'))):
    for r in csv.DictReader(open(f, encoding='utf-8')): cls[r['dominio'].strip()] = r
SOCIAL = ('instagram.com', 'facebook.com', 'reddit.com', 'youtube.com')
# Leitura harmonizada (sessão principal, 13/11/2026): os dois subagentes usaram critérios diferentes para "gerador de leads ou rede".
# Aqui a classe é refeita pelo que cada um registrou ter VISTO na página, e não pelo rótulo:
#  sem_identificacao = nenhum CNPJ, razão social, endereço nem número de licença visto (parte 1: os 5 classificados só por essa ausência;
#                      parte 2: os 10 marcados "identificação fraca")
#  rede_ou_satelite  = domínio de palavra-chave ou de outra marca, ou rede declarada (parte 2: os 12; parte 1: uniprag e biosolucoes)
SEM_ID = {'protecpragas.com.br', 'exterminex.com.br', 'gallidedetizadora.com.br', 'primosdedetizadora.com.br', 'santanadedetizadora.com.br',
          'insetotec.com.br', 'dedetizadoragalli.com.br', 'kalecpestcontrol.com.br', 'maspredial.com.br', 'ldtechbrasil.com.br', 'ddtize.com.br',
          'letecpragasurbanas.com.br', 'dedetizadorasamurai.com.br', 'osascenter.com.br', 'jupitersp.com.br'}
def harmonizada(d, c):
    if c == 'empresa_licenca_exibida': return 'empresa_com_numero_de_licenca'
    if d in SEM_ID: return 'marca_sem_identificacao_vista'
    if c == 'gerador_de_leads_ou_rede': return 'rede_ou_dominio_satelite'
    if c == 'empresa_sem_licenca_vista': return 'empresa_identificada_sem_numero_de_licenca'
    return c
def classe(d):
    if d in cls: return harmonizada(d, cls[d]['classe']), 'leitura de 1 a 3 páginas do site (subagente, 13/11/2026)'
    if d.endswith('.gov.br') or d in ('puspc.usp.br',): return 'governo_universidade', 'pelo domínio'
    if d in SOCIAL: return 'rede_social_forum', 'pelo domínio'
    return 'nao_classificado', 'não lido'
dom = collections.Counter(r['dominio'] for r in org); cons = collections.defaultdict(set); top3 = collections.Counter()
for r in org:
    cons[r['dominio']].add(r['id'])
    if int(r['posicao']) <= 3: top3[r['dominio']] += 1
campos = ['dominio', 'resultados_organicos', 'consultas_em_que_aparece', 'vezes_no_top3', 'classe', 'classe_do_subagente', 'base_da_classe', 'nome_exibido',
          'licenca_exibida', 'cnpj_exibido', 'sinais_de_rede_ou_intermediacao']
with open(os.path.join(BASE, 'serp_dominios.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=campos); w.writeheader()
    for d, n in dom.most_common():
        c, b = classe(d); x = cls.get(d, {})
        w.writerow(dict(dominio=d, resultados_organicos=n, consultas_em_que_aparece=len(cons[d]), vezes_no_top3=top3[d], classe=c, classe_do_subagente=x.get('classe', ''),
                        base_da_classe=b, nome_exibido=x.get('nome_exibido', ''), licenca_exibida=x.get('licenca_exibida', ''),
                        cnpj_exibido=x.get('cnpj_exibido', ''), sinais_de_rede_ou_intermediacao=x.get('sinais_de_rede_ou_intermediacao', '')))
NOMES = {'empresa_com_numero_de_licenca': 'Empresa com número de licença na página', 'empresa_identificada_sem_numero_de_licenca': 'Empresa identificada (CNPJ, razão social ou endereço), sem número de licença visto',
         'marca_sem_identificacao_vista': 'Marca sem identificação vista (nem CNPJ, nem razão social, nem endereço, nem licença)',
         'rede_ou_dominio_satelite': 'Rede declarada ou domínio satélite (de palavra-chave ou de outra marca)', 'diretorio_marketplace': 'Diretório ou marketplace',
         'governo_universidade': 'Governo ou universidade', 'rede_social_forum': 'Rede social ou fórum', 'outro': 'Outro',
         'nao_abriu': 'Não abriu', 'nao_classificado': 'Não classificado (não lido)'}
ag = collections.defaultdict(lambda: [0, 0, 0, 0])   # domínios, resultados, top3, posição 1
for d, n in dom.items():
    c, _ = classe(d); ag[c][0] += 1; ag[c][1] += n; ag[c][2] += top3[d]
for r in org:
    if r['posicao'] == '1': ag[classe(r['dominio'])[0]][3] += 1
tot = len(org); t3 = sum(top3.values()); p1 = sum(v[3] for v in ag.values())
out = ['# Domínios do resultado orgânico, por classe — anexo de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`', '',
       'Gerado por `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/junta_classes.py`. Classe atribuída por leitura de 1 a 3 páginas de',
       'cada site, por ferramenta que resume; "sem número de licença visto" **não prova** que o site não o exiba em outra página.', '',
       '## Resultados por classe', '', f'| Classe | Domínios | Resultados orgânicos (de {tot}) | Entre os três primeiros (de {t3}) | Na 1ª posição (de {p1}) |', '|---|---|---|---|---|']
for c, v in sorted(ag.items(), key=lambda kv: -kv[1][1]):
    out.append(f'| {NOMES[c]} | {v[0]} | {v[1]} ({round(100*v[1]/tot)}%) | {v[2]} ({round(100*v[2]/t3)}%) | {v[3]} ({round(100*v[3]/p1)}%) |')
out += ['', '## Domínios lidos (ordem de frequência)', '', '| Domínio | Resultados | Buscas | Top 3 | Classe | Nome exibido | Licença (número) | CNPJ | Sinais de rede ou intermediação |', '|---|---|---|---|---|---|---|---|---|']
for d, n in dom.most_common():
    if d in cls:
        x = cls[d]; s = (x.get('sinais_de_rede_ou_intermediacao') or '').replace('|', '/')
        out.append(f"| {d} | {n} | {len(cons[d])} | {top3[d]} | {NOMES[harmonizada(d, x['classe'])]} | {(x.get('nome_exibido') or '').replace('|','/')} | {x.get('licenca_exibida','')} | {x.get('cnpj_exibido','')} | {s} |")
fora = [d for d in cls if d not in dom]
if fora:
    out += ['', '## Lidos que não estão no orgânico da amostra (anunciantes)', '', '| Domínio | Classe | Nome exibido | Licença (número) | Sinais |', '|---|---|---|---|---|']
    for d in fora:
        x = cls[d]; out.append(f"| {d} | {NOMES[harmonizada(d, x['classe'])]} | {x.get('nome_exibido','')} | {x.get('licenca_exibida','')} | {(x.get('sinais_de_rede_ou_intermediacao') or '').replace('|','/')} |")
open(os.path.join(RAIZ, 'docs', 'mercado', 'serp_sp_dominios.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
lidos = sum(dom[d] for d in cls if d in dom)
print('domínios lidos', len(cls), '| cobrem', lidos, 'de', tot, f'resultados ({round(100*lidos/tot)}%)')
for c, v in sorted(ag.items(), key=lambda kv: -kv[1][1]): print(f'  {NOMES[c]}: {v[0]} domínios, {v[1]} resultados ({round(100*v[1]/tot)}%), top3 {v[2]} ({round(100*v[2]/t3)}%), pos1 {v[3]}')
lid = [d for d in cls if d in dom and cls[d]['classe'] not in ('nao_abriu', 'diretorio_marketplace', 'outro')]
print('sites de serviço lidos (no orgânico)', len(lid), '| com número de licença', sum(1 for d in lid if cls[d]['licenca_exibida'].strip().lower() == 'sim'), '| com CNPJ', sum(1 for d in lid if cls[d]['cnpj_exibido'].strip().lower() == 'sim'), '| páginas por bairro', sum(1 for d in lid if cls[d]['paginas_por_bairro'].strip().lower() == 'sim'), '| WhatsApp', sum(1 for d in lid if cls[d]['botao_whatsapp'].strip().lower() == 'sim'))
