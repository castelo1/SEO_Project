# Modelo de planilha de medição (fila de reserva, tarefa 5)

- **Estado:** escrito pela sessão principal em sexta, 13/11/2026, às 22:41 (Brasília, lido de `date`). Primeira
  verificação independente: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva5.md`
  (aprovado com ressalvas; 6 correções pedidas, aplicadas às 23:10 e não relidas por terceiro).
  **Segunda passada:** revisor novo, em contexto limpo,
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva5.md` (aprovado com ressalvas;
  0 falha em 12 afirmações sorteadas; 10 achados). Os 10 achados foram aplicados por um corretor em sábado,
  14/11/2026, às 02:34 (Brasília, lido de `TZ=America/Sao_Paulo date`): 6 como o revisor propôs e 4 com ajuste;
  relatório em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes2_reserva5.md`. Esta
  correção mexeu neste arquivo e no CSV (uma linha de exemplo a mais; as 30 colunas não mudaram) e não foi relida
  por terceiro.
  Nada foi medido: o site não existe. As três linhas do arquivo são EXEMPLO, com valores fictícios: duas só com
  zeros e vazios, e uma com números diferentes de zero, escolhidos para mostrar as contas — **não são medição,
  estimativa nem meta** (seção "As três linhas de EXEMPLO").
- **Arquivo:** `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` — uma linha por **página × período de 28
  dias × licenciada** (página sem licenciada: uma linha por página × período). A planilha é **por página e por
  período; não tem linha por busca** (ver "O que esta planilha não mede"). Separador: vírgula. Codificação: UTF-8.
  Datas em AAAA-MM-DD. Decimal com ponto. Programas de planilha configurados para o Brasil costumam esperar ponto e
  vírgula como separador e vírgula como decimal (afirmação sem fonte no repositório; o arquivo não foi aberto em
  nenhum programa nesta rodada, só lido pelo módulo `csv`): se ele abrir numa coluna só, ou com os decimais
  trocados, usar a opção de importar e escolher vírgula como separador e ponto como decimal.
- **De onde vêm as definições:** seção 6 de `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D 6"); seção 8
  de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` ("A 8"); seção 1.3 de
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` ("C 1.3"); seção 9 de
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` ("G 9"; "G 2" e "G 8" são as seções 2 e 8 do
  mesmo guia).
- **Quem preenche:** o owner, com a conta dele (Search Console) e com o registro do próprio site. Três colunas são
  **informadas pela licenciada e lançadas pelo owner**: ela informa só números agregados, nunca nome, telefone ou
  conversa de quem a procurou (D 6, linha "Lead válido"). Nenhuma coluna é preenchida por consulta automática ao
  Google, nem por grade ou rastreador de posição.
- **Com que frequência:** uma vez ao fim de cada período de 28 dias, para todas as colunas. As três colunas da
  licenciada dependem da contagem dela, que o desenho chama de "mensal" (D 6): pedir pelas datas do período. A
  conferência manual da posição "na tela" é "por amostra pequena" (D 6); o desenho não fixa quantas buscas nem de
  quanto em quanto tempo, e este modelo também não fixa. Ponto em aberto: o desenho quer guardar o registro de
  acesso bruto pelo menor tempo possível (seção 5.1 do desenho, PREMISSA de prudência); se ele for apagado antes de
  28 dias, as visitas dos robôs têm de ser contadas em intervalos menores e somadas — o intervalo não está definido.

## Por que 28 dias

O guia de busca orgânica recomenda comparar períodos iguais (semana ou 28 dias contra o período igual anterior) e
esperar ao menos uma semana depois do fim de uma atualização central do Google antes de comparar (A 8). A coluna
`atualizacao_central_no_periodo` existe para marcar o período que não deve ser comparado.

## Colunas

| Coluna | O que é | De onde vem | Quem preenche | Base |
|---|---|---|---|---|
| `exemplo` | "sim" nas linhas de exemplo; "não" nas reais | — | owner | marca "EXEMPLO" da rodada |
| `periodo_inicio`, `periodo_fim` | Primeiro e último dia do período de 28 dias | calendário | owner | A 8 |
| `pagina` | Caminho da página no site, como no endereço | o próprio site | owner | D 3.4 (endereços) |
| `tipo_pagina` | T1 a T12, pela tabela de tipos do desenho | D 3.1 | owner | D 3.1 |
| `praga`, `regiao` | Praga e região de que a página trata; vazio se não se aplica | D 3.1 | owner | D 3.1 |
| `licenciada` | Nome da empresa licenciada nomeada na página. Página com mais de uma licenciada: **uma linha por licenciada** para as colunas de lead; as colunas de busca se repetem e não devem ser somadas. **Página que não oferece o serviço**, isto é, sem licenciada e sem botão (pela coluna "Oferece o serviço?" de D 3.1: T1, T2 e T8 a T12; T6 enquanto não houver licenciada): `licenciada` e as colunas de lead, de cobrança e de receita ficam **vazias, não zero** | a página | owner | D 4.1; D 3.1 |
| `impressoes` | Vezes em que um link da página apareceu num resultado de busca do Google | relatório de desempenho do Search Console, filtro por página | owner | A 8 (classe A) |
| `cliques_na_busca` | Vezes em que alguém clicou no resultado do Google e veio à página. **Não é** o toque no botão | idem | owner | A 8 (classe A) |
| `taxa_de_clique` | `cliques_na_busca` ÷ `impressoes` (de 0 a 1); vazio se `impressoes` = 0 | idem | owner | A 8 (classe A) |
| `posicao_media` | Média da posição do resultado mais alto do site, como o Search Console calcula. É aproximada: os links de um mesmo bloco recebem a posição do bloco; o resumo de IA ocupa uma posição e os links dentro dele recebem a mesma; a ajuda lida não diz como o bloco do mapa conta. Por isso "posição 4" não é o quarto link visível. Vazio se `impressoes` = 0 | idem | owner | A 8 (classe A) |
| `impressoes_em_ia` | Vezes em que um link da página foi mostrado num recurso de IA generativa da busca do Google. O relatório só dá impressões e já faz parte do total de `impressoes`: **não somar** | relatório de IA generativa do Search Console | owner | C 1.3 (classe A) |
| `buscas_conferidas_a_mao` | Quantas buscas **uma pessoa digitou no navegador**, sem script, para ver a página "na tela" no período. É conferência manual, por amostra pequena. **Nunca** consulta automática (script, robô ou ferramenta que consulta o Google) **nem grade ou rastreador de posição**: se a busca não foi digitada por uma pessoa, não entra | anotação manual (termo, hora, local) | owner | D 6 (linhas "Posição na tela" e "Não medir"); A 8 (consulta automática é prática vedada pela política de spam do Google) |
| `posicao_na_tela_mediana` | Mediana da posição da página entre os resultados orgânicos, **nas buscas conferidas à mão** da coluna anterior (só delas: nunca de consulta automática nem de grade); vazio se nenhuma busca foi feita. Conta só os orgânicos: anúncios, bloco de mapa e resumo de IA acima da página não entram na conta e devem ser anotados em `observacao`. **Duas escolhas deste modelo:** (1) a mediana — D 6 não diz como resumir várias buscas; ela junta buscas de **termos diferentes** numa só medida, e o detalhe por termo fica na anotação manual; (2) a contagem só entre os orgânicos — **diverge de D 6**, que chama a medida de posição "na tela, com mapa e anúncios". Vale para uma pessoa, num lugar, num momento | a mesma anotação | owner | D 6; A 8 |
| `visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`, `visitas_chatgpt_user` | Pedidos de cada robô à página no período, **contados pelo nome que o próprio pedido declara** (user-agent). Esse nome pode ser forjado: qualquer programa pode declarar o nome de um robô (característica do protocolo; os guias do projeto não trazem fonte sobre isso). A alternativa é conferir o endereço IP do pedido contra a lista que o operador do robô publica. Para a OpenAI, o guia registra um arquivo de IPs publicado para cada robô (G 2, linhas 199–204, coluna "IPs publicados", e linha 223: as faixas mudam, ler na hora e não copiar para o repositório) e, para o OAI-SearchBot, manda conferir o IP do pedido contra o arquivo dele (G 8, linha 419); para o ChatGPT-User o guia lista o arquivo, mas não descreve a conferência (classe A; linhas lidas em 14/11/2026). Para o Googlebot e o Bingbot, como conferir **não foi levantado** (o guia de busca orgânica não trata disso). Sem essa conferência, o número é "pedidos que se declararam como o robô"; o mesmo limite vale para o desconto de robôs em `leads_toque_no_botao`. A planilha guarda só a contagem, nunca o IP | registro de acesso bruto do servidor | owner | D 3.4 e D 6; G 9, linha 15; G 2 e G 8 |
| `leads_toque_no_botao` | **Lead (Via A):** toques no botão que abre o WhatsApp da licenciada, fora os acessos de robôs conhecidos. Toques repetidos da mesma pessoa não são distinguidos | contador do próprio site (data, página, empresa, código) | owner | D 5.1 e D 6 |
| `leads_pedido_formulario` | **Lead (Via B):** pedidos enviados pelo formulário com autorização; vazio enquanto o formulário não existir | registro de pedidos, com a prova de consentimento | owner | D 5.2 e D 6 |
| `leads_validos` | Contatos que a licenciada confirma ter recebido com o código do site **entre `periodo_inicio` e `periodo_fim`** (pedir a ela a contagem por essas datas; o desenho fala em contagem "mensal", e o mês não coincide com os 28 dias — se ela só informar por mês, anotar isso em `observacao`). Fica abaixo do real quando a pessoa apaga o código. **A licenciada informa só o número** — nunca nome, telefone ou conversa de quem a procurou: se ela mandar esses dados para provar um lead, o aviso ao lado do botão deixa de ser verdade (D 6; seção 9.1 do desenho, linha do WhatsApp). Como conferir a contagem sem ver dado de consumidor está em aberto no desenho (PREMISSA, a rever com o advogado) | contagem mensal feita pela licenciada, de todos os contatos com código | **licenciada** informa (só o número); o owner lança | D 6 (PREMISSA: que ela informe) |
| `orcamentos` | Dos leads válidos, quantos receberam orçamento. **Só o número**, como em `leads_validos` | a mesma contagem | **licenciada** informa (só o número); o owner lança | D 6 (PREMISSA) |
| `servicos_fechados` | Dos leads válidos, quantos viraram serviço. Serve para calcular a taxa de fechamento, não para cobrar. **Só o número**, como em `leads_validos` | a mesma contagem | **licenciada** informa (só o número); o owner lança | D 6 (PREMISSA) |
| `leads_vendidos` | Leads válidos **pagos** pela licenciada: cobrados por unidade, ou cobertos pela mensalidade da região. Zero antes da fase 4 nas páginas com licenciada; vazio nas páginas sem licenciada | contrato e contagem | owner | D 6 e D 8 (fase 4) |
| `forma_de_cobranca` | "nenhuma (fase gratuita)", "mensalidade da região" ou "por lead válido"; vazio se a página não tem licenciada | contrato | owner | D 8 ("Unidade de cobrança": decisão do owner) |
| `preco_combinado_reais` | Valor da mensalidade ou do lead válido, em reais (R$), no período; 0 na fase gratuita; vazio se a página não tem licenciada. Na mensalidade, o valor cheio do contrato, só na linha em que a receita é lançada (ver `receita_reais`) | contrato | owner | D 8 (o valor não tem fonte de mercado) |
| `receita_reais` | Em reais (R$). **Por lead válido:** `leads_vendidos` × preço por lead. **Na mensalidade**, o mês não cabe em 28 dias (treze períodos somam 364 dias e há doze mensalidades por ano), e há duas formas de lançar: (a) **ratear por dia** — a parte da mensalidade que cabe aos dias do período (mensalidade ÷ dias do mês × dias do período naquele mês, somando os dois meses quando o período pega dois); os períodos ficam comparáveis, mas o número não bate com nenhuma cobrança; (b) **lançar no período em que vence** — a mensalidade inteira entra no período em que cai o vencimento; cada lançamento bate com uma cobrança, mas, pelo calendário, cerca de um período por ano fica sem mensalidade. **Este modelo adota (a) — PREMISSA**, porque a planilha existe para comparar períodos iguais; não é regra contábil nem fiscal, e nenhuma das duas formas vem de fonte. Quem usar (b) anota em `observacao` e usa em todas as linhas. A mensalidade de uma região entra **uma vez** por licenciada e por período: na linha da página de região (T4) ou, se ela não existir, na primeira página da região (**PREMISSA**); nas outras linhas da região, vazio — não somar entre as linhas | conta | owner | D 6 (linha "Receita por página": só diz "ou a mensalidade da região") |
| `atualizacao_central_no_periodo` | "sim" se uma atualização central do Google começou ou estava em curso no período, ou terminou menos de uma semana antes do início dele | painel de status da busca do Google | owner | A 8; A 1.3 |
| `observacao` | Texto livre **sem dado pessoal**: nada de nome, telefone ou conversa de quem pediu orçamento | — | owner | regra do projeto |

## Contas que a planilha permite (e as que não permite)

| Conta | Fórmula | Cuidado |
|---|---|---|
| Da busca ao toque | `leads_toque_no_botao` ÷ `cliques_na_busca` | O toque também vem de visita direta ou de IA; é indicador, não taxa exata |
| Do toque ao contato confirmado | `leads_validos` ÷ `leads_toque_no_botao` | A pessoa pode apagar o código ou tocar duas vezes: a razão é um piso aproximado |
| Taxa de fechamento | `servicos_fechados` ÷ `leads_validos` | É o número que hoje não tem fonte brasileira; depende de a licenciada informar |
| Receita por lead válido | `receita_reais` ÷ `leads_validos` | Só a partir da fase 4. Na mensalidade, somar antes as linhas da região para a mesma licenciada: a receita está numa linha só |
| **Não fazer:** somar `impressoes` com `impressoes_em_ia` | — | A segunda já está dentro da primeira (C 1.3) |
| **Não fazer:** comparar períodos com atualização central | — | A 8 |

## As três linhas de EXEMPLO do arquivo

Todas levam `exemplo` = "sim" e `observacao` começando por "LINHA DE EXEMPLO"; o nome da licenciada leva "EXEMPLO".
As datas também são fictícias.

| Linha do CSV | O que mostra | Contas que dá para conferir |
|---|---|---|
| 2 — `/zona-oeste/baratas/`, T3, com licenciada, fase gratuita | Página de oferta antes de qualquer medida | Tudo zero; `taxa_de_clique`, `posicao_media` e `posicao_na_tela_mediana` vazias, porque não houve impressão nem busca conferida |
| 3 — `/pragas/baratas/`, T2, sem licenciada | Página de guia: colunas de lead, de cobrança e de receita **vazias**, não zero | — |
| 4 — a mesma página da linha 2, num período posterior, cobrança "por lead válido" (acrescentada na segunda passada) | As contas, com números diferentes de zero | `taxa_de_clique` 0.05 = 50 ÷ 1000; `impressoes_em_ia` 120 ≤ `impressoes` 1000; `leads_vendidos` 6 ≤ `leads_validos` 8 ≤ `leads_toque_no_botao` 20; `orcamentos` 6 e `servicos_fechados` 2 ≤ `leads_validos` 8; `receita_reais` 6 = 6 × `preco_combinado_reais` 1; período de 2027-07-16 a 2027-08-12 = 28 dias |

**Os números da linha 4 são fictícios e foram escolhidos para a conta ser fácil de conferir.** As razões que saem
deles (0.05 de taxa de clique; 20 ÷ 50 = 0.4 da busca ao toque; 8 ÷ 20 = 0.4 do toque ao contato; 2 ÷ 8 = 0.25 de
fechamento) **não são estimativa, referência de mercado nem meta**: o projeto não tem fonte brasileira para nenhuma
delas. O preço de R$ 1 por lead é fictício de propósito: não é preço de mercado, e o desenho registra que o valor do
lead não tem fonte (D 8, "Unidade de cobrança").

## O que esta planilha não mede

- **Desempenho por busca (termo):** a planilha é por página e por período; não tem a dimensão "busca", embora D 6
  fale em posição, impressões e cliques "por página e por busca". A medição por busca fica em planilha à parte:
  (a) o relatório de consultas do Search Console — a dimensão "buscas" do relatório de desempenho (A 8) —, exportado
  pelo owner, sabendo que parte das buscas é omitida por privacidade (A 8); (b) a anotação manual da conferência
  (termo, hora, local), de onde sai `posicao_na_tela_mediana`; (c) para o ChatGPT, a planilha do roteiro (item
  abaixo). `posicao_na_tela_mediana` junta numa só mediana buscas de termos diferentes: serve para acompanhar a
  página, não para dizer a posição em uma busca.
- **Presença no ChatGPT:** tem roteiro e planilha próprios, com uma linha por execução de cada pergunta
  (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`, seção 3).
- **Posição no mapa do Google:** o site não tem perfil; os dados do perfil são da licenciada (D 6, "Não medir": nada
  de grade nem de rastreador de posição).
- **Volume de busca:** fica em `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, coluna "volume", hoje
  "não medido".
