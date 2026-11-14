# Guia (a) — Como se ranqueia um serviço local na busca orgânica do Google, hoje

- **Escopo:** busca orgânica do Google (os "links azuis"), para um site novo, em português, que capta contatos de quem
  procura dedetização em São Paulo (capital) e os repassa a empresas licenciadas. O site **não presta o serviço**
  (intermediário, diretório ou comparador). Mapa e perfil de empresa ficam no guia (b); respostas de IA, no guia (c).
- **Leitura das fontes:** sexta, 13/11/2026, das 19:38 às 19:57; guia gravado às 20:05 (Brasília, saída de
  `TZ=America/Sao_Paulo date`). Toda "data de leitura" deste guia é 13/11/2026.
- **Estado:** segunda passada em 14/11/2026 (relatório `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_item3_guias_a_b.md`: aprovado com ressalvas; 12 de 12 no sorteio); correções aplicadas por corretor em 14/11/2026 às 01:46 (Brasília, saída de `TZ=America/Sao_Paulo date`; registro em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes2_item3_guias_a_b.md`), sem nova leitura.
- **Como li:** só por busca na web e leitura de página pública. A ferramenta de leitura devolve o texto em inglês mesmo
  quando peço a versão em português; por isso as citações literais estão **em inglês, com tradução minha ao lado**.
  Só está entre aspas o trecho que conferi em **duas leituras separadas** da página oficial. O que li uma vez só está
  resumido com as minhas palavras e marcado "(1 leitura)".
- **O que este guia não faz:** não diz "quem aparece" em busca nenhuma (isso é o item 4, visto no navegador); não traz
  número do Brasil, porque não achei nenhum estudo com dado brasileiro; não é parecer jurídico.

**Classes de evidência** (regra da rodada, `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`):

| Classe | O que é | Vira regra? |
|---|---|---|
| A | Documentação oficial do Google, lida na fonte | sim |
| B | Estudo com amostra, método e dado expostos | sim, com o limite da amostra |
| C | Relato de praticante ou jornalismo com o caso à vista; autor não vende o método | só hipótese a testar |
| D | Vendedor de curso, ferramenta ou agência | não; é "alegação" |

**Quem ganha:** "Google" quer dizer que a fonte é o próprio Google, que tem interesse em resultados sem manipulação e
em que o dono de site siga as regras dele; não vende o método, mas também não conta tudo o que usa. Quase todo estudo
com dado (classe B) deste guia é de **empresa que vende ferramenta de SEO**: o dado pode ser conferido, o interesse
fica anotado.

**Abreviação de endereço:** `D:` = `https://developers.google.com/search/docs/`. A lista completa de endereços está
no fim.

---

## Em uma página — o que um iniciante precisa saber

| # | Regra | Classe |
|---|---|---|
| 1 | O Google não vende posição no orgânico e não garante rastrear, indexar nem mostrar página alguma, mesmo que ela siga todas as regras | A |
| 2 | Há três camadas: requisitos técnicos mínimos, políticas de spam (o que derruba) e boas práticas (o que ajuda). Não existe "segredo" que ponha um site em primeiro | A |
| 3 | A política de spam cita, como exemplo de "página de entrada" (doorway), páginas voltadas a regiões ou cidades que afunilam o usuário para uma página só (texto da política). **Aplicação ao projeto, inferência minha (seção 2.2): página por bairro em que só muda o nome do bairro cai nessa definição** | A (o texto da política) + inferência minha (a aplicação) |
| 4 | Gerar muitas páginas sem valor próprio é "abuso de conteúdo em escala", feito por pessoa, por IA ou pelos dois. O volume não é a infração; a falta de valor é | A |
| 5 | Comprar ou vender link para ranquear e trocar links em excesso é spam. Link pago é permitido como publicidade se levar `rel="sponsored"` ou `rel="nofollow"` | A |
| 6 | A consequência de violar é ser rebaixado ou sumir do resultado, por sistema automático ou por ação manual de um revisor | A |
| 7 | O Google diz priorizar conteúdo útil, confiável e feito para pessoas. "E-E-A-T" (experiência, especialidade, autoridade, confiança) não é um fator isolado, mas a confiança é o centro, e temas que afetam saúde ou segurança recebem mais peso | A |
| 8 | Um intermediário tem de dizer quem é: página "quem somos", autoria, como o conteúdo foi feito. O Google pede isso ao dono de site; fingir ser a dedetizadora é o oposto | A (o pedido) + inferência minha (a aplicação) |
| 9 | Na página: um título único e descritivo, um título principal visível, descrição única, endereço legível, links internos de verdade (`<a href>`) com texto descritivo. Não há contagem mágica de palavras, de títulos nem de links; palavra-chave no domínio quase não conta; a meta tag de palavras-chave não é usada | A |
| 10 | Dados estruturados só do que está visível e é verdadeiro. Estrelas de avaliação que a empresa controla sobre si mesma não valem. O resultado rico de perguntas frequentes (FAQ) deixou de existir em maio de 2026 | A |
| 11 | O Google indexa pela versão de celular; HTTPS e os indicadores de velocidade (Core Web Vitals) entram na conta, mas não passam por cima de relevância | A |
| 12 | Links de outros sites continuam sendo um sinal declarado pelo Google. Quanto pesam, ninguém de fora sabe: um estudo (Ahrefs, 2025, Estados Unidos) mostra correlação fraca (0,25 no geral; 0,33 em buscas locais) | A (é sinal) + B (o tamanho) |
| 13 | Prazo: o Google não dá prazo. Uma mudança leva de horas a meses para aparecer. Num estudo da Ahrefs de 2025 (abrangência — país — da amostra não informada pela fonte), 1,74% de 1 milhão de páginas novas chegaram aos dez primeiros em um ano | A + B |
| 14 | Em busca com intenção local, o resultado muda com a localização de quem busca e os recursos da página de resultado mudam com a busca (A). Que mapa e anúncios fiquem acima do orgânico **não está na fonte A**: é premissa minha, a conferir na observação ao vivo do item 4. Os estudos de clique de classe B (Near Media, Backlinko, Pew, SparkToro) são dos Estados Unidos e da Europa; o da First Page Sage é classe D e não sustenta esta regra; não achei dado do Brasil | A (o mecanismo) + B (os cliques) + premissa minha (mapa e anúncios acima do orgânico) |
| 15 | O placar é o Search Console, que só o dono do site abre. Ferramenta de terceiro não tem dado interno do Google, e raspar o resultado para checar posição está na lista de práticas vedadas | A |

---

## 1. Como a busca funciona e o que o Google diz usar

### 1.1 As três etapas e as três camadas de regra

| Afirmação | O que fazer num site de leads de dedetização em SP | Fonte | Data da fonte | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|
| A busca tem três etapas: rastrear (achar e baixar a página), indexar (entender e guardar) e servir (escolher o que mostrar). Nem toda página rastreada é indexada | Tratar "foi indexada?" como a primeira medição, antes de "em que posição?" | `D:fundamentals/how-search-works` | página viva, sem data | A | Google | — |
| "Google doesn't guarantee that it will crawl, index, or serve your page" (o Google não garante rastrear, indexar nem servir a sua página), mesmo seguindo as regras | Não prometer a parceiro nenhum que a página "vai aparecer" | idem | idem | A | Google | Citação conferida em 2 leituras |
| O Google não aceita pagamento para rastrear mais nem para ranquear melhor | Anúncio pago é outro produto; não compra orgânico | idem; `D:fundamentals/do-i-need-seo` | idem | A | Google | — |
| A maior parte das páginas é achada por links de outras páginas, não por envio manual | Site novo sem nenhum link de fora demora a ser achado: enviar o sitemap pelo Search Console (o owner) e conseguir ao menos alguns links legítimos | `D:fundamentals/how-search-works`; `D:fundamentals/seo-starter-guide` | idem | A | Google | (1 leitura) |
| A relevância depende de "centenas de fatores", entre eles a localização, o idioma e o aparelho de quem busca; a busca por oficina de bicicleta dá resultado diferente em Paris e em Hong Kong | A mesma busca por "dedetizadora" dá resultado diferente em Santana e em Santo Amaro. Não existe "a posição" única | `D:fundamentals/how-search-works` | idem | A | Google | Conferido em 2 leituras (resumo) |
| O Google resume o ranqueamento em cinco grupos: sentido da busca (intenção), relevância, qualidade, usabilidade e contexto (localização, histórico, configurações) | Escrever para a intenção de quem quer contratar; o resto deste guia detalha cada grupo | `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/` | página viva, sem data | A | Google | — |
| Para medir relevância o Google usa também "aggregated and anonymized interaction data to assess whether search results are relevant to queries" (dados de interação agregados e anônimos) | Página que promete e não entrega tende a perder; não há o que "otimizar" além de entregar o que a busca pede | idem | idem | A | Google | Citação conferida em 2 leituras. É a confirmação oficial de que comportamento do usuário entra; detalhes na seção 6.3 |
| Um dos fatores de qualidade é outros sites conhecidos apontarem ou se referirem ao conteúdo | Ver seção 6 | idem | idem | A | Google | — |
| Camada 1, requisitos técnicos: o mínimo para a página poder aparecer (o robô do Google não bloqueado, página que funciona, conteúdo indexável) | Conferir no protótipo: sem bloqueio no `robots.txt`, sem `noindex` | `D:essentials`; os três requisitos do parêntese estão em `D:essentials/technical` | página viva, sem data | A | Google | — |
| Camada 2, políticas de spam: o que leva a posição mais baixa ou à remoção | Seção 2 | `D:essentials/spam-policies` | idem | A | Google | — |
| Camada 3, boas práticas: conteúdo útil e feito para pessoas; palavras que as pessoas usam, postas em lugares de destaque (título, título principal, texto alternativo, texto de link); links rastreáveis; divulgar o site | Seções 3 e 4 | `D:essentials` | idem | A | Google | (1 leitura) |
| O guia de iniciantes diz que não há segredo que ponha o site em primeiro automaticamente, e lista mitos: meta tag de palavras-chave não é usada; repetir palavra cansa e é spam; palavra no domínio ou no endereço quase não tem efeito; não há contagem mágica de palavras; ordem dos títulos não importa; E-E-A-T não é fator direto; conteúdo duplicado não gera ação manual | Não gastar tempo com nada disso; desconfiar de quem vende qualquer um desses itens | `D:fundamentals/seo-starter-guide` | idem | A | Google | Conferidas em 2 leituras: "Google Search doesn't use the keywords meta tag."; "there's no magical word count target, minimum or maximum"; palavra no domínio com "hardly any effect beyond appearing in breadcrumbs" |

### 1.2 Os sistemas de classificação que o Google nomeia

Fonte: `D:appearance/ranking-systems-guide` (página viva, sem data; lida 2 vezes). Classe A; quem ganha: Google.

| Sistema | O que o Google diz | O que significa aqui |
|---|---|---|
| Análise de links e PageRank | PageRank é "one of our core ranking systems used when Google first launched" (um dos sistemas centrais desde o lançamento); a página diz que ele mudou muito e continua em uso | Link de outro site ainda conta (seção 6) |
| Diversidade de sites | "we generally won't show more than two web page listings from the same site in our top results" (em geral, no máximo duas páginas do mesmo site no topo) | Dezenas de páginas praga × bairro não ocupam a primeira tela de uma mesma busca; cada página disputa a busca dela |
| Domínio de correspondência exata | Existe um sistema para não dar crédito demais a domínio feito para casar com a busca | Comprar um domínio do tipo "dedetizadora-bairro-sp" não é atalho; decisão de domínio fica com o owner |
| Sistema de avaliações (reviews) | Premia análise original; avalia conteúdo próprio do site que recomenda ou compara, inclusive serviços e empresas; não avalia a avaliação deixada por usuário | Se o site publicar "comparativo de dedetizadoras", esse conteúdo é julgado por originalidade e análise (`D:appearance/reviews-system`, 1 leitura) |
| Conteúdo original, atualidade, deduplicação, correspondência neural, BERT, RankBrain, ranqueamento de trechos | Sistemas de entendimento de linguagem e de escolha entre páginas parecidas | Páginas quase iguais são deduplicadas: só uma tende a aparecer |
| Detecção de spam (SpamBrain) | Vários sistemas para o que viola as políticas | Seção 2 |
| Conteúdo útil (antigo "helpful content") | Aposentado como sistema separado: em março de 2024 passou a fazer parte dos sistemas centrais | "Conteúdo útil" não é um filtro à parte; está em toda atualização central |
| Notícias locais | É o único sistema "local" da página | **A página não descreve como o orgânico trata serviço local.** O que há está na seção 7 |

A página não menciona "experiência na página", "Core Web Vitals" nem "compatível com celular" (conferido); esses
temas estão em `D:appearance/page-experience` (seção 4).

### 1.3 O que mudou em 2025–2026

Atualizações de classificação, do painel oficial `https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history`
(lido 2 vezes, também em `https://status.search.google.com/summary`). Classe A; quem ganha: Google. As datas são de
início; a duração é a que o painel mostra.

| Atualização | Início | Duração no painel |
|---|---|---|
| Central (core) de março de 2025 | 13/03/2025 | 13 dias e 21 horas |
| Central de junho de 2025 | 30/06/2025 | 16 dias e 18 horas |
| De spam de agosto de 2025 | 26/08/2025 | 26 dias e 15 horas |
| Central de dezembro de 2025 | 11/12/2025 | 18 dias e 2 horas |
| Do Discover de fevereiro de 2026 | 05/02/2026 | 21 dias e 17 horas |
| De spam de março de 2026 | 24/03/2026 | 19 horas e 30 minutos |
| Central de março de 2026 | 27/03/2026 | 12 dias e 4 horas |
| Central de maio de 2026 | 21/05/2026 | 11 dias e 21 horas |
| De spam de junho de 2026 | 24/06/2026 | 2 dias e 1 hora |
| De spam de agosto de 2026 | 18/08/2026 | 2 dias e 16 horas |
| De spam de setembro de 2026 | 24/09/2026 | 13 dias e 16 horas |
| **Central de novembro de 2026** | **10/11/2026** | **sem duração no painel na hora da leitura (aparece como "Information")** |

**Atenção para o item 4 da rodada:** há uma atualização central aberta desde 10/11/2026, três dias antes desta
leitura. O Google recomenda "waiting at least a full week after a core update completes" (esperar ao menos uma semana
depois do fim) antes de analisar (`D:appearance/core-updates`, 2 leituras). As posições vistas neste fim de semana
podem mudar.

Mudanças de documentação e de política, do registro oficial `https://developers.google.com/search/updates` (classe A;
datas conferidas em 2 leituras, salvo marcação):

| Data | O que mudou | Efeito para este projeto |
|---|---|---|
| 05/03/2024 (antes do período; base das regras atuais) | Três políticas novas de spam: conteúdo em escala, domínio expirado, reputação de site (`https://developers.google.com/search/blog/2024/03/core-update-spam-policies`, 1 leitura) | São as políticas da seção 2 |
| 21/01/2025 | Política de abuso de reputação de site reescrita com as perguntas frequentes | Baixo |
| 22/01/2025 | Trilha de navegação (breadcrumb) passa a aparecer só no computador, não no celular | Seção 5 |
| 21/05/2025 | Entram as páginas sobre recursos de IA e sobre conteúdo feito com IA generativa (1 leitura) | Seção 3 |
| 16/06/2025 | Dados do Modo IA passam a contar nos totais do Search Console (1 leitura) | Seção 8 |
| 09/12/2025 | A página de atualizações centrais passa a dizer que há atualizações menores, não anunciadas, e que a melhora de um site pode ser reconhecida sem esperar a próxima grande | Seção 9 |
| 13/04/2026 | Nova seção sobre "sequestro do botão voltar" nas práticas maliciosas | Não usar script que prenda o visitante |
| 14 e 23/04/2026 | Denúncia de spam pode levar a ação manual (1 leitura) | Concorrente pode denunciar página de entrada |
| 08/05 e 15/06/2026 | Aviso de fim e depois remoção da documentação do resultado rico de FAQ, que deixou de aparecer na busca em 07/05/2026 | Seção 5 |
| 15/05/2026 | As políticas de spam passam a valer também para as respostas de IA generativa da busca; novo guia de otimização para IA | Guia (c) |
| 05/06/2026 | Nova página sobre ferramentas, serviços e conselhos de SEO de terceiros; a página "você precisa de um SEO?" foi simplificada | Seções 8 e 9 |
| 24/07/2026 | Nova regra nos trechos de avaliação: proibidas avaliações falsas ou incentivadas sem aviso | Seção 5 |
| 28/08/2026 | Política de reputação de site com aplicação diferente no Espaço Econômico Europeu | Nenhum (Brasil) |
| 08 e 18/09/2026 | Documentadas as "unidades de agregador e de fornecedor", inclusive para buscas de empresa local | As unidades de agregador e de fornecedor constam só para o Espaço Econômico Europeu; a mesma página lista outros recursos (não essas unidades) para a Turquia e a África do Sul; não cita o Brasil (`D:appearance/aggregator-features`, 2 leituras: a segunda na correção de 13/11/2026) |
| 01/10/2026 | O guia de conteúdo com IA passa a apontar as seções das diretrizes dos avaliadores sobre conteúdo em escala e conteúdo de pouco esforço | Seção 3 |

---

## 2. Políticas de spam do Google, lidas na fonte

Fonte de toda a seção: `D:essentials/spam-policies` (página viva, sem data; lida 4 vezes). Classe A; quem ganha: Google.
A página lista, nesta ordem: camuflagem (cloaking), abuso de páginas de entrada, abuso de domínio expirado, conteúdo
invadido, texto e links ocultos, excesso de palavras-chave, spam de links, tráfego gerado por máquina, práticas
maliciosas, funcionalidade enganosa, abuso de conteúdo em escala, raspagem, política de reputação de site,
redirecionamentos enganosos, afiliação sem valor, spam gerado por usuário, e "outras práticas" (remoções legais,
dados pessoais, burla de política, golpe e fraude).

### 2.1 As políticas que tocam este projeto

| Política | Texto curto que decide (inglês, com tradução) | O que fazer num site de leads de dedetização em SP | Observação |
|---|---|---|---|
| Páginas de entrada (doorway abuse) | "Doorway abuse is when sites or pages are created to rank for specific, similar search queries." (quando sites ou páginas são criados para ranquear em buscas específicas e parecidas) | Não criar página cujo único papel é pegar uma busca e empurrar para outra | Citação conferida em 2 leituras |
| Idem, exemplo de região | "Having multiple domain names or pages targeted at specific regions or cities that funnel users to one page" (vários domínios ou páginas voltados a regiões ou cidades que afunilam os usuários para uma página só) | **É o retrato de 96 páginas de bairro que levam todas ao mesmo botão de WhatsApp sem dizer nada próprio.** Ver 2.2 | Conferida em 3 leituras |
| Idem, exemplo de hierarquia | "Creating substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy" (páginas muito parecidas, mais próximas de resultados de busca do que de uma hierarquia navegável) | As páginas de bairro têm de estar numa estrutura que uma pessoa navega (região → bairro; praga → bairro), não soltas | Conferida em 2 leituras |
| Idem, o dano | A página diz que elas levam o usuário a páginas intermediárias menos úteis que o destino final | A página de bairro tem de ser o destino, não a escala | (1 leitura; resumo) |
| Conteúdo em escala (scaled content abuse) | "Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings" (muitas páginas geradas com o propósito principal de manipular o ranqueamento) | O teste é o propósito e o valor, não a ferramenta | Conferida em 2 leituras; a frase continua dizendo "e não de ajudar usuários" |
| Idem, tanto faz quem faz | "creating large amounts of unoriginal content that provides little to no value to users, no matter how it's created." (grande volume de conteúdo sem originalidade e de pouco ou nenhum valor, não importa como é criado) | Texto de bairro escrito à mão mas genérico também cai | Conferida em 2 leituras |
| Idem, exemplo de IA | "Using generative AI tools or other similar tools to generate many pages without adding value for users" (usar IA generativa para gerar muitas páginas sem acrescentar valor) | IA pode ajudar a redigir; cada página precisa de dado e revisão próprios | Conferida em 3 leituras |
| Excesso de palavras-chave | Exemplo: "Blocks of text that list cities and regions that a web page is trying to rank for" (blocos de texto listando cidades e regiões em que a página quer ranquear) | **Não pôr rodapé com a lista dos 96 distritos** nem parágrafo "atendemos Moema, Pinheiros, Lapa…" | Conferida em 2 leituras. Outro exemplo da mesma política: listas de telefones sem valor (1 leitura) |
| Spam de links: compra e venda | "Buying or selling links for ranking purposes." (comprar ou vender links para ranquear). Inclui pagar por link ou por publicação com link, trocar produto ou serviço por link | Não comprar link; não vender link no site para parceiro | Conferida em 2 leituras |
| Idem, troca | "Excessive link exchanges ("Link to me and I'll link to you") or partner pages exclusively for the sake of cross-linking" (troca excessiva de links ou páginas de parceiros só para cruzar links) | **Cuidado com a página "parceiros":** listar licenciadas por um critério útil ao usuário é diretório; exigir link de volta de cada parceira é troca | Conferida em 2 leituras. A palavra é "excessiva": o limite não é numérico |
| Idem, link pago legítimo | A página diz que comprar e vender link é parte normal da economia da web para publicidade e patrocínio, desde que o link leve `rel="nofollow"` ou `rel="sponsored"` | Se a licenciada paga para aparecer, o link do site para ela é publicidade: marcar `rel="sponsored"` | Conferida em 2 leituras. Liga com a regra de propaganda do item 2(b) da rodada |
| Idem, outros exemplos | Programas automáticos de criar links; exigir link em contrato ou termo de uso; links de diretórios ou favoritos de baixa qualidade; links em rodapés e modelos espalhados por vários sites; comentários de fórum com link otimizado; texto patrocinado com link que passa crédito | Não exigir, no contrato com a licenciada, link para o site; não cadastrar o site em massa em diretórios | (1 leitura; resumo) |
| Reputação de site | "The site reputation policy applies where third-party content is published on a host site mainly" (aplica-se quando conteúdo de terceiros é publicado num site hospedeiro principalmente) por causa dos sinais de ranqueamento que o hospedeiro já tem | Não alugar pasta de site de jornal ou de entidade para hospedar as páginas de dedetização | Conferida em 3 leituras (trecho). Nome atual: "política de reputação de site" |
| Domínio expirado | "Expired domain abuse is where an expired domain name is purchased and repurposed primarily to manipulate search rankings" (comprar domínio vencido e reaproveitá-lo principalmente para manipular o ranqueamento) | Não comprar domínio antigo de outro assunto pela "autoridade" | Conferida em 2 leituras |
| Afiliação sem valor (thin affiliation) | "Thin affiliation is the practice of publishing content with product affiliate links" (publicar conteúdo com links de afiliado de produto) copiando descrição e avaliação do vendedor, sem acrescentar nada | A política fala de **produto**; por analogia, um diretório que só copia a descrição que a dedetizadora dá de si não acrescenta valor. Acrescentar: conferência da licença, preço com fonte, comparação | Conferida em 3 leituras (trecho). A analogia com serviço é inferência minha |
| Texto e links ocultos | "Hidden text or link abuse is the practice of placing content on a page in a way solely to manipulate search engines" (pôr conteúdo na página só para manipular o buscador) | Sanfona, abas e texto para leitor de tela são permitidos (a página diz); texto branco em fundo branco, não | Conferida em 2 leituras |
| Raspagem e tráfego de máquina | Copiar conteúdo de outros sem acrescentar valor é vedado; enviar buscas automáticas ao Google, inclusive raspar o resultado para checar posição, também | Não copiar texto nem avaliação de site de dedetizadora; não rodar robô de posição contra o Google | (1 leitura; resumo) |
| Golpe e fraude; burla de política | A página tem essas duas subseções em "outras práticas que podem levar a rebaixamento ou remoção". **Li os títulos, não o texto delas** | O site não se apresenta como a dedetizadora (regra do projeto e do item 2 da rodada, não citação desta política) | Só os títulos conferidos (2 leituras) |

**Consequências** (conferidas em 3 leituras): a página diz que a detecção é por sistemas automáticos e, quando
preciso, por revisão humana que pode resultar em **ação manual**; e que "Sites that violate our policies may rank
lower in results or not appear in results at all." (sites que violam podem ficar mais abaixo ou não aparecer). Pelo
que sei, a ação manual é comunicada no Search Console, que só o owner abre; **não abri a página desse relatório nesta
leitura**.

### 2.2 O que isso significa para dezenas de páginas praga × bairro

O Google **não** publica uma lista do que torna legítima uma página por bairro. O que existe é a definição acima e as
perguntas de autoavaliação da seção 3. A tabela abaixo é **inferência minha a partir desses textos (classe A para o
texto, hipótese para a aplicação)**; não é regra do Google.

| Sinal de página de entrada (o texto da política) | Sinal de página legítima (o inverso, mais as perguntas de conteúdo útil) |
|---|---|
| Só muda o nome do bairro; o resto é igual | Cada página tem algo que só ela pode dizer: quais licenciadas atendem ali, com a licença conferida; o tipo de imóvel e a praga mais comum ali, com fonte; a regra que vale ali, se houver e com fonte (o exemplo "obrigação de restaurante na capital" é hipotético, meu, sem fonte conferida: não publicar sem a norma à vista) |
| Todas levam ao mesmo destino e nenhuma responde nada | A página é o destino: responde a dúvida de quem buscou (preço com fonte, como conferir a licença, o que perguntar) antes de oferecer o contato |
| Existe só para a busca; não há caminho de navegação até ela | Está numa hierarquia navegável (região → bairro; praga → bairro), com trilha e links internos |
| Lista de bairros no rodapé ou em bloco de texto | Bairros aparecem como navegação real (página de região que lista os bairros com link) |
| Dezenas publicadas de uma vez, por modelo | Começar por poucas, onde há dado próprio, e só replicar o que provar ter valor. O ritmo em si não está em documento do Google (seção 10, tática 2.7) |
| A pergunta do Google que resume: o conteúdo oferece valor substancial em comparação com as outras páginas do resultado? Você teria público para ele se a busca não existisse? | Se a resposta for "não" para uma página de bairro, ela não deve existir; um bairro sem nada próprio pode ser coberto pela página da região |

Dois limites honestos: (1) isso reduz o risco, não o elimina, porque quem julga é o sistema do Google e ele não é
público; (2) não sei quantas páginas por bairro um site novo sustenta sem ser tratado como escala: não há número em
fonte A nem B.

---

## 3. Conteúdo: útil, confiável, centrado nas pessoas; E-E-A-T; YMYL; IA; transparência

Fonte principal: `D:fundamentals/creating-helpful-content` (página viva, sem data; lida 3 vezes). Classe A; quem ganha:
Google.

| Afirmação | O que fazer num site de leads de dedetização em SP | Fonte | Classe | Observação |
|---|---|---|---|---|
| Os sistemas são feitos para priorizar informação útil e confiável, criada para beneficiar pessoas, não para manipular ranqueamento | É o critério de corte de cada página | fonte principal | A | — |
| Perguntas de autoavaliação: o conteúdo traz informação, pesquisa ou análise original? "Does the content provide substantial value when compared to other pages in search results?" (valor substancial frente às outras páginas do resultado?) | Cada página precisa de um "a mais" verdadeiro: licença conferida, tabela de preço com fonte, o que a norma exige | fonte principal | A | Citação conferida em 2 leituras |
| Pergunta sobre produção em massa: conteúdo produzido em massa ou terceirizado a muitos autores, ou espalhado por uma rede de sites, de modo que cada página recebe pouco cuidado? | Não montar rede de sites-satélite; revisão humana de cada página | fonte principal | A | Conferida em 2 leituras (resumo) |
| Sinais de conteúdo feito para o buscador: muitos temas na esperança de que algum renda; escrever até uma contagem de palavras; mudar a data sem mudar o conteúdo; deixar o leitor precisando buscar de novo; resumir os outros sem acrescentar | Não fazer nenhum dos cinco | fonte principal | A | (1 a 2 leituras; resumo) |
| E-E-A-T: "Of these aspects, trust is most important." (desses aspectos, a confiança é o mais importante) | Tudo o que o site afirma tem de ser conferível | fonte principal | A | Conferida em 3 leituras |
| "E-E-A-T itself isn't a specific ranking factor" (não é um fator de ranqueamento específico); os sistemas usam uma mistura de sinais que tentam identificar conteúdo com essas qualidades | Não existe "nota de E-E-A-T" a otimizar; quem vende isso vende opinião | fonte principal; `D:fundamentals/seo-starter-guide` | A | Conferida em 2 leituras |
| YMYL ("seu dinheiro ou sua vida"): os sistemas dão ainda mais peso a conteúdo com E-E-A-T forte em temas que podem afetar de modo significativo a saúde, a estabilidade financeira ou a segurança das pessoas, ou o bem-estar da sociedade | Ver o veredito logo abaixo | fonte principal | A | Definição conferida em 2 leituras |
| Avaliadores de qualidade: "Search raters have no control over how pages rank." (não controlam a posição); o dado deles não entra direto nos algoritmos; serve para avaliar se os sistemas funcionam | As diretrizes dos avaliadores descrevem o que o Google quer premiar; não são o algoritmo | fonte principal; `D:fundamentals/using-gen-ai-content` | A | Conferida em 2 leituras |
| "Quem, como e por quê": o Google recomenda deixar claro quem escreveu (autoria, página do autor ou "sobre"), como o conteúdo foi feito (inclusive automação e IA, quando o leitor poderia se perguntar) e por que existe (ajudar pessoas, não atrair busca) | Página "quem somos" com o nome de quem responde pelo site, CNPJ quando houver, como as licenciadas são escolhidas e como o site ganha dinheiro; autoria ou revisão técnica nas páginas de praga; aviso de uso de IA onde couber | fonte principal | A | Uma das perguntas cita literalmente o link para a página do autor ou a página "About" do site (2 leituras) |
| IA generativa: útil para pesquisar e estruturar conteúdo original; gerar muitas páginas sem valor pode violar a política de conteúdo em escala; revisar fatos; a revisão vale também para título, descrição, dados estruturados e texto alternativo | Usar IA como rascunho; toda página revisada por pessoa; nenhuma licença, preço ou norma escrita pela IA sem fonte | `D:fundamentals/using-gen-ai-content` | A | Página criada em 21/05/2025 e atualizada em 01/10/2026 (registro de mudanças). Conferida em 3 leituras |
| A mesma página remete às diretrizes dos avaliadores: seção 4.6.5 (conteúdo em escala) e 4.6.6 (conteúdo principal com pouco ou nenhum esforço, originalidade e valor) | Mesma regra, vista do lado do avaliador | idem | A | Conferida em 2 leituras. **Li a remissão, não o PDF** (ver "não abriram") |
| Avaliações comparativas (ex.: "melhores dedetizadoras de…") são julgadas pelo sistema de avaliações: análise original, de quem conhece o assunto | Se houver lista ou comparação, expor o critério e o que foi conferido; não se autodeclarar "a melhor" | `D:appearance/reviews-system` | A | (1 leitura) |

**Dedetização é YMYL?** A definição do Google (acima, classe A) fala em saúde e segurança das pessoas. Controle de
pragas envolve aplicação de produto químico dentro de casa e pragas ligadas a doenças; por isso **é razoável tratar
como YMYL as páginas que falam de risco à saúde, de produto, de segurança de crianças e animais e de quem está
habilitado a aplicar**. Isso é **inferência minha**: o PDF das Diretrizes dos Avaliadores de Qualidade, que traz os
exemplos e a escala de YMYL, não abriu em forma legível, então não sei como ele classifica serviço doméstico.
Consequência prática, de baixo custo: nessas páginas, fonte oficial para toda afirmação de saúde (norma sanitária,
rótulo, órgão público), revisão por responsável técnico quando houver parceiro que o tenha, e nenhuma promessa do tipo
"sem risco" (o que também é exigência da regra de propaganda do item 2(b)).

**Transparência de um intermediário.** O Google não tem regra específica para "site que repassa contato". O que há,
em classe A: a recomendação de dizer quem é o autor e o site; a diretriz de dados estruturados "Don't impersonate any
person or organization, or misrepresent your ownership, affiliation, or primary purpose." (não se passe por outra
pessoa ou organização nem deturpe a propriedade, a afiliação ou o propósito principal; `D:appearance/structured-data/sd-policies`,
2 leituras); e a política de golpe e fraude. Juntas, apontam na mesma direção das restrições do item 2 da rodada: o
site se apresenta como o que é.

