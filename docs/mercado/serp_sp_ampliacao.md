# Ampliação da amostra de buscas — mais bairros e pragas (fila de reserva, tarefa 1)

- **Estado:** escrito pela sessão principal em sábado, 14/11/2026, à 01:10 (Brasília, lido de `date`). **Não
  verificado.** Complementa `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (item 4, verificado) e não
  muda nenhum número dele.
- **O que é:** 40 buscas novas feitas ao vivo no Google na madrugada de sábado, 14/11/2026, das 00:12 à 01:06 — 20
  bairros que não estavam na primeira amostra, 10 combinações de praga com esses bairros e 10 pragas ou serviços novos
  com a cidade — e a ampliação do mapa de palavras-chave de 1.260 para 2.721 termos. **Amostra declarada, não censo;
  não é posição média; não é volume de busca.**
- **Novidade de método:** o coletor passou a registrar a **posição vertical** de cada camada da página (resumo de IA,
  primeiro anúncio de texto, bloco de mapa, primeiro resultado orgânico), que o item 4 deixou como "não registrada".
- **Arquivos:**
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv` — as 40 consultas (grupos I, J e K).
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv` — 537 linhas, uma por resultado visto (352
    orgânicos, 93 perfis no bloco de mapa, 25 perfis patrocinados, 67 anúncios de texto), com as mesmas colunas de
    `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`.
  - `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md` — o registro de cada busca
    (termo, hora, conta logada, localização exibida, ordem das camadas e posição em pixels).
  - Brutos e scripts: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/ampliacao_01.jsonl` a `ampliacao_04.jsonl`, as repetições em
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl`,
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` (função `fx2`) e
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`.
  - `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` — o mapa ampliado (seção 8).
- **Fonte de todo número deste arquivo**, salvo indicação: os arquivos acima (Brasil, cidade de São Paulo,
  14/11/2026). Para refazer as contas: `python3 /home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`.
  "Amostra principal" = as 79 buscas dos grupos A a G do item 4 (13/11/2026, 20:26 a 21:16).

## 1. Em uma página

1. **Os 20 bairros novos repetem o padrão dos 20 primeiros.** Nas 20 buscas "dedetizadora/dedetização + bairro"
   (grupo I), 88% dos 179 resultados orgânicos são páginas internas com o nome do local no endereço (87% no grupo D
   da amostra principal), e em 17 das 20 os três primeiros são todos desse tipo.
2. **Poucos sites cobrem quase todos os bairros.** protecpragas.com.br aparece em 17 das 20 buscas de bairro novo,
   primordialdedetizacao.com.br em 14 e lunardedetizadora.com.br em 13; os dois primeiros lugares mais frequentes são
   protecpragas.com.br (8 de 20) e lunardedetizadora.com.br (7 de 20). Dos 66 domínios do grupo I, 39 já tinham
   aparecido nas buscas de bairro da amostra principal.
3. **Praga nova com a cidade (grupo K) mostra outra página:** 72% dos 85 resultados são páginas internas de serviço,
   2% são páginas por local; governo aparece em 5 das 10 buscas e é o primeiro resultado em 3 (mosquitos, ratos,
   fumacê para condomínio); o bloco de mapa só aparece em 5 de 10.
4. **Ordem na página (40 buscas, janela de computador com 945 pixels de altura):** o resumo de IA é a primeira
   camada em 38 das 39 buscas em que apareceu; o bloco de mapa vem antes do primeiro orgânico em 21 das 31 buscas
   com bloco; o primeiro anúncio de texto vem **depois** do primeiro orgânico em 34 das 35 buscas com anúncio. O
   primeiro resultado orgânico fica abaixo da primeira tela em 23 das 40 buscas (17 das 20 no grupo I).
5. **A coincidência "licença exibida × primeira posição" do item 4 não se repete com a mesma força.** Pela classe
   dada no item 4, as 40 primeiras posições se dividem em: marca sem identificação vista, 11; empresa com número de
   licença na página, 11; empresa identificada sem número visto, 10; governo, 3; domínio novo não lido, 3; outros, 2. Na amostra
   principal eram 37 de 79 para os sites com número de licença.
6. **O mesmo anunciante segue dominante:** anúncio de texto dele em 33 das 40 buscas e perfil patrocinado em 25.
7. **46 domínios novos** (55 resultados, 16%) não tinham aparecido nas 89 buscas do item 4; **não foram lidos**. Nas
   129 buscas das duas coletas há 231 domínios distintos no orgânico e 96 perfis distintos no bloco de mapa.
8. **Sem verificação de robô.** Intervalo entre buscas de 72 a 190 segundos (mediana 77). Cinco buscas repetidas de
   31 a 60 minutos depois deram o mesmo orgânico, na mesma ordem, e os mesmos perfis no bloco (seção 11). Total
   gasto do limite de 600 na rodada: cerca de 155 (110 do item 4, 40 desta ampliação e 5 repetições).

## 2. Método

### 2.1 O que foi buscado

| Grupo | O que é | Buscas |
|---|---|---|
| I | bairro novo: Brooklin, Morumbi, Saúde, Campo Belo, Interlagos, Capão Redondo (sul); Vila Prudente, São Miguel Paulista, Sapopemba, Guaianases (leste); Tucuruvi, Pirituba, Freguesia do Ó, Casa Verde, Vila Maria (norte); Vila Leopoldina, Jaguaré (oeste); Liberdade, Consolação, Aclimação (centro) | 20 |
| J | praga × bairro novo ("desratização tucuruvi", "descupinização morumbi"…) | 10 |
| K | praga ou serviço que não estava na primeira amostra + cidade (traças, mosquitos, marimbondos, moscas, lacraias, "controle de ratos", cupim de solo, broca de madeira, fumacê para condomínio, piolho de pombo) | 10 |
| | **Total** | **40** |

Os termos foram escolhidos por mim; **são plausíveis, não os mais buscados** (não há volume medido). Os bairros foram
escolhidos para cobrir as cinco regiões; a divisão por região é minha.

### 2.2 Como foi buscado

- Igual ao item 4: busca web do Google pelo endereço (`…/search?q=<termo>&hl=pt-BR&gl=br&pws=0`), navegador pessoal do
  owner (Chrome, computador), aba aberta pela sessão e fechada à 01:07 (as repetições usaram outra aba, fechada à 01:18); **logado** na conta Google do owner nas 40;
  nada foi clicado.
- **Quando:** sábado, 14/11/2026, das 00:12:10 à 01:06:01 — madrugada. Hora de cada busca lida do relógio da página.
- **Intervalo entre buscas:** mínimo 72 segundos, mediana 77, máximo 190; nenhum abaixo de 20 segundos. **Não houve
  verificação de robô.**
- **Localização que o Google mostrou:** "São Paulo, SP" em 5 buscas, "Osasco, SP" em 5, nenhuma em 30.
- **Posição vertical:** para cada busca, a distância em pixels do topo da página até o rótulo "Visão geral criada por
  IA", até o primeiro anúncio de texto, até o título do bloco "Empresas" e até o primeiro título de resultado
  orgânico. A janela tinha 945 pixels de altura: "primeira tela" = posição menor que 945.
- **Dados de terceiros:** telefones mascarados como `[tel]`. Um telefone de empresa escrito no caminho de um endereço
  (lote 1) foi mascarado ao gravar e não entrou no repositório; da 11ª busca em diante o coletor mascara também o
  caminho. De cinco publicações de rede social que apareceram no orgânico (grupo de bairro, perfis e páginas), o
  identificador foi omitido ao gravar; em três delas, também o título.

### 2.3 Limites (ler antes de usar qualquer número)

1. **Um ponto, uma hora, uma conta — e outra hora que a do item 4.** Madrugada de sábado, do mesmo lugar (zona oeste
   da Grande São Paulo), logado. O bloco de mapa e os anúncios dependem da hora (empresa aberta, orçamento do
   anunciante): **a ordem e a quantidade de anúncios vistas aqui não valem para o horário comercial.**
2. **Uma busca por termo, só a primeira página.**
3. **A posição vertical é de uma janela de computador.** No celular a página é outra. A altura do resumo de IA não
   foi medida (só onde começa); se estava aberto ou recolhido, não sei.
4. **"Primeiro anúncio de texto" = o primeiro elemento que a página marca como anúncio de texto.** Outros formatos de
   anúncio, se houve, não foram lidos. Em 28 dos 67 anúncios o domínio não foi identificado.
5. **Tipo de página pelo endereço**, como no item 4; a lista de locais do script ganhou os 20 bairros novos. Páginas
   não lidas: **não afirmo que sejam "páginas de entrada"**.
6. **Classe dos domínios:** a do item 4, onde havia. Os 46 domínios novos não foram lidos nem classificados.
7. **Consulta automática:** vale o que está no item 4, seção 2.3, item 9 — é prática que a política do Google veda; a
   decisão de manter o limite da rodada está na fila do owner.

## 3. O que a página mostra, por grupo

| Grupo | Buscas | Visão geral criada por IA | Bloco "Empresas" | Anúncio de texto | Perfil patrocinado no bloco | Sem anúncio nenhum |
|---|---|---|---|---|---|---|
| I bairro novo | 20 | 19 | 18 | 19 | 15 | 1 |
| J praga × bairro novo | 10 | 10 | 8 | 8 | 7 | 1 |
| K praga ou serviço novo + cidade | 10 | 10 | 5 | 8 | 3 | 2 |
| **Total** | **40** | **39 (98%)** | **31 (78%)** | **35 (88%)** | **25 (63%)** | **4** |
| *Amostra principal (item 4)* | *79* | *73 (92%)* | *68 (86%)* | *60 (76%)* | *47 (59%)* | *12* |

- Sem resumo de IA: só "dedetizadora freguesia do ó". Sem bloco de mapa (9): Guaianases e Pirituba (grupo I);
  percevejo na Liberdade e escorpião em Pirituba (J); marimbondos, lacraias, broca de madeira, fumacê para condomínio
  e piolho de pombo (K).
- As duas amostras foram feitas em horas diferentes; a diferença nos percentuais **não** mede efeito de bairro novo.

## 4. Ordem na página (o que o item 4 não tinha)

| Ordem, de cima para baixo | Buscas (de 40) |
|---|---|
| IA > mapa > orgânico > anúncio | 19 |
| IA > orgânico > mapa > anúncio | 8 |
| IA > orgânico > anúncio (sem mapa) | 6 |
| IA > orgânico (sem mapa e sem anúncio) | 3 |
| anúncio > IA > mapa > orgânico | 1 |
| mapa > orgânico (sem IA e sem anúncio) | 1 |
| IA > orgânico > mapa (sem anúncio) | 1 |
| IA > orgânico > anúncio > mapa | 1 |

| Camada | Buscas em que aparece | Posição mediana (pixels do topo) | Mínima e máxima | Começa na primeira tela |
|---|---|---|---|---|
| Rótulo do resumo de IA | 39 | 250 | 172 a 924 | 39 de 39 |
| Título do bloco "Empresas" | 31 | 666 | 254 a 2.643 | 22 de 31 |
| Primeiro resultado orgânico | 40 | 1.558 | 626 a 2.758 | 17 de 40 |
| Primeiro anúncio de texto | 35 | 2.314 | 321 a 4.470 | 1 de 35 |

- **Por grupo:** nas buscas de bairro (I), a ordem "IA > mapa > orgânico > anúncio" aparece em 15 de 20 e o primeiro
  orgânico fica abaixo da primeira tela em 17 de 20 (abaixo de duas telas em 4). Nas de praga nova com cidade (K), o
  orgânico vem antes do mapa em 4 das 5 buscas com bloco e começa na primeira tela em 8 de 10.
- **O que isto responde:** a premissa do guia (a) e do desenho, de que mapa e anúncios ficam acima do orgânico, vale
  **em parte** nesta amostra: o resumo de IA e, nas buscas de bairro, o bloco de mapa vêm antes do orgânico; os
  anúncios de texto, nesta hora, vieram quase sempre no fim da página. *(observação de 40 buscas numa madrugada; não
  vale para o horário comercial — limite 1)*

## 5. Resultado orgânico

### 5.1 Tipo de página (pelo endereço), em % dos resultados de cada grupo

| Grupo | Página interna por local | Página interna de serviço ou outra | Página inicial | Blog ou artigo | Governo ou universidade | Rede social ou fórum |
|---|---|---|---|---|---|---|
| I bairro novo (179) | 88 | 4 | 5 | 2 | 0 | 2 |
| J praga × bairro novo (88) | 66 | 27 | 1 | 1 | 1 | 3 |
| K praga ou serviço novo + cidade (85) | 2 | 72 | 5 | 9 | 9 | 2 |
| *D bairro, amostra principal (181)* | *87* | *2* | *7* | *2* | *0* | *2* |
| *E praga × bairro, amostra principal (107)* | *79* | *10* | *1* | *2* | *7* | *1* |
| *B praga + cidade, amostra principal (116)* | *4* | *69* | *8* | *9* | *9* | *1* |

- Nos três primeiros lugares das 40 buscas (120 resultados): 78 páginas internas por local, 31 de serviço, 5
  iniciais, 5 de governo, 1 de blog. Em 21 das 30 buscas com bairro (I e J), os três primeiros são todos páginas por
  local (17 de 20 em I; 4 de 10 em J).
- **Domínio com o nome exato do bairro** aparece em 5 das 20 buscas de bairro novo (Brooklin, Saúde, Vila Prudente,
  Tucuruvi, Vila Maria), uma vez em primeiro lugar (Saúde) — não lidos.

### 5.2 Concentração e domínios

- 352 resultados, 119 domínios. Os mais frequentes (resultados · vezes entre os três primeiros): protecpragas.com.br
  (22 · 17), primordialdedetizacao.com.br (18 · 6), lunardedetizadora.com.br (16 · 10), dedetizadora.srv.br (14 · 4),
  hidrosampa.com.br (13 · 1), spdedetizadora.com.br (10 · 3), keikodedetizadora.com.br (8 · 8), uniprag.com.br (8 ·
  2), biosp.com.br (8 · 5), dedetizadoraddpilar.com.br (8 · 1).
- **Primeira posição (40 buscas):** protecpragas.com.br, 11; lunardedetizadora.com.br, 8; keikodedetizadora.com.br e
  zet-tecdedetizadora.com.br, 3 cada; ecoservicos.com.br, biosp.com.br e sp156.prefeitura.sp.gov.br, 2 cada.
- **Nas 20 buscas de bairro novo, onze domínios aparecem em 5 ou mais:** protecpragas.com.br (17),
  primordialdedetizacao.com.br (14), lunardedetizadora.com.br (13), spdedetizadora.com.br e dedetizadora.srv.br (8
  cada), hidrosampa.com.br (6), ohub.com.br, deltadedetizacao.com.br, dedetizadorasamurai.com.br,
  dedetizadoraddpilar.com.br e ambientalepragas.com.br (5 cada). Oito deles estão entre os treze que apareciam em 5 ou
  mais das 20 buscas de bairro da amostra principal.
- **Os dez domínios mais frequentes da amostra principal** aparecem todos aqui (de 5 a 22 resultados cada). No grupo
  K, o mais frequente é uniprag.com.br (6), com artigos de blog.
- **Domínios novos:** 46 de 119 (55 resultados, 16%); no grupo K são 21 de 54 (28% dos resultados). Entre eles,
  três de governo (`sp156.prefeitura.sp.gov.br`, `servicos.sp.gov.br`, `agricultura.sp.gov.br`), um portal de
  síndicos, uma página de consulta de empresas e sites de uma praga só (cupim, abelhas, piolho de pombo) — pelo
  endereço; não lidos.
- **Governo:** 9 resultados em 6 buscas — escorpião em Pirituba (3º), mosquitos (1º, 5º e 6º), marimbondos (2º),
  ratos (1º e 6º), broca de madeira (8º) e fumacê para condomínio (1º). Reforça, com mais quatro pragas, o que o item
  4 viu nas duas buscas de escorpião. *(observação; 10 buscas não sustentam regra)*

### 5.3 Classe (a do item 4, onde havia)

| Classe | Resultados (de 352) | Entre os três primeiros (de 120) | Na 1ª posição (de 40) |
|---|---|---|---|
| Empresa identificada, sem número de licença visto | 122 | 38 | 10 |
| Marca sem identificação vista | 49 | 26 | 11 |
| Empresa com número de licença na página | 48 | 20 | 11 |
| Domínio novo, não lido (fora governo e rede social) | 51 | 13 | 3 |
| Não lido no item 4 | 32 | 7 | 1 |
| Rede ou domínio satélite | 23 | 7 | 1 |
| Governo (pelo domínio) | 9 | 5 | 3 |
| Rede social, diretório, não abriu | 18 | 4 | 0 |

- **Leitura (observação, com os limites do item 4, seção 7.1):** nas buscas de bairro novo, as duas marcas que mais
  ocupam o primeiro lugar são uma "marca sem identificação vista" e uma "empresa com número de licença". A fatia das
  primeiras posições com sites que mostram número de licença cai de 47% (37 de 79, amostra principal) para 28% (11 de
  40) — o que enfraquece ainda mais a leitura de que exibir a licença acompanhe posição. A classe "sem identificação
  vista" depende de 1 a 3 páginas lidas por ferramenta que resume: **"não visto" não prova ausência.**
- Diretório: ohub.com.br em 5 das 20 buscas de bairro novo e em nenhuma das de praga; nenhum outro marketplace.

## 6. Bloco de mapa

- 93 linhas, 60 perfis distintos nas 31 buscas com bloco; **32 perfis não tinham aparecido na amostra principal**.
  Mais frequentes: SJG Controle de Pragas Urbanas (9), Sanitech (5), Primordial Dedetização (4).
- **Nas 18 buscas de bairro novo com bloco: 45 perfis distintos em 54 linhas** — só 12 deles tinham aparecido nas
  buscas de bairro da amostra principal. O bloco muda de bairro para bairro mais do que o orgânico. *(observação de
  uma só localização)*
- Nota: mediana 5,0, mínima 4,0; 92% das 92 linhas com nota lida têm 4,8 ou mais. Avaliações por perfil (59 lidos):
  mediana 82 (146 na amostra principal), de 1 a 867 — os perfis dos bairros novos têm menos avaliações.
- Nenhum diretório no bloco; perfis não foram abertos (vale o que diz o item 4, seção 5).

## 7. Anúncios

- Anúncio de texto: 67 em 35 buscas; brasiltechs.com em 33 buscas (34 anúncios); dedetizacaoexpress24horas.com, 3;
  dmetros.com.br e fortvenenodedetizadora.com.br, 1 cada; 28 sem domínio identificado.
- Perfil patrocinado no bloco: o mesmo do item 4, em 25 buscas.
- Posição: seção 4. Nenhum anúncio foi clicado. Custo por clique: não medido.

## 8. Mapa de palavras-chave ampliado (`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`)

- **De 1.260 para 2.721 termos.** As 129 consultas das duas coletas (todas feitas) e 2.592 combinações geradas por
  `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`: 18 serviços (dedetização, dedetizadora e 16
  pragas — entraram moscas, lacraias, marimbondos e brocas de madeira) × 46 locais (cidade, 5 regiões, 40 bairros) ×
  3 intenções com local, mais termos de confiança por local, de público por cidade e região e 21 informativos sem
  local.
- **Por intenção:** contratar 892; urgência 835; preço 833; confiança 140; informativa 21. **Por tipo de local:**
  bairro 2.289; região 315; cidade 92; sem local 25.
- **Volume: "não medido" em todas as linhas.** Continua sendo uma grade de hipóteses, não uma lista do que as pessoas
  buscam. Quatro dos bairros novos têm nome que é também palavra comum (Saúde, Liberdade, Consolação, Aclimação): uma
  combinação como "dedetização saúde" pode não ser lida como bairro — a própria coleta usou "sp" em duas delas.
- O método para medir volume segue o do item 4, seção 10 (Planejador de palavras-chave, na conta do owner).
- **Efeito em outros arquivos:** as contagens do mapa citadas no item 4 (seção 10) e no plano de conteúdo foram
  refeitas na mesma data (ver cada arquivo).

## 9. O que isto diz ao projeto (inferências, marcadas)

1. **A observação central do item 4 se sustenta em mais 20 bairros:** busca com bairro traz página do bairro, de
   poucos sites que têm página para quase todo bairro. *(observação; 40 bairros num total de duas noites)*
2. **Para o desenho, que não faz página por bairro, a porta continua sendo outra:** nas buscas de praga com a cidade
   (grupo K e grupo B), o orgânico é de páginas de serviço e de governo, e começa mais perto do topo. *(observação +
   inferência; sem volume medido não sei se há busca que compense)*
3. **A página de resultado, no computador, abre com o resumo de IA.** "Ser citável" pesa mais do que o item 4
   conseguia dizer; o que o resumo cita continua sem registro. *(observação de 40 buscas + inferência)*
4. **A hipótese de que mostrar a licença é diferencial segue sem apoio na posição:** os primeiros lugares dos bairros
   novos se dividem entre sites com e sem número de licença visto. O argumento do desenho para exibir a licença é a
   norma (RDC 622, art. 22), não a posição. *(observação)*
5. **Candidatas a parceira:** os perfis de bairro novo estão em
   `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`; ninguém foi contatado. *(lista de trabalho)*

## 10. O que não foi feito

- Lista completa do Google Maps e dados de cada perfil; o que o resumo de IA diz e cita (ficam em "Desdobramentos" no
  painel — não fazem parte desta tarefa).
- Leitura e classificação dos 46 domínios novos.
- Repetição em horário comercial, em outro dia, deslogado ou no celular.
- Volume de busca de qualquer termo.

## 11. Repetição de cinco buscas (01:12 a 01:17)

Cinco das 40 buscas foram sorteadas (`shuf -n 5` sobre os 40 ids, fonte aleatória `openssl enc -aes-256-ctr` com a
senha "repeticao-reserva1-20261114") e refeitas na mesma madrugada, no mesmo navegador, logado na mesma conta, com 73
a 77 segundos entre uma e outra. Brutos: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl` (não entram em
`serp_sp_ampliacao.csv`).

