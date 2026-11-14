# Mapa do mercado de busca — dedetização em São Paulo (item 4)

- **O que é:** quem aparece no Google quando alguém busca dedetização em São Paulo — no resultado orgânico, no bloco de
  mapa e nos anúncios — numa **amostra declarada** de 89 buscas feitas ao vivo em sexta, 13/11/2026 (Brasília), em duas
  janelas: 79 (grupos A a G) das 20:26 às 21:16 e 10 (grupo H) das 23:18 às 23:31; mais 5 repetições das 23:32 às
  23:37. **Não é censo, não é posição média, não é volume de busca.**
- **Como ler:** as contas das seções 1 (itens 1 a 7) e 3 a 9 são da **amostra principal** (79 buscas, grupos A a G).
  O grupo H está na seção 12 e as repetições, na seção 13.
- **Arquivos:**
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` — 1.180 linhas (1.060 dos grupos A a G e 120 do grupo H), uma por resultado visto (anúncio, perfil no
    bloco de mapa, resultado orgânico), com termo, hora, logado, local exibido.
  - `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_registro.md` — o registro de cada busca (termo, hora,
    conta logada, localização que o Google mostrou).
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` e
    `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md` — os 157 domínios do orgânico dos grupos A a G, por
    frequência, com a classe (empresa, diretório, rede ou satélite) de 77 deles (quais, na seção 7.1).
  - `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` — 2.721 termos por praga × local × intenção (1.260 quando o
    item 4 foi verificado; ampliado em 14/11/2026 pela fila de reserva 1), com "volume: não medido" (seção 10).
  - Brutos e scripts: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/` (lotes `lote_01.jsonl` a `lote_08.jsonl`,
    as repetições em `repeticao_01.jsonl`, `coletor.js`, `monta_csv.py`, `monta_registro.py`) e `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`.
- **Fonte de todo número deste arquivo**, salvo indicação: os arquivos acima (Brasil, cidade de São Paulo, 13/11/2026).
  Para refazer as contas: `python3 /home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_csv.py`.

## 1. Em uma página

1. **A página de resultado de uma busca comercial de dedetização em São Paulo tem quatro camadas.** Em 79 buscas:
   "Visão geral criada por IA" em 73; bloco de mapa "Empresas" em 68; anúncio de texto em 60; perfil patrocinado dentro
   do bloco de mapa em 47. Só 12 buscas não tinham nenhum anúncio. A ordem vertical das camadas **não foi registrada**.
2. **O orgânico é de sites de dedetizadoras, com uma página por bairro.** 709 resultados, 157 domínios; os 10 domínios
   mais frequentes somam 39% dos resultados e os 20 mais frequentes, 57%. Nas buscas por bairro, 87% dos resultados
   são páginas internas com o nome do local no endereço (`/dedetizadora-em-pinheiros/`); em 21 das 32 buscas com bairro,
   os três primeiros são todos desse tipo.
3. **Diretório e marketplace aparecem pouco.** Um diretório (ohub.com.br) está em 21 das 79 buscas, quase sempre do
   meio da página para baixo (posição mediana 5); os demais (triider, reclameaqui, coteibem, pedegas, pestwase,
   listazn) aparecem uma ou duas vezes. Rede social e fórum: 6 resultados em 709.
4. **Quase tudo é site que se apresenta como dedetizadora; intermediário declarado, só os diretórios.** Lidos 77
   domínios — os 48 com 3 ou mais aparições, 18 dos 22 com 2 e 11 com 1 (86% dos resultados): empresas identificadas, 60% dos resultados; marcas sem identificação
   e domínios satélites, 20%; diretórios, 4%. **Só 12 dos 67 sites de serviço lidos mostram o número da licença**
   sanitária na página, que é o que a regra de propaganda pede (seção 7).
5. **O bloco de mapa muda com o bairro e com o lugar de quem busca** (a parte do lugar de quem busca é inferência:
   houve um só ponto de busca). 64 perfis distintos em 202 linhas; três perfis
   ocupam 43% das linhas, e um deles é de Osasco — a cidade que o Google exibiu como localização do navegador em parte
   das buscas. Nas 20 buscas por bairro apareceram 37 perfis distintos. Nota mediana 5,0; 96% das linhas com nota 4,8
   ou mais; mediana de 146 avaliações por perfil.
6. **Um único anunciante domina a amostra:** aparece nos anúncios de texto de 58 das 79 buscas e como perfil
   patrocinado em 47. Nenhum anúncio foi clicado.
7. **Nas duas buscas de escorpião, o resultado é do governo:** em "controle de escorpião" (cidade e Butantã), 12 dos 16
   resultados são de órgãos públicos e do Instituto Butantan; não há bloco de mapa.
8. **Não sei:** volume de busca de qualquer termo; o que a "Visão geral criada por IA" citou em cada busca (só a
   presença foi registrada); o resultado para quem busca de outro ponto da cidade, deslogado ou pelo celular.
9. **As buscas de confiança, preço e informação (grupo H, 10 buscas) mostram outra página de resultado:** resumo de
   IA em 10 de 10; bloco de mapa só em 2 (as duas com "sp" ou "são paulo" e intenção de contratar); nenhum anúncio em
   3. No orgânico (86 resultados, 60 domínios), 28 domínios não tinham aparecido nas 79 buscas anteriores. Nas quatro
   buscas informativas, três primeiras posições são de imprensa, de um site de fabricante e de uma loja de produtos
   para animais; em "como saber se dedetizadora é licenciada", a consulta pública de licenças do estado aparece em
   segundo; nas três de preço, a mesma página de "tabela de preço" de uma dedetizadora está em primeiro (seção 12).
10. **Cinco buscas repetidas de 2 a 3,1 horas depois deram quase o mesmo:** o primeiro resultado é o mesmo nas cinco e os
    três primeiros domínios são os mesmos nas cinco; o bloco de mapa repetiu os três perfis em 3 delas e dois de três
    em 2 (seção 13). Vale para a mesma noite, o mesmo navegador e a mesma conta.

## 2. Método e amostra

### 2.1 O que foi buscado

89 consultas planejadas em oito grupos (`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas.csv`), escolhidas por
mim para cobrir o que o portão pede (por praga, por bairro ou região, "24 horas", empresa × residência). **São termos
plausíveis, não os termos mais buscados:** não há volume medido (seção 10).

| Grupo | O que é | Planejadas | Feitas |
|---|---|---|---|
| A | genérica + cidade ("dedetização são paulo") | 10 | 10 |
| B | praga + cidade ("desratização são paulo") | 13 | 13 |
| C | região ("dedetizadora zona leste sp") | 5 | 5 |
| D | bairro ("dedetizadora moema"), 20 bairros das cinco regiões | 20 | 20 |
| E | praga × bairro ("descupinização pinheiros") | 12 | 12 |
| F | empresa × residência (restaurante, condomínio, apartamento, escola, indústria) | 13 | 13 |
| G | urgência ("24 horas", "urgente", "hoje", "aberta agora") | 6 | 6 |
| H | confiança, preço e informação ("dedetizadora com licença…", "quanto tempo dura…") | 10 | 10 (segunda janela, 23:18–23:31) |
| | **Total** | **89** | **89** |

### 2.2 Como foi buscado

- **Onde:** busca web do Google (`https://www.google.com/search?q=<termo>&hl=pt-BR&gl=br&pws=0`), pelo endereço, no
  navegador pessoal do owner (Chrome, computador), numa aba aberta pela sessão. **Não é o aplicativo nem o site do
  Google Maps:** o "mapa" deste arquivo é o bloco "Empresas" que a busca web mostra (em geral 3 perfis, às vezes mais
  um patrocinado).
