# Ficha de frente — 10. Controle de pragas (pessoal)

Preenchida em 13/11/2026 por leitura de `/home/ancastelo/pessoal/SEO_Project` (8 arquivos, todos de 25/09/2026
20:44–21:31 BRT; **não é repositório git**; está fora de `~/pessoal`) e do transcript
`/home/ancastelo/.claude/projects/-home-ancastelo-work-core-banking/ff795d73-a0b2-423a-8f5b-4f5ca254d59b.jsonl`
(283 registros, 25/09 22:53Z → 26/09 00:31Z; 0 compactações; 2 prompts humanos). Molde de referência:
`/home/ancastelo/Pessoal/microverdes` (também fora de git). Pasta abreviada abaixo como `CP`; destino aprovado da
migração (a cargo da orquestradora): `/home/ancastelo/pessoal/SEO_Project`.

## 1. Para quem é e o que destrava

Leitor final: o owner, como fundador em potencial. O estudo responde se vale montar, em fases, uma empresa de controle de
pragas em SP com o gatilho "pró-labore ≥ salário líquido atual" para sair do CLT (`CP/PROMPT_PLANO.md` linhas 12–14).
Entregáveis definidos: simulador no Google Sheets, dossiê de pesquisa, mapa comparativo de modelos de negócio, parecer
go/no-go e playbook de 30 dias (linhas 93–119). Prazo conhecido: nenhum; o owner não voltou ao tema desde 26/09.

## 2. Estado verificado

**Sobre "O computador reiniciou, volte com as perguntas" (prompt de 25/09 23:41Z).** Era o segundo e último prompt
humano, mas **a sessão não parou nele**: a Fable retomou os 4 agentes de pesquisa (registros L159–L162) e fez três
rodadas de `AskUserQuestion`, **todas respondidas pelo owner**:
- Rodada 1 (L176, respondida 23:44Z): objetivo (empresa para sair do CLT, faseada), recursos por gatilho (iguais ao
  microverdes, com flexibilidade; sem sócio), lead-gen vs intermediação (quis o debate), RT (modelar os dois cenários).
- Rodada 2 (L208, respondida 26/09 00:06Z): formação (engenharia civil, CREA inativo), geografia (centro expandido),
  SEO (nenhuma experiência), entregáveis (mesmo formato do microverdes + 1 item: mapa de modelos de negócio).
- Rodada 3 (L250, respondida 00:30Z): rota do E3 (decidir pelo simulador), público (híbrido B2C caixa + B2B ativo),
  validação do E0 (três canais em paralelo: Ads, SEO, prospecção direta).
As respostas estão consolidadas em `CP/PROMPT_PLANO.md` §"Contexto e decisões do fundador" (linhas 11–32). **Não há
pergunta pendente para o owner desse ciclo.** A única pergunta sem resposta é a última do assistente (L276): "quer
registrar no compound o aprendizado de que a regulação elimina o estágio caseiro e barra a revenda com marca própria?".

**O que existe (tudo de 25–26/09; sem alteração desde então, por mtime)**

| Artefato | Estado | Evidência |
|---|---|---|
| Pesquisa 01 regulação e licenças (RDC 622/2022, CVS 9/2000 e 1/2024, licença Risco III, RT, MEI vs ME, Lei 12.268/96, legalidade do lead-gen) | pronta; 10 seções; §9 com 8 divergências; §10 com 10 fontes inacessíveis | `CP/research/01_regulacao_licencas.md` linhas 10–22 (resumo), 219–245 |
| Pesquisa 02 mercado, serviços, preços, concorrência | pronta; §9 com 9 divergências; §10 lacunas (Maps, Trends, Keyword Planner exigem navegador/conta) | `CP/research/02_mercado_servicos_precos.md` linhas 238–262 |
| Pesquisa 03 modelos de negócio e escala (lead-gen, rank-and-rent, própria, franquia, compra, sociedade) | pronta; §8 tabela de divergências; "incertezas que mais pesam" listadas | `CP/research/03_modelos_negocio_escala.md` linhas 172–200 |
| Pesquisa 04 mão de obra, custos, unit economics | pronta; §9 com 10 divergências (CCT 2026 é PDF-imagem, piso inferido) | `CP/research/04_mao_de_obra_custos_operacao.md` linhas 289–315 |
| `data/servicos.csv` (21 serviços), `data/concorrentes_sp.csv` (21), `data/custos_operacao.csv` (79) — colunas com fonte e confiança | prontos, **não curados** (sem `data/final/` como no microverdes) | `ls CP/data`; cabeçalhos lidos em 13/11 |
| `PROMPT_PLANO.md` — prompt-mestre para o modo plano (4 especialistas, 5 achados a respeitar, 3 verificações cruzadas, 9 lacunas a pesquisar, estágios E0–E5, 5 entregáveis) | pronto; **nunca executado** | `CP/PROMPT_PLANO.md` (128 linhas) |
| Simulador, dossiê, mapa de modelos, parecer, playbook | **não iniciados** (não há `docs/` nem `*.py` em `CP`) | árvore da pasta |
| Memória: 2 entradas no meli-memory, escopo `personal` (ids 322 e 323) com as premissas e os achados | existem; **conflitam com a regra de 04/11** de não usar meli-memory em projetos pessoais (`~/pessoal/carreira/CLAUDE.md` linha 10) | transcript L189, L243, L271 |