| Busca | 1ª vez | 2ª vez | Mesmo 1º resultado? | Mesma ordem dos 9 domínios? | Perfis do bloco em comum (de 3) | Local exibido | Anúncios de texto (1ª → 2ª) | 1º orgânico (px, 1ª → 2ª) |
|---|---|---|---|---|---|---|---|---|
| J01 dedetização de baratas brooklin | 00:41 | 01:12 | sim | sim | 3 | nenhum nas duas | 2 → 1 | 704 → 704 |
| I08 dedetização são miguel paulista | 00:21 | 01:14 | sim | sim | 3 | nenhum nas duas | 2 → 2 | 1.654 → 1.654 |
| I20 dedetização aclimação | 00:39 | 01:15 | sim | sim | 3 | nenhum nas duas | 2 → 2 | 1.682 → 1.682 |
| I04 dedetização campo belo | 00:16 | 01:16 | sim | sim | 3 | Osasco, SP nas duas | 2 → 1 | 1.490 → 1.490 |
| I14 dedetização casa verde | 00:31 | 01:17 | sim | sim | 3 | Osasco, SP nas duas | 2 → 2 | 2.758 → 1.653 |

- **O que dá para dizer:** em até uma hora, do mesmo lugar e com a mesma conta, o orgânico e o bloco de mapa não
  mudaram. A posição vertical mudou numa das cinco (Casa Verde: o bloco de mapa e o primeiro orgânico começaram cerca
  de 1.100 pixels mais acima na segunda vez), o que mostra que a medida da seção 4 **varia de uma carga da página para
  outra**; o número de anúncios variou em duas.
- **O que não dá para dizer:** nada sobre outro dia, outro horário, outro ponto da cidade, outra conta ou celular.
