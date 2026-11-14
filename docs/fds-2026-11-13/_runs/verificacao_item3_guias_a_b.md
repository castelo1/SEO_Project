# Verificação independente — item 3, parte 1 de 2: guias (a) e (b)

- **Data e hora** (`TZ=America/Sao_Paulo date`): início em `Fri Nov 13 20:45:12 -03 2026`; gravação deste arquivo em
  `Fri Nov 13 20:57:43 -03 2026`.
- **Quem verifica:** subagente em contexto limpo, que não produziu os artefatos e não recebeu a conclusão de quem os fez.
- **Artefatos conferidos** (lidos inteiros, na versão do commit `343047c`, sem diferença para a árvore de trabalho):
  - `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` — guia (a), 596 linhas
  - `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` — guia (b), 561 linhas
- **Apoio lido:** `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (seção (a) inteira, linhas 42–157, e
  os trechos da seção (b) que o guia (b) cita); `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`
  (inteiro); `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md`;
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`.
- **Ferramentas:** só `WebFetch` (49 chamadas, uma delas com erro e repetida) e leitura local. Nenhum navegador, nenhum
  subagente, nenhuma memória ou plug-in, nenhum formulário, nenhuma conta, nenhum assistente de IA aberto. Não alterei
  nenhum outro arquivo e não fiz commit.
- **Fora do escopo desta parte:** guia (c) e `03b_chatgpt.md` (outro verificador).

## VEREDITO: APROVADO, com correções pendentes

- **Sorteio:** 12 conferidas → **11 OK, 1 FALHA, 0 INCONCLUSIVO** (limite de reprovação: mais de 2 falhas).
- **Seis itens obrigatórios (i)–(vi):** 6 OK.
- **Portão:** cumprido nos dois guias (detalhe na seção 2).
- **Fora do sorteio:** 13 falhas numeradas (F2–F14), nenhuma derruba o portão. **F1, F2, F3 e F5 mudam conteúdo** e devem
  ser corrigidas antes de o item ser dado como fechado; as demais são de precisão e de forma.

---

## 1. O portão, transcrito do `RODADA.md` (linha do item 3, sem reescrever)

> Três guias em `docs/estudo/`: (a) busca orgânica do Google para serviço local; (b) Google Maps e perfil de empresa,
> **dentro do que o item 2 permitiu**; (c) respostas de IA (o que faz um site ser citado). Cada tática com fonte e
> classe A–D. Cada guia termina em "o que é consenso / o que é disputado / o que não sei". Guia (c) curto é resultado
> aceitável **Pedido do dono em 13/11: além do Google, estudar o ranqueamento no ChatGPT.** O guia (c) passa a ter uma
> parte própria, `docs/estudo/03b_chatgpt.md`: como a busca do ChatGPT escolhe e cita fontes para um pedido de serviço
> local (de onde vem o índice, o papel do Bing e dos robôs da OpenAI como `OAI-SearchBot` e `GPTBot`, o que a
> documentação da OpenAI diz que um site precisa permitir, de onde vêm os dados de empresa local e de mapa, como
> citações em terceiros, avaliações e diretórios pesam), o que difere do Google e dos resumos de IA do Google, e como
> medir presença (quais perguntas testar, com que frequência, o que registrar). Fonte primária primeiro (documentação da
> OpenAI e do Bing), depois estudos com dado; relato de praticante e de vendedor de curso só com a classe marcada. A
> sessão **não** abre o ChatGPT nem digita em página: entrega `docs/estudo/03b_chatgpt_roteiro_de_teste.md` com 30
> perguntas reais de um morador ou síndico de São Paulo (por praga, bairro, urgência) e a planilha de registro, para o
> dono rodar na conta dele; o desenho do item 6 e o protótipo do item 7 trazem o que o estudo indicar (por exemplo
> `robots.txt`, dados estruturados, página "quem somos" verificável).

Regra de evidência aplicada (mesmo arquivo): classes A–D; "Consenso" exige classe A ou duas fontes B independentes;
fonte anterior a 2025 leva "pode estar desatualizada"; número de outro país entra com o país e não é convertido; anotar
quem ganha com a afirmação.

## 2. Conferência do portão (ponto 1)

| Exigência do portão | Guia (a) | Guia (b) |
|---|---|---|
| Cada tática com fonte e classe A–D | **Cumprido.** Seções 2, 4 e 5 declaram a classe no cabeçalho da seção (A); as demais têm coluna de classe. Duas linhas sem classe são avisos, não táticas (linhas 337 e 338). Ressalvas: classes compostas ("C com ressalva (quase D)", "C/D", "B com ressalva forte (quase D)") onde a regra pede **uma** classe — ver F8 | **Cumprido.** Tabelas 1.1 e 1.2 declaram a classe no cabeçalho; as demais têm coluna. Linhas 290 e 346 estão sem classe, mas marcadas "inferência". O guia cria a marca "B fraco" (declarada na legenda, mais restritiva que B: não infla) e usa "C/D" em oito linhas |
| Termina em "consenso / disputado / não sei" | **Cumprido** (seção 11, linhas 437–498). Depois dela há dois apêndices de fontes (seções 12 e 13) | **Cumprido** (linhas 480–543). Depois há o apêndice de fontes não abertas |
| Guia (b) dentro do item 2 | não se aplica | **Cumprido.** Toda coluna "o que fazer" é "no perfil da licenciada"; a seção 10.2 e a seção "O que não cabe para um gerador de leads" repetem as vedações do item 2 (perfil próprio, fachada, avaliação incentivada, telefone, WhatsApp ou site do intermediário, perfil "alugado", promessa de posição). Não achei nenhuma tática que dependa de algo vedado |

