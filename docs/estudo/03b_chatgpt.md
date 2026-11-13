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
- **Aviso central:** as duas páginas de ajuda da OpenAI que mais importam (`help.openai.com`) e todo o `openai.com`
  devolveram **403** à ferramenta. O que elas diriam aparece numa tabela à parte (seção 3.2), marcada **não conferido /
  não conclusivo**, com o endereço para o dono abrir no navegador. Nada dali entrou como classe A.

## Legenda das classes (regra de evidência de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`)

| Classe | O que é aqui | Vira regra? |
|---|---|---|
| **A** | Documentação oficial lida na página: OpenAI sobre os sistemas da OpenAI; Microsoft sobre o Bing; Google sobre o Google | sim |
| **B** | Estudo com amostra, método e dado expostos. Quase todos são de empresas que vendem ferramenta ou serviço de SEO: o conflito vai anotado em "quem ganha" | sim, com o limite da amostra e o país |
| **C** | Relato sem método de estudo: reportagem, depoimento relatado pela imprensa, pesquisa de opinião com praticantes | só hipótese |
| **D** | Vendedor (ferramenta, agência, curso) sem amostra ou método expostos, mesmo com caso mostrado | não; "alegação" |

"Consenso" = classe A, ou duas B independentes. Sobre respostas de IA, fonte anterior a 2026 leva **"pode estar
desatualizada"**. Número de outro país vai com o país ao lado.

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
| F10 | Google · comunicado do processo contra a SerpApi | https://blog.google/technology/safety-security/serpapi-lawsuit/ | 19/12/2025 | A só para "o Google processou e alega isto"; é parte no processo | Google |
| F11 | Search Engine Roundtable (B. Schwartz) · relato da reportagem do The Information sobre SerpApi | https://www.seroundtable.com/chatgpt-serpapi-scrape-google-39989.html | 25/08/2025 | C (reportagem de segunda mão; o original, pago, não foi aberto) · **pode estar desatualizada** | veículo do setor |
| F12 | PYMNTS/CPI · relato da Reuters sobre o depoimento do chefe do ChatGPT no julgamento do Google | https://www.pymnts.com/cpi-posts/openai-eyes-chrome-if-doj-forces-google-to-sell-browser-exec-testifies/ | 22/04/2025 | C (depoimento relatado pela imprensa) · **pode estar desatualizada** | — |
| F13 | Resoneo · estudo de engenharia reversa da recuperação do ChatGPT | https://think.resoneo.com/chatgpt-retrieval/ | julho/2026, atualizado em agosto/2026 | B | Resoneo, consultoria francesa de SEO/GEO; distribui a extensão usada na captura |
| F14 | Search Engine Journal (M. Southern) · matéria sobre o estudo da Resoneo | https://www.searchenginejournal.com/chatgpts-search-index-serves-small-sites-too-data-shows/585388/ | 11/08/2026 | C (reportagem) | veículo do setor |
| F15 | Peec · "ChatGPT search result providers" | https://docs.peec.ai/research/chatgpt-search-result-providers | setembro/2026 | D (não declara amostra, países nem período de coleta) | Peec, ferramenta de monitoramento de presença em IA (a página não diz o que vende; informação não conferida nela) |
| F16 | Peec · "ChatGPT has its own search index — the Labrador family" | https://docs.peec.ai/research/chatgpt-own-search-index-labrador | setembro/2026 | D (mesmo motivo) | idem |
| F17 | Peec · "Fan-outs per prompt by engine" | https://docs.peec.ai/research/fanouts-per-prompt-by-engine | maio/2026 (dados de 1–21/04/2026) | B (amostra e período expostos; país não) | idem |
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

