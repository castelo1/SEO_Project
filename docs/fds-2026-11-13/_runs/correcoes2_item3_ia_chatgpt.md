# Correções 2 — item 3, parte 2: guia (c) respostas de IA, parte do ChatGPT e roteiro de teste

- **Quem corrigiu:** subagente corretor. Não verifiquei o meu próprio trabalho: estas correções **não foram
  verificadas de novo**.
- **Quando:** sábado, 14/11/2026, das 01:40 às 01:52 (Brasília; `TZ=America/Sao_Paulo date`). Edições nos artefatos
  concluídas às 01:50. Toda "reaberta" abaixo é de 14/11/2026.
- **De onde vieram os achados:**
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_item3_ia_chatgpt.md` (17 achados;
  aprovado com ressalvas; 0 falha em 12).
- **Arquivos editados (só estes três, mais este relatório):**
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` (abaixo "guia (c)"),
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` ("03b") e
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` ("roteiro").
- **Como reabri fontes:** só a ferramenta de leitura de página pública (sem navegador, sem busca ao vivo, sem abrir o
  ChatGPT). Ela responde por meio de um modelo pequeno: cada pergunta levou frase falsa de controle (todas rejeitadas);
  o que decidiu classe foi pedido em duas chamadas. Nenhuma página da ajuda da OpenAI foi tentada nem substituída.
- **Nenhum `git` de escrita.** Nada apagado. Nenhum arquivo fora do projeto.
- **Lembretes ignorados (1 linha):** o `CLAUDE.md` global pediu carregar as ferramentas do meli-memory, chamar
  `mem_context`, salvar memória, resumir a sessão e oferecer "compound" — **não executei** (regra da rodada e do
  `CLAUDE.md` do projeto).
- **Ocorrência a registrar:** às 01:49:20 a sessão principal fez o commit `25d4fab` ("segunda passada: item 6 … item
  2 …"), que levou junto as minhas edições **parciais** no guia (c) e no 03b (as feitas até aquele minuto). O que fiz
  depois (cabeçalhos, fecho do 03b, todo o roteiro e este relatório) está na árvore de trabalho, sem commit. Conferi o
  `git diff e436ae3` dos três arquivos: só há edições minhas.

## Resumo

| Achado | Situação | Arquivo |
|---|---|---|
| 1 | aplicado | 03b |
| 2 | aplicado | 03b |
| 3 | aplicado (saída (a)); duas fontes rebaixadas ou reenquadradas; **nenhum consenso mudou de lugar** | guia (c), 03b |
| 4 | aplicado | guia (c) |
| 5 | aplicado | 03b |
| 6 | aplicado (a e b) | guia (c) |
| 7 | aplicado | guia (c) |
| 8 | (a) aplicado **em parte**; (b) e (c) aplicados | guia (c) |
| 9 | aplicado | 03b |
| 10 | aplicado | roteiro, guia (c) |
| 11 | aplicado | 03b |
| 12 | aplicado | 03b |
| 13 | aplicado | 03b, roteiro |
| 14 | aplicado | guia (c) |
| 15 | aplicado | guia (c) |
| 16 | aplicado só na classificação (texto da pergunta 27 intocado, por instrução) | roteiro |
| 17 | não aplicado (pendência do dono); ressalva conferida nos dois arquivos | 03b, roteiro |

Linhas abaixo = numeração **atual** dos arquivos, depois das edições.

## Achado por achado

**1 — aplicado.** 03b, linha 332. Antes: "O ChatGPT citou empresas em 33% das buscas (29,4% quando a empresa atende em
domicílio) … 10% de respostas vazias". Depois: "O ChatGPT mencionou **o negócio rastreado** em 33% das buscas (29,4%
quando é empresa que atende em domicílio) … 10% de respostas sem empresa". Fonte reaberta:
https://www.brightlocal.com/research/local-ai-visibility-study/ — a página fala em "mention rate of tracked
businesses as a percentage of the total number of searches"; 29,4% é a taxa das empresas de atendimento em domicílio;
4,1 empresas por resposta; 10% de respostas vazias; país ausente. Confere com o achado.

**2 — aplicado.** 03b, linha 482. Antes: "o H1 entrou em 83,6% dos trechos, 387 de 463". Depois: "nas 463 páginas com
H1, de 534 citadas, o H1 entrou no trecho em 387, isto é, 83,6%". Fonte reaberta:
https://think.resoneo.com/chatgpt-retrieval/ — "Of the 463 that have an H1, 387 snippets contain it, that is 83.6 %";
534 páginas citadas comparadas. Confere.