---

## 4. Elementos de página que o Google documenta

Classe A e "quem ganha: Google" em todas as linhas. Páginas vivas, sem data exibida.

| Elemento | O que o Google diz | O que fazer aqui | Fonte | Observação |
|---|---|---|---|---|
| Link de título (o título azul do resultado) | O Google monta o título a partir de: elemento `<title>`, título visual principal, títulos como `<h1>`, `og:title`, texto grande e destacado, outros textos, texto âncora na página, texto de links que apontam para a página, dado estruturado `WebSite`. Pede título em toda página, descritivo e conciso, sem repetição de palavras, distinto por página, com a marca de forma breve | Um `<title>` por página, do tipo "Dedetização de baratas em Pinheiros: preços e empresas licenciadas", coerente com o `<h1>`. O Google pode reescrever | `D:appearance/title-link` | Lista conferida em 2 leituras. **A página não fala em ranqueamento** (conferido): a frase "o título é o elemento mais forte" não tem fonte A |
| Trecho (snippet) e meta descrição | "Snippets are primarily created from the page content itself." (o trecho vem principalmente do conteúdo da página); a meta descrição pode ser usada quando descreve melhor. Sem limite de tamanho, mas é cortada. Descrições iguais em todas as páginas não ajudam; em site grande, gerar por programa é aceitável e incentivado, desde que cada uma seja específica | Meta descrição própria por página, com praga, bairro e o que a página entrega; pode vir de modelo com dados reais | `D:appearance/snippet` | Conferida em 2 leituras. A página não diz que a descrição afeta posição |
| Títulos (`<h1>`, `<h2>`…) | Ajudam o leitor e ajudam o Google a escolher o título; a ordem e a quantidade não importam para a busca | Um título principal claro; subtítulos pelo que o leitor procura | `D:fundamentals/seo-starter-guide`; `D:appearance/title-link` | "Um só H1" é boa prática de redação, não regra do Google |
| Endereços (URLs) | Palavras legíveis em vez de números; hífen em vez de sublinhado; palavras no idioma do público; caracteres acentuados codificados; não usar `#` para trocar conteúdo; evitar muitos endereços para conteúdo igual ou parecido; pastas agrupando temas ajudam em site grande | `/dedetizacao/baratas/pinheiros/` em minúsculas e sem acento; uma página, um endereço | `D:crawling-indexing/url-structure`; `D:fundamentals/seo-starter-guide` | (1 leitura). Atualizada em 23/10/2026 (hífen × sublinhado). Palavra no endereço quase não pesa no ranqueamento (seção 1.1) |
| Links rastreáveis | O Google em geral só segue link que seja elemento `<a>` com atributo `href` | Botão de WhatsApp e navegação como `<a href>`, não como script | `D:crawling-indexing/links-crawlable` | Conferida em 2 leituras |
| Texto âncora | "Good anchor text is descriptive, reasonably concise, and relevant to the page that it's on and to the page it links to." (descritivo, razoavelmente curto e pertinente às duas páginas) | "dedetização de cupins na Lapa" em vez de "clique aqui" | idem | Conferida em 2 leituras |
| Links internos | "Every page you care about should have a link from at least one other page on your site." (toda página que importa deve ter link de pelo menos outra página do site); "There's no magical ideal number of links a given page should contain." (não há número ideal) | Cada página de bairro ligada pela página da região e pela da praga; **o "cinco links" do artigo do owner não tem base** | idem | Conferidas em 2 leituras |
| Links para fora | Citar fonte com link gera confiança; `nofollow` só quando não se confia na fonte; link pago com `sponsored` ou `nofollow`; link de usuário com `ugc` | Link para a norma e para a consulta de licença sem `nofollow`; link pago para parceira com `sponsored` | idem | (1 a 2 leituras) |
| Imagens | Usar elemento `<img>` (imagem de fundo em CSS não é indexada); texto alternativo descritivo, sem empilhar palavras; nome de arquivo curto e descritivo; imagem perto do texto a que se refere | Foto real, se houver, com descrição verdadeira; nada de foto de banco apresentada como "nossa equipe" | `D:appearance/google-images`; `D:fundamentals/seo-starter-guide` | (1 leitura) |
| Duplicidade e página canônica | O Google agrupa páginas iguais ou parecidas e escolhe uma (a canônica). Sinais: redirecionamento (forte), `rel="canonical"` (forte), presença no sitemap (fraco); somam-se. Não usar `robots.txt` nem `noindex` para isso; linkar sempre o endereço canônico. Duplicado não gera ação manual, é só ineficiente | `rel="canonical"` apontando para si em cada página (A). **Inferência minha, não regra do Google:** evitar duas páginas para a mesma busca (ex.: tratar "dedetização Pinheiros" e "dedetizadora Pinheiros" numa página só). A página de canonização só trata de conteúdo duplicado ou muito parecido em endereços diferentes; "uma palavra-chave, uma página" permanece tática de classe D (seção 10, tática 2.1) | `D:crawling-indexing/consolidate-duplicate-urls`; `D:fundamentals/seo-starter-guide` | (1 leitura da primeira; a frase do guia de iniciantes conferida em 2). Atenção: páginas de bairro quase iguais podem ser **agrupadas** e só uma aparecer |
| Sitemap | Arquivo que lista as páginas. Pode ser dispensável em site pequeno (cerca de 500 páginas ou menos) e bem ligado por links; **ajuda em site novo com poucos links de fora**. Enviar "is merely a hint" (é só uma dica). "Google ignores `<priority>` and `<changefreq>` values."; a data `lastmod` só é usada se for confiável. Limite de 50.000 endereços ou 50 MB por arquivo; só endereços canônicos | Gerar `sitemap.xml` com `lastmod` verdadeiro; o owner o envia no Search Console | `D:crawling-indexing/sitemaps/overview`; `D:crawling-indexing/sitemaps/build-sitemap` | Citações conferidas em 2 leituras |
| `robots.txt` | Serve para gerir o rastreamento; "it is not a mechanism for keeping a web page out of Google" (não é o meio de tirar página do Google): endereço bloqueado ainda pode ser indexado se houver link para ele. Para tirar da busca: `noindex` ou senha | Não bloquear CSS nem scripts; usar `noindex` para páginas de obrigado ou de teste | `D:crawling-indexing/robots/intro` | Conferida em 2 leituras |
| Indexação e pedido de rastreamento | "Crawling can take anywhere from a few days to a few weeks." (de dias a semanas); pedir rastreamento não garante inclusão; a ferramenta de inspeção de endereço tem cota; para muitos endereços, sitemap | Depois de publicar (decisão do owner), inspecionar algumas páginas e esperar; não repetir pedidos | `D:crawling-indexing/ask-google-to-recrawl` | Conferida em 2 leituras |
| Indexação pelo celular | "Google uses the mobile version of a site's content, crawled with the smartphone agent, for indexing and ranking." (usa a versão de celular para indexar e ranquear). Mesmo conteúdo, dados estruturados e metadados nas duas versões; recomenda desenho responsivo | Desenho responsivo único; o que não aparece no celular não existe para o Google | `D:crawling-indexing/mobile/mobile-sites-mobile-first-indexing` | Conferida em 2 leituras |
| Experiência na página e Core Web Vitals | "There is no single signal." (não há um sinal único); "Core Web Vitals are used by our ranking systems." (são usados); mas o Google mostra o conteúdo mais relevante "even if the page experience is sub-par" (mesmo com experiência fraca). Perguntas: página segura (HTTPS)? boa no celular? sem intersticial intrusivo? sem excesso de anúncio? conteúdo principal fácil de distinguir? | HTML e CSS leves (o protótipo já é assim), HTTPS, sem janela que cubra a tela | `D:appearance/page-experience` | Conferidas em 2 leituras. Avaliação em geral por página, com alguns sinais do site todo |
| Intersticiais e janelas | Elemento que cobre o conteúdo, em geral promocional, frustra o usuário e dificulta o entendimento da página; preferir faixa pequena; o exigido por lei é isento | **Botão flutuante de WhatsApp pequeno, sim; janela "fale agora" cobrindo a tela ao entrar, não.** O aviso de privacidade em faixa | `D:appearance/avoid-intrusive-interstitials` | (1 leitura). A página não cita aviso de cookies pelo nome |
| JavaScript | O Google processa em três fases (rastrear, renderizar, indexar); a renderização entra em fila; gerar o HTML no servidor continua sendo boa ideia; `noindex` e página com erro podem não ser renderizados | Conteúdo e links no HTML puro; script só para o acessório | `D:crawling-indexing/javascript/javascript-seo-basics` | (1 leitura). Notas de 15 a 18/12/2025 no registro de mudanças |

