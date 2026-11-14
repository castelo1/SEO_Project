# Verificação das correções do item 3 (guias (a), (b), (c), parte do ChatGPT e roteiro)

- **Data e hora:** sexta, 13/11/2026, 21:43 (Brasília; saída de `TZ=America/Sao_Paulo date`). Leituras na web feitas
  entre 21:28 e 21:42 do mesmo dia.
- **Quem verificou:** verificador independente, em contexto limpo. Não produzi os artefatos, não recebi a conclusão de
  ninguém e li, dos dois relatórios anteriores, só as seções de falhas numeradas (seção 12 de
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_a_b.md` e seção 8 de
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_ia_chatgpt.md`).
- **Versão conferida:** `docs/estudo` do commit `86af317`. Na hora da conferência o `HEAD` do repositório já era
  `9e4cc55`, mas `git diff 86af317 -- docs/estudo` não mostra diferença: o que está no disco é o que foi conferido.
  As correções foram lidas por `git diff 343047c 86af317 -- docs/estudo`.
- **Arquivos conferidos:**
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` (guia (a)),
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` (guia (b)),
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` (guia (c)),
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` e
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`; para ponteiros e limites,
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`.
- **Ferramentas:** leitura de arquivo; `git diff`, `git show`, `git log`, `git status` (só leitura); `grep`; scripts
  curtos em `python3` passados pela entrada padrão (nenhum arquivo criado); `shuf` com fonte de aleatoriedade fixada por
  `openssl enc -aes-256-ctr -pass pass:20261113 -nosalt`; leitura de página pública pela ferramenta de web (26
  chamadas: 21 com resposta, 4 com tempo esgotado em páginas de ajuda do Google chamadas em paralelo — refeitas uma a
  uma, com resposta — e 1 com erro 403). Não usei busca na web. Não usei navegador, subagente, skill, modelo externo
  nem conector.
- **Instruções que ignorei, de propósito:** o `CLAUDE.md` global pede para carregar a memória corporativa, salvar
  memória, fazer resumo de sessão e perguntar sobre "compound". Nada disso foi executado: o projeto e a tarefa vedam.
- **Nada foi editado nos artefatos.** Este é o único arquivo que gravei. Não fiz commit nem push.

## VEREDITO: APROVADO COM RESSALVAS

| Conferência | Resultado |
|---|---|
| 26 falhas dos dois verificadores | **25 resolvidas · 1 resolvida em parte (falha 11) · 0 não resolvidas · 0 correção errada** |
| Sorteio de 12 afirmações em linhas alteradas ou acrescentadas | **12 conferem · 0 falhas** (limite de reprovação: mais de 2) |
| Conferências obrigatórias na fonte (fora do sorteio) | **6 conferem · 0 falhas** |
| Ajuda da OpenAI (artigo 9237897) | **INCONCLUSIVO** (erro 403); não é falha |
| Ponteiros do guia (b) para o item 2 | **12 de 12 sorteados certos**; conferi também os outros 44: **56 de 56 certos** |
| Roteiro contra o portão | **cumpre**: 30 perguntas, nenhuma de comerciante, contagens batem, 22 colunas = 22 campos |
| Regra de medição única | **texto idêntico, byte a byte, nos três arquivos** |
| Consenso sem classe A nem duas B independentes | **nenhum sobrou**; duas observações menores no guia (c) (seção 7, itens O6) |
| Defeitos novos introduzidos pela correção | **5, todos menores** (seção 6) |
| Defeitos antigos que ficaram, fora das 26 falhas | **7, todos menores** (seção 7) |

As ressalvas são: a falha 11 ficou com um ponto justificado em vez de alterado (as perguntas 12 e 25 continuam sem
bairro); cinco defeitos pequenos entraram com a correção; e a seção "Complemento da sessão principal" do
`03b_chatgpt.md` continua apoiada só na leitura da sessão principal. Nenhuma delas muda uma regra do estudo.

---

## 1. O portão, transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 61

> | 3 | Estudo: como se ranqueia um serviço local hoje | Três guias em `docs/estudo/`: (a) busca orgânica do Google para serviço local; (b) Google Maps e perfil de empresa, **dentro do que o item 2 permitiu**; (c) respostas de IA (o que faz um site ser citado). Cada tática com fonte e classe A–D. Cada guia termina em "o que é consenso / o que é disputado / o que não sei". Guia (c) curto é resultado aceitável **Pedido do dono em 13/11: além do Google, estudar o ranqueamento no ChatGPT.** O guia (c) passa a ter uma parte própria, `docs/estudo/03b_chatgpt.md`: como a busca do ChatGPT escolhe e cita fontes para um pedido de serviço local (de onde vem o índice, o papel do Bing e dos robôs da OpenAI como `OAI-SearchBot` e `GPTBot`, o que a documentação da OpenAI diz que um site precisa permitir, de onde vêm os dados de empresa local e de mapa, como citações em terceiros, avaliações e diretórios pesam), o que difere do Google e dos resumos de IA do Google, e como medir presença (quais perguntas testar, com que frequência, o que registrar). Fonte primária primeiro (documentação da OpenAI e do Bing), depois estudos com dado; relato de praticante e de vendedor de curso só com a classe marcada. A sessão **não** abre o ChatGPT nem digita em página: entrega `docs/estudo/03b_chatgpt_roteiro_de_teste.md` com 30 perguntas reais de um morador ou síndico de São Paulo (por praga, bairro, urgência) e a planilha de registro, para o dono rodar na conta dele; o desenho do item 6 e o protótipo do item 7 trazem o que o estudo indicar (por exemplo `robots.txt`, dados estruturados, página "quem somos" verificável). | 6–8 |

Regra de evidência usada: linhas 36–48 do mesmo arquivo (classes A a D; "quem ganha"; consenso = classe A ou duas
fontes B independentes; fonte anterior a 2025 leva "pode estar desatualizada", e anterior a 2026 quando o assunto é
resposta de IA; número de outro país com o país ao lado).

