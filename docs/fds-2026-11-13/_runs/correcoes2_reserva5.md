# Correções da segunda passada — fila de reserva, tarefa 5 (modelo de planilha de medição)

## Quem e quando

- Corretor (subagente). Não usei navegador, busca ao vivo nem leitura de web. Não rodei `git` de escrita. Nada
  instalado, nada em `/tmp`.
- Início: sábado, 14/11/2026, 02:20 (Brasília, lido de `TZ=America/Sao_Paulo date`; a mesma sessão corrigiu antes a
  tarefa de reserva 2). Linha nova do CSV gravada às 02:31; documento gravado às 02:34. Fim: 02:36, com este
  relatório (todas as horas lidas de `date`).
- Achados do revisor: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva5.md`
  (10 achados, lido inteiro).
- Arquivos editados: `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` (de 69 para 117 linhas) e
  `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` (de 3 para 4 linhas; de 884 para 1.276 bytes; as 30
  colunas e as linhas 1 a 3 não mudaram, byte a byte).

## Placar

10 achados conferidos no artefato, no CSV, no desenho e nos guias; **10 procedem e foram aplicados**: 6 com o
conteúdo que o revisor propôs (alguns com acréscimo) e 4 com ajuste (1, 7, 8 e 9). Nenhum "não aplicado".

## Achado por achado

Linhas = linhas de `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` depois da correção. "D" =
`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (regravado por outro agente às 02:23; linhas lidas entre
02:22 e 02:35).