**3 — aplicado, saída (a).**
- Definição reescrita. Guia (c), linhas 24–25: antes "falta amostra, país ou método: **não vira regra**"; depois "falta
  amostra ou método expostos: **não vira regra**. País não declarado é limite anotado ao lado do número e não rebaixa a
  classe". 03b, linhas 69–72: mesma troca, mantendo "e não conta como uma das duas B de um consenso".
- Conferência da definição nova em **todas** as fontes B e "B fraca" dos dois arquivos (amostra e método expostos?):

| Fonte | Onde | Amostra e método expostos? | Resultado |
|---|---|---|---|
| Whitespark 12/05/2025 | guia (c) | sim (540 buscas manuais) | B (amostra pequena), sem mudança |
| BrightLocal 16/09/2026 (F21 no 03b) | os dois | sim (cerca de 200 mil buscas, cerca de 1.300 locais, 60 dias; reaberta); país ausente | B, sem mudança; limite de país anotado nos consensos (guia (c), linha 455; 03b, linhas 552–553 e 405) |
| Ahrefs `llms.txt`, Ahrefs 02/03/2026, Ahrefs cliques (2025 e 2026), Seer, Semrush 15/12/2025, Pew, artigo da KDD, SparkToro/Gumshoe, Peec listas | guia (c) | sim (amostras escritas no próprio guia e conferidas pela verificação 2) | B, sem mudança |
| Ahrefs Brasil 23/10/2026, **lista de domínios** | guia (c), linha 245 | em parte: reaberta em duas chamadas — os 6.698.455 são só da medição de presença; a lista de domínios dá contagem de respostas por domínio, ferramenta, mês e país, mas **não o total de respostas** nem explica a base "% do top 100" | **mantida B** (decisão minha, ver "Para a sessão principal", item 1); acrescentado à observação: "A página dá a contagem de respostas por domínio, não o total de respostas analisadas (limite anotado)" |
| **SparkToro com Similarweb 09/06/2026** | guia (c), linhas 140 e 263 | **não**: reaberta em duas chamadas — período, país (EUA) e método descritos, **tamanho do painel ausente** | **rebaixada de B para "B fraca"** (antes "B"; depois "B fraca (a página não dá o tamanho do painel…)" e "B fraca (tamanho do painel não exposto)"). Não sustentava consenso, "Em uma página", regra nem implicação |
| BrightEdge 18/09/2025; Peec 31/03/2026 | guia (c) | não (já diziam: sem número de palavras-chave; método não exposto) | "B fraca", sem mudança |
| **Lily Ray 17/06/2026** | guia (c), linhas 310, 367 e 486 | amostra sim (100 buscas, lista pública, três datas); método em parte: reaberta em duas chamadas — um modelo de IA separou as listas autopromocionais, sem critério escrito nem conferência manual declarada | classe mantida ("B fraca"), **motivo reescrito** para caber na definição nova: antes "B fraca (amostra pequena)"; depois "amostra pequena e método só em parte exposto / critério de classificação não exposto" |
| F13 Resoneo, F19 Ahrefs, F20, F22 BrightLocal, F23, F24 Seer, F25 Vercel, F29 Semrush | 03b | sim (amostras escritas no arquivo; F13, F19, F20, F23, F24 e F29 conferidas pela verificação 2; F13 e F20 reabertas por mim) | B, sem mudança |
| F17 Peec | 03b, linhas 95 e 374 | não (número de perguntas ausente) | "B fraca" mantida; motivo reescrito: antes "número de perguntas e país não"; depois "número de perguntas não: falta a amostra. País não declarado: limite anotado" |

- Outro uso do critério antigo acertado: 03b, linha 531 (tática 4.8). Antes: "não a classifico como consenso, porque uma
  delas (F29) é de 2025 e não declara país". Depois: "…porque as duas medem quedas em períodos diferentes e uma delas
  (F29) é de 2025; F29 também não declara país (limite anotado, não o motivo)". O veredito ("não é consenso") **não
  mudou**.
- **Itens de consenso que mudaram de lugar: nenhum.** Consenso 9 do guia (c) (linha 454) e consensos 7 e 8 do 03b
  (linhas 552–557) ficam: as duas B de cada um expõem amostra e método; ganharam a anotação do limite de país. Consenso
  10 do guia (c) (YouTube; Ahrefs Brasil + Pew) fica, com a ressalva do item 1 de "Para a sessão principal".

