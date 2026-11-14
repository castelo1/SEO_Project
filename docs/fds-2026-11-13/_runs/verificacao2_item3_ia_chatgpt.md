# Verificação 2 — item 3, parte 2: guia (c) respostas de IA, parte do ChatGPT e roteiro de teste

- **Quem verificou:** subagente em contexto limpo, sem a conclusão de ninguém. Não abri nenhum arquivo cujo nome
  começa por `verificacao` ou `correcoes` em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`, e
  desconsiderei o que os próprios artefatos dizem sobre verificações anteriores.
- **Quando:** sábado, 14/11/2026, das 01:22 às 01:34 (Brasília; `TZ=America/Sao_Paulo date`). Toda "reaberta em" abaixo
  é 14/11/2026.
- **Como:** leitura integral dos três artefatos; reabertura das fontes pela ferramenta de leitura de página pública
  (sem navegador, sem busca ao vivo no Google, sem abrir o ChatGPT, sem digitar em página). A ferramenta responde por
  meio de um modelo pequeno: cada trecho literal foi conferido com frases falsas de controle misturadas (todas
  rejeitadas), e o que deu divergência foi pedido uma segunda vez, em chamada separada, antes de virar achado.
- **Nada foi editado** além deste arquivo. Nenhum `git` de escrita.
- **Lembretes ignorados (1 linha):** o `CLAUDE.md` global pediu carregar as ferramentas do meli-memory, chamar
  `mem_context`, salvar memória, resumir a sessão e oferecer "compound" — **não executei** (regra da rodada e do
  `CLAUDE.md` do projeto).
- **Efeito colateral a registrar:** ao ler `https://openai.com/chatgpt-user.json`, a ferramenta de leitura gravou
  sozinha uma cópia de 8,4 KB na pasta de resultados dela, fora do projeto. Não baixei nada para o projeto nem para `/tmp`.

## Vereditos

| Arquivo | Veredito | Sorteio | Resumo |
|---|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | **APROVADO COM RESSALVAS** | 0 falhas em 12 | Fontes oficiais conferem, trecho a trecho. Ressalvas: quatro frases mais fortes que a fonte e um critério de "B fraca" aplicado de modo desigual |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | **APROVADO COM RESSALVAS** | 0 falhas em 12 (3 sorteadas **não reabertas** por erro 403 e trocadas) | Portão coberto ponto a ponto. Ressalvas: um número mal enquadrado (33%), três "disputados" com um lado não aberto, critério de "B fraca" que derrubaria dois consensos, e a ajuda da OpenAI segue sem leitura independente |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | **APROVADO COM RESSALVAS** | não se aplica | 30 perguntas, contagens e planilha conferem por script. Ressalva: os tipos de fonte da planilha não batem com os do guia (c) e deixam de fora vídeo e rede social |

Nenhum arquivo passou de 2 falhas em 12. Não achei promessa de citação nem de posição em nenhum dos três.

---

## 1. O que abri