---

## 5. Dados estruturados para um site assim

Classe A e "quem ganha: Google" em todas as linhas. Páginas vivas do Google, sem data exibida (as datas do registro de mudanças estão no texto da linha).
O Google diz que usa dados estruturados para entender a página e mostrar o conteúdo de forma mais rica, e que **não garante** que o recurso apareça.

| Tipo ou regra | O que o Google diz | O que fazer aqui | Fonte | Observação |
|---|---|---|---|---|
| Regras gerais | "Don't mark up content that is not visible to readers of the page." (não marque o que o leitor não vê); não marcar conteúdo irrelevante ou enganoso, como avaliação falsa; o dado tem de ser retrato fiel da página; não se passar por outra organização nem deturpar afiliação ou propósito | Todo campo marcado aparece escrito na página; nada inventado | `D:appearance/structured-data/sd-policies` | Conferidas em 2 leituras |
| Punição | Ação manual de dados estruturados tira a página dos resultados ricos; "it doesn't affect how the page ranks in Google web search" (não muda a posição na busca comum) | Risco limitado, mas real, de perder o recurso | idem | Conferida em 2 leituras |
| `Organization` | Para os dados administrativos da organização (nome, logotipo, endereço do site, contatos, razão social, identificadores fiscais, perfis em outros sites); recomenda pôr na página inicial ou numa página "sobre"; nenhum campo é obrigatório | **É o tipo certo para o próprio site**: nome, logotipo, endereço do site, contato, CNPJ quando houver, na página inicial ou em "quem somos" | `D:appearance/structured-data/organization` | (1 leitura) |
| `LocalBusiness` | Descreve um local de empresa (horário, departamentos, avaliações) para a busca e o mapa; obrigatórios: nome e endereço. A página diz que pode ir em qualquer página do site, de preferência numa que traga as informações do negócio | **Não marcar o próprio site como `LocalBusiness`**: ele não é o estabelecimento que presta o serviço, e isso bateria na regra de não deturpar o propósito (inferência minha) | `D:appearance/structured-data/local-business` | Conferida em 2 leituras |
| `LocalBusiness` de terceiros | A página não diz "só o dono pode marcar". Sobre os campos de avaliação (`aggregateRating` e `review`) a página diz: "This property is only recommended for sites that capture reviews about other local businesses" (esta propriedade só é recomendada para sites que captam avaliações de outras empresas locais), o que mostra que o Google prevê diretórios marcando empresas de terceiros | **Não conclusivo para uso geral.** Se houver página de detalhe de uma licenciada, marcar `LocalBusiness` com os dados verdadeiros e visíveis dela não é vedado por texto que eu tenha lido, mas não há frase que o autorize expressamente nem promessa de resultado. Só com autorização da licenciada (regra do projeto) | idem; `D:appearance/structured-data/review-snippet` | Trecho conferido em 3 leituras; na correção de 13/11/2026 a citação foi completada com a palavra "recommended", que faltava (mais 1 leitura) |
| Estrelas de avaliação (review snippet), regra de autopromoção | "If the entity that's being reviewed controls the reviews about itself, their pages that use LocalBusiness or any other type of Organization structured data are ineligible for star review feature." (se a entidade avaliada controla as avaliações sobre si, não tem direito às estrelas), inclusive quando as avaliações vêm de janela incorporada de terceiro | O site não marca estrelas sobre si mesmo. Estrelas para licenciadas só seriam possíveis com avaliações captadas pelo próprio site, de usuários reais | `D:appearance/structured-data/review-snippet` | Conferida em 2 leituras |
| Idem, origem das avaliações | "Don't aggregate reviews or ratings from other websites." (não agregue avaliações de outros sites); notas têm de vir direto de usuários; proibidas avaliações falsas ou incentivadas sem aviso (regra de 24/07/2026); a avaliação marcada tem de estar visível | **Não copiar nota nem avaliação do Google ou de outro site** (também é regra do projeto). Na fase atual: sem estrelas | idem | Conferidas em 2 leituras. Atenção: "sem aviso" é a regra dos **dados estruturados**; no perfil de empresa do Google, incentivo em troca de avaliação é vedado sempre, com ou sem aviso (guia (b), seção 3.1; item 2 da rodada) |
| `BreadcrumbList` | Marca a trilha de navegação; mínimo de dois itens; a trilha deve refletir um caminho típico do usuário, não o endereço. Aparece só no computador | Usar (Início → Zona Oeste → Pinheiros → Baratas); efeito visual só no computador | `D:appearance/structured-data/breadcrumb`; registro de mudanças de 22/01/2025 | (1 leitura da página; a data conferida em 2) |
| `FAQPage` | **O resultado rico de perguntas frequentes deixou de aparecer na busca em 07/05/2026**; aviso de fim em 08/05/2026 e documentação removida em 15/06/2026. O endereço antigo da documentação hoje leva ao registro de mudanças | Perguntas e respostas visíveis na página continuam úteis ao leitor; marcar `FAQPage` **não gera mais resultado rico no Google**. Se serve a outros sistemas, é assunto do guia (c) | `https://developers.google.com/search/updates` | Datas conferidas em 2 leituras |
| `Service` e `Offer` | Não há recurso para `Service` na galeria de recursos do Google (25 recursos listados; `Service`, `FAQ` e `HowTo` não estão) | Marcar `Service` não produz resultado visual no Google; não é proibido, só não tem efeito documentado. Preço só se estiver visível e com fonte | `D:appearance/structured-data/search-gallery` | (1 leitura) |
| Unidades de agregador | Recurso em que diretórios e comparadores aparecem em bloco próprio para buscas de empresa local | **Não existe no Brasil**: a página lista as unidades de agregador e de fornecedor só para o Espaço Econômico Europeu (outros recursos da mesma página valem para a Turquia e a África do Sul); o Brasil não é citado | `D:appearance/aggregator-features` | (2 leituras: a segunda na correção de 13/11/2026) |