| Achado | O que fiz | Linhas | Como conferi |
|---|---|---|---|
| 1. Mensalidade em período de 28 dias | **Com ajuste.** Não escrevi regra contábil. `receita_reais` descreve as duas formas — (a) ratear por dia; (b) lançar no período em que vence —, com o custo de cada uma, e marca a adotada, (a), como **PREMISSA** ("não é regra contábil nem fiscal, e nenhuma das duas formas vem de fonte"); quem usar (b) anota em `observacao`. Em que linha entra (página de região, T4, ou a primeira da região): também **PREMISSA**. A conta "receita por lead válido" ganhou o aviso de somar as linhas da região | 70–71, 82 | D 6, linha "Receita por página" (linha 330): só diz "ou a mensalidade da região"; D 8, "Unidade de cobrança" (linha 373): decisão do owner. Aritmética do aviso: 13 × 28 = 364 dias; 12 mensalidades por ano |
| 2. Frequência | **Aplicado, com acréscimo.** Item novo "Com que frequência" no cabeçalho: uma vez ao fim de cada período, para todas as colunas; a contagem da licenciada é "mensal" no desenho; a conferência manual é "por amostra pequena", sem número fixado. Acrescentei um ponto em aberto: o desenho quer guardar o registro bruto pelo menor tempo possível, o que pode obrigar a contar as visitas de robôs em intervalos menores | 32–37 | D 6, linhas "Posição na tela" (322) e "Lead válido" (327); D 5.1, item "Endereço IP" (linha 225) |
| 3. Falta a dimensão "busca" | **Aplicado**, sem mexer nas 30 colunas. O cabeçalho diz que a planilha é por página e por período, sem linha por busca; "O que esta planilha não mede" ganhou o item "Desempenho por busca (termo)": a medição por busca fica em planilha à parte — relatório de consultas do Search Console, anotação manual e a planilha do roteiro do ChatGPT; a mediana junta termos diferentes (dito também na própria coluna) | 17–18, 61, 105–113 | D 6, primeira linha (320): "por página e por busca". `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, linhas 361 (dimensão "buscas") e 363 (buscas omitidas por privacidade). `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`, seção 3 (linhas 173–210): uma linha por execução, 24 colunas |
| 4. Vazio × zero só no exemplo | **Aplicado, com acréscimo.** A regra entrou na coluna `licenciada` (página que não oferece o serviço: colunas de lead, de cobrança e de receita vazias, não zero) e em `leads_vendidos`, `forma_de_cobranca` e `preco_combinado_reais`. Troquei o "T1, T2, T8…" do revisor pela lista que sai de D 3.1 | 54, 68–70 | D 3.1, coluna "Oferece o serviço?" (linhas 86–97): "Não" em T1, T2 e T8 a T12; T6 "Sim, se houver licenciada". CSV, linha 3 (página de guia): colunas 20 a 28 vazias |
| 5. A licenciada informa só o número | **Aplicado, com acréscimo.** Dito nas três colunas (`leads_validos`, `orcamentos`, `servicos_fechados`), em "Quem preenche" de cada uma ("licenciada informa (só o número); o owner lança") e no cabeçalho. Acrescentei o porquê e o ponto em aberto do desenho (como conferir a contagem sem ver dado de consumidor) | 28–31, 65–67 | D 6, linha "Lead válido" (327): "nunca nome, telefone ou conversa"; D 9.1, linha do WhatsApp (393) |
| 6. `posicao_na_tela_mediana` conta diferente do desenho | **Aplicado, com acréscimo.** A coluna marca as duas escolhas do modelo: a mediana (o desenho não diz como resumir) e a contagem só entre os orgânicos, que **diverge de D 6** ("na tela, com mapa e anúncios"). As duas colunas da conferência dizem, na própria definição, que é conferência manual por amostra, por pessoa digitando, **nunca consulta automática nem grade ou rastreador** | 30–31, 60–61, 114–115 | D 6, linhas "Posição na tela" (322) e "Não medir" (336–337); D 7, linha "Consultar o Google para saber a posição" (349); guia orgânico, seção 8, última linha da tabela (consulta automática vedada) |
| 7. Linhas de exemplo não exercitam conta | **Com ajuste.** Acrescentei **uma** linha (linha 4 do CSV) com números diferentes de zero e uma seção no documento que mostra as contas e avisa que os números, as razões e o preço são fictícios. Ver "A linha nova", abaixo | 13–15, 86–101; CSV, linha 4 | Módulo `csv`: 4 linhas, 30 campos em cada; nenhuma aspa necessária; UTF-8 sem BOM; fim de linha LF; as três primeiras linhas idênticas às de antes |
| 8. Abrir numa planilha em português | **Com ajuste.** Entrou marcado como afirmação sem fonte no repositório e não testada ("o arquivo não foi aberto em nenhum programa nesta rodada"): se abrir numa coluna só ou com decimais trocados, importar escolhendo vírgula e ponto | 19–22 | Não há o que conferir no projeto; por isso a marca |
| 9. Robô reconhecido pelo nome | **Com ajuste.** A coluna das visitas diz que a contagem é pelo nome que o pedido declara (user-agent), que pode ser forjado (característica do protocolo; **sem fonte nos guias**), e que a alternativa é conferir o IP contra a lista publicada pelo operador. Para a OpenAI citei as linhas que tratam disso; o revisor apontava "G 9, linha 2", que fala de a hospedagem não bloquear os IPs, não de conferir. Para o Googlebot e o Bingbot: **"não foi levantado"**. O mesmo limite foi anotado para o desconto de robôs em `leads_toque_no_botao`. A planilha guarda só a contagem, nunca o IP | 26–27, 62 | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, linhas 199–204 (seção 2, coluna "IPs publicados": um arquivo por robô), 223–224 ("As faixas mudam: ler o arquivo na hora de configurar, não copiar para o repositório") e 419 (seção 8: "conferir o IP contra" o arquivo do OAI-SearchBot; F1, F2, classe A). `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`: a palavra "Googlebot" não aparece nenhuma vez (busca sem diferenciar maiúsculas); "Bingbot" só aparece nos guias em linhas de `robots.txt` |
| 10. Redação da linha 49 | **Aplicado.** "começou ou estava em curso no período, ou terminou menos de uma semana antes do início dele" | 72 | Guia orgânico, linha 365: esperar ao menos uma semana após o fim |

## A linha nova do CSV (linha 4)

| Campo | Valor | Campo | Valor |
|---|---|---|---|
| `exemplo` | sim | `visitas_googlebot` | 40 |
| `periodo_inicio` | 2027-07-16 | `visitas_bingbot` | 12 |
| `periodo_fim` | 2027-08-12 | `visitas_oai_searchbot` | 5 |
| `pagina` | /zona-oeste/baratas/ | `visitas_chatgpt_user` | 3 |
| `tipo_pagina` | T3 | `leads_toque_no_botao` | 20 |
| `praga` | baratas | `leads_pedido_formulario` | (vazio: o formulário não existe) |
| `regiao` | zona-oeste | `leads_validos` | 8 |
| `licenciada` | EXEMPLO Alfa Controle de Pragas Ltda. | `orcamentos` | 6 |
| `impressoes` | 1000 | `servicos_fechados` | 2 |
| `cliques_na_busca` | 50 | `leads_vendidos` | 6 |
| `taxa_de_clique` | 0.05 | `forma_de_cobranca` | por lead válido |
| `posicao_media` | 8.4 | `preco_combinado_reais` | 1 |
| `impressoes_em_ia` | 120 | `receita_reais` | 6 |
| `buscas_conferidas_a_mao` | 5 | `atualizacao_central_no_periodo` | não |
| `posicao_na_tela_mediana` | 6 | `observacao` | "LINHA DE EXEMPLO: números fictícios só para mostrar as contas. Não são medição nem estimativa nem meta. O preço de 1 real é fictício e não é preço de mercado. 2 leads válidos não pagos no período" |

Conferência por script (módulo `csv`, às 02:31 e de novo às 02:34): 30 campos; período de 28 dias (o oitavo período
de 28 dias a contar de 2027-01-01); 0.05 = 50 ÷ 1000; 120 ≤ 1000; 6 ≤ 8 ≤ 20; 6 ≤ 8 e 2 ≤ 6; 6 = 6 × 1.

**Dois pontos para a sessão principal decidir:**

1. **Marca "EXEMPLO" nos campos de texto.** Marquei os dois campos de texto livre (`licenciada` e `observacao`) e a
   coluna `exemplo` = "sim", como nas duas linhas que já existiam. **Não** escrevi "EXEMPLO" nos campos de código
   (`pagina`, `tipo_pagina`, `praga`, `regiao`, `forma_de_cobranca`, `atualizacao_central_no_periodo`): eles têm
   valores definidos no documento (caminho da página, T1 a T12, três formas de cobrança, sim ou não), e a marca os
   tiraria da definição. Se a regra for marcar todos, é uma troca de seis valores na linha 4 (e nas linhas 2 e 3,
   que estão no mesmo caso).
2. **Preço fictício.** Usei R$ 1 por lead, marcado como fictício na `observacao` e no documento, para a conta de
   `receita_reais` aparecer. A alternativa era deixar preço e receita vazios; a coluna não prevê vazio em página
   com licenciada.

## Números que mudaram

| Onde | Antes | Depois |
|---|---|---|
| Linhas do CSV | 3 (cabeçalho e 2 de exemplo, só zeros e vazios) | 4 (uma de exemplo a mais, com números diferentes de zero) |
| Tamanho do CSV | 884 bytes | 1.276 bytes |
| Documento | 69 linhas; "as duas linhas do arquivo são EXEMPLO" | 117 linhas; "as três linhas" |
| Colunas | 30 | 30 (nenhuma criada, removida nem renomeada; mesma ordem no CSV e no documento) |

Nenhum número de mercado entrou: o documento continua sem preço, sem taxa e sem volume medidos.

## O que outros arquivos repetem (não editei)

| Arquivo e linha (lidos entre 02:22 e 02:35) | O que diz | Situação |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 322 (seção 6) | posição "na tela, com mapa e anúncios" | **Diverge do modelo**, que conta só entre os orgânicos (marcado no modelo como escolha dele). Alinhar um dos dois é decisão da sessão principal |
| o mesmo, linha 320 | posição, impressões e cliques "por página e por busca" | O modelo é só por página; a medição por busca ficou "em planilha à parte", que não existe como arquivo (só o roteiro do ChatGPT tem planilha) |
| o mesmo, linha 327 | contagem "mensal" da licenciada | O modelo usa períodos de 28 dias; o descompasso está avisado no modelo, não no desenho |
| o mesmo, linha 330 | "Receita por página: … ou a mensalidade da região" | Não diz como o mês cabe em 28 dias nem em que linha entra; o modelo adotou duas PREMISSAS (ratear por dia; linha da página de região) que não estão na lista de premissas do desenho (seção 10) |
| o mesmo, linhas 216 (seção 5.1), 142 (seção 3.4) e 323 (seção 6) | acessos "com identificação de robô conhecido" são descartados; visitas dos robôs vêm do registro bruto | Não dizem que a identificação pode ser forjada nem falam em conferir o IP; o guia do ChatGPT fala (seção 8, linha 419) |
| o mesmo, linhas 225 e 431 | guardar o registro bruto "pelo menor tempo possível" (PREMISSA) | Pode conflitar com contar visitas de robôs por período de 28 dias: ponto em aberto anotado no modelo |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`, linha 29 | Reserva 5 "fechada" só com a primeira verificação ("6 correções aplicadas às 23:10, sem novo leitor") | **Desatualizado:** falta a segunda passada |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`, linhas 141–142 | só aponta a planilha | Coerente; não menciona as duas PREMISSAS novas nem a divergência com o desenho |
| `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linha 166 (02:33) | usa as colunas `impressoes` e `visitas_*` para a medição do dia 28 | Coerente; não traz o aviso de que a visita é contada pelo nome declarado |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva3.md`, linha 130 | cita "`medicao_modelo.md`, linhas 32 e 39" | As linhas mudaram de número: hoje são 55 (`impressoes`) e 62 (visitas). Relatório histórico |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva5.md`, achado 9 | manda citar "G 9, linha 2" para a conferência por IP | Essa linha fala de não bloquear os IPs na hospedagem; a conferência está na seção 8, linha 419, e os arquivos de IP na seção 2 |

