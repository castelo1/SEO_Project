# Guia (c) — Respostas de IA: o que faz um site ser citado (serviço local, São Paulo)

- **Escopo:** recursos de IA do Google (Visão geral criada por IA / AI Overviews, Modo IA / AI Mode, Gemini) e, em
  menor profundidade, Perplexity, Copilot/Bing, Apple e Anthropic, mais o que é comum a todos. Caso de uso: site que
  capta contatos de quem procura dedetização em São Paulo.
- **O ChatGPT não está aqui:** tem guia próprio em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`.
- **Leitura das fontes:** sexta, 13/11/2026, das 19:48 às 20:11 (Brasília; `TZ=America/Sao_Paulo date`). Toda "data de
  leitura" abaixo é 13/11/2026.
- **Como li:** só busca e leitura de página pública. Nenhum assistente de IA foi aberto para teste. A ferramenta de
  leitura responde por meio de um modelo pequeno; por isso, trecho entre aspas só aparece quando a página oficial foi
  aberta e o trecho foi confirmado numa segunda chamada. O que foi lido uma vez só está em paráfrase, sem aspas.
- **Classes de evidência** (regra de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`):
  **A** documentação oficial lida na fonte (aqui: do próprio motor sobre o próprio produto) · **B** estudo com amostra
  e método expostos · **C** relato de praticante conferível · **D** vendedor de curso, ferramenta ou agência (entra
  como alegação). "B fraca" = há número, mas falta amostra, país ou método: **não vira regra**.
- **Datas:** sobre respostas de IA, fonte anterior a 2026 leva "pode estar desatualizada".
- **País:** quase todo estudo é dos Estados Unidos. Número de outro país fica com o país ao lado e não vale como
  número do Brasil.
- **Aviso de tamanho:** o guia é curto de propósito na parte de "táticas". O que tem fonte oficial é pouco e quase
  todo diz "não há nada especial a fazer"; o resto é estudo de quem vende ferramenta.

## Em uma página

1. **[A]** O Google diz que não existe requisito extra nem otimização especial para aparecer na Visão geral criada
   por IA ou no Modo IA: a página precisa estar indexada e apta a aparecer com trecho (snippet) na busca comum.
2. **[A]** O Google diz que não usa `llms.txt`, arquivo "para IA", marcação especial nem texto picado em pedaços; e
   que dado estruturado não é requisito para IA. **[B]** Registros de servidor de 137 mil domínios mostram que 97% dos
   `llms.txt` não receberam nenhum pedido em maio de 2026.
3. **[A]** Controles do Google: `nosnippet` e `max-snippet` também limitam o uso do texto como entrada direta dos
   recursos de IA; `noindex` tira da busca; desde 31/08/2026 há um controle no Search Console para excluir o site só
   dos recursos de IA. `Google-Extended` **não** tira o site da Visão geral nem do Modo IA e não afeta ranqueamento.
4. **[A]** Medição oficial: desde 2026 o Search Console tem um relatório de desempenho de IA generativa que mostra só
   **impressões**, por página, país, aparelho e data. Não mostra consulta nem clique separado.
5. **[A]** Para negócio local, a única orientação oficial é manter o Perfil da Empresa atualizado; o Google não
   documenta como escolhe as empresas que cita. **Para nós, o perfil é da licenciada, não do gerador de leads.**
6. **[A]** A política de spam do Google passou a citar a manipulação de respostas de IA; o guia do Google diz que
   buscar "menções" inautênticas não ajuda como parece. Compra de citação fica fora.
7. **[A]** Disponibilidade: Visão geral criada por IA no Brasil desde 15/08/2024; Modo IA em português do Brasil
   desde 08/09/2025.
8. **[B, consenso de direção; EUA]** Quando aparece o resumo de IA, cai o clique nos resultados (Pew, Ahrefs, Seer).
   O tamanho da queda e a causa são disputados.
9. **[B, duas fontes]** A resposta de IA muda a cada execução: medir "posição" não faz sentido; mede-se frequência de
   aparição em muitas repetições.
10. **[B]** No Brasil, quase metade das palavras-chave com 100+ buscas mensais já mostra Visão geral criada por IA
    (Ahrefs, outubro de 2026), e os domínios mais citados são YouTube e Instagram. **Não há dado de serviço local.**
11. **[A, por motor]** Cada motor separa o robô de busca do robô de treino. Bloquear o de treino não tira o site da
    busca; bloquear o de busca tira.
12. **Não sei:** se a busca "dedetização + bairro" em São Paulo dispara resposta de IA, e que fontes ela cita. Nenhum
    estudo aberto cobre controle de pragas nem serviço local no Brasil.

---

## 1. O que o Google documenta

Fontes oficiais abertas (todas do Google; quem ganha: o Google, que tem interesse em manter os sites abertos ao
rastreamento e em dizer que os cliques continuam bons):

- **F1** "AI features and your website", Search Central — https://developers.google.com/search/docs/appearance/ai-features
  (sem data na página; a versão `?hl=pt-br` devolveu o texto em inglês).
- **F2** "Optimizing your website for generative AI features on Google Search", Search Central —
  https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (sem data na página; cita o relatório
  de IA generativa lançado em junho de 2026, logo o texto atual é de 2026).
- **F3** Blog do Search Central, 21/05/2025, "Top ways to ensure your content performs well in Google's AI
  experiences on Search" — https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search
- **F4** Especificação de meta tag robots — https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag (sem data)
- **F5** Rastreadores comuns do Google, seção Google-Extended —
  https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers (sem data)
- **F6** Ajuda do Search Console, "Search generative AI control" — https://support.google.com/webmasters/answer/16908024?hl=en
- **F7** Ajuda do Search Console, "Generative AI performance report (Search)" — https://support.google.com/webmasters/answer/16984139?hl=en
- **F8** Blog do Search Central, 03/06/2026, "Introducing Search Generative AI performance reports in Search Console" —
  https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- **F9** Políticas de spam — https://developers.google.com/search/docs/essentials/spam-policies (sem data)
- **F10** Blog do Google Brasil, 15/08/2024 — https://blog.google/intl/pt-br/produtos/explore-e-encontre-respostas/novas-formas-de-se-conectar-com-a-web-com-as-visoes-gerais-criadas-por-ia/
- **F11** Blog do Google Brasil, 08/09/2025 — https://blog.google/intl/pt-br/produtos/busca-do-google-agora-o-brasil-ja-pode-usar-o-modo-ia-em-portugues

### 1.1 Requisitos para aparecer

