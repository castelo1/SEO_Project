# Guia (c), parte própria — como a busca do ChatGPT escolhe e cita fontes para um pedido de serviço local

- **Leitura das fontes:** sexta, 13/11/2026, das 19:47 às 20:16 (Brasília; `TZ=America/Sao_Paulo date`). Toda "data de leitura"
  deste arquivo é 13/11/2026.
- **Pergunta-guia:** o que acontece quando alguém escreve "preciso de uma dedetizadora confiável na Vila Mariana" no
  ChatGPT, hoje, e o que um site que **gera leads e não presta o serviço** pode fazer a respeito.
- **Como foi lido:** só busca na web e leitura de página pública. O ChatGPT **não** foi aberto; nenhuma pergunta foi
  feita a modelo algum. A ferramenta de leitura responde por meio de um modelo pequeno, que pode errar: toda citação
  literal de fonte oficial (classe A) foi pedida e **confirmada em uma segunda chamada** (uma delas com frases falsas de
  controle, que a ferramenta rejeitou). Números de estudos (classe B) foram lidos em uma chamada, salvo indicação: o
  verificador deve reabri-los.
- **Aviso central (atualizado depois do complemento abaixo):** as duas páginas de ajuda da OpenAI que mais importam
  (`help.openai.com`) e todo o `openai.com` devolveram **403** à ferramenta de leitura. **Uma delas** — o artigo
  9237897, "Searching the web with ChatGPT" — foi depois lida pela sessão principal no navegador (seção "Complemento da
  sessão principal", logo abaixo) e **entra como classe A**, com a ressalva de que o verificador independente recebeu
  403 e não pôde reconferir. O que o complemento **não** cobre (`utm_source=chatgpt.com`, `noindex`, "só link e
  título", Bing em contas Enterprise/Edu, notas de versão, páginas de `openai.com`) segue na seção 3.2 como **não
  conferido**.
- **Fórmula usada neste arquivo** para o que veio do complemento: "conferido na ajuda oficial da OpenAI
  (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal
  no navegador; o verificador independente recebeu erro 403 e não pôde reconferir)". Onde aparecer só **"conferido na
  ajuda oficial da OpenAI (complemento)"**, leia-se a fórmula inteira.

## Complemento da sessão principal — ajuda oficial da OpenAI lida no navegador (13/11/2026, 20:37)

A página de ajuda que deu 403 à ferramenta do subagente abriu no navegador pessoal, sem conta. É **classe A** (OpenAI
sobre o próprio produto; quem ganha: OpenAI). Fonte: "Searching the web with ChatGPT",
https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt (a página diz "atualizada há 25 dias", isto
é, por volta de 19/10/2026). **Limite:** só a sessão principal leu esta página; o verificador independente recebeu
erro 403 nas três tentativas e não pôde reconferir os trechos. O que ela diz, com o trecho curto que decide:

| Ponto | Trecho literal (lido no texto da página) | O que significa |
|---|---|---|
| Provedores parceiros | "ChatGPT search sometimes partners with other search providers." | A OpenAI **declara** que usa provedores de busca de terceiros, "às vezes". Não diz quais são todos |
| Quais provedores aparecem | A página manda ver a política de privacidade de dois: "Microsoft privacy statement" e "Shopify privacy policy" | **A Microsoft é a única empresa de busca nomeada**, e só pela remissão à declaração de privacidade. A página **não escreve "Bing"**: ler "Microsoft" como "Bing" é **inferência** minha, não frase da fonte. O Google não é citado. Isso não prova que o Google não é usado por via indireta (ponto disputado da seção 1) |
| Reescrita da consulta | "ChatGPT search typically rewrites your query into one or more targeted queries that it sends those providers." | Confirma, em fonte primária, a reescrita em uma ou mais buscas curtas (seção 6) |
| Localização na busca | ChatGPT "collects general location information based on your IP address and may share that general location with third-party search providers"; exemplo da página: "good restaurants near me" vira "top restaurants San Francisco" | Pedido local sem bairro é reescrito com a cidade inferida do IP. **Para o roteiro de teste: escrever o bairro na pergunta e anotar se a rede tinha VPN** |
| Memória | "If memory is enabled, ChatGPT may use relevant saved memories when rewriting a search query." | Conta com memória ligada muda a busca: o roteiro deve usar conversa temporária ou memória desligada (deixa de ser premissa não conferida) |
| Dados locais | Para resultados mais ajustados, o ChatGPT pode compartilhar a localização com "trusted third-party providers that help provide more local information, such as nearby business listings or weather reports" | A OpenAI **declara** que listagens de empresas próximas vêm de provedores terceiros; **não diz quais** (exceto, para reserva de restaurante, OpenTable, Resy e Yelp, com Resy e Yelp restritos aos Estados Unidos e Canadá) |
| Mapa | "On iOS and Android, relevant results may also include a map." | A página só **menciona** mapa para iOS e Android; **não diz "só"**. Que o mapa não apareça no navegador de computador é **inferência**, não conferida: o roteiro registra o que aparecer, na coluna `mostrou_mapa_ou_cartoes` |
| Critério de escolha | "ChatGPT ranks search results using multiple factors intended to help users find relevant, reliable information. Placement is not guaranteed." | A OpenAI não publica os fatores; ninguém garante posição |
| O que o site precisa permitir | "To make a website eligible for inclusion, allow OAI-Searchbot to crawl the site and confirm that the website host or content delivery network allows traffic from OpenAI's published searchbot IP addresses." | Confirma a seção 2: liberar o `OAI-SearchBot` no `robots.txt` **e** na hospedagem ou rede de distribuição |
| Quem pode buscar | "People who are not signed in can also use web search." | O teste deslogado é possível |

**O que continua não conferido:** a página "Publishers and developers FAQ"
(`https://help.openai.com/en/articles/12627856-publishers-and-developers-faq`) hoje **redireciona para um artigo sem
relação** (aposentadoria de um navegador da OpenAI); logo, `utm_source=chatgpt.com` e a regra de `noindex` seguem
**sem fonte primária lida**. As páginas de `openai.com` (anúncio da busca, anúncios pagos, subprocessadores) não foram
tentadas no navegador.

## Legenda das classes (regra de evidência de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`)

| Classe | O que é aqui | Vira regra? |
|---|---|---|
| **A** | Documentação oficial lida na página: OpenAI sobre os sistemas da OpenAI; Microsoft sobre o Bing; Google sobre o Google | sim |
| **B** | Estudo com amostra, método e dado expostos. Quase todos são de empresas que vendem ferramenta ou serviço de SEO: o conflito vai anotado em "quem ganha" | sim, com o limite da amostra e o país |
| **C** | Relato sem método de estudo: reportagem, depoimento relatado pela imprensa, pesquisa de opinião com praticantes | só hipótese |
| **D** | Vendedor (ferramenta, agência, curso) sem amostra ou método expostos, mesmo com caso mostrado | não; "alegação" |

"Consenso" = classe A, ou duas B independentes. "B fraca" (mesmo critério de
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`) = há número, mas falta amostra, país ou
método: **não vira regra** e não conta como uma das duas B de um consenso. Sobre respostas de IA, fonte anterior a 2026
leva **"pode estar desatualizada"**. Número de outro país vai com o país ao lado.

## Fontes abertas (o que cada "F" quer dizer)

| ID | Fonte (autor · título resumido) | URL | Data da fonte | Classe | Quem ganha com a afirmação |
|---|---|---|---|---|---|
| F1 | OpenAI · "Overview of OpenAI Crawlers" | https://developers.openai.com/api/docs/bots (o endereço antigo `https://platform.openai.com/docs/bots` redireciona, 301, para este) | sem data na página | A | OpenAI (quer que os sites liberem seus robôs); é a regra vigente dos robôs |
| F2 | OpenAI · lista de IPs do OAI-SearchBot | https://openai.com/searchbot.json | campo `creationTime` 02/01/2026 | A | OpenAI |
| F3 | OpenAI · documentação da API, "Web search" | https://developers.openai.com/api/docs/guides/tools-web-search | sem data | A (vale para a **API**, não para o aplicativo) | OpenAI (vende a API) |
| F4 | Microsoft · blog do Bing Webmaster, "Start Using Bing Webmaster Tools…" | https://blogs.bing.com/webmaster/2025/6/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility/ | 17/06/2025 | A (Microsoft sobre o Bing) · **pode estar desatualizada** | Microsoft (quer sites cadastrados no Bing) |
| F5 | Microsoft · "Introducing AI Performance in Bing Webmaster Tools Public Preview" | https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/ | 10/02/2026 | A | Microsoft |
| F6 | Microsoft · "Keeping Content Discoverable with Sitemaps in AI Powered Search" | https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search | 31/07/2025 | A · **pode estar desatualizada** | Microsoft |
| F7 | Microsoft · IndexNow, "Get started" | https://www.bing.com/indexnow/getstarted | sem data | A | Microsoft |
| F8 | Microsoft · "Announcing Microsoft Web IQ" | https://blogs.bing.com/search/June-2026/Announcing-Microsoft-Web-IQ | 02/06/2026 | A | Microsoft (vende a API) |
| F9 | Google · "AI features and your website" | https://developers.google.com/search/docs/appearance/ai-features | data não lida | A (Google sobre o Google) | Google |
| F10 | Google · comunicado do processo contra a SerpApi | https://blog.google/technology/safety-security/serpapi-lawsuit/ | 19/12/2025 | A só para "o Google processou e alega isto"; é parte no processo · **pode estar desatualizada** | Google |
| F11 | Search Engine Roundtable (B. Schwartz) · relato da reportagem do The Information sobre SerpApi | https://www.seroundtable.com/chatgpt-serpapi-scrape-google-39989.html | 25/08/2025 | C (reportagem de segunda mão; o original, pago, não foi aberto) · **pode estar desatualizada** | veículo do setor |
| F12 | PYMNTS/CPI · relato da Reuters sobre o depoimento do chefe do ChatGPT no julgamento do Google | https://www.pymnts.com/cpi-posts/openai-eyes-chrome-if-doj-forces-google-to-sell-browser-exec-testifies/ | 22/04/2025 | C (depoimento relatado pela imprensa) · **pode estar desatualizada** | — |
| F13 | Resoneo · estudo de engenharia reversa da recuperação do ChatGPT | https://think.resoneo.com/chatgpt-retrieval/ | julho/2026, atualizado em agosto/2026 | B | Resoneo, consultoria francesa de SEO/GEO; distribui a extensão usada na captura |
| F14 | Search Engine Journal (M. Southern) · matéria sobre o estudo da Resoneo | https://www.searchenginejournal.com/chatgpts-search-index-serves-small-sites-too-data-shows/585388/ | 11/08/2026 | C (reportagem) | veículo do setor |
| F15 | Peec · "ChatGPT search result providers" | https://docs.peec.ai/research/chatgpt-search-result-providers | setembro/2026 | D (não declara amostra, países nem período de coleta) | Peec, ferramenta de monitoramento de presença em IA (a página não diz o que vende; informação não conferida nela) |
| F16 | Peec · "ChatGPT has its own search index — the Labrador family" | https://docs.peec.ai/research/chatgpt-own-search-index-labrador | setembro/2026 | D (mesmo motivo) | idem |
| F17 | Peec · "Fan-outs per prompt by engine" | https://docs.peec.ai/research/fanouts-per-prompt-by-engine | maio/2026 (dados de 1–21/04/2026) | **B fraca** (período e total de buscas derivadas expostos; **número de perguntas e país não**) | idem |
| F18 | Peec · "GPT-5.6 retrieval changes" | https://docs.peec.ai/research/gpt-56-retrieval-changes | agosto/2026 | D (resumo sem amostra) | idem |
| F19 | Ahrefs (L. Linehan) · "How ChatGPT Does Query Fan-Out (15 Million Queries Studied)" | https://ahrefs.com/blog/query-fan-out-chatgpt/ | 12/10/2026 | B | Ahrefs, ferramenta de SEO; o artigo promove produto de monitoramento de IA |
| F20 | BrightLocal · "Top sources and directories for local AI search" | https://www.brightlocal.com/resources/ai-directory-sources/ | 26/08/2026 | B | BrightLocal vende cadastro em diretórios e monitoramento local |
| F21 | BrightLocal · "Local AI visibility study" | https://www.brightlocal.com/research/local-ai-visibility-study/ | 16/09/2026 | B | idem |
| F22 | BrightLocal · "Uncovering ChatGPT search sources" | https://www.brightlocal.com/learn/local-seo/uncovering-chatgpt-search-sources/ | 12/12/2024 | B · **pode estar desatualizada** | idem |
| F23 | SparkToro e Gumshoe (R. Fishkin) · inconsistência das recomendações de IA | https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/ | 28/01/2026 (dados de nov–dez/2025) | B | a Gumshoe vende monitoramento de IA (conflito declarado pelo autor) |
| F24 | Seer Interactive · "87% of SearchGPT citations match Bing's top results" | https://www.seerinteractive.com/insights/87-percent-of-searchgpt-citations-match-bings-top-results | 06/02/2025 | B · **pode estar desatualizada** | agência de SEO/GEO |
| F25 | Vercel e MERJ · "The rise of the AI crawler" | https://vercel.com/blog/the-rise-of-the-ai-crawler | 17/12/2024 | B · **pode estar desatualizada** | Vercel vende hospedagem com renderização no servidor |
| F26 | Whitespark (D. Shaw) · Local Search Ranking Factors 2026 | https://whitespark.ca/local-search-ranking-factors/ | 06/11/2025 | C (opinião de 47 especialistas, não dado medido) · **pode estar desatualizada** | Whitespark vende software e serviço de SEO local |
| F27 | Yext · "Where do … ChatGPT get local business information?" | https://www.yext.com/blog/where-do-google-gemini-chatgpt-get-local-business-information | 13/06/2024 | D · **desatualizada** | Yext vende gestão de cadastros em diretórios |
| F28 | Local Falcon · "ChatGPT local search data sources" | https://www.localfalcon.com/blog/chatgpt-local-search-data-sources-where-does-business-info-come-from | 05/11/2025 | D (sem número nem método) · **pode estar desatualizada** | Local Falcon vende monitoramento local |
| F29 | Semrush · domínios mais citados por IA | https://www.semrush.com/blog/most-cited-domains-ai/ | 10/11/2025 | B (230 mil perguntas, 13 semanas; país não declarado) · **pode estar desatualizada** | Semrush, ferramenta de SEO |
| F30 | MarTech (C. von Hoffman) · acordo Yelp–OpenAI, citando o Axios | https://martech.org/yelp-brings-reviews-and-local-leads-to-chatgpt/ | 28/07/2026 | C (reportagem de segunda mão; o Axios deu 403) | veículo do setor |
| F31 | Search Engine Roundtable · compartilhamento de localização no ChatGPT | https://www.seroundtable.com/chatgpt-location-sharing-41128.html | 31/03/2026 | C (reportagem que cita as notas de versão da OpenAI) | veículo do setor |
| F32 | Tecnoblog · anúncios no ChatGPT para usuários no Brasil | https://tecnoblog.net/noticias/openai-comeca-a-mostrar-anuncios-no-chatgpt-para-usuarios-no-brasil/ | 04/08/2026 | C (reportagem) | — |
| F33 | Conversion (agência brasileira) · resumo do estudo da Resoneo | https://www.conversion.com.br/blog/indice-do-chatgpt-tambem-inclui-sites-pequenos-aponta-estudo | 18/08/2026 | D que repassa uma B (F13) | agência de SEO |
| F34 | Canaltech · matéria sobre o estudo "Quem influencia o ChatGPT no Brasil?" (Ranqia) | https://canaltech.com.br/inteligencia-artificial/canaltech-e-o-portal-tech-brasileiro-que-mais-influencia-no-chatgpt/ | 25/08/2026 | C (reportagem; o veículo é parte interessada) | Canaltech; a Ranqia é consultoria |
| F35 | SOCi · comunicado do "2026 Local Visibility Index" | https://www.soci.ai/news/in-ai-driven-discovery-few-brands-are-chosen-most-disappear/ | 28/01/2026 | D (comunicado; método não explicado) | SOCi vende marketing local para redes |
| F36 | Método do artigo salvo pelo dono | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md` | 08/10/2026 | D | autor vende ferramenta |

---

## 1. De onde vem o índice da busca do ChatGPT

### 1.1 O que a OpenAI declara (e eu consegui abrir)

| Afirmação | Fonte | Classe |
|---|---|---|
| A OpenAI tem um robô próprio de busca. Texto: "OAI-SearchBot is used to surface websites in search results in ChatGPT's search features." | F1 | A |
| A página dos robôs **não menciona** Bing, Google, parceiros de busca, sitemap, `noindex` nem JavaScript (perguntado à página; resposta "não" para os quatro termos conferidos: sitemap, noindex, JavaScript, Bing) | F1 | A (silêncio da fonte) |
| A documentação da **API** não nomeia provedor de busca (Bing, Google ou outro) | F3 | A (silêncio; vale para a API) |

**Sobre provedores de busca terceiros** (texto reconciliado com o complemento): a OpenAI **declara** que a busca do
ChatGPT "sometimes partners with other search providers" e remete à declaração de privacidade da Microsoft — conferido
na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em
13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir).
Classe A, com essa ressalva. O que **continua sem fonte primária conferida**: a frase "a OpenAI declara que usa o
**Bing**" (a página nomeia a Microsoft, não o Bing; a ligação é inferência), em que proporção cada provedor entra, e o
uso do Bing em contas Enterprise/Edu (seção 3.2).

### 1.2 O que a Microsoft declara

| Afirmação | Fonte | Classe |
|---|---|---|
| Em junho de 2025 a Microsoft listou o ChatGPT entre as experiências que o Bing alimenta. Trechos: "Bing powers a wide range of AI and search experiences" e, na lista que segue, "AI tools like ChatGPT and Inflection.ai" | F4 | A (Microsoft) · **pode estar desatualizada** |
| Em junho de 2026 a Microsoft lançou o "Web IQ" ("Web IQ is a search engine for AI systems."), apoiado em "the Bing global index and ecosystem". O anúncio **não cita** ChatGPT nem OpenAI (conferido com frase falsa de controle) | F8 | A |
| O relatório de desempenho de IA do Bing cobre "Microsoft Copilot, AI-generated summaries in Bing, and select partner integrations" e **não nomeia** os parceiros | F5 | A |

### 1.3 Reportagem e depoimento (classe C)

| Afirmação | Fonte | Classe |
|---|---|---|
| Em abril de 2025, no julgamento do Google nos EUA, o chefe do ChatGPT disse (segundo a Reuters, relatada pela PYMNTS) que o Google **recusou** um pedido de parceria feito em agosto (o ano não está no trecho lido), que não havia parceria com o Google e que o ChatGPT estava a anos de atender a maioria das consultas com busca própria. A matéria dá o **Bing** como provedor de busca do ChatGPT na época; se isso foi dito no depoimento ou é atribuição do veículo, não conferi | F12 | C · **pode estar desatualizada** |
| Em agosto de 2025, o The Information (pago; lido por relato) publicou que a OpenAI usava resultados do Google raspados pela SerpApi, para temas de atualidade (notícias, esportes). Sem comentário da OpenAI nem do Google no relato | F11 | C · **pode estar desatualizada** |
| Em 19/12/2025 o Google processou a SerpApi; diz que ela burla proteções, raspa resultados e revende o conteúdo. O comunicado **não cita** a OpenAI | F10 | A só para o fato do processo |
| Em meados de setembro de 2025 o Google deixou de aceitar o parâmetro de 100 resultados por página. Na mesma época as citações do ChatGPT a Reddit e Wikipedia caíram (Reddit: de perto de 60% das respostas para cerca de 10%; Wikipedia: de cerca de 55% para menos de 20%; país não declarado). A própria Semrush **duvida** que o parâmetro seja a causa principal | F29 | B para a queda; C para a causa · **pode estar desatualizada** |

### 1.4 Estudos com dado, 2026

| Afirmação | Fonte | Classe |
|---|---|---|
| Até 21/07/2026, cada resultado de busca no tráfego do ChatGPT trazia um campo com o nome do "encanamento" de origem: `labrador` (lido como índice próprio da OpenAI), `bright`, `oxylabs` e `serp` (raspadores terceiros; cerca de uma em cada três URLs do `bright` estava na primeira página do Google, contra uma em vinte no Bing). O campo sumiu em 21/07; depois disso a origem é inferida pelo formato do trecho | F13 | B |
| Amostra: 1.249 respostas com busca (682 no modo instantâneo, 567 no modo de raciocínio), cerca de 88 mil resultados, 26,9 mil páginas, 6,4 mil domínios; contas gratuitas, pagas e deslogada, por VPN; **corpus em inglês** (a página fala só em "our English-language corpus", uma vez); **sem recorte por país** | F13 | B |
| Conta **gratuita, modo instantâneo** (julho; 1.793 resultados): 63,6% índice próprio, 34,7% Google raspado, 1,6% outro raspador | F13 | B |
| Conta **paga, modo de raciocínio** (julho; 16.407 resultados): 23,6% índice próprio, 74,6% Google raspado. Em agosto: 24,7% × 75,3% | F13 | B |
| Conta **gratuita, modo de raciocínio** (agosto): 74,7% índice próprio, 22,2% de um segundo raspador (`oxylabs`), 3,1% Google | F13 | B |
| Por tipo de pergunta, no gratuito instantâneo, **"empresas e lugares" vieram 100% do índice próprio**; no pago com raciocínio, cerca de 95% do Google raspado. O estudo avisa que as médias dependem da mistura de perguntas | F13 | B |
| Cerca de **um terço** das perguntas repetidas trocou de encanamento: o roteamento não é determinístico | F13 | B |
| O índice próprio **não é o Bing com outro nome** (títulos mais longos do que o Bing guarda). Um "encanamento Bing" foi visto por outro pesquisador numa conta de plano Team em junho; a Resoneo **nunca** o viu nas contas dela | F13 | B |
| A matéria que cobriu o estudo **não traz posição da OpenAI**; registra que a página dos robôs não descreve o índice próprio. Confirmação desses rótulos pela OpenAI: não encontrei em nenhuma fonte aberta | F14 | C |
| Outro vendedor leu o mesmo campo entre 21/05 e 21/07/2026 e descreve índice próprio "em família" (web, notícias, local, compras…) mais ao menos oito provedores externos; diz que o Bing aparece sobretudo em sessões de pesquisa aprofundada. **Não declara amostra** | F15, F16 | D |
| Em fevereiro de 2025, 87% das citações da busca do ChatGPT coincidiam com os 20 primeiros do Bing e 56% com o Google (EUA presumido; cerca de 100 consultas, quase todas com "melhor"/"top"; os autores chamam de "direcional") | F24 | B · **pode estar desatualizada** |

### 1.5 Conclusão sobre o índice

- **Consenso (A):** a OpenAI rastreia a web com robô próprio (`OAI-SearchBot`) para alimentar a busca do ChatGPT (F1).
- **Indício forte, não consenso:** a OpenAI mantém **índice próprio**. Sustentação: **uma B** (F13) mais **inferência**
  a partir de F1 — que descreve o robô, não um índice (ver a linha de F14 na seção 1.4); F15–F16 concordam, mas são
  alegação de vendedor (D). Uma B e uma inferência não cumprem a regra de consenso.
- **Indício forte, não consenso:** resultados do **Google** chegam ao ChatGPT por raspadores terceiros, em proporção que
  muda com o plano e o modo. Sustentação: uma B (F13), uma reportagem (F11) e alegação de vendedor (F15). A OpenAI não
  declara; o Google processa um dos raspadores (F10). A tática 4.2 do artigo do dono ("ele busca no Google", F36) fica
  **parcialmente apoiada e mal formulada**: não é o ChatGPT consultando o Google, e sim resultados do Google comprados de
  terceiros, sobretudo em contas pagas com raciocínio — e, em conta gratuita, pergunta sobre empresa e lugar veio do
  índice próprio.
- **Disputado:** o papel do **Bing hoje**. A favor: a Microsoft o afirmava em junho de 2025 (F4), o depoimento de abril
  de 2025 (F12), um estudo de fevereiro de 2025 (F24) — as três de 2025, **podem estar desatualizadas** — e a ajuda
  oficial da OpenAI, que declara parceria "às vezes" com outros provedores de busca e remete à declaração de
  privacidade da **Microsoft**, sem escrever "Bing" e sem dar proporção (conferido na ajuda oficial da OpenAI,
  https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal
  no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). Contra: o estudo de 2026 não vê o
  Bing nas contas comuns (F13). Tratar "estar no Bing" como sinônimo de "estar no ChatGPT" **não se
  sustenta** em 2026; descartar o Bing também não.
- **Não sei:** as proporções para perguntas **em português feitas do Brasil**; o que mudou depois de 15/08/2026.

---

## 2. Os robôs da OpenAI (página oficial, F1 — classe A em toda a tabela)

| Robô | Para que serve (texto literal curto) | Identificação (trecho do user-agent; a versão pode mudar) | IPs publicados | `robots.txt` |
|---|---|---|---|---|
| **OAI-SearchBot** | "OAI-SearchBot is used to surface websites in search results in ChatGPT's search features." | `OAI-SearchBot/1.4; +https://openai.com/searchbot` | https://openai.com/searchbot.json | respeita; é o que controla aparecer na busca |
| **GPTBot** | "GPTBot is used to make our generative AI foundation models more useful and safe." e "Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models." | `GPTBot/1.4; +https://openai.com/gptbot` | https://openai.com/gptbot.json | respeita; controla **treino** |
| **ChatGPT-User** | "ChatGPT-User is not used for crawling the web in an automatic fashion." Visita quando um usuário pede (inclusive GPTs personalizados e ações) | `ChatGPT-User/1.0; +https://openai.com/bot` | https://openai.com/chatgpt-user.json | "Because these actions are initiated by a user, robots.txt rules may not apply." |
| **OAI-AdsBot** | "OAI-AdsBot is used to validate the safety of web pages submitted as ads on ChatGPT." e "OAI-AdsBot only visits pages submitted as ads" | `OAI-AdsBot/1.0; +https://openai.com/adsbot` | https://openai.com/adsbot.json | — |

A página lista **só esses quatro**. Não há robô de "agente" ou "operador" nela; como o modo agente e o navegador da
OpenAI se identificam ao visitar um site: **não sei** (não há fonte primária aberta).

Outras regras da mesma página (F1, classe A):

- **O que permitir para poder ser citado:** "To help ensure your site appears in search results, we recommend allowing
  OAI-SearchBot in your site's robots.txt file and allowing requests from our published IP ranges". São duas condições:
  o `robots.txt` **e** a hospedagem/CDN/firewall não barrarem os IPs publicados.
- **Bloquear o GPTBot e permitir o OAI-SearchBot:** é possível e não tira o site da busca. "Each setting is independent
  of the others"; "a webmaster can allow OAI-SearchBot in order to appear in search results while disallowing GPTBot".
  Se os dois forem permitidos, uma mesma visita pode servir aos dois usos.
- **Site que bloqueia o OAI-SearchBot:** "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search
  answers, though can still appear as navigational links." Ou seja: some das respostas, mas o endereço ainda pode
  aparecer como link de navegação.
- **ChatGPT-User não decide a busca:** "ChatGPT-User is not used to determine whether content may appear in Search."
- **Prazo:** "For search results, please note it can take ~24 hours from a site's robots.txt update for our systems to
  adjust."
- **Faixas de IP:** o arquivo do OAI-SearchBot tinha 39 faixas IPv4 e `creationTime` de 02/01/2026 na leitura de
  13/11/2026 (F2, duas chamadas). As faixas mudam: ler o arquivo na hora de configurar, não copiar para o repositório.
- **`noindex` e "só link e título":** a página dos robôs **não trata**. Estaria na página de perguntas de publishers,
  que deu 403 à ferramenta e que, no navegador da sessão principal, hoje redireciona para um artigo sem relação
  (complemento): **não conferido**.

O que estudo acrescenta (não é regra da OpenAI):

| Afirmação | Fonte | Classe |
|---|---|---|
| O OAI-SearchBot constrói o índice de busca, que guarda um **trecho curto e congelado** de cada página; o ChatGPT-User alimenta só um cache de leitura (página inteira em Markdown) e **nunca** altera o índice; o GPTBot não alimenta nenhum dos dois | F13 | B (uma fonte) |
| O `noindex` foi ignorado pelo cache de leitura (medição de terceiro citada no estudo) | F13 | B (uma fonte) |
| Em dezembro de 2024 nenhum dos três robôs da OpenAI executava JavaScript (dados da rede da Vercel; GPTBot com 569 milhões de visitas no mês) | F25 | B · **pode estar desatualizada** |
| Em 2026 há relatos soltos de que o OAI-SearchBot passou a executar JavaScript em alguns sites; nenhum estudo aberto confirma, e a OpenAI não documenta | só resultado de busca, páginas não abertas | **não sei** |

---

## 3. O que a OpenAI diz a donos de site

### 3.1 Conferido na fonte

| Pergunta | Resposta | Fonte | Classe |
|---|---|---|---|
| Como aparecer? | Permitir o OAI-SearchBot no `robots.txt` e não barrar os IPs publicados | F1 | A |
| Há como "enviar" o site ou o sitemap à OpenAI? | A página dos robôs não oferece envio nem cita sitemap. Se existe outro canal: **não sei** | F1 | A (silêncio) |
| A OpenAI declara fatores de escolha de fonte? | Na página dos robôs, **não**. Na API, só diz que o modelo decide se busca: "Like any other tool, the model can choose to search the web or not based on the content of the input prompt." A ajuda do aplicativo diz só que a ordenação usa "multiple factors" e que "Placement is not guaranteed." (conferido na ajuda oficial da OpenAI — complemento); **não publica quais fatores** | F1, F3; ajuda da OpenAI (complemento) | A |
| Existe anúncio no ChatGPT? | Sim: há um robô só para validar páginas de anúncios (F1). No Brasil, piloto anunciado em 04/08/2026 para contas gratuitas e Go, maiores de 18 anos, anúncios marcados como patrocinados; segundo a OpenAI, relatada pela matéria, não influenciam as respostas (F32) | F1 (A) · F32 (C) |
| Dá para pagar por posição na resposta? | Nada nas fontes abertas indica que sim; a negativa da OpenAI só foi lida por reportagem (F32). A página oficial de anúncios deu 403: **não conclusivo** | F32 | C |

### 3.2 Visto só no trecho devolvido pela ferramenta de busca — páginas que deram **403** à ferramenta

Quando esta seção foi escrita, nenhuma destas páginas tinha aberto. Depois disso, a sessão principal leu **uma** delas
no navegador (o artigo 9237897; ver "Complemento da sessão principal", no alto do arquivo). A coluna "Situação" diz o
que mudou. O endereço `…/9237897-chatgpt-search`, usado abaixo, e o endereço `…/9237897-searching-the-web-with-chatgpt`,
usado no complemento, são o **mesmo artigo** (número 9237897). As linhas marcadas **não conferido** continuam **não
sendo evidência**: servem para o dono conferir em cinco minutos no navegador.

| O que a página diria | Página (abrir no navegador) | Situação depois do complemento |
|---|---|---|
| A busca do ChatGPT às vezes recorre a provedores de busca parceiros e reescreve a pergunta em uma ou mais consultas dirigidas | https://help.openai.com/en/articles/9237897-chatgpt-search | **Conferido** na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). Classe A |
| A busca não repassa IP nem dados da conta ao provedor | https://help.openai.com/en/articles/9237897-chatgpt-search | **Não conferido** nesses termos. O que o complemento leu é outra coisa: a localização geral, inferida do endereço IP, **pode ser compartilhada** com provedores terceiros |
| Em contas Enterprise/Edu, consultas desassociadas podem ir ao **Bing** | https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu | **Não conferido** (página não aberta por ninguém) |
| A classificação usa "vários fatores"; não há como garantir posição | https://help.openai.com/en/articles/9237897-chatgpt-search | **Conferido** na ajuda oficial da OpenAI (complemento). Classe A |
| Para entrar em resumos e trechos, não bloquear o OAI-SearchBot | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | A exigência de permitir o `OAI-SearchBot` e os IPs publicados está **conferida** em F1 e na ajuda oficial da OpenAI (complemento). Classe A |
| Página bloqueada pode aparecer só com link e título; para evitar, usar `noindex` (e o robô precisa conseguir ler a página para ver a marca) | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | **Não conferido**: no navegador da sessão principal, a página hoje redireciona para um artigo sem relação. F1 só confirma que site bloqueado "can still appear as navigational links" |
| O ChatGPT acrescenta `utm_source=chatgpt.com` aos links de saída | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | **Não conferido** (mesmo motivo) |
| Compartilhamento de localização do aparelho, opcional e desligado por padrão (março de 2026) | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | **Não conferido** na fonte primária (só por reportagem, F31, C). O complemento confere outra coisa: a localização geral **por IP** |
| Anúncio de lançamento da busca (31/10/2024): provedores terceiros e conteúdo de parceiros | https://openai.com/index/introducing-chatgpt-search/ | **Não conferido** (não tentado no navegador). A existência de provedores parceiros está conferida pela ajuda (primeira linha) |

**Veredito da seção (atualizado):** a menção a provedores parceiros, a reescrita da pergunta e "vários fatores, sem
garantia de posição" **deixaram de ser não conclusivos**: são classe A pelo complemento, lido só pela sessão principal
(o verificador independente recebeu 403). Continuam **não conferidos**: `utm_source=chatgpt.com`, a regra do
`noindex`, "só link e título", o Bing em contas Enterprise/Edu, as notas de versão e o anúncio de 2024.

---

## 4. O Bing como caminho

| Afirmação | Fonte | Classe |
|---|---|---|
| O Bing Webmaster Tools é gratuito ("Free and full of powerful features"); aceita importar o site do Google Search Console ("Import your site from Google Search Console"); recebe sitemap ("Submit and monitor your sitemap") e confere atualização ao menos uma vez por dia | F4 | A · página de 2025, **pode estar desatualizada** |
| O IndexNow avisa os buscadores participantes quando uma página muda ("Instantly notify Bing and other search engines participating in IndexNow"); exige uma chave em arquivo de texto hospedado no site e o envio das URLs; **não garante** rastreio nem indexação; a página não cita OpenAI | F4, F7 | A (F4 é de 2025: **pode estar desatualizada**; F7 não tem data) |
| Sitemap continua sendo o sinal de base para cobertura; `lastmod` deve refletir a mudança real do conteúdo; sitemap e IndexNow se somam | F6 | A · página de 2025, **pode estar desatualizada** |
| Desde 10/02/2026 existe o relatório **AI Performance** (prévia pública): total de citações, páginas citadas, "consultas de fundamentação", tendência. Cobre Copilot, resumos de IA do Bing e parceiros não nomeados. Aviso: "This reflects how often pages are cited, not page importance, ranking, or placement" | F5 | A |
| Em junho e outubro de 2026 o relatório ganhou novas visões (intenções, tópicos, participação de citações) | só resultado de busca (blogs.bing.com), não aberto | não conferido |
| O relatório **não diz** se inclui o ChatGPT; não tem dado de clique na leitura feita | F5 | A (silêncio) |

**Bing Places for Business (perfil de empresa do Bing).** As páginas oficiais de ajuda
(`https://www.bing.com/forbusiness/help/`, `…/dataQualityGuidelines`, `…/businessesWithoutPhysicalStore`) carregam o
texto por JavaScript e vieram **vazias** na ferramenta. Elegibilidade, país e a regra para intermediário: **não
conclusivo**. O trecho devolvido pela busca (não conferido) diz que o perfil exige endereço físico visitável ou área de
atendimento onde a equipe vai ao cliente, com endereço válido para verificação — a mesma lógica que vedou o perfil do
Google ao gerador de leads em
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos, linhas 25–27). **Premissa
adotada:** tratar como vedado para o gerador de leads até prova em contrário; o caminho legítimo é o perfil ser da
licenciada. Criar ou reivindicar perfil está fora da rodada de qualquer modo.

**Quanto o Bing vale para o ChatGPT:** disputado (seção 1.5). Vale com certeza para o Bing e o Copilot (A). É barato,
mas exige conta: ação do dono, fora desta rodada.

---

## 5. De onde vêm os dados de empresa local e de mapa

### 5.1 O que a OpenAI declara

Texto reconciliado com o complemento. A página dos robôs (F1) não fala de resultados locais. A ajuda do aplicativo
fala — conferido na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt,
lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde
reconferir). Classe A, com essa ressalva:

| Afirmação | Trecho curto | O que fica em aberto |
|---|---|---|
| Listagens de empresas próximas vêm de **provedores terceiros** | "trusted third-party providers that help provide more local information, such as nearby business listings or weather reports" | A OpenAI **não diz quais** (só nomeia, para reserva de restaurante, OpenTable, Resy e Yelp, com Resy e Yelp restritos aos Estados Unidos e Canadá) |
| A localização usada na busca é a **geral, inferida do endereço IP**, e pode ser repassada a provedores de busca terceiros | "collects general location information based on your IP address and may share that general location with third-party search providers" | Qual a precisão (cidade? bairro?): não dito. O exemplo da página troca "near me" pelo nome de uma cidade |
| Mapa | "On iOS and Android, relevant results may also include a map." | A página não diz "só"; no navegador de computador: não conferido |

Continua **não conferido** em fonte primária: o acordo com o Yelp (só reportagem, seção 5.2), os anúncios em
`openai.com` (403) e qualquer lista de bases locais usadas fora dos Estados Unidos e do Canadá.

### 5.2 Reportagem

| Afirmação | Fonte | Classe |
|---|---|---|
| O Yelp licencia avaliações, notas, fotos e dados de empresas à OpenAI; marca e links do Yelp aparecem junto; previsto o pedido de orçamento do Yelp dentro do ChatGPT; acordo não exclusivo; valores não divulgados. A matéria não nomeia países | F30 (repassa o Axios) | C |
| Desde março de 2026 o usuário pode compartilhar a localização do aparelho; é opcional e vem desligado. Um teste citado achou resultados "perto de mim" a cerca de 45 minutos de distância | F31 | C |

### 5.3 Estudos com dado — todos de fora do Brasil

| Afirmação | Amostra · país · data | Fonte | Classe |
|---|---|---|---|
| Os resultados locais chegam por alimentações reconhecíveis pelo formato do identificador: **Yelp, TripAdvisor e Google Maps**. Quase um em cada cinco registros rotulados Yelp trazia link copiado de um perfil de empresa do Google. No modo instantâneo a resposta sobre empresas vem com **mapa**; no modo de raciocínio o mapa some | 1.249 respostas · corpus em inglês, sem país · jul–ago/2026 | F13 | B |
| O **Yelp** apareceu em 80% das respostas do ChatGPT e recebeu 99.281 de 162.966 citações a domínios terceiros (cerca de 61%). Depois: TripAdvisor (10.227), OpenTable (9.147), BBB (4.247), Angie's List (1.768), Trustpilot (1.136), Yellow Pages (711), HomeAdvisor (705) | 60.970 checagens, cerca de 1.355 locais, 13 categorias · **EUA, Reino Unido, Austrália** · publicado em 26/08/2026 | F20 | B |
| O ChatGPT citou empresas em 33% das buscas (29,4% quando a empresa atende em domicílio); média de 4,1 empresas por resposta; 10% de respostas vazias; "quase não usa" o perfil de empresa do Google e se apoia em Yelp e Bing; coincide só 19–20% com as superfícies do Google; cerca de 53% das empresas citadas ficam a até 5 km | cerca de 200 mil buscas, cerca de 1.300 locais, 60 dias · país não declarado na página (o estudo irmão F20 é EUA/Reino Unido/Austrália) · 16/09/2026 | F21 | B |
| Em novembro de 2024: 58% das fontes eram sites das próprias empresas, 27% menções (Wikipedia à frente), 15% diretórios; Yelp, Facebook e Google Maps **não** apareciam | 800 buscas manuais, 20 setores, 20 cidades · **EUA** | F22 | B · **pode estar desatualizada** (o retrato de 2026 é outro) |
| O ChatGPT recomendaria 1,2% dos locais de redes; o pacote local do Google, 35,9%; nota média dos recomendados, 4,3 estrelas | 350 mil locais de 2.751 **redes com várias unidades** · país e método não declarados · 28/01/2026 | F35 | D |
| Especialistas apontam como fatores de visibilidade em IA: estar em listas "melhores de" feitas por terceiros; página dedicada a cada serviço; presença em domínios do setor; citações não estruturadas de qualidade; autoridade dos sites onde estão as avaliações | 47 especialistas, pesquisa de opinião · foco norte-americano · 06/11/2025 | F26 | C · **pode estar desatualizada** |
| "60–70% dos dados locais do ChatGPT vêm do Foursquare" | sem método localizado; um estudo de agosto de 2026 que contestaria o número não abriu | — | **não sei** (alegação sem fonte aberta) |
| "O ChatGPT lê Bing Places" / "tem integração direta com o Bing" para dados locais | sem número nem método | F28 | D |
| Listas de diretórios que o ChatGPT "disse" usar quando perguntado | resposta do próprio modelo, 2024 | F27 | D · desatualizada |

**Peso de cada coisa, pelo que as fontes abertas dão:** para **diretórios e citações em terceiros** há dado B (F20, F21,
F22), todo de fora do Brasil. Para **avaliações** (nota, quantidade, texto) **não há A nem B**: só F35 (D; nota média de
4,3 estrelas entre os recomendados, método não explicado) e F26 (C; opinião de especialistas sobre a "autoridade dos
sites onde estão as avaliações"). Quanto as avaliações pesam para uma empresa ser citada pelo ChatGPT: **não sei**.

### 5.4 Brasil

- **Não encontrei estudo com dado** sobre fontes que o ChatGPT cita para serviço local no Brasil.
- O único levantamento brasileiro aberto trata de notícias e referências, não de serviço local: mais de 60 mil domínios,
  dezembro de 2025 a julho de 2026; Reddit e Wikipedia no topo; a maioria das respostas usa de três a cinco fontes
  (F34, C).
- Se o Yelp, base principal nos estudos de língua inglesa, tem cobertura útil de dedetizadoras em São Paulo: **não sei**.
  É o que o roteiro de teste mede.

**Candidatos brasileiros — HIPÓTESE, nenhum com evidência** (a conferir pela coluna "fontes citadas" do roteiro
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`):

| Tipo | Candidatos | Por que entram na lista |
|---|---|---|
| Mapas e perfis | Google Maps (via terceiros), Bing Places, Apple Maps, Foursquare | são os equivalentes das alimentações vistas em F13 e F20 |
| Reclamações e avaliações | Reclame Aqui, Trustpilot, páginas do Facebook | papel análogo ao de BBB e Trustpilot em F20 |
| Plataformas de orçamento | GetNinjas, Habitissimo, Triider, Cronoshare | análogas a Angi e HomeAdvisor em F20; GetNinjas e Triider já aparecem em `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md`, linhas 168–169; o Habitissimo está lá só como "não verificado" (linha 171) e a Cronoshare não aparece |
| Guias e listas telefônicas | Guia Mais, Apontador, TeleListas, Solutudo | análogos a Yellow Pages em F20 |
| Fontes oficiais e do setor | páginas da vigilância sanitária (estado e município), associações de controladores de pragas | o ChatGPT de 2026 busca mais fonte "oficial" (F19); pode pesar em pergunta sobre licença |
| Imprensa local | portais e jornais de bairro, matérias sobre golpe de dedetização | "menções" eram 27% das fontes em F22 |

---

## 6. Reescrita da pergunta em buscas ("fan-out")

| Afirmação | Amostra · país · data | Fonte | Classe |
|---|---|---|---|
| Na API, o modelo decide se busca ou não, e os modelos de raciocínio refinam a busca enquanto leem: "It can refine its searches as it reads results." A página não fala do aplicativo | — | F3 | A (para a API) |
| A ajuda do aplicativo diz: "ChatGPT search typically rewrites your query into one or more targeted queries that it sends those providers." Com a memória ligada, memórias salvas podem entrar na reescrita | — | conferido na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir) | A (para o aplicativo) |
| ChatGPT: 2,1 buscas por pergunta (Perplexity 1,4; Grok 6,8) | cerca de 5 milhões de buscas derivadas · **número de perguntas e país não declarados** · 1–21/04/2026 | F17 | **B fraca** (critério do guia (c): falta amostra de perguntas e país; não vira regra) |
| Em respostas gratuitas e deslogadas, só **14,4%** continham buscas derivadas; nessas, média de 1,6 busca. O ano "2026" estava em 22,9% das buscas de setembro; "official" em 13,1%; "price" em 8,9%; o operador `site:` em 6,8% (75,9% dos mais comuns miravam o site da própria marca) | 66,6 milhões de respostas e 15 milhões de buscas · todos os países; análise de palavras em **inglês** · ago–set/2026 | F19 | B |
| Em perguntas factuais, 84,4% das respostas citaram ao menos uma fonte oficial; em perguntas de comparação, 68,3%. Sites oficiais: 63,4% das citações em factuais e 46,4% em comparações | 20 mil perguntas · **EUA** · 2026 | F19 | B |
| Citações ao Reddit caíram 88% em seis meses (março a setembro de 2026); Wikipedia, 80% | **EUA** · 2,4 a 3,8 milhões de respostas por mês | F19 | B |
| Com o modelo que virou padrão em agosto de 2026, perguntas resolvidas com uma só rodada de busca caíram de 94,0% para 43,5%; `site:` foi de 0,3% para 23% das buscas; fontes por pergunta de cerca de 12 para cerca de 24 | sem amostra declarada · ago/2026 | F18 | D |
| "De 2,17 para 7,61 buscas por pergunta" no modelo mais forte | relato de segunda mão; original não localizado | só resultado de busca | **não sei** |
| O ChatGPT reescreve a conversa em "duas a cinco buscas curtas" (tática 4.3 do artigo do dono) | — | F36 | D; **a ordem de grandeza é compatível** com F17 e F19 para o período até meados de 2026; o formato exato das buscas em português não foi medido |

**Leitura:** a reescrita existe: **A para a API** (F3) e **A para o aplicativo** (conferido na ajuda oficial da OpenAI —
complemento; lida só pela sessão principal, o verificador independente recebeu 403), com apoio de uma B (F19).
**Quantas** buscas e **com que palavras** varia com o modelo, o plano e o mês: disputado (F19 é B; F17 é B fraca; F18 é
D). Para uma pergunta de serviço local em português: **não sei**.

---

## 7. O que difere do Google orgânico e dos resumos de IA do Google

Detalhe do lado Google nos guias (a) e (b) do item 3 (por exemplo
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`); aqui, só o contraste.

| Tema | Google orgânico e resumos de IA do Google | Busca do ChatGPT | Fonte · classe |
|---|---|---|---|
| Requisito para aparecer | "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."; a página precisa estar indexada e apta a trecho | permitir o OAI-SearchBot e não barrar seus IPs | F9 (A) · F1 (A) |
| Índice | um só, do Google | índice próprio **mais** resultados de terceiros (Google raspado; Bing em disputa), variando por plano e modo | F13 (B) |
| Robôs | Googlebot; o controle de uso em IA fora da busca é à parte | **quatro** robôs com funções separadas: busca (`OAI-SearchBot`), treino (`GPTBot`), visita a pedido do usuário (`ChatGPT-User`) e validação de anúncios (`OAI-AdsBot`) | F9, F1 (A) |
| Reescrita da pergunta | os recursos de IA podem usar "query fan-out": "issuing multiple related searches across subtopics and data sources" | também reescreve (ajuda oficial da OpenAI, complemento); quantidade instável | F9 (A) · ajuda da OpenAI (A, complemento) · F19 (B) · F17 (B fraca) |
| Dados de empresa local | perfil de empresa do Google, que o dono da empresa controla | **não há perfil de empresa próprio da OpenAI** nas fontes abertas; a OpenAI declara que as listagens vêm de provedores terceiros, sem dizer quais (ajuda oficial, complemento); nos estudos, vêm de Yelp, TripAdvisor, Google Maps via terceiros e dos sites | ajuda da OpenAI (A, complemento) · F13, F20, F21 (B; fora do Brasil) |
| Coincidência das empresas citadas | — | só 19–20% de coincidência com as superfícies do Google (**país não declarado** na página) | F21 (B) |
| Proximidade | — | 90% das empresas citadas dentro de um raio de 287 km no ChatGPT, contra 39–64 km no Google; cerca de 53% a até 5 km (**país não declarado** na página) | F21 (B) |
| Localização do usuário | — | compartilhamento do aparelho opcional desde março de 2026 (F31, C); **sem ele, a busca usa a localização geral inferida do endereço IP**, que pode ser repassada a provedores terceiros — conferido na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir) | F31 (C) · ajuda da OpenAI (A, complemento) |
| Memória e personalização | — | com a memória ligada, o ChatGPT "may use relevant saved memories when rewriting a search query" — conferido na ajuda oficial da OpenAI (complemento; mesma ressalva). **Tamanho** do efeito: não sei | ajuda da OpenAI (A, complemento) |
| Estabilidade | posições mudam, mas há uma lista | menos de 1 chance em 100 de duas execuções darem a mesma lista (ChatGPT e Google IA juntos; EUA presumido); 23% de coincidência entre repetições em busca local | F23, F21 (B) |
| Medição pelo dono do site | Search Console inclui o tráfego dos recursos de IA no relatório de desempenho | **não há painel** para dono de site nas fontes abertas; sobram registro do servidor, origem do tráfego e teste manual | F9 (A) · F1 (A, silêncio) |
| Anúncio | Google Ads | piloto no Brasil desde agosto de 2026, contas gratuitas e Go | F32 (C) |

---

## 8. Como medir presença sem ferramenta paga

| O que medir | Como | O que sustenta | Limite |
|---|---|---|---|
| **O robô de busca visitou?** | Nos registros de acesso do servidor, filtrar por `OAI-SearchBot`; conferir o IP contra `https://openai.com/searchbot.json` | F1, F2 (A) | exige hospedagem que entregue o registro bruto; visita não garante citação |
| **Alguém pediu a página dentro do ChatGPT?** | Filtrar por `ChatGPT-User` nos mesmos registros | F1 (A) | pelo menos metade das páginas visitadas entrou no cache, segundo F13 (B): visita não é citação |
| **Tráfego vindo do ChatGPT** | Sessões com `utm_source=chatgpt.com` **e**, por garantia, com origem `chatgpt.com` | parâmetro: **não conferido** (seção 3.2: a página de publishers hoje redireciona para outro artigo) | clique sem parâmetro e conversa sem clique ficam invisíveis |
| **O site aparece nas respostas?** | Roteiro manual de 30 perguntas, na conta do dono: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | F23, F21, F13 (B) | uma rodada é **amostra agregada**, não posição, e não mede uma pergunta isolada (regra abaixo) |
| **Presença no ecossistema Microsoft** | Relatório AI Performance do Bing Webmaster Tools | F5 (A) | cobre Copilot e Bing; ChatGPT não é nomeado; exige conta |

**Regra de medição (texto igual em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`,
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` e
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`):**

1. **Rodada mensal das 30 perguntas:** uma execução de cada pergunta, logado, em chat temporário, todas no mesmo dia.
   É uma **amostra agregada**: responde "em quantas das 30 o site ou a empresa aparece". **Ela não mede uma pergunta
   isolada.**
2. **Obrigatório, todo mês:** um subconjunto fixo de **6 perguntas** (1, 2, 12, 13, 16 e 29) repetido **5 vezes, em
   dias diferentes**, no mesmo perfil da rodada (30 execuções a mais por mês); e uma **subamostra deslogada** (janela
   anônima) das mesmas 6, **uma vez**.
3. **Limite declarado:** a SparkToro/Gumshoe dá como orientação prática repetir cada pergunta "usually at least
   60-100X" e tirar a média
   (https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/,
   28/01/2026, lida em 13/11/2026). É opinião prática dos autores, não resultado medido — a mesma página lista "quantas
   execuções bastam" como questão em aberto; a fonte é classe B de vendedor (a Gumshoe vende monitoramento de IA).
   **Este roteiro não atinge esse número:** as 6 execuções logadas por pergunta do subconjunto (1 da rodada mais 5
   repetições) mostram o tamanho do ruído; não estimam com precisão a frequência de uma pergunta.
4. **"API ≠ aplicativo":** uma B (Resoneo) apoia; os autores da SparkToro tratam como questão em aberto; não é
   consenso.

**Por que mensal** (motivos, com a classe de cada fonte): o sistema muda em escala de semanas — o campo de origem sumiu
em 21/07/2026 (F13, B); as citações ao Reddit caíram 88% em seis meses nos EUA (F19, B); a troca do modelo padrão em
agosto de 2026 vem de F18, que é **classe D** e entra só como alegação. Rodar as 30 mais de uma vez por mês, com uma
execução por pergunta, custa horas do dono e não melhora a medida de nenhuma pergunta: por isso o esforço extra vai
para a repetição do subconjunto (item 2 da regra).

**Limites que valem para qualquer medição manual:**

1. **A resposta muda a cada execução.** Menos de 1 em 100 de repetir a mesma lista (F23); 23% de coincidência em busca
   local (F21). O que é estável é a **frequência** com que um nome aparece ao longo de muitas execuções, não a ordem.
2. **Conta e modo mudam a origem dos resultados.** Gratuita instantânea puxa mais do índice próprio; paga com raciocínio,
   mais do Google raspado (F13). Sobre sessão deslogada: no estudo da Ahrefs (F19), que **só tem sessões gratuitas
   deslogadas**, 14,4% das respostas **continham buscas derivadas** — pela releitura do verificador independente, a
   Ahrefs corrigiu a própria frase: o número não é "14,4% buscaram na web". Como o estudo não tem sessão logada, ele **não permite dizer** que deslogado busca menos
   que logado: é o que a subamostra deslogada do roteiro observa.
3. **"API ≠ aplicativo":** uma B (Resoneo) apoia; os autores da SparkToro tratam como questão em aberto; não é
   consenso. O dado da Resoneo (F13): o modelo "puro" repete buscas em 61–71% dos casos, contra 0–17% no produto. A
   SparkToro (F23) lista a pergunta como aberta. Isso dá apoio parcial à parte "testar à mão" da tática 4.10 (F36); a
   parte "deslogado" **não** é sustentada: deslogado é só um dos perfis; a parte "uma vez por mês" só vale como
   amostra agregada (item 1 da regra).
4. **Memória e localização alteram a busca**: com a memória ligada, memórias salvas podem entrar na reescrita; sem
   bairro na pergunta, a cidade vem do endereço IP — conferido na ajuda oficial da OpenAI
   (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão
   principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). O **tamanho** do efeito:
   não sei. Por isso o roteiro usa chat temporário, escreve o bairro na pergunta e anota a rede.

**O que registrar:** data, hora, conta, modelo exibido, rede (rede de casa, rede móvel ou VPN), se buscou na web,
empresas citadas, domínios e tipos de fonte, mapa ou cartões, menção a licença ou vigilância sanitária, presença de
intermediário, observações. Cabeçalho pronto no roteiro.

---

## 9. Implicações para o desenho (item 6) e o protótipo (item 7)

| # | O que fazer | Fonte que sustenta | Classe | Situação |
|---|---|---|---|---|
| 1 | `robots.txt` permitindo o OAI-SearchBot (bloco abaixo) | F1 | A | **regra** |
| 2 | Hospedagem, CDN e firewall sem bloqueio aos IPs publicados da OpenAI; conferir depois de qualquer "proteção contra robôs" | F1, F2 | A | **regra** |
| 3 | Não bloquear o `ChatGPT-User` (é a visita que lê a página quando o usuário pede) | F1 (o que ele é) + F13 (alimenta o cache de leitura) | A + B | regra, com limite: uma só B sobre o efeito |
| 4 | `GPTBot`: liberar ou bloquear **não muda** a presença na busca | F1 | A | decisão do dono; padrão adotado: liberar (o site não tem conteúdo a proteger). **Premissa**, não evidência |
| 5 | Conteúdo principal no HTML que o servidor entrega, sem depender de JavaScript | F25 | B de 2024, **pode estar desatualizada**; OpenAI não documenta | hipótese forte e sem custo: o protótipo já é HTML e CSS puros |
| 6 | Abrir o corpo da página com o H1 e uma frase que diga o quê, onde e quem (o índice guardaria cerca de 200 caracteres do início do corpo; o H1 entrou em 83,6% dos trechos, 387 de 463) | F13 | uma B; o estudo **não testou** se isso aumenta citação | **hipótese** |
| 7 | Tudo o que importa (CNPJ, licença, órgão, região atendida, preço com fonte) em **texto visível**, não só em dados estruturados (o JSON-LD seria descartado na leitura sob demanda) | F13 | uma B | **hipótese** para o ChatGPT. Dados estruturados coerentes seguem valendo pelo Google (guia (a)) |
| 8 | `sitemap.xml` com `lastmod` verdadeiro | F6, F4 (as duas de 2025: **podem estar desatualizadas**) | A **para o Bing**; a OpenAI não cita sitemap | regra para o Bing; **hipótese** para o ChatGPT |
| 9 | Cadastro no Bing Webmaster Tools e IndexNow | F4 (2025: **pode estar desatualizada**), F5, F7 | A para Bing e Copilot | papel no ChatGPT **disputado**; exige conta: fica pronto para o dono, fora da rodada |
| 10 | Página "quem somos" verificável: responsável pelo site, o que o site é (intermediário que não executa o serviço), critérios de seleção das licenciadas, como conferir a licença; CNPJ por escolha de desenho | decorre de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`: quadro de vereditos, **linha 30** (site de terceiro: permitido com condição, "site declarado intermediário") e conclusão (iii), **linhas 246–251**, que o próprio item 2 marca como **inferência**, não frase de norma; pelas **linhas 236–237**, CNPJ **não** é exigido na propaganda (exibi-lo é escolha de desenho). Apoio indireto: o ChatGPT cita mais fonte "oficial" (F19, EUA) | **premissa marcada** (inferência do item 2) + B indireta | **premissa de desenho**, igual à do guia (c), seção 7.1; **não é regra legal conferida**. Como fator de citação no ChatGPT é **hipótese** |
| 11 | Uma página por serviço (praga) | F26; F22 | C + B de 2024 | **hipótese** |
| 12 | O site se apresenta como **lista de licenciadas com critério exposto**, não como "a melhor dedetizadora" | F26 (listas de terceiros no topo, opinião); F19 (comparações citam mais fonte não oficial); tática 4.5 de F36 | C + B indireta + D | **hipótese**; coincide com a restrição de propaganda |
| 13 | Em cada página, data de atualização visível, faixa de preço com fonte e o ano corrente quando for verdadeiro | F19 ("2026" em 22,9% e "price" em 8,9% das buscas derivadas, em inglês) | B indireta | **hipótese** |
| 14 | Páginas das licenciadas parceiras: orientar (com autorização delas) presença correta nas bases que o ChatGPT de fato citar no teste | F20, F21 (EUA, Reino Unido, Austrália) | B de outro país | **hipótese** até o roteiro mostrar quais bases aparecem em São Paulo; depende de contato com terceiros: **fora da rodada** |
| 15 | Hospedagem que entregue o registro de acesso bruto (para ver `OAI-SearchBot` e `ChatGPT-User`) | F1 | A | requisito de medição |
| 16 | Medição: guardar `utm_source` e a origem da visita em cada lead | seção 3.2 (a página de publishers hoje redireciona para outro artigo; o complemento não cobre) | **não conferido** | hipótese barata |
| 17 | Página de menos de 4 MB | F13 | uma B | trivial no protótipo |
| 18 | Não gastar esforço com `llms.txt` | nenhuma fonte aberta da OpenAI diz que seus robôs consomem o `llms.txt` de sites de terceiros. A página dos robôs (F1) traz um link para o `llms.txt` **do próprio site de documentação** (visto pelo verificador independente); não diz que os robôs leem esse tipo de arquivo nos sites que visitam | A (silêncio sobre o uso) | sem base para incluir |
| 19 | Anúncio no ChatGPT | F32 | C | fora da rodada (anúncio pago) |

**Bloco sugerido para o `robots.txt` do protótipo** (arquivo local; nada é publicado):

```
# Busca do ChatGPT: permitir para poder ser citado
User-agent: OAI-SearchBot
Allow: /

# Visita a pedido de um usuário do ChatGPT
User-agent: ChatGPT-User
Allow: /

# Treino de modelos: nao afeta a busca; decisao do dono (padrao: permitir)
User-agent: GPTBot
Allow: /

# Demais robos (inclui Googlebot e Bingbot)
User-agent: *
Allow: /

Sitemap: https://EXEMPLO.example/sitemap.xml
```

Para tirar o site do treino sem sair da busca, trocar só a linha do `GPTBot` por `Disallow: /` (F1, classe A). Mudança
no `robots.txt` leva cerca de 24 horas para valer na busca (F1).

### 9.1 Vereditos sobre as táticas do artigo do dono (F36) que o guia (c) remete a este arquivo

O guia (c) (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, seção 6) deixa para cá a parte
"ChatGPT" das táticas 4.1, 4.2, 4.3, 4.8 e 4.10. As táticas 4.2, 4.3 e 4.10 já têm veredito nas seções 1.5, 6 e 8. As
duas que faltavam:

| # | Tática do exemplo | Veredito para o ChatGPT | Base (fontes já listadas neste arquivo) |
|---|---|---|---|
| 4.1 | Sem SEO não há o que a IA achar; a IA vem depois do SEO | **Apoiada em parte; não é consenso.** O que é A: sem rastreio não há citação — o site precisa permitir o `OAI-SearchBot` e os IPs publicados (F1; ajuda oficial da OpenAI, complemento). O que é uma B: parte dos resultados chega do Google por raspadores, sobretudo em conta paga com raciocínio, e aí ranquear no Google importa (F13). O que pesa contra tratar "SEO do Google" como caminho suficiente: em conta gratuita instantânea, "empresas e lugares" vieram do índice próprio (F13), e as empresas citadas coincidem só 19–20% com as superfícies do Google (F21, B, país não declarado). **Leitura:** ser rastreável e indexável é condição (A); ir bem no Google ajuda em parte dos casos e não garante citação | F1 (A); ajuda da OpenAI (A, complemento); F13 (B); F21 (B) |
| 4.8 | O Reddit pesa de forma diferente por motor e cai no ChatGPT; comentar nos tópicos que o modelo lê | **Queda no ChatGPT: apoiada por duas B de empresas diferentes, fora do Brasil; não a classifico como consenso**, porque uma delas (F29) é de 2025 e não declara país. F19 (Ahrefs): citações ao Reddit caíram 88% de março a setembro de 2026, **EUA**. F29 (Semrush): de perto de 60% para cerca de 10% das respostas em setembro de 2025, país não declarado, **pode estar desatualizada**. São quedas em períodos diferentes, medidas por empresas diferentes. **No Brasil: não sei** — não há medição, e o único levantamento brasileiro aberto (F34, C) ainda põe Reddit e Wikipedia no topo entre dezembro de 2025 e julho de 2026. **Método de comentar nos tópicos:** permanece D (F36), sem estudo aberto que meça efeito | F19 (B); F29 (B, 2025); F34 (C); F36 (D) |

---

## 10. Fecho

### O que é consenso (classe A, ou duas B independentes)

1. A OpenAI tem robô próprio de busca; para um site poder ser citado, precisa **permitir o OAI-SearchBot** e não barrar
   os IPs publicados (F1, A).
2. Bloquear o GPTBot (treino) **não** tira o site da busca; as regras são independentes (F1, A).
3. Site que bloqueia o OAI-SearchBot some das respostas, mas pode aparecer como link de navegação (F1, A).
4. O ChatGPT-User age a pedido do usuário, pode não seguir o `robots.txt` e não decide a presença na busca (F1, A).
5. Mudança no `robots.txt` leva cerca de 24 horas (F1, A).
6. A OpenAI **declara** que a busca do ChatGPT "às vezes" faz parceria com outros provedores de busca (a Microsoft é a
   única nomeada, pela declaração de privacidade), usa a localização geral inferida do endereço IP e, com a memória
   ligada, pode usar memórias salvas na reescrita da busca; e que as listagens de empresas próximas vêm de provedores
   terceiros que ela não nomeia — conferido na ajuda oficial da OpenAI
   (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão
   principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). Classe A, com essa
   ressalva. *(Este item substitui "a OpenAI mantém índice próprio", que saiu do consenso: ver "indício forte" abaixo.)*
7. As respostas **variam a cada execução**; posição não é métrica, frequência é (F23 e F21, duas B independentes).
8. Em inglês, em 2026, os dados locais do ChatGPT vêm, entre outras fontes, de **plataformas de avaliação e
   diretórios, entre elas o Yelp**: o Yelp aparece entre as fontes citadas na amostra de EUA, Reino Unido e Austrália (F20, B) e é uma
   das alimentações identificadas no tráfego, ao lado de TripAdvisor e Google Maps (F13, B independente, que não dá a
   participação de cada uma). **Vale para esses países, não para o Brasil.** Que o Yelp esteja "à frente" **não** é
   consenso: ver "indício forte" abaixo.
9. O ChatGPT reescreve a pergunta em buscas próprias (ajuda oficial da OpenAI, A — complemento, mesma ressalva do
   item 6; F19, B. F17 é B fraca e não conta).
10. O Bing Webmaster Tools, o sitemap e o IndexNow funcionam como descrito **para o Bing e o Copilot** (F4–F7, A; F4 e
    F6 são de 2025: **podem estar desatualizadas**).

### Indício forte, não consenso (uma B, ou B de um só publicador, mais inferência)

1. **A OpenAI mantém índice próprio.** Uma B (F13) e inferência a partir de F1, que descreve o robô e não um índice;
   F15–F16 concordam, mas são classe D. Não cumpre "A ou duas B independentes".
2. **O Yelp é a principal fonte local do ChatGPT em inglês** ("à frente", 80% das respostas, cerca de 61% das
   citações a terceiros). Vem só de F20 — **uma B de vendedor**: a BrightLocal vende cadastro em diretórios, e F21 é da
   mesma empresa, logo não é uma segunda B independente. F13 confirma que o Yelp é **uma** das alimentações, sem
   participação. EUA, Reino Unido e Austrália; não vale para o Brasil.
3. **Resultados do Google chegam por raspadores terceiros** (seção 1.5): uma B (F13), uma C (F11) e uma D (F15).

### O que é disputado

1. **Bing × Google × índice próprio como origem dos resultados.** Uma B de 2026 mostra índice próprio mais Google
   raspado e nenhum Bing nas contas comuns (F13); a Microsoft dizia em 2025 que o Bing alimenta o ChatGPT (F4, **pode
   estar desatualizada**); a OpenAI declara só que "às vezes" faz parceria com outros provedores de busca e remete à
   declaração de privacidade da Microsoft — conferido na ajuda oficial da OpenAI
   (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão
   principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). Ela **não** diz quais
   são todos os provedores, em que proporção entram, nem cita o Google ou um índice próprio.
2. **"Ele busca no Google"** (F36, tática 4.2): apoiada em parte (seção 1.5), não declarada pela OpenAI.
3. **Quantas buscas o ChatGPT faz por pergunta**: de 1,6 a mais de 7 conforme estudo, modelo e plano (F17, F18, F19).
4. **Foursquare** como base local: alegações sem método de um lado; contestação que não consegui abrir do outro.
5. **Se os robôs da OpenAI executam JavaScript em 2026.**
6. **Se o `noindex` é respeitado**: a ajuda diria que sim — **não conferido**: a página de publishers deu 403 à
   ferramenta e, no navegador, redireciona para outro artigo (complemento); uma medição diz que o cache o ignora (F13).
7. **Quanto o perfil de empresa do Google pesa no ChatGPT**: um estudo diz que ele "quase não usa" o perfil e coincide
   só 19–20% com o Google (F21); outro mostra dados do Google Maps chegando por terceiros e links de perfil do Google
   dentro de registros do Yelp (F13).

### O que não sei

1. O que a OpenAI diz **hoje** sobre `utm_source=chatgpt.com`, `noindex`, "só link e título" e o Bing em contas
   Enterprise/Edu: as páginas deram 403 ou redirecionam (seção 3.2). **Deixou de estar aqui** o que o complemento
   conferiu na ajuda oficial (provedores parceiros, reescrita, memória, localização por IP), lido só pela sessão
   principal — o verificador independente recebeu 403. Dentro disso, segue sem resposta: **quais** são os provedores
   além da Microsoft, se "Microsoft" quer dizer Bing, e que precisão tem a localização por IP.
2. **Quais fontes o ChatGPT cita para dedetização em São Paulo, em português.** Nenhum estudo; o roteiro mede.
3. Se o Yelp ou outra base licenciada cobre dedetizadoras paulistanas.
4. As regras de elegibilidade do Bing Places e se barram intermediário (página vazia na ferramenta).
5. Se o relatório de IA do Bing inclui citações feitas dentro do ChatGPT.
6. Como o modo agente e o navegador da OpenAI se identificam num site.
7. Se existe canal para enviar site ou sitemap à OpenAI.
8. Se anunciante pequeno já consegue comprar anúncio no ChatGPT no Brasil, e a que custo.
9. Qual fração dos moradores de São Paulo usa conta gratuita, paga ou nenhuma — o que decide qual "encanamento" importa.
10. O efeito real de cada hipótese da seção 9 sobre a chance de ser citado: nenhum estudo aberto testou causa.
11. **Quanto as avaliações pesam** (nota, quantidade, texto) para uma empresa ser citada pelo ChatGPT. Só há F35 (D) e
    F26 (C); nenhuma A, nenhuma B (seção 5.3).
12. Se o Reddit perdeu peso no ChatGPT também **no Brasil** (seção 9.1, tática 4.8).
13. Quantas execuções por pergunta bastam para medir a frequência de uma pergunta: a SparkToro/Gumshoe (F23) lista como
    questão em aberto e dá "usually at least 60-100X" como orientação prática; o roteiro não atinge isso (seção 8).

### Fontes que tentei abrir e não abriram

| Fonte | Endereço | O que aconteceu |
|---|---|---|
| OpenAI, ajuda "ChatGPT search" | https://help.openai.com/en/articles/9237897-chatgpt-search (também `/articles/9237897`, a versão `pt-br` e `help-lb.openai.com`) | 403 na ferramenta de leitura, para o subagente e para o verificador independente. **Aberta depois pela sessão principal no navegador** (13/11/2026, 20:37), no endereço https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt: ver o complemento, no alto do arquivo |
| OpenAI, perguntas de publishers e desenvolvedores | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq (e a variante `.json`) | 403 na ferramenta; no navegador da sessão principal, redireciona para um artigo sem relação (complemento). Segue **não conferida** |
| OpenAI, anúncio da busca | https://openai.com/index/introducing-chatgpt-search/ | 403 |
| OpenAI, descoberta de produtos | https://openai.com/chatgpt/search-product-discovery/ | 403 |
| OpenAI, anúncios no ChatGPT | https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/ | 403 |
| OpenAI, lista de subprocessadores | https://openai.com/policies/sub-processor-list/ | 403 |
| Cópia de arquivo das páginas de ajuda | `web.archive.org` | a ferramenta não acessa esse domínio |
| Bing, diretrizes para webmasters | https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | veio só o título (texto carregado por JavaScript) |
| Bing Places, ajuda e diretrizes | https://www.bing.com/forbusiness/help/ · `…/dataQualityGuidelines` · `…/businessesWithoutPhysicalStore` | vieram sem texto |
| Search Engine Land (SerpApi; acordo com o Yelp; busca local do ChatGPT) | https://searchengineland.com/openai-chatgpt-serpapi-google-search-results-461226 · https://searchengineland.com/openai-yelp-deal-483326 · https://searchengineland.com/how-does-chatgpt-conduct-local-searches-454894 | 403 |
| Axios, acordo Yelp–OpenAI | https://axios.com/2026/07/23/yelp-reviews-chatgpt-geo-partnership | 403 |
| NPR, julgamento do Google | https://www.npr.org/2025/04/29/nx-s1-5377353/google-antitrust-remedies-trial-ai | tempo esgotado |
| Estudo que contesta o Foursquare | https://www.steadydemand.com/?p=4927 | conexão recusada (duas tentativas) |
| Matéria sobre anúncios do ChatGPT no Brasil | https://www.mercadoeeventos.com.br/?p=726414 | 403 |
| Conversion, compartilhamento de localização | https://www.conversion.com.br/?p=52982 | caiu na página inicial |
| The Information (original sobre a SerpApi) | — | pago; não tentado |

Não abertos por escolha (só apareceram em resultado de busca e **não** sustentam nenhuma linha acima): o estudo da
Nectiv sobre buscas por pergunta, as postagens do Bing de junho e outubro de 2026 sobre o relatório de IA, o relatório
completo do índice da SOCi e o estudo da Ranqia na origem.
