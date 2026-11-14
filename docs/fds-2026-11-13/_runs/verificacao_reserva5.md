# Verificação independente — fila de reserva, tarefa 5 (modelo de planilha de medição)

- **Quando:** sexta, 13/11/2026, 23:05 (Brasília, lido de `TZ=America/Sao_Paulo date`).
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu.
- **Artefatos conferidos:** `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` (3 linhas, lido inteiro) e
  `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` (67 linhas, lido inteiro).
- **Portão (de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, fila de reserva, item 5):**
  "Modelo de planilha de medição em CSV (posição, clique, lead, lead vendido) com as definições de cada coluna."
- **Modo:** conferência completa (todas as 30 colunas, todas as bases citadas, as duas linhas de exemplo, as seis
  contas). Nenhum artefato foi editado. Nenhum `git` de escrita.

## Veredito

**APROVADO COM RESSALVAS.** O CSV abre, as 30 colunas têm definição com o mesmo nome e na mesma ordem, e as
definições de lead, lead válido e lead vendido são as da seção 6 do desenho. Há **um erro de definição** (o que a
posição média do Search Console conta: correção 1) e **três incoerências** entre as linhas de exemplo e as
definições, ou entre definições (correções 2 a 4). Nenhuma muda o que a planilha mede nem as quatro colunas do
portão; por isso não reprova. As correções estão no fim.

## 1. Portão

| Pergunta | Resultado |
|---|---|
| O CSV abre? | Sim. UTF-8 válido, sem marca de ordem de bytes, fim de linha simples; 3 linhas com **30 campos cada**. |
| Coluna de posição | `posicao_media` (Search Console) e `posicao_na_tela_mediana` (conferência manual). |
| Coluna de clique | `cliques_na_busca` (com o aviso de que não é o toque no botão). |
| Coluna de lead | `leads_toque_no_botao`, `leads_pedido_formulario`, `leads_validos`. |
| Coluna de lead vendido | `leads_vendidos`. |
| Toda coluna do CSV tem definição no `.md`? | Sim: 30 de 30. |
| Toda coluna definida existe no CSV, com o mesmo nome? | Sim: 30 de 30, na mesma ordem (comparação feita por programa). |
| Diz que nada foi medido? | Sim (linha 4 do `.md`). |

## 2. Cada definição contra a base citada

