# Segunda passada — fila de reserva, tarefa 5 (modelo de planilha de medição)

## Quem e quando

- Revisor independente, em contexto limpo (subagente), sem acesso à conclusão de ninguém. Não abri nenhum arquivo
  `verificacao*` nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só listei os
  nomes) e desconsiderei o que o artefato diz sobre a verificação anterior (linhas 3–5).
- Início desta tarefa: sábado, 14/11/2026, 02:08 (Brasília, lido de `TZ=America/Sao_Paulo date`). Relatório gravado
  às 02:16 do mesmo dia (idem).
- Não editei artefato nenhum. Não rodei `git` de escrita. Não usei navegador, busca ao vivo nem leitura de web.

## O que abri

| Arquivo (caminho absoluto) | Como | Hora da leitura |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` (884 bytes; de 13/11, 23:09:18) | inteiro, bruto e por `csv.reader` | 02:08 |
| `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` (69 linhas; de 13/11, 23:09:18) | inteiro | 02:08 |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` | seções 2, 3, 4, 5.1, 5.2 (fim), 5.3, 6, 7, 8, 9 e 10 (começo) | 02:04 e 02:09 |
| `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` (alterado às 01:59:04) | linhas 82, 121–124, 147–158 e 240–249 | 02:09 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | seção 8 (linhas 356–375) e seção 1.3 (linhas 96–113) | 02:09 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | seção 1.3 (linhas 118–127) | 02:09 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | seção 9 (tabela de 19 linhas) | 02:09 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` | trechos sobre a grade de posição (linhas 108–111, 354–355, 402–404) | 02:10 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | trechos da planilha (linhas 176–205) | 02:10 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (**outro agente o editava**) | quadro de vereditos (linhas 21–38) | 02:10 |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (**outro agente o editava**) | busca por "taxa de fechamento" | 02:12 |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` | cabeçalho e coluna `volume`, por script | 02:10 |