**Trechos do guia (b) que não escapam do limite, mas encostam nele e precisam de ressalva** (viraram F7):

1. Linha 155, observação: cita sem ressalva "Different Business Profiles can use the same WhatsApp link." (a frase
   existe na página). Lida sozinha, sugere um mesmo WhatsApp — o do intermediário — em vários perfis de parceiras, o que
   o item 2 veda (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 27 e 78–85). A coluna de
   ação da linha 142 diz "o link de WhatsApp **dela**", então a conduta está certa; falta a ressalva junto da citação.
2. Linha 217, observação: repassa a afirmação da agência de que premiar **funcionários** por avaliações "a política não
   veda expressamente". A política lida hoje (https://support.google.com/contributionpolicy/answer/7400114?hl=en, 2
   leituras) lista entre o que **não** é permitido ao comerciante: pedir que a equipe solicite "a certain number of
   reviews" e pedir que a equipe solicite avaliações "that include specific content, including content that identifies
   a staff member". O programa descrito no artigo sorteava prêmio para o funcionário citado na avaliação. Não é tática
   recomendada pelo guia, mas a frase fica como porta aberta e contradiz a fonte A que o próprio guia usa.

## 3. Método do sorteio (ponto 2)

- **Universo:** linhas de tabela de dados (uma afirmação por linha) das seções de conteúdo, excluídas as tabelas de
  conferência do exemplo do owner, as de "consenso/disputado", as de passos (seção 10 do guia (b), que repete as
  anteriores) e a tabela "fator por fator" do guia (b) (linhas compostas). Linhas de classe C ou D ficaram fora do
  universo, porque o pedido é misturar A e B.
  - Guia (a), classe A: linhas 63–74, 82–89, 156–173, 209–220, 246–262, 273–283, 293–297, 333–336, 358–365, 381–384
    (99 linhas). Classe B: linhas 303–306, 339–345, 385 (12 linhas).
  - Guia (b), classe A: linhas 110–117, 130–146, 152, 154, 155, 168–174, 188–194, 213, 309–314, 340–345, 354–357,
    375–377 (62 linhas). Classe B (inclui "B fraco"): linhas 200–206, 214, 215, 246–252, 316, 358–360, 379, 380 (22 linhas).
- **Estratos:** 4 de classe A + 2 de classe B em cada guia (6 + 6 = 12).
- **Comando:** `shuf -n <k> --random-source=<(openssl enc -aes-256-ctr -pass pass:"<semente>" -nosalt </dev/zero)`,
  com a semente `verificacao_item3_guias_a_b_2026-11-13_20:45` seguida de `-aA`, `-aB`, `-bA`, `-bB` (reproduzível).
- **Resultado:** guia (a): linhas 72, 161, 168, 360 (A) e 344, 345 (B). Guia (b): linhas 114, 154, 354, 377 (A) e 204,
  359 (B).
- **Obrigatórios (i)–(vi):** conferidos à parte (seção 5), porque nenhum saiu no sorteio; não entram na contagem de 12.
- **Regra de leitura:** para citação entre aspas pedi o trecho literal e perguntei "a página contém exatamente a
  frase X?"; só declarei FALHA depois de duas chamadas à mesma página.

## 4. As 12 conferências do sorteio

