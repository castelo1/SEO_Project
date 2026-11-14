# Verificação independente — item 3, parte 2 de 2: guia (c) respostas de IA, parte do ChatGPT e roteiro de teste

- **Data e hora:** sexta, 13/11/2026, das 20:45 às 20:59 (Brasília; `TZ=America/Sao_Paulo date`).
- **Quem verificou:** subagente em contexto limpo; não produziu os artefatos e não recebeu a conclusão de quem os fez.
- **Versão conferida:** a do commit `343047c` (13/11/2026, 20:52), igual em conteúdo ao que estava no disco quando li.
- **Artefatos:**
  - `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` (478 linhas) — "guia (c)"
  - `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` (504 linhas) — "03b"
  - `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` (214 linhas) — "roteiro"
- **Apoio lido:** `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md` (Parte 4) e
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`.
- **Ferramentas:** só leitura de arquivo, `shuf`, WebFetch e uma chamada de WebSearch. Nenhum navegador, nenhum
  assistente de IA aberto, nenhuma memória ou plug-in corporativo, nenhum subagente, nenhum commit. Único arquivo
  gravado: este.
- **Limite da ferramenta:** o WebFetch responde por um modelo pequeno, que corta citações em cerca de 125 caracteres.
  Citação entre aspas foi conferida pedindo o trecho e perguntando "a página contém exatamente a frase X?".

## VEREDITO

**APROVADO, com correções a fazer antes de fechar o item.**

- Sorteio: **12 OK · 0 FALHA · 0 INCONCLUSIVO** (critério: reprova com mais de 2 falhas).
- Seis conferências obrigatórias (a–f): **6 OK**.
- Seção "Complemento da sessão principal" do 03b: **INCONCLUSIVO** (403 em três tentativas; não conta como falha).
- Portão: **cumprido**, com uma ressalva de leitura no roteiro (falha 11) que cabe ao dono ou à sessão principal decidir.
- Fora do sorteio: **12 falhas numeradas**. Nenhuma é fonte inventada ou número errado; são uma atribuição que a
  fonte não sustenta (1), incoerência entre os arquivos (2, 3), fonte sem endereço (4), "consenso" e "regra" acima do
  que a evidência dá (5, 6, 7, 9), marca de data que falta (8), inferência sem marca (10), desenho do roteiro (11) e
  miudezas (12). As de número 1 a 7 mudam o que o dono lê e deveriam ser corrigidas antes de o item fechar.

---

## 1. O portão, transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linha 61)

> Três guias em `docs/estudo/`: (a) busca orgânica do Google para serviço local; (b) Google Maps e perfil de empresa,
> **dentro do que o item 2 permitiu**; (c) respostas de IA (o que faz um site ser citado). Cada tática com fonte e
> classe A–D. Cada guia termina em "o que é consenso / o que é disputado / o que não sei". Guia (c) curto é resultado
> aceitável **Pedido do dono em 13/11: além do Google, estudar o ranqueamento no ChatGPT.** O guia (c) passa a ter uma
> parte própria, `docs/estudo/03b_chatgpt.md`: como a busca do ChatGPT escolhe e cita fontes para um pedido de serviço
> local (de onde vem o índice, o papel do Bing e dos robôs da OpenAI como `OAI-SearchBot` e `GPTBot`, o que a
> documentação da OpenAI diz que um site precisa permitir, de onde vêm os dados de empresa local e de mapa, como
> citações em terceiros, avaliações e diretórios pesam), o que difere do Google e dos resumos de IA do Google, e como
> medir presença (quais perguntas testar, com que frequência, o que registrar). Fonte primária primeiro (documentação
> da OpenAI e do Bing), depois estudos com dado; relato de praticante e de vendedor de curso só com a classe marcada.
> A sessão **não** abre o ChatGPT nem digita em página: entrega `docs/estudo/03b_chatgpt_roteiro_de_teste.md` com 30
> perguntas reais de um morador ou síndico de São Paulo (por praga, bairro, urgência) e a planilha de registro, para o
> dono rodar na conta dele; o desenho do item 6 e o protótipo do item 7 trazem o que o estudo indicar (por exemplo
> `robots.txt`, dados estruturados, página "quem somos" verificável).

Esta verificação cobre só (c), o 03b e o roteiro. Os guias (a) e (b) são de outro verificador.

### 1.1 Conferência do portão

| Ponto | O que conferi | Resultado |
|---|---|---|
| (i) guia (c): cada tática com fonte e classe | Tabelas das seções 1 a 4 e 7 têm coluna de fonte e de classe. Exceções: linha 295 (duas fontes sem endereço — falha 4); linha 354 (classe "—"); linhas 337 e 355 (base é o item 2, marcadas "premissa" e "restrição") | **cumprido, com ressalva** |
| (i) guia (c) termina em consenso / disputado / não sei | Linhas 390–462; depois vem só o apêndice de fontes que não abriram | **cumprido** |
| (ii) de onde vem o índice | 03b seção 1 (linhas 97–157) | coberto |
| (ii) papel do Bing | 03b seções 1.2, 1.5 e 4 | coberto |
| (ii) robôs `OAI-SearchBot` e `GPTBot` | 03b seção 2 (linhas 161–199); conferidos na página oficial | coberto |
| (ii) o que a documentação da OpenAI diz que o site precisa permitir | 03b seção 2 (linha 175), seção 3.1 e o complemento (linha 33) | coberto |
| (ii) dados de empresa local e de mapa | 03b seção 5 e complemento (linhas 30–31) | coberto |
| (ii) como citações em terceiros, avaliações e diretórios pesam | 03b seção 5.3. Diretórios e citações: há dado B (F20, F21, F22). **Avaliações:** só F35 (D) e F26 (C); o texto não fecha dizendo "não sei" sobre o peso das avaliações | coberto, **fraco em avaliações** (falha 12) |
| (ii) o que difere do Google e dos resumos de IA do Google | 03b seção 7 | coberto |
| (ii) como medir: perguntas, frequência, o que registrar | 03b seção 8 e o roteiro | coberto (ver falha 3) |
| (ii) fonte primária primeiro; relato e vendedor com classe | A ordem das seções 1.1 → 1.2 → 1.3 → 1.4 respeita isso; a tabela de fontes (linhas 56–93) dá classe e "quem ganha" a cada uma das 36 | **cumprido** |
| (iii) exatamente 30 perguntas | Contei 30 itens numerados (linhas 59–88) e 30 linhas na tabela (94–123) | **30** |
| (iii) distribuição por praga, bairro e urgência | Ver 1.2 | cumprido, com ressalvas (falha 11) |
| (iii) planilha de registro | Colunas (linhas 141–162), cabeçalho CSV e duas linhas de exemplo (167–169) | **cumprido** |
| (iii) pergunta com dado pessoal | Nenhuma tem nome, endereço, telefone ou número de apartamento. As perguntas 6, 7 e 18 falam de criança e de picadas: são fictícias, mas o dono as digita na conta dele (observação, não falha) | sem dado pessoal |
| (iii) instrução proibida | Os avisos 2 e 3 (linhas 208–210) mandam **não** clicar em ligar, WhatsApp, orçamento, rota ou anúncio e **não** contatar empresa. Não há instrução de criar conta, aceitar termos ou preencher formulário | nenhuma |
| (iv) implicações para o desenho e o protótipo | 03b seção 9, 19 linhas, cada uma com fonte, classe e situação; bloco de `robots.txt`; "quem somos"; dados estruturados (linha 393) | **cumprido** (ver falha 7) |

### 1.2 Contagem da distribuição do roteiro (refeita por script sobre a tabela das linhas 94–123)

| Recorte | Contagem | Bate com a linha 127–132 do roteiro? |
|---|---|---|
| Praga | baratas 4 · baratas e formigas 1 · baratas e ratos 1 · ratos 4 · cupim 3 · escorpião 2 · percevejo 2 · pulgas 2 · formigas 2 · pombos 2 · mosquito 2 · geral 5 | sim |
| Zona | sul 6 · leste 6 · centro 6 · norte 5 · oeste 5 · cidade inteira 2 | sim |
| Urgência | agora/hoje 9 · planejado 21 | sim |
| Público | morador de casa 10 · morador de apartamento 7 · síndico ou síndica 6 · dono de bar, restaurante ou lanchonete 5 · não especificado 2 | sim |
| Tipo | indicação 17 · confiança 6 · comparação 4 · preço 3 | sim |

Conferi também cada linha da tabela contra o texto da pergunta (praga, bairro, urgência, público): batem. Os 28
bairros são distintos e a zona atribuída a cada um é aceitável.

O que a contagem cruzada mostra e o roteiro não avisa (falha 11): das 9 perguntas urgentes, **5 são da zona leste**
(5 das 6 perguntas da leste), 2 da oeste, 1 do centro, 1 da sul e **nenhuma da norte**. Nenhuma pergunta de morador
de apartamento é urgente.

---

## 2. Sorteio

**Método.** Candidatas = linhas de tabela com afirmação (começam com `|`, sem cabeçalho nem separador): guia (c)
linhas 78–274 (70 candidatas); 03b linhas 23–34 e 101–360 (100); roteiro linhas 23–31 (9). Embaralhei cada lista com
`shuf --random-source=<(openssl enc -aes-256-ctr -pass pass:<semente> -nosalt </dev/zero)`, sementes
`verif-item3-guia-20261113`, `verif-item3-03b-20261113` e `verif-item3-rot-20261113`, e peguei na ordem sorteada: 4
do guia (c), 7 do 03b, 1 do roteiro. Regras de substituição, fixadas antes de abrir qualquer fonte: (1) no máximo uma
afirmação por endereço; (2) pula a linha que o próprio artefato marca como hipótese, "não conferido" ou ponteiro
interno, porque não tem fonte para abrir. Puladas: guia (c) 189 e 180 (mesmo endereço de 188 e 179; conferidas como
bônus); 03b 303, 307 e 304 (lista de hipóteses), 223 (seção 3.2, "não conferido"; tratada na seção 3.2 abaixo) e 359
(ponteiro interno). Mistura final: 6 de classe A, 5 de classe B, 1 de classe D.

| # | Afirmação | Arquivo e linha | Endereço aberto | O que a fonte devolveu | Classe conferida | Resultado |
|---|---|---|---|---|---|---|
| 1 | 37,9% das URLs citadas na Visão geral nos 10 primeiros; 31,2% entre 11 e 100; 31,0% fora; 863 mil resultados, 4 milhões de URLs; 02/03/2026 | guia (c), 218 | https://ahrefs.com/blog/ai-overview-citations-top-10/ | Os três percentuais, "863K" e "4M", data de 2 de março de 2026, país não informado; cita ~76% de julho de 2025 e a "query fan-out" | B, vendedor anotado: correto | **OK** |
| 2 | `Applebot` alimenta a busca de Spotlight, Siri e Safari; 04/09/2026 | guia (c), 188 | https://support.apple.com/en-us/119829 | Data de publicação 4 de setembro de 2026; texto confirma. Bônus (linha 189): as duas frases sobre `Applebot-Extended` estão na página, exatas | A: correto | **OK** |
| 3 | Microsoft, sem meta tag: "No action is needed to remain in Bing Chat."; 22/09/2023 | guia (c), 179 | https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat | Data 22 de setembro de 2023; frase exata presente. Bônus (linhas 180–181): as frases de `NOCACHE` e `NOARCHIVE` existem, mas na página continuam depois do ponto onde o guia fechou as aspas | A: correto. Falta "pode estar desatualizada" na linha (falha 8) | **OK** |
| 4 | Taxa sem clique das mesmas palavras-chave foi de 33,75% para 31,53%; presença do resumo 6,49%, 24,61%, 15,69%; 15/12/2025 | guia (c), 247 | https://www.semrush.com/blog/semrush-ai-overviews-study/ | Todos os números, a data e "10M+" e "200K+" confirmados; país não informado | B: correto. Fonte de 2025 sem a marca (falha 8) | **OK** |
| 5 | Listas de diretórios que o ChatGPT "disse" usar quando perguntado; 2024 | 03b, 286 (F27) | https://www.yext.com/blog/where-do-google-gemini-chatgpt-get-local-business-information | Publicado em 13 de junho de 2024; o método foi perguntar ao próprio modelo; sem amostra; a Yext vende gestão de cadastros | D · desatualizada: correto | **OK** |
| 6 | Yelp em 80% das respostas do ChatGPT; 99.281 de 162.966 citações; TripAdvisor 10.227, OpenTable 9.147, BBB 4.247, Angie's List 1.768, Trustpilot 1.136, Yellow Pages 711, HomeAdvisor 705; 60.970 checagens; EUA, Reino Unido, Austrália; 26/08/2026 | 03b, 279 (F20) | https://www.brightlocal.com/resources/ai-directory-sources/ | Todos os números, os três países e a data confirmados. A página dá 1.355 locais num trecho e 1.365 em outro | B, vendedor anotado, país ao lado: correto | **OK** |
| 7 | Google: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."; ChatGPT: permitir o OAI-SearchBot e não barrar os IPs | 03b, 337 (F9 e F1) | https://developers.google.com/search/docs/appearance/ai-features e https://developers.openai.com/api/docs/bots | Frase do Google exata; exigência de página indexada e apta a trecho confirmada; recomendação da OpenAI confirmada | A: correto | **OK** |
| 8 | Bing Webmaster Tools: "Free and full of powerful features"; "Import your site from Google Search Console"; "Submit and monitor your sitemap"; confere ao menos uma vez por dia; 17/06/2025 | 03b, 238 (F4) | https://blogs.bing.com/webmaster/2025/6/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility/ | Data e as três frases confirmadas; "at least once every 24 hours". A mesma página lista "AI tools like ChatGPT and Inflection.ai" (linha 114 do 03b) | A, com "página de 2025": correto | **OK** |
| 9 | Filtrar por `ChatGPT-User`; pelo menos metade das páginas visitadas entrou no cache (F13) | 03b, 357 (F1 e F13) | https://developers.openai.com/api/docs/bots e https://think.resoneo.com/chatgpt-retrieval/ | F1 descreve o `ChatGPT-User`; a Resoneo diz "at least half" e chama isso de piso | A + B: correto | **OK** |
| 10 | Na API, "Like any other tool, the model can choose to search the web or not based on the content of the input prompt."; a página dos robôs não declara fatores | 03b, 211 (F1 e F3) | https://developers.openai.com/api/docs/guides/tools-web-search | Frase exata presente; a página não nomeia provedor e não fala do aplicativo; sem data | A (para a API): correto | **OK** |
| 11 | ChatGPT 2,1 buscas por pergunta; Perplexity 1,4; Grok 6,8; cerca de 5 milhões de buscas derivadas; 1–21/04/2026; país não declarado | 03b, 317 (F17) | https://docs.peec.ai/research/fanouts-per-prompt-by-engine | Os três números, "5 million query fan-outs", o período e "May 2026" confirmados; sem país e sem número de perguntas | B no 03b. Pelo critério do guia (c), linha 15 ("falta amostra, país ou método"), seria "B fraca" (falha 12) | **OK** |
| 12 | Busca local: 23% de coincidência entre repetições; 10% de respostas sem empresa; 4,1 empresas por resposta; cerca de 200 mil buscas; país não declarado; 16/09/2026 | roteiro, 24 | https://www.brightlocal.com/research/local-ai-visibility-study/ | Todos confirmados; a página não declara país (os exemplos são de cidades dos EUA) | B, vendedor anotado: correto | **OK** |

**Contagem do sorteio: 12 OK, 0 FALHA, 0 INCONCLUSIVO.**

### 2.1 Conferências obrigatórias

| | O que era para conferir | Endereço | O que a fonte devolveu | Resultado |
|---|---|---|---|---|
| a | Página oficial dos robôs da OpenAI: `OAI-SearchBot`, `GPTBot`, prazo de cerca de 24 horas | https://developers.openai.com/api/docs/bots (duas chamadas, a segunda com frases falsas de controle, rejeitadas) | Todas as frases citadas na seção 2 do 03b estão na página, inclusive "~24 hours", "navigational links", "Each setting is independent of the others" e os quatro user-agents com as versões citadas. Quatro robôs; sem data; não cita Bing, sitemap, `noindex` nem JavaScript | **OK** |
| b | Google: não há requisito adicional; o que diz de `llms.txt` | https://developers.google.com/search/docs/appearance/ai-features e https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | Frase exata na primeira. A segunda nomeia `llms.txt` e diz que a Busca do Google ignora esses arquivos; também confirma as frases sobre texto picado, dado estruturado, "still SEO" e "menções" inautênticas | **OK** |
| c | Chegada ao Brasil da Visão geral criada por IA e do Modo IA | https://blog.google/intl/pt-br/produtos/explore-e-encontre-respostas/novas-formas-de-se-conectar-com-a-web-com-as-visoes-gerais-criadas-por-ia/ e https://blog.google/intl/pt-br/produtos/busca-do-google-agora-o-brasil-ja-pode-usar-o-modo-ia-em-portugues | 15 de agosto de 2024 e 8 de setembro de 2025; os dois trechos em português estão nas páginas, exatos | **OK** |
| d | Estudo da Resoneo: percentuais, amostra, idioma | https://think.resoneo.com/chatgpt-retrieval/ (duas chamadas) | 1.249 respostas (682 e 567), 88 mil resultados, 26,9 mil páginas, 6,4 mil domínios; 63,6% × 34,7% × 1,6% (1.793 resultados); 23,6% × 74,6% (16.407); agosto 24,7% × 75,3%; gratuito com raciocínio 74,7% × 22,2% × 3,1%; "empresas e lugares" 100% e 95%; um terço troca de origem; índice próprio não é o Bing; campo sumiu em 21/07; Yelp, TripAdvisor e Google Maps; H1 em 387 de 463; 4 MB; 61–71% contra 0–17%. **Idioma:** a página só fala em "our English-language corpus", uma vez; "majoritariamente em inglês" (03b, linha 132) é leitura do autor do guia, não frase da fonte | **OK**, com a ressalva do idioma |
| e | Um número da BrightLocal e o país da amostra | linhas 6 e 12 do sorteio | F20 declara EUA, Reino Unido e Austrália; F21 não declara país, e os dois arquivos dizem isso | **OK** |
| f | Controle do Search Console (31/08/2026) e relatório de IA generativa | https://support.google.com/webmasters/answer/16908024?hl=en · https://support.google.com/webmasters/answer/16984139?hl=en · https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | "As of August 31, 2026, we've rolled out this control to all websites worldwide." (com apóstrofo tipográfico); cobre Visão geral, Modo IA e Discover; não afeta treino. Relatório: só impressões; dimensões páginas, países, datas, aparelhos; sem consultas, cliques, CTR ou posição. Anúncio de 3 de junho de 2026 com nota de 31 de agosto | **OK** |

### 2.2 Seção "Complemento da sessão principal" do 03b (linhas 16–40)

`https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt`, a variante
`…/9237897-chatgpt-search` e `https://help.openai.com/en/articles/12627856-publishers-and-developers-faq` devolveram
**403** à ferramenta de leitura (três tentativas). **INCONCLUSIVO, não FALHA:** a ferramenta não conseguiu ler; não
há indício de que a página diga outra coisa. Uma busca pelas duas frases entre aspas devolveu o artigo 9237897 e um
resumo compatível com "partners with other search providers" e com a reescrita em "one or more targeted" buscas; isso
é resultado de busca, não leitura da página, e não confirma os demais trechos (Microsoft, memória, localização por
IP, mapa, `OAI-Searchbot`, uso sem conta) nem o redirecionamento da página de publishers. Ficam apoiados só na
leitura da sessão principal.