Scripts meus, só de leitura: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res5_csv.py` e
`v2res5_sorteio.py` (mesma pasta).

## Portão, parte por parte

Portão (`RODADA.md`, fila de reserva, 5): "Modelo de planilha de medição em CSV (posição, clique, lead, lead
vendido) com as definições de cada coluna."

| Parte do portão | O que conferi | Cumprida? |
|---|---|---|
| É um CSV válido | 3 linhas (cabeçalho e 2 de exemplo); **30 campos em cada uma**; UTF-8 sem BOM; fim de linha LF; termina com quebra de linha; nomes de coluna únicos, só minúsculas, números e `_`; nenhum valor precisa de aspas | sim |
| Posição | `posicao_media` (Search Console) e `posicao_na_tela_mediana` (conferência manual) | sim |
| Clique | `cliques_na_busca` (e `taxa_de_clique`, `impressoes`) | sim |
| Lead | `leads_toque_no_botao`, `leads_pedido_formulario`, `leads_validos` | sim |
| Lead vendido | `leads_vendidos` (e `forma_de_cobranca`, `preco_combinado_reais`, `receita_reais`) | sim |
| Definição de cada coluna | 30 colunas no CSV, 30 definidas no `.md`, **na mesma ordem**; nenhuma sobra de um lado nem do outro; nenhum nome entre crases no `.md` que não seja coluna | sim |

## O que conferi

### (a) e (b) Coluna por coluna

| Coluna | De onde vem | Quem preenche | A base citada existe e diz aquilo? | Pede dado vedado? |
|---|---|---|---|---|
| `exemplo` | — | owner | marca da rodada | não |
| `periodo_inicio`, `periodo_fim` | calendário | owner | A 8, linha 365: semana ou 28 dias contra período igual — sim | não |
| `pagina` | o site | owner | D 3.4, linha de endereços (linha 132) — sim | não |
| `tipo_pagina` | D 3.1 | owner | T1 a T12 em D 3.1 (linhas 86–97) — sim | não |
| `praga`, `regiao` | D 3.1 | owner | sim | não |
| `licenciada` | a página | owner | D 4.1, primeira linha (nome como consta na licença) — sim | não (nome de empresa) |
| `impressoes` | Search Console | owner | A 8, linha 360 — sim, classe A | não: conta do owner |
| `cliques_na_busca` | idem | owner | A 8, linha 360 — sim | não |
| `taxa_de_clique` | idem | owner | A 8, linha 360 (cliques ÷ impressões) — sim | não |
| `posicao_media` | idem | owner | A 8, linhas 360 e 362 (resultado mais alto; posição do bloco; resumo de IA; "a página não diz como conta o bloco do mapa") — sim | não: vem do relatório, não de consulta |
| `impressoes_em_ia` | relatório de IA generativa do Search Console | owner | C 1.3, linhas 122–124 (só impressões; dados já dentro do relatório geral) — sim, classe A | não |
| `buscas_conferidas_a_mao` | anotação manual | owner | D 6, linha "Posição na tela" (linha 322): pessoa digita, sem script — sim | não: é o que o desenho permite; consulta por robô segue vedada |
| `posicao_na_tela_mediana` | a mesma anotação | owner | D 6 (linha 322); A 8 (linhas 369–371: "para uma pessoa, num lugar, num momento") — sim, com a ressalva do achado 6 | não |
| `visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`, `visitas_chatgpt_user` | registro de acesso bruto do servidor | owner | D 3.4 (linha 142), D 6 (linha 323), G 9, linha 15 — sim | não: contagem, sem IP |
| `leads_toque_no_botao` | contador do site | owner | D 5.1 (linhas 199 e 212–218) e D 6 (linha 325) — sim, texto igual | não: o contador não guarda dado de contato |
| `leads_pedido_formulario` | registro de pedidos | owner | D 5.2 e D 6 (linha 326) — sim | não: é contagem |
| `leads_validos` | contagem mensal da licenciada | licenciada | D 6 (linha 327) — sim, texto igual; PREMISSA marcada | não: é número. Falta dizer "só o número" (achado 5) |
| `orcamentos` | a mesma contagem | licenciada | D 6 (linha 329) — sim | não |
| `servicos_fechados` | a mesma contagem | licenciada | D 6 (linha 329: "não para cobrar") — sim | não |
| `leads_vendidos` | contrato e contagem | owner | D 6 (linha 328) e D 8, fase 4 (linha 365) — sim, texto igual | não |
| `forma_de_cobranca` | contrato | owner | D 8, "Unidade de cobrança" (linhas 373–377): decisão do owner — sim | não |
| `preco_combinado_reais` | contrato | owner | D 8 (linhas 376–377: "O valor não tem fonte") — sim; **não afirma preço** | não |
| `receita_reais` | conta | owner | D 6, linha "Receita por página" (linha 330) — sim, com a ressalva do achado 1 | não |
| `atualizacao_central_no_periodo` | painel de status da busca | owner | A 8 (linha 365) e A 1.3 (linhas 96–113: o painel) — sim | não |
| `observacao` | — | owner | regra do projeto | proíbe expressamente nome, telefone e conversa |

- **Frequência:** o `.md` não tem coluna nem frase de frequência; ela decorre de "uma linha por página × período de
  28 dias" (linhas 7–8) e, nas três colunas da licenciada, de "contagem mensal" (linha 42, que já avisa que o mês
  não coincide com os 28 dias). Para a conferência manual não há frequência nem quantidade (achado 2).
- **Grade de posição e consulta automática:** nenhuma coluna pede; a linha 14 diz que nenhuma coluna vem de
  consulta automática ao Google, e a linha 67 exclui a posição no mapa, remetendo a D 6, "Não medir" (linhas
  336–337), que por sua vez remete ao guia (b), seção 9 — onde a grade aparece como vedada e a alternativa são os
  dados do próprio perfil (linhas 354–355 e 402–403 do guia). Coerente.
- **Dado de painel da licenciada:** as três colunas que dependem dela estão marcadas como dela; nada do perfil de
  empresa nem do WhatsApp dela é tratado como dado do site. Coerente com D 6 e D 9.1 (linha do WhatsApp).
- **Dado pessoal de consumidor:** nenhuma coluna guarda. O CSV e o `.md` não têm telefone, nome de pessoa nem
  conversa; o único nome é "EXEMPLO Alfa Controle de Pragas Ltda.", o mesmo do protótipo.

### (c) Linhas de exemplo

| Linha do CSV | Marcada como exemplo? | Aritmética |
|---|---|---|
| 2 (`/zona-oeste/baratas/`, T3, com licenciada) | `exemplo` = "sim"; `observacao` começa por "LINHA DE EXEMPLO"; a licenciada leva "EXEMPLO" | período de 01/01 a 28/01/2027 = 28 dias; `impressoes` 0 → `taxa_de_clique` e `posicao_media` vazias (como a definição manda); `buscas_conferidas_a_mao` 0 → `posicao_na_tela_mediana` vazia; `leads_vendidos` 0 × preço 0 = `receita_reais` 0; forma "nenhuma (fase gratuita)". Coerente |
| 3 (`/pragas/baratas/`, T2, sem licenciada) | `exemplo` = "sim"; `observacao` começa por "LINHA DE EXEMPLO" | mesmas datas; `impressoes` 0 → taxa e posição vazias; colunas de lead, de cobrança e de receita vazias. Coerente com a observação da própria linha; a regra não está nas definições (achado 4) |

Todos os números das duas linhas são zero ou vazio: **nenhuma razão é exercitada**. A coerência aritmética está
conferida, mas por vacuidade (achado 7).

### (d) "Lead" e "lead vendido" contra o desenho e contra o levantamento de contrato

| Termo | `medicao_modelo.md` | `desenho_v0.md`, seção 6 | `contrato_pontos.md` | Bate? |
|---|---|---|---|---|
| Lead (Via A) | toque no botão, fora robôs conhecidos; repetidos não se distinguem | linha 325: o mesmo | linha 82: "toque (lead)" entre as quatro medidas | sim |
| Lead (Via B) | pedido enviado com autorização | linha 326: o mesmo | — | sim |
| Lead válido | contato que a licenciada confirma ter recebido com o código | linha 327: o mesmo; ela informa só números | linha 151: a mesma definição; a regra de contato **inválido** está prevista para a fase 4, sem conteúdo | sim. A planilha não inventa regra de lead inválido, o que é coerente com o levantamento |
| Lead vendido | lead válido pago: por unidade ou coberto pela mensalidade; zero antes da fase 4 | linha 328: o mesmo | linha 82 | sim |
| Unidade de cobrança | "mensalidade da região" ou "por lead válido" | seção 8, linhas 373–377: decisão do owner; o toque **não** é unidade de cobrança | linha 114 (mensalidade × por unidade) | sim: o toque não aparece como forma de cobrança |
| Preço | nenhum valor; "o valor não tem fonte de mercado" | linhas 376–377 | — | sim: não afirma preço |

### (e) Remissões

Todas as remissões do `.md` existem e dizem aquilo: D 3.1, D 3.4, D 4.1, D 5.1, D 5.2, D 6 (linhas "Posição na
tela", "Receita por página" e o item "Não medir"), D 8 ("Unidade de cobrança"; fase 4); A 8; A 1.3; C 1.3; G 9,
linha 15; `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` (existe e tem planilha
própria, hoje com 24 colunas; o `.md` não cita o número, então não há o que divergir);
`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (a coluna chama-se `volume` e as 2.721 linhas trazem
"não medido"). "Taxa de fechamento sem fonte brasileira" (linha 58) confere com D 6 (linha 329) e com
`/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (linhas 49, 601 e 644, lidas às 02:12).

### (f) Forma

Português; caminhos absolutos; siglas "D", "A", "C", "G" definidas nas linhas 9–12; unidade (R$) nas duas colunas de
dinheiro; taxa "de 0 a 1"; datas em AAAA-MM-DD. O documento diz que nada foi medido e que as linhas são exemplo.
Não há número de mercado nenhum.

## Sorteio

As 36 afirmações conferíveis que listei foram **todas** conferidas (tabelas acima). Para o placar, sorteei 12 com a
semente `verificacao2-reserva5-20261114` (`random.Random(semente).sample`, lista em
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res5_sorteio.py`): 5, 7, 9, 12, 16, 17, 19, 21, 22,
24, 29, 30.