| # | Afirmação (resumo) | Arquivo e linha | URL aberta | O que a fonte devolveu | Classe conferida | Resultado |
|---|---|---|---|---|---|---|
| 1 | Camada 2, políticas de spam: o que leva a posição mais baixa ou à remoção | guia (a), linha 72 | https://developers.google.com/search/docs/essentials/spam-policies e https://developers.google.com/search/docs/essentials | A página "essentials" diz que as políticas detalham comportamentos que levam a página ou o site a "being ranked lower or completely omitted"; a de spam traz "Sites that violate our policies may rank lower in results or not appear in results at all." Sem data nas duas | A, correta | **OK** |
| 2 | Conteúdo em escala: "creating large amounts of unoriginal content that provides little to no value to users, no matter how it's created." | guia (a), linha 161 | https://developers.google.com/search/docs/essentials/spam-policies | Frase exata presente (resposta "sim" à pergunta literal) | A, correta | **OK** |
| 3 | Reputação de site: "The site reputation policy applies where third-party content is published on a host site mainly" por causa dos sinais do hospedeiro | guia (a), linha 168 | idem | Frase exata presente; continua com "because of that host's already-established ranking signals" | A, correta | **OK** |
| 4 | Search Console: impressão conta mesmo sem rolar (carrossel e lista infinita exigem rolar); links do mesmo bloco têm a mesma posição; resumo de IA ocupa uma posição; a página não diz como conta o bloco do mapa | guia (a), linha 360 | https://support.google.com/webmasters/answer/7042828?hl=en | 1ª chamada: erro da ferramenta. 2ª: "whether or not the item is scrolled into view"; carrossel "must be scrolled into view"; "all links in the element occupy the same position"; "An AI Overview occupies a single position"; nada sobre bloco local | A, correta | **OK** |
| 5 | "de cada 1.000 buscas no Google, **374** cliques vão para a web aberta **nos Estados Unidos** e **360 na União Europeia**" (SparkToro, 02/07/2024) | guia (a), linha 344 | https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/ | Duas chamadas, mesma resposta: o título exibido é "For every 1,000 **EU** Google Searches, only 374 clicks go to the Open Web. In the **US**, it's 360."; no corpo, "In the EU, for every 1,000 Google searches, 374 clicks go to the open web." e "for every 1,000 searches on Google in the United States, 360 clicks". Data 02/07/2024 e dados da Datos (Semrush): conferem. **Os países estão trocados no guia** (o guia seguiu o endereço da página, que guarda o título antigo) | B com "pode estar desatualizada": correta | **FALHA** |
| 6 | Estudo antigo de cliques em busca de serviço: orgânico ~44% a 51%, bloco local ~29% a 32%; São Francisco; escolha declarada; 19/10/2018 | guia (a), linha 345 | https://www.brightlocal.com/research/local-services-ads-click-study/ | 19/10/2018; São Francisco; 5.500 participantes; escolha declarada; orgânico 43,9% (com anúncio de serviço local) e 50,8% (sem); bloco local 28,8% e 32,3% | B, antiga e marcada: correta | **OK** |
| 7 | "More reviews and positive ratings can help your business's local ranking." | guia (b), linha 114 | https://support.google.com/business/answer/7091?hl=en | Frase presente no parágrafo "Prominence" (a página usa apóstrofo curvo; texto idêntico) | A, correta | **OK** |
| 8 | "Ask Maps starts rolling out now in the U.S. and India on Android and iOS, with desktop coming soon." (12/03/2026) | guia (b), linha 154 | https://blog.google/products-and-platforms/products/maps/ask-maps-immersive-navigation/ | Frase exata presente; data 12/03/2026; usa dados de lugares e avaliações; Brasil e Austrália não constam do texto | A, correta | **OK** |
| 9 | Em 2025: mais de 292 milhões de avaliações bloqueadas ou removidas, mais de 13 milhões de perfis falsos, 79 milhões de edições, mais de 782 mil contas (16/04/2026) | guia (b), linha 354 | https://blog.google/products-and-platforms/products/maps/new-ways-were-protecting-businesses-on-maps/ | Os quatro números, o ano e a data conferem. **Ressalva:** a observação da linha diz "Números mundiais"; em duas leituras o texto não informa a abrangência geográfica dos números (ver F9) | A, correta | **OK** (com ressalva) |
| 10 | O painel de desempenho não mostra posição (A por ausência) | guia (b), linha 377 | https://support.google.com/business/answer/9918094?hl=en | A lista de métricas (interações, buscas, visualizações, rotas, ligações, cliques no site, mensagens, reservas) não tem posição; a palavra "ranking" só aparece num link para as dicas de classificação; sem período máximo | "A (por ausência)": aceitável e declarada | **OK** |
| 11 | 89% esperam resposta do dono; 80% preferem empresa que responde a todas (EUA, 11/02/2026) | guia (b), linha 204 | https://www.brightlocal.com/research/local-consumer-review-survey/ | 11/02/2026; 1.002 adultos dos EUA, SurveyMonkey; "89% of consumers expect business owners to respond to reviews"; "80% ... likely to use a business that responds to all of its reviews" ("preferem" é paráfrase próxima de "likely to use") | B, correta; é pesquisa de comportamento **declarado** (ver ponto 3) | **OK** |
| 12 | Nomes com palavra-chave indevida corrigidos pelo Google: de 0,15% a 17,3% dos perfis, por setor (11/04/2022) | guia (b), linha 359 | https://www.sterlingsky.ca/google-maps-spam-study/ | 11/04/2022; menor 0,15% (portão de garagem, 1 de 676), maior 17,27% (restauração capilar, 43 de 249); só conta o que o Google corrigiu; sem controle de pragas | "B fraco": correta e conservadora | **OK** |

**Contagem: 11 OK · 1 FALHA · 0 INCONCLUSIVO.**

## 5. Itens obrigatórios (i)–(vi), conferidos à parte