- **Conta:** **logado** na conta Google do owner em todas as 89 (só leitura; nenhum painel aberto). O parâmetro
  `pws=0` pede resultado sem personalização; **não garante** que ela esteja ausente.
- **Localização que o Google mostrou:** "São Paulo, SP" em 33 das 79 buscas da amostra principal, "Osasco, SP" em 10,
  nenhuma em 36 (a página não exibiu local); no grupo H, "São Paulo, SP" em 2 e nenhuma em 8. O Google atribuiu ao navegador uma posição na zona oeste da Grande São Paulo; o bloco de mapa reflete
  isso (seção 5).
- **Quando:** sexta-feira à noite, 20:26 a 21:16 (grupos A a G) e 23:18 a 23:37 (grupo H e repetições). Hora de cada busca: lida do relógio da própria página (momento da
  navegação). Uma atualização central do Google estava em curso desde 10/11/2026
  (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`): os resultados podem estar em movimento.
- **O que se leu de cada página**, por um script que só lê o que está na tela
  (`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js`): se há "Visão geral criada por IA"; domínio dos
  anúncios de texto; nome, nota e número de avaliações dos perfis do bloco "Empresas" e do perfil patrocinado; domínio,
  caminho e título dos resultados orgânicos da primeira página (9, em geral). Telefones foram mascarados como `[tel]`
  antes de sair da página; o título e o fim do endereço de uma reclamação de consumidor (busca D05, posição 7) foram
  omitidos em 14/11/2026, no bruto e no CSV. **Nada foi clicado:** nem anúncio, nem "ligar", nem "WhatsApp", nem "rota", nem site.
- **Intervalo entre buscas:** mediana de 28 segundos (mínimo 17, máximo 224). **Três intervalos ficaram abaixo dos 20 segundos da regra da
  rodada, por erro meu na montagem do lote:** B11→B12 (18 s), D02→D03 (19 s) e E02→E03 (17 s). Na segunda janela (grupo H e
  repetições) o intervalo ficou entre 67 e 124 segundos.

### 2.3 Limites da amostra (ler antes de usar qualquer número)

1. **Um ponto, uma hora, uma conta.** Tudo foi visto de um único lugar (zona oeste da Grande São Paulo), numa sexta à
   noite, logado. O bloco de mapa depende de onde está quem busca e de quem está aberto na hora
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seções 4.3 e 6). O orgânico também pode
   variar.
2. **Uma busca por termo**, salvo cinco repetidas na mesma noite (seção 13): não dá para separar o que é estável do
   que é ruído entre dias, lugares e contas.
3. **Só a primeira página, só a busca web.** A lista completa do Maps não foi coletada (a ampliação de 14/11 também não a
   incluiu; está em "Desdobramentos" no painel).
4. **Ordem vertical não registrada.** O script não guardou se o bloco de mapa e os anúncios vinham acima do orgânico;
   a premissa do guia (a) de que vêm acima **não foi conferida nesta amostra**; a ampliação de 14/11 registrou a
   posição vertical em 40 buscas (`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, seção 4; não verificado).
5. **"Visão geral criada por IA": só a presença.** O script detectou o rótulo na página; não registrou se o resumo
   estava aberto, o que dizia nem que fontes citava.
6. **Títulos e caminhos cortados.** Título em até 60 caracteres nos lotes 1 e 2 e em 34 nos lotes 3 a 8 (três títulos do
   lote 3 têm 35 ou 36); caminho em 50.
   Contagens de palavras no título ("24 horas", "preço") são piso, não valor exato.
7. **Anunciante não identificado em 31 dos 102 anúncios de texto** (a leitura do domínio falhou; saiu "google.com").
8. **Tipo de página pelo endereço, não pelo conteúdo.** "Página interna por local" = o caminho contém o nome de um
   bairro ou região da lista do script. A coleta não leu as páginas; a leitura da seção 7 abriu de 1 a 3 por domínio e a
   fila de reserva 2 mediu dez. **Não afirmo que sejam "páginas de entrada"** no sentido da política de spam do
   Google: isso exigiria comparar o texto de várias páginas do mesmo site, o que não foi feito.