**4 — aplicado.** Guia (c), linha 165. Antes: "Agendamento de serviço local pelo Modo IA estava "em breve" em agosto de
2025, só para assinantes nos Estados Unidos". Depois: a redação pedida ("…o recurso de agente do Modo IA (reserva de
restaurante) saía para assinantes do Google AI Ultra nos Estados Unidos; o texto diz que ele seria ampliado "em breve"
para agendamento de serviço local, sem dizer público nem país"). Fonte reaberta:
https://blog.google/products-and-platforms/products/search/ai-mode-agentic-personalized/ (21/08/2025) — "rolling out
for Google AI Ultra subscribers in the U.S."; "expanding soon to local service appointments and event tickets", sem
público nem país. Confere.

**5 — aplicado.** 03b, "O que é disputado" (linhas 584–593): saíram os antigos itens 4 (Foursquare), 5 (JavaScript) e 6
(`noindex`); o antigo 7 (perfil de empresa do Google) virou o 4; entrou o parágrafo "Saíram de "disputado"…". "O que
não sei" ganhou os itens 14 (Foursquare: nenhum lado aberto), 15 (JavaScript: lado lido = F25, dezembro de 2024) e 16
(`noindex`: lado lido = medição citada em F13; lado da OpenAI não conferido), linhas 616–623. Os itens 1 a 13 de "O que
não sei" não foram renumerados. Nenhum outro arquivo cita esses itens por número (conferido com `grep`).

**6 — aplicado.** Guia (c). (a) linhas 40–41: antes "desde 31/08/2026 há um controle no Search Console para excluir…";
depois "desde 31/08/2026 o controle do Search Console para excluir o site só dos recursos de IA está disponível para
todos os sites". (b) linha 110: antes "(Incluir / Excluir; padrão = Incluir)"; depois "(Incluir / Excluir / herdar da
propriedade-mãe; padrão = Incluir, ou herdar quando a propriedade tem propriedade-mãe)". Fonte reaberta:
https://support.google.com/webmasters/answer/16908024?hl=en — três opções; "Inherit control from parent" é o padrão
"if your property has a parent property"; "As of August 31, 2026, we've rolled out this control to all websites
worldwide." Confere.

**7 — aplicado.** Guia (c), linha 233. Antes: "Explica pela "query fan-out"". Depois: "Levanta a "query fan-out" como
hipótese ("it may be that fan out queries are playing a bigger role"), não como causa demonstrada". Fonte reaberta:
https://ahrefs.com/blog/ai-overview-citations-top-10/ — a frase está na página, com "may". Confere.

**8 — (a) aplicado em parte; (b) e (c) aplicados.** Guia (c).
- (a) linhas 36–37 e 435–436. Antes: "não usa `llms.txt`, arquivo "para IA", marcação especial nem texto picado" e
  "…não são usados pelo Google (F2)". Depois: "ignora `llms.txt` e arquivos parecidos, … não é preciso criar arquivo nem
  marcação "para IA" e … picar o texto em pedaços não é exigido" e "O Google ignora `llms.txt` e arquivos parecidos e
  diz que arquivo ou marcação "para IA" não são necessários e que picar o texto não é exigido (F1, F2)".
  **Por que em parte:** a redação pedida dizia "ignora `llms.txt` **e marcação 'especial'**". Reabri
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide em duas chamadas: o "Google Search
  ignores them" refere-se aos arquivos `llms.txt` e parecidos; sobre marcação a página diz que não é preciso
  ("there's no special schema.org markup you need to add") e **não** diz "ignora". Escrevi "não é preciso" para a
  marcação.
- (b) linhas 57–59. Antes: "Cada motor separa o robô de busca do robô de treino." Depois: "Google, Apple e Anthropic
  separam o robô (ou token) de busca do de treino; a Microsoft controla por meta tag; a Perplexity só declara que o
  `PerplexityBot` não serve a treino."
- (c) linhas 449–451. Antes: "Perplexity, Apple, Anthropic e Google separam…". Depois: "Apple, Anthropic e Google
  separam…. A página da Perplexity só diz que o `PerplexityBot` não serve a treino; não descreve robô de treino." Fonte
  reaberta: https://docs.perplexity.ai/guides/bots — só `PerplexityBot` e `Perplexity-User`; nenhum robô de treino.