| Item | Afirmação | Arquivo e linha | URL | O que a fonte devolveu | Resultado |
|---|---|---|---|---|---|
| (i) | Páginas de entrada com o exemplo de regiões e cidades | guia (a), linhas 156–158 e 163 | https://developers.google.com/search/docs/essentials/spam-policies | Presentes, literais: "Doorway abuse is when sites or pages are created to rank for specific, similar search queries."; "Having multiple domain names or pages targeted at specific regions or cities that funnel users to one page"; "Creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy"; "Blocks of text that list cities and regions that a web page is trying to rank for" | **OK** |
| (ii) | Resultado rico de FAQ deixou de aparecer em 07/05/2026; aviso em 08/05/2026; documentação removida em 15/06/2026 | guia (a), linhas 133 e 281 | https://developers.google.com/search/updates | Entrada de 8 de maio de 2026: "This feature will no longer appear in Google Search starting May 7, 2026."; entrada de 15 de junho de 2026: "Removed documentation for the FAQ rich result feature." | **OK** |
| (iii) | Ahrefs: 1,74% de 1 milhão de páginas nos dez primeiros em um ano; correlação 0,33 em buscas locais | guia (a), linhas 303 e 306 | https://ahrefs.com/blog/how-long-does-it-take-to-rank/ e https://ahrefs.com/blog/links-matter-less-but-still-matter/ | 15/05/2025: "Only 1.74% of them did" (1 milhão de endereços vistos em setembro de 2023); 6,11%; 40,82%; 72,9%; 13,7%; 5 anos; 2017: 5,7%, 59%, 22%, 2 anos. 30/01/2025: 1.000.000 de palavras-chave dos EUA, Spearman, 0,255 / 0,248 / 0,131 / 0,117 / 0,034; "Links and RDs correlated at .33 for local queries". Todos conferem. Ressalva sobre o país da amostra do 1,74% em F10 | **OK** |
| (iv) | Frase da ajuda sobre relevância, distância e destaque | guia (b), linhas 110–115 | https://support.google.com/business/answer/7091?hl=en | As seis citações das linhas 110–115 estão na página, literais. A página também tem a frase "Local results are mainly based on relevance, distance, and popularity.", que o guia (b) não registra (ver F6) | **OK** |
| (v) | API de perguntas e respostas descontinuada em 03/11/2025; chat encerrado em 31/07/2024 | guia (b), linhas 141, 152 e 155 | https://developers.google.com/my-business/content/qanda/change-log e https://support.google.com/business/answer/14919056?hl=en | "The My Business Q&A API was discontinued on November 3, 2025."; aviso de 15/09/2025; sem substituta. "As of July 31, 2024, the chat and call history features are no longer available in your Business Profile." | **OK** |
| (vi) | Local Services Ads: a lista de termos para prestadores não inclui o Brasil | guia (b), linha 344 | https://support.google.com/localservices/answer/7501778?hl=en | Página "Google Local Services Ads Additional Terms for Providers": EUA, Canadá, Áustria, Bélgica, França, Alemanha, Irlanda, Itália, Países Baixos, Espanha, Suíça, Reino Unido. Brasil ausente. Termos dos EUA com "2026-08" no endereço. A página não afirma indisponibilidade no Brasil — o guia diz exatamente isso ("A (por ausência)") | **OK** |

## 6. Outras conferências na fonte, fora do sorteio (usadas nos pontos 3 a 6)

Todas por `WebFetch`, uma leitura, salvo indicação. Resultado: confere com o guia, salvo o que virou falha numerada.

- Painel de atualizações (https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history): as 12 datas e durações
  da tabela das linhas 100–113 do guia (a) conferem, inclusive a atualização central de 10/11/2026 com "Information".