### 2.3 Outras fontes abertas fora do sorteio (todas bateram, salvo as indicadas nas falhas)

Ahrefs Brasil de 23/10/2026 (6.698.455 palavras-chave; 47,4%; 11,8%; os sete domínios e o Reclame Aqui em 18º) ·
Ahrefs `llms.txt` (137.210 domínios; 28%; 97%; 1,1%) · Ahrefs sobre buscas derivadas do ChatGPT, F19 (duas chamadas:
66,6 milhões; 14,4%; 1,6; 22,9%; 13,1%; 8,9%; 6,8%; 75,9%; 84,4%; 68,3%; 63,4%; 46,4%; Reddit −88%; Wikipedia −80%;
EUA) · SparkToro e Gumshoe, F23 (duas chamadas; ver falha 3) · Pew 22/07/2025 (todos os números) · Whitespark
12/05/2025 (540 buscas; 15% e 93%; 92% e 6%) · políticas de spam do Google (frase sobre respostas de IA; troca de
links) · guia de sistemas de ranqueamento (diversidade de sites, "generally won't show more than two") · meta tag
robots (`nosnippet`, `max-snippet`, `nocache`) · rastreadores comuns do Google (`Google-Extended`, frase exata) ·
Bing "AI Performance", F5 (10/02/2026; frase exata; parceiros não nomeados) · Perplexity (três frases exatas) · Seer,
F24 (87%, 56%, cerca de 100 perguntas, "directional") · Semrush, F29 (Reddit de perto de 60% para cerca de 10%; a
Semrush duvida do parâmetro) · MarTech, F30 · Tecnoblog, F32 · Search Engine Journal, F14 (duas chamadas; ver falha 1).