| Afirmação | O que fazer aqui | Fonte | Data da fonte | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|
| Não há requisito extra: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." | Tratar IA do Google como consequência do SEO comum (guia (a)) | F1 | sem data; lida em 13/11/2026 | A | Google | Confirmado em duas leituras |
| Para ser link de apoio: "a page must be indexed and eligible to be shown in Google Search with a snippet" | Garantir indexação e não usar `nosnippet` nas páginas que devem ser citadas | F1 | idem | A | Google | Indexação não é garantida, diz a mesma página |
| "You don't need to create new machine readable files, AI text files, or markup to appear in these features." | Não criar `llms.txt` nem marcação "para IA" | F1 | idem | A | Google | F2 repete e nomeia `llms.txt` entre os mitos |
| "There's no requirement to break your content into tiny pieces for AI to better understand it." | Escrever para a pessoa; não picar o texto | F2 | 2026 (sem dia) | A | Google | Ver disputa com a Microsoft na seção 3 |
| "Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add." | Dado estruturado só o que vale para a busca comum, igual ao texto visível | F2; F3 pede que a marcação corresponda ao conteúdo visível | 2026; 21/05/2025 | A | Google | — |
| Na visão do Google, otimizar para IA "is optimizing for the search experience, and thus still SEO." | Não separar um "projeto de GEO" | F2 | 2026 | A | Google | — |
| Conteúdo único, "non-commodity", boa experiência de página, texto rastreável, imagens e vídeos de apoio | Fatos em texto HTML, não só em imagem | F3 | 21/05/2025 | A | Google | Fonte de 2025: pode estar desatualizada; F2 (2026) mantém a linha |
| "Query fan-out": o sistema dispara várias buscas relacionadas, "issuing multiple related searches across subtopics and data sources" | Cobrir as perguntas vizinhas do tema (preço, licença, prazo de reentrada, praga × tipo de imóvel) em páginas indexáveis | F1; F11 chama de "desdobramento de pergunta (query fan-out)" | sem data; 08/09/2025 | A | Google | O Google não expõe quais buscas gera; o que ferramentas mostram é simulação (Ahrefs, 02/03/2026) |

### 1.2 Controles: o que cada um controla e o que não controla

| Controle | O que controla | O que NÃO controla | Fonte | Classe |
|---|---|---|---|---|
| `robots.txt` para Googlebot | Rastreamento para a Busca, que inclui os recursos de IA (F1 diz que a IA é parte da Busca) | Não há token separado para a Visão geral ou o Modo IA | F1 | A |
| `nosnippet` | Além de tirar o trecho, "will also prevent the content from being used as a direct input for AI Overviews and AI Mode." | Não tira a página do resultado | F4 | A |
| `max-snippet:[n]` | "will also limit how much of the content may be used as a direct input for AI Overviews and AI Mode" | — | F4 | A |
| `data-nosnippet` | Marca trechos do HTML que não podem virar snippet | A seção não cita IA pelo nome; F1 e F3 o listam entre os controles de exibição | F4, F1, F3 | A |
| `noindex` | Tira a página dos resultados (e, portanto, da IA) | — | F4 | A |
| Controle "Search generative AI" no Search Console (Incluir / Excluir; padrão = Incluir) | Excluir: "Content crawled from your site won't be eligible to be used as an input to generate an AI response or preview in Search generative AI features." Vale para Visão geral, Modo IA e recursos de IA do Discover | "This control doesn't affect AI training; to limit training of the models used to generate responses in Search generative AI features, use Google-Extended." Também não é sinal de ranqueamento nem de inclusão no resto da Busca. A página não fala do aplicativo Gemini | F6 ("As of August 31, 2026, we've rolled out this control to all websites worldwide.") | A |
| `Google-Extended` (token de robots.txt, sem robô próprio) | Uso do conteúdo para treinar modelos Gemini e para fundamentação (grounding) no aplicativo Gemini e na Vertex AI | "Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search." Logo, não tira da Visão geral nem do Modo IA | F5 | A |
| `noarchive` / `nocache` | Nada no Google: a especificação diz que a Busca do Google não usa essas regras | São controles do Bing (seção 3) | F4 | A |

Leitura para o projeto: um site que **quer** ser citado deixa tudo no padrão (Googlebot liberado, sem `nosnippet`,
controle em "Incluir"). Bloquear `Google-Extended` não muda a Busca, mas, pelo texto de F5, pode tirar o site da
fundamentação do aplicativo Gemini; é decisão do owner, e a inferência sobre o Gemini é minha, não frase do Google.

### 1.3 Como aparece no Search Console

| Afirmação | O que fazer aqui | Fonte | Data | Classe | Observação |
|---|---|---|---|---|---|
| Aparições em recursos de IA entram no relatório de Desempenho, tipo de pesquisa "Web" | Não esperar linha separada de cliques de IA | F1 | sem data | A | — |
| Existe o relatório "Generative AI performance (Search)". Cobre Visão geral e Modo IA. Métrica: só impressões — "Impressions are how many times links to your site were shown to a user in a generative AI feature on Google Search." | Usar como contagem de aparições por página | F7; anúncio em F8 | F8: 03/06/2026; nota de 31/08/2026 dizendo que chegou a todos os sites | A | Dimensões: páginas, países, datas, aparelhos. **Sem aba de consultas, sem cliques, sem CTR, sem posição.** A ajuda não descreve como separar Visão geral de Modo IA |
| Esses dados são parte do relatório geral: o relatório de IA "includes data from the Web search type in the Performance report (Search results)" | Não somar os dois relatórios | F7; F8 diz o mesmo | 2026 | A | — |
| Na Visão geral, todos os links recebem a mesma posição (a do bloco); no Modo IA, pergunta de acompanhamento conta como nova consulta | Ler "posição média" com cuidado quando houver resumo de IA | https://support.google.com/webmasters/answer/7042828?hl=en | sem data | A | Lido uma vez; paráfrase |
| Site excluído pelo controle de F6 não recebe impressões nem tráfego desses recursos | Manter "Incluir" | F6 | 2026 | A | — |

### 1.4 O que o Google diz sobre cliques (afirmação do interessado)

| Afirmação | Fonte | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|
| Cliques vindos de páginas de resultado com Visão geral seriam melhores: "these clicks are higher quality, where users are more likely to spend more time on the site." | F3; F10 diz algo parecido em português | 21/05/2025; 15/08/2024 | A quanto a "o Google afirma"; **o Google não publica o dado** | Google | Não é evidência de volume de cliques. Os estudos da seção 4 medem queda. Fica em "disputado" |

### 1.5 Disponibilidade no Brasil

| Recurso | Data | Trecho | Fonte | Classe |
|---|---|---|---|---|
| Visão geral criada por IA | 15/08/2024 | "Reino Unido, Índia, Japão, Indonésia, México e Brasil, com suporte ao idioma local em cada um deles." | F10 | A |
| Modo IA | 08/09/2025 (início da liberação) | "Hoje, estamos começando a lançar o Modo IA na Busca do Google em português do Brasil." | F11 | A |
| Uso do Modo IA | janeiro a abril de 2026, **Estados Unidos** | 0,34% das buscas no Google passaram ao Modo IA | SparkToro com painel da Similarweb, 09/06/2026 — https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ | B (quem ganha: SparkToro vende ferramenta de pesquisa de audiência; Similarweb vende dados) |

Não achei número de uso do Modo IA no Brasil.

### 1.6 Spam e "menções"

| Afirmação | O que fazer aqui | Fonte | Classe | Observação |
|---|---|---|---|---|
| A definição de spam inclui tentar manipular respostas de IA: "attempting to manipulate generative AI responses in Google Search" | Nada de texto escondido para modelo, lista falsa, rede de menções | F9 (parágrafo de abertura) | A | Confirmado em duas leituras |
| Os recursos de IA podem mostrar o que se diz de produtos e serviços pela web (blogs, vídeos, fóruns), mas "seeking inauthentic "mentions" across the web isn't as helpful as it might seem." | Ser citado por terceiros só de forma legítima (imprensa local, entidade do setor, diretório verdadeiro) | F2 (seção de mitos) | A | O Google descreve, não promete efeito |
| Trocar dinheiro, bens ou serviços por links e troca excessiva de links são spam de links | Mesma regra do guia (a) | F9 | A | Lido uma vez; paráfrase |