Abri cada seção citada: desenho (`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`), seções 3.1, 3.4, 4.1,
5.1, 5.2, 6 e 8; guia de busca orgânica (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`),
seções 1.3 e 8; guia de respostas de IA (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`),
seção 1.3; guia do ChatGPT (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`), seção 9.

| Coluna | Base citada | O que a base diz | Resultado |
|---|---|---|---|
| `exemplo` | marca "EXEMPLO" da rodada | — | sem base a conferir; coerente |
| `periodo_inicio`, `periodo_fim` | A 8 | "Comparar semana ou 28 dias contra período igual anterior" (coluna "O que fazer" do guia, linha 365); D 6, linha 314, repete | confere. O `.md` diz "o guia recomenda", o que é exato: é recomendação do guia, não frase do Google |
| `pagina` | D 3.4 (endereços) | endereços legíveis, em minúsculas, com hífen; exemplo `/zona-oeste/baratas/` | confere |
| `tipo_pagina` | D 3.1 | T1 a T12 | confere |
| `praga`, `regiao` | D 3.1 | tipos por praga e por região | confere |
| `licenciada` | D 4.1 | "Nome da empresa como consta na licença" | confere |
| `impressoes` | A 8 | "How many times your site appeared in Search results." | confere (adaptado ao filtro por página) |
| `cliques_na_busca` | A 8 | "The number of times a user clicked your site from Google Search results." | confere |
| `taxa_de_clique` | A 8 | "The click count divided by the impression count." | confere |
| `posicao_media` | A 8 | "The average position of the topmost result from your site."; e, na linha seguinte do guia (linha 362): posição aproximada; os links de um mesmo bloco recebem a posição do bloco; **"o resumo de IA ocupa uma posição"**; "a página não diz como conta o bloco do mapa" | a primeira frase e "os links de um mesmo bloco" conferem. **"mapa, anúncios e resumo de IA acima não entram" não confere**: o guia diz que o resumo de IA **ocupa** uma posição, e diz que **não sabe** como o mapa conta. O que o guia sustenta é só que "posição 4" não quer dizer quarto link visível (correção 1) |
| `impressoes_em_ia` | C 1.3 | "Impressions are how many times links to your site were shown to a user in a generative AI feature on Google Search."; métrica: só impressões; o relatório de IA "includes data from the Web search type in the Performance report" → "Não somar os dois relatórios" | confere. **"já fazem parte do total: não somar" está sustentado** (C 1.3, linhas 116–117; também C 7.3, passo 2, e A 8, linha 364) |
| `buscas_conferidas_a_mao` | D 6 (linha "Posição na tela") | "uma pessoa digita a busca no navegador, sem script, e anota termo, hora e local" | confere |
| `posicao_na_tela_mediana` | D 6; A 8 | D 6: "Posição 'na tela', **com mapa e anúncios**"; A 8: a busca manual mostra uma posição, para uma pessoa, num lugar, num momento | confere em parte: a coluna guarda só a "posição orgânica"; o que fazer com mapa e anúncios acima não está dito. "Mediana" é escolha do modelo, sem base (não precisa de base, mas deve ser dita como escolha) |
| `visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`, `visitas_chatgpt_user` | D 3.4 e D 6; G 9, linha 15 | registro de acesso bruto do servidor; G 9, linha 15: "para ver `OAI-SearchBot` e `ChatGPT-User`" | confere |
| `leads_toque_no_botao` | D 5.1 e D 6 | D 6: "**Lead** (Via A): toque no botão — registro do próprio site: data, página, empresa, código; fora os acessos de robôs conhecidos. Toques repetidos da mesma pessoa não se distinguem" | **a mesma definição** |
| `leads_pedido_formulario` | D 5.2 e D 6 | D 6: "**Lead** (Via B), quando existir: pedido enviado com autorização — registro do pedido com a prova de consentimento" | **a mesma definição** |
| `leads_validos` | D 6 | "**Lead válido**: contato que a licenciada confirma ter recebido com o código do site — contagem mensal, feita por ela, de todos os contatos com código; fica abaixo do real quando a pessoa apaga o código" | **a mesma definição**. Ressalva: a contagem é **mensal** e a linha da planilha é de **28 dias** (correção 4) |
| `orcamentos`, `servicos_fechados` | D 6 | "Informados pela licenciada na mesma contagem; servem para calcular a taxa de fechamento, não para cobrar" | confere |
| `leads_vendidos` | D 6 e D 8 (fase 4) | "**Lead vendido**: lead válido **pago** pela licenciada — por unidade, ou coberto pela mensalidade da região. Só existe a partir da fase 4; antes disso é zero por definição" | **a mesma definição** |
| `forma_de_cobranca` | D 8 | "Unidade de cobrança: mensalidade da região ou lead válido — DECISÃO DO OWNER" | confere |
| `preco_combinado_reais` | D 8 | "O valor não tem fonte" | confere |
| `receita_reais` | D 6 | "Leads vendidos × preço combinado, ou a mensalidade da região" | confere; ver ressalva sobre soma (correção 5) |
| `atualizacao_central_no_periodo` | A 8; A 1.3 | A 8: esperar ao menos uma semana após o fim; A 1.3: painel de status e a frase "waiting at least a full week after a core update completes" | confere. **A regra da atualização central está no guia** |
| `observacao` | regra do projeto | sem dado pessoal | confere |

- **"28 dias":** está no guia (A 8, linha 365) e no desenho (D 6, linha 314). Confere.
- **"três colunas vêm da licenciada" (linha 11–12 do `.md`):** `leads_validos`, `orcamentos`, `servicos_fechados`.
  Confere.
- Registro, sem pedir correção: o guia de busca orgânica (A 8, linha 364) diz "não há relatório separado de
  'citações em IA' nessa leitura", e o guia de respostas de IA (C 1.3) diz que o relatório existe desde 2026. O
  modelo segue C 1.3, como o desenho. A divergência é entre os guias, não deste artefato.

## 3. Coerência

| Conferência | Resultado |
|---|---|
| Página de guia (T2) sem licenciada tem colunas de lead vazias | Sim: linha 3 do CSV traz `licenciada`, as três colunas de lead, `orcamentos`, `servicos_fechados`, `leads_vendidos`, cobrança, preço e receita vazios. |
| Fase gratuita tem lead vendido zero | Sim: linha 2 do CSV, `leads_vendidos` = 0, `forma_de_cobranca` = "nenhuma (fase gratuita)", preço e receita 0. |
| `tipo_pagina` bate com o desenho | Sim: `/zona-oeste/baratas/` = T3; `/pragas/baratas/` = T2. |
| Período tem 28 dias | Sim: 2027-01-01 a 2027-01-28, contados os dois extremos. |
| Valores claramente fictícios e marcados "EXEMPLO" | Sim: coluna `exemplo` = "sim", `observacao` começa por "LINHA DE EXEMPLO", empresa "EXEMPLO Alfa…", datas futuras, todos os números zero. |
| Alguma coluna pede dado pessoal de consumidor? | Não. `licenciada` é nome de empresa; `observacao` proíbe nome, telefone e conversa. |
| Alguma coluna supõe consulta automática ao Google? | Não. `posicao_media` vem do Search Console; `posicao_na_tela_mediana` e `buscas_conferidas_a_mao` são anotação manual, "sem script"; o `.md` repete a regra na linha 12. |
| `posicao_media` = 0 e `taxa_de_clique` = 0 com `impressoes` = 0 (linhas 2 e 3 do CSV) | **Não bate.** Sem impressão não há posição (zero não é posição; e, como número menor é melhor, zero leria como "o melhor possível") nem taxa (0 ÷ 0). O próprio modelo usa vazio para `posicao_na_tela_mediana` nesse caso (correção 2). |
| `leads_pedido_formulario` = 0 na linha 2 do CSV | **Não bate** com a definição (linha 39 do `.md`): "vazio enquanto o formulário não existir". Na fase gratuita o formulário não existe (desenho, seção 5.2) (correção 3). |
| "uma linha por página × período" (linha 5 do `.md`) × "uma linha por licenciada" (linha 29) | Incoerência de redação: a unidade é página × período × licenciada (correção 5). |

## 4. Contas que a planilha permite

| Conta | As colunas existem? | O cuidado bate com o desenho? |
|---|---|---|
| `leads_toque_no_botao` ÷ `cliques_na_busca` | sim | O cuidado ("o toque também vem de visita direta ou de IA") é raciocínio do modelo, não trecho do desenho; é correto e está dito como cuidado. |
| `leads_validos` ÷ `leads_toque_no_botao` | sim | Bate: D 5.1 diz que a pessoa pode apagar o código e que toques repetidos não se distinguem. As duas coisas puxam a razão para baixo; "piso aproximado" está certo. |
| `servicos_fechados` ÷ `leads_validos` | sim | Bate: D 6 ("taxa de fechamento: sem fonte brasileira"; depende de a licenciada informar). |
| `receita_reais` ÷ `leads_validos` | sim | Bate: receita só a partir da fase 4 (D 6 e D 8). |
| Não somar `impressoes` com `impressoes_em_ia` | sim | Bate (C 1.3). |
| Não comparar períodos com atualização central | sim (`atualizacao_central_no_periodo`) | Bate (A 8). |

Faltam dois cuidados que as definições criam: (a) com mensalidade da região, a mesma mensalidade pode ser escrita em
várias linhas (várias páginas da mesma região, ou várias licenciadas) e a soma de `receita_reais` contaria em dobro;
(b) `cliques_na_busca` e `impressoes` se repetem nas linhas de uma página com mais de uma licenciada — o `.md` avisa
disso na linha 29, mas não na tabela de contas.

## 5. Forma

- Português: sim. Caminhos absolutos: sim, em todos os arquivos citados; os três existem
  (`03b_chatgpt_roteiro_de_teste.md` e `palavras_chave.csv` conferidos; este tem a coluna "volume" com "não medido").
- Número com unidade: reais nas colunas `preco_combinado_reais` e `receita_reais` e no texto ("em reais (R$)");
  período de 28 dias dito na linha 5 e na seção própria. Taxa "de 0 a 1" e decimal com ponto estão ditos.
- Diz que nada foi medido: sim (linha 4).
- "O que esta planilha não mede": as três linhas conferem (roteiro do ChatGPT; D 6, "Não medir", para o mapa; volume
  "não medido").

## Correções pedidas

1. **`/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, linha 33 (`posicao_media`):** tirar "mapa,
   anúncios e resumo de IA acima não entram". Pôr o que A 8 diz: a posição é aproximada; os links de um mesmo bloco
   recebem a posição do bloco; o resumo de IA ocupa uma posição e os links dentro dele recebem a mesma; a ajuda não
   diz como o bloco do mapa conta; por isso "posição 4" não é o quarto link visível. **É o único erro de definição.**
2. **`/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv`, linhas 2 e 3:** `posicao_media` e
   `taxa_de_clique` vazios quando `impressoes` = 0; e, no `.md`, linhas 32 e 33, dizer "vazio se `impressoes` = 0".
3. **`/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv`, linha 2:** `leads_pedido_formulario` vazio (o
   formulário não existe na fase gratuita), como manda a linha 39 do `.md`; ou mudar a definição.
4. **`/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, linha 40 (`leads_validos`) e linhas 41–42:** a
   contagem da licenciada é "mensal" (D 6) e a linha da planilha é de 28 dias. Dizer como casar (pedir a contagem
   pelas mesmas datas do período, ou registrar que o mês não coincide com o período).
5. **`/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, linhas 5, 29 e 46:** dizer que a unidade da linha
   é página × período × licenciada; e avisar, em `receita_reais` ou na tabela de contas (linhas 52–59), que a
   mensalidade da região não deve ser somada entre linhas da mesma região.
6. **`/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, linha 36 (`posicao_na_tela_mediana`):** dizer o
   que conta como "posição orgânica" quando há mapa e anúncios acima (D 6 chama a linha de "posição 'na tela', com
   mapa e anúncios") e que a mediana é escolha do modelo.

## O que não conferi

- As páginas de ajuda do Google que os guias transcrevem: conferi o modelo contra os guias, não os guias contra a
  fonte (isso foi objeto das verificações do item 3).
- Se um programa de planilha específico abre o arquivo: conferi com o leitor de CSV do Python.