---

## 6. Links e autoridade

### 6.1 O que o Google documenta

| Afirmação | O que fazer aqui | Fonte (páginas vivas do Google, sem data exibida) | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|
| "Google uses links as a signal when determining the relevancy of pages and to find new pages to crawl." (usa links como sinal de relevância e para achar páginas) | Links de fora importam por dois motivos: ser achado e ser considerado relevante | `D:crawling-indexing/links-crawlable` | A | Google | Conferida em 2 leituras |
| PageRank continua entre os sistemas centrais; o guia de iniciantes lembra que há muitos sinais e o PageRank é só um | Não tratar link como o único fator | `D:appearance/ranking-systems-guide`; `D:fundamentals/seo-starter-guide` | A | Google | — |
| Qualidade: um dos fatores é outros sites conhecidos apontarem ou se referirem ao conteúdo | Mérito citável (dado próprio) atrai referência | `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/` | A | Google | — |
| Link "natural": o Google não define em uma frase; define o oposto (seção 2). O guia de iniciantes recomenda divulgar o site (comunidades, redes, boca a boca) e avisa que exagerar na promoção pode prejudicar | Divulgar o que for útil de verdade (por exemplo, um guia de como conferir a licença); pedir link sem contrapartida não está na lista de spam, mas contato com terceiros está fora da rodada | `D:fundamentals/seo-starter-guide` | A | Google | (1 leitura) |
| Ferramentas de terceiros "don't have access to our internal ranking data" (não têm acesso aos dados internos de ranqueamento) | "Autoridade de domínio" e notas parecidas são métricas das ferramentas, não do Google | `D:fundamentals/third-party-seo` | A | Google | Página criada em 05/06/2026. Conferida na página e numa reprodução (Search Engine Roundtable, 08/06/2026) |