9. **Consulta automática.** A política de spam do Google lista o envio de consultas automáticas entre as práticas que
   veda (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 8). A rodada autorizou até 600
   buscas com 20 segundos de intervalo; a decisão de manter isso está na fila do owner
   (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`).

### 2.4 O que deu errado na coleta

- **Verificação de robô às 21:16.** Na 80ª busca válida (H01, "dedetizadora confiável são paulo"), 49 minutos depois
  do início da coleta (20:26) e 23 minutos depois da última pausa longa (20:52), o Google mostrou a página de "tráfego incomum". **Não foi resolvida.** As buscas ao
  vivo pararam por 2 horas, como manda a regra da rodada; a aba foi fechada.
- **Retomada às 23:18**, duas horas depois, só com o que faltava: as 10 buscas do grupo H e 5 repetições, com 67
  segundos ou mais entre uma e outra. **Não houve nova verificação de robô.** A aba foi fechada às 23:38.
- **Lotes de teste descartados (20:10–20:22).** Um lote de 5 buscas estourou o tempo da ferramenta, continuou rodando e
  se sobrepôs ao seguinte, com buscas a menos de 20 segundos e rótulos trocados. Descartei tudo e recomecei; desde
  então cada registro guarda o termo lido do título da própria página.
- **Queda de conexão às 20:55.** Um lote seguiu rodando sem resposta; um registro saiu duplicado (D17), removido ao
  gravar; uma busca (D18) pode ter sido enviada duas vezes.
- **Total gasto do limite de 600:** cerca de 110 buscas — 89 válidas, 5 repetições, 1 barrada e cerca de 15 perdidas
  em testes e lotes descartados.

## 3. O que a página mostra, por grupo de busca

Número de buscas em que cada camada apareceu.

| Grupo | Buscas | Visão geral criada por IA | Bloco "Empresas" | Anúncio de texto | Perfil patrocinado no bloco |
|---|---|---|---|---|---|
| A genérica + cidade | 10 | 10 | 10 | 8 | 8 |
| B praga + cidade | 13 | 13 | 11 | 11 | 6 |
| C região | 5 | 4 | 5 | 5 | 5 |
| D bairro | 20 | 16 | 17 | 9 | 14 |
| E praga × bairro | 12 | 11 | 8 | 10 | 6 |
| F empresa × residência | 13 | 13 | 12 | 11 | 6 |
| G urgência | 6 | 6 | 5 | 6 | 2 |
| **Total** | **79** | **73 (92%)** | **68 (86%)** | **60 (76%)** | **47 (59%)** |

- **Sem resumo de IA (6):** "dedetizadora zona oeste sp", "dedetizadora mooca", "dedetização perdizes", "dedetização
  ipiranga", "dedetização campo limpo", "cupim vila mariana dedetizadora".
- **Sem bloco "Empresas" (11):** as duas de escorpião; mosquito da dengue; "dedetizadora santana" (os resultados são
  de uma empresa que se chama Santana); "dedetizadora santa cecília"; "dedetização campo limpo"; "cupim vila mariana
  dedetizadora"; percevejo na Bela Vista; pulgas no Ipiranga; "comprovante vigilância sanitária"; "dedetizadora 24h
  zona leste".
- **Contraste com o estudo citado no guia (c):** nos Estados Unidos, em 2025, a Whitespark achou resumo de IA em 15%
  das buscas de "serviço + cidade" (540 buscas no total do estudo, locais e informativas, em 3 cidades; classe B, amostra pequena;
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, seção 2). Aqui, em novembro de 2026, logado,
  foi 92%. As duas medidas não são comparáveis (país, data, método), mas a premissa "busca local quase não dispara
  resumo de IA" **não vale para esta amostra**.

## 4. Resultado orgânico

### 4.1 Concentração

- 709 resultados orgânicos, 157 domínios. Os 5 mais frequentes somam 23% dos resultados; os 10 mais frequentes, 39%; os
  20 mais frequentes, 57%. 83 domínios apareceram uma única vez.
- **Primeira posição:** dedetizadora.srv.br em 16 das 79 buscas; eccocleandedetizacao.com.br em 12;
  protecpragas.com.br e keikodedetizadora.com.br em 6 cada; biosp.com.br em 5; prefeitura.sp.gov.br e
  ecoservicos.com.br em 4 cada.
- **Os dez domínios mais frequentes** (resultados · buscas em que aparece · vezes entre os três primeiros):
  dedetizadora.srv.br (45 · 45 · 30); eccocleandedetizacao.com.br (36 · 34 · 21); keikodedetizadora.com.br (29 · 29 ·
  20); uniprag.com.br (26 · 26 · 4); protecpragas.com.br (26 · 26 · 10); dedetizabem.com.br (25 · 25 · 6);
  deltadedetizacao.com.br (23 · 23 · 6); termitek.com.br (23 · 22 · 6); ohub.com.br (22 · 21 · 5); ecoservicos.com.br
  (20 · 20 · 12). A lista inteira está em `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`.
- **Por grupo, quantos domínios respondem por metade dos resultados:** A, 10 de 37; B, 9 de 45; C, 6 de 22; D, 12 de
  66; E, 17 de 62; F, 7 de 47; G, 8 de 31. A busca por praga × bairro é a mais espalhada; a de empresa × residência, a
  mais concentrada.

### 4.2 Tipo de página (pelo endereço)

Percentual dos resultados orgânicos de cada grupo.

| Grupo | Página interna por local | Página interna de serviço ou outra | Página inicial | Blog ou artigo | Governo ou universidade | Rede social ou fórum |
|---|---|---|---|---|---|---|
| A genérica + cidade (90) | 13 | 52 | 29 | 3 | 2 | 0 |
| B praga + cidade (116) | 4 | 69 | 8 | 9 | 9 | 1 |
| C região (45) | 84 | 7 | 2 | 7 | 0 | 0 |
| D bairro (181) | 87 | 2 | 7 | 2 | 0 | 2 |
| E praga × bairro (107) | 79 | 10 | 1 | 2 | 7 | 1 |
| F empresa × residência (117) | 1 | 68 | 15 | 13 | 3 | 1 |
| G urgência (53) | 32 | 34 | 26 | 8 | 0 | 0 |

- Entre os três primeiros de todas as buscas (237 resultados): 104 páginas internas por local, 85 páginas internas de
  serviço, 34 páginas iniciais, 10 de governo, 3 de blog, 1 de rede social.
- **Nas buscas com bairro predominam páginas do bairro.** Em 21 das 32 buscas dos grupos D e E, os três primeiros são todos páginas
  internas por local. 249 das 316 páginas por local têm o endereço em um nível só (`dominio/bairro/`).
- **Treze domínios aparecem em 5 ou mais das 20 buscas por bairro**, quase sempre com a página daquele bairro (95 de
  98 resultados; as exceções são a página inicial de primordialdedetizacao.com.br na busca da Bela Vista e a página
  da cidade de ohub.com.br nas buscas do Ipiranga e de Campo Limpo):
  protecpragas.com.br (11), lunardedetizadora.com.br, keikodedetizadora.com.br e dedetizadora.srv.br (10 cada),
  primordialdedetizacao.com.br (8), dedetizadoraddpilar.com.br e biodesin.com.br (7 cada), zet-tecdedetizadora.com.br,
  ohub.com.br, hidrosampa.com.br e ambientalepragas.com.br (6 cada), grupoexpansao.com e etoprag.com.br (5 cada).
- **Domínio com o nome exato do bairro** aparece, mas pouco: dedetizadoraemmoema.com.br,
  dedetizadoranamooca.com.br, dedetizadoraemhigienopolis.com.br, dedetizadoranobutanta.com.br,
  dedetizadoranavilamadalena.com.br, dedetizadoranavilamariana.com.br e dedetizadorazonaleste.net, uma vez cada.
- **Nas buscas de empresa (grupo F) predominam páginas de segmento** ("dedetização para restaurantes", "condomínios",
  "escolas"), não páginas de bairro (68% contra 1% na tabela acima); aparecem ali sites de multinacionais
  (rentokil.com, 3 resultados no grupo F — 5 na amostra, com 1 em A e 1 em B; orkinbrasil.com.br e orkinsp.com.br, 1
  cada) que não aparecem nas buscas por bairro.

### 4.3 O que os títulos dizem (piso; títulos cortados)

A contagem inclui palavra cortada pelo limite do título ("[t" de "[tel]", "24 h", "preç").

| No título | Todos os orgânicos (709) | Três primeiros (237) |
|---|---|---|
| telefone (mascarado) | 54 (8%) | 20 (8%) |
| "24 horas" ou "24h" | 71 (10%) | 28 (12%) |
| "preço" ou "a partir de" | 30 (4%) | 13 (5%) |
| "melhor" | 27 (4%) | 6 (3%) |
| "orçamento" | 9 (1%) | 2 (1%) |

"24 horas" (10% no conjunto, 12% nos três primeiros), "preço" (4% e 5%) e telefone (7,6% e 8,4%) são um pouco mais
frequentes no topo; "melhor" (4% e 3%) e "orçamento", menos. As diferenças são de poucos resultados: nesta amostra
**não há sinal claro de que esses termos acompanhem posição melhor**. É contagem, não teste.

### 4.4 Diretórios, marketplaces, redes sociais e governo

- **ohub.com.br:** 22 resultados em 21 buscas; posições 1 a 8, mediana 5; páginas de lista por cidade, região ou
  bairro (`/empresas/dedetizacao/sp/sao-paulo/<local>`).
- **Outros sites de lista, orçamento ou reputação:** triider.com.br (2), reclameaqui.com.br (2), coteibem.com.br (1),
  pedegas.com (1), pestwase.com (1), listazn.com.br (1). GetNinjas e Habitissimo, citados na pesquisa de 25/09, **não
  apareceram** na primeira página de nenhuma das 79 buscas.
- **Rede social e fórum:** instagram.com (4), facebook.com (1), reddit.com (1, numa busca de apartamento).
- **Governo e universidade:** 23 resultados, 12 deles nas duas buscas de escorpião; os demais em pombos, morcegos,
  mosquito da dengue, desratização, "controle de pragas", "comprovante vigilância sanitária", escola e certificado. A consulta
  pública de licenças do estado (sivisa.saude.sp.gov.br) apareceu uma vez, na busca do comprovante.

## 5. Bloco de mapa ("Empresas")

- **202 linhas, 64 perfis distintos** nas 68 buscas com bloco. Três perfis respondem por 43% das linhas: ARMOR
  Dedetizadora e Desentupidora (30 buscas; cidade exibida: Osasco), SJG Controle de Pragas Urbanas (29) e Sanitech
  (27). Depois: Primordial Dedetização (10), Lunar Dedetização (8), Heloin Dedetizadora (6).
- **O bloco acompanha o lugar.** Nas buscas sem bairro (grupos A, B, F, G) os mesmos três perfis se repetem — coerente
  com a posição que o Google atribuiu ao navegador (zona oeste, perto de Osasco). Nas 17 buscas por bairro com bloco
  (grupo D) apareceram 37 perfis distintos, e os líderes mudam (Primordial em 5, Heloin e SJG em 3). **Leitura
  (inferência a partir de uma só localização):** quem busca de outro ponto da cidade vê outros perfis nas buscas sem
  bairro; o nome do bairro na busca desloca o bloco para perto do bairro.
- **Cidade exibida na linha do perfil:** São Paulo em 114 linhas, Osasco em 32, Embu das Artes em 1; 55 linhas sem
  cidade visível (endereço oculto ou texto cortado — não distingo).
- **Nota e avaliações:** das 199 linhas em que o script leu nota e número (em outras 2 a nota aparece e o script
  não leu), mediana 5,0, mínima 4,3; 96% com 4,8 ou mais. Por perfil (61 com
  número lido): mediana de 146 avaliações; um quarto tem até 42 e um quarto tem mais de 313; máximo lido, 867 (um
  perfil exibia "1,1 mil", que o script não converteu).
- **"N anos no mercado"** aparece em pelo menos 156 das 202 linhas (58 nos lotes 1 e 2, por extenso; 98 nos lotes 3 a
  7, na forma abreviada pelo script; é piso, porque a linha do perfil foi cortada em 110 ou 80 caracteres), de 3 a
  35 anos.
- **Nome do perfil:** 51 dos 64 nomes trazem palavra de serviço (regra: o nome, sem acento, contém "dedetiz",
  "pragas" ou "cupi"). 12 casam com a regra de local ou "24h" (o nome contém "zona norte/sul/leste/oeste", "24h",
  "são paulo", "sp" como palavra, "vila …", "osasco" ou um dos 20 bairros da coleta); desses, 10 são de fato local
  ou "24h" no nome (por exemplo "… zona norte", "… na Vila Mariana", "… no Butantã", "… 24h SP") e 2 são falso
  positivo da regra (uma empresa que se chama Santana e uma linha em que a cidade do perfil ficou grudada ao nome).
  **Não dá para dizer se o nome é o nome real da empresa:** sem o nome registrado de cada uma não se distingue nome
  legítimo de nome inflado (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção 8).
- **Empresa, diretório ou gerador de leads, no mapa:** as 202 linhas são perfis com nome de empresa (a categoria, quando a
  linha a mostra, é "Dedetizadora"; uma vez, "Serviço de controle de pássaros"); **nenhum diretório ou marketplace
  apareceu no bloco**. Se cada perfil é de quem executa o serviço **não
  foi conferido** (nenhum perfil foi aberto; licença, CNPJ e site de cada um não foram vistos). Dos seis perfis mais
  frequentes, três têm no orgânico um domínio de nome parecido, classificado na seção 7 (a ligação é pelo nome, não
  conferida): Primordial (primordialdedetizacao.com.br, empresa identificada sem número de licença visto), Lunar
  (lunardedetizadora.com.br, empresa com número de licença na página) e Heloin (heloindedetizadora.com.br, empresa
  identificada sem número visto). Sanitech tem um domínio de nome parecido no orgânico
  (sanitechdedetizadora.com.br, 1 resultado), não lido; ARMOR e SJG, os dois perfis mais frequentes, não têm domínio de
  nome parecido entre os 157 do orgânico. O perfil patrocinado tem o nome do anunciante da seção 6 (brasiltechs.com,
  que mostra número de licença na página).
- **O que não foi observado:** endereço visível ou oculto, categoria, horário, data das últimas avaliações, respostas
  do dono, site e telefone de cada perfil (exigiria abrir cada perfil; não feito — "Desdobramentos" no painel).

## 6. Anúncios

- **Anúncio de texto:** 102 anúncios em 60 buscas. Domínios lidos: brasiltechs.com em 58 buscas;
  dedetizacaoexpress24horas.com em 8 anúncios; dedetizamos.com.br em 2; ddteasy.com.br, saonadedetizacao.com.br e
  mgkdedetiza.com.br em 1 cada; 31 anúncios sem domínio identificado.
- **Perfil patrocinado no bloco de mapa:** em 47 buscas, sempre o mesmo ("BRASILTECHS DEDETIZADORA", nota 4,3, 166
  avaliações).
- **Sem anúncio nenhum:** 12 das 79 buscas.
- **Não medido:** custo por clique, posição do anúncio na página, anúncios de outros horários e de outras localizações.
  Nenhum anúncio foi clicado (cobra o anunciante).

## 7. Empresa, diretório ou gerador de leads

### 7.1 Como foi classificado, e o limite

Dois subagentes abriram, pela ferramenta de leitura de página, de 1 a 3 páginas de cada um de **77 domínios** do orgânico
(inicial, uma página que apareceu no resultado e "quem somos", quando havia), em 13/11/2026, entre 21:21 e 21:36. São
os 48 com 3 ou mais aparições (fora governo e rede social, classificados pelo domínio), 18 dos 22 com 2 aparições e
11 com 1 (domínios de bairro, diretórios e anunciantes). Esses 77 domínios cobrem 610 dos 709 resultados (86%). Dados por domínio:
`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` e
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md`; brutos em
`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios_classe_parte1.csv` e `…parte2.csv`; notas com a página e a hora
de cada achado em `/home/ancastelo/pessoal/SEO_Project/docs/mercado/_notas_dominios_parte1.md` e `…parte2.md`.

**Limites:** a ferramenta resume a página por um modelo pequeno; ninguém viu o HTML nem as imagens. **"Não visto" não
prova ausência** (número de licença em imagem, em PDF ou em página não aberta fica de fora). Nenhum número de licença
foi conferido em base oficial; nenhum CNPJ foi consultado; "mesmo dono" não foi provado em caso nenhum — o que há é
mesmo molde, mesma marca, mesmo rodapé ou links cruzados. Os dois subagentes usaram critérios diferentes para a classe
"gerador de leads"; refiz as classes pelo **que cada um registrou ter visto** (regra escrita em
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/junta_classes.py`).

### 7.2 Resultado

| Classe (pelo que foi visto na página) | Domínios | Resultados orgânicos (de 709) | Entre os três primeiros (de 237) | Na 1ª posição (de 79) |
|---|---|---|---|---|
| Empresa identificada (CNPJ, razão social ou endereço), **sem** número de licença visto | 27 | 286 (40%) | 89 (38%) | 18 (23%) |
| Empresa **com** número de licença na página | 11 | 138 (19%) | 70 (30%) | 37 (47%) |
| Marca sem identificação vista (nem CNPJ, nem razão social, nem endereço, nem licença) | 15 | 93 (13%) | 25 (11%) | 9 (11%) |
| Rede declarada ou domínio satélite (domínio de palavra-chave ou de outra marca) | 14 | 51 (7%) | 14 (6%) | 3 (4%) |
| Diretório ou marketplace (ohub.com.br, triider.com.br, pedegas.com) | 3 | 25 (4%) | 5 (2%) | 1 (1%) |
| Governo ou universidade (pelo domínio) | 11 | 23 (3%) | 10 (4%) | 5 (6%) |
| Rede social ou fórum (pelo domínio) | 3 | 6 (1%) | 1 (0%) | 0 |
| Não abriu (rentokil.com, dddrin.com.br, reclameaqui.com.br, ecogama.com.br e dois com "conta suspensa") | 6 | 16 (2%) | 5 (2%) | 2 (3%) |
| Outro (pestwase.com: programa de gestão para dedetizadoras) | 1 | 1 | 0 | 0 |
| Não lido (66 domínios de 1 ou 2 aparições) | 66 | 70 (10%) | 18 (8%) | 4 (5%) |

### 7.3 O que a tabela diz

1. **Quase tudo é site que se apresenta como dedetizadora.** Empresa com ou sem número de licença, marca sem
   identificação e domínio satélite somam 568 dos 709 resultados (80%).
2. **Intermediário declarado, só os diretórios.** ohub.com.br diz reunir empresas e prometer "até 4 propostas
   qualificadas em 24 horas", lista 30 empresas na página de São Paulo e diz que a ordem considera o "volume de
   respostas na plataforma". triider.com.br diz conectar cliente e profissional, com orçamento, contratação e
   pagamento no próprio site. pedegas.com diz ser "plataforma de intermediação de pedidos" e mostra planos para o
   parceiro de R$ 0, R$ 99 e R$ 199 por mês (Brasil, página pública lida em 13/11/2026; classe A sobre ela mesma).
   **Nenhum outro dos 71 sites lidos diz, nas páginas abertas, que repassa pedidos a terceiros;** dois falam em
   "profissionais filiados" e em "franquias" sem dizer como funciona (higitec.com.br, jupitersp.com.br).
3. **Gerador de leads disfarçado não dá para provar; dá para apontar candidatos.** 29 domínios (144 resultados, 20%)
   têm cara de dedetizadora e não mostram quem executa, ou são domínio de palavra-chave de outra marca:
   - seis domínios com o nome exato do bairro (Moema, Mooca, Butantã, Vila Madalena, Higienópolis, Vila Mariana) —
     quatro classificados e dois (Higienópolis e Vila Mariana) abertos só para comparar, que seguem em "não lido" na
     tabela e fora dos 29 — saem do mesmo molde, com a frase "Legalizada pela Vigilância Sanitária e Corpo de Bombeiros" sem número e sem razão
     social, CNPJ ou endereço; o contato é um link de WhatsApp; quem está por trás não foi identificado;
   - uma família de domínios `.eco.br` com páginas `/d/…` geradas em série, com o mesmo desenvolvedor no rodapé,
     ligada à marca de uma empresa que mostra número de licença;
   - pares de marca de uma praga só (cupim e rato) do mesmo molde, sem identificação;
   - os dois anunciantes mais frequentes parecem ser, **pelo rodapé, uma só empresa em dois domínios** (o segundo
     traz outra marca no topo e o nome da primeira no rodapé; não é prova de mesmo dono);
   - uma marca nacional cujos contatos por estado apontam para domínios de outras marcas (rede declarada).
   Quem recebe o WhatsApp desses sites — a própria dedetizadora ou um intermediário — **não sei**; saber exigiria
   contato, que a rodada proíbe.
4. **Número de licença é minoria.** Dos 67 sites de serviço lidos, **12 mostram número de licença** na página (18%);
   pelo menos 14 afirmam ser "licenciada", "legalizada" ou "certificada" **sem número**. Quando há número, o rótulo
   varia ("CEVS", "Licença Sanitária", "SIVISA", "Licença Anvisa", "Alvará nº"). A RDC 622, art. 22, pede que toda
   propaganda de empresa especializada traga a identificação no órgão licenciador e o número da licença
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, seção (b)). **Leitura, com o limite do "não
   visto":** na maior parte das páginas abertas a exigência não aparece cumprida.
5. **Os 11 domínios com número de licença ocupam 47% das primeiras posições** (37 de 79), com 19% dos resultados. Dois
   deles respondem por 28 das 37 (dedetizadora.srv.br, 16; eccocleandedetizacao.com.br, 12). É coincidência observada
   numa amostra, **não prova de que exibir a licença melhore a posição**.
6. **Duas classes são disputáveis**, como dizem as notas da leitura: universoambiental.eco.br está em "empresa com
   número de licença" (o número aparece numa página de preço, não na inicial) sem CNPJ, razão social nem endereço
   vistos, e cupim.eco.br, que mostra o mesmo número, está em "rede ou domínio satélite"; biosolucoes.app.br está em
   "rede ou domínio satélite" embora mostre CNPJ, porque lista "sites parceiros" e outro nome de empresa nos links.
   São 10, 1 e 6 resultados orgânicos (3, 1 e 2 entre os três primeiros), nessa ordem: trocar a classe de qualquer
   um deles desloca esses resultados entre linhas da tabela 7.2.

## 8. Padrões dos primeiros colocados

Cada linha diz de onde vem: "coleta" = `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`; "leitura" = as notas
dos subagentes (seção 7.1), com a página e a hora.

| Padrão | O que se viu | De onde vem |
|---|---|---|
| Site próprio de dedetizadora, com uma página por bairro, região ou cidade | 50 dos 67 sites de serviço lidos têm páginas por localidade; nas buscas com bairro, 79% a 87% dos resultados são dessas páginas | leitura + coleta (seção 4.2) |
| A página de bairro é texto de molde com o nome trocado | Em vários sites sobrou texto de outro lugar: depoimentos de outras cidades na página do Ipiranga; "Morumbi" e "Atibaia" na página de Pinheiros; "Itaquaquecetuba" na página de Itaquera; "zona norte" na página da zona leste; "São Paulo é uma cidade média de São Paulo" | leitura (notas, parte 1 item (b)1 e parte 2 item (b)2, com as páginas) |
| Listas longas de links internos para bairros e palavras-chave | De 80 a cerca de 270 links numa página, em nove sites; cerca de 600 na inicial de outro site (estimativas da ferramenta) | leitura |
| Contato por WhatsApp | 65 dos 67 sites de serviço lidos | leitura |
| "24 horas" | 35 dos 71 sites lidos; em 10% dos títulos (piso); um site diz "24 horas" e "10h às 18h" na mesma página | leitura + coleta (seção 4.3) |
| Dedetizadora e desentupidora na mesma marca | pelo menos 10 dos 34 da parte 1 | leitura |
| Licença afirmada sem número; "Anvisa" quase sempre sobre o produto | seção 7.3, item 4; "produtos aprovados pela Anvisa" em vários | leitura |
| Vocabulário de segurança | "sem cheiro" em pelo menos 7 sites; "100% segura para humanos e animais domésticos", "atóxicos" e "totalmente seguros" em páginas de três domínios; um site diz o contrário ("Nenhum inseticida é atóxico") | leitura |
| Preço à vista é raro | "a partir de R$ 79" e "a partir de 69,90" em títulos; "planos a partir de R$ 150"; os demais dizem "orçamento grátis" (valores lidos nas páginas, Brasil, 13/11/2026; não são preço de mercado) | leitura |
| Agência de SEO no rodapé | pelo menos doze agências creditadas; uma delas se anuncia como de "performance para dedetizadoras" | leitura |
| Selos | selos técnicos de site (W3C, PageSpeed, SSL) usados como "selo da empresa"; logotipos de órgãos; selo do Reclame Aqui; avaliações do Google incorporadas | leitura |
| Perfil no mapa com centenas de avaliações e nota perto de 5 | mediana de 146 avaliações; 96% das linhas com nota 4,8 ou mais | coleta (seção 5) |
| Anúncio | um anunciante em 58 das 79 buscas, com dois domínios | coleta (seção 6) + leitura |

**INFERÊNCIA: o padrão dominante pode encostar no que a política do Google descreve como página de entrada.** Página
por bairro em que só muda o nome do bairro é o sinal que o guia (a) tira do texto da política
(`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 2.2; a aplicação é inferência do guia,
não frase do Google). **A base aqui é fraca:** sobra de texto de outro lugar vista em cerca de dez sites; duas
páginas de bairro do mesmo site não foram comparadas. Páginas por local estão nos primeiros lugares desta amostra
(seção 4.2). Três leituras possíveis, nenhuma provada: (i) as páginas não são o que a política veda (têm conteúdo
próprio suficiente, ou a política não as alcança); (ii) são, e a política não está sendo aplicada a este nicho, ou
não ainda; (iii) são, e o risco pode se materializar numa atualização (havia uma em curso desde 10/11/2026). **Em
nenhuma das três isto autoriza copiar o padrão:** o desenho do projeto não pode depender de prática que a política
lista como spam.

## 9. O que isto diz ao projeto (inferências, marcadas)

1. **O orgânico já está ocupado pelo formato "uma página por bairro".** Um site novo que faça o mesmo entra sem
   diferença nenhuma, contra cerca de 150 domínios, e carregando o risco da política. *(observação + inferência)*
2. **O que quase ninguém mostra é o que a norma pede e o que um intermediário honesto pode oferecer:** quem executa,
   com o número da licença conferido, e como a pessoa confere. Só 12 de 67 sites mostram o número. É **hipótese** de
   diferencial, não medida. Nas buscas em que isso apareceria ("dedetizadora com licença…", "como saber se é
   licenciada"; grupo H, seção 12), algumas dedetizadoras já têm páginas com esses termos (3 de 9 resultados
   numa delas), e a consulta pública do estado aparece em segundo na outra.
3. **Diretório existe e aparece no meio da página** (ohub em 21 de 79 buscas, posição mediana 5). Um comparador novo
   disputaria esse lugar, não o primeiro. *(observação + inferência)*
4. **Preço com fonte é lacuna visível:** quase nenhum site mostra preço; os que mostram usam "a partir de". *(observação;
   se preço com fonte atrai busca, não sei — sem volume medido)*
5. **O mapa é de quem tem perfil com muitas avaliações, perto de quem busca.** Reforça o item 2: o mapa não é ativo do
   projeto; é da licenciada. Para uma parceira, a região da base decide onde ela aparece
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção 6). *(observação de uma só
   localização + guia)*