**9 — aplicado.** 03b. Linha 379: antes `"De 2,17 para 7,61 buscas por pergunta" … | relato de segunda mão; original não
localizado | só resultado de busca | não sei`; depois "7,61 buscas por pergunta no modelo mais forte (o "2,17" de
partida não está em F19: visto só em resultado de busca) | cerca de 4 mil perguntas · medido pela API, não no
aplicativo · país não lido | relatado em F19 (número de outro estudo, da Nectiv; original não aberto) | C (relato de
segunda mão)". Linhas 584–586: acrescentado que o "mais de 7" é esse relato, classe C. Fonte reaberta:
https://ahrefs.com/blog/query-fan-out-chatgpt/ — a tabela de comparação traz 7,61 "via API, ~4,000 prompts", de outro
estudo; **a página não traz o "2,17"**, por isso ele saiu da afirmação.

**10 — aplicado.** Roteiro: linha 197, `tipos_de_fonte` ganhou `avaliação` (só o tipo, nunca o texto), `vídeo` e
`rede social`; linha 186, coluna nova `motor`; linha 203, coluna nova `parceira_nomeada`; linhas 177–178, "22 colunas"
virou "24 colunas"; linhas 209–211, cabeçalho e as duas linhas de exemplo com 24 campos; linha 261, indicador "Tipos de
fonte" com avaliação, vídeo e rede social. Guia (c), linhas 419–422: a lista de tipos passou a ser a da planilha e cita
as duas colunas. A frase do guia (c) de que o roteiro serve também para o Google ficou, porque a coluna `motor` passou
a existir. **Não mexi** nas 30 perguntas nem no bloco da regra de medição. Conferido por script depois de editar: o
bloco "Regra de medição" é **idêntico, caractere a caractere, nos três arquivos**; cabeçalho e exemplos têm 24 campos;
as 24 colunas descritas batem, na ordem, com o cabeçalho; 30 perguntas numeradas e 30 linhas na tabela.