| Nº | Afirmação | Conferida em | Resultado |
|---|---|---|---|
| 5 | `exemplo` = "sim" nas linhas de exemplo | CSV, linhas 2 e 3 | ok |
| 7 | `pagina` = caminho, como no endereço (D 3.4) | desenho, linha 132; CSV (`/zona-oeste/baratas/`, `/pragas/baratas/`) | ok |
| 9 | `licenciada`: nome da empresa nomeada; uma linha por licenciada (D 4.1) | desenho, linha 155 | ok |
| 12 | `taxa_de_clique` = cliques ÷ impressões (A 8) | guia orgânico, linha 360 | ok |
| 16 | `posicao_na_tela_mediana` (D 6; A 8) | desenho, linha 322; guia, linhas 369–371 | ok, com ressalva (achado 6) |
| 17 | Visitas dos robôs, do registro bruto (D 3.4, D 6; G 9, linha 15) | desenho, linhas 142 e 323; guia do ChatGPT, seção 9, linha 15 | ok |
| 19 | `leads_pedido_formulario` (D 5.2 e D 6) | desenho, linha 326 | ok |
| 21 | `orcamentos` (D 6, PREMISSA) | desenho, linha 329 | ok |
| 22 | `servicos_fechados`: para a taxa de fechamento, não para cobrar | desenho, linha 329 | ok |
| 24 | `forma_de_cobranca`: unidade de cobrança é decisão do owner (D 8) | desenho, linhas 373–377 | ok |
| 29 | Taxa de fechamento não tem fonte brasileira | desenho, linha 329; `modelos_de_negocio.md`, linhas 49, 601 e 644 (02:12) | ok |
| 30 | Não somar `impressoes` com `impressoes_em_ia` (C 1.3) | guia de IA, linha 124 | ok |