6. **A página de resultado tem resumo de IA em 92% das buscas;** a posição dele na página não foi registrada. O que
   ele cita aqui, não sei; o desenho tem de
   tratar "ser citável" como parte do orgânico
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, seção 7). *(observação + guia)*
7. **Candidatas a parceira, para o owner olhar (ninguém foi contatado):** os 11 sites que mostram número de licença e
   os perfis que mais aparecem no mapa estão em `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` e na
   seção 5. Antes de qualquer conversa, conferir cada número na consulta pública de licenças do estado, que apareceu
   numa das buscas (sivisa.saude.sp.gov.br). *(lista de trabalho)*
8. **Pista não verificada sobre as licenças:** os números exibidos começam por prefixos diferentes; se o prefixo for
   o código do município emissor, parte das empresas que ranqueiam na capital é licenciada em outro município. Não
   conferi em fonte; fica em "Desdobramentos" no painel.

## 10. Mapa de palavras-chave (`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`)

- **O que tem:** 2.721 termos desde a ampliação de 14/11/2026, 01:08 (fila de reserva 1; ver
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, seção 8). Quando o item 4 foi verificado eram 1.260: as 89 consultas
  da coleta e 1.171 combinações geradas (14 serviços × 26 locais × 3 intenções com local, mais confiança, público e
  21 informativos). Hoje: as 129 consultas das duas coletas (todas feitas) e 2.592 **combinações geradas** por
  `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`: 18 serviços (dedetização, dedetizadora e 16 pragas) × 46 locais (cidade, 5
  regiões, 40 bairros) × 3 intenções com local (contratar, urgência "24 horas", preço), mais termos de confiança
  por local, de público (restaurante, condomínio, apartamento, empresa, escola) por cidade e região, e 21 termos
  informativos sem local.