**Ferramentas reutilizáveis do microverdes** (`PROMPT_PLANO.md` linhas 41–44): `gsheets.py` (cliente Sheets via
`~/.claude/gdrive-helper.py`, token do gcloud), `build_simulator.py` (58 KB), `curate.py` (research → `data/final/`),
`check_model.py` e `stress_test.py` (recálculo em Python puro), e os 4 docs em `/home/ancastelo/Pessoal/microverdes/docs/`.
O `gcloud auth list` mostra duas contas (uma pessoal, uma corporativa); **não verificado** qual delas o helper usa nem em
qual Drive a pasta "Pessoal – Microverdes" está (`/home/ancastelo/Pessoal/microverdes/DRIVE_IDS.md`).

## 3. Itens em aberto

| ID | Item | Condição de término verificável | Depende do owner? | Cabe na fronteira? | BigQuery | Horas de relógio | Paralelizável? | Valor e por quê |
|---|---|---|---|---|---|---|---|---|
| P0 | **Pré-requisito**: migração para `~/pessoal/SEO_Project` + `git init -b main` + remoto `git@github-pessoal:castelo1/SEO_Project.git` + 1º push | `git -C ~/pessoal/SEO_Project rev-list --count @{u}..HEAD` = 0; `.gitignore` com `*.local.*` | **Sim**: o repositório privado no GitHub é criado **pelo navegador pessoal, logado como castelo1** (`~/pessoal/CLAUDE.md` regra 3); sem ele não há push e o Stop hook bloqueia todo fim de turno em `~/pessoal/*` | Sim (mover arquivos, sem rede além do push) | nenhum | 15 min dele + 15 min | Não | **Bloqueante** para qualquer trabalho em `~/pessoal` |
| P1 | **Curadoria** (`curate.py` no molde do microverdes): `data/final/premissas.csv` com mín/base/máx, unidade, fonte, confiança e nota de curadoria por item, a partir dos 3 CSVs + research; lista explícita das premissas Baixa | `data/final/*.csv` gerados por script reproduzível; 100% das linhas com fonte e confiança; divergências dos §9 anotadas como faixa | Não | Sim | nenhum | 2–3 h | Sim (por CSV) | **Alto** — base de todo o resto; sem ela o simulador repete o erro do TCC que o microverdes evitou |
| P2 | **Mapa comparativo de modelos de negócio** (`docs/mapa_modelos_negocio.md`, o item que o owner pediu a mais): lead-gen, rank-and-rent, própria, franquia, compra de carteira, sociedade — capital, horas, risco regulatório, valor do ativo, onde entra na jornada E0–E5 | Doc com uma linha por modelo e as 5 restrições de `PROMPT_PLANO.md` linhas 47–57 respeitadas; cada número com fonte do research | Não | Sim | nenhum | 2 h | Sim | **Alto** — é o que o owner disse não saber ("muito pouco sobre modelos de negócio", transcript L18) |
| P3a | **Desenho do simulador** (`docs/simulador_estrutura.md`): abas, inputs com fonte/confiança, duas unidades econômicas (lead e serviço/contrato), demanda × capacidade, carteira recorrente, tempo do dono, comparador das 3 rotas do E3, linha "saída do CLT", tornado | Doc com toda a lista de `PROMPT_PLANO.md` linhas 94–108 mapeada em abas e named ranges; perguntas de desenho marcadas | **Sim para construir** (linha 122: "revisar a estrutura com o fundador antes de construir"); não para desenhar | Sim | nenhum | 2 h | Não | **Alto** — é o gate que o owner julga na segunda |
| P3b | **Modelo em Python puro** (`check_model.py`-style) sobre `data/final/`: P&L e caixa 36 meses, 3 cenários, 3 rotas do E3, break-even, payback/VPL/TIR vs CDI, mês de saída do CLT com salário como variável de entrada | Script roda sem rede; tabela de saídas por cenário × rota em `docs/`; teste de sanidade (vendido ≤ min(capacidade, demanda)) | Não (salário líquido fica como placeholder; o owner preenche depois) | Sim | nenhum | 4–6 h | Parcial | **Alto** — permite um parecer preliminar sem tocar o Sheets nem a conta Google |
| P4 | **Dossiê de pesquisa v0** (`docs/dossie_pesquisa.md`): método, fontes, faixas, confiança, as 3 verificações cruzadas pedidas (NF da licenciada; faixa 3× do contrato mensal; GVS × COVISA) e as 9 lacunas de `PROMPT_PLANO.md` linhas 68–78 | Doc no formato do microverdes; seção "Verificação cruzada" preenchida ou marcada "não verificado: exige fonte primária" | Não | **Depende de a rodada poder ler a web** para a verificação cruzada; sem web sai v0 só com o que já está no research | nenhum | 2 h sem web / +4 h com web | Sim | **Alto-médio** — o `PROMPT_PLANO.md` manda fazer isto antes de qualquer número entrar na planilha |
| P5 | Parecer go/no-go preliminar + playbook de 30 dias (rascunho) a partir de P1–P4, com premissas Baixa no topo do tornado | Dois docs no formato de `/home/ancastelo/Pessoal/microverdes/docs/`; cada veredito remete a uma linha de `data/final/` | Não para rascunhar; sim para valer (preferências de risco, horas dele) | Sim | nenhum | 3 h | Não (depende de P3b) | **Médio** — útil só como rascunho marcado; as premissas decisivas ainda são Baixa |
| P6 | Simulador no Google Sheets (`build_simulator.py` adaptado) | Planilha criada, `check_model` bate com as fórmulas | **Sim**: aprovar P3a; dizer a conta Google (pessoal) e a pasta de destino; token do helper válido | Não neste fim de semana: cria arquivo fora do repo, em Drive de conta a confirmar | nenhum | 6–8 h | Não | Alto, mas fora de ordem antes do P3a aprovado |
| P7 | Pesquisas que exigem login ou navegador: volume de busca e CPC (Keyword Planner), custo do lead no GetNinjas (conta de profissional), notas no Google Maps dos concorrentes do centro, PDF-imagem da CCT 2026, consulta ao CREA-SP/GVS sobre RT e licenciamento | — | **Sim** (contas dele, telefonemas, cliente oculto) | Não | — | — | — | Alto para a decisão, mas é trabalho dele |
| P8 | Higiene: mover as 2 entradas de meli-memory (ids 322, 323) para memória local do projeto e apagá-las do gateway; responder à pergunta de compound de 26/09 | Entradas apagadas; `docs/` ou `CLAUDE.md` do projeto com as premissas | **Sim** (apagar memória e compound só com "sim" dele) | — | — | 20 min | — | Baixo em valor, alto em coerência com a regra de 04/11 |