### 6.2 O que estudos com dado mostram (todos de vendedores de ferramenta)

| Estudo | Amostra, método, ano, país | Resultado | Classe | Quem ganha | Limite |
|---|---|---|---|---|---|
| Ahrefs, "Google diz que links importam menos" — `https://ahrefs.com/blog/links-matter-less-but-still-matter/` | Publicado em 30/01/2025. 1.000.000 de palavras-chave de maior volume dos **Estados Unidos**; 20 primeiras posições; correlação de Spearman | Domínios que apontam: 0,255; links: 0,248; nota de domínio da ferramenta: 0,131; links internos recebidos: 0,117; palavra-chave no endereço: 0,034. **Buscas locais: 0,33.** Menor que no estudo de 2019 (0,27 a 0,29), que usou outro tipo de busca | B | Ahrefs vende ferramenta de links | Correlação fraca e não é causa (o autor diz); inglês, Estados Unidos; palavras de alto volume, o oposto da cauda longa de bairro; números por tipo de busca só em gráfico, salvo o local |
| Backlinko, 11,8 milhões de resultados — `https://backlinko.com/search-engine-ranking` | Página atualizada em 14/04/2025; pelos arquivos, os dados são de cerca de 2020. Dados de links da Ahrefs. País não informado | O primeiro resultado tem em média 3,8 vezes mais links que os de 2 a 10; nota de domínio correlaciona com posição; **palavra-chave no título, tamanho do texto, velocidade e dados estruturados: pouca ou nenhuma correlação** | B, **pode estar desatualizada** | Backlinko pertence à Semrush (ferramenta) | Não é independente do estudo acima (mesma base de links); correlação; país e idioma não declarados |
| Semrush, fatores de ranqueamento 2024 — `https://www.semrush.com/blog/ranking-factors-semrush-study/` | Publicado em 04/01/2024. 16.298 palavras-chave em inglês; 20 primeiras posições (cerca de 300 mil); país não informado | O texto destaca relevância do conteúdo e tráfego direto; **os números de correlação estão só num gráfico que a ferramenta de leitura não leu** | B, **pode estar desatualizada** | Semrush vende ferramenta | Não consegui os coeficientes; o endereço antigo do estudo hoje redireciona para outro produto |
| Ahrefs, tempo até ranquear — `https://ahrefs.com/blog/how-long-does-it-take-to-rank/` | Publicado em 15/05/2025. (a) 1 milhão de páginas aleatórias vistas em setembro de 2023; (b) 2 milhões de páginas em inglês, não vazias, criadas em outubro de 2023; (c) 1,3 milhão de palavras-chave dos **Estados Unidos** para a idade das páginas | (a) **1,74%** chegaram aos dez primeiros em um ano; (b) **6,11%**; das que chegaram, 40,82% em até um mês. (c) 72,9% das páginas nos dez primeiros têm mais de 3 anos; 13,7% têm menos de 1 ano; a primeira colocada tem em média 5 anos. Em 2017 eram 5,7%, 59%, 22% e 2 anos | B | Ahrefs | "Chegar aos dez primeiros" vale para **qualquer** busca, inclusive de volume ínfimo; o autor admite efeito de amostragem; país informado só para a amostra (c), Estados Unidos; a amostra (a), do 1,74%, não informa país; a (b) informa só o idioma (inglês) |

Leitura conjunta: (1) que link é sinal é classe A; (2) o **tamanho** do efeito só tem classe B de uma base (Ahrefs,
reaproveitada pela Backlinko), logo **não fecha consenso** pela regra da rodada; (3) o dado que mais interessa aqui é
o 0,33 para buscas locais, com a explicação do autor de que sites de serviço local têm conteúdo parecido e o link
vira o diferencial. É hipótese plausível, de vendedor de ferramenta de links.

### 6.3 Cliques e comportamento (Navboost), autoridade de site: julgamento e vazamento

| Afirmação | Fonte | Classe | Quem ganha | Observação |
|---|---|---|---|---|
| O Google usa dados de interação agregados e anônimos para avaliar se os resultados são relevantes | Página oficial "como a busca funciona" (seção 1.1) | A | Google | É o que está confirmado em fonte primária que abri |
| No julgamento *Estados Unidos v. Google* (ação de 20/10/2020; julgamento a partir de 12/09/2023; decisão de responsabilidade em 05/08/2024; decisão de remédios em 02/09/2025, que mandou compartilhar com concorrentes parte do índice e dos dados de interação de usuários; recursos das duas partes em curso no início de 2026) | `https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2020)` | C (enciclopédia, fonte terciária) | ninguém | **Não abri a decisão nem os depoimentos**: os PDFs do tribunal e do governo não vieram em texto legível e as versões em HTML recusaram acesso. Datas de fonte terciária, 1 leitura |
| Slides internos exibidos no julgamento (por exemplo, "Life of a Click", de 2017) descrevem o uso de cliques e de interação do usuário para melhorar o ranqueamento | `https://www.blindfiveyearold.com/its-goog-enough` (AJ Kohn, 08/11/2023), com imagens dos slides e links para os PDFs do governo | D (consultor de SEO descrevendo documentos que eu não abri), **pode estar desatualizada** | o autor vende consultoria de SEO; não vende curso nem ferramenta | Vi a descrição dos slides pelo artigo, não os PDFs. O artigo não traz os detalhes que circulam ("13 meses de dados", "Glue"): esses **não consegui confirmar em fonte com o documento à vista** |
| Vazamento da documentação da API interna (maio de 2024): cerca de 2.500 páginas e 14.014 atributos; nomes como `goodClicks`, `badClicks`, `lastLongestClicks` (módulo ligado a cliques), `siteAuthority`, `hostAge`, `titlematchScore`, uso de dados do Chrome | `https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/` (Rand Fishkin, 28/05/2024, com capturas); `https://ipullrank.com/google-algo-leak` (Mike King, 27/05/2024, com capturas) | C (Fishkin: vende programa de pesquisa de público, não SEO) e D (King: agência de SEO), **podem estar desatualizadas** | SparkToro; iPullRank | Os dois autores avisam: **não há pesos, não se sabe o que está em uso, parte pode estar aposentada**; a referência mais recente no material é de 2023–2024 |
| Resposta do Google ao vazamento: "We would caution against making inaccurate assumptions about Search" (cautela com suposições imprecisas) com base em informação "out-of-context, outdated, or incomplete" (fora de contexto, desatualizada ou incompleta) | `https://www.theregister.com/2024/05/29/internal_google_search_documents/` (29/05/2024) | C (jornalismo citando porta-voz), **pode estar desatualizada** | The Register é veículo de notícias e não vende SEO; o porta-voz citado é do Google, que tem interesse em reduzir o peso do vazamento | 1 leitura da reportagem; frase idêntica aparece em outros veículos no resultado de busca (não abertos) |

O que dá para levar: comportamento de quem busca entra no ranqueamento (A, em termos gerais). Nomes de sinais, janelas
de tempo e "autoridade de site" são C ou D e **não viram regra**. Para o projeto, a consequência é a mesma com ou sem
os detalhes: a página tem de satisfazer quem clicou. Tentar fabricar cliques é tráfego gerado por máquina (seção 2).

---

## 7. Especificidades de serviço local no orgânico