**Não abri** (ficam sem conferência minha): Anthropic; IndexNow; texto da Microsoft de 08/10/2025; artigo da KDD;
BrightEdge; Peec "30 milhões"; Seer sobre CTR; os dois textos da Ahrefs sobre CTR; SparkToro sobre buscas sem clique;
Conversion; `llmstxt.org`; os três textos de 2025 do blog do Google; a ajuda 7042828; F2, F6, F7, F8, F10, F11, F12,
F15, F16, F18, F22, F25, F26, F28, F31, F33, F34, F35.

---

## 3. Classe de evidência — arquivos inteiros

| Pergunta | O que achei |
|---|---|
| Fonte D ou C como base de regra | Nenhuma regra apoiada só em C ou D. No guia (c), Conversion (C/D) e a reportagem sobre o Bing (C) estão marcadas "não vira regra". No 03b, as linhas 11 e 12 da seção 9 (C + B antiga; C + D) estão como **hipótese**. Ressalva: a frequência mensal (03b, linhas 362–364) cita F18, classe D, ao lado de F13 e F19 |
| "Consenso" que não é A nem duas B independentes | **Três casos** — falhas 5, 6 e 9 |
| Estudo de vendedor sem "quem ganha" | A tabela de fontes do 03b e as tabelas do guia (c) anotam o conflito. Faltam: Lily Ray e Peec de 03/03/2026 (guia (c), linha 295 — falha 4) e a reportagem do Search Engine Journal (guia (c), linhas 205–208) |
| Fonte sobre IA anterior a 2026 sem "pode estar desatualizada" | 03b: marcadas na tabela de fontes (F4, F6, F11, F12, F22, F24–F29); falta em F10 (19/12/2025). Guia (c): **falta em várias linhas** — falha 8 |
| Número de outro país sem o país ou tratado como do Brasil | Não achei número estrangeiro tratado como brasileiro. Os dois guias repetem "não vale para o Brasil". Imprecisões: o consenso 9 do guia (c) rotula "EUA" um conjunto em que Ahrefs e Seer têm país "não informado"; as linhas 342–343 do 03b ("19–20%", "287 km") não repetem que F21 não declara país |
| "O ChatGPT busca no Google" × Bing × índice próprio | A conclusão da seção 1.5 do 03b **decorre das fontes** e é cautelosa: Google por raspadores terceiros = "indício forte, não consenso" (uma B, uma C, uma D); Bing hoje = "disputado" (Microsoft em 2025, depoimento de 2025 e estudo de 2025 de um lado; a B de 2026 do outro). O que não decorre: "índice próprio" como consenso (falha 5) |
| A Microsoft aparece como buscador nomeado só onde há fonte? | Sim no corpo: F4 (A, Microsoft, 2025, conferida no sorteio), F12 (C), F24 (B, 2025), F21 ("relies on Yelp and Bing", conferido). A linha 26 do complemento ("A Microsoft (Bing) é o único buscador nomeado") depende da página que não consegui abrir; e o que a página nomearia é a **Microsoft**, pela política de privacidade — "(Bing)" é inferência (falha 10) |