O que a OpenAI diria sobre "provedores de busca terceiros" e sobre o Bing está nas páginas de ajuda que **não abriram**
(seção 3.2). Sem elas, a frase "a OpenAI declara que usa o Bing" **não tem fonte primária conferida nesta rodada**.

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
| Amostra: 1.249 respostas com busca (682 no modo instantâneo, 567 no modo de raciocínio), cerca de 88 mil resultados, 26,9 mil páginas, 6,4 mil domínios; contas gratuitas, pagas e deslogada, por VPN; **corpus majoritariamente em inglês; sem recorte por país** | F13 | B |
| Conta **gratuita, modo instantâneo** (julho; 1.793 resultados): 63,6% índice próprio, 34,7% Google raspado, 1,6% outro raspador | F13 | B |
| Conta **paga, modo de raciocínio** (julho; 16.407 resultados): 23,6% índice próprio, 74,6% Google raspado. Em agosto: 24,7% × 75,3% | F13 | B |
| Conta **gratuita, modo de raciocínio** (agosto): 74,7% índice próprio, 22,2% de um segundo raspador (`oxylabs`), 3,1% Google | F13 | B |
| Por tipo de pergunta, no gratuito instantâneo, **"empresas e lugares" vieram 100% do índice próprio**; no pago com raciocínio, cerca de 95% do Google raspado. O estudo avisa que as médias dependem da mistura de perguntas | F13 | B |
| Cerca de **um terço** das perguntas repetidas trocou de encanamento: o roteamento não é determinístico | F13 | B |
| O índice próprio **não é o Bing com outro nome** (títulos mais longos do que o Bing guarda). Um "encanamento Bing" foi visto por outro pesquisador numa conta de plano Team em junho; a Resoneo **nunca** o viu nas contas dela | F13 | B |
| A OpenAI **não confirmou** esses rótulos; a matéria que cobriu o estudo registra que não houve comentário e que a documentação dos robôs não descreve o índice próprio | F14 | C |
| Outro vendedor leu o mesmo campo entre 21/05 e 21/07/2026 e descreve índice próprio "em família" (web, notícias, local, compras…) mais ao menos oito provedores externos; diz que o Bing aparece sobretudo em sessões de pesquisa aprofundada. **Não declara amostra** | F15, F16 | D |
| Em fevereiro de 2025, 87% das citações da busca do ChatGPT coincidiam com os 20 primeiros do Bing e 56% com o Google (EUA presumido; cerca de 100 consultas, quase todas com "melhor"/"top"; os autores chamam de "direcional") | F24 | B · **pode estar desatualizada** |

### 1.5 Conclusão sobre o índice

- **Consenso (A + B):** a OpenAI rastreia a web com robô próprio (`OAI-SearchBot`) para alimentar a busca do ChatGPT
  (F1) e mantém índice próprio (F13; F15–F16 como alegação concordante).
- **Indício forte, não consenso:** resultados do **Google** chegam ao ChatGPT por raspadores terceiros, em proporção que
  muda com o plano e o modo. Sustentação: uma B (F13), uma reportagem (F11) e alegação de vendedor (F15). A OpenAI não
  declara; o Google processa um dos raspadores (F10). A tática 4.2 do artigo do dono ("ele busca no Google", F36) fica
  **parcialmente apoiada e mal formulada**: não é o ChatGPT consultando o Google, e sim resultados do Google comprados de
  terceiros, sobretudo em contas pagas com raciocínio — e, em conta gratuita, pergunta sobre empresa e lugar veio do
  índice próprio.
- **Disputado:** o papel do **Bing hoje**. A favor: a Microsoft o afirmava em junho de 2025 (F4), o depoimento de abril
  de 2025 (F12), um estudo de fevereiro de 2025 (F24) e, não conferida, a ajuda da OpenAI (seção 3.2). Contra: o estudo
  de 2026 não vê o Bing nas contas comuns (F13). Tratar "estar no Bing" como sinônimo de "estar no ChatGPT" **não se
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
  que não abriu (seção 3.2): **não conclusivo**.

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
| A OpenAI declara fatores de escolha de fonte? | Na página dos robôs, **não**. Na API, só diz que o modelo decide se busca: "Like any other tool, the model can choose to search the web or not based on the content of the input prompt." | F1, F3 | A |
| Existe anúncio no ChatGPT? | Sim: há um robô só para validar páginas de anúncios (F1). No Brasil, piloto anunciado em 04/08/2026 para contas gratuitas e Go, maiores de 18 anos, anúncios marcados como patrocinados; segundo a OpenAI, relatada pela matéria, não influenciam as respostas (F32) | F1 (A) · F32 (C) |
| Dá para pagar por posição na resposta? | Nada nas fontes abertas indica que sim; a negativa da OpenAI só foi lida por reportagem (F32). A página oficial de anúncios deu 403: **não conclusivo** | F32 | C |

