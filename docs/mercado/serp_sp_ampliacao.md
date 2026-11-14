# Ampliação da amostra de buscas — mais bairros e pragas (fila de reserva, tarefa 1)

- **Estado:** escrito pela sessão principal em sábado, 14/11/2026, à 01:10 (Brasília, lido de `date`); a seção 11 é
  da 01:18. Conferido por verificador independente
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva1.md`: aprovado com ressalvas; 0 falha em 12 no sorteio;
  21 correções pedidas, de leitura e não de conta). As 21 foram aplicadas pela sessão principal à 01:38, sem nova
  leitura. **Segunda passada:** um revisor novo, em contexto limpo, releu tudo em 14/11/2026, das 02:01 às 02:14
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva1.md`: aprovado com ressalvas;
  0 falha em 12 no sorteio; 14 achados). Os 14 foram conferidos nos dados e aplicados por um corretor em 14/11/2026
  às 02:30 (Brasília, lido de `date`; relato em
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes2_reserva1.md`), **sem nova leitura depois
  da correção**. O que mudou: dois números (perfis distintos nas duas coletas, 96 → 95; perfis que não estavam na
  amostra principal, 32 → 31), uma afirmação que era falsa (caminhos cortados entre os três primeiros: limite 5 e
  seção 5.1) e redação (classe de evidência declarada; hipóteses marcadas; registro das repetições na seção 11). O
  CSV e o registro **não** foram regravados: duas correções dependem de troca no script e estão descritas no relato.
  Complementa `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (item 4, verificado) e não muda nenhum
  número dele.
- **O que é:** 40 buscas novas feitas ao vivo no Google na madrugada de sábado, 14/11/2026, das 00:12 à 01:06 — 20
  bairros que não estavam na primeira amostra, 10 combinações de praga com esses bairros e 10 pragas ou serviços novos
  com a cidade — e a ampliação do mapa de palavras-chave de 1.260 para 2.721 termos. **Amostra declarada, não censo;
  não é posição média; não é volume de busca.**
- **Novidade de método:** o coletor passou a registrar a **posição vertical** de cada camada da página (resumo de IA,
  primeiro anúncio de texto, bloco de mapa, primeiro resultado orgânico), que o item 4 deixou como "não registrada".
- **Arquivos:**
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv` — as 40 consultas (grupos I, J e K).
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv` — 537 linhas, uma por resultado visto (352
    orgânicos, 93 linhas de perfil no bloco de mapa, 25 linhas de perfil patrocinado — um único perfil —, 67 anúncios
    de texto), com as mesmas colunas de `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`.
  - `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md` — o registro de cada uma das 40
    buscas (termo, hora, conta logada, localização exibida, ordem das camadas e posição em pixels). As 5 repetições
    não estão nesse arquivo, que é gerado por script só a partir dos lotes das 40: o registro delas, com os mesmos
    campos e a hora em segundos, está na seção 11 deste documento.
  - Brutos e scripts: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/ampliacao_01.jsonl` a `ampliacao_04.jsonl`, as repetições em
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl`,
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` (função `fx2`) e
    `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`.
  - `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` — o mapa ampliado (seção 8).
- **Fonte de todo número deste arquivo**, salvo indicação: os arquivos acima (Brasil, cidade de São Paulo,
  14/11/2026). Para refazer as contas: `python3 /home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`
  (atenção: esse script regrava o CSV e o registro). As contas da segunda passada, só de leitura, estão em
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/corr2res1_contas.py`.
  "Amostra principal" = as 79 buscas dos grupos A a G do item 4 (13/11/2026, 20:26 a 21:16).
- **Classe de evidência desta coleta** (regra de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`):
  **B — dado próprio, com amostra, método e bruto expostos**, que dá para conferir nos arquivos acima. O limite da
  amostra acompanha todo número: 40 buscas numa madrugada (sábado, 14/11/2026, 00:12 à 01:06), uma conta logada, um
  ponto de acesso, uma busca por termo, só a primeira página, coleta por script (seção 2.3). A segunda
  verificação conferiu arquivo contra arquivo, sem repetir busca ao vivo; as cinco repetições da seção 11 foram
  feitas por quem coletou. Os números são **observação desta amostra, não regra**; as leituras da seção 9 são inferência, marcadas uma a uma; a classe de cada domínio vem do
  item 4. Quem ganha com a afirmação: ninguém vende nada aqui, mas quem coletou é o próprio projeto, que também
  escolheu os termos (seção 2.1).

## 1. Em uma página

1. **Os 20 bairros novos repetem o padrão dos 20 primeiros.** Nas 20 buscas "dedetizadora/dedetização + bairro"
   (grupo I), 88% dos 179 resultados orgânicos são páginas internas com o nome do local no endereço (87% no grupo D
   da amostra principal), e em 17 das 20 os três primeiros são todos desse tipo.
2. **Três sites aparecem em 13 a 17 das 20 buscas de bairro novo.** protecpragas.com.br aparece em 17 das 20 buscas de bairro novo,
   primordialdedetizacao.com.br em 14 e lunardedetizadora.com.br em 13; os dois primeiros lugares mais frequentes são
   protecpragas.com.br (8 de 20) e lunardedetizadora.com.br (7 de 20). Dos 66 domínios do grupo I, 39 já tinham
   aparecido nas buscas de bairro da amostra principal.
3. **Praga ou serviço novo com a cidade (grupo K) mostra outra página:** 72% dos 85 resultados são páginas internas de serviço,
   2% são páginas por local; governo aparece em 5 das 10 buscas e é o primeiro resultado em 3 (mosquitos, ratos,
   fumacê para condomínio); o bloco de mapa só aparece em 5 de 10.
4. **Ordem na página (40 buscas, janela de computador com 945 pixels de altura):** o resumo de IA é a primeira
   camada em 38 das 39 buscas em que apareceu; o bloco de mapa vem antes do primeiro orgânico em 21 das 31 buscas
   com bloco; o primeiro anúncio de texto vem **depois** do primeiro orgânico em 34 das 35 buscas com anúncio. O
   primeiro resultado orgânico fica abaixo da primeira tela em 23 das 40 buscas (17 das 20 no grupo I). Uma medida
   por busca, de quatro marcadores; variou em duas das cinco repetições (seção 11).
5. **A coincidência "licença exibida × primeira posição" fica parecida nas buscas de bairro e, nas de praga nova com
   a cidade, ficou em 1 de 10 — que é piso.** Pela classe dada no item 4, as 40 primeiras posições se dividem em:
   marca sem identificação vista, 11; empresa com número de licença na página, 11; empresa identificada sem número
   visto, 10; governo, 3; domínio novo não lido, 3; outros, 2. Sites com número de licença na primeira posição:
   bairro, 8 de 20 (7 de 20 no grupo D do item 4) — sete das oito são de um mesmo site, lunardedetizadora.com.br (no
   grupo D, as sete eram de três sites); praga × bairro, 2 de 10 (2 de 12 no grupo E); praga ou serviço novo com a
   cidade, 1 de 10 (7 de 13 no grupo B) — piso, porque das 10 primeiras posições do grupo K 3 são de governo e 2 de
   domínio novo não lido, e as pragas do grupo K não são as do grupo B. O total do item 4 (37 de 79) inclui grupos
   sem par aqui (A, C, F e G: 21 de 34) e não se compara com 11 de 40.
6. **O mesmo anunciante segue dominante:** anúncio de texto dele em 33 das 40 buscas e perfil patrocinado em 25.
7. **46 domínios novos** (55 resultados, 16%) não tinham aparecido nas 89 buscas do item 4; **não foram lidos**. Nas
   129 buscas das duas coletas há 231 domínios distintos no orgânico e 95 perfis distintos no bloco de mapa (pelo
   nome; até 14/11/2026, 02:38, a coluna de nome do CSV dava 96, porque um perfil ficava com a nota grudada no nome — seção 6).
8. **Sem verificação de robô** (relato de quem coletou, a sessão principal; os 40 identificadores estão nos brutos, na ordem)**.** Intervalo entre buscas de 72 a 190 segundos (mediana 77). Cinco buscas repetidas de
   31 a 60 minutos depois deram o mesmo orgânico, na mesma ordem, e os mesmos perfis no bloco (seção 11). Total
   gasto do limite de 600 na rodada: cerca de 155 (110 do item 4, 40 desta ampliação e 5 repetições). Dessas, 139
   têm registro bruto (89 buscas e 5 repetições do item 4; 40 e 5 daqui); as outras cerca de 16, do item 4 (1
   barrada e cerca de 15 perdidas em testes, segundo
   `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`), não têm bruto e não dá para conferi-las.

## 2. Método

### 2.1 O que foi buscado

| Grupo | O que é | Buscas |
|---|---|---|
| I | bairro novo: Brooklin, Morumbi, Saúde, Campo Belo, Interlagos, Capão Redondo (sul); Vila Prudente, São Miguel Paulista, Sapopemba, Guaianases (leste); Tucuruvi, Pirituba, Freguesia do Ó, Casa Verde, Vila Maria (norte); Vila Leopoldina, Jaguaré (oeste); Liberdade, Consolação, Aclimação (centro) | 20 |
| J | praga × bairro novo ("desratização tucuruvi", "descupinização morumbi"…) | 10 |
| K | praga ou serviço que não estava na primeira amostra + cidade (traças, mosquitos, marimbondos, moscas, lacraias, "controle de ratos", cupim de solo, broca de madeira, fumacê para condomínio, piolho de pombo) — seis são pragas que não estavam na primeira coleta (traças, marimbondos, moscas, lacraias, broca de madeira, piolho de pombo) e quatro são termo ou serviço novo de praga já buscada (mosquitos, ratos, cupim de solo, fumacê) | 10 |
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
   da Grande São Paulo), logado. O bloco de mapa pode depender da hora: num estudo de 2023 (Estados Unidos, classe B,
   "pode estar desatualizada"; confirmação do Google lida de segunda mão), estar aberto na hora da busca esteve
   associado a posição melhor — `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção
   4.3, linha "Horário ('aberto agora')"; a seção 6 do mesmo guia trata da distância entre quem busca e a base da
   empresa. Que os anúncios também mudem com a hora (por exemplo, pelo orçamento do anunciante) é **hipótese minha,
   sem fonte neste projeto**. Nada disso foi medido aqui: **a ordem e a quantidade de anúncios e de perfis vistas
   nesta madrugada não podem ser estendidas ao horário comercial.**
2. **Uma busca por termo, só a primeira página.**
3. **A posição vertical é de uma janela de computador.** No celular a página é outra. A altura do resumo de IA não
   foi medida (só onde começa); se estava aberto ou recolhido, não sei. Cada posição foi medida uma vez, de 11 a 17
   segundos depois da navegação, e não diz se o elemento estava visível nem o que há entre uma camada e outra. Em
   cinco buscas repetidas, bloco e orgânico mudaram cerca de 1.100 pixels em uma e o primeiro anúncio mais de 1.000
   em duas (seção 11): as ordens e as medianas se mantêm; os extremos e as contagens "na primeira tela" têm folga de
   pelo menos uma busca. "Ordem na página" é a ordem de quatro marcadores, não de tudo o que a página mostra.
4. **"Primeiro anúncio de texto" = o primeiro elemento que a página marca como anúncio de texto.** Outros formatos de
   anúncio, se houve, não foram lidos. Em 28 dos 67 anúncios o domínio não foi identificado.
5. **Tipo de página pelo endereço**, como no item 4; a lista de locais do script ganhou os 20 bairros novos. Páginas
   não lidas: **não afirmo que sejam "páginas de entrada"**. A regra erra para os dois lados: uma notícia do g1
   (J05, 6º) conta como página por local por causa de "centro", e o coletor corta o caminho em 50 caracteres (54 dos
   352 resultados têm caminho com exatamente 50, cortado ou no limite), o que esconde o nome do local quando ele vem
   no fim. Quatro resultados contam como página de serviço e terminam no começo de um nome de bairro: I05, 6º
   ("…-em-int", busca de Interlagos); K10, 2º ("…-no-jardim-paulist"); e um mesmo endereço em I08, 4º, e em J10, 3º
   ("…-em-sao", que tanto pode ser São Miguel, o bairro das duas buscas, quanto São Paulo, que a regra não conta como
   local); fica de fora uma página de consulta de empresas (I17, 9º), em que o que está cortado é o nome de uma
   empresa. **Dois dos quatro estão entre os três primeiros** (J10, 3º, e K10, 2º). Se os quatro contassem como página por
   local, o efeito seria de cerca de 1 ponto percentual em cada grupo (I: 157 → 159 de 179; J: 58 → 59 de 88; K: 2 →
   3 de 85); nos três primeiros lugares, 80 páginas por local e 29 de serviço, em vez de 78 e 31; e 22 das 30 buscas
   com bairro teriam os três primeiros todos por local, em vez de 21 (5 de 10 no grupo J, em vez de 4) — seção 5.1.
   Os números deste documento seguem a regra como está no CSV; essas páginas não foram abertas. No grupo I, 147 das
   157 páginas por local trazem o bairro buscado; as outras 10 são de região ou têm o caminho cortado.
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
- As duas amostras foram feitas em horas diferentes e com grupos de busca diferentes; a diferença nos percentuais
  **não** mede efeito de bairro novo. Bairro com bairro: grupo D 16, 17, 9 e 14 de 20; grupo I 19, 18, 19 e 15 de 20.

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
  **em parte** nesta amostra: o resumo de IA e, nas buscas de bairro, o bloco de mapa vêm antes do orgânico; o
  primeiro anúncio de texto, nesta hora, ficou abaixo do primeiro orgânico em 34 de 35 buscas (se no fim da página,
  não foi medido); o bloco que contém o perfil patrocinado (anúncio dentro do bloco de mapa) começa acima do primeiro
  orgânico em 18 das 25 buscas em que o patrocinado apareceu (14 de 15 no grupo I). **A posição da linha patrocinada
  não foi medida:** o coletor mede o título do bloco, e a linha patrocinada é a primeira da lista em 11 dessas buscas
  e a última em 14. *(observação de 40 buscas numa madrugada; não pode ser estendida ao horário comercial — limite
  1)*

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

- **Duas listas de locais na mesma tabela:** as linhas I, J e K usam a lista de locais com os 20 bairros novos; as
  linhas do item 4 (D, E e B) usam o tipo gravado em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, com a
  lista de 13/11. Com a lista ampliada, D e E não mudam; no grupo B um resultado muda (B01, 8º, linha 159 desse CSV,
  caminho terminado em "-no-morumbi"): página por local, 6 de 116 (5%, em vez de 4%); de serviço, 79 de 116 (68%, em
  vez de 69%).
- Nos três primeiros lugares das 40 buscas (120 resultados): 78 páginas internas por local, 31 de serviço, 5
  iniciais, 5 de governo, 1 de blog. Em 21 das 30 buscas com bairro (I e J), os três primeiros são todos páginas por
  local (17 de 20 em I; 4 de 10 em J). Ressalva do limite 5: dois caminhos cortados que contam como serviço estão
  entre os três primeiros (J10, 3º, e K10, 2º); se contassem como página por local, seriam 80 e 29, e 22 das 30 (5
  de 10 em J). As páginas não foram abertas.
- **Domínio com o nome do bairro** aparece em 5 das 20 buscas de bairro novo (Brooklin, Saúde, Vila Prudente,
  Tucuruvi, Vila Maria), uma vez em primeiro lugar (Saúde) — não lidos. O de Tucuruvi é subdomínio
  (`dedetizadoranotucuruvisp.pgmp.com.br`); na busca de Vila Maria há dois: o 2º lugar e, em 9º, o guia de bairro
  citado na seção 5.3.

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
  K, o mais frequente é uniprag.com.br (6 resultados: cinco artigos de blog e uma página de serviço).
- **Domínios novos:** 46 de 119 (55 resultados, 16%); no grupo K são 21 de 54 (28% dos resultados). Entre eles,
  três de governo (`sp156.prefeitura.sp.gov.br`, `servicos.sp.gov.br`, `agricultura.sp.gov.br`), um portal de
  síndicos, uma página de consulta de empresas e sites de uma praga só (cupim, abelhas, piolho de pombo) — pelo
  endereço; não lidos.
- **Governo:** 9 resultados em 6 buscas — escorpião em Pirituba (3º), mosquitos (1º, 5º e 6º), marimbondos (2º),
  ratos (1º e 6º), broca de madeira (8º) e fumacê para condomínio (1º). O item 4 já tinha visto governo em
  desratização e em mosquito da dengue (5ª posição em cada); pragas novas com governo são duas (marimbondos e broca
  de madeira). Aqui o governo tem de 1 a 3 resultados por busca e é o primeiro em três; nas de escorpião do item 4
  era a maior parte da página (12 de 16). *(observação; 10 buscas não sustentam regra)*

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
  ocupam o primeiro lugar são uma "marca sem identificação vista" e uma "empresa com número de licença". Os totais
  (37 de 79 no item 4; 11 de 40 aqui) não se comparam: os grupos são outros. Grupo a grupo: bairro 35% → 40% (7 de
  20 → 8 de 20; sete das oito são de um mesmo site); praga × bairro 17% → 20% (2 de 12 → 2 de 10); praga com a cidade
  54% → 10% (7 de 13 → 1 de 10). Este último não mede queda: são 10 buscas, de pragas que não são as do grupo B, e 1
  de 10 é piso — 3 das 10 primeiras posições são de governo e 2 de domínio novo não lido. Continua sem prova de que
  exibir a licença acompanhe posição. A classe "sem identificação
  vista" depende de 1 a 3 páginas lidas por ferramenta que resume: **"não visto" não prova ausência.**
- Diretório: ohub.com.br em 5 das 20 buscas de bairro novo e em nenhuma das de praga; nenhum outro marketplace; há
  dois outros sites de lista no grupo I, não lidos: listazn.com.br (I11, 6º; já visto no item 4) e
  encontravilamaria.com.br (I15, 9º; guia de bairro, domínio novo).

## 6. Bloco de mapa

- 93 linhas, 60 perfis distintos (pelo nome; "Ddtizz" aparece com duas notas e dois números de avaliações — 5,0 com
  327 e 4,9 com 632 — e pode ser dois perfis) nas 31 buscas com bloco; **31 perfis não tinham aparecido na amostra principal**.
  Até 14/11/2026, 02:38, a coluna de nome do CSV dava 32 (e o script também): um perfil (busca I07, linha 98 de
  `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`) ficou com a nota e o resto da linha grudados no
  nome, porque o Google mostrou o número de avaliações dele como "1,1 mil"; por isso não casa com o mesmo perfil no
  item 4 (busca B06, linha 218 de `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`). A sessão principal corrigiu o script e regravou o CSV às 02:38 (só a linha 98 mudou); o script agora imprime 31.
  Mais frequentes: SJG Controle de Pragas Urbanas (9), Sanitech (5), Primordial Dedetização (4).
- **Nas 18 buscas de bairro novo com bloco: 45 perfis distintos em 54 linhas** — só 12 deles tinham aparecido nas
  buscas de bairro da amostra principal. O bloco muda de bairro para bairro mais do que o orgânico. *(observação de
  uma só localização)*
- Nota: mediana 5,0, mínima 4,0; 92% das 92 linhas com nota lida têm 4,8 ou mais (a 93ª linha é a do perfil do "1,1
  mil", com nota 5,0; com ela, 86 de 93, também 92%). Avaliações por perfil (59 lidos, de 60): mediana 82 nos 59
  perfis das 40 buscas (146 nos 61 da amostra principal), de 1 a 867. O 60º perfil mostra "1,1 mil" e ficou fora da
  conta, aqui e no item 4; com ele, a mediana daqui seria 86 e o máximo, cerca de 1.100. Só bairro: 76,5 (44 perfis
  lidos do grupo I; 78 com o perfil do "1,1 mil", que é do grupo I) contra 130 (35 perfis do grupo D). As coletas
  foram em horas diferentes e o bloco pode depender da hora (limite 1, com a fonte): é diferença observada, não
  característica dos bairros.
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
  local. Sem termo repetido; há 10 pares de variantes quase iguais, que só diferem por preposição, ordem das palavras
  ou "sp" no lugar de "são paulo". Em 9 deles uma das duas foi buscada e a outra está como "não buscado" — dois são
  desta ampliação: K08, linha 128 ("tratamento broca de madeira são paulo"), com a linha 2405 ("tratamento de broca
  de madeira são paulo"), e J04, linha 114, com a linha 1167; sete são do item 4 (linhas 6, 9, 55, 65, 72, 80 e 82).
  No décimo par (linhas 3 e 4) as duas foram buscadas.
- **Por intenção:** contratar 892; urgência 835; preço 833; confiança 140; informativa 21. **Por tipo de local:**
  bairro 2.289; região (`tipo_local` = zona) 315; cidade 92; sem local 25. A consulta K10 ("dedetização piolho de
  pombo são paulo") está com `praga` = pombos; piolho de pombo é outra praga — classificação discutível, mantida.
- **Volume: "não medido" em todas as linhas.** Continua sendo uma grade de hipóteses, não uma lista do que as pessoas
  buscam. Quatro dos bairros novos têm nome que é também palavra comum (Saúde, Liberdade, Consolação, Aclimação): uma
  combinação como "dedetização saúde" pode não ser lida como bairro — a própria coleta usou "sp" em duas delas.
- O método para medir volume segue o do item 4, seção 10 (Planejador de palavras-chave, na conta do owner).
- **Efeito em outros arquivos:** as contagens do mapa citadas no item 4 (seção 10) e no plano de conteúdo foram
  refeitas na mesma data (ver cada arquivo).

## 9. O que isto diz ao projeto (inferências, marcadas)

1. **A observação central do item 4 se sustenta em mais 20 bairros:** busca com bairro traz página do bairro, de
   poucos sites que aparecem na maioria das buscas de bairro (um em 17 de 20; dois em 14 e 13). *(observação; 40 bairros num total de duas noites)*
2. **Para o desenho, que não faz página por bairro, a porta continua sendo outra:** nas buscas de praga com a cidade
   (grupo K e grupo B), o orgânico é de páginas de serviço e de governo; no grupo K — o único dos dois com
   posição medida — começa na primeira tela em 8 de 10. *(observação +
   inferência; sem volume medido não sei se há busca que compense)*
3. **Nas 40 buscas, o rótulo do resumo de IA foi o primeiro dos quatro marcadores medidos em 38 das 39 em que
   apareceu;** se o resumo estava aberto e o que mais havia acima não foi medido. "Ser citável" **pode** pesar mais do
   que o item 4 conseguia dizer — hipótese: a posição do rótulo não mede clique nem citação, e o que o resumo cita
   continua sem registro. *(observação de 40 buscas + hipótese, não medida)*
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

Cinco das 40 buscas foram sorteadas (`shuf -n 5 --random-source=<(openssl enc -aes-256-ctr -pass
pass:"repeticao-reserva1-20261114" -nosalt </dev/zero 2>/dev/null)` sobre a coluna `id` de
`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv`, na ordem do arquivo; com `-pbkdf2` o resultado é outro) e refeitas na mesma madrugada, no mesmo navegador, logado na mesma conta, com 73
a 77 segundos entre uma e outra. Brutos: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl` (não entram em
`/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`).

**Registro das cinco repetições** (mesmos campos de
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md`, que é gerado por script e só traz as
40 buscas). Lido de `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl`, linhas 1 a 5; Google,
14/11/2026 (sábado, madrugada), horário de Brasília; "—" = a página não mostrou local; pixels a partir do topo da
página, janela de 945 pixels de altura. A primeira repetição saiu 403 segundos depois da última das 40 buscas
(01:06:01).

| id | termo (lido do título da página) | hora da navegação | logado | local exibido | IA | anúncios de texto | perfis no bloco (+ patrocinado) | orgânicos | ordem na página | IA (px) | 1º anúncio (px) | mapa (px) | 1º orgânico (px) | 1ª vez (hora da navegação) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| J01r | dedetização de baratas brooklin | 01:12:44 | sim | — | sim | 1 | 3 + 1 | 9 | IA > orgânico > mapa > anúncio | 249 | 2296 | 814 | 704 | 00:41:39 |
| I08r | dedetização são miguel paulista | 01:14:01 | sim | — | sim | 2 | 3 + 1 | 9 | IA > mapa > orgânico > anúncio | 250 | 2308 | 666 | 1654 | 00:21:26 |
| I20r | dedetização aclimação | 01:15:17 | sim | — | sim | 2 | 3 + 1 | 9 | IA > mapa > orgânico > anúncio | 250 | 2336 | 666 | 1682 | 00:39:55 |
| I04r | dedetização campo belo | 01:16:30 | sim | Osasco, SP | sim | 1 | 3 | 9 | IA > mapa > orgânico > anúncio | 251 | 2144 | 667 | 1490 | 00:16:08 |
| I14r | dedetização casa verde | 01:17:43 | sim | Osasco, SP | sim | 2 | 3 + 1 | 9 | IA > mapa > orgânico > anúncio | 203 | 2307 | 619 | 1653 | 00:31:23 |

**Comparação com a primeira vez:**

| Busca | 1ª vez | 2ª vez | Mesmo 1º resultado? | Mesmos 9 endereços, na mesma ordem? | Perfis do bloco em comum (de 3) | Local exibido | Anúncios de texto (1ª → 2ª) | 1º orgânico (px, 1ª → 2ª) | 1º anúncio (px, 1ª → 2ª) |
|---|---|---|---|---|---|---|---|---|---|
| J01 dedetização de baratas brooklin | 00:41 | 01:12 | sim | sim | 3 | nenhum nas duas | 2 → 1 | 704 → 704 | 2.295 → 2.296 |
| I08 dedetização são miguel paulista | 00:21 | 01:14 | sim | sim | 3 | nenhum nas duas | 2 → 2 | 1.654 → 1.654 | 3.344 → 2.308 |
| I20 dedetização aclimação | 00:39 | 01:15 | sim | sim | 3 | nenhum nas duas | 2 → 2 | 1.682 → 1.682 | 2.336 → 2.336 |
| I04 dedetização campo belo | 00:16 | 01:16 | sim | sim | 3 | Osasco, SP nas duas | 2 → 1 | 1.490 → 1.490 | 2.144 → 2.144 |
| I14 dedetização casa verde | 00:31 | 01:17 | sim | sim | 3 | Osasco, SP nas duas | 2 → 2 | 2.758 → 1.653 | 4.470 → 2.307 |

- **O que dá para dizer:** em até uma hora, do mesmo lugar e com a mesma conta, o orgânico e o bloco de mapa não
  mudaram. A posição do bloco de mapa e do primeiro orgânico mudou numa das cinco (Casa Verde: 1.724 → 619 e 2.758 →
  1.653, 1.105 pixels mais acima). A do primeiro anúncio de texto mudou em duas (São Miguel Paulista: 3.344 → 2.308;
  Casa Verde: 4.470 → 2.307). A ordem das quatro camadas foi a mesma nas cinco. Isso mostra que as posições da seção
  4 **variam de uma carga da página para outra**; o número de anúncios variou em duas.
- **O que não dá para dizer:** nada sobre outro dia, outro horário, outro ponto da cidade, outra conta ou celular.