**Placar: 0 falha em 12** (e 0 afirmação falsa nas 36).

## Veredito

**APROVADO COM RESSALVAS.** O portão está cumprido: CSV válido, as quatro medidas presentes, 30 colunas com 30
definições. Nenhuma coluna pede dado vedado, nenhuma afirma preço, e "lead", "lead válido" e "lead vendido" são os
do desenho e os do levantamento de contrato. As ressalvas são lacunas de definição que fariam duas pessoas
preencherem a mesma planilha de modo diferente (achados 1, 3 e 4) e pontos menores.

## Achados

Arquivo de todos, salvo indicação: `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`.

1. **Mensalidade num período de 28 dias, e em que linha ela entra.** Linha 48. "A mensalidade do período" não diz
   como o mês cabe em 28 dias (treze períodos somam 364 dias: lançar a mensalidade cheia em cada um conta uma a mais
   por ano) nem em qual das linhas da região o valor entra. A linha 42 já avisa do descompasso para a contagem da
   licenciada; falta o mesmo aviso aqui. Redação certa: "`leads_vendidos` × preço por lead; ou, na mensalidade, a
   parte que cabe aos 28 dias (mensalidade × 28 ÷ dias do mês) — se for lançada cheia, anotar em `observacao`. A
   mensalidade de uma região entra **uma vez**, na linha da página de região (T4) ou, se ela não existir, na primeira
   página da região; nas outras linhas, vazio."
2. **Falta dizer com que frequência.** Linhas 13–14. Acrescentar: "**Com que frequência:** uma vez ao fim de cada
   período de 28 dias, para todas as colunas; as três da licenciada dependem da contagem mensal dela (D 6); a
   conferência manual de `buscas_conferidas_a_mao` é por amostra pequena (D 6), sem número fixado."
3. **A planilha não tem a dimensão "busca".** Linhas 7–8 e 37–38. D 6 (linha 320) fala em posição, impressões e
   cliques "por página **e por busca**"; o modelo é só por página, e `posicao_na_tela_mediana` junta buscas de termos
   diferentes. Acrescentar em "O que esta planilha não mede": "**Desempenho por busca (termo):** a linha é por
   página; o detalhe por busca fica no Search Console e na anotação manual (termo, hora, local).
   `posicao_na_tela_mediana` resume as buscas conferidas da página, de termos diferentes."