### 3.2 Visto só no trecho devolvido pela ferramenta de busca — página **não aberta (403)**, **não conferido**

Estas linhas **não são evidência**. Servem para o dono conferir em cinco minutos no navegador.

| O que a página diria | Página (abrir no navegador) |
|---|---|
| A busca do ChatGPT às vezes recorre a provedores de busca parceiros e reescreve a pergunta em uma ou mais consultas dirigidas; não repassa IP nem dados da conta ao provedor | https://help.openai.com/en/articles/9237897-chatgpt-search |
| Em contas Enterprise/Edu, consultas desassociadas podem ir ao **Bing** | https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu |
| A classificação usa "vários fatores"; não há como garantir posição | https://help.openai.com/en/articles/9237897-chatgpt-search |
| Para entrar em resumos e trechos, não bloquear o OAI-SearchBot; página bloqueada pode aparecer só com link e título; para evitar, usar `noindex` (e o robô precisa conseguir ler a página para ver a marca) | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq |
| O ChatGPT acrescenta `utm_source=chatgpt.com` aos links de saída | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq |
| Compartilhamento de localização do aparelho, opcional e desligado por padrão (março de 2026) | https://help.openai.com/en/articles/6825453-chatgpt-release-notes |
| Anúncio de lançamento da busca (31/10/2024): provedores terceiros e conteúdo de parceiros | https://openai.com/index/introducing-chatgpt-search/ |

**Veredito da seção:** `utm_source=chatgpt.com`, a regra do `noindex`, "só link e título" e a menção a provedores
parceiros ficam **não conclusivos** até alguém abrir as páginas.

---

## 4. O Bing como caminho

| Afirmação | Fonte | Classe |
|---|---|---|
| O Bing Webmaster Tools é gratuito ("Free and full of powerful features"); aceita importar o site do Google Search Console ("Import your site from Google Search Console"); recebe sitemap ("Submit and monitor your sitemap") e confere atualização ao menos uma vez por dia | F4 | A · página de 2025 |
| O IndexNow avisa os buscadores participantes quando uma página muda ("Instantly notify Bing and other search engines participating in IndexNow"); exige uma chave em arquivo de texto hospedado no site e o envio das URLs; **não garante** rastreio nem indexação; a página não cita OpenAI | F4, F7 | A |
| Sitemap continua sendo o sinal de base para cobertura; `lastmod` deve refletir a mudança real do conteúdo; sitemap e IndexNow se somam | F6 | A · página de 2025 |
| Desde 10/02/2026 existe o relatório **AI Performance** (prévia pública): total de citações, páginas citadas, "consultas de fundamentação", tendência. Cobre Copilot, resumos de IA do Bing e parceiros não nomeados. Aviso: "This reflects how often pages are cited, not page importance, ranking, or placement" | F5 | A |
| Em junho e outubro de 2026 o relatório ganhou novas visões (intenções, tópicos, participação de citações) | só resultado de busca (blogs.bing.com), não aberto | não conferido |
| O relatório **não diz** se inclui o ChatGPT; não tem dado de clique na leitura feita | F5 | A (silêncio) |

**Bing Places for Business (perfil de empresa do Bing).** As páginas oficiais de ajuda
(`https://www.bing.com/forbusiness/help/`, `…/dataQualityGuidelines`, `…/businessesWithoutPhysicalStore`) carregam o
texto por JavaScript e vieram **vazias** na ferramenta. Elegibilidade, país e a regra para intermediário: **não
conclusivo**. O trecho devolvido pela busca (não conferido) diz que o perfil exige endereço físico visitável ou área de
atendimento onde a equipe vai ao cliente, com endereço válido para verificação — a mesma lógica que vedou o perfil do
Google ao gerador de leads em
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos, linhas 24–27). **Premissa
adotada:** tratar como vedado para o gerador de leads até prova em contrário; o caminho legítimo é o perfil ser da
licenciada. Criar ou reivindicar perfil está fora da rodada de qualquer modo.