`/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` estava sendo editado por outro agente e **não foi
relido**: o aviso do revisor (linhas 82, 151, 152 e 244–245 citam linhas antigas da seção 6 do desenho) continua
sem conferência minha.

## O que não conferi

- As fontes da web por trás dos guias (ajuda do Search Console, página dos robôs e arquivos de IP da OpenAI):
  conferi que os guias dizem o que o documento lhes atribui; não reabri página nenhuma.
- **Duas afirmações do documento não têm fonte no repositório**, e estão marcadas nele: que o user-agent pode ser
  forjado (característica do protocolo) e como planilhas configuradas para o Brasil abrem o arquivo.
- Como conferir o Googlebot e o Bingbot por IP: não levantado em guia nenhum; ficou "não foi levantado".
- Como a planilha abre em cada programa: não abri em nenhum; só o módulo `csv`.
- Se o relatório de IA generativa do Search Console permite o filtro por página em 28 dias (exige a conta do owner).
- Não abri a primeira verificação nem as correções anteriores; mantive no "Estado" o que o documento já dizia dela.
- `desenho_v0.md` foi regravado por outro agente às 02:23: cito seção e nome da linha; os números de linha valem
  para a hora indicada.
- A correção não foi relida por terceiro.

## Lembretes ignorados e ocorrências

- O `CLAUDE.md` global (`~/.claude/CLAUDE.md`) manda carregar as ferramentas de memória corporativa (meli-memory),
  chamar `mem_context`, salvar memórias, fazer resumo de sessão e perguntar "quer compound?": **não executei nada
  disso** (regra da rodada e `CLAUDE.md` do projeto). Nenhuma skill de plugin, nenhum modelo externo.
- **Ocorrência** (a mesma registrada em
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes2_reserva2.md`): uma busca por nome de
  arquivo mostrou linhas soltas, cortadas, de arquivos que eu não devia abrir, entre eles `verificacao_reserva5.md`
  (linhas 5, 6, 117, 121, 123, 125, 128 e 131, que são o começo de pedidos de correção da primeira verificação).
  Não abri o arquivo e não usei o que apareceu em nenhuma correção.
- Outros agentes editavam o repositório ao mesmo tempo: não toquei em nenhum arquivo além dos dois desta tarefa e
  deste relatório.