**Artefatos (inteiros):** os três acima. **Regras:** seções "Fronteira", "Pesquisa na web e navegador", "Verificação"
e "Forma" de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md`. **Remissões internas conferidas:**
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 25–30, 236–237 e 246–251 (dizem o que o
03b afirma); `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md`, linhas 168–171 (idem).

### 1.1 Fontes oficiais reabertas (todas as citadas da OpenAI, da Microsoft/Bing e do Google)

| Fonte | Endereço | Resultado em 14/11/2026 |
|---|---|---|
| OpenAI, robôs | https://developers.openai.com/api/docs/bots | **Confere**, em duas chamadas. Os 13 trechos literais do 03b (seção 2) estão na página; as 2 frases falsas foram rejeitadas. Só quatro robôs (`OAI-SearchBot`, `GPTBot`, `ChatGPT-User`, `OAI-AdsBot`), com os user-agents e os arquivos de IP citados. Sem data. Não cita Bing, Google, sitemap, `noindex` nem JavaScript; traz o link para o `llms.txt` do próprio site de documentação; não descreve índice nem robô de agente |
| OpenAI, endereço antigo | https://platform.openai.com/docs/bots | **Confere**: 301 para o endereço acima |
| OpenAI, IPs do robô de busca | https://openai.com/searchbot.json | **Confere**: `creationTime` 2026-01-02; 39 faixas IPv4 |
| OpenAI, IPs dos outros robôs | https://openai.com/gptbot.json · https://openai.com/chatgpt-user.json | Existem (18 e 237 faixas). O 03b não cita esses números |
| OpenAI, API "Web search" | https://developers.openai.com/api/docs/guides/tools-web-search | **Confere**: os 2 trechos literais; não nomeia provedor; não fala do aplicativo; sem data |
| OpenAI, ajuda "Searching the web with ChatGPT" | https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt e `…/9237897-chatgpt-search` | **Não reaberto** (erro 403 nas duas). Não substituí por fonte de segunda mão |
| OpenAI, perguntas de publishers | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | **Não reaberto** (403) |
| OpenAI, busca em Enterprise/Edu | https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu | **Não reaberto** (403) |
| OpenAI, anúncio da busca | https://openai.com/index/introducing-chatgpt-search/ | **Não reaberto** (403) |
| Microsoft, Bing Webmaster Tools | https://blogs.bing.com/webmaster/2025/6/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility/ | **Confere**: 17/06/2025; os 6 trechos literais (inclui "AI tools like ChatGPT and Inflection.ai"); sitemap processado ao menos a cada 24 horas |
| Microsoft, AI Performance | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview (e a forma `/2026/2/…`) | **Confere**: 10/02/2026; os 3 trechos; parceiros não nomeados; sem ChatGPT, sem cliques; recomenda títulos, tabelas, perguntas e respostas, evidência, conteúdo atual, IndexNow e Bing Places. **Não cita esquema** (esquema está só no texto de 08/10/2025) |
| Microsoft, sitemaps | https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search | **Confere**: 31/07/2025; sinal de base, `lastmod` real, somar com IndexNow |
| Microsoft, IndexNow | https://www.bing.com/indexnow/getstarted | **Confere**: chave em arquivo no site; "does not guarantee"; sem OpenAI; sem data |
| Microsoft, Web IQ | https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ | **Confere**: 02/06/2026; os 2 trechos; não cita ChatGPT nem OpenAI |
| Microsoft, controles do Bing Chat | https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat | **Confere**: 22/09/2023; os 3 trechos; `NOARCHIVE` fora do treino; com as duas tags vale `NOCACHE`; seguem na busca |
| Microsoft, blog de anúncios | https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers | **Confere**: 08/10/2025; os seis pontos da paráfrase |
| IndexNow | https://www.indexnow.org/ e https://www.indexnow.org/documentation | **Confere**: cinco buscadores, sem Google; 200 = só recebimento |
| Bing, diretrizes | https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | **Não reaberto**: só o título (igual ao que os artefatos declaram) |
| Bing Places, ajuda | https://www.bing.com/forbusiness/help/ | **Não reaberto**: página vazia (igual ao declarado) |
| Google, recursos de IA | https://developers.google.com/search/docs/appearance/ai-features | **Confere**: os 4 trechos literais; tipo "Web"; indexação não garantida; não nomeia `llms.txt`; sem data. A frase sobre o Perfil da Empresa aqui é "Checking that your Merchant Center and Business Profile information is up-to-date" (o trecho com "ensure that" é da fonte de 21/05/2025, como o guia indica) |
| Google, guia de otimização para IA | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | **Confere**: os 5 trechos; `llms.txt` nomeado entre os mitos ("Google Search ignores them"); seção de negócio local; sem data |
| Google, blog de 21/05/2025 | https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search | **Confere**: data e os 2 trechos; marcação igual ao conteúdo visível; sem número que sustente "cliques de maior qualidade" |
| Google, meta tag robots | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag | **Confere**: os 2 trechos (`nosnippet`, `max-snippet`); `noarchive` e `nocache` não usados pela Busca; `data-nosnippet` não cita IA |
| Google, rastreadores comuns | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers | **Confere**: trecho do `Google-Extended`; sem user-agent próprio; treino e fundamentação no Gemini e na Vertex AI |
| Google, controle de IA no Search Console | https://support.google.com/webmasters/answer/16908024?hl=en | **Confere**: os 3 trechos. A página tem **três** opções: Incluir, Excluir e "herdar do pai" (ver achado 6) |
| Google, relatório de IA generativa | https://support.google.com/webmasters/answer/16984139?hl=en | **Confere**: os 2 trechos; só impressões; páginas, países, datas, aparelhos |
| Google, blog de 03/06/2026 | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | **Confere**: data; nota de 31/08/2026; "included in the overall performance report"; sem "Web"; inclui Discover |
| Google, políticas de spam | https://developers.google.com/search/docs/essentials/spam-policies | **Confere**: trecho sobre manipular respostas de IA; os três itens de spam de links |
| Google, posição na Visão geral | https://support.google.com/webmasters/answer/7042828?hl=en | **Confere** a paráfrase |
| Google, sistemas de ranqueamento | https://developers.google.com/search/docs/appearance/ranking-systems-guide | **Confere**: em geral, não mais de duas listagens do mesmo site |
| Google Brasil, 15/08/2024 e 08/09/2025 | endereços F10 e F11 do guia (c) | **Conferem**: datas e os dois trechos em português; "desdobramento de pergunta (query fan-out)" |
| Google, Modo IA (05/03/2025 e 21/08/2025) | https://blog.google/products-and-platforms/products/search/ai-mode-search/ · https://blog.google/products-and-platforms/products/search/ai-mode-agentic-personalized/ | **Conferem** quanto ao Mapa do Conhecimento e ao Maps. **Divergência** no agendamento de serviço local (achado 4) |
| `llms.txt` | https://llmstxt.org/ | **Confere**: 03/09/2024; modificada em 10/08/2026; pensada para a consulta; não afirma uso por buscador |
| Perplexity, Apple, Anthropic | https://docs.perplexity.ai/guides/bots · https://support.apple.com/en-us/119829 · endereço da Anthropic citado no guia (c) | **Conferem** todos os trechos literais; Apple com data 04/09/2026 |

---

## 2. Sorteios

Semente **20261114** (`random.seed`, depois `random.sample` sobre a lista de linhas). População: linhas de dados das
tabelas (sem cabeçalho). Tomei as 12 primeiras da permutação.

### 2.1 `03_respostas_de_ia.md` — população de 71 linhas (linhas 83 a 282) — **0 falhas em 12**

| # | Linha | Afirmação (resumo) | Fonte reaberta | Existe? Diz aquilo? Data? | Resultado |
|---|---|---|---|---|---|
| 1 | 98 | `robots.txt` do Googlebot controla o rastreamento, IA incluída; sem token separado | Google, recursos de IA | "AI is built into Search"; Googlebot é o controle; nenhum token separado nomeado | confere |
| 2 | 156 | Modo IA usa Mapa do Conhecimento e "informações do mundo real"; agente usa Mapa do Conhecimento e Maps; nenhum cita o Perfil da Empresa | Blog do Google, 05/03/2025 e 21/08/2025 | trechos e datas conferem; Perfil da Empresa ausente nos dois | confere |
| 3 | 241 | Busca local: Perfil da Empresa, site, Yelp, Facebook; 16/09/2026; país não informado | BrightLocal, estudo de visibilidade | 28,5%, 42%, 9,53%, 2,23%; data confere; país ausente | confere |
| 4 | 253 | −58% na 1ª posição (dez/2023 × dez/2025); 2ª −50,8%; 10ª −19,4%; sem resumo 0,076 → 0,039 | Ahrefs, 04/02/2026 | todos os números e a data | confere |
| 5 | 115 | Aparições em IA entram no relatório de Desempenho, tipo "Web" | Google, recursos de IA | "within the "Web" search type" | confere |
| 6 | 252 | −34,5% (mar/2024 × mar/2025); 300 mil palavras-chave; só computador; país não informado | Ahrefs, 17/04/2025 | tudo confere; a página diz que o "sem resumo" é projeção, como o guia anota | confere |
| 7 | 88 | "There's no requirement to break your content into tiny pieces…" | Google, guia de otimização | literal | confere |
| 8 | 227 | 32,3% → 54,5%; 16,7% nos 10 primeiros; saúde 75,3%; restaurantes 19,2%; 9 setores; sem palavras-chave nem país; 18/09/2025 | BrightEdge | tudo confere | confere |
| 9 | 196 | `Applebot-Extended`: dois trechos literais; 04/09/2026 | Apple | literais; data confere | confere |
| 10 | 200 | Robôs da Anthropic seguem `robots.txt` e aceitam `Crawl-delay` | Anthropic | confere; "Updated over a week ago" | confere |
| 11 | 105 | `noarchive`/`nocache` não são usados pela Busca do Google | Google, meta tag robots | confere | confere |
| 12 | 143 | Dinheiro, bens ou serviços por links e troca excessiva são spam de links | Google, políticas de spam | os três itens estão na página | confere |

### 2.2 `03b_chatgpt.md` — população de 94 linhas (linhas 36–47 e 118–401, sem a tabela de candidatos 351–358) — **0 falhas em 12**

Quatro das doze primeiras sorteadas não puderam ser conferidas e foram trocadas pelas quatro seguintes da mesma
permutação: **linhas 46, 308 e 41** (as três apoiadas só na ajuda da OpenAI: **não reaberto**, erro 403) e **linha
330** (alegação do Foursquare, que o próprio arquivo dá como "não sei", sem fonte aberta). Entraram 145, 393, 273 e 371.

| # | Linha | Afirmação (resumo) | Fonte reaberta | Existe? Diz aquilo? Data? | Resultado |
|---|---|---|---|---|---|
| 1 | 161 | 87% das citações nos 20 primeiros do Bing; 56% no Google; ~100 consultas com "melhor"/"top"; "direcional" | Seer, 06/02/2025 | tudo confere; país não dito (o guia marca "presumido") | confere |
| 2 | 368 | 2,1 buscas por pergunta (Perplexity 1,4; Grok 6,8); 5 milhões de buscas derivadas; 1–21/04/2026; sem número de perguntas nem país | Peec | tudo confere | confere |
| 3 | 324 | Alimentações Yelp, TripAdvisor e Google Maps; um em cinco registros do Yelp com link de perfil do Google; mapa no modo instantâneo, some no de raciocínio | Resoneo | os três pontos conferem | confere |
| 4 | 142 | Depoimento de abril de 2025: pedido recusado em agosto (sem ano), sem parceria com o Google, anos até busca própria; Bing dado pelo veículo | PYMNTS, 22/04/2025 | confere, com as mesmas cautelas que o guia já escreve | confere |
| 5 | 318 | Localização do aparelho opcional e desligada; teste a ~45 minutos | Search Engine Roundtable, 31/03/2026 | confere | confere |
| 6 | 276 | Relatório AI Performance desde 10/02/2026; métricas; trecho literal | Microsoft | confere | confere |
| 7 | 400 | Search Console inclui a IA no relatório de desempenho; OpenAI sem painel nas fontes abertas | Google, recursos de IA; OpenAI, robôs | confere (a página dos robôs só lista robôs) | confere |
| 8 | 275 | Sitemap como sinal de base; `lastmod` real; somar com IndexNow | Microsoft, 31/07/2025 | confere | confere |
| 9 | 145 | Reddit de ~60% para ~10%; Wikipedia de ~55% para menos de 20%; a Semrush duvida da causa | Semrush, 10/11/2025 | confere, com a frase de dúvida | confere |
| 10 | 393 | "issuing multiple related searches across subtopics and data sources" (Google); ChatGPT também reescreve | Google, recursos de IA; Ahrefs 12/10/2026 | lado Google e Ahrefs conferem; o lado "ajuda da OpenAI" é **não reaberto** | confere no que foi reaberto |
| 11 | 273 | Bing Webmaster Tools gratuito; importa do Search Console; sitemap; verificação diária | Microsoft, 17/06/2025 | os três trechos; "at least once every 24 hours" | confere |
| 12 | 371 | Reddit −88% em seis meses (mar–set/2026); Wikipedia −80%; EUA; 2,4 a 3,8 milhões de respostas por mês | Ahrefs, 12/10/2026 | confere | confere |

### 2.3 Fontes reabertas fora do sorteio (as que sustentam consenso ou regra)

| Fonte | O que conferi | Resultado |
|---|---|---|
| SparkToro/Gumshoe, 28/01/2026 (duas chamadas) | 600 voluntários, 12 perguntas, 2.961 respostas; menos de 1 em 100; "usually at least 60-100X" como conselho do autor; "quantas execuções bastam" e "API × aplicativo" como perguntas em aberto; conflito e "não é revisão por pares" | confere |
| BrightLocal, estudo de 16/09/2026 (duas chamadas) | os números do guia (c) e do 03b | conferem, **menos o enquadramento dos 33%** (achado 1) |
| BrightLocal, diretórios, 26/08/2026 | 60.970 checagens, 1.355 locais, 13 categorias, EUA/Reino Unido/Austrália; Yelp em 80% das respostas do ChatGPT; 99.281 de 162.966 | confere; as 60.970 checagens são das **três** plataformas (achado 13) |
| Resoneo (duas chamadas) | amostra; percentuais por plano e modo; um terço troca; `noindex` no cache; 61–71% × 0–17%; "ao menos metade" no cache; H1 | confere, **menos o denominador do H1** (achado 2) |
| Ahrefs, 12/10/2026 | 66,6 milhões de respostas; 14,4% e a nota de correção; 1,6; 22,9%, 13,1%, 8,9%, 6,8%, 75,9%; 84,4%, 68,3%, 63,4%, 46,4% | confere. A página cita ela mesma os "7,61" de outro estudo (achado 9) |
| Ahrefs Brasil, 23/10/2026 | 6.698.455 palavras-chave; 47,4% e 11,8%; intenções; domínios; sem recorte local; sem clique | confere |
| Ahrefs `llms.txt`, 15/06/2026 | 137.210 domínios; 28%; 97%; 1,1% | confere |
| Ahrefs, citações × 10 primeiros, 02/03/2026 | 37,9%, 31,2%, 31,0%; 863 mil; 4 milhões; 76% em julho de 2025 | confere; a "query fan-out" é **hipótese** da página (achado 7) |
| Pew, 22/07/2025 | 900 adultos; 68.879 buscas; 8% × 15%; 1%; 26% × 16%; 15%; 6% × 2%; 88% | confere |
| Semrush, 15/12/2025 | 33,75% → 31,53%; 6,49%, 24,61%, 15,69%; amostra; sem país | confere |
| Seer, 04/11/2025 | 1,76% → 0,61%; −61% e −41%; 0,70% × 0,52%; 42 clientes; 3.119 termos; 25,1 milhões | confere com a página; a conta da própria página não fecha (achado 14) |
| SparkToro/Similarweb, 09/06/2026 | 0,34%; 68,01% × 60,45%; EUA; "apples and oranges" | confere |
| Whitespark, 12/05/2025 | 540 buscas; 6 ramos; 3 cidades; 15% × 93%; 92% × 6% | confere |
| Peec, listas autopromocionais, 03/03/2026 | 232 mil; 13 mil; 12 semanas; ~11%; sem país; denominador não explícito | confere |
| Tecnoblog, 04/08/2026; MarTech, 28/07/2026 | anúncios no Brasil; acordo com o Yelp | conferem |

---

## 3. Classes, "quem ganha" e "pode estar desatualizada"

- **Tática A sem documentação oficial:** não achei. Observação: a regra da rodada lista como A "Google, OpenAI,
  Microsoft/Bing"; o guia (c) estende A a Perplexity, Apple, Anthropic, `indexnow.org` (linha 17, "do próprio motor
  sobre o próprio produto"). A extensão é declarada e as páginas conferem; fica como decisão do dono aceitar.
- **B sem amostra e método:** não achei B "cheia" sem amostra. Mas o critério de **"B fraca"** está escrito de um jeito
  e aplicado de outro (achado 3).
- **Regra apoiada só em C ou D:** não achei. Na seção 9 do 03b, só as linhas 1, 2, 3 e 8 são "regra" (a 15 é
  requisito de medição), todas com A; o resto está como hipótese, premissa ou decisão do dono.
- **"Quem ganha":** dito em quase tudo. Faltam F12 e F32 no 03b (achado 11).
- **"Pode estar desatualizada":** não achei prática apoiada só em fonte anterior a 2026 sem a marca, nos dois guias.
- **Consensos:** ver achados 3, 5 e 8. Os demais itens de consenso têm A reaberta ou duas B de publicadores diferentes.

## 4. Portão do ChatGPT, ponto a ponto

| Ponto do portão | Onde está no 03b | Fonte primária? | Situação |
|---|---|---|---|
| De onde vem o índice | seção 1 | robô próprio: A (reaberta). Índice próprio: uma B + inferência, dito como "indício forte" | cumpre |
| Papel do Bing | seções 1.2, 1.5 e 4 | Microsoft 2025 (A, reaberta, marcada desatualizada); ajuda da OpenAI (**não reaberto**) | cumpre; dito como disputado |
| Robôs (`OAI-SearchBot`, `GPTBot`, `ChatGPT-User`) | seção 2 | A, reaberta, todos os trechos | cumpre |
| O que o site precisa permitir | seções 2 e 3.1 | A, reaberta | cumpre |
| Dados de empresa local e de mapa | seção 5 | ajuda da OpenAI (**não reaberto**); estudos B de fora do Brasil; Brasil = "não sei" | cumpre |
| Citações em terceiros, avaliações e diretórios | seção 5.3 e "Peso de cada coisa" | diretórios: B; avaliações: "não sei", dito | cumpre |
| Diferença para o Google e os resumos de IA | seção 7 | lado ChatGPT com fonte; lado Google em 4 linhas é "—" e em 3 não tem fonte (achado 12) | cumpre com ressalva |
| Como medir (perguntas, frequência, registro) | seção 8 e roteiro | B para a variação; regra de medição igual nos três arquivos | cumpre |
| Sem fonte primária = "não sei" | seção 3.2 e fecho | `utm_source`, `noindex`, Enterprise/Edu, notas de versão: "não conferido" | cumpre |

## 5. Roteiro

| Pergunta do portão | Resultado |
|---|---|
| São 30 perguntas? | **Sim**: 30 numeradas (linhas 73–102) e 30 linhas na tabela (contagem por script) |
| De morador ou síndico de São Paulo? | **Sim**: morador de apartamento 10, de casa 11, síndico ou síndica 7, morador sem dizer o imóvel 2. Nenhuma de comerciante (as 5 extras estão no apêndice, fora das 30). A pergunta 27 é de quem **vai comprar** o apartamento (achado 16) |
| Praga | 12 valores: baratas 4, ratos 4, cupim 3, escorpião 2, percevejo 2, pulgas 2, formigas 2, pombos 2, mosquito 2, baratas e ratos 1, baratas e formigas 1, geral 5. Soma 30 |
| Bairro | 28 bairros diferentes, todos escritos no texto da pergunta; 2 sem bairro de propósito (12 e 25). Sul 6, leste 6, centro 6, norte 5, oeste 5 |
| Urgência | agora/hoje 9 (2, 6, 9, 16, 18, 19, 23, 24, 26); planejado 21 |
| Planilha com colunas definidas? | **Sim**: 22 colunas descritas; cabeçalho com 22 campos; as duas linhas de exemplo têm 22 campos e estão marcadas como fictícias |
| Frequência e método coerentes entre os três? | **Sim** quanto à regra de medição: o bloco é idêntico, caractere a caractere, nos três (comparado por script). Tempo estimado confere (66 execuções × 2 a 3 minutos). **Não** quanto aos campos a registrar (achado 10) |
| Deixa claro quem roda e que a sessão não abriu o ChatGPT? | **Sim**: título e linha 11 |

## 6. O que não conferiu ou não foi reaberto

1. **Ajuda da OpenAI** (artigo 9237897, nos dois endereços; 12627856; 10093903) e `openai.com/index/…`: erro 403.
   Tudo o que o 03b e o roteiro tiram do "complemento da sessão principal" continua **sem leitura independente**. Os
   artefatos dizem isso com todas as letras.
2. **Diretrizes do Bing e ajuda do Bing Places:** página vazia, como declarado.
3. Divergências achadas: achados 1, 2, 4 e 7 abaixo.

---

## 7. Achados e correção pedida

**Mais importantes**

1. **`03b_chatgpt.md`, linha 326 — número mal enquadrado.** O texto diz "O ChatGPT citou empresas em 33% das buscas
   (29,4% quando a empresa atende em domicílio)". A página mede outra coisa: a taxa de menção **do negócio rastreado**
   ("mention rate of tracked businesses as a percentage of the total number of searches"). Como está, contradiz a
   mesma linha (10% de respostas vazias). O guia (c), linha 167, enquadra certo.
   **Redação certa:** "O ChatGPT mencionou **o negócio rastreado** em 33% das buscas (29,4% quando é empresa que atende
   em domicílio); média de 4,1 empresas por resposta; 10% de respostas sem empresa; …".

2. **`03b_chatgpt.md`, linha 476 — denominador errado.** "o H1 entrou em 83,6% dos trechos, 387 de 463". A página diz:
   "Of the 463 that have an H1, 387 snippets contain it, that is 83.6 %", sobre 534 páginas citadas.
   **Redação certa:** "nas 463 páginas com H1 (de 534 citadas), o H1 entrou no trecho em 387 (83,6%)".

3. **`03_respostas_de_ia.md`, linha 19, e `03b_chatgpt.md`, linhas 64–66 — critério de "B fraca" aplicado de modo
   desigual, e isso alcança três consensos.** A definição diz "falta amostra, **país** ou método: não vira regra" e, no
   03b, "não conta como uma das duas B de um consenso". Mas ficam como B cheia fontes sem país: BrightLocal de
   16/09/2026 (guia (c), linha 166: "Não informa ramos, cidades nem país"), Resoneo (03b, linha 152: "sem recorte por
   país"), Semrush (03b, linha 101), Ahrefs e Seer (guia (c), linhas 226 e 252–255). Pela letra da definição, cairiam
   o consenso 9 do guia (c) (linha 445) e os consensos 7 e 8 do 03b (linhas 546–551).
   **Correção pedida (uma das duas):** (a) reescrever a definição nos dois arquivos — "B fraca = há número, mas falta
   **amostra ou método**; país não declarado é limite anotado ao lado do número e não rebaixa a classe" (é o que a
   regra da rodada pede de uma B); ou (b) manter a definição e rebaixar essas fontes, tirando os três itens do consenso.

4. **`03_respostas_de_ia.md`, linha 158 — mais forte que a fonte.** "Agendamento de serviço local pelo Modo IA estava
   "em breve" em agosto de 2025, só para assinantes nos Estados Unidos". O texto de 21/08/2025 diz que o recurso de
   agente (reserva de restaurante) estava "rolling out for Google AI Ultra subscribers in the U.S." e que ele estava
   "expanding soon to local service appointments and event tickets" — **sem dizer para quem nem onde**.
   **Redação certa:** "Em agosto de 2025 o recurso de agente do Modo IA (reserva de restaurante) saía para assinantes
   do Google AI Ultra nos Estados Unidos; o texto diz que ele seria ampliado "em breve" para agendamento de serviço
   local, sem dizer público nem país."

5. **`03b_chatgpt.md`, linhas 578–581 — três "disputados" com um lado não aberto.** Item 4 (Foursquare: nenhum lado
   aberto; a linha 330 já diz "não sei"), item 5 (JavaScript: o lado "passou a executar" são relatos não abertos; a
   linha 226 já diz "não sei") e item 6 (`noindex`: o lado da OpenAI é "não conferido"). O guia (c), linhas 484–492,
   usa a regra certa: sem os dois lados lidos não há disputa documentada.
   **Correção pedida:** mover os três para "O que não sei", cada um com o lado que foi lido (F25 para o JavaScript em
   2024; F13 para o `noindex` no cache).

**Menores**

6. **`03_respostas_de_ia.md`, linhas 34 e 103.** (a) Linha 34, "desde 31/08/2026 há um controle": a página diz que
   nessa data o controle **chegou a todos os sites**. Redação: "desde 31/08/2026 o controle … está disponível para
   todos os sites". (b) Linha 103, "(Incluir / Excluir; padrão = Incluir)": há uma terceira opção, herdar da
   propriedade-mãe, que é o padrão quando há propriedade-mãe. Acrescentar.

7. **`03_respostas_de_ia.md`, linha 226.** "Explica pela 'query fan-out'": a página levanta como hipótese ("it may be
   that fan out queries are playing a bigger role"). Redação: "levanta a 'query fan-out' como hipótese".

8. **`03_respostas_de_ia.md`, linhas 30, 51–52, 427 e 441 — três generalizações.** (a) Linhas 30 e 427: "texto picado"
   entra na lista do que o Google "não usa"; a fonte diz que **não é exigido** ("There's no requirement"). O "ignora"
   vale para `llms.txt` e marcação "especial". Redação: "o Google ignora `llms.txt` e marcação 'especial' e diz que
   picar o texto não é exigido". (b) Linhas 51–52: "Cada motor separa o robô de busca do robô de treino" não vale para
   a Microsoft, que usa meta tags (o próprio consenso 8 trata o Bing à parte). Redação: "Google, Apple e Anthropic
   separam…; a Microsoft controla por meta tag". (c) Linha 441: a página da Perplexity só diz que o `PerplexityBot`
   não serve a treino; não descreve robô de treino. Tirar a Perplexity da frase "separam" ou dizer isso.

9. **`03b_chatgpt.md`, linhas 373 e 577.** A linha 373 dá "7,61 buscas por pergunta" como "original não localizado, só
   resultado de busca"; a linha 577 usa "mais de 7" citando F17, F18 e F19. A própria F19 relata o número: 7,61, de
   outro estudo, **pela API**, em cerca de 4 mil perguntas, no modelo mais forte. **Correção:** na linha 373, trocar a
   fonte por "relatado em F19; original não aberto; medido pela API, não no aplicativo" e classe C; na linha 577, dizer
   que o "mais de 7" é esse relato.

10. **Roteiro, linhas 187 e 250, contra `03_respostas_de_ia.md`, linhas 411–415 — campos de registro diferentes.** O
    guia (c) pede tipos "site de empresa, perfil no mapa, diretório, avaliação, imprensa, **vídeo, rede social**, órgão
    público", mais "motor" e "se a parceira foi nomeada". A planilha tem `site de empresa`, `diretório`, `mapa`,
    `imprensa`, `fórum`, `governo`, `intermediário`, `outro`; não tem coluna de motor nem de parceira. Como o único
    dado brasileiro aberto põe YouTube e Instagram no topo (guia (c), linha 238), vídeo e rede social cairiam em
    "outro". **Correção pedida:** acrescentar `vídeo`, `rede social` e `avaliação` aos valores de `tipos_de_fonte`
    (linha 187) e ao indicador da linha 250; alinhar a lista do guia (c) com a da planilha; e ou acrescentar a coluna
    `motor`, ou tirar do guia (c), linhas 382–384, a frase de que o roteiro serve também para o Google.

11. **`03b_chatgpt.md`, linhas 84 e 104.** "Quem ganha" está "—" em F12 e F32. Preencher ("veículo de imprensa").
    Linha 81: F9 com "data não lida"; o guia (c), linha 64, diz "sem data na página" (conferi: sem data). Igualar.

12. **`03b_chatgpt.md`, linhas 391, 394–399.** Na tabela da seção 7, o lado Google está "—" em quatro linhas
    (coincidência, proximidade, localização, memória) e sem fonte em três ("um só, do Google"; "perfil de empresa…
    que o dono controla"; "posições mudam, mas há uma lista"). **Correção:** onde está "—", escrever "não levantado
    aqui"; nas três, apontar a seção do guia (a) ou (b) que sustenta.

13. **`03b_chatgpt.md`, linha 325, e roteiro, linha 36.** As "60.970 checagens" são das três plataformas juntas, não
    só do ChatGPT. Acrescentar "(nas três plataformas; a parte do ChatGPT não é dada)".

14. **`03_respostas_de_ia.md`, linha 254.** A página da Seer escreve "−61%", mas 1,76% → 0,61% dá cerca de −65%; e
    usa 2,72% e 2,74% como base do "sem resumo". Acrescentar na observação: "os números da própria página não fecham".

15. **`03_respostas_de_ia.md`, linhas 243–245.** "o equivalente brasileiro medido é o Reclame Aqui" é leitura do
    autor, não frase da fonte. Marcar como inferência.

16. **Roteiro, linhas 99 e 134.** A pergunta 27 é de comprador, classificada como "morador de apartamento". Cabe no
    espírito do portão; se quiser a letra, trocar "Vou comprar" por "Comprei e vou me mudar para".

**Pendência que não é defeito de redação**

17. **Consensos 6 e 9 do `03b_chatgpt.md` (linhas 539–545 e 552)** apoiam-se, na parte A, só na ajuda da OpenAI, que
    nenhum verificador independente conseguiu abrir (403 de novo). O arquivo declara a ressalva. **Ação do dono, 5
    minutos no navegador:** abrir https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt e conferir
    os dez trechos da tabela das linhas 36–47 do 03b.

## 8. Forma

Português nos três; caminhos absolutos em tudo o que o dono abre; números com unidade, período, país (ou "não
informado") e fonte com URL e data de leitura; citações literais curtas; nenhum telefone, nenhum texto de avaliação,
nenhum nome de pessoa física fora de autoria de fonte. Sem promessa de citação ou de posição: os três dizem o
contrário ("Placement is not guaranteed"; "Nunca 'posição'").