- **Colunas:** `termo`, `praga`, `tipo_local`, `local`, `intencao`, `publico`, `volume` (sempre "não medido"),
  `origem_do_termo` (consulta da coleta ou combinação gerada), `id_na_coleta`, `situacao_na_coleta` (coletado
  ou não buscado).
- **Por intenção:** contratar 892; urgência 835; preço 833; confiança 140; informativa 21 (no mapa de 1.260 termos
  verificado no item 4, depois das correções: 419; 371; 369; 80; 21).
- **O que o arquivo não é:** lista de termos que as pessoas buscam. É uma grade de hipóteses. Uma combinação gerada
  pode não ter busca nenhuma; termos reais podem faltar (os bairros são só 40 dos distritos da cidade).
- **Como medir o volume depois (nenhum destes foi usado; os dois primeiros exigem a conta do owner; como cada
  ferramenta funciona não foi conferido em fonte nesta rodada):**
  1. **Planejador de palavras-chave do Google Ads** — colar a coluna `termo`, com local "São Paulo" e idioma
     português; registrar a faixa de buscas mensais e a data. Fica pronto para o owner: o arquivo já está no formato
     de uma coluna por termo.
  2. **Search Console**, quando houver site no ar: impressões por consulta são a medida real da demanda que o site já
     alcança (não da demanda total).
  3. **Google Trends** (página pública): só compara termos entre si, em índice de 0 a 100, e não mostra termo de
     pouco volume. Serve para sazonalidade (por exemplo escorpião e mosquito no verão), não para volume.
  4. **Sugestões do próprio Google** (autocompletar, "As pessoas também perguntam", buscas relacionadas): mostram como
     as pessoas escrevem; não foram coletadas ("Desdobramentos" no painel).