- Registro de mudanças (https://developers.google.com/search/updates): entradas de 13/04, 14/04, 23/04, 15/05, 05/06,
  24/07, 28/08, 18/09, 01/10 e 23/10/2026 existem com o assunto que o guia (a) dá. A de 08/09/2026 é sobre "diferenças
  regionais" (cita as unidades de agregador como exemplo).
- https://developers.google.com/search/docs/appearance/core-updates: "Deleting content is a last resort, and only to be
  considered if you think the content can't be salvaged."; "We recommend waiting at least a full week after a core
  update completes"; atualizações menores não anunciadas. Confere.
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable: as quatro citações das linhas 251, 252
  e 293 do guia (a) estão na página.
- https://developers.google.com/search/docs/fundamentals/third-party-seo: "Third-party tools don't have access to our
  internal ranking data."; recomendação forte do Search Console. Confere.
- https://developers.google.com/search/docs/appearance/structured-data/review-snippet: regra de autopromoção e "Don't
  aggregate reviews or ratings from other websites." presentes; a regra de avaliações falsas ou incentivadas sem aviso
  está na página e a data de 24/07/2026 está no registro de mudanças. Confere.
- https://developers.google.com/search/docs/appearance/structured-data/local-business: `name` e `address` obrigatórios;
  "any page on your site"; sem `areaServed`; ver F11 para a citação.
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls: só trata de conteúdo duplicado
  ou muito parecido em endereços diferentes (ver F3).
- https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/:
  900 adultos dos EUA, 68.879 buscas, março de 2025, 8% × 15%, 1%. Confere.
- https://www.nearmedia.co/eu-home-services-search-behavior/: 20/11/2024; Alemanha, França, Irlanda; 300 pessoas; 78%,
  42%, 8 em 10, 1 em 10, 73%. Confere.
- https://firstpagesage.com/reports/google-click-through-rates-ctrs-by-ranking-position/: 22/09/2026; "1,184 client and
  panel domains"; 7,1% / 22,6% / 3,6%; 14,8% / 12,6% / 11,9%. Números conferem; classe em F8.
- https://support.google.com/business/answer/7249669?hl=en, `/3370250`, `/3038177`, `/9157481`, `/7163406`, `/15013580`
  e https://support.google.com/localservices/answer/7549288?hl=en: todas as citações que o guia (b) põe entre aspas e
  que testei estão nas páginas (categoria afeta a classificação; até 9 categorias adicionais, na página da planilha de
  envio em massa; "Choose the fewest number of categories…"; nome; horário; um perfil; 20 áreas; cerca de 2 horas; sem
  raio; terceiro não promete posição; WhatsApp ou SMS; selo único e 07/12/2025).
- https://support.google.com/contributionpolicy/answer/7400114?hl=en (2 leituras): a frase completa é "Solicit or
  encourage the posting of content that does represent a genuine experience, without offering incentives to do so or
  attempting to influence the rating or the contents of the review." Confere; ver F7 para o que o guia não trouxe.
- https://whitespark.ca/local-search-ranking-factors/ (primeiros 100 mil caracteres): 06/11/2025; 47 especialistas
  convidados; 187 fatores; os dez primeiros na ordem do guia; 152º, 148º, 171º, 22º; a frase sobre endereço oculto.
  Confere.
- https://rankings.io/proximity-data-study: 30/06/2021; EUA; 56%; −8 posições na primeira milha (−5 a −12); 27% a 92%;
  80% em Nova York; "20+" gravado como 25. Confere. O estudo **não** afirma que a proximidade é o fator principal (F2).
- https://searchatlas.com/research/beyond-proximity-a-feature-level-correlation-analysis-of-google-business-profile-rankings/:
  21/08/2025; 3.269; 55,2% e 36,2%; 19,2% e 26%; 5,3% e 22,8%; 5,9%; país não informado; dados não publicados; números
  divergentes entre seções. Confere com o guia, que já anota essas fraquezas.
- https://www.brightlocal.com/research/vicinity-gbp-spam-impact/ e
  https://brightlocal.com/research/study-business-opening-hours-and-local-rankings/: 01/03/2022, 391 perfis dos EUA
  (85 / 149 / 157), inclui controle de pragas, −7,9 / −5,5 / +4,1; 21/12/2023, 50 unidades, 10 categorias, três dias,
  grade 7 × 7 a 500 m, 2,4 posições (lanchonetes). Confere.
- https://www.sterlingsky.ca/google-review-recency-ranking/: data exibida 28/07/2025; um cliente; programa de sorteio de
  prêmio para funcionário citado na avaliação. Confere com a descrição; ver F7.

## 7. Classe de evidência nos dois guias inteiros (ponto 3)

| O que procurei | Achado |
|---|---|
| Fonte D ou C como base de regra ou em "consenso" | Guia (a): não achei; a lista de consenso (linhas 441–461) é toda classe A e as duas afirmações com uma só fonte B ficaram, corretamente, em "quase consenso" (linhas 463–467). Guia (b): os itens 1–8 e 10–15 do consenso são classe A; **o item 9 não é** (F2). A pesquisa de opinião aparece sempre como "D (opinião)" e nunca sustenta a coluna de ação |
| "Consenso" que não seja A nem duas B independentes | Guia (b), linha 496 (item 9) — F2. Itens 7, 13 e 14 são "A por ausência", o que o guia declara; aceitável, mas é silêncio da fonte, não afirmação dela |
| Estudo de vendedor sem "quem ganha" | Não achei. O guia (a) tem a coluna em todas as tabelas de estudo; o guia (b) tem a lista "Quem ganha, por fonte" (linhas 43–56) e a coluna nas tabelas. Exceção menor: guia (a), linha 321, "quem ganha" em branco |
| Fonte anterior a 2025 sem "pode estar desatualizada" | F12 |
| Número de outro país sem o país ou convertido | Nenhum número convertido para o Brasil. País ausente ou atribuído sem base: F10. O guia (b), linha 72, tira de estudo dos EUA uma conclusão sobre São Paulo sem a marca de inferência (F2) |
| Pesquisa de opinião tratada como dado medido | Whitespark: não (sempre "D (opinião)"). BrightLocal 2026 (linhas 200–206 do guia (b)): é pesquisa de comportamento **declarado** por 1.002 consumidores, classificada B; o guia a relata no indicativo ("97% leem", "68% só usam"). Sugestão: "dizem ler", "dizem só usar". Não conto como falha |
| Classe das 12 sorteadas | As 12 classes conferem (coluna "Classe conferida" da seção 4) |

## 8. Afirmação sem fonte e recomendação além da fonte (ponto 4)

Reunidas em F13 (lista completa lá). Bem feito e conferido: as inferências principais estão marcadas — guia (a), seção
2.2 ("inferência minha"), YMYL (linhas 222–229), `LocalBusiness` próprio (linha 276), analogia de afiliação (linha 170),
prazo "premissa, não promessa" (linha 389); guia (b), "Consequência para São Paulo" ("inferência, não medida aqui",
linha 325), art. 22 aplicado ao perfil ("leitura minha, não parecer", linhas 411 e 432), selo do Google (linha 346).

## 9. Conferência do exemplo do owner (ponto 5): seis táticas

| Tática (`00x_metodo_do_exemplo_x.md`) | Veredito do guia | Fonte que o guia cita | O veredito decorre da fonte? |
|---|---|---|---|
| 2.6 — página em que só muda a cidade é página de entrada | guia (a), linha 413: "Confirmada. Subiu para A" | política de spam | **Sim.** O exemplo de regiões e cidades é literal |
| 2.5 — um H1, dados estruturados coerentes, cinco links internos | guia (a), linha 412: "Princípios confirmados, número contrariado" | links rastreáveis; guia de iniciantes | **Sim.** "There's no magical ideal number of links a given page should contain." e "at least one other page" estão na página. "Contrariado" é um pouco forte; "sem base" (que o guia também escreve) é o termo exato |
| 2.1 — uma palavra-chave, uma página | guia (a), linha 408: "Confirmada no princípio", classe A | canonização; diversidade de sites | **Não** (F3). A página de canonização trata de conteúdo duplicado em endereços diferentes e não fala de busca nem de duas páginas disputando o mesmo termo; a regra de diversidade diz que em geral até **duas** páginas do mesmo site aparecem, o que não é "uma" |
| 2.10 — cortar páginas sem clique | guia (a), linha 417: "Em parte contrariada" | atualizações centrais | **Sim.** "Deleting content is a last resort…" |
| 2.15 — pedir ao cliente que cite o serviço na avaliação | guia (b), linha 468: "Contrariada pela política (A), na minha leitura" | 7400114 | **Sim, e com mais força do que o guia diz:** além de "attempting to influence the rating or the contents of the review", a página veda pedir à equipe avaliações "that include specific content" |
| 2.14 — até 10 categorias, 20–40 serviços, 20 fotos, postagem semanal | guia (b), linha 467: parte confirmada, parte contrariada, números D | 3370250, 3038177, estudos | **Sim.** "up to 9 additional categories" e "Choose the fewest number of categories…" conferem; os números do autor não têm fonte |
| 2.12 — três fatores do mapa | guia (b), linha 465: fatores confirmados por A; "três perfis" não conferido | 7091 | **Sim**, com a ressalva de F6 |

Cinco de seis decorrem da fonte (2.12 conta como sétima, extra). Uma não decorre (F3).

## 10. Coerência entre os guias e com `00_restricoes.md` (ponto 6)

| Tema | Guia (a) | Guia (b) | `00_restricoes.md` | Conclusão |
|---|---|---|---|---|
| Destaque (prominence) | linha 335: relevância, distância e destaque, "o Google hoje escreve também 'popularidade'"; links e avaliações contam; não há a frase sobre posição na web | linhas 110–122 e 484: relevância, distância e destaque; mesma lista de ausências; **não menciona "popularity"** | — | Sem contradição; **omissão no guia (b)** (F6) |
| Medir posição | linhas 53, 172 e 365: raspar o resultado para checar posição é prática vedada (classe A); "não montar robô de posição" | linhas 96, 378 e 417: posição "só se mede com grade de ferramenta paga"; passo 15 recomenda a grade se a licenciada contratar | — | **Tensão não tratada** (F5): a grade é consulta automática de posição |
| `LocalBusiness` | linhas 276–277: não marcar o site do projeto; de terceiros, não conclusivo e só com autorização | linhas 289–290: no site da licenciada | linhas 117–119 | Coerente |
| Avaliações | linhas 278–279: sem estrelas próprias; não agregar avaliações de outros sites; regra de dados estruturados veda avaliação incentivada **sem aviso** | linhas 188–191: no Google, incentivo é vedado **sempre** | linhas 29 e 95–98: vedado | Coerente (são regras de produtos diferentes). Convém uma linha no guia (a) dizendo que a regra do perfil é mais dura, para a linha 279 não ser lida como "incentivo com aviso pode" |
| Site e telefone no perfil | linha 335: o site do intermediário não entra no mapa | linhas 286 e 428: só os da licenciada | linhas 78–85 e 117–119 | Coerente |
| Ponteiros de linha | — | cerca de 25 remissões a "linhas N–M" | arquivo mudou depois (correções F1–F8 do item 2) | **Ponteiros vencidos** (F4) |
| Endereço em propaganda | — | linha 290: "por prudência, na propaganda" | linhas 235–236: "Por prudência, sem base conferida na fonte" | Coerente no conteúdo; a linha citada (189–191) hoje aponta para outro texto (F4) |

## 11. Forma (ponto 7)

- **Português:** sim. O guia (a) traduz toda citação em inglês; o **guia (b) deixa cerca de 28 linhas com citação em
  inglês sem tradução** (por exemplo linhas 77, 94, 130, 168, 310, 313, 340). Ver F14.
- **Caminhos absolutos:** sim nos dois; nenhum caminho relativo de arquivo do projeto (busca por `docs/`, `research/`,
  `data/` sem `/home/ancastelo` não achou nada).
- **Nome de pessoa física do mercado local:** nenhum. Os únicos nomes de pessoa são de autores de fonte (guia (a),
  linhas 319–320), o que é permitido. O guia (b) não nomeia ninguém.
- **"Quem aparece" tirado de ferramenta de busca:** nenhum. Os dois guias dizem que isso é do item 4 (guia (a), linhas
  13 e 338; guia (b), linhas 20–21 e 363–367). O que foi visto só em resultado de busca está marcado "não aberto" e não
  é usado como evidência (guia (a), linhas 520–523; guia (b), linhas 361 e 558).
- **Números com unidade, período, país e fonte:** sim, salvo F9 e F10.
- **Citação longa:** não há; as citações são trechos curtos de política.
- **"Não é parecer jurídico":** declarado nos dois (guia (a), linha 14; guia (b), linha 22).

## 12. Falhas numeradas e correção sugerida

**F1 — FALHA do sorteio. Países trocados no estudo de buscas sem clique.** Guia (a), linha 344: escreve 374 para os
Estados Unidos e 360 para a União Europeia. A página diz o contrário (374 na União Europeia, 360 nos Estados Unidos),
no título exibido e no corpo, em duas leituras. A própria linha avisava que o resumo da ferramenta "trocava os países";
o guia ficou com a versão do endereço da página, que guarda o título antigo. *Correção:* "360 cliques nos Estados Unidos
e 374 na União Europeia"; trocar a nota final por "o endereço da página traz os países invertidos; vale o título
exibido e o corpo".

**F2 — "Consenso" e regra de resumo sem a evidência exigida (distância).** Guia (b), linha 496 (consenso, item 9: "A
distância pesa muito e a posição cai depressa") e linha 72 ("[A + B] … é o fator que mais pesa"; "**Uma base não cobre
São Paulo inteira.**"), repetido na linha 474. A ajuda do Google lista os três fatores sem ordená-los; o estudo B
(rankings.io, EUA, 2021, advogados, uma busca, "pode estar desatualizada") mede a queda com a distância e **não** compara
fatores; quem põe a distância em primeiro é só o modelo da Search Atlas ("B fraco", que pela legenda do próprio guia é
"só indício", e cuja limitação declarada é superestimar a distância); a opinião da Whitespark a põe em 2º. Não há
classe A nem duas B independentes para "o que mais pesa" nem para o tamanho da queda. *Correção:* tirar o item 9 do
consenso (o fator em si já está no item 1) e levá-lo a "disputado" ou a uma linha "indício: um estudo B dos EUA de
2021 e um B fraco"; na linha 72, trocar por "é um dos três fatores (A) e o gestor não o controla; um estudo dos EUA de
2021 mede queda forte na primeira milha (B, pode estar desatualizada)" e marcar "Uma base não cobre São Paulo inteira"
como inferência, como a seção 6 já faz (linha 325); ajustar a linha 474.

**F3 — Veredito do exemplo do owner que não decorre da fonte.** Guia (a), linha 408 (tática 2.1, "Confirmada no
princípio", classe A) e linha 255 ("nunca duas páginas para a mesma busca (ex.: 'dedetização Pinheiros' e 'dedetizadora
Pinheiros' são uma página só)"). A página de canonização só trata de conteúdo duplicado em endereços diferentes; a
regra de diversidade admite duas páginas do mesmo site. *Correção:* veredito "não confirmada como regra do Google;
prática de mercado (D) com apoio indireto de A (páginas muito parecidas são agrupadas)"; na linha 255, marcar a
recomendação como inferência.

**F4 — Ponteiros de linha vencidos para o item 2.** Guia (b): as remissões a "linhas N–M" de
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (linhas 13, 15, 17, 172–174, 183, 191, 271, 273,
286, 287, 290, 314, 356, 393, 411, 426, 428, 429, 431–433, 443–449, 465) apontam para a versão do commit `08e541d`.
Os ponteiros para o anexo `00a_perfil_google.md` (linhas 61 e 149) estão certos. Depois das
correções do item 2 o texto desceu: seção (a), +3 linhas até a linha 120 e +5 depois; seção (b), +9 ou mais. Exemplos
no arquivo atual: avaliações estão em 95–100 (o guia diz 92–97); promessa de posição em 126–128 (diz 121–123);
ocultar endereço em 72–73 (diz 69); telefone e site em 78–80 e 117–119 (diz 75–77 e 114–116, que hoje são o nome e a
propriedade do perfil); "não é caminho" em 133–134 (diz 128–129); art. 22 da RDC em 185–193 (diz 176–183); "por
prudência" em 235–236 (diz 189–191, que hoje são os incisos I e II do art. 22). *Correção:* refazer os ponteiros ou
citar pelo título da subseção, que não se desloca.

**F5 — Tensão entre os guias sobre medir posição.** Guia (a), linhas 53, 172 e 365: enviar buscas automáticas e
"scraping results for rank-checking purposes" sem permissão é prática vedada (conferi o texto: "Such activities violate
our spam policies and the Google Terms of Service"). Guia (b), linhas 96, 378, 417 e 466: recomenda, sob condição, a
grade de posição de ferramenta paga, que é consulta automática de posição, sem citar essa política nem dizer como a
ferramenta obtém os dados. *Correção:* acrescentar a ressalva no guia (b), seção 9 e passo 15 ("a política de spam do
Google veda consulta automática de posição sem permissão; como cada ferramenta de grade obtém o dado: não sei; decisão
e risco são da licenciada"), ou rebaixar a grade para "não sei se é compatível".

**F6 — Omissão no guia (b) sobre a página que ele mais usa.** A página 7091 traz, em duas leituras minhas, "Local
results are mainly based on relevance, distance, and popularity." O guia (a) registra isso (linha 335); o guia (b), que
declara três leituras e lista "o que a página não diz" (linhas 119–122), não. *Correção:* acrescentar à tabela 1.1 e ao
item 1 do consenso que a frase-resumo usa "popularity" e o título da seção usa "Prominence".

**F7 — Dois trechos do guia (b) que encostam no limite do item 2 sem ressalva.** (a) Linha 217: repassa "premiar
funcionários… a política não veda expressamente", contra os itens da política que vedam pedir à equipe um número de
avaliações ou avaliações com conteúdo específico, "including content that identifies a staff member". (b) Linha 155:
"Different Business Profiles can use the same WhatsApp link." sem dizer que o link tem de ser o da própria empresa.
*Correção:* (a) acrescentar a citação da política e "não adotar"; incluir esses dois itens na seção 3.1 e no passo 12;
(b) acrescentar "isso não autoriza pôr o WhatsApp do intermediário em perfis de parceiras (item 2)".

**F8 — Classe inflada.** Guia (a), linha 341: First Page Sage é agência de SEO, a amostra são clientes e painel
próprios e o guia mesmo escreve "método pouco exposto"; pela regra da rodada isso é D, não "B com ressalva forte".
Também está na lista "Estudos com dado (classe B)" (linha 581) e sustenta a metade "B" da regra 14 do resumo (linha 52).
*Correção:* classificar como D ("alegação") e, na linha 52, apoiar a parte B só nas fontes B. Em geral, trocar as
classes compostas ("C/D", "quase D") por uma classe só.

**F9 — Abrangência não informada pela fonte.** Guia (b), linha 354 ("**Números mundiais**") e linha 505 ("no mundo"):
o texto do Google não diz a que países os números de 2025 se referem (duas leituras). *Correção:* "a fonte não informa
a abrangência geográfica; presumo que sejam globais".

**F10 — País atribuído sem base.** Guia (a), linhas 51 e 385: "estudo dos Estados Unidos" para o 1,74%. A página só
declara "(in the US)" para a amostra de 1,3 milhão de palavras-chave (idade das páginas); para o 1 milhão de endereços
do 1,74% não informa país, e para os 2 milhões só o idioma (inglês). A ficha da linha 306 está certa. *Correção:*
"país da amostra não informado (palavras-chave da parte de idade: Estados Unidos)".

**F11 — Citação e detalhe imprecisos, sem efeito na conclusão.** (a) Guia (a), linha 277: a frase da página é "This
property is only **recommended** for sites that capture reviews about other local businesses."; o trecho entre aspas
omite "recommended". (b) Guia (a), linhas 138 e 283: dizem que as unidades de agregador existem no Espaço Econômico
Europeu, na Turquia e na África do Sul; na minha leitura (uma só) a página lista essas unidades só para o Espaço
Econômico Europeu e outros recursos para a Turquia. A conclusão "não existe no Brasil" se mantém. *Correção:* ajustar a
citação; reler a página de diferenças regionais e corrigir a lista de regiões.

**F12 — Fonte anterior a 2025 sem "pode estar desatualizada".** Guia (b): linha 267 (Sterling Sky, 15/09/2023, D);
linha 272 (Search Engine Roundtable, 16/05/2024, C); linha 217 (caso de cerca de 2022); linha 254 (teste de cerca de
2023); linha 256 (testes de 2019 e 2022); e as duas vezes em que o estudo de horário de 2023 vira frase de resumo sem
a marca (linha 83, "melhora a posição"; linha 408, "Afeta a posição na hora da busca"). Guia (a): linha 321 (The
Register, 29/05/2024). Nenhuma delas sustenta regra. *Correção:* acrescentar a marca.

**F13 — Afirmação sem fonte ou recomendação além da fonte, sem marca de inferência.**
- Guia (a), linha 52 (regra 14, classe "A (o mecanismo)"): "mapa e anúncios ficam acima do orgânico" — a fonte A só diz
  que os recursos da página mudam com a busca (o próprio guia admite na linha 334). Isso é observação do item 4.
- Guia (a), linha 189: "obrigação de restaurante na capital" como exemplo de regra local, sem fonte.
- Guia (a), linha 337: "o que circula… é prática de agência (D)", sem fonte.
- Guia (a), linha 390: "de 6 a 12 meses" — marcado como premissa, mas a base indicada (A e B) não contém esse número;
  dizer "número meu".
- Guia (a), linha 41 (regra 3, classe A): a frase em negrito é a aplicação, que a seção 2.2 chama de inferência; o
  texto da política é a segunda frase.
- Guia (b), linha 312: "Em São Paulo, 2 horas de carro cobrem a região metropolitana", sem fonte.
- Guia (b), linha 290: "o endereço dela já é público na licença", sem fonte.
- Guia (b), linha 112: recomenda "citações" a partir de uma página que, segundo o próprio guia, não fala de diretórios.
- Guia (b), linha 415 (passo 13): "`LocalBusiness`… Sustenta relevância e destaque", quando a linha 289 diz que a
  página não liga a marcação ao mapa.
*Correção:* fonte ou a marca "inferência minha" em cada uma.

**F14 — Forma.** Guia (b): citações em inglês sem tradução (cerca de 28 linhas), inclusive no resumo "Em uma página"
(linhas 77 e 94), que é o que o owner lê primeiro. *Correção:* tradução ao lado, como no guia (a).

## 13. O que conferi e não achei problema

Política de spam (páginas de entrada, conteúdo em escala, excesso de palavras-chave, reputação de site, consequências,
tráfego de máquina, links pagos com `nofollow` ou `sponsored`; a página não diz que link pago é "ignorado", como o guia
(a) afirma na linha 425); datas do registro de mudanças e do painel de atualizações; fim do resultado rico de FAQ;
os dois estudos da Ahrefs; Pew; Near Media; BrightLocal (três estudos); Whitespark como opinião; rankings.io; Search
Atlas; os números do Google sobre spam no Maps; as citações das páginas de ajuda do perfil (classificação local,
categorias, nome, horário, área de cobertura, terceiros, avaliações, WhatsApp, desempenho); API de perguntas e
respostas e chat; Local Services Ads e o selo; a ausência de "quem aparece", de nome de pessoa do mercado local e de
caminho relativo.

## 14. Limites desta verificação

- O `WebFetch` responde por um modelo pequeno e corta páginas longas (o registro de mudanças e a pesquisa da Whitespark
  foram lidos só nos primeiros 100 mil caracteres). As entradas de 2025 do registro de mudanças (21/01, 22/01, 21/05,
  16/06 e 09/12/2025) **não foram conferidas**.
- Não conferi: os PDFs e as fontes que os guias já declaram não ter aberto; as páginas do Search Console além de
  7042828; Backlinko e Semrush; os artigos sobre o vazamento e o julgamento (classes C e D, fora do universo do
  sorteio); as demais páginas da Sterling Sky; o anexo `00a_perfil_google.md` além das linhas 61 e 149.
- F11(b) vem de uma leitura só.