**Quanto o Bing vale para o ChatGPT:** disputado (seção 1.5). Vale com certeza para o Bing e o Copilot (A). É barato,
mas exige conta: ação do dono, fora desta rodada.

---

## 5. De onde vêm os dados de empresa local e de mapa

### 5.1 O que a OpenAI declara

Nada foi **conferido** em fonte primária: a ajuda e os anúncios deram 403. **Não conclusivo.** A página dos robôs (F1)
não fala de resultados locais.

### 5.2 Reportagem

| Afirmação | Fonte | Classe |
|---|---|---|
| O Yelp licencia avaliações, notas, fotos e dados de empresas à OpenAI; marca e links do Yelp aparecem junto; previsto o pedido de orçamento do Yelp dentro do ChatGPT; acordo não exclusivo; valores não divulgados. A matéria não nomeia países | F30 (repassa o Axios) | C |
| Desde março de 2026 o usuário pode compartilhar a localização do aparelho; é opcional e vem desligado. Um teste citado achou resultados "perto de mim" a cerca de 45 minutos de distância | F31 | C |

### 5.3 Estudos com dado — todos de fora do Brasil

| Afirmação | Amostra · país · data | Fonte | Classe |
|---|---|---|---|
| Os resultados locais chegam por alimentações reconhecíveis pelo formato do identificador: **Yelp, TripAdvisor e Google Maps**. Quase um em cada cinco registros rotulados Yelp trazia link copiado de um perfil de empresa do Google. No modo instantâneo a resposta sobre empresas vem com **mapa**; no modo de raciocínio o mapa some | 1.249 respostas · majoritariamente inglês, sem país · jul–ago/2026 | F13 | B |
| O **Yelp** apareceu em 80% das respostas do ChatGPT e recebeu 99.281 de 162.966 citações a domínios terceiros (cerca de 61%). Depois: TripAdvisor (10.227), OpenTable (9.147), BBB (4.247), Angie's List (1.768), Trustpilot (1.136), Yellow Pages (711), HomeAdvisor (705) | 60.970 checagens, cerca de 1.355 locais, 13 categorias · **EUA, Reino Unido, Austrália** · publicado em 26/08/2026 | F20 | B |
| O ChatGPT citou empresas em 33% das buscas (29,4% quando a empresa atende em domicílio); média de 4,1 empresas por resposta; 10% de respostas vazias; "quase não usa" o perfil de empresa do Google e se apoia em Yelp e Bing; coincide só 19–20% com as superfícies do Google; cerca de 53% das empresas citadas ficam a até 5 km | cerca de 200 mil buscas, cerca de 1.300 locais, 60 dias · país não declarado na página (o estudo irmão F20 é EUA/Reino Unido/Austrália) · 16/09/2026 | F21 | B |
| Em novembro de 2024: 58% das fontes eram sites das próprias empresas, 27% menções (Wikipedia à frente), 15% diretórios; Yelp, Facebook e Google Maps **não** apareciam | 800 buscas manuais, 20 setores, 20 cidades · **EUA** | F22 | B · **pode estar desatualizada** (o retrato de 2026 é outro) |
| O ChatGPT recomendaria 1,2% dos locais de redes; o pacote local do Google, 35,9%; nota média dos recomendados, 4,3 estrelas | 350 mil locais de 2.751 **redes com várias unidades** · país e método não declarados · 28/01/2026 | F35 | D |
| Especialistas apontam como fatores de visibilidade em IA: estar em listas "melhores de" feitas por terceiros; página dedicada a cada serviço; presença em domínios do setor; citações não estruturadas de qualidade; autoridade dos sites onde estão as avaliações | 47 especialistas, pesquisa de opinião · foco norte-americano · 06/11/2025 | F26 | C · **pode estar desatualizada** |
| "60–70% dos dados locais do ChatGPT vêm do Foursquare" | sem método localizado; um estudo de agosto de 2026 que contestaria o número não abriu | — | **não sei** (alegação sem fonte aberta) |
| "O ChatGPT lê Bing Places" / "tem integração direta com o Bing" para dados locais | sem número nem método | F28 | D |
| Listas de diretórios que o ChatGPT "disse" usar quando perguntado | resposta do próprio modelo, 2024 | F27 | D · desatualizada |

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
| Plataformas de orçamento | GetNinjas, Habitissimo, Triider, Cronoshare | análogas a Angi e HomeAdvisor em F20; já citadas em `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md` linhas 167–171 |
| Guias e listas telefônicas | Guia Mais, Apontador, TeleListas, Solutudo | análogos a Yellow Pages em F20 |
| Fontes oficiais e do setor | páginas da vigilância sanitária (estado e município), associações de controladores de pragas | o ChatGPT de 2026 busca mais fonte "oficial" (F19); pode pesar em pergunta sobre licença |
| Imprensa local | portais e jornais de bairro, matérias sobre golpe de dedetização | "menções" eram 27% das fontes em F22 |