---

## 4. Afirmação sem fonte e recomendação além da fonte

- **Lista de diretórios brasileiros (03b, linhas 297–307):** está marcada "HIPÓTESE, nenhum com evidência", em
  negrito, e remete à coluna de fontes do roteiro. **Cumpre.** Um detalhe errado: a linha 304 diz que GetNinjas,
  Habitissimo, Triider e Cronoshare "já [são] citadas" em
  `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md`, linhas 167–171; ali estão GetNinjas e
  Triider, o Habitissimo aparece como "não verificado" e a Cronoshare não aparece.
- **Seção 9 do 03b (implicações):** cada linha tem fonte, classe e situação; 10 das 19 estão marcadas como hipótese,
  premissa ou "não conferido". Uma linha afirma mais do que a base dá: falha 7.
- Demais achados: falhas 3, 4, 7 e 10.

---

## 5. Conferência do exemplo do dono (táticas 4.1 a 4.10 de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`)

Vereditos do guia (c), linhas 307–318, e do 03b, linhas 149–152, 323, 372–374 e 398.

| # | Veredito dado | Decorre da fonte citada? |
|---|---|---|
| 4.1 | Confirmada por A para o Google; "para o ChatGPT: ver 03b" | Sim para o Google (F1 e F2, conferidas). **O 03b não traz veredito explícito para a 4.1** (falha 12) |
| 4.2 | Permanece D; duas partes com apoio B; "busca no Google" tratada no 03b como "parcialmente apoiada e mal formulada" | Sim. O 03b sustenta com F13 (conferida), F11 (C) e F15 (D), sem chamar de consenso |
| 4.3 | Mecanismo confirmado por A no Google; moldes de busca permanecem D | Sim (F1 e F11 conferidas). No 03b a linha 316 ainda diz "não conferido", enquanto o complemento (linha 27) dá classe A (falha 2) |
| 4.4 | Confirmada por A, e por B quanto ao `llms.txt` | Sim (F1, F2 e Ahrefs conferidas) |
| 4.5 | Não provada; disputada | **Não dá para conferir:** as duas fontes (Peec de 03/03/2026 e Lily Ray de 17/06/2026) não têm endereço (falha 4). O veredito é conservador |
| 4.6 | Parte A, parte contrariada, parte D | Em parte. A política de spam fala em troca **excessiva de links**; tratar "troca de rankings" como troca de links é inferência razoável, não frase da fonte |
| 4.7 | Contrariada por A; eficácia alegada: D | A política **proíbe**; não mede eficácia. O guia diz isso na segunda frase; "contrariada" é palavra mais forte que a fonte |
| 4.8 | Parte B; no Brasil o Reddit é o 6º domínio citado (3,3%); "queda no ChatGPT: 03b" | Sim (Ahrefs Brasil conferida: 6º, 3,3%). O 03b tem o dado (F19, −88%, EUA; F29), mas **não dá o veredito** que o guia (c) remete a ele (falha 12) |
| 4.9 | Parte A, parte B, resto hipótese | Sim (diversidade de sites conferida; Ahrefs Brasil conferida) |
| 4.10 | Teste manual razoável; "uma vez por mês" contrariado por B; "API ≠ aplicativo" permanece D | A fonte confirma que os autores tratam a API como questão em aberto. **Mas os dois guias divergem:** o 03b (linha 372) diz que uma B (F13) apoia "a API não reproduz o aplicativo" e recomenda medição mensal (falha 3) |