- **Coluna a acrescentar quando houver medição:** `volume_faixa`, `fonte_do_volume`, `data_da_medicao`.

## 11. O que não foi feito e o que não sei

- **Lista completa do Google Maps** e dados de cada perfil (endereço, categoria, horário, recência das avaliações).
- **Conteúdo das páginas que ranqueiam:** tamanho, estrutura, dados estruturados, se exibem licença (a classificação
  da seção 7 leu de 1 a 3 páginas por domínio, por ferramenta que resume). A análise de 10 páginas foi feita depois e está em
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`.
- **O que a "Visão geral criada por IA" diz e cita** nessas buscas.
- **Volume de busca, custo por clique, taxa de clique.**
- **Estabilidade:** cinco buscas foram repetidas na mesma noite (seção 13); nenhuma em outro dia, outro lugar,
  deslogado ou no celular.

## 12. Grupo H — confiança, preço e informação (10 buscas, 23:18 a 23:31)

Coletado depois da pausa de duas horas, com o mesmo script, a mesma conta e o mesmo navegador. Os números desta seção
**não entram** nas contas das seções 3 a 9. A classe de cada domínio é a da seção 7 quando ele já tinha aparecido; os
28 domínios novos **não foram lidos** (escrito às 23:41).

### 12.1 O que a página mostra

| Busca | Resumo de IA | Anúncios de texto | Bloco de mapa | Primeiro resultado orgânico |
|---|---|---|---|---|
| H01 dedetizadora confiável são paulo | sim | 5 | 3 perfis + 1 patrocinado | ohub.com.br (diretório) |
| H02 dedetizadora com licença vigilância sanitária sp | sim | 6 | não | heloindedetizadora.com.br (dedetizadora, página de cidade vizinha) |
| H03 como saber se dedetizadora é licenciada | sim | 0 | não | dethetiza.com (não lido; página "como conferir") |
| H04 preço dedetização apartamento sp | sim | 5 | não | dedetizadoranovatec.com.br (página "tabela de preço") |
| H05 tabela de preço dedetização | sim | 5 | não | dedetizadoranovatec.com.br (a mesma página) |
| H06 dedetização vale a pena | sim | 2 | não | imoveis.estadao.com.br (imprensa) |
| H07 como acabar com baratas em apartamento | sim | 0 | não | br.envu.com (não lido; pelo endereço, site de fabricante de produto) |
| H08 dedetização é segura para pets | sim | 1 | não | petlove.com.br (não lido; loja de produtos para animais) |
| H09 quanto tempo dura dedetização | sim | 0 | não | ecoservicos.com.br (dedetizadora, artigo) |
| H10 orçamento dedetização sp | sim | 2 | 3 perfis + 1 patrocinado | dedetizadoranovatec.com.br (a mesma página de preço) |

- Resumo de IA em 10 de 10 (na amostra principal: 73 de 79). Bloco de mapa em 2 de 10 (68 de 79). Anúncio de texto em
  7 de 10 (60 de 79): 26 anúncios, 11 do mesmo anunciante da amostra principal e 8 não identificados.
- O bloco de mapa só apareceu nas duas buscas que juntam cidade e intenção de contratar ("confiável são paulo",
  "orçamento … sp").

### 12.2 Orgânico

- 86 resultados, 60 domínios. **28 domínios (30 resultados, 35%) não tinham aparecido nas 79 buscas anteriores.**
- Tipo de página pelo endereço: página interna de serviço ou outra, 46; blog ou artigo, 20; rede social ou fórum, 8;
  página inicial, 7; governo, 3; página interna por local, 2. Na amostra principal, página interna por local era 45%
  dos resultados (316 de 709); aqui é 2%.
- Por classe (a da seção 7, onde havia; governo e rede social pelo domínio): domínio novo, não lido, 27; empresa
  identificada sem número de licença, 16; empresa com número de licença, 12; rede social ou fórum, 8; diretório ou
  marketplace, 6; rede ou domínio satélite, 6; não classificado, 4; governo, 3; não abriu, 2; marca sem identificação,
  2.
- **Por tipo de busca:**

| Tipo | Buscas | Resultados | O que domina | Anúncios |
|---|---|---|---|---|
| Confiança | H01, H02, H03 | 28 | Dedetizadoras já classificadas (11), domínios novos não lidos (7), governo (3: um documento da prefeitura em 9º em H02; a consulta pública de licenças do estado em 2º e o portal gov.br em 10º em H03) | 11 |
| Preço | H04, H05, H10 | 26 | Dedetizadoras (14) com páginas de "tabela de preço" e "quanto custa"; marketplaces (5: triider nas três, pedegas e ohub em H10) | 12 |
| Informativa | H06 a H09 | 32 | Domínios novos não lidos (16: pelos endereços, imprensa, portal imobiliário, loja, associação de consumidores e blogs de dedetizadoras); rede social e fórum (7) | 3 |

- **dedetizadora.srv.br**, o domínio mais frequente da amostra principal, está em 7 dos 86 resultados e em 6 das 10
  buscas — inclusive com artigos ("evita multas da vigilância sanitária", "tabela de preços médios").
- Em H02 ("dedetizadora com licença vigilância sanitária sp"), 3 dos 9 resultados trazem no título ou no endereço
  "certificada e legalizada", "critérios legais" ou "vigilância sanitária"; 5 são páginas genéricas de dedetizadora e
  1 é documento da prefeitura (títulos cortados em 34 caracteres: piso).

### 12.3 O que isto diz ao projeto (inferências, marcadas; dez buscas não sustentam regra)

1. **Nas buscas de informação há resultado que não é de dedetizadora** (imprensa, loja, governo, fórum). É onde um
   guia de praga ou de "como conferir a licença" disputaria lugar. *(observação de 4 buscas + inferência)*
2. **"Como conferir a licença" já tem resposta oficial em segundo lugar** (a consulta pública do estado) e um site de
   conteúdo em primeiro. Uma página do projeto sobre isso teria de acrescentar algo — o passo a passo, que não foi
   lido — e apontar para a consulta. *(observação de 1 busca)*
3. **Preço é disputado por páginas de "tabela de preço" das próprias dedetizadoras e por marketplaces.** A hipótese
   "preço com origem declarada é lacuna" (seção 9, item 4) fica mais fraca: há oferta de página de preço; o que não
   sei é se os preços têm origem e data. *(observação de 3 buscas; páginas não lidas)*
4. **A premissa de que licença visível atrai busca não sai confirmada:** nas buscas com "licença" e "confiável", o
   resultado é de dedetizadoras e de anúncios (11 anúncios em 3 buscas). *(observação; volume não medido)*

## 13. Repetição de cinco buscas (23:32 a 23:37)

Cinco das 79 buscas foram sorteadas (`shuf` com a semente "repeticao-item4-20261113") e refeitas na mesma noite, de 2
a 3,1 horas depois, no mesmo navegador, logado na mesma conta. Brutos:
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_01.jsonl` (não entram em `serp_sp.csv`).