## 4. O que esta frente faria com 48 horas sem o owner

Só depois do **P0** (migração + repo privado criado pelo owner). Sessão própria em `~/pessoal/SEO_Project` (para valerem
as regras de `~/pessoal/CLAUDE.md` e o hook de git, e para não herdar o protocolo meli-memory do core-banking).
1. `CLAUDE.md` do projeto (molde do de `carreira`: sem meli-memory, sem conectores corporativos, segredos fora, commit e
   push por etapa) + `.gitignore`; copiar `gsheets.py`/`curate.py`/`check_model.py` do microverdes como base.
2. **P1** e **P2** em paralelo (2 subagentes); commit.
3. **P4 v0** em paralelo com o passo 2; se a web estiver autorizada, as 3 verificações cruzadas e as lacunas sem login
   (CREA-SP/CONFEA, CVS 33/2008, TFE municipal, dispensa CETESB, anúncios de dedetizadoras à venda, aluguel de imóvel
   térreo no centro) em 1 subagente, com URL, data e confiança por item.
4. **P3a** (desenho) e depois **P3b** (modelo em Python) em série; commit.
5. **P5** só se P3b passar o teste de sanidade; rascunho marcado "preliminar: premissas Baixa".
6. Total ≈ 12–16 h de relógio. Onde escreve: `~/pessoal/SEO_Project/{data/final,docs,tools}`; nada no core-banking;
   nada no Drive.