---

## 6. Reescrita da pergunta em buscas ("fan-out")

| Afirmação | Amostra · país · data | Fonte | Classe |
|---|---|---|---|
| Na API, o modelo decide se busca ou não, e os modelos de raciocínio refinam a busca enquanto leem: "It can refine its searches as it reads results." A página não fala do aplicativo | — | F3 | A (para a API) |
| A ajuda do aplicativo diria que a pergunta é reescrita em uma ou mais consultas dirigidas | — | seção 3.2 | **não conferido** |
| ChatGPT: 2,1 buscas por pergunta (Perplexity 1,4; Grok 6,8) | cerca de 5 milhões de buscas derivadas · país não declarado · 1–21/04/2026 | F17 | B |
| Em respostas gratuitas e deslogadas, só **14,4%** continham buscas derivadas; nessas, média de 1,6 busca. O ano "2026" estava em 22,9% das buscas de setembro; "official" em 13,1%; "price" em 8,9%; o operador `site:` em 6,8% (75,9% dos mais comuns miravam o site da própria marca) | 66,6 milhões de respostas e 15 milhões de buscas · todos os países; análise de palavras em **inglês** · ago–set/2026 | F19 | B |
| Em perguntas factuais, 84,4% das respostas citaram ao menos uma fonte oficial; em perguntas de comparação, 68,3%. Sites oficiais: 63,4% das citações em factuais e 46,4% em comparações | 20 mil perguntas · **EUA** · 2026 | F19 | B |
| Citações ao Reddit caíram 88% em seis meses (março a setembro de 2026); Wikipedia, 80% | **EUA** · 2,4 a 3,8 milhões de respostas por mês | F19 | B |
| Com o modelo que virou padrão em agosto de 2026, perguntas resolvidas com uma só rodada de busca caíram de 94,0% para 43,5%; `site:` foi de 0,3% para 23% das buscas; fontes por pergunta de cerca de 12 para cerca de 24 | sem amostra declarada · ago/2026 | F18 | D |
| "De 2,17 para 7,61 buscas por pergunta" no modelo mais forte | relato de segunda mão; original não localizado | só resultado de busca | **não sei** |
| O ChatGPT reescreve a conversa em "duas a cinco buscas curtas" (tática 4.3 do artigo do dono) | — | F36 | D; **a ordem de grandeza é compatível** com F17 e F19 para o período até meados de 2026; o formato exato das buscas em português não foi medido |

**Leitura:** a reescrita existe (A para a API; B para o aplicativo). **Quantas** buscas e **com que palavras** varia com
o modelo, o plano e o mês: disputado. Para uma pergunta de serviço local em português: **não sei**.

---

## 7. O que difere do Google orgânico e dos resumos de IA do Google