| Afirmação | O que fazer aqui | Fonte | Data da fonte | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|---|
| O Google reconhece que muitas buscas têm intenção local e usa a localização de quem busca; o exemplo oficial é "pizza" mostrar empresas próximas | "Dedetizadora" sem bairro já é busca local; o resultado depende de onde a pessoa está | `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/` | página viva | A | Google | Conferido em 2 leituras |
| Os recursos da página de resultado mudam conforme a busca; a busca por oficina de bicicleta tende a mostrar resultados locais | Premissa minha, a conferir no item 4: em buscas de serviço, mapa e anúncios tendem a vir antes do orgânico (a fonte só diz que os recursos da página mudam com a busca) | `D:fundamentals/how-search-works` | página viva | A | Google | Conferido em 2 leituras. O **quanto** o mapa empurra o orgânico o Google não diz |
| O bloco do mapa é ordenado por outra lógica: relevância, distância e destaque (o Google hoje escreve também "popularidade"); o destaque considera quantos sites apontam para a empresa e quantas avaliações ela tem. Não há como pedir nem pagar | O site do intermediário **não entra no mapa** (item 2(a) da rodada). Ele disputa o orgânico abaixo; pode, no máximo, ser um dos sites que apontam para a licenciada | `https://support.google.com/business/answer/7091?hl=en` | página viva | A | Google | 2 leituras. **Na versão que li não há a frase sobre "posição nos resultados da web" contar para o mapa**; se alguma fonte citar essa frase, confira a data. Detalhe no guia (b) |
| Em geral, no máximo duas páginas do mesmo site no topo de uma busca | Não esperar dominar a tela. "Uma página por busca" é escolha de desenho, inferência minha: a fonte diz "em geral até duas" | `D:appearance/ranking-systems-guide` | página viva | A | Google | — |
| Páginas de serviço × páginas de localidade: **não há documento do Google** que diga como estruturar; só a política de páginas de entrada (seção 2) | Usar a matriz da seção 2.2; a página de praga (serviço) carrega o conteúdo técnico, a de bairro só existe se tiver algo próprio | — | — | sem fonte A ou B | — | Inferência minha, sem fonte aberta nesta leitura: o que circula sobre "página de serviço + página de cidade" é prática de agência (se for citado, entra como classe D) |
| Diretórios e agregadores no orgânico: não afirmo quem aparece em busca alguma (isso é o item 4, no navegador) | Registrar no item 4 que tipo de site ocupa cada busca | — | — | — | — | Hipótese antiga em `/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md` linhas 26–30 |
| Estudo de uso na Europa, serviços para casa: perfis de empresa visíveis em 78% das buscas com localização explícita e com 42% dos cliques quando visíveis; cerca de 8 em 10 cliques foram para empresas, 1 em 10 para agregadores; o tráfego dos agregadores veio 73% do orgânico | Indício de que agregador recebe a menor fatia e depende do orgânico | `https://www.nearmedia.co/eu-home-services-search-behavior/` | 20/11/2024 | B, **pode estar desatualizada** | Near Media vende consultoria e critica o Google na regulação europeia | **Alemanha, França e Irlanda**; 300 pessoas; uma tarefa (reforma de cozinha), painel recrutado, com tela e voz gravadas; página é trecho do estudo |
| Cliques no bloco do mapa: 42% das pessoas em buscas locais clicaram num resultado do mapa. No conjunto das sete tarefas do estudo (só uma local), 65% clicaram em algum resultado orgânico e 19% em anúncio; a fonte não dá esses dois números só para as buscas locais | Ordem de grandeza: o mapa leva uma fatia grande | `https://backlinko.com/google-user-behavior` | atualizada em 14/04/2025; a página não informa a data da coleta (cerca de 2020 é estimativa minha) | B, **pode estar desatualizada** | Backlinko pertence à Semrush | **Estados Unidos**; 259 pessoas, 1.801 sessões, sete tarefas dadas; a própria página tem número divergente (65% no texto, 76% num gráfico) |
| Taxa de clique por posição, 2026: primeira posição orgânica 7,1% no geral, 22,6% sem resposta de IA e 3,6% com resposta de IA; bloco local 14,8%, 12,6% e 11,9% nas posições 1 a 3 | Só alegação (classe D): não vira regra nem entra em consenso. O que a fonte afirma: a primeira posição orgânica vale muito menos quando há resposta de IA; o bloco local rende mais que o orgânico abaixo dele | `https://firstpagesage.com/reports/google-click-through-rates-ctrs-by-ranking-position/` | 22/09/2026 | D (alegação: agência de SEO; amostra de clientes e painel próprios; método pouco exposto) | First Page Sage é agência de SEO e ganha quando o número convence o leitor a contratar SEO; a amostra são os próprios clientes e um painel próprio | **Estados Unidos**; 1.184 domínios, março a agosto de 2026; método pouco exposto; não dá a primeira posição orgânica com mapa presente |
| Taxa de clique por posição, base antiga: primeira posição 27,6%; os três primeiros somam 54,4%; 0,63% dos cliques vão à segunda página | Só como referência de formato da curva (cai rápido) | `https://backlinko.com/google-ctr-stats` | atualizada em 16/04/2025; dados anteriores | B, **pode estar desatualizada** | Backlinko/Semrush | País não informado; anterior às respostas de IA; inclui buscas de marca, que inflam a primeira posição |
| Resumo de IA reduz o clique: 8% das visitas a resultados com resumo de IA tiveram clique num resultado tradicional, contra 15% sem resumo; cerca de 1% clicou em link dentro do resumo | Buscas informativas ("como acabar com barata") rendem menos visita; buscas de contratação tendem a ter menos resumo (hipótese, não medida aqui) | `https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/` | 22/07/2025 | B | Pew é instituto de pesquisa sem produto de SEO | **Estados Unidos**; 900 adultos, 68.879 buscas em março de 2025; associação, não causa. É a única fonte B sem interesse comercial deste guia |
| Buscas sem clique: de cada 1.000 buscas no Google, 360 cliques vão para a web aberta nos Estados Unidos e 374 na União Europeia | A maior parte das buscas não gera visita a site algum | `https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/` | 02/07/2024 | B, **pode estar desatualizada** | SparkToro; dados da Datos, que é da Semrush | **Estados Unidos (360) e União Europeia (374)**. Os dois números estão no título exibido e no corpo da página (relida na correção de 13/11/2026). O endereço da página traz os países invertidos, porque guarda o título antigo; vale o título exibido e o corpo |
| Estudo antigo de cliques em buscas de serviço: orgânico cerca de 44% a 51%, bloco local cerca de 29% a 32%, conforme haja ou não anúncio de serviço local | Só histórico | `https://www.brightlocal.com/research/local-services-ads-click-study/` | 19/10/2018 | B, **pode estar desatualizada** | BrightLocal vende ferramenta de SEO local | **São Francisco, Estados Unidos**; teste com escolha declarada, não clique real |

Nenhuma dessas fontes é do Brasil, nenhuma é de dedetização, e os números não se somam entre si (métodos diferentes).
O que se repete em duas fontes B de métodos diferentes, as duas com interesse comercial e uma delas antiga (Near
Media e Backlinko; a First Page Sage aponta na mesma direção, mas é classe D e não conta como evidência): **em busca
local o bloco do mapa leva uma fatia grande dos cliques** (na Backlinko, 42% clicaram no mapa nas buscas
locais; o estudo não dá a fatia do orgânico só para buscas locais). Isso sustenta, como hipótese, que o canal orgânico do intermediário rende mais na
cauda longa e em buscas de comparação e de dúvida do que em "dedetizadora perto de mim".

---

## 8. Medição

| Afirmação | O que fazer aqui | Fonte (páginas vivas do Google, sem data exibida) | Classe | Quem ganha | Observação |
|---|---|---|---|---|---|
| O relatório de desempenho do Search Console mede: cliques ("The number of times a user clicked your site from Google Search results."), impressões ("How many times your site appeared in Search results."), taxa de clique ("The click count divided by the impression count.") e posição média ("The average position of the topmost result from your site.") | São as quatro colunas do placar. Posição média é a média da posição mais alta do site em cada busca em que apareceu | `https://support.google.com/webmasters/answer/7576553?hl=en` | A | Google | Conferidas em 2 leituras. Visão padrão: últimos três meses |
| Dimensões: buscas, páginas, países, aparelhos, aparência na busca, datas | Filtrar por página (cada praga × bairro) e por busca | idem; `https://support.google.com/webmasters/answer/17011259?hl=en` | A | Google | (1 leitura) |
| Impressão: conta quando o link aparece na página de resultado carregada, mesmo sem rolar até ele (em carrosséis e listas infinitas é preciso rolar). Posição: aproximada; todos os links de um mesmo bloco recebem a posição do bloco; o resumo de IA ocupa uma posição e todos os links dentro dele recebem a mesma | "Posição 4" não quer dizer quarto link visível: pode haver mapa, anúncios e resumo de IA acima. Queda de clique com posição estável pode ser mudança de formato da página | `https://support.google.com/webmasters/answer/7042828?hl=en` | A | Google | (1 leitura). A página não diz como conta o bloco do mapa |
| Algumas buscas são omitidas para proteger a privacidade; a tabela mostra só as linhas mais importantes | Em bairro pequeno, parte das buscas não aparecerá na tabela; os totais do gráfico contam | `https://support.google.com/webmasters/answer/17011259?hl=en` | A | Google | (1 leitura). O prazo de guarda de 16 meses aparece nessa página só para o filtro de buscas de marca; a página que dá o prazo geral não foi aberta |
| O tráfego de recursos de IA da busca entra nos totais de busca do Search Console | Não há relatório separado de "citações em IA" nessa leitura | `D:appearance/ai-features`; registro de mudanças de 16/06/2025 | A | Google | (1 leitura) |
| Depois de atualização central, esperar ao menos uma semana após o fim para comparar períodos | Comparar semana ou 28 dias contra período igual anterior | `D:appearance/core-updates` | A | Google | Conferida em 2 leituras |
| Ferramenta de terceiro não tem acesso aos dados internos de ranqueamento e não garante resultado; o Google recomenda fortemente o Search Console | Volume de busca, "dificuldade" e "autoridade" de ferramenta são estimativas da ferramenta | `D:fundamentals/third-party-seo` | A | Google | 2 leituras |
| Enviar buscas automáticas e raspar o resultado para checar posição consta entre as práticas vedadas (tráfego gerado por máquina) | Não montar robô de posição; a posição vem do Search Console | `D:essentials/spam-policies` | A | Google | (1 leitura do resumo; relida na correção de 13/11/2026). A seção "Machine-generated traffic" (tráfego gerado por máquina) fala em enviar consultas automáticas ao Google, inclusive para checar posição, sem permissão expressa, e diz: "Such activities violate our spam policies and the Google Terms of Service." (essas atividades violam nossas políticas de spam e os Termos de Serviço do Google). Limite à automação do item "medir" do desenho. Vale também para rastreador de posição e para a "grade de posição" de ferramenta de mapa: guia (b), seção 9 (a página é a das políticas de spam da Busca e não cita o Maps; estender a regra ao Maps é leitura dos guias) |

**O que dá para medir sem conta: nada confiável.** Sem o Search Console não há impressão, clique nem posição. A
busca manual no navegador mostra uma posição, para uma pessoa, num lugar, num momento (é o que o item 4 registra, como
amostra). O operador `site:` indica se há páginas no índice, sem número exato (guia de iniciantes, 1 leitura).

**O que fica para o owner** (exige conta ou decisão dele; nada disso foi feito): criar e verificar a propriedade no
Search Console; enviar o sitemap; ler ações manuais e o relatório de indexação; exportar os dados para a planilha de
medição; decidir se assina alguma ferramenta paga.

---

## 9. Prazo realista para site novo

| Afirmação | Fonte (classe A: páginas vivas do Google, sem data exibida; classes B e D: a data está no texto) | Classe | Quem ganha | Observação |
|---|---|---|---|---|
| "Some changes might take effect in a few hours, others could take several months." (algumas mudanças valem em horas, outras levam vários meses); em geral, esperar algumas semanas para avaliar | `D:fundamentals/seo-starter-guide` | A | Google | Citação conferida em 2 leituras |
| Rastreamento de página nova: de alguns dias a algumas semanas; sem garantia de inclusão | `D:crawling-indexing/ask-google-to-recrawl` | A | Google | 2 leituras |
| Depois de melhorar um site, o efeito pode vir em dias ou levar meses, até os sistemas confirmarem a melhora; não é preciso esperar a próxima atualização central grande | `D:appearance/core-updates` | A | Google | 2 leituras (resumo); texto de 09/12/2025 |
| **O Google não dá prazo para SEO "dar resultado".** A página "você precisa de um SEO?" não traz número de meses; manda perguntar ao profissional que resultado ele espera e em quanto tempo, e diz: "No one can guarantee a #1 ranking on Google." | `D:fundamentals/do-i-need-seo` | A | Google | Ausência de prazo conferida em 2 leituras. A frase "de quatro meses a um ano", que circula atribuída a essa página, **não está na versão atual** (a página foi simplificada em 05/06/2026; não conferi a versão antiga); não a cite como vigente |
| De 1 milhão de páginas novas, 1,74% chegaram aos dez primeiros em um ano (6,11% numa amostra filtrada); 72,9% das páginas nos dez primeiros têm mais de 3 anos | Ahrefs, 15/05/2025 (seção 6.2) | B | Ahrefs | Abrangência (país) não informada pela fonte para a amostra do 1,74%; a do 6,11% informa só o idioma (inglês); "Estados Unidos" vale só para a amostra de palavras-chave da parte de idade das páginas (72,9%). Qualquer busca, não só as comerciais |
| "Site novo fica cerca de seis meses sem resultado" | artigo do owner, tática 3.1 | D | autor vende ferramenta | Coerente com as fontes acima, mas o número não tem amostra |
| Existiria uma "caixa de areia" para site novo (atributo `hostAge` no vazamento) | iPullRank, 27/05/2024 (seção 6.3) | D, **pode estar desatualizada** | agência | Uso real desconhecido; não é regra |