---

## 2. Busca local: o que os recursos de IA do Google mostram

O que tem fonte oficial é pouco. O Google **não documenta** como escolhe as empresas locais que aparecem numa resposta
de IA.

| Afirmação | O que fazer aqui | Fonte | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|
| Respostas de IA podem incluir informação de negócios locais; Merchant Center e Perfil da Empresa "can help your products and services to be visible in both AI responses and other Google Search results" | O perfil é da **licenciada parceira**. O gerador de leads não tem perfil (ver `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, seção do perfil de empresa) | F2, seção "Optimize your local business and ecommerce details" | 2026 | A | Google | É a única frase oficial sobre local em IA que achei |
| Manter as informações do Perfil da Empresa atualizadas | Idem: tarefa da licenciada | F1 e F3 ("ensure that your Merchant Center and Business Profile information is up-to-date") | sem data; 21/05/2025 | A | Google | — |
| O Modo IA usa fontes em tempo real como o Mapa do Conhecimento e "informações do mundo real"; os recursos de agente apoiam-se no Mapa do Conhecimento e no Google Maps | Nenhuma ação direta | Blog do Google, 05/03/2025 (https://blog.google/products-and-platforms/products/search/ai-mode-search/) e 21/08/2025 (https://blog.google/products-and-platforms/products/search/ai-mode-agentic-personalized/) | 2025 | A | Google | Lidos uma vez; paráfrase. Pode estar desatualizada. Nenhum dos dois cita o Perfil da Empresa pelo nome |
| A Busca pode telefonar para negócios locais e pedir preço e disponibilidade; o negócio controla isso nas configurações do Perfil da Empresa | Nenhuma: recurso dos **Estados Unidos** | Blog do Google, 16/07/2025 — https://blog.google/products/search/deep-search-business-calling-google-search/ | 2025 | A | Google | Lido uma vez; não achei anúncio para o Brasil |
| Agendamento de serviço local pelo Modo IA estava "em breve" em agosto de 2025, só para assinantes nos **Estados Unidos** | Nenhuma | Blog do Google, 21/08/2025 (acima) | 2025 | A | Google | Não sei se foi lançado nem se existe no Brasil |

Estudos sobre local (todos dos **Estados Unidos**, todos de quem vende ferramenta ou serviço de SEO local; nenhum com
controle de pragas):

| Achado | Fonte | Amostra e método | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|
| Em busca com intenção local ("serviço + cidade") a Visão geral apareceu em 15% dos casos e o bloco de mapa em 93%; em busca informativa, 92% e 6% | Whitespark — https://whitespark.ca/blog/case-study-the-prevalence-of-ai-overviews-in-local-search/ | 540 buscas manuais, 6 ramos (encanador é o único de serviço para casa), 3 cidades dos EUA | 12/05/2025 | B (amostra pequena) | Whitespark vende ferramenta e serviço de listagens | **Pode estar desatualizada** (2025). Um texto de 2026 visto só no resultado de busca fala em 88%: não aberto, não usado |
| Em ~200 mil buscas locais sem marca: Perfil da Empresa foi ~28,5% das citações (muito nos recursos do Google, quase nada no ChatGPT); sites das empresas, 42% das citações; Yelp ~9,5%; Facebook ~2,2% | BrightLocal — https://www.brightlocal.com/research/local-ai-visibility-study/ | ~200 mil buscas, ~1.300 locais, 60 dias, três plataformas (ChatGPT, Modo IA, Visão geral), coletadas pela ferramenta da própria empresa | 16/09/2026 | B | BrightLocal vende rastreador de visibilidade em IA e construção de citações | Não informa ramos, cidades nem país; números divergem entre seções do próprio texto |
| Mesmo estudo: o Maps citou o negócio rastreado em 66% das buscas; Modo IA 32%, Visão geral 38%. Só 29,3% das empresas coincidem entre Modo IA e Visão geral | idem | idem | 16/09/2026 | B | idem | Ir bem no mapa não garante aparecer na IA |
| No Modo IA, ~80% das citações em busca local iriam para Maps/Perfil da Empresa; na Visão geral, ~70% para o site da empresa | Steady Demand (agência de perfil de empresa), agosto de 2026 | ~8 mil buscas, 50 regiões dos EUA, 10 ramos de serviço para casa | 2026 | **não aberta** (conexão recusada três vezes) | Agência que vende gestão de perfil | Vista só em resultado de busca: **não usada como base de regra** |

Leitura para o projeto: (1) em busca de contratação ("dedetização + bairro") o mapa ainda era o bloco dominante nos
EUA em 2025 e a Visão geral aparecia mais em pergunta informativa — é hipótese a conferir ao vivo no item 4, não fato
do Brasil; (2) quando a IA lista empresas, ela se apoia muito em dado de perfil e no site **da empresa**; um site
intermediário aparece, se aparecer, como fonte de informação, não como "a empresa recomendada".

---

## 3. Robôs e controles dos outros motores (documentação de cada um)

| Motor | Robô / controle | O que a documentação diz | O que fazer aqui | Fonte | Data da fonte | Classe | Quem ganha |
|---|---|---|---|---|---|---|---|
| Perplexity | `PerplexityBot` | Indexa para mostrar e linkar sites nos resultados; "It is not used to crawl content for AI foundation models." A empresa recomenda liberá-lo no `robots.txt` e no firewall | Liberar | https://docs.perplexity.ai/guides/bots | sem data | A | Perplexity |
| Perplexity | `Perplexity-User` | Busca páginas a pedido do usuário; "Since a user requested the fetch, this fetcher generally ignores robots.txt rules." | Saber que `robots.txt` não o barra | idem | sem data | A | Perplexity |
| Perplexity | Prazo | Mudança no `robots.txt`: "it may take up to 24 hours for our systems to reflect changes" | — | idem | sem data | A | — |
| Microsoft (Bing, Copilot) | Sem meta tag | Conteúdo pode aparecer nas respostas: "No action is needed to remain in Bing Chat." | Não pôr `nocache` nem `noarchive` | https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat | 22/09/2023 | A | Microsoft |
| Microsoft | `NOCACHE` | Só URL, trecho e título entram na resposta: "We will only display URL/Snippet/Title in the answer." | Não usar | idem | 22/09/2023 | A | Microsoft |
| Microsoft | `NOARCHIVE` | "Content tagged NOARCHIVE will not be included in Bing Chat answers." Também não é usado para treinar os modelos da Microsoft. Com as duas tags, vale `NOCACHE` | Não usar | idem | 22/09/2023 | A | Microsoft |
| Microsoft | Busca comum | Páginas com essas tags continuam nos resultados do Bing | — | idem | 22/09/2023 | A | — |
| Microsoft | Relatório "AI Performance" no Bing Webmaster Tools (prévia pública) | Mostra citações no Copilot, nos resumos de IA do Bing e em parceiros; traz as "grounding queries": "the key phrases the AI used when retrieving content". A contagem indica "how often pages are cited, not page importance, ranking, or placement" | Quando houver site, verificar no Bing Webmaster Tools (ação do owner: exige conta) | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | 10/02/2026 | A | Microsoft |
| Microsoft | Recomendações do mesmo anúncio | Títulos claros, tabelas e seções de perguntas e respostas; afirmações com evidência; conteúdo atualizado; IndexNow; cadastro no Bing Places para negócio local | Estrutura clara é barata e não conflita com o Google. Bing Places é da licenciada | idem | 10/02/2026 | A (orientação do motor, sem dado) | Microsoft |
| Microsoft | Texto de 08/10/2025 no blog de anúncios | Diz que nada garante a seleção; descreve que a IA quebra a página em pedaços; pede perguntas com resposta direta, listas e tabelas; pede não esconder resposta em aba, PDF ou imagem; diz que rastreabilidade, metadados, links internos e backlinks seguem essenciais | Idem | https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers | 08/10/2025 | A (lido uma vez; paráfrase) | Microsoft |
| IndexNow | Protocolo de aviso de URL nova, alterada ou removida | A página inicial lista Microsoft Bing, Naver, Seznam.cz, Yandex e Yep; **o Google não aparece na lista**. Resposta 200 só indica recebimento | Opcional; não vale para o Google | https://www.indexnow.org/ e https://www.indexnow.org/documentation | sem data | A (lido uma vez; paráfrase) | Microsoft e demais participantes |
| Google | `Google-Extended` | Ver seção 1.2 | Decisão do owner | F5 | sem data | A | Google |
| Apple | `Applebot` | Alimenta a tecnologia de busca usada em Spotlight, Siri e Safari | Liberar | https://support.apple.com/en-us/119829 | 04/09/2026 | A | Apple |
| Apple | `Applebot-Extended` | Serve para recusar o uso em treino dos modelos da Apple. "Applebot-Extended does not crawl webpages." e "Webpages that disallow Applebot-Extended can still be included in search results." | Decisão do owner; não afeta busca | idem | 04/09/2026 | A | Apple |
| Anthropic | `ClaudeBot` | Coleta conteúdo que pode ir para treino; bloqueá-lo sinaliza exclusão do material futuro dos conjuntos de treino | Decisão do owner | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | sem data ("atualizado há mais de uma semana") | A | Anthropic |
| Anthropic | `Claude-User` | Acessa sites quando um usuário pergunta; bloquear "prevents our system from retrieving your content in response to a user query" | Liberar | idem | idem | A | Anthropic |
| Anthropic | `Claude-SearchBot` | Indexa para a busca; bloquear "prevents our system from indexing your content for search optimization" | Liberar | idem | idem | A | Anthropic |
| Anthropic | Regras | Os robôs seguem `robots.txt` e aceitam `Crawl-delay` | — | idem | idem | A | — |

**`llms.txt`:** proposta de Jeremy Howard, publicada em 03/09/2024 em https://llmstxt.org/ (página modificada em
10/08/2026; lida uma vez). É um arquivo na raiz para ajudar agentes a usar um site, pensado para o momento da
consulta e não para treino. A própria página **não afirma** que algum buscador ou assistente o consome. O Google diz
que não usa (F2, classe A). Não achei documentação de Perplexity, Microsoft, Apple ou Anthropic declarando que usam
`llms.txt` para escolher fontes. Dado: Ahrefs, 15/06/2026, 137.210 domínios (clientes da ferramenta de análise da
empresa, viés técnico), maio de 2026: 28% tinham arquivo válido e 97% desses não receberam nenhum pedido; robôs de
recuperação de IA foram 1,1% dos pedidos — https://ahrefs.com/blog/llmstxt-study/ (classe B; quem ganha: Ahrefs vende
ferramenta de SEO; aqui o achado é contra criar trabalho novo). Um segundo estudo (SE Ranking, ~300 mil domínios)
foi visto só em resultado de busca: **não aberto**.

**Diretrizes atuais do Bing:** a página oficial não abriu (só o título carregou). Uma reportagem de 27/02/2026
(Search Engine Journal, https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442/)
relata que as diretrizes passaram a nomear "GEO", a explicar `NOARCHIVE`/`NOCACHE` para o Copilot e a tratar injeção
de prompt como abuso. É relato de segunda mão (classe C): **não usado como regra**.

---

## 4. Estudos com dado sobre o que é citado e sobre cliques

### 4.1 Citações de IA × primeiros resultados orgânicos

| Achado | Fonte | Amostra e método | País | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|---|
| 37,9% das URLs citadas na Visão geral estavam entre os 10 primeiros; 31,2% entre 11 e 100; 31,0% fora dos 100 | Ahrefs — https://ahrefs.com/blog/ai-overview-citations-top-10/ | 863 mil resultados de palavras-chave, 4 milhões de URLs citadas, base da ferramenta da empresa | não informado | 02/03/2026 | B | Ahrefs vende ferramenta que monitora citações | Em julho de 2025 a mesma empresa media 76%; ela diz que a comparação não é direta (mudou a leitura das citações e o modelo do Google). Explica pela "query fan-out" |
| Sobreposição subiu de 32,3% (maio de 2024) para 54,5% (setembro de 2025), contando qualquer posição orgânica; só 16,7% das citações vinham dos 10 primeiros. Por setor: saúde 75,3%; restaurantes 19,2% | BrightEdge — https://www.brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio | 9 setores; sem número de palavras-chave nem país | não informado | 18/09/2025 | B fraca | BrightEdge vende plataforma de SEO e produtos de "IA" | Pode estar desatualizada (2025). Limite de "sobreposição" não definido |

O que as duas têm em comum: **a maior parte das citações não vem dos 10 primeiros da mesma busca**. Como a segunda
fonte é "B fraca", isso fica como indicação, não como consenso. O que nenhuma das duas diz: que dá para ser citado
sem estar indexado e ranqueando para alguma busca vizinha (F1 exige indexação).

### 4.2 Que tipo de fonte é citado

| Achado | Fonte | Amostra e método | País | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|---|
| **Brasil:** 47,4% das palavras-chave com 100+ buscas mensais mostram Visão geral criada por IA; 11,8% na faixa de 10 a 99 buscas; por intenção: informacional 47,7%, comercial 49,6%, transacional 48,9%, navegacional 30,8% | Ahrefs — https://ahrefs.com/pt/blog/ai-overviews-brasil/ | 6.698.455 palavras-chave do Google Brasil; presença contada no resultado mais recente guardado pela ferramenta | **Brasil** | 23/10/2026 | B | Ahrefs (vende a ferramenta usada) | "Fotografia": muda de semana a semana. **Sem categoria de serviço local, casa ou "intenção local"**. A cauda longa (onde ficam "praga + bairro") tem bem menos resumo de IA |
| **Brasil:** domínios mais citados na Visão geral: youtube.com (19,5% do top 100), instagram.com (16,4%), google.com (6,6%), facebook.com (5,2%), tiktok.com (4,8%), reddit.com (3,3%), Mercado Livre, Wikipédia em português (2,8%); reclameaqui.com.br em 18º | idem | respostas monitoradas pela ferramenta de marca da empresa | **Brasil** | 23/10/2026 | B | idem | Base do percentual é "o top 100", não todas as citações. Não há lista para serviços locais |
| Wikipedia, YouTube e Reddit somaram 15% das fontes nos resumos de IA; sites `.gov` foram 6% (contra 2% nos resultados comuns); 88% dos resumos citaram 3 ou mais fontes | Pew Research Center — https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ | 900 adultos, navegação de março de 2025, 68.879 buscas | **EUA** | 22/07/2025 | B | Pew é instituto sem fins lucrativos; não vende ferramenta | Pode estar desatualizada (2025) |
| Reddit e YouTube no top 5 de citações de todos os cinco motores; nos recursos do Google aparecem também Facebook, LinkedIn e Yelp | Peec AI — https://peec.ai/blog/top-domains-cited-by-ai-search-analysis-based-on-30m-sources | "30 milhões de fontes"; sem período, sem número nem critério de perguntas | **EUA** | 31/03/2026 | B fraca | Peec vende monitoramento de IA | Método não exposto: não vira regra |
| Busca local: Perfil da Empresa, site da empresa, Yelp, Facebook (ver seção 2) | BrightLocal | ver seção 2 | EUA (presumido; não informado) | 16/09/2026 | B | BrightLocal | — |

Leitura: no Brasil, o que a Visão geral mais cita são **vídeo e rede social**, não fórum. Diretório e site de
avaliação aparecem nos estudos locais dos EUA (Yelp); o equivalente brasileiro medido é o Reclame Aqui (18º no
geral). Para dedetização em São Paulo, **não há dado**.

### 4.3 Efeito sobre cliques

| Achado | Fonte | Amostra e método | País | Data | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|---|
| Com resumo de IA, o usuário clicou num resultado em 8% das visitas; sem resumo, 15%. Clique em link dentro do resumo: 1%. Sessão encerrada: 26% contra 16% | Pew Research Center (URL acima) | 900 adultos; 68.879 buscas; resumo em 18% delas | **EUA** | 22/07/2025 | B | não vende ferramenta | Um painel, um mês; pode estar desatualizada |
| CTR da 1ª posição 34,5% menor quando há Visão geral (março de 2024 × março de 2025) | Ahrefs — https://ahrefs.com/blog/ai-overviews-reduce-clicks/ | 300 mil palavras-chave (150 mil com resumo, 150 mil informativas sem), dados agregados do Search Console, só computador | não informado | 17/04/2025 | B | Ahrefs | Correlação; o "sem resumo" é projeção |
| Atualização: 58% menor (dezembro de 2023 × dezembro de 2025); 2ª posição −50,8%; 10ª −19,4% | Ahrefs — https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/ | mesmo desenho | não informado | 04/02/2026 | B | Ahrefs | O CTR das informativas **sem** resumo também caiu (0,076 → 0,039) |
| CTR orgânico em buscas com resumo: 1,76% → 0,61% (−61%) de junho de 2024 a setembro de 2025; sem resumo, −41%. Quando a marca é citada no resumo: 0,70% contra 0,52% | Seer Interactive — https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update | 42 clientes, 3.119 termos informativos, 25,1 milhões de impressões | não informado | 04/11/2025 | B | Seer é agência e vende rastreador de respostas de IA | A autora diz que não prova causa e que pode não valer para busca comercial, transacional ou **local** |
| Mesmas palavras-chave antes e depois de ganhar resumo: taxa de busca sem clique foi de 33,75% para 31,53% (não subiu). Presença do resumo: 6,49% (janeiro de 2025), 24,61% (julho), 15,69% (novembro) | Semrush — https://www.semrush.com/blog/semrush-ai-overviews-study/ | 10 milhões+ de palavras-chave; 200 mil+ com dados de navegação de empresa do grupo | não informado | 15/12/2025 | B | Semrush vende ferramenta | **Contraria** a leitura de "resumo de IA causa menos clique" |
| 68,01% das buscas no Google terminaram sem clique (janeiro a abril de 2026), contra 60,45% em 2024 | SparkToro com Similarweb (URL na seção 1.5) | painel de navegação em computador e navegador de celular; exclui o aplicativo do Google | **EUA** | 09/06/2026 | B | SparkToro; Similarweb | O autor chama a comparação entre anos de "maçãs e laranjas" (painéis diferentes) |
| **Brasil:** queda de ~31% (Globo) e ~35% (UOL) no clique das palavras-chave em 1ª posição, março de 2024 × março de 2025 | Conversion — https://www.conversion.com.br/blog/estudo-ai-overview | 26.486 e 30.000 palavras-chave; a página não diz de onde vêm os dados nem como descontou a queda natural | **Brasil** | 22/04/2025 (atualizado em 20/05/2025) | C/D | Agência de SEO | Portais de notícia, não serviço local; método não exposto: **não vira regra**; pode estar desatualizada |

### 4.4 O artigo acadêmico "GEO: Generative Engine Optimization"

- **Fonte:** Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande; arXiv 2311.09735 (16/11/2023; versão 3 de
  28/06/2024); aceito na KDD 2024 — https://arxiv.org/abs/2311.09735 e https://arxiv.org/html/2311.09735v3. Classe B.
  Quem ganha: autores acadêmicos; não vendem ferramenta (o termo "GEO" depois foi adotado por vendedores).
- **O que mediu:** quanto do texto de uma fonte aparece na resposta gerada, por contagem de palavras ajustada pela
  posição da citação e por uma nota de "impressão subjetiva" dada por outro modelo.
- **Em que motor:** um motor montado pelos autores (os 5 primeiros resultados do Google + GPT-3.5 redigindo a
  resposta), sobre um conjunto de 10 mil perguntas; e uma conferência no Perplexity com 200 perguntas, por envio de
  arquivo.
- **Resultado:** acrescentar citações de terceiros entre aspas, estatísticas e referência a fontes elevou a
  visibilidade (melhor método: cerca de +41% na contagem ajustada, no motor dos autores; cerca de +22% no Perplexity).
  Encher de palavra-chave piorou (17,8 contra 19,5 de base). Sites em 5º lugar ganharam mais do que o 1º.
- **Limites:** motor simulado com modelo de 2023; só 5 fontes por pergunta; nenhuma pergunta de serviço local nem em
  português; nota subjetiva dada por modelo; os autores dizem que os métodos podem ter de mudar conforme os motores
  mudam; não mediram efeito no ranqueamento. **Pode estar desatualizada** (2023–2024). Não foi testado na Visão geral
  nem no Modo IA do Google, e o Google diz que não é preciso reescrever para IA (F2).

### 4.5 Variação das respostas (importa para medir)

| Achado | Fonte | Amostra e método | País | Data | Classe | Quem ganha |
|---|---|---|---|---|---|---|
| Menos de 1 chance em 100 de duas respostas trazerem a mesma lista de marcas (ChatGPT e IA do Google); mesma ordem, cerca de 1 em 1.000. Conclusão dos autores: "posição" em IA não é métrica; percentual de aparição em muitas execuções é | SparkToro com Gumshoe — https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/ | 600 voluntários, 12 perguntas, 2.961 respostas, novembro e dezembro de 2025 | não controlado (ferramentas populares nos EUA) | 28/01/2026 | B | Gumshoe vende rastreamento de IA; os autores declaram o conflito e que não é revisão por pares |
| Busca local repetida: sobreposição média entre listas de 21% (Modo IA), 33% (Visão geral), 23% (ChatGPT); 71–80% das empresas aparecem em metade das tentativas ou menos | BrightLocal (URL na seção 2) | ~200 mil buscas | não informado | 16/09/2026 | B | BrightLocal |

### 4.6 Há estudo com dado do Brasil ou em português?

- **Sim, um com amostra e método expostos:** Ahrefs, 23/10/2026, 6,7 milhões de palavras-chave do Google Brasil —
  mede **presença** da Visão geral e **domínios citados**. Não mede clique e não tem recorte local.
- **Um fraco:** Conversion, 2025, clique em dois portais de notícia, método não exposto.
- **Não achei:** estudo brasileiro de clique com método exposto; estudo de fontes citadas em busca local no Brasil;
  qualquer estudo sobre controle de pragas; estudo do Modo IA em português. Outros textos brasileiros que apareceram
  na busca são resumos de estudos estrangeiros.

---

## 5. O que é só alegação (classe D) e circula muito

| Alegação | Quem costuma afirmar e o que ganha | O que A ou B dizem | Situação |
|---|---|---|---|
| "`llms.txt` é fator para ser citado" | Ferramentas e agências que vendem auditoria de "GEO" | Google: não usa (F2, A). Ahrefs: 97% dos arquivos sem nenhum pedido (B) | **Contrariada** para o Google; sem prova nos demais |
| "Otimize para prompts" (escrever páginas com a frase exata que a pessoa digitaria no assistente; templates de consulta) | Vendedores de rastreador de prompts | Google confirma a "query fan-out", mas não expõe as buscas geradas e diz que não há otimização especial (F1, F2). A Microsoft mostra as "grounding queries" do próprio site no relatório dela (A) | O mecanismo existe (A); a tática é D |
| "Aumente a densidade de citações e estatísticas no texto" | Vendedores de "GEO", citando o artigo da KDD | O artigo mediu isso em motor simulado de 2023 e em 200 perguntas no Perplexity (B, limitado). Google: não reescrever para IA (F2) | D para o Google; hipótese fraca para os demais. Dado verdadeiro com fonte é bom por outros motivos (propaganda e CDC) |
| "Compre menções / citações em blogs e rankings" | Quem vende link e publicação paga | Google: troca de dinheiro por link é spam; manipular resposta de IA é spam; menção inautêntica não ajuda como parece (F9, F2 — A) | **Contrariada por A**; vedada pelo portão do item 6 |
| "Ponha-se em primeiro no seu próprio ranking" | Agências de conteúdo para software | Peec (03/03/2026, 232 mil citações, só software): ~11% das citações vêm dessas listas, sem queda em 12 semanas. Lily Ray (17/06/2026, 100 buscas de software, 3 datas): em 69% dos casos a lista foi citada e a marca autora **não** foi recomendada | Disputado (seção final) |
| "Dado estruturado especial / esquema de FAQ faz a IA citar" | Plugins e agências | Google: não é requisito e não há esquema especial (F2, A). Microsoft: esquema ajuda a entender (A, sem dado) | D para o Google |
| "Quem está no mapa aparece na IA" | Agências de SEO local | BrightLocal: Maps 66% × Modo IA 32% × Visão geral 38% de menção ao negócio rastreado (B, EUA presumido) | Não confirmada |
| "Posição nº X no ChatGPT / no Modo IA" como métrica | Rastreadores de IA | Dois estudos B mostram que a lista muda a cada execução | **Contrariada** |

---

## 6. O que o exemplo do owner acertou, errou ou não provou (táticas 4.1–4.10)

Referência: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`, Parte 4. O que é só do
ChatGPT fica para `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`.

| # | Tática do exemplo | Veredito neste guia | Base |
|---|---|---|---|
| 4.1 | Sem SEO não há o que a IA achar; IA vem depois do SEO | **Confirmada por A para o Google.** Para o ChatGPT: ver 03b | F1 (página indexada e apta a snippet); F2 ("still SEO") |
| 4.2 | Dados franceses: respostas com fonte vêm de busca; "busca no Google"; fontes giram; autoridade do domínio não é o filtro | **Permanece D** aqui. Duas partes têm apoio B: as fontes giram (seção 4.5) e a maioria das citações da Visão geral não vem dos 10 primeiros (seção 4.1). "Busca no Google" é assunto do 03b | SparkToro/Gumshoe; BrightLocal; Ahrefs 02/03/2026 |
| 4.3 | O assistente reescreve a conversa em várias buscas curtas; otimizar para elas | **Mecanismo confirmado por A no Google** (query fan-out). Os moldes de busca ("melhor + termo + ano + país") e a tática de mirar neles **permanecem D**: o Google não expõe as buscas e diz que não há otimização especial | F1, F11, F2 |
| 4.4 | O Google diz que não há requisito extra; não gastar tempo com `llms.txt` | **Confirmada por A**, e por B quanto ao `llms.txt` | F1, F2; Ahrefs 15/06/2026 |
| 4.5 | Pôr-se em primeiro no próprio ranking deixou de render citação | **Não provada; disputada.** Um estudo diz que essas listas ainda são citadas (~11%); outro, que são citadas mas a marca autora não é recomendada (69%). Ambos só de software, nos EUA ou sem país | Peec 03/03/2026; Lily Ray 17/06/2026 |
| 4.6 | Ser listado em rankings de terceiros; troca de rankings; renovar com o ano no título | **Parte A, parte contrariada, parte D.** A: os recursos de IA mostram o que terceiros dizem (F2). Contrariada por A: troca combinada é troca de links, e menção inautêntica "não ajuda como parece" (F9, F2). Ano no título: D | F2, F9 |
| 4.7 | Citação barata comprada rende como mídia grande; redes de blogs | **Contrariada por A** (spam de links; manipulação de resposta de IA). A eficácia alegada não tem estudo: D | F9, F2 |
| 4.8 | Reddit pesa de forma diferente por motor e cai no ChatGPT; comentar nos tópicos que o modelo lê | **Parte B.** Varia por motor (Peec, B fraca, EUA). **No Brasil o Reddit é o 6º domínio citado na Visão geral (3,3% do top 100)**; YouTube e Instagram lideram (Ahrefs, B). Queda no ChatGPT: 03b. Método de comentar: D | Ahrefs 23/10/2026; Peec 31/03/2026; Pew 22/07/2025 |
| 4.9 | Ocupar a primeira tela com vídeo, rede social e lista de terceiros, porque o domínio só leva duas posições | **Parte A, parte B, resto hipótese.** A: o sistema de diversidade de sites em geral não mostra mais de duas listagens do mesmo site (https://developers.google.com/search/docs/appearance/ranking-systems-guide, lido uma vez). B: vídeo e rede social são os domínios mais citados na Visão geral no Brasil. Que isso traga lead: sem dado | ranking systems guide; Ahrefs 23/10/2026 |
| 4.10 | Testar à mão, deslogado, uma vez por mês, porque a API devolve fontes diferentes do aplicativo | **Teste manual: razoável. "Uma vez por mês": contrariado por B** — uma execução isolada diz pouco. "API ≠ aplicativo": os autores do estudo B dizem que é questão em aberto. Permanece D nesse ponto | SparkToro/Gumshoe 28/01/2026; BrightLocal 16/09/2026 |

Resumo: o exemplo **acertou** onde repetiu a documentação do Google (4.1, 4.4, o mecanismo de 4.3). **Errou** ao
propor uma medição mensal única (4.10) e ao tratar citação comprada e troca de rankings como tática (4.6, 4.7), que
a política do Google enquadra como spam. **Não provou** nada do que traz número próprio (4.2, 4.5, 4.8), e nenhum
dos seus casos é de serviço local.

---

## 7. O que isso implica para um site de leads de dedetização em São Paulo

### 7.1 O que fazer (cada linha aponta a base)

| Ação | Base | Classe |
|---|---|---|
| Tratar resposta de IA do Google como resultado do SEO comum: página indexada, apta a snippet, útil e original. Sem projeto separado de "GEO" | F1, F2 | A |
| Pôr os fatos em **texto HTML rastreável**, não só em imagem, aba fechada ou PDF: quem executa o serviço, número da licença, região atendida, faixa de preço com fonte e data, prazo de reentrada, o que a norma exige | F3 (Google); texto da Microsoft de 08/10/2025 | A |
| Manter datas e números atualizados e visíveis (data de revisão na página) | Microsoft 10/02/2026 (frescor); F3 | A (orientação, sem dado) |
| Estrutura clara: um título por pergunta real, tabela onde há comparação, bloco de perguntas e respostas | Microsoft (A para Bing/Copilot). No Google não é requisito, mas não conflita | A (Microsoft) |
| Página "quem somos" verificável: quem responde pelo site, CNPJ, que o site **não executa** o serviço, como as licenciadas são escolhidas, como pedir exclusão de dados | Decorre do item 2 da rodada (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`) e de F3 (conteúdo para pessoas). Efeito sobre citação: **sem evidência A ou B** | premissa marcada |
| Dados estruturados só os que correspondem ao texto visível; nada de marcar como negócio local com endereço o que não é | F3 (marcação = conteúdo visível); F2 (não é requisito para IA) | A |
| `robots.txt`: liberar Googlebot, Bingbot, `PerplexityBot`, `Claude-SearchBot`, `Claude-User`, `Applebot` (e os robôs de busca da OpenAI, conforme o 03b). Tokens de treino (`Google-Extended`, `Applebot-Extended`, `ClaudeBot`): decisão do owner; pela documentação, bloqueá-los não tira o site da busca | Seção 3 | A |
| Sem `nosnippet`, `max-snippet` baixo, `NOCACHE` ou `NOARCHIVE` nas páginas que devem ser citadas; controle do Search Console em "Incluir" | F4, F6, Bing 22/09/2023 | A |
| Ser citado por terceiros **de forma legítima**: imprensa local, entidade do setor, página da licenciada parceira, diretório real em que o negócio de fato caiba | F2 descreve que a IA mostra o que se diz pela web; BrightLocal mostra diretórios e redes entre as fontes locais (EUA) | A (descrição) + B (EUA) — **hipótese a testar** no Brasil; depende de contato com terceiros, fora da rodada |
| Considerar vídeo e rede social como formatos que a Visão geral cita no Brasil | Ahrefs 23/10/2026 | B (sem recorte local) — hipótese |
| O perfil de empresa, o Bing Places e as avaliações são **da licenciada**; o site ajuda a parceira a mantê-los corretos, com autorização dela | F2; Microsoft 10/02/2026; item 2 da rodada | A |

### 7.2 O que NÃO fazer

| Não fazer | Base | Classe |
|---|---|---|
| Comprar citação, menção, publicação paga com link ou vaga em "ranking" | F9, F2 | A |
| Combinar troca de rankings ou de links | F9 | A |
| Declarar-se "a melhor dedetizadora" em lista própria. Além do risco de não render (seção 5), o site não é dedetizadora, e autoelogio sem prova encosta em propaganda enganosa (ver `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`) | Lily Ray (B pequena, software); item 2 | B fraca + restrição |
| Criar `llms.txt`, páginas "só para IA", texto picado ou marcação especial esperando citação | F2; Ahrefs | A + B |
| Texto escondido ou instrução para modelo dentro da página | F9 (manipular resposta de IA é spam) | A |
| Inflar o texto com citações e estatísticas sem fonte para "parecer citável" | Artigo da KDD não sustenta isso para o Google; propaganda de controle de pragas tem regra própria | — |
| Marcar o gerador de leads como negócio local nos dados estruturados ou em diretório | Item 2 da rodada | restrição |
| Vender ao parceiro "posição nº 1 na IA" | Seção 4.5 | B |

### 7.3 Como medir

**Pelo Search Console (quando houver site e conta do owner; a sessão não abre o painel):**

1. Relatório de desempenho de IA generativa (Busca): impressões por página, país, aparelho e data. Serve para saber
   **quais páginas** aparecem em resposta de IA. Não dá a consulta nem o clique (F7).
2. Relatório de Desempenho comum, tipo "Web": cliques e consultas, já com a IA dentro (F1, F7). Não somar com o
   relatório do passo 1.
3. Queda de CTR com posição estável numa consulta informativa é compatível com resumo de IA acima, mas o painel não
   prova isso; conferir a busca à mão.
4. Bing Webmaster Tools → "AI Performance": citações no Copilot e as frases de busca que o modelo usou (Microsoft,
   10/02/2026). É o único painel oficial que mostra consultas de fundamentação. Exige conta: ação do owner.

**Roteiro manual (para o owner rodar; nenhuma pergunta foi feita a assistente nesta rodada):**

- Conjunto fixo de perguntas reais (o roteiro de 30 perguntas previsto em
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` pode servir também para a Busca
  do Google e o Modo IA).
- Para cada pergunta, **várias execuções** em dias diferentes, em janela anônima e, se possível, de mais de um ponto
  da cidade. Uma execução por mês não basta (seção 4.5). Quantas são necessárias: **não sei**; os autores do estudo B
  também dizem que não sabem.
- Registrar: data e hora; motor (Visão geral, Modo IA, Gemini, Copilot, Perplexity); logado ou não; local mostrado;
  se houve resposta de IA; empresas nomeadas; URLs citadas e o tipo de cada uma (site de empresa, perfil no mapa,
  diretório, avaliação, imprensa, vídeo, rede social, órgão público); se o nosso domínio foi citado; se a parceira
  foi nomeada.
- Métrica: **percentual de execuções** em que o domínio é citado e em que a parceira é nomeada, por pergunta e por
  motor. Nunca "posição".
- O primeiro uso do roteiro é responder ao que este guia não sabe: a busca de contratação em São Paulo dispara
  resposta de IA? Que tipo de fonte ela cita?

---

## O que é consenso (só classe A, ou duas fontes B independentes)

1. **[A]** No Google não há requisito extra nem otimização especial para a Visão geral ou o Modo IA; a página precisa
   estar indexada e apta a snippet (F1, F2).
2. **[A + B]** `llms.txt`, arquivo "para IA", marcação especial e texto picado não são usados pelo Google (F2); os
   arquivos quase não são pedidos por robôs (Ahrefs, 137 mil domínios).
3. **[A]** `nosnippet` e `max-snippet` limitam o uso do texto como entrada direta dos recursos de IA; `noindex` tira
   da busca; o controle do Search Console exclui só dos recursos de IA; `Google-Extended` não afeta inclusão nem
   ranqueamento na Busca (F4, F5, F6).
4. **[A]** O Search Console mostra impressões em recursos de IA por página, país, aparelho e data, sem consulta e sem
   clique separado; esses dados já estão dentro do relatório "Web" (F7, F8).
5. **[A]** Visão geral criada por IA no Brasil desde 15/08/2024; Modo IA em português do Brasil a partir de
   08/09/2025 (F10, F11).
6. **[A]** Manter o Perfil da Empresa atualizado é a única orientação oficial do Google para negócio local em IA (F1,
   F2, F3).
7. **[A]** Tentar manipular respostas de IA é spam para o Google; compra e troca excessiva de links também (F9).
8. **[A, por motor]** Perplexity, Apple, Anthropic e Google separam o robô ou token de busca do de treino; bloquear o
   de treino não tira o site da busca (seção 3). No Bing, `NOARCHIVE` tira o conteúdo das respostas de IA e `NOCACHE`
   o reduz a URL, título e trecho (Bing, 2023 — pode estar desatualizada; a confirmação de 2026 veio só por
   reportagem, porque a página oficial das diretrizes não abriu).
9. **[B × 2, EUA]** Quando há resumo de IA, o clique nos resultados é menor (Pew, painel de usuários; Ahrefs e Seer,
   dados de Search Console). Vale a **direção**, não o número; a causa está em "disputado".
10. **[B × 2]** As respostas de IA variam muito entre execuções; mede-se frequência, não posição (SparkToro/Gumshoe;
    BrightLocal).
11. **[B × 2, países diferentes]** YouTube aparece entre as fontes mais citadas nos resumos de IA do Google (Ahrefs,
    Brasil, 23/10/2026; Pew, EUA, 22/07/2025, que o lista com Wikipedia e Reddit).

Ficou **fora** do consenso, por depender de uma fonte "B fraca": "a maior parte das citações da Visão geral não vem
dos 10 primeiros resultados" (Ahrefs 02/03/2026 é B; BrightEdge não expõe amostra).

## O que é disputado (dois lados, com fonte)

1. **Tamanho e causa da queda de cliques.** Ahrefs: −34,5% (2025) e −58% (2026) na 1ª posição; Seer: −61%; Pew: 8%
   contra 15% de visitas com clique. **Do outro lado:** Semrush mediu que a taxa sem clique das mesmas palavras-chave
   não subiu depois do resumo (33,75% → 31,53%); a própria Ahrefs mostra que o CTR sem resumo também caiu pela
   metade; e o Google afirma, sem publicar dado, que os cliques restantes são de "maior qualidade" (F3).
2. **Quanto a citação coincide com o ranqueamento.** Ahrefs: 76% (julho de 2025) e 38% (março de 2026) nos 10
   primeiros; BrightEdge: 54,5% em qualquer posição e 16,7% nos 10 primeiros. Métodos diferentes; as próprias fontes
   dizem que não são comparáveis.
3. **Estruturar o texto para IA.** Microsoft: títulos, perguntas e respostas, listas, tabelas e esquema ajudam a IA a
   referenciar (10/02/2026 e 08/10/2025). Google: não é preciso picar, reescrever nem usar esquema especial (F2).
   Valem para motores diferentes; não há dado de nenhum dos dois.
4. **Acrescentar citações e estatísticas ao texto.** Artigo da KDD 2024: até ~+41% de visibilidade em motor simulado.
   Google: não reescrever para IA (F2). Sem teste independente em motor atual.
5. **Lista própria com a marca em primeiro.** Peec: ainda rende citação (~11% das citações de listas, sem correção em
   12 semanas). Lily Ray: a lista é citada, mas em 69% dos casos a marca autora não é recomendada. Só software.
6. **Busca local dispara resumo de IA?** Whitespark (EUA, maio de 2025, 540 buscas): 15% nas buscas de contratação.
   Texto de 2026 visto só em resultado de busca fala em 88% (não aberto). Sem dado do Brasil.
7. **De onde a IA tira a empresa local.** BrightLocal: Perfil da Empresa ~28,5% e sites das empresas 42% das citações,
   somando três plataformas. Steady Demand (não aberta): ~80% do Modo IA em Maps/Perfil. O Google não documenta.
8. **Peso do Reddit e de fóruns.** Alto nos estudos dos EUA (Peec; Pew junta Wikipedia, YouTube e Reddit em 15%).
   No Brasil, 6º lugar com 3,3% do top 100 (Ahrefs).

## O que não sei

1. Se as buscas de contratação de dedetização em São Paulo ("dedetização + bairro", "dedetizadora 24 horas") mostram
   Visão geral criada por IA, e com que frequência. O item 4 pode observar ao vivo.
2. Que fontes a IA do Google cita para dedetização no Brasil (site de empresa, perfil no mapa, diretório, Reclame
   Aqui, vídeo). Nenhum estudo aberto cobre controle de pragas nem serviço local brasileiro.
3. Se um site intermediário, que não executa o serviço, chega a ser citado em busca local, ou se só as empresas
   aparecem.
4. Como o Google escolhe e ordena as empresas locais numa resposta de IA; que peso têm avaliações e completude do
   perfil. Não há documentação.
5. O efeito sobre cliques no Brasil em busca comercial ou local, com método exposto.
6. Quanto o Modo IA é usado no Brasil; se o agendamento de serviço local e a ligação automática a negócios existem
   aqui.
7. O texto atual das diretrizes do Bing (a página não abriu) e quanto Copilot e Perplexity pesam na busca de serviço
   local no Brasil.
8. Como o aplicativo Gemini escolhe fontes para pedido local. Só sei que `Google-Extended` governa treino e
   fundamentação no Gemini (F5).
9. Quantas execuções por pergunta bastam para uma medição confiável de aparição.
10. Se os achados do artigo da KDD (2023–2024) valem em algum motor de 2026.
11. As datas de publicação e de última alteração de F1, F2, F4, F5 e F9 (as páginas não mostram).

## Fontes que tentei abrir e não abriram

| Fonte | O que houve | Consequência |
|---|---|---|
| https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a (e a variante `webmaster-guidelines-30fba23a`) | Só o título carregou (página montada por script) | Diretrizes atuais do Bing ficam "não conclusivo"; usei os dois textos oficiais de blog e marquei a reportagem como segunda mão |
| https://www.steadydemand.com/?p=4932, `?p=4957`, `?p=4964` | Conexão recusada nas três | Estudo de citações locais do Modo IA marcado "não aberta"; fora das regras |
| https://searchengineland.com/google-ai-overviews-cite-self-serving-listicles-recommend-competitors-480573 | Erro 403 | Abri a fonte primária (texto da autora, 17/06/2026) |
| https://developers.google.com/search/docs/appearance/ai-features?hl=pt-br | Abriu, mas devolveu o texto em inglês | Citações de F1 ficaram em inglês |
| F1, primeira tentativa de reprodução integral | A ferramenta de leitura recusou copiar a página inteira | Resolvido com pedidos de trecho curto, em duas chamadas |

Vistas só em resultado de busca, **não abertas e não usadas como base**: estudo da SE Ranking sobre `llms.txt`
(~300 mil domínios); Semrush, 325 mil perguntas em três motores; "Local SEO Data" (junho de 2026); Near Media;
Similarweb (43% das buscas nos EUA com resumo); SISTRIX (Alemanha); reexecução da Ahrefs com dados de junho de 2026
(texto em japonês); BrightEdge de fevereiro de 2026 (17%); Scrunch; atualização da Seer até fevereiro de 2026;
Tinuiti; Wellows; Meltwater; texto de 2026 com "88% das buscas de serviço local"; anúncio oficial do "Ask Maps".
