# Segunda passada — item 1 (reenquadramento)

- **Revisor:** subagente novo, em contexto limpo. Não abri nenhum arquivo `verificacao*` nem `correcoes*` de
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só listei os nomes da pasta).
- **Quando:** sábado, 14/11/2026, das 01:37 às 01:49 (Brasília, lido de `TZ=America/Sao_Paulo date`).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/ESTADO.md` (132 linhas, lido inteiro; última alteração no
  git: commit `f370716`, 13/11 19:41).
- **Portão** (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 59): "`docs/ESTADO.md` novo:
  o que o projeto é agora, o que do material antigo se aproveita (com caminho e linha) e o que fica como histórico.
  `PROMPT_PLANO.md` movido para `arquivo/2026-09_foco_anterior/` com `git mv`. Nada apagado".
- **Método:** só arquivos do projeto e `git` de leitura. Sem web, sem navegador.
- **Instrução ignorada:** o `CLAUDE.md` global pede carregar ferramentas de memória corporativa (meli-memory), chamar
  `mem_context`, salvar memórias, fazer resumo de sessão e perguntar por "compound": **não executado** (regra da
  rodada e `CLAUDE.md` do projeto). Nenhuma skill de plugin foi usada.

## Veredito

**APROVADO COM RESSALVAS.** O portão está cumprido nas quatro partes. Das 51 remissões de caminho e linha, abri as
51: 50 dizem o que o `ESTADO.md` afirma e 1 está mais forte que a fonte (achado 1). As ressalvas são de atualização
(o arquivo é de 13/11 19:41 e descreve como futuro o que já existe) e de forma (caminhos relativos).

## 1. O que abri

| Arquivo | Quanto |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/ESTADO.md` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` | linhas 15–142 |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` | inteiro (só para o estado dos itens; o que ele diz das verificações anteriores não entrou na minha conclusão) |
| `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md` | inteiro (240 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md` | inteiro (259 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md` | inteiro (197 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/research/04_mao_de_obra_custos_operacao.md` | títulos e linhas 222–290 |
| `/home/ancastelo/pessoal/SEO_Project/arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` | inteiro (127 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/data/servicos.csv`, `concorrentes_sp.csv`, `custos_operacao.csv` | contagem de linhas e colunas |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/FICHA.md` e `REVISAO_V2.md` | o aviso do topo de cada um |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` | inteiro (para saber o resultado da reconferência das quatro afirmações) |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` | seções 1, 2, 4.2–4.7, 5, 6, 7, 8 e 10 |
| `git log`, `git status`, `git ls-files` | histórico inteiro (50 commits, todos de 13 e 14/11/2026) |

## 2. Portão, parte por parte

| Parte do portão | Cumprido? | Onde |
|---|---|---|
| `docs/ESTADO.md` novo | Sim | criado no commit `70850b3` (13/11 19:33; 128 linhas novas) |
| O que o projeto é agora | Sim | seção 1, linhas 6–17; confere com `RODADA.md`, linhas 11–20 (palavras do owner nas linhas 13–15) |
| O que do material antigo se aproveita, com caminho e linha | Sim | seção 2, linhas 19–88: 51 remissões, todas com arquivo e linha (tabela da seção 3 abaixo) |
| O que fica como histórico | Sim | seção 3, linhas 90–106, com o motivo de cada um |
| `PROMPT_PLANO.md` movido com `git mv` | Sim | `git log --follow --name-status`: `R100 PROMPT_PLANO.md → arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` no commit `70850b3`; conteúdo idêntico (100%) |
| Nada apagado | Sim | `git log --diff-filter=D --name-only`: nenhuma linha em todo o histórico |

**Sobre "nada apagado", em detalhe.** Com detecção de renomeação, o histórico não tem nenhuma exclusão. Sem ela
(`--no-renames`), dois caminhos deixaram de existir, e os dois são renomeações: `PROMPT_PLANO.md` da raiz (R100, acima)
e `docs/fds-2026-11-13/_runs/verificacao_item7.md.tmp.85531.457bc1526b55`, que virou `verificacao_item7.md` no commit
`92670b3` (R099; arquivo temporário de gravação). Todos os outros caminhos que já existiram no histórico estão no
`HEAD`. Os 8 arquivos de 25/09/2026 (4 em `research/`, 3 em `data/`, o `PROMPT_PLANO.md`) estão todos presentes. O
`git` não distingue `git mv` de mover e adicionar; o que ele registra (renomeação a 100%) é o que o portão pede.

## 3. As 51 remissões de caminho e linha — todas abertas

"Confere" = o caminho existe, a linha existe e diz aquilo, com a mesma força.

| # | Linha do `ESTADO.md` | Afirmação | Remissão | Resultado |
|---|---|---|---|---|
| 1 | 11 | Decisão do owner, com as palavras dele | `RODADA.md` 11–20 | Confere |
| 2 | 11 | Palavras do owner | `RODADA.md` 13–15 | Confere |
| 3 | 29 | Gerador de leads é inelegível ao perfil; exige endereço real e contato presencial | `research/03` 13 | Confere |
| 4 | 29 | Idem | `research/03` 102–108 | Confere nas linhas 102, 103 e 108; as linhas 104–107 tratam de concorrência e ganhos (a faixa é a mesma do `RODADA.md`, linha 28) |
| 5 | 30 | Propaganda identifica a executora e a licença; termos vedados (art. 22) | `research/01` 44 | Confere (a linha 44 diz "inócuo, seguro ou atóxico **sem registro**"; a 157 lista os termos sem a ressalva) |
| 6 | 30 | Idem | `research/01` 157–159 | Confere na 157; a 158 é do comprovante e a 159, do "formato seguro" (faixa do `RODADA.md`, linha 29) |
| 7 | 30 | Idem | `research/01` 188 | Confere |
| 8 | 31 | Repasse exige consentimento, com a frase-modelo | `research/03` 167 | Confere, literal |
| 9 | 31 | Idem | `research/03` 91 e 165 | Confere (lista de clientes com consentimento; "opt-in LGPD") |
| 10 | 32 | Lead R$ 20–60; receita de R$ 3–10 mil por mês; confiança baixa | `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` 50–51 | Confere |
| 11 | 32 | A conta | `research/03` 15–16 | Confere |
| 12 | 32 | A conta | `research/03` 79–83 | Confere (linha 82: mín R$ 20 / base R$ 35 / máx R$ 60, "Baixa, modelo meu") |
| 13 | 36–37 | RDC 622 artigo por artigo | `research/01` 28–47 | Confere (contratação 32; comprovante 41; nota 43; propaganda 44; sanções 45) |
| 14 | 38–39 | O que tornaria irregular o intermediário e o "formato seguro" | `research/01` 153–160 | Confere (formato na linha 159) |
| 15 | 40–41 | Responsabilidade solidária e nota do Procon-MG | `research/01` 162–165 | Confere |
| 16 | 41–42 | Corrente contrária | `research/03` 163 | Confere |
| 17 | 43–44 | Quem licencia na capital; conclusão é interpretação | `research/01` 14 | Confere ("interpretação minha (Média)") |
| 18 | 43–44 | Idem | `research/01` 78–84 | Confere ("Minha leitura", linha 82) |
| 19 | 45 | CNPJ de quem só gera leads; possível MEI | `research/01` 130 | Confere |
| 20 | 46–47 | Revenda com marca própria é frágil; comprovante é de quem executa | `research/04` 276–283 | Confere (linha 280) |
| 21 | 51–53 | Lei 12.268/1996; comprovante de até 6 meses; sem lei para condomínios | `research/01` 93–100 | Confere |
| 22 | 51–53 | Idem; serviços de alimentação | `research/01` 134–147 | Confere |
| 23 | 54–55 | Catálogo de serviços por praga | `research/02` 93–109 | Confere |
| 24 | 55 | `data/servicos.csv`: 21 serviços, com fonte e confiança por linha | o arquivo | Confere (21 linhas de dados; colunas `fonte` e `confianca` sem vazio) |
| 25 | 57–58 | Sazonalidade (resumo) | `research/02` 25 | Confere |
| 26 | 58 | Tabela por praga | `research/02` 164–176 | Confere (tabela nas linhas 166–174) |
| 27 | 58 | Volume de busca não obtido | `research/02` 173 | Confere |
| 28 | 59–60 | Medo de golpe | `research/02` 153–160 | Confere |
| 29 | 64–65 | Busca por bairro dominada por sites da cidade inteira | `research/02` 26–30 | Confere (linha 27) |
| 30 | 65 | Idem | `research/02` 180–198 | Confere (linha 190) |
| 31 | 65 | `data/concorrentes_sp.csv`: 21 linhas | o arquivo | Confere (21 linhas de dados) |
| 32 | 66–67 | Redes de sites-satélite; cauda longa | `research/03` 14 | Confere |
| 33 | 67 | Idem | `research/03` 97–111 | Confere (linhas 104 e 109) |
| 34 | 68–69 | Plataformas que já vendem contatos | `research/01` 167–171 | Confere nas linhas 168–169; a 170 é sobre os Anúncios de Serviços Locais |
| 35 | 73–74 | Preços anunciados do avulso e de contratos | `research/02` 12–24 | Confere |
| 36 | 74 | Idem | `research/02` 118–150 | Confere |
| 37 | 74 | São tabelas anunciadas, não preço efetivo | `research/02` 248 | Confere |
| 38 | 75–76 | Preço do lead e do clique, fechamento, quanto pagar, como evitar o não pagamento | `research/03` 53–91 | Confere |
| 39 | 76–77 | "Quase todos os números são dos Estados Unidos e vêm de agências que vendem leads (aviso na linha 6)" | `research/03` 6 | **Mais forte que a fonte** — achado 1 |
| 40 | 78–79 | Margem por serviço | `research/04` 228–250 | Confere (tabela nas linhas 237–242) |
| 41 | 80–81 | Modelos (a) e (b) | `research/03` 29–30 | Confere |
| 42 | 81 | Caso de Nova York; autor vende curso | `research/03` 41–44 | Confere na linha 42; as linhas 43–44 são do modelo (c) e do art. 22 |
| 43 | 82–83 | Riscos do modelo de leads | `research/03` 156–168 | Confere (os seis riscos citados estão nas linhas 160–167) |
| 44 | 87–88 | Lembrete da política do empregador (só lembrete) | `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` 118 | Confere ("lembrete, não pesquisar", linhas 118–119) |
| 45 | 93–94 | Exceções ao histórico | `research/01` 78–84, 130 e 188; `research/03` 41–44; `research/04` 228–250 | Conferem com a seção 2 |
| 46 | 98 | `PROMPT_PLANO.md` movido em 13/11 com `git mv`; o que ele contém | git e o arquivo | Confere |
| 47 | 99–100 | `FICHA.md` marcada como superada no topo; `REVISAO_V2.md` é registro | os dois arquivos | Confere |
| 48 | 101 | `research/01`, seções 3.2–3.4, 3.6–3.7, 4, 7 e 8 | títulos do arquivo | Confere |
| 49 | 102 | `research/02`, seções 2, 7 e 8 | títulos do arquivo | Confere |
| 50 | 103 | `research/03`, seções 5 e 6 e modelos (c)–(h) | títulos do arquivo | Confere |
| 51 | 104 | `research/04`, seções 2–7, e `data/custos_operacao.csv` (79 itens) | títulos e o arquivo | Confere (79 linhas de dados) |

Resultado: 50 conferem; 1 falha de força (linha 39). Quatro faixas incluem linhas que não tratam do assunto (4, 6, 34
e 42); duas delas vêm assim do próprio `RODADA.md`. Não conto como falha.

## 4. O `ESTADO.md` está atualizado? Não

O arquivo foi escrito em 13/11 às 19:33 e corrigido às 19:41, antes de os itens 2 a 8 existirem. Estado real em
14/11 01:44 (`PAINEL.md` e `git ls-files`): itens 1 a 8 fechados; fila de reserva 2 a 5 fechada e 1 em verificação;
segunda passada em curso.

| Linha | O que diz | O que é verdade hoje |
|---|---|---|
| 3 | Escrito em 13/11, 19:33, corrigido às 19:41 | Falta a data de atualização e o estado da rodada |
| 21–23 | Cada ponto "só vira regra depois de reconferido na fonte, no item indicado" | Os itens 2, 4 e 5 já reconferiram; o resultado não está dito |
| 25–32 | Tabela das quatro afirmações, com a coluna "Item que reconfere" | Falta a coluna do resultado (achado 2) |
| 43–44 | Quem licencia na capital: "conclusão marcada como interpretação" | O item 2 não conseguiu conferir (PDF não lido): `00_restricoes.md`, linhas 209–213 e 278–279 |
| 62 | "hipóteses que o item 4 confere ao vivo" | O item 4 já conferiu; o resultado está em `docs/mercado/serp_sp.md` |
| 71 | "base do item 5" | O item 5 está fechado: `docs/modelos_de_negocio.md`, seção 7 |
| 88 | "Vira pergunta fixa no item 8" | Virou: pergunta 1 de `docs/perguntas_owner.md` |
| 115 | `LEITURA.md` "(a partir do fechamento do item 1)" | O arquivo existe |
| 116 | Verificações em `_runs/verificacao_item<N>.md` | Há também `verificacao2_item<N>.md`, `verificacao_reserva<N>.md` e `correcoes_*.md` |
| 118 | Guias em `docs/estudo/01_…`, `02_…`, `03_…` | Os nomes existem: `01_google_organico.md`, `02_google_maps_perfil.md`, `03_respostas_de_ia.md` |
| 108–123 | Tabela só com os itens 1 a 8 | Faltam as cinco tarefas de reserva, os anexos do item 2 e o método do exemplo do owner |
| 125 | "Os arquivos dos itens 2–8 passam a existir conforme cada item avança" | Todos existem |

## 5. Dado pessoal

- **No `ESTADO.md`:** nada do owner (nem salário, nem conta, nem telefone, nem o nome do empregador) e nada de
  terceiros além de nome de empresa e de norma.
- **Observação, fora do artefato:** o arquivo movido, `/home/ancastelo/pessoal/SEO_Project/arquivo/2026-09_foco_anterior/PROMPT_PLANO.md`,
  nomeia o empregador (linha 12) e a formação do owner (linha 18); não traz valor de salário. Está assim desde o
  primeiro commit e já consta da "Fila do owner" do `PAINEL.md` (linha 46). Não é falha do item 1; fica registrado.

## 6. Forma

- Português: sim.
- Caminhos absolutos: **não**. A linha 4 declara a raiz e avisa que os caminhos são relativos. A regra da rodada
  (`SISTEMA.md`, "Forma") pede caminho absoluto em tudo o que o owner precise abrir, e as seções 4 e 5 são justamente
  a lista do que ele abre (achado 4).
- Nada dito como feito sem ter sido: o título da seção 2.1 diz "reconferidas no item 2" e foi escrito às 19:33, antes
  de o item 2 terminar (leitura das 19:31 às 19:57, pelo próprio `00_restricoes.md`). Hoje é verdade.

## 7. O que não conferi

- As URLs citadas dentro dos quatro arquivos de `research/` (não usei a web; o `ESTADO.md` só aponta para as linhas).
- O restante de `research/04` fora das linhas 222–290 e dos títulos; o corpo de `FICHA.md` e de `REVISAO_V2.md`.
- Se o commit do item 1 foi feito com `git mv` ou com mover e adicionar (o histórico é igual nos dois casos).
- Se há commit sem push (não rodei comando de rede).
- Os arquivos `verificacao*` e `correcoes*`, por regra desta revisão.

## 8. Achados e correção pedida

1. **Linhas 76–77 — afirmação mais forte que a fonte.** O texto diz "quase todos os números são dos Estados Unidos e
   vêm de agências que vendem leads (aviso na linha 6)". A linha 6 de `research/03` diz outra coisa: a maioria **dos
   números dos Estados Unidos** vem de agências. E nas linhas 53–91 há números do Brasil em oito linhas (64–66, 68,
   81–83 e 87). Redação certa: "Atenção: boa parte dos números de preço do lead, do clique e de fechamento é dos
   Estados Unidos, e a maioria desses vem de agências que vendem leads (aviso na linha 6); não viram número do
   Brasil. Os números do Brasil (linhas 64–66, 68 e 81–83) são estimativa ou têm confiança baixa ou média, salvo a
   faixa de preço anunciado do serviço (linha 81)."

2. **Linhas 21–32 — falta o resultado da reconferência.** Trocar "cada ponto abaixo só vira regra depois de
   reconferido na fonte, no item indicado" por "os itens 2, 4 e 5 já reconferiram; o resultado está na coluna ao
   lado", e acrescentar à tabela da seção 2.1 a coluna "Resultado (onde está)":
   - linha 29: "Continua valendo; incompleta: faltava o caminho de administrar o perfil da licenciada
     (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 149–152)";
   - linha 30: "Continua valendo, com termos vedados a mais; que o art. 22 alcance o site de terceiro é
     interpretação, a norma é silente (mesmo arquivo, linhas 267–272)";
   - linha 31: "Vale na direção, corrigida no detalhe: consentimento 'específico' e destacado; a frase-modelo sozinha
     não basta (mesmo arquivo, linhas 372–376)";
   - linha 32: "Não dá para confirmar nem para derrubar
     (`/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`, seção 7, linhas 633–648)".
   O arquivo `00_restricoes.md` estava sendo editado enquanto eu lia (alterações sem commit às 01:44); conferir os
   números de linha depois que ele for comitado.

3. **Seção 4, linhas 108–125 — tabela desatualizada.** Redação certa das linhas que mudam, e as que faltam:
   - linha 115: "Leitura do owner | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`";
   - linha 116: "Verificações independentes | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`:
     `verificacao_item<N>.md` (primeira), `verificacao2_item<N>.md` (segunda passada), `verificacao_reserva<N>.md` e
     `correcoes_*.md`";
   - linha 117: acrescentar "anexos em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes_anexos/`";
   - linha 118: "`01_google_organico.md`, `02_google_maps_perfil.md`, `03_respostas_de_ia.md`, `03b_chatgpt.md`,
     `03b_chatgpt_roteiro_de_teste.md`; método do exemplo do owner em `00x_metodo_do_exemplo_x.md`", todos em
     `/home/ancastelo/pessoal/SEO_Project/docs/estudo/`;
   - linha 119: acrescentar `docs/mercado/serp_sp_registro.md`, `docs/mercado/serp_sp_dominios.md`,
     `data/serp_dominios.csv` e `data/serp_raw/`;
   - linhas novas, fila de reserva: "1 Ampliação do mapa | `docs/mercado/serp_sp_ampliacao.md`,
     `data/serp_sp_ampliacao.csv`"; "2 Dez páginas × página-modelo | `docs/mercado/paginas_top10.md`"; "3 Plano de
     conteúdo de 90 dias | `docs/plano_conteudo_90d.md`"; "4 Pontos de contrato | `docs/contrato_pontos.md`"; "5
     Planilha de medição | `docs/medicao_modelo.md`, `data/medicao_modelo.csv`";
   - linha nova: "Respostas do owner | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RESPOSTAS_OWNER.md`
     (ainda não existe; é o owner quem cria)";
   - linha 125: trocar por "Em 14/11/2026 todos os arquivos acima existem; o painel diz o estado de cada item."

4. **Linha 4 e seções 4 e 5 — caminhos relativos.** Trocar os caminhos das seções 4 e 5 (o que o owner abre) por
   caminhos absolutos, começando em `/home/ancastelo/pessoal/SEO_Project/`. Na seção 2 os relativos podem ficar,
   desde que a linha 4 continue declarando a raiz.

5. **Linha 3 — data.** Acrescentar: "Atualizado em 14/11/2026, <hora lida de `date`>: itens 1 a 8 fechados; fila de
   reserva e segunda passada no painel."

6. **Linhas 43–44, 62, 71 e 88 — tempo verbal.** Linha 44: trocar "(conclusão marcada como interpretação)" por
   "(interpretação da pesquisa antiga; o item 2 não conseguiu conferir: PDF não lido)". Linha 62: "hipóteses que o
   item 4 conferiu ao vivo; resultado em `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`". Linha 71:
   "base do item 5, fechado". Linha 88: "Virou a pergunta 1 de
   `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`".

7. **Observação, sem correção pedida no `ESTADO.md`:** quatro faixas de linha são mais largas que o assunto (linhas
   29, 30, 68–69 e 81 do `ESTADO.md`; itens 4, 6, 34 e 42 da tabela acima). Se quiser apertar: `research/03` "13,
   102–103 e 108"; `research/01` "44, 157 e 188"; `research/01` "167–169"; `research/03` "29–30 e 41–42".