Detalhe do lado Google nos guias (a) e (b) do item 3 (por exemplo
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`); aqui, só o contraste.

| Tema | Google orgânico e resumos de IA do Google | Busca do ChatGPT | Fonte · classe |
|---|---|---|---|
| Requisito para aparecer | "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."; a página precisa estar indexada e apta a trecho | permitir o OAI-SearchBot e não barrar seus IPs | F9 (A) · F1 (A) |
| Índice | um só, do Google | índice próprio **mais** resultados de terceiros (Google raspado; Bing em disputa), variando por plano e modo | F13 (B) |
| Robôs | Googlebot; o controle de uso em IA fora da busca é à parte | três robôs com funções separadas: busca, treino, visita a pedido do usuário | F9, F1 (A) |
| Reescrita da pergunta | os recursos de IA podem usar "query fan-out": "issuing multiple related searches across subtopics and data sources" | também reescreve; quantidade instável | F9 (A) · F17, F19 (B) |
| Dados de empresa local | perfil de empresa do Google, que o dono da empresa controla | **não há perfil de empresa próprio da OpenAI** nas fontes abertas; dados vêm de Yelp, TripAdvisor, Google Maps via terceiros e dos sites | F13, F20, F21 (B; fora do Brasil) |
| Coincidência das empresas citadas | — | só 19–20% de coincidência com as superfícies do Google | F21 (B) |
| Proximidade | — | 90% das empresas citadas dentro de um raio de 287 km no ChatGPT, contra 39–64 km no Google; cerca de 53% a até 5 km | F21 (B) |
| Localização do usuário | — | compartilhamento do aparelho opcional desde março de 2026; sem ele, o que o aplicativo usa: não conferido | F31 (C) |
| Memória e personalização | — | a resposta pode variar com a conta; efeito da memória sobre a busca: **não sei** (ajuda não aberta) | — |
| Estabilidade | posições mudam, mas há uma lista | menos de 1 chance em 100 de duas execuções darem a mesma lista (ChatGPT e Google IA juntos; EUA presumido); 23% de coincidência entre repetições em busca local | F23, F21 (B) |
| Medição pelo dono do site | Search Console inclui o tráfego dos recursos de IA no relatório de desempenho | **não há painel** para dono de site nas fontes abertas; sobram registro do servidor, origem do tráfego e teste manual | F9 (A) · F1 (A, silêncio) |
| Anúncio | Google Ads | piloto no Brasil desde agosto de 2026, contas gratuitas e Go | F32 (C) |

---

## 8. Como medir presença sem ferramenta paga

| O que medir | Como | O que sustenta | Limite |
|---|---|---|---|
| **O robô de busca visitou?** | Nos registros de acesso do servidor, filtrar por `OAI-SearchBot`; conferir o IP contra `https://openai.com/searchbot.json` | F1, F2 (A) | exige hospedagem que entregue o registro bruto; visita não garante citação |
| **Alguém pediu a página dentro do ChatGPT?** | Filtrar por `ChatGPT-User` nos mesmos registros | F1 (A) | pelo menos metade das páginas visitadas entrou no cache, segundo F13 (B): visita não é citação |
| **Tráfego vindo do ChatGPT** | Sessões com `utm_source=chatgpt.com` **e**, por garantia, com origem `chatgpt.com` | parâmetro: **não conferido** (seção 3.2) | clique sem parâmetro e conversa sem clique ficam invisíveis |
| **O site aparece nas respostas?** | Roteiro manual de 30 perguntas, na conta do dono: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | F23, F21, F13 (B) | uma rodada é **amostra**, não posição |
| **Presença no ecossistema Microsoft** | Relatório AI Performance do Bing Webmaster Tools | F5 (A) | cobre Copilot e Bing; ChatGPT não é nomeado; exige conta |

**Frequência recomendada: mensal, com as mesmas 30 perguntas.** Motivos: o sistema muda em escala de semanas (o campo de
origem sumiu em 21/07/2026 e o modelo padrão trocou em agosto de 2026 — F13, F18; as citações ao Reddit caíram 88% em
seis meses — F19); medir mais vezes custa horas do dono e, com uma execução por pergunta, só acrescenta ruído.

**Limites que valem para qualquer medição manual:**

1. **A resposta muda a cada execução.** Menos de 1 em 100 de repetir a mesma lista (F23); 23% de coincidência em busca
   local (F21). O que é estável é a **frequência** com que um nome aparece ao longo de muitas execuções, não a ordem.
2. **Conta e modo mudam a origem dos resultados.** Gratuita instantânea puxa mais do índice próprio; paga com raciocínio,
   mais do Google raspado (F13). Sessão gratuita deslogada busca menos (14,4% das respostas, F19).
3. **A API não reproduz o aplicativo** (F13: o modelo "puro" repete buscas em 61–71% dos casos, contra 0–17% no
   produto). Isso apoia a parte "testar à mão" da tática 4.10 (F36); a parte "deslogado" **não** é sustentada: deslogado
   é só um dos perfis.
4. **Memória e localização** podem alterar a resposta; o tamanho do efeito: não sei.

**O que registrar:** data, hora, conta, modelo exibido, se buscou na web, empresas citadas, domínios e tipos de fonte,
mapa ou cartões, menção a licença ou vigilância sanitária, presença de intermediário, observações. Cabeçalho pronto no
roteiro.

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
| 8 | `sitemap.xml` com `lastmod` verdadeiro | F6, F4 | A **para o Bing**; a OpenAI não cita sitemap | regra para o Bing; **hipótese** para o ChatGPT |
| 9 | Cadastro no Bing Webmaster Tools e IndexNow | F4, F5, F7 | A para Bing e Copilot | papel no ChatGPT **disputado**; exige conta: fica pronto para o dono, fora da rodada |
| 10 | Página "quem somos" verificável: CNPJ, responsável, o que o site é (intermediário), critérios de seleção das licenciadas, como conferir a licença | exigência de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos, linha 29); apoio indireto: o ChatGPT cita mais fonte "oficial" (F19, EUA) | restrição legal (A no item 2) + B indireta | **regra pelo item 2**; como fator de citação no ChatGPT é **hipótese** |
| 11 | Uma página por serviço (praga) | F26; F22 | C + B de 2024 | **hipótese** |
| 12 | O site se apresenta como **lista de licenciadas com critério exposto**, não como "a melhor dedetizadora" | F26 (listas de terceiros no topo, opinião); F19 (comparações citam mais fonte não oficial); tática 4.5 de F36 | C + B indireta + D | **hipótese**; coincide com a restrição de propaganda |
| 13 | Em cada página, data de atualização visível, faixa de preço com fonte e o ano corrente quando for verdadeiro | F19 ("2026" em 22,9% e "price" em 8,9% das buscas derivadas, em inglês) | B indireta | **hipótese** |
| 14 | Páginas das licenciadas parceiras: orientar (com autorização delas) presença correta nas bases que o ChatGPT de fato citar no teste | F20, F21 (EUA, Reino Unido, Austrália) | B de outro país | **hipótese** até o roteiro mostrar quais bases aparecem em São Paulo |
| 15 | Hospedagem que entregue o registro de acesso bruto (para ver `OAI-SearchBot` e `ChatGPT-User`) | F1 | A | requisito de medição |
| 16 | Medição: guardar `utm_source` e a origem da visita em cada lead | seção 3.2 | **não conferido** | hipótese barata |
| 17 | Página de menos de 4 MB | F13 | uma B | trivial no protótipo |
| 18 | Não gastar esforço com `llms.txt` | nenhuma fonte aberta da OpenAI o cita; F1 não o menciona | A (silêncio) | sem base para incluir |
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