Resumo: os vereditos decorrem das fontes nos casos 4.1 (Google), 4.2, 4.3, 4.4, 4.8 e 4.9; 4.6 e 4.7 usam palavra um
pouco mais forte que a fonte; 4.5 não é conferível; 4.10 está em conflito entre os dois arquivos.

---

## 6. Coerência entre os três arquivos e com `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`

- **Com o item 2:** nenhuma recomendação depende de perfil de empresa próprio, de compra de citação ou de avaliação
  fabricada. Perfil do Google, Bing Places e avaliações são tratados como **da licenciada** (guia (c), linhas 149 e
  343; 03b, linhas 245–253, com "premissa adotada: vedado"). O que exige conta (Search Console, Bing Webmaster Tools)
  fica como ação do dono. O que exige contato com terceiros está marcado "fora da rodada" no guia (c), linha 341; na
  linha 14 da seção 9 do 03b está só "com autorização delas", sem dizer que fica fora da rodada.
- **Roteiro × 03b sobre conta logada:** coerentes (passada logada mais subamostra deslogada; 03b, linhas 372–374).
- **Roteiro × complemento sobre memória e localização:** incoerentes (falha 2).
- **Roteiro × guia (c) sobre como medir:** incoerentes (falha 3).

---

## 7. Forma