4. **Vazio × zero só aparece no exemplo.** Linhas 40–48, contra a linha 3 do CSV. A regra "página sem botão nem
   licenciada: colunas de lead vazias" está só na observação da linha de exemplo; e a linha 45 diz "Zero antes da
   fase 4", enquanto o exemplo de guia traz vazio; a linha 46 não prevê `forma_de_cobranca` vazia. Redação certa, na
   linha 31: "Página sem licenciada (T1, T2, T8…): `licenciada` e as colunas de lead, de cobrança e de receita ficam
   **vazias**, não zero." Na linha 45: "Zero antes da fase 4 nas páginas com licenciada." Na linha 46: acrescentar
   "vazio se a página não tem licenciada".
5. **Dizer, nas três colunas da licenciada, que ela informa só o número.** Linhas 42–44. O desenho põe isso na
   própria definição (linha 327: "nunca nome, telefone ou conversa") e explica por quê (seção 9.1, linha do
   WhatsApp: se ela mandar esses dados, o aviso do botão deixa de ser verdade). No `.md` a proibição só está em
   `observacao`. Redação certa, ao fim da linha 42: "A licenciada informa **só o número** — nunca nome, telefone ou
   conversa de quem a procurou (D 6)." E, em "Quem preenche": "**licenciada** informa; o owner lança".
6. **`posicao_na_tela_mediana` conta diferente do desenho.** Linha 38. D 6 chama a medida de posição "na tela, com
   mapa e anúncios"; o modelo conta só entre os orgânicos e manda o resto para `observacao`. O `.md` avisa que a
   mediana é escolha dele; falta avisar o mesmo da contagem. Redação certa: "A mediana e a contagem só entre os
   orgânicos são escolhas deste modelo (D 6 fala em posição 'na tela, com mapa e anúncios')."
7. **As linhas de exemplo não exercitam nenhuma conta.** CSV, linhas 2 e 3: todos os números são zero ou vazio.
   Opção, se a sessão quiser: uma terceira linha de EXEMPLO com valores diferentes de zero e a razão visível (por
   exemplo `impressoes` 200, `cliques_na_busca` 10, `taxa_de_clique` 0.05), com "LINHA DE EXEMPLO: valores
   fictícios, não são estimativa" na observação. O risco de o número fictício ser lido como estimativa é real;
   deixar como está também é defensável, desde que a linha 6 diga "os valores de exemplo são todos zero".
8. **Abrir o arquivo numa planilha em português.** Linha 8. Separador vírgula e decimal com ponto são o contrário do
   padrão das planilhas configuradas para o Brasil (ponto e vírgula; vírgula decimal). Acrescentar: "Numa planilha
   em português, abrir por 'importar', escolhendo vírgula como separador e ponto como decimal."
9. **Robô reconhecido pelo nome.** Linha 39. Acrescentar: "contados pela identificação que o pedido declara
   (user-agent), que pode ser forjada; conferir contra os endereços IP publicados é outro passo (G 9, linha 2)."
10. **Redação da linha 49.** "terminou há menos de uma semana do período" → "terminou menos de uma semana antes do
    início do período".

Visto de passagem, fora do escopo desta tarefa: `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md`,
linhas 82, 151, 152 e 244–245, cita as linhas 302 e 307–312 da seção 6 do desenho; às 02:09 essas linhas da tabela de
medição estavam em 320 e 325–330 de `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`.

## O que não conferi

- As fontes da web por trás de A 8, C 1.3 e G 9 (ajuda do Search Console, registro de mudanças do Google, página dos
  robôs da OpenAI): conferi que os **guias** dizem o que o `.md` lhes atribui, não reabri as páginas.
- Se o relatório de IA generativa do Search Console permite mesmo o filtro por página no período de 28 dias: o guia
  (c) lista "páginas" e "datas" entre as dimensões; não vi o relatório (exige a conta do owner).
- Como a planilha abre em cada programa (não abri em nenhum; só `csv.reader`).
- `00_restricoes.md` e `modelos_de_negocio.md` estavam sendo editados por outro agente; o que cito é das horas
  indicadas.

## Lembretes ignorados

- O `CLAUDE.md` global (`~/.claude/CLAUDE.md`) manda, no início da sessão, carregar as ferramentas de memória
  corporativa (meli-memory), chamar `mem_context`, salvar memórias, fazer resumo de sessão e perguntar "quer
  compound?": **não executei nada disso** (regra da rodada e `CLAUDE.md` do projeto).
- Nenhuma skill de plugin foi usada; nenhum modelo externo; nada em `/tmp`; nada instalado.