---

## 10. Fecho

### O que é consenso (classe A, ou duas B independentes)

1. A OpenAI tem robô próprio de busca; para um site poder ser citado, precisa **permitir o OAI-SearchBot** e não barrar
   os IPs publicados (F1, A).
2. Bloquear o GPTBot (treino) **não** tira o site da busca; as regras são independentes (F1, A).
3. Site que bloqueia o OAI-SearchBot some das respostas, mas pode aparecer como link de navegação (F1, A).
4. O ChatGPT-User age a pedido do usuário, pode não seguir o `robots.txt` e não decide a presença na busca (F1, A).
5. Mudança no `robots.txt` leva cerca de 24 horas (F1, A).
6. A OpenAI mantém índice próprio (F1, A, por decorrência; F13, B).
7. As respostas **variam a cada execução**; posição não é métrica, frequência é (F23 e F21, duas B independentes).
8. Em inglês, em 2026, os dados locais do ChatGPT vêm em boa parte de **plataformas de avaliação e diretórios, com o
   Yelp à frente**: o Yelp esteve em 80% das respostas na amostra de EUA, Reino Unido e Austrália (F20, B) e é uma das
   alimentações identificadas no tráfego, ao lado de TripAdvisor e Google Maps (F13, B independente). **Vale para esses
   países, não para o Brasil.**