| Ponto | Resultado |
|---|---|
| Português | Sim. Inglês só em citação literal curta de documentação |
| Caminhos absolutos | Sim para arquivos do projeto. "guia (a)" aparece sem caminho no guia (c), linhas 80 e 138, e no 03b, linha 393 |
| Nome de pessoa física do mercado local | Nenhum. Só autores de fonte |
| Exemplos fictícios do roteiro marcados "EXEMPLO" | Sim: as duas linhas do CSV, os nomes de empresa, o modelo e os domínios (`.example`); o `robots.txt` do 03b usa `EXEMPLO.example` |
| Número com unidade, período, país e fonte | Sim na quase totalidade; ver falhas 4 e 8 |
| Citação literal longa | Não há |

---

## 8. Falhas numeradas, com a correção sugerida

**1. Atribuição que a fonte não sustenta (03b, linha 139).** O texto diz que a matéria do Search Engine Journal (F14)
"registra que não houve comentário" da OpenAI. Em duas leituras, a matéria não tem frase alguma sobre comentário,
confirmação ou recusa; só diz que a página dos robôs não detalha o índice próprio. *Correção:* trocar por "a matéria
não traz posição da OpenAI; registra que a página dos robôs não descreve o índice próprio".

**2. O complemento foi acrescentado sem reconciliar o resto (03b e roteiro).** O arquivo hoje afirma as duas coisas.
Linhas que ficaram contraditórias com as linhas 16–40: 12–14 ("nada dali entrou como classe A"); 107–108; 153–154
("não conferida, a ajuda da OpenAI"); 215–230 (seção 3.2 inteira, com outro endereço para o mesmo artigo 9237897);
264–265 ("nada foi conferido"); 316 e 325; 344 (localização: "não conferido"); 345 (memória: "não sei, ajuda não
aberta"); 456–457 ("a OpenAI não confirma nada disso em fonte que eu tenha aberto"); 469–470; 485. No roteiro: linha
31 ("premissa não conferida") e linha 42 ("não sei"), quando o complemento diz que deixou de ser premissa; a linha 43
não menciona que, sem bairro na pergunta, a cidade vem do IP (perguntas 12 e 25), e não há coluna para anotar rede
ou VPN, que o complemento pede. *Correção:* atualizar essas linhas, apontando para o complemento e dizendo que ele
foi lido só pela sessão principal no navegador e que o verificador recebeu 403; acrescentar ao roteiro a coluna de
rede.

**3. Os dois guias dão instruções opostas sobre como medir, e uma frase omite o que a fonte diz.**
- Guia (c), linhas 318 e 376–378: "uma vez por mês" é contrariado por B; várias execuções, em dias diferentes, em
  **janela anônima**. 03b, linhas 362–364, e roteiro, linhas 178–180: **mensal, uma execução por pergunta, logado**
  em chat temporário, no mesmo dia; repetir é opcional.
- Guia (c), linha 377: "os autores do estudo B também dizem que não sabem" quantas execuções bastam. A página da
  SparkToro lista a pergunta como aberta, mas dá a orientação prática "usually at least 60-100X, then average these
  out" (duas leituras). O roteiro apoia a escolha de frequência nessa mesma fonte e roda 1 vez.
- "API ≠ aplicativo": permanece D no guia (c), linha 318; apoiada por uma B no 03b, linha 372.
*Correção:* escolher uma regra e escrevê-la igual nos três arquivos. Sugestão: manter a rodada mensal de 30
perguntas como **amostra agregada** ("em quantas das 30"), dizer com todas as letras que ela não mede uma pergunta
isolada, citar a orientação de 60 a 100 repetições como opinião prática dos autores, e tornar obrigatória (não
opcional) a repetição de um subconjunto.

**4. Duas fontes sem endereço (guia (c), linha 295; usadas também nas linhas 313, 351 e 434–435).** "Peec
(03/03/2026, 232 mil citações)" e "Lily Ray (17/06/2026, 100 buscas)" não têm URL em lugar nenhum do arquivo; Lily
Ray também não tem "quem ganha". A regra de evidência pede URL para cada fonte. Não pude conferir os números 11% e
69%. *Correção:* pôr os dois endereços e o conflito de interesse, ou rebaixar as linhas a "não conferível".

**5. "Índice próprio" como consenso sem cumprir a regra (03b, linhas 145–146 e 444).** A base é "F1, A, por
decorrência" mais uma B (F13). F1 não descreve índice — a linha 139 do mesmo arquivo diz isso — e F15–F16 são
classe D. Fica uma B mais uma inferência. *Correção:* mover para "indício forte" ou escrever "consenso: a OpenAI
rastreia com robô próprio (A); índice próprio: uma B e inferência".

**6. "Com o Yelp à frente" como consenso (03b, linhas 446–449).** F13 confirma que o Yelp é **uma** das alimentações,
sem dar participação; "à frente" e "80%" vêm só de F20, da BrightLocal, que vende cadastro em diretórios (F21 é da
mesma empresa). *Correção:* consenso = "plataformas de avaliação e diretórios, entre elas o Yelp"; "à frente" = uma
B de vendedor.

**7. Página "quem somos" classificada acima da base (03b, linha 396).** A linha diz "restrição legal (A no item 2)" e
"regra pelo item 2", citando o "quadro de vereditos, linha 29". A linha 29 de
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` trata de avaliação comprada; o ponto certo é a
linha 30 e a conclusão (iii), linhas 246–251, que o próprio item 2 marca como **inferência**; e a linha 236–237 diz
que CNPJ **não** é exigido na propaganda. O guia (c), linha 337, está certo ("premissa marcada"). *Correção:* igualar
ao guia (c) e corrigir as linhas citadas (também a referência "linhas 24–27" da linha 251 do 03b, que é 25–27).

**8. Falta "pode estar desatualizada" em fontes anteriores a 2026 no guia (c).** Linhas 179–182 (Bing, 2023), 185
(Microsoft, 08/10/2025), 244 (Ahrefs, 17/04/2025), 246 (Seer, 04/11/2025), 247 (Semrush, 15/12/2025); e nas ações da
seção 7.1: linha 334 (apoiada só em F3, de 2025, e no texto da Microsoft de 2025, com classe A) e linha 340 (Bing,
2023). No 03b: F10 e as linhas 8 e 10 dos consensos, que usam F4 e F6 de 2025. *Correção:* acrescentar a marca.

**9. Consenso 9 do guia (c) (linhas 410–411) convive com uma B que o contraria.** "Quando há resumo de IA, o clique é
menor [B × 2, EUA]"; a linha 247 traz a Semrush (B) marcada "**contraria**", e Ahrefs e Seer têm país "não
informado". *Correção:* mover a direção para "disputado" ou restringir o consenso ao que a Pew mediu, tirando o
rótulo "EUA" de Ahrefs e Seer.

**10. Inferências sem marca.**
- 03b, linha 31: de "On iOS and Android, relevant results may also include a map" o texto conclui "mapa **só** no
  aplicativo de celular". A frase não diz "só"; e o roteiro recomenda rodar no computador (linha 45) com uma coluna
  de mapa.
- 03b, linha 26: "(Bing)" depois de "Microsoft".
- Guia (c), linhas 167–168: "um site intermediário aparece, se aparecer, como fonte de informação, não como a
  empresa recomendada" está como leitura; o item 3 de "não sei" (linha 449) diz que isso não se sabe.
- Guia (c), linhas 34 e 403: "a **única** orientação oficial" é "a única que encontrei".
- Roteiro, linhas 37, 40 e 202: "logado é como a maioria usa", "padrão é o que o morador comum usa" e "só tratar
  como mudança o que se repetir em duas rodadas" não têm fonte nem marca de premissa.
*Correção:* marcar cada uma como inferência ou premissa.

**11. Roteiro: público, bairro e urgência.**
- 5 das 30 perguntas (4, 14, 20, 21, 28) são de dono de bar, restaurante ou lanchonete. O portão fala em "morador ou
  síndico de São Paulo". Li "morador de São Paulo" como quem mora na cidade, o que inclui o comerciante, e por isso
  não reprovei; na leitura estrita (morador de residência ou síndico) são 25. **Decisão do dono ou da sessão
  principal:** manter, dizendo isso no roteiro, ou trocar as 5.
- As perguntas 12 e 25 não têm bairro.
- Urgência e zona estão confundidas: 5 das 9 urgentes são da leste e nenhuma da norte. O indicador "recortes por
  região e por urgência" (linha 200) não separa uma coisa da outra, e com 2 perguntas por praga o recorte por praga
  não sustenta conclusão. *Correção:* redistribuir duas ou três urgências para norte e sul e avisar o limite dos
  recortes.

**12. Miudezas.**
- 03b, linha 404: "F1 não o menciona" (`llms.txt`). A página dos robôs tem um link para o `llms.txt` do próprio site
  de documentação; não diz que os robôs consomem o arquivo de terceiros. A conclusão se mantém; a frase não.
- 03b, linha 339: "três robôs"; a seção 2 lista quatro.
- 03b, linha 132: "majoritariamente em inglês" não é frase da Resoneo.
- 03b, linha 371, e roteiro, linha 26: "14,4% … busca menos". A Ahrefs corrigiu a própria frase: 14,4% das respostas
  **continham buscas derivadas**, não "buscaram na web"; e o estudo só tem sessões gratuitas deslogadas.
- 03b, linha 317: F17 como "B" sem número de perguntas nem país; pelo critério do guia (c) seria "B fraca".
- 03b: falta veredito explícito para as táticas 4.1 e 4.8, que o guia (c) remete a ele; falta dizer "não sei" sobre
  o peso das avaliações.
- Guia (c), linhas 436–439: os itens 6 e 7 de "disputado" usam como um dos lados uma fonte **não aberta** (o texto
  dos "88%" e a Steady Demand).
- Guia (c), linhas 180–181: aspas fechadas com ponto onde a frase da página continua.
- Guia (c), linha 112: "F8 diz o mesmo"; o anúncio diz "included in the overall performance report", sem citar o
  tipo "Web", e inclui o Discover.
- Guia (c), linha 218: "ela diz que a comparação não é direta"; a página aponta as mudanças de método e de modelo,
  sem essa frase.

---

## 9. O que esta verificação não cobre

- A leitura no navegador feita pela sessão principal (complemento do 03b): 403 para mim.
- As fontes listadas em "Não abri" na seção 2.3.
- Os guias (a) e (b) do item 3.
- Se as 30 perguntas são "reais" no sentido de terem sido observadas em algum lugar: são plausíveis e escritas em
  linguagem de morador, mas não há fonte que mostre de onde vieram.