## 5. O que o owner lê na segunda

- `/home/ancastelo/pessoal/SEO_Project/docs/simulador_estrutura.md` — aprova ou corrige a estrutura antes do Sheets
  (gate do `PROMPT_PLANO.md` linha 122) (10 min).
- `/home/ancastelo/pessoal/SEO_Project/docs/mapa_modelos_negocio.md` — lê para decidir se a tese híbrida (lead-gen
  como ponte → carteira B2B) continua (10 min).
- `/home/ancastelo/pessoal/SEO_Project/docs/parecer_go_no_go.md` (preliminar) — só a seção "premissas Baixa que
  mandam no resultado": é a lista do que ele mesmo precisa medir (P7) (5 min).
- `/home/ancastelo/pessoal/SEO_Project/docs/dossie_pesquisa.md` — não precisa ler; só a tabela "verificação cruzada"
  se quiser conferir o que mudou (3 min).

## 6. Riscos e armadilhas

- **Stop hook de git**: em `~/pessoal/*` o hook bloqueia o fim do turno se a pasta não for repo, se o remoto não for
  `github-pessoal:castelo1` ou se houver commit sem push (`~/.claude/hooks/pessoal-git-guard.sh` linhas 11–22). Sem o
  repo remoto criado pelo owner, uma rodada autônoma em `~/pessoal/SEO_Project` **trava em todo turno**. Alternativa
  se ele não criar: a orquestradora deixa a pasta fora de `~/pessoal` até segunda (contraria a migração aprovada) ou
  trabalha com `stop_hook_active` — não recomendado.
- **Memória corporativa**: a sessão de 25/09 gravou premissas pessoais no meli-memory (escopo `personal`, ids 322 e 323).
  A regra de 04/11 proíbe isso em projetos pessoais; subagente lançado do core-banking herdaria o "mem_save obrigatório".
- **Relatório de subagente é hipótese**: `PROMPT_PLANO.md` linhas 61–67 registra que o research/04 ("intermediação com
  repasse 60–75%") contradiz o research/01 (NF só da licenciada) e manda resolver como comissão com NF da licenciada; a
  faixa de 3× no contrato mensal e GVS × COVISA também estão sem fonte primária. Nenhum número entra em `data/final/`
  sem anotar isso.
- **Fronteira de rede**: a pesquisa original usou WebSearch/WebFetch; a fronteira do `_MODELO.md` não cita web. Sem
  autorização, P4 fica em v0 e as 9 lacunas continuam abertas.
- **Conta Google**: o `gdrive-helper.py` usa o token do gcloud, que tem conta pessoal e corporativa logadas; criar o Sheets
  na conta errada violaria "nada da empresa / nada no Drive corporativo". Por isso P6 fica fora.
- **Dado pessoal no modelo**: o salário líquido é input do simulador (`PROMPT_PLANO.md` linha 13; transcript L276). Fica
  como campo vazio ou `*.local.*`; nunca no git nem nos docs.
- **Molde parcialmente inaplicável**: o microverdes tinha estágio "em casa" com R$ ~0; aqui a regulação o elimina
  (`PROMPT_PLANO.md` linha 47). Copiar `build_simulator.py` sem redesenhar os estágios reproduz o erro.

## 7. Modo recomendado

**Workflow de subagentes numa sessão própria (12–16 h de relógio), effort high — mas só se o P0 fechar antes de
sexta à noite.** Razão: há trabalho de síntese e modelagem de valor alto que não depende de preferência do owner (P1–P4,
P3b), e o estudo nunca saiu da fase de pesquisa. Se o P0 não fechar, **não rodar neste fim de semana**: o hook de git
inviabiliza a pasta em `~/pessoal` e rodar fora dela contraria a decisão de migração.

## 8. Perguntas que só o owner responde

1. **Cria hoje o repositório privado vazio `castelo1/SEO_Project` no GitHub (navegador pessoal)?** Padrão se não
   responder: a frente **não roda**; a orquestradora só move a pasta e deixa o `git init` + remoto prontos para o 1º push.
2. **A rodada pode pesquisar na web (leitura de fontes públicas, sem login) para a verificação cruzada e as lacunas?**
   Padrão: não; P4 sai em v0 marcando "não verificado: exige fonte primária".
3. **Qual conta Google e pasta do Drive para o simulador, quando chegar a hora?** Padrão: nenhum Sheets neste fim de
   semana; o modelo fica em Python + CSV no repo (P3b), e o Sheets espera a resposta.