---

## 2. As 26 falhas, uma a uma

Abreviações de arquivo: **01** = `01_google_organico.md`; **02** = `02_google_maps_perfil.md`; **03** =
`03_respostas_de_ia.md`; **03b** = `03b_chatgpt.md`; **rot.** = `03b_chatgpt_roteiro_de_teste.md` (todos em
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/`). Os números de linha são os da versão atual.

### 2.1 Falhas F1–F14 (guias (a) e (b))

| Falha | Situação | Onde está agora e o que vi |
|---|---|---|
| F1 — países trocados (360/374) | **Resolvida** | 01, linha 344: "360 cliques … nos Estados Unidos e 374 na União Europeia"; a nota final diz que o endereço guarda o título antigo. Reabri a página: o título exibido e o corpo dão 360 para os Estados Unidos e 374 para a União Europeia (seção 3.2) |
| F2 — "a distância pesa muito" como consenso | **Resolvida** | 02, linhas 81–84 (resumo: "é um dos três fatores"; ordem "disputada / não sei"; "uma base não cobre São Paulo inteira" marcada como inferência); linha 286 (classe do conjunto reescrita); linhas 342–351; linha 452; item 9 do consenso retirado (linhas 528–532); primeira linha de "disputado" (linha 553); item 17 de "não sei" (linhas 586–587). Sobrou uma frase solta na linha 299 (seção 7, O3) |
| F3 — "uma palavra-chave, uma página" confirmada como A | **Resolvida** | 01, linha 410: "Não confirmada por fonte oficial… permanece classe D"; linha 255: recomendação marcada "Inferência minha, não regra do Google"; linha 336: "'Uma página por busca' é escolha de desenho, inferência minha" |
| F4 — ponteiros de linha vencidos | **Resolvida** | 02: achei 56 remissões a linhas de `00_restricoes.md`; todas trazem o título da subseção ou do veredito e todas apontam para o trecho certo (seção 4). O cabeçalho (linhas 20–22) avisa que, se o arquivo mudar, vale o título |
| F5 — tensão entre os guias sobre medir posição | **Resolvida** | 02, linhas 105–112, 338, 352–356, 402–406, 444, 461, 479, 495 e item 16 do consenso (linhas 543–547): a grade de posição passou a "contraria a política do Google; não recomendada"; item 18 de "não sei" (linhas 588–589) diz que não se sabe como a ferramenta obtém o dado. 01, linha 366, remete ao guia (b), seção 9. Os dois guias dizem o mesmo. Ressalva de classe na seção 6, N2 |
| F6 — frase "popularity" ausente do guia (b) | **Resolvida** | 02, linhas 73–75 (resumo), 127 (linha nova na tabela 1.1), 136–139 e 514–516 (item 1 do consenso). A frase foi confirmada na página (seção 3.2) |
| F7 — dois trechos no limite do item 2 | **Resolvida** | (a) 02, linha 212 (linha nova com os dois itens da política), linha 238 (o relato ganhou "A política lida hoje diz o contrário… não usar"), passo 12 (linha 441), linha 453 e linha 475. (b) 02, linha 173: "isso **não** autoriza pôr o WhatsApp do intermediário em perfis de parceiras"; linha 455. Os dois itens da política foram confirmados na página (seção 3.2). Ressalva de classe na seção 6, N1 |
| F8 — First Page Sage como "B" | **Resolvida** | 01, linha 341: classe D, "só alegação"; linha 52 (regra 14): "é classe D e não sustenta esta regra"; linhas 348–349; linhas 466–467; linha 483; saiu da lista de classe B e entrou na de C e D (linhas 590–591). Classes compostas trocadas por uma só nas linhas 319, 409, 419, 428 e 482. Efeito colateral na seção 6, N3 |
| F9 — "números mundiais" | **Resolvida** | 02, linha 378: "**Abrangência (país) não informada pela fonte**"; linhas 540–541 do consenso. Reabri a página do Google de 16/04/2026: os quatro números são de 2025 e a página não diz a que países se referem |
| F10 — "estudo dos Estados Unidos" para o 1,74% | **Resolvida** | 01, linha 51 (regra 13), linha 306 (ficha), linha 386, linhas 393–394 e linha 408: país não informado para a amostra do 1,74%; "Estados Unidos" só para a amostra de palavras-chave. Confere com a página (seção 3.1, nº 9) |
| F11 — citação sem "recommended"; regiões das unidades de agregador | **Resolvida** | (a) 01, linha 277: citação completa, "This property is only recommended for sites that capture reviews about other local businesses" — confirmada na página. (b) 01, linhas 138 e 283: unidades de agregador e de fornecedor só no Espaço Econômico Europeu; outros recursos para a Turquia e a África do Sul — confere com a página (seção 3.1, nº 11) |
| F12 — fonte anterior a 2025 sem a marca | **Resolvida** | 02: linha 288 (15/09/2023), linha 293 (16/05/2024), linha 238 (caso de cerca de 2022), linha 275 (teste de cerca de 2023), linha 277 (2019 e 2022), linhas 93–94 (resumo) e linha 435 (passo 6). 01: linha 321. Todas as linhas listadas pelo verificador têm a marca. Uma linha fora da lista ficou sem ela (seção 7, O2) |
| F13 — nove afirmações sem fonte ou sem marca de inferência | **Resolvida** | 01: linha 52 ("não está na fonte A: é premissa minha"); linha 189 (exemplo "hipotético, meu, sem fonte conferida"); linha 337 ("Inferência minha, sem fonte aberta"); linhas 391–392 ("número meu, premissa de desenho"); linha 41 (classe "A (o texto da política) + inferência minha (a aplicação)"). 02: linha 333 ("Inferência minha, sem fonte e sem medição"); linha 311 ("Premissa minha, não conferida em fonte"); linha 129 ("recomendá-las é inferência minha… classe D"); linha 442 ("Inferência minha: tenderia a sustentar…") |
| F14 — citações em inglês sem tradução no guia (b) | **Resolvida** | 02: procurei por script todas as citações entre aspas com palavras inglesas: 40; 38 têm a tradução entre parênteses logo depois e as outras 2 (linhas 120 e 126) têm o título ou o texto oficial em português ao lado. As linhas 87–88 e 105–107 do resumo estão traduzidas. A nota da linha 48–49 explica o critério |

### 2.2 Falhas 1–12 (guia (c), parte do ChatGPT e roteiro)

| Falha | Situação | Onde está agora e o que vi |
|---|---|---|
| 1 — "registra que não houve comentário" | **Resolvida** | 03b, linha 159: "A matéria que cobriu o estudo **não traz posição da OpenAI**; registra que a página dos robôs não descreve o índice próprio" |
| 2 — complemento sem reconciliar o resto | **Resolvida** | 03b: aviso central reescrito (linhas 16–26); seção 1.1 (linhas 122–128); linhas 215–217; linha 238; seção 3.2 com a coluna "Situação depois do complemento" e a explicação de que os dois endereços são o mesmo artigo (linhas 242–265); seção 5.1 (linhas 299–311); linha 367 e leitura da seção 6 (linhas 376–379); linhas 397–398; limite 4 da seção 8 (linhas 455–459); itens 6 e 9 do consenso; item 6 de "disputado"; item 1 de "não sei". Rot.: linhas 36–38, 50–51 e a coluna `rede` (linha 178 e cabeçalho da linha 196). Procurei as frases antigas ("nada dali entrou", "nada foi conferido", "premissa não conferida"): não sobrou nenhuma |
| 3 — instruções opostas sobre como medir | **Resolvida** | A regra de medição é o mesmo bloco de 19 linhas nos três arquivos (seção 5.2). 03, linha 326 (tática 4.10) e linhas 328–329 passaram a remeter a ela. A frase da SparkToro foi citada e confirmada na página. "API ≠ aplicativo" está igual nos três ("uma B apoia… não é consenso") |
| 4 — Peec e Lily Ray sem endereço | **Resolvida** | 03, linha 303 (endereço, data, amostra, classe e "quem ganha" das duas), linha 321, linha 360 e item 5 de "disputado" (linhas 474–479). Abri as duas: endereços, datas, 11% e 69% conferem (seção 3) |
| 5 — "índice próprio" como consenso | **Resolvida** | 03b, linhas 165–168 (seção 1.5) e linhas 559–560 ("Indício forte, não consenso"); o item 6 do consenso foi trocado (linhas 539–545) |
| 6 — "com o Yelp à frente" como consenso | **Resolvida** | 03b, item 8 do consenso (linhas 547–551): "plataformas de avaliação e diretórios, entre elas o Yelp", com duas B independentes; "à frente" foi para "indício forte" (linhas 561–564), dizendo que as duas fontes da BrightLocal não contam como independentes |
| 7 — página "quem somos" acima da base | **Resolvida** | 03b, linha 480: "premissa marcada"; cita a linha 30 do quadro, a conclusão (iii), linhas 246–251, e as linhas 236–237 (CNPJ não exigido). Conferi as três em `00_restricoes.md`: estão certas. A remissão da linha 286 passou a "linhas 25–27", também certa |
| 8 — falta "pode estar desatualizada" | **Resolvida** | 03: linhas 186–189 (Bing, 2023), 192 (Microsoft, 08/10/2025), 252 (Ahrefs, 17/04/2025), 254 (Seer), 255 (Semrush), 343 e 349 (ações da seção 7.1). 03b: linha 82 e linha 144 (F10), linhas 76 e 78 (F4 e F6), linhas 273–275, 478–479 e item 10 do consenso (linhas 554–555) |
| 9 — consenso 9 convive com uma B contrária | **Resolvida** | 03: saiu do consenso (linhas 452–455) e virou o item 1 de "disputado" (linhas 459–464), com país por fonte; o item 8 do resumo (linhas 44–46) acompanha |
| 10 — inferências sem marca | **Resolvida** | 03b, linha 44 ("não diz 'só'… é inferência") e linha 39 ("ler 'Microsoft' como 'Bing' é inferência minha"). 03, linhas 173–175 ("Inferência minha, sem fonte… não se sabe") e linhas 38 e 437–438 ("que encontrei"). Rot., linhas 44 e 48 ("Premissa, sem fonte") e 257–258 ("premissa minha, sem fonte"); linhas 38 e 53 tratam do mapa no computador |
| 11 — roteiro: público, bairro e urgência | **Resolvida em parte** | Público: as cinco perguntas de comerciante saíram das 30 e estão no apêndice (rot., linhas 66–69 e 273–286); a contagem diz "Nenhuma pergunta de comerciante" (linha 148) e confere. Urgência: as 9 urgentes agora são leste 3, sul 2, norte 2, oeste 1, centro 1 (linhas 152–154), e há o aviso "Limite dos recortes" (linhas 156–159). **Bairro: as perguntas 12 e 25 continuam sem bairro**; o roteiro passou a dizer que é de propósito e por quê (linhas 51 e 67–68). O ponto foi justificado, não alterado: se "por bairro" no portão admite duas perguntas no nível da cidade é decisão do dono |
| 12 — miudezas (dez pontos) | **Resolvida** | `llms.txt`: 03b, linha 488. "Três robôs": 03b, linha 392 ("quatro"). "Majoritariamente em inglês": 03b, linha 152. "14,4%": 03b, linhas 369 e 446–449; rot., linha 31. F17 como "B fraca": 03b, linhas 89, 368, 378 e 553. Vereditos 4.1 e 4.8: 03b, seção 9.1 (linhas 516–525). Peso das avaliações: 03b, linhas 334–337 e item 11 de "não sei". Itens com fonte não aberta saíram de "disputado": 03, linhas 483–491. Aspas da Microsoft: 03, linhas 187–188. Anúncio F8: 03, linhas 117 e 433–434. "Não é direta": 03, linhas 226 e 465–468 |

---

## 3. Sorteio e conferências na fonte

### 3.1 Sorteio de 12 afirmações

**Método.** População: as linhas acrescentadas ou alteradas (prefixo `+`) do
`git diff -U0 343047c 86af317 -- docs/estudo` que trazem endereço de fonte (`http…` ou a abreviação `D:`), menos as
linhas da tabela de identificadores do `03b`: **122 linhas**. Embaralhei os números de 1 a 122 com `shuf` e a semente
`20261113` (`shuf --random-source=<(openssl enc -aes-256-ctr -pass pass:20261113 -nosalt </dev/zero)`) e percorri a
ordem sorteada pegando as 12 primeiras com endereço ainda não usado. Pulei: duas linhas cuja única fonte é a ajuda da
OpenAI (posições 113 e 121 da população; ela é tratada à parte na seção 3.3) e uma linha com endereço repetido
(posição 22). Ordem sorteada, do começo: 44, 32, 8, 66, 20, 28, 113, 121, 22, 45, 88, 5, 62, 4, 39.

| Nº | Afirmação conferida | Arquivo e linha | Endereço aberto | O que a fonte devolveu | Classe | Resultado |
|---|---|---|---|---|---|---|
| 1 | "The categories you select affect your local ranking on Google." | 02, linha 287 | https://support.google.com/business/answer/7249669?hl=en | A frase existe, igual. Pergunta falsa de controle ("Categories are the single most important ranking factor for Maps") rejeitada. A página não dá limite numérico de categorias, como o guia diz | A, certa | **Confere** |
| 2 | "There should only be one profile per business" | 02, linha 191 | https://support.google.com/business/answer/3038177?hl=en | A frase existe; também "Including unnecessary information in your business name isn't permitted", "Provide your regular customer-facing hours of operation." e a regra de ocultar o endereço. Controle falso ("one profile per neighborhood") rejeitado | A, certa | **Confere** |
| 3 | A fonte só diz que os recursos da página de resultado mudam com a busca; "mapa e anúncios acima do orgânico" é premissa | 01, linha 334 | https://developers.google.com/search/docs/fundamentals/how-search-works | "Based on the user's query the search features that appear on the search results page also change."; o exemplo da oficina de bicicleta está lá; a página não diz que mapa ou anúncio vêm acima do orgânico | A para a frase; premissa para o resto, como o guia marca | **Confere** |
| 4 | Estudo de 2023: aberto na hora da busca associado a posição melhor; 50 unidades, EUA | 02, linha 435 | https://brightlocal.com/research/study-business-opening-hours-and-local-rankings/ | 21/12/2023; 50 unidades em 10 categorias, EUA; grade 7 × 7 a cada 500 m; três dias; maior diferença: lanchonetes, 2,4 posições; inclui eletricista e ar-condicionado | B, com "pode estar desatualizada": certa | **Confere** |
| 5 | "When local customers search Google for an offering you provide, that service may be highlighted on your profile." | 02, linha 154 | https://support.google.com/business/answer/9455399?hl=en | A frase existe, igual; também "Custom services that violate policy will be automatically rejected."; sem limite numérico. Controle falso ("up to 50 services") rejeitado | A, certa | **Confere** |
| 6 | "If you add both options, only the text message option will be shown to customers." e "Different Business Profiles can use the same WhatsApp link." | 02, linha 173 | https://support.google.com/business/answer/15013580?hl=en | As duas frases existem; também a de "select regions". A página não lista países nem cita o Brasil. Controle falso rejeitado. Não abri a outra página citada na linha (14919056) | A, certa | **Confere** |
| 7 | Agência afirma ganho "quase imediato" com palavra-chave no nome, sem dado; 15/09/2023; classe D | 02, linha 288 | https://www.sterlingsky.ca/google-business-name-ranking/ | Data 15/09/2023; a página fala em "near-instant ranking boost"; não traz amostra nem números próprios (cita pesquisa de opinião de terceiro); quem publica é agência de SEO local | D, com "pode estar desatualizada": certa | **Confere** (os números do estudo de 2022 citado na mesma linha não foram reabertos) |
| 8 | Peec: 232 mil citações, 13 mil listas, 12 semanas, só software, seis motores; "~11% of citations come from self-promotional listicles"; taxa estável; país não informado | 03, linha 303 | https://peec.ai/blog/self-promotional-listicles-analysis-from-232k-citations | 03/03/2026; 232.000 citações e 13.000 listas; dezembro de 2025 a fevereiro de 2026; software; seis plataformas; a frase dos 11% existe; taxa estável; país não informado; a base do percentual não é explicitada. Controle falso ("37%") rejeitado | B (vendedor, amostra exposta): certa | **Confere** |
| 9 | Ahrefs: 1,74% de 1 milhão de páginas; país não informado para essa amostra; "Estados Unidos" só para a de palavras-chave | 01, linha 306 | https://ahrefs.com/blog/how-long-does-it-take-to-rank/ | 15/05/2025; 1 milhão de endereços vistos em setembro de 2023, sem país; 2 milhões em inglês, sem país; 1,3 milhão de palavras-chave "(in the US)"; 72,9%, 13,7%, 40,82% e 94% conferem. Controle falso rejeitado | B, certa | **Confere** |
| 10 | Grade de posição: 3 × 3 a 15 × 15; raio de 0,1 a 100 milhas; cobra por ponto; 20/05/2021; a fonte não diz como obtém o dado | 02, linha 402 | https://www.localfalcon.com/blog/how-to-find-the-optimal-local-scan-settings-for-new-keywords-or-businesses | 20/05/2021; grades de 3 × 3 a 15 × 15; exemplos com raio de 0,1 e de 100 milhas; créditos por ponto; nada sobre como o dado é obtido nem sobre permissão do Google. Controle falso ("official Google partner") rejeitado | D, certa | **Confere** (ver O1, sobre outra linha que usa a mesma fonte) |
| 11 | Unidades de agregador e de fornecedor só no Espaço Econômico Europeu; outros recursos para Turquia e África do Sul; Brasil não citado | 01, linha 283 | https://developers.google.com/search/docs/appearance/aggregator-features | Unidades de agregador e de fornecedor: região "EEA", incluindo "local businesses"; Turquia: recursos de sites de lugares e carrosséis; África do Sul: selo e carrosséis; Brasil não aparece | A, certa | **Confere** |
| 12 | rankings.io: cerca de 1.100 escritórios, 20 por cidade, 50 cidades, EUA, 30/06/2021; uma busca; posição acima de 20 gravada como 25 | 02, linha 268 | https://rankings.io/proximity-data-study | Atualizado em 30/06/2021; 1.100 escritórios; "car accident lawyer"; queda média de 8 posições na primeira milha, de 5 a 12 entre cidades; 56% em 1º no próprio endereço; "20+" gravado como 25; Pittsburgh 27%, Queens 92%, Nova York 80% a cerca de 10 milhas. Não compara a distância com outros fatores | B, com "pode estar desatualizada": certa | **Confere** |

**Resultado do sorteio: 12 conferem, 0 falhas.**

### 3.2 Conferências obrigatórias, fora do sorteio

| Ponto | Arquivo e linha | Endereço aberto | O que a fonte devolveu | Resultado |
|---|---|---|---|---|
| Lily Ray, 17/06/2026: endereço, 69%, o que mede | 03, linhas 303, 321, 360 e 477 | https://lilyraynyc.substack.com/p/why-calling-yourself-the-best-could | Publicado em 17/06/2026; 100 buscas "best [category] software" em 15/04, 15/05 e 08/06/2026, pela ferramenta de marca da Ahrefs; 80 mostraram resumo de IA; "224 of the 323 self-promotional listicles cited"; a marca autora ficou fora da recomendação "69% of the time". País não informado; a autora não declara empregador nem vínculo. Controle falso ("92%") rejeitado. **Mede se a marca autora é recomendada**; a Peec (nº 8 acima) **mede se a lista é citada** — é o que o guia diz | **Confere** |
| "usually at least 60-100X" | 03, linhas 398–404; 03b, linhas 425–431; rot., linhas 28 e 217–223 | https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/ | 28/01/2026. A frase existe: "…you need to ask over and over again; usually at least 60-100X, then average these out". Está na parte de opinião do autor; a página lista como pergunta em aberto quantas execuções bastam e se a API imita o uso manual; conflito com a Gumshoe declarado. Controle falso ("500-1000X") rejeitado | **Confere** |
| "Machine-generated traffic" | 01, linha 366; 02, linhas 403 e 543–547 | https://developers.google.com/search/docs/essentials/spam-policies | A seção existe; define a prática como "sending automated queries to Google"; cita "scraping results for rank-checking purposes" e "without express permission"; traz "Such activities violate our spam policies and the Google Terms of Service." Não menciona Maps nem perfil de empresa. Controle falso rejeitado | **Confere** (a aplicação ao Maps é leitura do guia: ver N2) |
| "Local results are mainly based on relevance, distance, and popularity." | 02, linhas 73–75, 127 e 514–516; 01, linha 335 | https://support.google.com/business/answer/7091?hl=en | A frase existe, igual; a seguinte é "Together, these factors help Google find the best match for customers' searches."; há seção "Prominence"; a página não ordena os fatores; não contém a frase antiga com "primarily… prominence"; não cita diretórios. Controle falso ("Distance is the most important ranking factor") rejeitado | **Confere** |
| Itens da política de avaliações sobre equipe | 02, linhas 212 e 238 | https://support.google.com/contributionpolicy/answer/7400114?hl=en | Sob "We do not allow merchants to:" estão "Merchants requesting that staff solicit a certain number of reviews" e "Merchants requesting that staff solicit reviews that include specific content, including content that identifies a staff member"; também os trechos de "We do allow merchants to:". Controle falso ("may reward employees") rejeitado. A página **não fala de prêmio a funcionário** (ver N1) | **Confere** |
| 360 (Estados Unidos) e 374 (União Europeia) | 01, linha 344 | https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/ | Título exibido: "For every 1,000 EU Google Searches, only 374 clicks go to the Open Web. In the US, it's 360."; corpo: 360 nos Estados Unidos, 374 na União Europeia; 02/07/2024; dados da Datos, "A Semrush Company". O endereço, lido ao pé da letra, traz os países na ordem contrária, como o guia registra (a ferramenta disse que o endereço também liga 374 à Europa; a leitura literal do endereço é minha) | **Confere** |

Outras duas páginas abertas para fechar F9 e F11: a página de dados estruturados `LocalBusiness` (a frase com
"recommended" existe para `aggregateRating` e `review`) e o texto do Google de 16/04/2026 sobre o Maps (292 milhões,
13 milhões, 79 milhões e 782 mil, de 2025, sem abrangência geográfica declarada). As duas conferem.

### 3.3 Seção "Complemento da sessão principal" do `03b_chatgpt.md` (linhas 28–53)

https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt devolveu **erro 403** à ferramenta de
leitura. **INCONCLUSIVO; não é falha.** Os trechos do complemento (provedores parceiros, reescrita da consulta,
localização por IP, memória, dados locais, mapa, critério de escolha, o que o site precisa permitir, uso sem conta)
continuam apoiados **só na leitura da sessão principal no navegador**. O arquivo diz isso em todos os lugares onde usa
o complemento (a "fórmula" das linhas 23–26), inclusive nos itens 6 e 9 do consenso.

---

## 4. Ponteiros do guia (b) para `00_restricoes.md`

**Método.** Listei por script todas as remissões "linha N" e "linhas N–M" do guia (b) que apontam para
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`: 56. Sorteei 12 com a mesma semente (`20261113`);
ordem: 54, 46, 34, 33, 9, 24, 16, 19, 49, 6, 7, 42. Para cada um, li as linhas citadas.

| Nº | Linha do guia (b) | O que o guia diz que está lá | O que as linhas citadas contêm | Resultado |
|---|---|---|---|---|
| 54 | 477 | subseção "4. Caminhos legítimos para o mapa" inteira, até "O que isso corta do plano", linhas 105–140 | linha 105: título da subseção 4; linhas 136–140: "O que isso corta do plano" | Certo |
| 46 | 472 | subseção 2, linhas 67–71 (caixa postal, escritório virtual, coworking); quadro, linha 26 | 67: caixa postal; 68–69: escritório virtual; 70–71: coworking; linha 26: "Endereço de fachada… Vedado" | Certo |
| 34 | 453 | veredito da linha 29 do quadro | linha 29: "Avaliação comprada, incentivada ou escrita por quem tem vínculo — Vedado" | Certo |
| 33 | 453 | subseção 3, itens "Avaliações" e "Sanção ao perfil por avaliação falsa", linhas 95–100 | 95–98: avaliações; 99–100: sanção ao perfil | Certo |
| 9 | 173 | seção (d), "Os dois desenhos", linhas 434–437 | 432: título "Os dois desenhos"; 434–437: desenho A, vedado na API e não conclusivo no aplicativo gratuito | Certo |
| 24 | 307 | subseção 4, linhas 117–119; veredito da linha 27 do quadro | 117–119: "Website content must be owned and managed by the business owner"…; linha 27: perfil com site ou telefone do intermediário, vedado | Certo |
| 16 | 212 | quadro de vereditos, linha 29 | como no nº 34 | Certo |
| 19 | 238 | seção (a), subseção 3, linhas 95–98 | item "Avaliações": pago, incentivo, seleção, conflito de interesses | Certo |
| 49 | 474 | subseção 4, linhas 113–115 (propriedade do perfil) | "make the business owner the owner of the profile"… "retain ownership or co-ownership" | Certo |
| 6 | 173 | quadro de vereditos, linha 27 | como no nº 24 | Certo |
| 7 | 173 | subseção 2, linhas 78–80, e vereditos, linhas 82–85 | 78–80: telefone e site do perfil; 82–85: parágrafo "Vereditos" | Certo |
| 42 | 460 | subseção 3, citação sobre conta restrita, linhas 90–91 | "If a merchant's account is restricted, all Business Profiles… will be suspended." | Certo |

**12 de 12 certos.** Conferi também os outros 44, lendo as mesmas faixas de `00_restricoes.md` (linhas 21–38, 53–144,
179–251 e 432–437): **56 de 56 certos**. Os dois ponteiros para o anexo
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes_anexos/00a_perfil_google.md` (linhas 61 e 149) também
estão certos. Os ponteiros do `03b` para `00_restricoes.md` (linhas 25–27, 30, 236–237 e 246–251) e para
`/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md` (linhas 168–169 e 171) estão certos. Nenhuma
remissão aponta para linha que não existe. As remissões internas entre guias ("guia (b), seção 9"; "guia (a), seções
2.1 e 8"; "seção 7.3"; "seção 9.1"; "seção 3.2") apontam para seções que existem.

---

## 5. Roteiro, regra de medição e coerência

### 5.1 Roteiro contra o portão (`03b_chatgpt_roteiro_de_teste.md`)

| Exigência | O que vi | Resultado |
|---|---|---|
| Exatamente 30 perguntas | Lista numerada de 1 a 30, sem salto (linhas 71–100); tabela com 30 linhas (linhas 106–135) | Cumpre |
| Todas de morador ou síndico; nenhuma de comerciante nas 30 | Li as 30: 10 de morador de apartamento, 11 de morador de casa, 7 de síndico ou síndica, 2 sem dizer casa ou apartamento. Busca por "bar", "restaurante", "lanchonete", "loja", "comércio": nada nas 30. As cinco de comerciante estão no apêndice (linhas 273–286), fora das contagens | Cumpre |
| Distribuição por praga | Refeita por script: baratas 4 · baratas e formigas 1 · baratas e ratos 1 · ratos 4 · cupim 3 · escorpião 2 · percevejo 2 · pulgas 2 · formigas 2 · pombos 2 · mosquito 2 · geral 5 = 30. Igual ao declarado (linhas 140–142), números das perguntas inclusive | Bate |
| Distribuição por bairro e região | sul 6 · leste 6 · centro 6 · norte 5 · oeste 5 · cidade, sem bairro 2 = 30. Igual ao declarado (linhas 143–144). 28 bairros diferentes; cada bairro está na região certa | Bate |
| Distribuição por urgência | agora/hoje 9 (2, 6, 9, 16, 18, 19, 23, 24, 26) · planejado 21 = 30; urgentes por região: leste 3, sul 2, norte 2, oeste 1, centro 1. Igual ao declarado (linhas 145 e 152–154). Li o texto das 9: todas pedem atendimento "hoje" ou "agora" | Bate |
| Público e tipo | Público: 10 + 11 + 7 + 2 = 30; tipo: indicação 17, confiança 6 (a 25 também fala de preço), comparação 4, preço 3 = 30. Igual ao declarado (linhas 146–150) | Bate |
| Planilha de registro | 22 colunas na lista (linhas 171–191, contando `data` e `hora` como duas), 22 no cabeçalho CSV (linha 196) e 22 campos em cada uma das duas linhas de exemplo (linhas 197–198), lidas com leitor de CSV; a lista e o cabeçalho têm os mesmos nomes, na mesma ordem | Cumpre |
| Nenhuma pergunta com nome, endereço, telefone | Nenhum nome de pessoa ou de empresa, nenhum telefone, e-mail, CEP, rua ou número. "99 reais" (pergunta 25) é preço de anúncio genérico | Cumpre |
| Nenhuma instrução de contatar empresa, criar conta, aceitar termos, preencher formulário | Os avisos (linhas 262–271) proíbem dado pessoal, botão de contato, anúncio e contato com empresa; o roteiro usa a conta que o dono já tem e a janela anônima; não manda criar conta nem aceitar nada | Cumpre |
| Exemplos marcados "EXEMPLO" | As duas linhas de exemplo começam com `EXEMPLO-2026-11`, têm nomes "EXEMPLO…" e domínios `.example`; o bloco de `robots.txt` do `03b` usa `EXEMPLO.example` | Cumpre |
| Subconjunto das repetições | As perguntas 1, 2, 12, 13, 16 e 29 cobrem as cinco regiões mais a pergunta sem bairro, as duas urgências e os quatro tipos, como a linha 236–237 afirma. A conta de tempo (66 execuções, 2h15 a 3h20) fecha | Confere |

### 5.2 Regra de medição única

O bloco "Regra de medição (texto igual em…)" está em 03, linhas 388–406; em 03b, linhas 415–433; e no roteiro, linhas
207–225. Extraí os três por script: **19 linhas cada, mesma soma SHA-1 (`dd99fe7d…`), iguais byte a byte.** O bloco
diz, com todas as letras, que a rodada mensal "**não mede uma pergunta isolada**" (item 1) e que "**Este roteiro não
atinge esse número**" (item 3, sobre as 60 a 100 repetições). O resto de cada arquivo acompanha: 03, linhas 326,
328–329 e 415–417; 03b, linhas 412 e 435–439; roteiro, linhas 28, 46 e 229–239. Não achei, em nenhum dos três, frase
que ainda trate a repetição como opcional ou a janela anônima como o modo principal.

### 5.3 Coerência entre os guias e com o item 2

- **Medir posição por consulta automática.** Guia (a), linhas 53 e 366: prática vedada pela política de spam; a
  posição vem do Search Console. Guia (b), linhas 105–112, 352–356, 402–406, 444, 461, 479, 495 e 543–547: a grade e o
  rastreador de posição "contrariam a política do Google; não recomendada", fora do serviço oferecido. **Dizem o
  mesmo.**
- **Guia (b) dentro do item 2.** Perfil próprio do site: vedado (linhas 12–14, 77–78, 471). Endereço de fachada:
  vedado (linhas 292, 456, 472). Telefone, WhatsApp ou site do intermediário no perfil: vedado (linhas 160, 173, 294,
  307, 434, 455, 473). Avaliação incentivada, filtrada ou roteirizada: vedada (linhas 208–212, 441, 453, 475, 497).
  WhatsApp compartilhado entre parceiras: "não usar" (linhas 173 e 455). Não achei tática que saia do que o item 2
  permitiu.
- **Seções "O que é consenso", lidas inteiras.** Guia (a), linhas 441–470: 15 itens, todos classe A; o que tem só uma
  B fica no parágrafo "Quase consenso, mas não fecha", fora da lista. Guia (b), linhas 510–547: 15 itens vigentes,
  todos classe A (dois "por ausência"); o item 9 é só o registro da retirada. Guia (c), linhas 423–455: 8 itens classe
  A e 2 com duas B independentes (itens 9 e 10); ver O6. `03b`, linhas 531–555: itens 1 a 5 e 10 classe A; item 6
  classe A com a ressalva do 403; item 7 com duas B independentes; item 8 com duas B independentes; item 9 classe A
  (com a mesma ressalva) mais uma B. O roteiro não tem seção de consenso. **Nenhum "consenso" sem classe A nem duas B
  independentes.**

---

## 6. Defeitos novos, introduzidos pela correção (todos menores)

**N1 — "Prêmio a funcionário por avaliação" com classe A e atribuído ao item 2.** Guia (b), linhas 96–97 (resumo,
item 9, sob "[A + B]"), 212, 441, 453 ("A") e 475. A política lida veda pedir à equipe um número de avaliações e
avaliações com conteúdo específico ou que identifique funcionário; **não fala de prêmio a funcionário**, e as linhas
95–100 de `00_restricoes.md` tratam de incentivo a quem avalia, não à equipe. A orientação "não usar" é prudente; a
classe é que está acima da base. *Correção sugerida:* "meta de número e pedido de citar funcionário: vedados (A);
prêmio a funcionário por avaliação: não usar, por inferência minha (a política não o cita)".

**N2 — "Contraria a política do Google (A)" sem a ressalva de alcance.** Guia (b), linhas 108–111, 354–355, 402, 444,
461, 479 e 495 afirmam, com classe A, que a grade de posição do mapa contraria a política. A ressalva de que a página
é a das políticas de spam da **Busca** e de que alcançar a consulta feita dentro do Maps "é leitura minha" só aparece
nas linhas 403 e 545–546. Guia (a), linha 366, também afirma sem ressalva ("Vale também para… a 'grade de posição' de
ferramenta de mapa"). A seção da política, relida, não menciona Maps. *Correção sugerida:* nas linhas citadas, "A
para a regra; aplicação ao Maps: leitura minha", e a mesma ressalva na linha 366 do guia (a).

**N3 — Frase que perdeu a base quando a First Page Sage virou classe D.** Guia (a), linhas 348–350: "O que se repete
em duas fontes B… **em busca local o orgânico não é o primeiro lugar para onde o clique vai**". Quem dizia isso era a
First Page Sage (bloco local acima do orgânico). A linha 340 do próprio guia dá, para a Backlinko, 65% de cliques em
orgânico contra 42% no mapa — o contrário. *Correção sugerida:* usar a formulação das linhas 468–470 ("o bloco do
mapa leva fatia grande dos cliques em busca local"), que as duas fontes B sustentam.

**N4 — Três rótulos para a mesma fonte.** Guia (c): a fonte de 17/06/2026 sobre listas autopromocionais é "Classe B
(amostra pequena)" na linha 303, "B pequena" e "B fraca + restrição" na linha 360, e "B pequena" na linha 477. Pela
legenda do próprio guia (linha 19), "B fraca" não vira regra. Não muda conclusão (o ponto está em "disputado").
*Correção sugerida:* um rótulo só, nos três lugares.

**N5 — Coluna `execucao` não definida para a subamostra deslogada.** Roteiro, linha 174: "1 na rodada mensal; 2 a 6
nas cinco repetições"; a linha 239 só diz `conta` = `deslogada`. *Correção sugerida:* "na subamostra deslogada,
`execucao` = 1 e `conta` = `deslogada`".

Não achei, entre os efeitos da correção: tabela quebrada (ver O4, que é anterior), remissão para linha inexistente,
contradição entre trecho antigo e novo além de N3, nem classe trocada sem motivo (a troca de "C com ressalva (quase
D)" por "D" na linha 319 do guia (a) segue o pedido de F8 e é coerente com "quem ganha").

---

## 7. Defeitos antigos que ficaram (fora das 26 falhas; todos menores)

**O1 — "Raio" onde a fonte diz "tamanho da grade"; "EUA" não declarado.** Guia (b), linha 338: "sugere medir num raio
de 2 milhas… e 5 milhas"; coluna de observação: "**EUA.**". Em duas leituras, a página diz "Grid size = 2 miles" e
"Grid size = 5 miles" e não declara país. *Correção sugerida:* "grade de 2 milhas… e de 5 milhas"; "país não
informado".

**O2 — Linha de 2022 sem "pode estar desatualizada".** Guia (b), linha 383 ("idem", 11/04/2022, B fraco); a linha 382,
da mesma fonte, tem a marca. *Correção sugerida:* acrescentar.

**O3 — Resto do tom de F2.** Guia (b), linha 299: "'perto de mim' é uma busca em que a distância **decide**", com
"A (mecanismo)". A fonte A só diz que, sem local na busca, o Google usa a localização da pessoa. *Correção sugerida:*
"em que a localização de quem busca entra (A)".

**O4 — Linha de tabela com 3 colunas numa tabela de 4.** `03b_chatgpt.md`, linha 239 ("Existe anúncio no ChatGPT?"):
"F1 (A) · F32 (C)" ocupa uma célula só e falta a coluna de classe. Já estava assim no commit `343047c` (linha 212).
Foi a única linha com número de colunas divergente nas 88 tabelas dos cinco arquivos (contagem por script).
*Correção sugerida:* "… | F1; F32 | A (F1) · C (F32) |".

**O5 — Classes compostas fora do guia (a).** Guia (c), linha 257: "C/D"; guia (b), linhas 85 e 90: "[B fraco/C]" e
"[D/B]". F8 pediu classe única só para o guia (a). *Correção sugerida:* uma classe por fonte.

**O6 — Dois detalhes no consenso do guia (c).** Item 2 (linhas 427–428): a primeira metade é classe A; a segunda ("os
arquivos quase não são pedidos por robôs") apoia-se em **uma** B. Item 10 (linhas 446–447): uma das duas B é de
22/07/2025 e não leva "pode estar desatualizada" na linha do consenso (leva na linha 239). *Correção sugerida:* no
item 2, "(uma B)" ao lado da segunda metade; no item 10, a marca.

**O7 — Miudezas do roteiro.** Linha 135: a pergunta 30 está como "síndico", mas o texto só diz "Nosso condomínio";
linha 108: a pergunta 3 está como "baratas e ratos", e o texto diz "dedetização e desratização". Linhas 197–198: os
exemplos usam `nao`, `diretorio` e `mapa e cartoes`, e a lista de valores (linhas 181–188) usa `não`, `diretório` e
`cartões`. *Correção sugerida:* acertar o rótulo ou o texto; escolher uma grafia.

---

## 8. O que conferi e não achei problema

- As 26 falhas, cada uma na linha atual, lendo os cinco arquivos inteiros (2.652 linhas) e o diff das correções.
- 20 páginas públicas abertas com resposta (12 do sorteio, 6 obrigatórias e 2 extras), com pergunta falsa de controle
  nas que decidiam: todas rejeitaram a frase falsa.
- 56 ponteiros do guia (b) e 6 do `03b`.
- Número de colunas de 88 tabelas (um desvio, antigo: O4).
- As 30 perguntas contra a tabela (praga, bairro, região, urgência, público) e contra o portão.
- Igualdade do bloco da regra de medição nos três arquivos.
- 40 citações em inglês do guia (b), todas com tradução.
- As quatro seções "O que é consenso", item por item.
- Limites do item 2 no guia (b), um a um.

## 9. O que esta verificação não cobre

- **Fontes das linhas que a correção não tocou.** Só reabri fontes de linhas alteradas ou acrescentadas. Não reabri,
  por exemplo, First Page Sage, Backlinko, Near Media, Pew, Semrush, Seer, Resoneo, BrightLocal (os três estudos de
  IA), Whitespark, Search Atlas, a página 14919056 do Google nem os números do estudo de 2022 citado na linha 288 do
  guia (b).
- **A ajuda da OpenAI** (erro 403): o complemento do `03b` não foi reconferido por ninguém além da sessão principal.
- **Limite da ferramenta de leitura.** Ela responde por um modelo pequeno e corta citações acima de cerca de 125
  caracteres: as frases longas (por exemplo a segunda da política de avaliações e a seção inteira "Machine-generated
  traffic") foram confirmadas em pedaços, não por cópia integral. Uma resposta dela contrariou a leitura literal de um
  endereço (seção 3.2, última linha): fiquei com a leitura literal.
- **Páginas vivas.** As páginas de ajuda do Google não têm data; o que conferi vale para 13/11/2026, 21:28 a 21:42.
- **Conteúdo jurídico.** Conferi ponteiros e coerência com `00_restricoes.md`, não o mérito das normas.
- **O roteiro na prática.** Não abri o ChatGPT nem outro assistente; não sei se o chat temporário exclui a memória,
  nem se a versão sem conta deixa buscar.
- **Outros arquivos.** Não conferi `00x_metodo_do_exemplo_x.md`, o anexo `00a` além das duas linhas citadas, nem nada
  do item 4. Havia arquivos de outro trabalho em andamento em `data/` e `docs/mercado/`; não os li nem toquei.
- **Posição no Google.** Nada aqui diz quem aparece em busca alguma.