**11 — aplicado.** 03b. Linhas 90 e 110: "Quem ganha" de F12 e F32, de "—" para "veículo de imprensa". Linha 87: F9, de
"data não lida" para "sem data na página" (fonte reaberta:
https://developers.google.com/search/docs/appearance/ai-features — sem data de publicação nem de atualização).

**12 — aplicado.** 03b, tabela da seção 7. Linhas 401–404: lado Google de "—" para "não levantado aqui"
(coincidência, proximidade, localização, memória). Linha 397 ("um só, do Google"): aponta o guia (a), seção 1.1, e diz
que "um só" é resumo, não frase da fonte. Linha 400 (perfil que o dono controla): aponta o guia (b), seção 2. Linha 405
("posições mudam, mas há uma lista"): aponta o guia (a), seções 1.1 e 8. Conferi nos dois guias, depois do commit
`25d4fab`, que essas seções existem e dizem isso
(`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, linhas 59–67 e 356–360;
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, linhas 182–190).

**13 — aplicado.** 03b, linha 331, e roteiro, linha 42: "60.970 checagens" ganhou "(nas três plataformas — Visão geral,
Modo IA e ChatGPT; a parte do ChatGPT não é dada)". Fonte reaberta:
https://www.brightlocal.com/resources/ai-directory-sources/ — as três plataformas; sem número só do ChatGPT. Confere.

**14 — aplicado.** Guia (c), linha 261, observação: "Os números da própria página não fecham: 1,76% → 0,61% dá cerca de
−65%, não −61%, e ela usa 2,72% e 2,74% como base do "sem resumo"". Fonte reaberta:
https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update — confere. O "−61%" ficou onde
estava (é o que a página escreve), inclusive no item 1 de "disputado".

**15 — aplicado.** Guia (c), linhas 250–252. Antes: "o equivalente brasileiro medido é o Reclame Aqui (18º no geral)".
Depois: "o Reclame Aqui (18º no geral na lista da Ahrefs) seria o equivalente brasileiro — **inferência minha**, não
frase da fonte".

**16 — aplicado só na classificação.** Roteiro. Linha 141: público da pergunta 27, de "morador de apartamento" para
"comprador de apartamento (futuro morador)". Linhas 155–156: "morador de apartamento 10 (…27…)" virou "morador de
apartamento 9 (1, 4, 5, 7, 9, 13, 20, 23, 28) · comprador de apartamento, futuro morador 1 (27)"; a soma segue 30
(recontado por script). Linhas 74–75: uma frase avisando que a 27 é de quem vai comprar. **O texto da pergunta 27 não
mudou** (instrução da sessão principal).

**17 — não aplicado (pendência do dono).** Conferi que os dois arquivos declaram a ressalva: 03b, linhas 21–31 (aviso
central e fórmula), 38–39 (limite do complemento) e consensos 6 e 9 ("Classe A, com essa ressalva"); roteiro, linhas
44–46 ("A (com a ressalva do 403)") e linha 58. Nenhum verificador independente leu a ajuda da OpenAI; eu também não
tentei.

## Cabeçalhos

Os três arquivos ganharam o item "Segunda passada" (guia (c), linha 13; 03b, linha 9; roteiro, linha 11): relatório da
verificação 2, "aprovado com ressalvas; 0 falha em 12", correções por corretor às 01:50, "sem nova leitura de
verificador", com o caminho deste relatório. No roteiro escrevi "0 falha em 12 nos dois guias, sorteio não se aplica ao
roteiro", que é o que a verificação diz.

## O que outros arquivos repetem

Procurei com `grep` em `/home/ancastelo/pessoal/SEO_Project/docs` e `/home/ancastelo/pessoal/SEO_Project/prototipo`
(fora `_runs` e os três artefatos), depois do commit `25d4fab`. **Nenhum outro arquivo repete um número ou uma classe
que mudou** (33%, 83,6%, 7,61, 60.970, "22 colunas", "B fraca", SparkToro/Similarweb 0,34% e 68,01%, Lily Ray,
Foursquare, 31/08/2026: zero ocorrências). O que encosta, para a sessão principal decidir:

| Arquivo e linha | O que diz | Relação com a correção |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`, linha 51 | "as 30 ficam só de morador e síndico" | Achado 16: a pergunta 27 é de comprador (futuro morador) e agora está classificada assim |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 139 | controle de IA do Search Console em "Incluir" ([C], seção 1.2) | Achado 6(b): há a terceira opção "herdar da propriedade-mãe"; a escolha "Incluir" continua certa |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 129 | "[G], seção 9, linha 6 (uma fonte B; o estudo não testou efeito)" | Achado 2: não repete o número; a remissão segue válida |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 141, e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`, linha 78 | "sem `llms.txt`…" e "o Google não usa `llms.txt`" | Achado 8(a): seguem certos (a fonte diz "ignores them") |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 402 | "[C], "O que é disputado"" | Sem número de item; segue válido |
| `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, linhas 65–66 | remete ao roteiro e à planilha | Não lista colunas; segue válido com as 24 |

## Para a sessão principal

1. **Ahrefs Brasil, lista de domínios (decisão de classe).** A página não dá o total de respostas analisadas na lista
   de domínios nem explica a base "% do top 100"; dá a contagem por domínio. Mantive B e anotei o limite, porque o que o
   consenso 10 do guia (c) usa é a ordem (YouTube entre os mais citados), que a contagem por domínio sustenta. Leitura
   mais dura da definição nova daria "B fraca" nessa parte; aí o consenso 10 perderia uma das duas B e iria para "O que
   não sei", e "Em uma página" (item 10), as táticas 4.8 e 4.9 da seção 6 e uma linha da seção 7.1 teriam de dizer "B
   fraca". Não fiz isso.
2. **SparkToro/Similarweb rebaixada e motivo da Lily Ray reescrito** vão além da letra dos 17 achados; vieram da
   conferência "por igual" pedida para o achado 3. Reverter é trocar três células.
3. **Achado 8(a):** fiquei com "não é preciso" para marcação "para IA", em vez do "ignora" pedido.
4. **03b, linha 379:** tirei o "2,17" da afirmação, porque F19 não o traz.
5. **Roteiro:** não criei indicador para `parceira_nomeada` na tabela "O que comparar" (a métrica está no guia (c),
   seção 7.3), e a frase "contagem refeita por script … em 13/11/2026" (linha 146) ficou, embora o recorte de público
   tenha sido refeito hoje. O resumo "O que registrar" do 03b (linhas 467–469) não lista `motor` nem
   `parceira_nomeada`; ele já remete ao cabeçalho do roteiro.
6. **Pergunta 27:** o texto segue "Vou comprar…". Para cumprir a letra do portão e da decisão do painel (linha 51),
   falta trocar por "Comprei e vou me mudar para…" e devolver a classificação a "morador de apartamento".
7. **Pendência do dono (achado 17):** abrir
   https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt no navegador e conferir os dez trechos da
   tabela do complemento do 03b (linhas 43–52).
8. **Commit:** as edições posteriores a 01:49 estão sem commit; o commit `25d4fab` levou as anteriores sem citar este
   item na mensagem.