9. O ChatGPT reescreve a pergunta em buscas próprias (F17 e F19, duas B).
10. O Bing Webmaster Tools, o sitemap e o IndexNow funcionam como descrito **para o Bing e o Copilot** (F4–F7, A).

### O que é disputado

1. **Bing × Google × índice próprio como origem dos resultados.** Uma B de 2026 mostra índice próprio mais Google
   raspado e nenhum Bing nas contas comuns (F13); a Microsoft dizia em 2025 que o Bing alimenta o ChatGPT (F4); a OpenAI
   não confirma nada disso em fonte que eu tenha aberto.
2. **"Ele busca no Google"** (F36, tática 4.2): apoiada em parte (seção 1.5), não declarada pela OpenAI.
3. **Quantas buscas o ChatGPT faz por pergunta**: de 1,6 a mais de 7 conforme estudo, modelo e plano (F17, F18, F19).
4. **Foursquare** como base local: alegações sem método de um lado; contestação que não consegui abrir do outro.
5. **Se os robôs da OpenAI executam JavaScript em 2026.**
6. **Se o `noindex` é respeitado**: a ajuda diria que sim (não conferida); uma medição diz que o cache o ignora (F13).
7. **Quanto o perfil de empresa do Google pesa no ChatGPT**: um estudo diz que ele "quase não usa" o perfil e coincide
   só 19–20% com o Google (F21); outro mostra dados do Google Maps chegando por terceiros e links de perfil do Google
   dentro de registros do Yelp (F13).

### O que não sei

1. O que as páginas de ajuda da OpenAI dizem **hoje**, palavra por palavra, sobre provedores de busca, Bing,
   `utm_source=chatgpt.com`, `noindex`, memória e localização (403).
2. **Quais fontes o ChatGPT cita para dedetização em São Paulo, em português.** Nenhum estudo; o roteiro mede.
3. Se o Yelp ou outra base licenciada cobre dedetizadoras paulistanas.
4. As regras de elegibilidade do Bing Places e se barram intermediário (página vazia na ferramenta).
5. Se o relatório de IA do Bing inclui citações feitas dentro do ChatGPT.
6. Como o modo agente e o navegador da OpenAI se identificam num site.
7. Se existe canal para enviar site ou sitemap à OpenAI.
8. Se anunciante pequeno já consegue comprar anúncio no ChatGPT no Brasil, e a que custo.
9. Qual fração dos moradores de São Paulo usa conta gratuita, paga ou nenhuma — o que decide qual "encanamento" importa.
10. O efeito real de cada hipótese da seção 9 sobre a chance de ser citado: nenhum estudo aberto testou causa.

### Fontes que tentei abrir e não abriram

| Fonte | Endereço | O que aconteceu |
|---|---|---|
| OpenAI, ajuda "ChatGPT search" | https://help.openai.com/en/articles/9237897-chatgpt-search (também `/articles/9237897`, a versão `pt-br` e `help-lb.openai.com`) | 403 |
| OpenAI, perguntas de publishers e desenvolvedores | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq (e a variante `.json`) | 403 |
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