| Busca | 1ª vez | 2ª vez | Mesmo 1º resultado? | Mesmos três primeiros domínios? | Domínios em comum na página | Perfis do bloco de mapa em comum (de 3) | Local exibido | Anúncios (1ª → 2ª) |
|---|---|---|---|---|---|---|---|---|
| F10 dedetização para bares e lanchonetes sp | 21:10 | 23:32 | sim | sim | 7 de 7 | 3 | São Paulo, SP nas duas | 2 → 2 |
| G01 dedetização urgente são paulo | 21:13 | 23:33 | sim | sim | 8 de 9 | 3 | São Paulo, SP nas duas | 2 → 2 |
| A03 dedetizadora sp | 20:27 | 23:34 | sim | sim | 8 de 9 | 3 | São Paulo, SP nas duas | 2 → 2 |
| B04 dedetização de cupim sp | 20:34 | 23:36 | sim | sim | 9 de 9 | 2 | Osasco, SP nas duas | 2 → 1 |
| D16 dedetização jabaquara | 20:55 | 23:37 | sim | sim | 9 de 9 | 2 | Osasco, SP nas duas | 0 → 2 |

- **O que dá para dizer:** em poucas horas, do mesmo lugar e com a mesma conta, o orgânico da primeira página quase
  não muda e o bloco de mapa muda pouco. Os anúncios variam mais.
- **O que não dá para dizer:** nada sobre outro dia, outro ponto da cidade, outra conta, deslogado ou celular. Cinco
  buscas não medem ruído; só mostram que a coleta não foi um acaso de minuto.

