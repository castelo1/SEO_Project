# Modelo de planilha de medição (fila de reserva, tarefa 5)

- **Estado:** escrito pela sessão principal em sexta, 13/11/2026, às 22:41 (Brasília, lido de `date`). Conferido por
  verificador independente (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva5.md`:
  aprovado com ressalvas; 6 correções pedidas, aplicadas às 23:10 e não relidas por terceiro).
  Nada foi medido: o site não existe; as duas linhas do arquivo são EXEMPLO, com valores fictícios.
- **Arquivo:** `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` — uma linha por **página × período de 28
  dias × licenciada** (página sem licenciada: uma linha por página × período). Separador: vírgula. Codificação: UTF-8. Datas em AAAA-MM-DD. Decimal com ponto.
- **De onde vêm as definições:** seção 6 de `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D 6"); seção 8
  de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` ("A 8"); seção 1.3 de
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` ("C 1.3"); seção 9 de
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` ("G 9").
- **Quem preenche:** o owner, com a conta dele (Search Console) e com o registro do próprio site; três colunas vêm da
  licenciada. Nenhuma coluna é preenchida por consulta automática ao Google.

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
| `licenciada` | Nome da empresa licenciada nomeada na página. Página com mais de uma licenciada: **uma linha por licenciada** para as colunas de lead; as colunas de busca se repetem e não devem ser somadas | a página | owner | D 4.1 |
| `impressoes` | Vezes em que um link da página apareceu num resultado de busca do Google | relatório de desempenho do Search Console, filtro por página | owner | A 8 (classe A) |
| `cliques_na_busca` | Vezes em que alguém clicou no resultado do Google e veio à página. **Não é** o toque no botão | idem | owner | A 8 (classe A) |
| `taxa_de_clique` | `cliques_na_busca` ÷ `impressoes` (de 0 a 1); vazio se `impressoes` = 0 | idem | owner | A 8 (classe A) |
| `posicao_media` | Média da posição do resultado mais alto do site, como o Search Console calcula. É aproximada: os links de um mesmo bloco recebem a posição do bloco; o resumo de IA ocupa uma posição e os links dentro dele recebem a mesma; a ajuda lida não diz como o bloco do mapa conta. Por isso "posição 4" não é o quarto link visível. Vazio se `impressoes` = 0 | idem | owner | A 8 (classe A) |
| `impressoes_em_ia` | Vezes em que um link da página foi mostrado num recurso de IA generativa da busca do Google. O relatório só dá impressões e já faz parte do total de `impressoes`: **não somar** | relatório de IA generativa do Search Console | owner | C 1.3 (classe A) |
| `buscas_conferidas_a_mao` | Quantas buscas uma pessoa digitou no navegador, sem script, para ver a página "na tela" no período | anotação manual (termo, hora, local) | owner | D 6 (linha "Posição na tela") |
| `posicao_na_tela_mediana` | Mediana da posição da página entre os resultados orgânicos (contando só os orgânicos; anúncios, bloco de mapa e resumo de IA acima dela não entram na conta e devem ser anotados em `observacao`); vazio se nenhuma busca foi feita. A mediana é escolha deste modelo. Vale para uma pessoa, num lugar, num momento | a mesma anotação | owner | D 6; A 8 |
| `visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`, `visitas_chatgpt_user` | Pedidos de cada robô à página no período | registro de acesso bruto do servidor | owner | D 3.4 e D 6; G 9, linha 15 |
| `leads_toque_no_botao` | **Lead (Via A):** toques no botão que abre o WhatsApp da licenciada, fora os acessos de robôs conhecidos. Toques repetidos da mesma pessoa não são distinguidos | contador do próprio site (data, página, empresa, código) | owner | D 5.1 e D 6 |
| `leads_pedido_formulario` | **Lead (Via B):** pedidos enviados pelo formulário com autorização; vazio enquanto o formulário não existir | registro de pedidos, com a prova de consentimento | owner | D 5.2 e D 6 |
| `leads_validos` | Contatos que a licenciada confirma ter recebido com o código do site **entre `periodo_inicio` e `periodo_fim`** (pedir a ela a contagem por essas datas; o desenho fala em contagem "mensal", e o mês não coincide com os 28 dias — se ela só informar por mês, anotar isso em `observacao`). Fica abaixo do real quando a pessoa apaga o código | contagem mensal feita pela licenciada, de todos os contatos com código | **licenciada** | D 6 (PREMISSA: que ela informe) |
| `orcamentos` | Dos leads válidos, quantos receberam orçamento | a mesma contagem | **licenciada** | D 6 (PREMISSA) |
| `servicos_fechados` | Dos leads válidos, quantos viraram serviço. Serve para calcular a taxa de fechamento, não para cobrar | a mesma contagem | **licenciada** | D 6 (PREMISSA) |
| `leads_vendidos` | Leads válidos **pagos** pela licenciada: cobrados por unidade, ou cobertos pela mensalidade da região. Zero antes da fase 4 | contrato e contagem | owner | D 6 e D 8 (fase 4) |
| `forma_de_cobranca` | "nenhuma (fase gratuita)", "mensalidade da região" ou "por lead válido" | contrato | owner | D 8 ("Unidade de cobrança": decisão do owner) |
| `preco_combinado_reais` | Valor da mensalidade ou do lead válido, em reais (R$), no período | contrato | owner | D 8 (o valor não tem fonte de mercado) |
| `receita_reais` | `leads_vendidos` × preço por lead, ou a mensalidade do período, em reais (R$). A mensalidade de uma região entra **uma vez**: não somar entre as linhas de páginas da mesma região | conta | owner | D 6 (linha "Receita por página") |
| `atualizacao_central_no_periodo` | "sim" se uma atualização central do Google começou, estava em curso ou terminou há menos de uma semana do período | painel de status da busca do Google | owner | A 8; A 1.3 |
| `observacao` | Texto livre **sem dado pessoal**: nada de nome, telefone ou conversa de quem pediu orçamento | — | owner | regra do projeto |

## Contas que a planilha permite (e as que não permite)

| Conta | Fórmula | Cuidado |
|---|---|---|
| Da busca ao toque | `leads_toque_no_botao` ÷ `cliques_na_busca` | O toque também vem de visita direta ou de IA; é indicador, não taxa exata |
| Do toque ao contato confirmado | `leads_validos` ÷ `leads_toque_no_botao` | A pessoa pode apagar o código ou tocar duas vezes: a razão é um piso aproximado |
| Taxa de fechamento | `servicos_fechados` ÷ `leads_validos` | É o número que hoje não tem fonte brasileira; depende de a licenciada informar |
| Receita por lead válido | `receita_reais` ÷ `leads_validos` | Só a partir da fase 4 |
| **Não fazer:** somar `impressoes` com `impressoes_em_ia` | — | A segunda já está dentro da primeira (C 1.3) |
| **Não fazer:** comparar períodos com atualização central | — | A 8 |

## O que esta planilha não mede

- **Presença no ChatGPT:** tem roteiro e planilha próprios
  (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`).
- **Posição no mapa do Google:** o site não tem perfil; os dados do perfil são da licenciada (D 6, "Não medir").
- **Volume de busca:** fica em `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, coluna "volume", hoje
  "não medido".