**Prazo a assumir no desenho (premissa, não promessa):** semanas para as páginas serem rastreadas e indexadas;
**de 6 a 12 meses** para saber se as páginas de cauda longa recebem impressões e cliques (**número meu, premissa de
desenho: "6 a 12 meses" não está em nenhuma fonte A ou B deste guia**); sem garantia de chegar à primeira página em
busca alguma. Base: classe A para "horas a meses" e para "sem garantia"; classe B (Ahrefs, 2025; abrangência — país —
da amostra não informada pela fonte) para a raridade de página nova nos dez primeiros. Não há dado para site novo em português, em São Paulo, neste setor.

---

## 10. O que o exemplo do owner acertou, errou ou não provou

Referência: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`.

| # | Tática do artigo | Veredito | Classe agora | Fonte que decide |
|---|---|---|---|---|
| 1.1 | Mirar busca de quem quer contratar; ler a intenção pelo que já ranqueia | **Confirmada em parte.** O Google diz que primeiro estabelece a intenção da busca e reconhece intenção local. O método "olhar o que já ranqueia" é prática, sem fonte | A para "a intenção decide"; D para o método | página "como a busca funciona" (seção 1.1) |
| 1.2 | Trabalhar por padrão de busca | Permanece método de trabalho. O risco do padrão está confirmado em 2.6 | D | — |
| 1.3 | Não inventar volume de busca | Coerente com a página de ferramentas de terceiros (não têm dado interno do Google) | A para o princípio | `D:fundamentals/third-party-seo` |
| 1.4 | Nove tipos de página para software | Não se aplica; não conferida | D | — |
| 1.5 | Site novo deve ir no pequeno e específico | **Apoio parcial de B:** entre as páginas que chegaram aos dez primeiros, as de busca de baixo volume se distribuíram ao longo do tempo e 94% nunca ranquearam para alto volume. Não há estudo de "dificuldade × autoridade" em português | B fraco (abrangência — país — não informada pela fonte para este recorte) | Ahrefs, 15/05/2025 |
| 1.6 | Domínio novo publicando muito de uma vez nunca ranqueou | Permanece relato. É coerente com a política de conteúdo em escala e com o 1,74% do estudo | D | — |
| 2.1 | Uma palavra-chave, uma página | **Não confirmada por fonte oficial.** A página de canonização trata de conteúdo duplicado ou muito parecido em endereços diferentes, não de duas páginas disputando a mesma busca; a regra de diversidade admite, em geral, até **duas** páginas do mesmo site no topo, o que não é "uma". A tática permanece classe D (relato do autor do artigo). O apoio de A é só indireto: páginas muito parecidas são agrupadas e uma é escolhida. "Canibalização" como termo não é do Google | D (a tática); A só para o agrupamento de páginas duplicadas | canonização; diversidade de sites (seções 1.2 e 4) |
| 2.2 | Cobrir buscas secundárias numa página; **título é o elemento mais forte**; descrição ganha o clique | **Em parte confirmada, em parte não provada.** O Google documenta como monta o título e que a descrição alimenta o trecho. **"Mais forte" não tem fonte A**; o estudo da Backlinko achou pouca correlação entre palavra no título e posição | A para o que são; "mais forte" segue D | `D:appearance/title-link`; `D:appearance/snippet`; Backlinko |
| 2.3 | Cobrir o que os três primeiros cobrem, mais um elemento próprio | **Metade confirmada:** o Google pergunta se o conteúdo dá valor substancial frente aos outros resultados e se traz informação original. "Copiar a ordem dos três primeiros" é opinião | A para o "a mais"; D para o resto | conteúdo útil (seção 3) |
| 2.4 | O Google pune escala sem originalidade, feita por pessoa ou IA | **Confirmada. Subiu para A** | A | política de conteúdo em escala (seção 2) |
| 2.5 | Um H1; dados estruturados coerentes; cinco links internos | **Princípios confirmados, número contrariado.** Dado estruturado tem de retratar a página (A). Link interno: pelo menos um por página e "não há número ideal" (A). Ordem e quantidade de títulos não importam (A) | A para os princípios; "cinco" e "um só H1" não têm base | seções 4 e 5 |
| 2.6 | Página em que só muda a cidade é doorway; política cita páginas por região | **Confirmada. Subiu para A**, com o texto literal | A | política de páginas de entrada (seção 2) |
| 2.7 | Ritmo constante de publicação | **Permanece D.** Não achei documento do Google nem estudo sobre ritmo. O que existe é a política de escala, que olha valor, não calendário | D | — |
| 2.8 | Molde, arquivo de processo, aprovação humana | Método de trabalho; coerente com a recomendação do Google de revisar conteúdo de IA | D (método); A para "revisar" | `D:fundamentals/using-gen-ai-content` |
| 2.9 | Atualizar o sitemap a cada publicação | **Confirmada em parte.** Sitemap ajuda site novo; é "só uma dica"; `lastmod` só vale se for verdadeiro | A | sitemaps (seção 4) |
| 2.10 | Cortar páginas sem clique, reapontar, reagrupar | **Em parte contrariada.** O Google diz que apagar conteúdo é o último recurso, só para o que não tem salvação. Reapontar e consolidar são compatíveis com canonização. O caso do autor segue sem site conferível | A para a cautela; D para o caso | `D:appearance/core-updates` |
| 2.11 | Multilíngue e hreflang | Não se aplica; não conferida | D | — |
| 3.1 | Seis meses sem resultado; métricas de ferramenta não são do Google; o placar é o Search Console | **Duas partes confirmadas, uma não provada.** Ferramentas não têm dado interno (A); Search Console é a fonte recomendada (A). "Seis meses" não tem amostra; o estudo aponta que o prazo é longo e incerto (B) | A + B; "seis meses" segue D | seções 8 e 9 |
| 3.2 | Pedir link a quem citou a marca; substituir link quebrado | Não proibido pela política (não é compra nem troca). Eficácia sem estudo que eu tenha aberto | D | — |
| 3.3 | Pedir link a listas e a quem aponta para concorrentes | Idem; atenção a "diretórios de baixa qualidade", que a política lista como spam | D; limite em A | política de links |
| 3.4 | Máquina de e-mails de prospecção | Sem fonte sobre eficácia; fora do escopo do Google; fora da rodada | D | — |
| 3.5 | Troca excessiva de links é spam | **Confirmada. Subiu para A.** O teste "eu incluiria sem contrapartida?" é do autor, não do Google | A para a regra; D para o teste | política de links |
| 3.6 | Conteúdo citável (dado próprio, ferramenta) | **Apoio indireto de A:** o Google valoriza informação original e referência de outros sites. Não abri estudo sobre o que atrai links | A indireto; eficácia segue D | seções 3 e 6 |
| 3.7 | Link pago que passa crédito viola a política; o desfecho comum é ser ignorado | **Primeira parte confirmada (A).** "É ignorado" não está na política que li: ela fala em posição mais baixa ou remoção. As "cinco checagens" são do autor | A para a regra; D para o resto | política de links |
| 3.8 | Perfil "limpo demais" chama atenção; dois terços dos links somem | Permanece | D | — |
| 5.1 | Esperar dois meses antes de reverter; três antes de links; seis em domínio novo | **Princípio confirmado, números não.** O Google diz horas a meses e "algumas semanas" para avaliar; não dá dois, três nem seis | A para "esperar"; números seguem D | seção 9 |
| 5.2 | Revisão semanal no Search Console; separar queda de posição de queda de clique | Método; as definições do Search Console o sustentam (o resumo de IA ocupa posição e muda o clique) | D (método) apoiado em A | seção 8 |
| 5.3 | Regras do agente (aprovação para publicar etc.) | Método; coerente com as regras do projeto | D (método) | — |

**Resumo:** o artigo acertou onde citou política do Google (2.4, 2.6, 3.5, 3.7) e onde disse que ferramenta não é o
Google (3.1). Errou ou exagerou nos números de bolso (cinco links, um H1, seis meses, dois meses) e em "título é o
elemento mais forte". Não provou ritmo de publicação (2.7), poda de páginas (2.10) nem nada sobre links além da regra.

---

## 11. O que é consenso, o que é disputado, o que não sei

### O que é consenso (só classe A, ou duas fontes B independentes)

1. O Google não vende posição orgânica e não garante rastrear, indexar nem mostrar (A).
2. Páginas voltadas a regiões ou cidades que afunilam para uma só, e páginas muito parecidas feitas para buscas
   parecidas, são páginas de entrada (A).
3. Muitas páginas geradas sem valor para o usuário são abuso de conteúdo em escala, com ou sem IA (A).
4. Comprar ou vender link para ranquear e trocar links em excesso viola a política; link pago leva `rel="sponsored"`
   ou `rel="nofollow"` (A).
5. Violação leva a posição mais baixa ou remoção, por sistema ou por ação manual (A).
6. Links são um sinal declarado, para relevância e para descoberta; PageRank segue entre os sistemas centrais (A).
7. O Google usa dados de interação agregados e anônimos para avaliar relevância (A).
8. E-E-A-T não é fator específico; confiança é o aspecto central; temas de saúde, finanças e segurança recebem mais
   peso (A).
9. Não há contagem mágica de palavras, de títulos nem de links; a meta tag de palavras-chave não é usada; palavra no
   domínio ou no endereço quase não tem efeito (A).
10. Dado estruturado tem de corresponder ao que está visível; avaliação controlada pela própria empresa não dá
    estrelas; não se agregam avaliações de outros sites (A).
11. O resultado rico de FAQ acabou em maio de 2026; a trilha de navegação aparece só no computador desde janeiro de
    2025 (A).
12. A indexação usa a versão de celular; Core Web Vitals são usados, mas relevância vem antes (A).
13. O resultado muda com a localização de quem busca; o Google reconhece intenção local (A).
14. Ferramentas de terceiros não têm os dados internos de ranqueamento; a medição oficial é o Search Console (A).
15. O Google não dá prazo; mudança leva de horas a meses; ninguém garante primeira posição (A).

**Quase consenso, mas não fecha pela regra da rodada:** resposta de IA no topo reduz o clique nos resultados
tradicionais. Há uma fonte B independente (Pew, Estados Unidos, 2025) e uma segunda que é de agência com amostra dos
próprios clientes (First Page Sage, Estados Unidos, 2026), que é classe D e não conta. Falta a segunda fonte B
independente. O mesmo vale para "o
bloco do mapa leva fatia grande dos cliques em busca local": Near Media (Europa, 2024) e Backlinko (Estados Unidos,
cerca de 2020) apontam na mesma direção, mas as duas têm interesse comercial e a segunda é antiga.

### O que é disputado

| Ponto | Um lado | Outro lado |
|---|---|---|
| Quanto pesam os links hoje | Pesam menos que antes: a correlação caiu frente a 2019 (Ahrefs, 30/01/2025, B) | Ainda são dos sinais mais fortes entre os medidos e pesam mais em busca local, 0,33 (mesmo estudo); o primeiro colocado tem 3,8 vezes mais links (Backlinko, dados de cerca de 2020, B antigo). As duas fontes usam a mesma base e vendem ferramenta |
| O título é "o elemento de página mais forte"? | Sim (artigo do owner, D; o vazamento mostra um atributo `titlematchScore`, D, uso desconhecido) | O Google não diz isso em lugar algum que eu tenha lido; a Backlinko achou pouca ou nenhuma correlação entre palavra no título e posição (B antigo) |
| Cliques como sinal direto de ranqueamento | Sim, por sistema próprio (leituras do julgamento e do vazamento, C e D) | O Google confirma só "dados de interação agregados e anônimos" (A) e pede cautela com o vazamento (porta-voz, via reportagem, C). Não abri a decisão judicial |
| Existe "autoridade de site" e "caixa de areia" para site novo? | Atributos `siteAuthority` e `hostAge` no vazamento (D) | Sem peso nem confirmação de uso; os próprios autores avisam; o que há de dado é só que página nova raramente chega ao topo (B) |
| Dados estruturados ajudam a ranquear? | Vendedores costumam dizer que sim (D) | O Google diz que servem para entender a página e habilitar recursos visuais; a punição de dados estruturados "não afeta a posição" (A); a Backlinko não achou correlação (B antigo) |
| Um diretório pode marcar `LocalBusiness` de terceiros? | A documentação prevê sites que captam avaliações "de outras empresas locais" (A, indireto) | Não há frase que autorize o uso geral, e a regra de não deturpar afiliação ou propósito limita (A). Fica não conclusivo |
| Vale podar páginas sem clique? | Sim, o autor relata ganho (D) | O Google trata apagar como último recurso (A) |
| Taxa de clique da primeira posição | 27,6% (Backlinko, base antiga, país não informado) | 7,1% no geral e 22,6% sem resposta de IA (First Page Sage, classe D, Estados Unidos, 2026). Métodos e épocas diferentes; nenhum é do Brasil |

### O que não sei

1. Quantas páginas praga × bairro um site novo sustenta antes de ser tratado como escala ou como página de entrada:
   não há número em fonte A nem B.
2. Como as Diretrizes dos Avaliadores classificam serviço doméstico com produto químico (YMYL ou não) e o que dizem,
   literalmente, sobre "quem é responsável pelo site": o PDF não abriu em forma legível.
3. Qualquer taxa de clique, fatia do mapa ou tempo até ranquear **no Brasil, em português, para dedetização**.
4. O que a decisão judicial e os depoimentos dizem, literalmente, sobre Navboost, janelas de tempo e sinais de
   qualidade: não abri a fonte primária.
5. Se ritmo de publicação (poucas por semana × muitas de uma vez) muda algo: sem documento e sem estudo.
6. Se o Google trata diferente um intermediário transparente e uma dedetizadora nas buscas de contratação: não há
   documento; só a observação ao vivo do item 4 e, depois, o Search Console podem indicar.
7. Os coeficientes do estudo da Semrush de 2024 (estão em imagem).
8. O prazo geral de guarda de dados do Search Console (a página que o informa não foi aberta) e como ele conta
   impressões do bloco do mapa.
9. O efeito, no Brasil, da atualização central iniciada em 10/11/2026, ainda aberta na hora desta leitura.
10. Se marcar `FAQPage` ou `Service` ajuda outros sistemas (respostas de IA): fora deste guia.

---

## 12. Fontes que tentei abrir e não abriram

| Fonte | O que houve | Efeito |
|---|---|---|
| Diretrizes dos Avaliadores de Qualidade — `https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf` (redireciona para `https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf`) | A ferramenta baixou o PDF (8,6 MB) mas não extraiu o texto | YMYL e E-E-A-T vêm só das páginas HTML do Google que resumem as diretrizes; nenhum trecho do PDF foi citado |
| Visão geral das diretrizes — `https://services.google.com/fh/files/misc/hsw-sqrg.pdf` | Idem (PDF sem texto legível) | Idem |
| Decisão de remédios de 02/09/2025, *Estados Unidos v. Google* — `https://www.govinfo.gov/content/pkg/USCOURTS-dcd-1_20-cv-03010/pdf/USCOURTS-dcd-1_20-cv-03010-3.pdf` | PDF sem texto legível | Nada da decisão foi citado |
| Decisão de 05/08/2024 em HTML — `https://law.justia.com/cases/federal/district-courts/district-of-columbia/dcdce/1:2020cv03010/223205/1033/` e `https://www.courtlistener.com/docket/18552824/1033/united-states-of-america-v-google-llc/` | Acesso recusado (erro 403); a busca do CourtListener pediu autenticação (401) | Idem |
| Página do Departamento de Justiça com os documentos do caso — `https://www.justice.gov/atr/us-and-plaintiff-states-v-google-llc` | Erro 404 | Não vi os documentos de prova |
| Cópia em `case-law.vlex.com` | Era outro processo (publicidade digital, Virgínia, 17/04/2025) e estava atrás de cadastro | Descartada |
| Search Engine Land sobre o vazamento — `https://searchengineland.com/google-search-document-leak-ranking-442617` | Erro 403 | Usei The Register para a frase do porta-voz |
| The Verge sobre a confirmação do vazamento — `https://www.theverge.com/2024/5/29/24167407/google-search-algorithm-documents-leak-confirmation` | A ferramenta não acessa o domínio | Idem |
| Ahrefs, endereço antigo — `https://ahrefs.com/blog/how-long-does-it-take-to-rank-in-google/` | Erro 404; o estudo abriu no endereço novo | Sem efeito |
| Semrush, endereço antigo — `https://www.semrush.com/ranking-factors/` | Redireciona para outro produto; o estudo abriu no blog, sem os números do gráfico | Coeficientes não lidos |
| Ajuda do Search Console, suposta página "sobre os dados" — `https://support.google.com/webmasters/answer/15964767` | Erro 404 (endereço que tentei adivinhar) | Prazo geral de guarda não confirmado |
| Documentação do sistema de diversidade — `D:appearance/site-diversity` | Erro 404 (não existe página própria); o texto está no guia dos sistemas | Sem efeito |
| Documentação de FAQ — `D:appearance/structured-data/faqpage` | Leva ao registro de mudanças (documentação removida) | É o próprio achado |

**Vistas só no resultado de busca, não abertas, e por isso não usadas como base:** relatório trimestral de taxa de
clique da Advanced Web Ranking (2026); estudo da GrowthSRC sobre taxa de clique (2025); página de ajuda do Google
Analytics que menciona 16 meses de dados do Search Console; publicação do Google de 2022 sobre filtros e limites dos
dados de desempenho; cobertura de terceiros sobre as unidades de agregador.

---

## 13. Endereços completos das fontes abertas

Documentação do Google (classe A):
- `https://developers.google.com/search/docs/fundamentals/how-search-works`
- `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/`
- `https://developers.google.com/search/docs/essentials`
- `https://developers.google.com/search/docs/essentials/technical`
- `https://developers.google.com/search/docs/essentials/spam-policies`
- `https://developers.google.com/search/docs/appearance/ranking-systems-guide`
- `https://developers.google.com/search/docs/fundamentals/seo-starter-guide`
- `https://developers.google.com/search/docs/fundamentals/creating-helpful-content`
- `https://developers.google.com/search/docs/fundamentals/using-gen-ai-content`
- `https://developers.google.com/search/docs/fundamentals/do-i-need-seo`
- `https://developers.google.com/search/docs/fundamentals/third-party-seo`
- `https://developers.google.com/search/docs/appearance/core-updates`
- `https://developers.google.com/search/docs/appearance/reviews-system`
- `https://developers.google.com/search/docs/appearance/title-link`
- `https://developers.google.com/search/docs/appearance/snippet`
- `https://developers.google.com/search/docs/appearance/page-experience`
- `https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials`
- `https://developers.google.com/search/docs/appearance/google-images`
- `https://developers.google.com/search/docs/appearance/ai-features`
- `https://developers.google.com/search/docs/appearance/aggregator-features`
- `https://developers.google.com/search/docs/appearance/structured-data/sd-policies`
- `https://developers.google.com/search/docs/appearance/structured-data/search-gallery`
- `https://developers.google.com/search/docs/appearance/structured-data/local-business`
- `https://developers.google.com/search/docs/appearance/structured-data/organization`
- `https://developers.google.com/search/docs/appearance/structured-data/breadcrumb`
- `https://developers.google.com/search/docs/appearance/structured-data/review-snippet`
- `https://developers.google.com/search/docs/crawling-indexing/links-crawlable`
- `https://developers.google.com/search/docs/crawling-indexing/url-structure`
- `https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls`
- `https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview`
- `https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap`
- `https://developers.google.com/search/docs/crawling-indexing/robots/intro`
- `https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl`
- `https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing`
- `https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics`
- `https://developers.google.com/search/updates` (registro de mudanças da documentação)
- `https://developers.google.com/search/blog/2024/03/core-update-spam-policies` (05/03/2024)
- `https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t` (15/12/2022; só para confirmar
  o endereço do PDF das diretrizes e que as notas dos avaliadores não influem direto)
- `https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history` e `https://status.search.google.com/summary`
- `https://support.google.com/webmasters/answer/7576553?hl=en` (relatório de desempenho)
- `https://support.google.com/webmasters/answer/7042828?hl=en` (impressão, posição e clique)
- `https://support.google.com/webmasters/answer/17011259?hl=en` (dimensões do relatório)
- `https://support.google.com/business/answer/7091?hl=en` (classificação local; detalhe no guia (b))

Estudos com dado (classe B, com o interesse anotado nas tabelas):
- `https://ahrefs.com/blog/links-matter-less-but-still-matter/` (30/01/2025)
- `https://ahrefs.com/blog/how-long-does-it-take-to-rank/` (15/05/2025)
- `https://backlinko.com/search-engine-ranking` (atualizada em 14/04/2025)
- `https://backlinko.com/google-ctr-stats` (atualizada em 16/04/2025)
- `https://backlinko.com/google-user-behavior` (atualizada em 14/04/2025)
- `https://www.semrush.com/blog/ranking-factors-semrush-study/` (04/01/2024)
- `https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/` (22/07/2025)
- `https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/` (02/07/2024)
- `https://www.nearmedia.co/eu-home-services-search-behavior/` (20/11/2024)
- `https://www.brightlocal.com/research/local-services-ads-click-study/` (19/10/2018)

Relatos, análises e jornalismo (classes C e D):
- `https://firstpagesage.com/reports/google-click-through-rates-ctrs-by-ranking-position/` (22/09/2026; classe D:
  agência de SEO, amostra de clientes e painel próprios; estava na lista de classe B até a correção de 13/11/2026)
- `https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/` (28/05/2024)
- `https://ipullrank.com/google-algo-leak` (27/05/2024)
- `https://www.blindfiveyearold.com/its-goog-enough` (08/11/2023)
- `https://www.theregister.com/2024/05/29/internal_google_search_documents/` (29/05/2024)
- `https://www.seroundtable.com/google-third-party-seo-tools-services-advice-41461.html` (08/06/2026; reprodução do texto do Google)
- `https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2020)` (datas do processo)
- `https://www.hobo-web.co.uk/united-states-v-google-llc-doj/` (09/10/2025; aberta e **descartada**: traz frases entre
  aspas sem página nem número de documento)
