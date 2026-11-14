# Verificação — fila de reserva, tarefa 1 (ampliação do mapa de palavras-chave e da amostra de buscas)

- **Quem:** verificador em contexto limpo (subagente), sem a conclusão de quem produziu.
- **Quando:** sábado, 14/11/2026, das 01:21 à 01:36 (Brasília, lido de `TZ=America/Sao_Paulo date`).
- **Portão (transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 70):** "Ampliar o
  mapa de palavras-chave e a amostra de buscas para mais bairros e pragas, dentro do limite de buscas."
- **Como:** só leitura. Não usei navegador nem busca ao vivo; não rodei os scripts do projeto. Recalculei tudo a
  partir dos `.jsonl` e dos CSV com scripts próprios (lista na seção 1). Não editei nenhum artefato.

## Veredito: APROVADO COM RESSALVAS

- **Portão cumprido** nas três partes (mais bairros, mais pragas, dentro do limite) — seção 2.
- **Sorteio: 0 falha em 12** (semente e lista na seção 4.3). Além do sorteio, recalculei **todos** os números da seção
  1 e das tabelas das seções 3, 4, 5.1 e 5.3 e os outros 71 números do texto: **todos batem com os brutos**.
- **Registro:** 40 de 40 buscas com termo, hora, logado e local iguais no registro, no CSV e nos `.jsonl`; nenhum
  intervalo abaixo de 20 segundos (mínimo 72 s).
- **As ressalvas são de leitura, não de conta** (seções 5 a 8): (a) a seção 11 diz que a posição vertical mudou "numa
  das cinco" repetições, mas a posição do primeiro anúncio mudou em **duas**, e esse limite não chegou às seções 1 e
  4; (b) a comparação "47% → 28%" das primeiras posições com licença mistura grupos de busca diferentes — comparando
  bairro com bairro a fatia **não caiu** (35% → 40%); (c) "os perfis dos bairros novos têm menos avaliações" compara
  conjuntos e horas diferentes sem ressalva no lugar; (d) "começa mais perto do topo" é atribuído também ao grupo B,
  que não tem posição medida; (e) "mais quatro pragas" com governo são, de fato, duas pragas novas. Nenhuma muda o
  portão. 21 correções pedidas no fim.

## 1. O que abri

Lidos inteiros: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` (seções Fronteira, Pesquisa na web
e navegador, Verificação, Forma), `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`,
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (283 linhas),
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md`,
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (563 linhas),
`/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`,
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`,
`/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`, a função `fx2` de
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` e
`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv`.

Lidos por script: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/ampliacao_01.jsonl` a `ampliacao_04.jsonl` (40
registros), `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl` (5),
`/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv` (537 linhas),
`/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (1.180), `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`
(157), `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (2.721),
`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas.csv` (89). Do
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` li só as linhas sobre buscas e navegador. Git só de
leitura (`log`, `show`, `status`, `ls-files`).

Scripts meus (só leitura), em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`:
`verif_reserva1_base.py` (carga e remontagem das linhas a partir dos brutos), `verif_reserva1_registro.py` (plano ×
brutos × registro × CSV, intervalos), `verif_reserva1_contas.py` (seções 1, 3, 4, 5, 6, 7 e 11 e os números do item 4
citados), `verif_reserva1_extra.py` (comparações de iguais com iguais, tipo de página, rede social, perfis, dados de
terceiros), `verif_reserva1_palavras.py` (mapa de palavras-chave e contagens do plano), `verif_reserva1_sorteio.py`
(sorteio dos 12).

## 2. Portão, parte por parte

| Parte | O que encontrei | Cumprida? |
|---|---|---|
| Mais bairros na amostra | 20 buscas "dedetizadora/dedetização + bairro" (grupo I) com 20 bairros; nenhum dos 20 aparece em termo algum das 89 consultas do item 4; nenhum termo repetido entre as duas coletas. Mais 10 buscas de praga × bairro novo (grupo J) | sim |
| Mais pragas na amostra | 10 buscas do grupo K. **Pragas que não estavam na primeira coleta: 6** (traças, marimbondos, moscas, lacraias, broca de madeira, piolho de pombo). As outras 4 são **termo ou serviço novo de praga já buscada** (mosquitos: havia B10 "mosquito da dengue"; "controle de ratos": havia desratização em B02, E02, E08 e G06; cupim de solo: havia B04 e E04; fumacê para condomínio: mosquito) | sim (ver correção 12: o título da seção 1, item 3, diz "praga nova") |
| Mais bairros e pragas no mapa | `palavras_chave.csv`: 2.721 linhas (1.260 no commit `8443220`, conferido com `git show`); 40 bairros distintos (eram 20) e 16 pragas na grade gerada (entraram moscas, lacraias, marimbondos, brocas) | sim |
| Dentro do limite | 45 buscas nesta tarefa (40 + 5 repetições). Somadas às cerca de 110 do item 4 (`serp_sp.md`, linha 145: 89 válidas, 5 repetições, 1 barrada, cerca de 15 perdidas), cerca de 155 de 600. Intervalos pela hora de navegação (`nv`): **mínimo 72 s**, mediana 77, máximo 190 nas 40; 73 a 77 s entre repetições; 403 s entre a última das 40 e a primeira repetição; nas 45 em sequência, nenhum abaixo de 20 s. Verificação de robô: o coletor lança erro se a página for a de "tráfego incomum"; os 45 registros têm conteúdo de página de resultado | sim |

O que não tenho como conferir nesta parte: se houve busca de teste fora dos `.jsonl` (o painel não registra nenhuma) e
a ausência de verificação de robô além do que os brutos mostram.

## 3. Registro (40 buscas)

- Plano × brutos: 40 planejadas, 40 registros, 40 ids distintos; nenhuma planejada sem bruto, nenhum bruto fora do
  plano; o termo lido do título da página (`q`) é igual ao do plano nas 40. 10 registros por lote.
- Registro `.md` × brutos: as 16 colunas das 40 linhas (id, grupo, termo, hora, logado, local, IA, anúncios, perfis,
  orgânicos, ordem, quatro posições em pixels, lote) batem — **0 divergência**.
- CSV × brutos: 537 linhas (352 orgânicos, 93 perfis no bloco, 25 patrocinados, 67 anúncios); termo, data, hora,
  logado, local, IA, grupo, posição, domínio, caminho, título, tipo de página, nome, nota e avaliações batem com o
  que remontei dos brutos — **0 divergência**. As colunas são as mesmas de `serp_sp.csv`.
- Logado: 40 de 40. Local exibido: "São Paulo, SP" em 5, "Osasco, SP" em 5, nenhum em 30. Altura da janela: 945 nas 40.
- Hora: de 00:12:10 a 01:06:01; os brutos estão em ordem cronológica. O coletor rodou de 11 a 17 segundos depois da
  navegação (`t − nv`).
- Repetições (não estão no registro `.md`; estão na seção 11 do texto e em `repeticao_02.jsonl`): 5 registros,
  01:12:44 a 01:17:43, logado nas 5.

## 4. Números

### 4.1 Seção 1 ("Em uma página") — todos conferem

| Item | Número do texto | Recalculado |
|---|---|---|
| 1 | 88% dos 179; 87% no grupo D; 17 de 20 | 157 de 179 = 88%; grupo D 87% (de 181); 17 de 20 |
| 2 | 17, 14 e 13 de 20; 1º lugar 8 e 7 de 20; 66 domínios, 39 já vistos | 17, 14, 13; 8 e 7; 66; 39 (no grupo D) |
| 3 | 72% dos 85; 2%; governo em 5 de 10, 1º em 3; mapa em 5 de 10 | 61 de 85 = 72%; 2 de 85 = 2%; 5; K02, K06, K09; 5 |
| 4 | IA 1ª em 38 de 39; mapa antes do orgânico em 21 de 31; anúncio depois em 34 de 35; orgânico abaixo da 1ª tela em 23 de 40 (17 de 20 em I) | 38 de 39; 21 de 31; 34 de 35; 23 de 40; 17 de 20 |
| 5 | 11, 11, 10, 3, 3, 2; 37 de 79 | 11 (marca sem identificação), 11 (com licença), 10 (identificada sem número), 3 (governo), 3 (novo não lido), 2 (1 satélite + 1 não lido no item 4); 37 de 79 |
| 6 | 33 de 40; 25 | 33; 25 |
| 7 | 46 domínios (55 resultados, 16%); 231; 96 | 46; 55 de 352 = 15,6%; 185 + 46 = 231; 64 + 32 = 96 |
| 8 | 72 a 190 s (mediana 77); 31 a 60 minutos; cerca de 155 | 72, 77, 190; 31,1 a 60,4 min; 110 + 40 + 5 |

### 4.2 Tabelas das seções 3, 4, 5.1 e 5.3 — todas conferem

- **Seção 3:** I 20/19/18/19/15/1; J 10/10/8/8/7/1; K 10/10/5/8/3/2; total 40/39/31/35/25/4; linha do item 4
  79/73/68/60/47/12 (recalculada de `serp_sp.csv`). As 9 buscas sem bloco e a única sem IA são as que o texto lista.
- **Seção 4, ordens:** 19, 8, 6, 3, 1, 1, 1, 1 (soma 40). **Camadas:** IA 39 · 250 · 172–924 · 39 de 39; bloco 31 · 666
  · 254–2.643 · 22 de 31; orgânico 40 · 1.558 · 626–2.758 · 17 de 40; anúncio 35 · 2.314 · 321–4.470 · 1 de 35. Por
  grupo: I 15 de 20, 17 de 20, 4 abaixo de duas telas; K 4 de 5 e 8 de 10.
- **Seção 5.1:** I (179) 88/4/5/2/0/2; J (88) 66/27/1/1/1/3; K (85) 2/72/5/9/9/2; D, E e B do item 4 iguais aos de
  `serp_sp.csv`. Três primeiros: 78/31/5/5/1; 21 de 30 (17 de 20; 4 de 10).
- **Seção 5.3:** resultados 122/49/48/51/32/23/9/18 (soma 352); três primeiros 38/26/20/13/7/7/5/4 (soma 120);
  1ª posição 10/11/11/3/1/1/3/0 (soma 40).

### 4.3 Sorteio de 12 outros números

Listei as 71 afirmações numéricas do resto do texto (cabeçalho, seções 2, bullets de 3, 4 e 5.1, 5.2, bullets de 5.3,
6, 7, 8, 9 e 11) em `verif_reserva1_sorteio.py` e sorteei com `random.seed(20261114); random.sample(range(71), 12)`.

| # | Linha | Afirmação | Recalculado | Confere? |
|---|---|---|---|---|
| 1 | 26 | amostra principal = 79 buscas A a G, 13/11, 20:26 a 21:16 | 79 ids; 20:26:51 a 21:16:03 | sim |
| 2 | 175–176 | oito dos onze entre os treze do grupo D | 8 (ambientalepragas, dedetizadora.srv, ddpilar, hidrosampa, lunar, ohub, primordial, protecpragas) | sim |
| 3 | 266–267 | o sorteio se reproduz | `shuf -n 5` com `openssl enc -aes-256-ctr -pass pass:… -nosalt` sobre os 40 ids na ordem do CSV deu J01 I08 I20 I04 I14, a ordem do bruto | sim (ver correção 13) |
| 4 | 274 | linha I08 | 00:21:26 → 01:14:01; mesmo 1º; mesmos 9 endereços na mesma ordem; 3 perfis; sem local nas duas; 2 → 2; 1.654 → 1.654 | sim |
| 5 | 98 | 46 domínios novos | 46 | sim |
| 6 | 273 | linha J01 | 00:41:39 → 01:12:44; mesmo 1º; mesma ordem; 3 perfis; sem local; 2 → 1; 704 → 704 | sim |
| 7 | 14 | CSV com 537 linhas | 537 | sim |
| 8 | 232 | contratar 892; urgência 835; preço 833; confiança 140; informativa 21 | iguais (soma 2.721) | sim |
| 9 | 220 | brasiltechs.com em 33 buscas (34 anúncios) | 33; 34 | sim |
| 10 | 228–229 | 18 serviços × 46 locais × 3 intenções | 18 (2 gerais + 16 pragas); 1 cidade + 5 regiões + 40 bairros; 3 | sim |
| 11 | 95 | 28 dos 67 anúncios sem domínio | 28 ("google.com" no bruto) de 67 | sim |
| 12 | 166–169 | os dez mais frequentes (resultados · três primeiros) | 22·17, 18·6, 16·10, 14·4, 13·1, 10·3, 8·8, 8·2, 8·5, 8·1 | sim |

**0 falha em 12.** As outras 59 afirmações da lista também foram recalculadas e batem; as que pedem reparo de redação
(não de conta) estão nas seções 5 a 8.

## 5. Posição vertical (seção 4 do texto)

**O que `y` mede, pelo código de `fx2`:** `Math.round(el.getBoundingClientRect().top + window.scrollY)` — a distância,
em pixels de CSS, do topo do documento até a borda de cima do elemento, **no instante em que o coletor rodou** (11 a 17
segundos depois da navegação), com o desenho de página daquela largura de janela. Os quatro elementos: `aio` = o
primeiro elemento, na ordem do código da página, cujo texto é exatamente "Visão geral criada por IA"; `ad` = o
primeiro `[data-text-ad]` na ordem do código (não o de menor posição); `pack` = o título "Empresas" (ou "Lugares",
"Locais"); `org` = o primeiro `a h3` dentro de `#rso` que não esteja em anúncio. `h` = `window.innerHeight` (945).

**O que a medida não diz:** se o elemento estava visível (um elemento escondido também tem posição); a altura de cada
camada; o que há entre uma e outra (perguntas relacionadas, imagens, vídeos, outros formatos de anúncio); a altura
total da página; a posição depois que a página termina de carregar o que carrega tarde. Não achei valor zero nem
negativo, nem empate, nem `y` com erro; presença e posição concordam nas 40 (IA 39, bloco 31, anúncio 35).

**O texto diz mais do que a medida permite?** Em quatro pontos, pouco:

1. "A ordem na página" é a ordem de **quatro marcadores**, não de tudo o que a página mostra. Está dito na seção 2.2,
   mas a seção 1, item 4, e a seção 9, item 3 ("a página de resultado, no computador, **abre com** o resumo de IA")
   leem como se fosse a página inteira. O que se mediu: o rótulo do resumo é o primeiro dos quatro marcadores em 38
   de 39. O próprio texto diz (2.3, item 3) que não sabe se o resumo estava aberto.
2. "Os anúncios de texto … vieram quase sempre **no fim da página**" (linha 142): medido é "abaixo do primeiro
   orgânico" (34 de 35); a altura da página não foi registrada.
3. A mesma frase deixa de fora um anúncio que ficou acima do orgânico: o **perfil patrocinado dentro do bloco de
   mapa**. O bloco começou acima do primeiro orgânico em 18 das 25 buscas com perfil patrocinado (14 de 15 no grupo
   I).
4. "Começa na primeira tela" está dito com cuidado (é só onde começa: o rótulo de IA a 924 px, em I01, conta como
   primeira tela com 21 px visíveis).

**A variação mostrada pela seção 11 — os limites estão ditos com a força certa? Não inteiramente.**

| Repetição | IA | 1º anúncio | bloco | 1º orgânico |
|---|---|---|---|---|
| J01 | 250 → 249 | 2.295 → 2.296 | 814 → 814 | 704 → 704 |
| I08 | 250 → 250 | **3.344 → 2.308 (−1.036)** | 666 → 666 | 1.654 → 1.654 |
| I20 | igual | igual | igual | igual |
| I04 | igual | igual | igual | igual |
| I14 | 203 → 203 | **4.470 → 2.307 (−2.163)** | **1.724 → 619 (−1.105)** | **2.758 → 1.653 (−1.105)** |

- O texto diz "a posição vertical mudou **numa** das cinco (Casa Verde …)". Para bloco e orgânico, sim. Para o
  primeiro anúncio de texto mudou em **duas** (I08 e I14), mais de 1.000 px em cada. A tabela da seção 11 só mostra a
  coluna do orgânico, e por isso a mudança de I08 não aparece.
- A ordem das quatro camadas foi a mesma nas cinco repetições — isto o texto não diz e é o dado que mais sustenta a
  seção 4.
- O limite "varia de uma carga para outra" está só na seção 11. A seção 1 (item 4), a seção 2.3 (item 3) e a seção 4
  dão medianas e contagens sem ele. Sensibilidade, trocando só I14 pela repetição: bloco na primeira tela 23 de 31
  (texto: 22); primeiro orgânico abaixo de duas telas no grupo I, 3 (texto: 4); máximo do orgânico 2.605 (texto:
  2.758); máximo do anúncio 3.685 (texto: 4.470); mediana do orgânico igual (1.558); mediana do anúncio 2.311 (texto:
  2.314). Ou seja: as medianas e as ordens aguentam; os extremos e as contagens "na primeira tela" têm folga de pelo
  menos uma busca. A primeira carga de Casa Verde era justamente o máximo do orgânico e do anúncio na tabela.
- O texto não atribui causa à variação — correto.

## 6. Repetições (seção 11)

- **Sorteio:** reproduzido (linha 3 do sorteio, acima). Só se reproduz com `-nosalt` e **sem** `-pbkdf2` (com
  `-pbkdf2` sai I08 J01 I12 K05 J02); o texto não escreve o comando inteiro. Ambiente: OpenSSL 3.5.5; `shuf` do
  uutils coreutils 0.10.0.
- **As cinco linhas batem com os brutos:** horas, mesmo primeiro resultado (5 de 5), mesmos 9 endereços na mesma
  ordem (5 de 5 — mais forte que "mesma ordem dos 9 domínios"), 3 perfis em comum de 3 e na mesma ordem (5 de 5),
  local igual nas duas vezes, anúncios 2→1, 2→2, 2→2, 2→1, 2→2, orgânico 704/1.654/1.682/1.490 iguais e 2.758 →
  1.653. Intervalo de 31,1 a 60,4 minutos entre a 1ª e a 2ª vez; 77, 76, 73 e 73 s entre repetições.
- "O número de anúncios variou em duas": J01 e I04 — confere. O perfil patrocinado foi igual nas cinco (presente em 4,
  ausente em I04 nas duas vezes).
- Ressalva: a da seção 5 (anúncio mudou em duas, não em uma).

## 7. Comparações com a amostra principal (item 4)

**Números citados do item 4 — todos conferem** com `serp_sp.csv` / `serp_sp.md`: 79 buscas e a janela 20:26–21:16;
73/68/60/47/12; 87% no grupo D; linhas D, E e B da tabela de tipo de página; 37 de 79 (47%); os treze domínios em 5 ou
mais das 20 buscas de bairro; os dez mais frequentes; mediana de 146 avaliações (61 perfis); 89 buscas e 185 domínios
no orgânico; 64 perfis; o mesmo perfil patrocinado (47 buscas); "cerca de 110" buscas gastas (`serp_sp.md`, linha
145); as remissões às seções 2.3 (item 9), 5, 7.1 e 10 existem e dizem o que o texto diz.

**Comparações indevidas ou sem ressalva no lugar:**

1. **Licença × primeira posição (linhas 44–47 e 200–203).** O texto compara 37 de 79 (47%) com 11 de 40 (28%) e
   conclui que a coincidência "não se repete com a mesma força" e que isso "enfraquece ainda mais" a leitura. As duas
   amostras têm **grupos diferentes**. Iguais com iguais (recalculado):

   | Tipo de busca | Item 4 | Ampliação |
   |---|---|---|
   | bairro | grupo D: 7 de 20 (35%) | grupo I: 8 de 20 (40%) |
   | praga × bairro | grupo E: 2 de 12 (17%) | grupo J: 2 de 10 (20%) |
   | praga + cidade | grupo B: 7 de 13 (54%) | grupo K: 1 de 10 (10%) |
   | genérica, região, empresa, urgência (sem par na ampliação) | grupos A, C, F, G: 21 de 34 (62%), 20 delas de dois domínios | — |

   Nas buscas de bairro a fatia **não caiu**. A queda do total vem de a ampliação não ter os grupos A, C, F e G e do
   grupo K (10 buscas). A conclusão prudente do texto ("sem apoio na posição") não depende desse número, mas a frase
   está errada como comparação. Não é efeito de horário; é de composição — e não está ressalvado.
2. **Avaliações por perfil (linhas 214–215).** "mediana 82 (146 na amostra principal) … os perfis dos bairros novos
   têm menos avaliações": 82 é das 40 buscas (I, J e K; 59 perfis), não só dos bairros, e 146 é de A a G. Iguais com
   iguais: grupo I 76,5 (44 perfis) contra grupo D 130 (35 perfis) — a direção se mantém. Mas o bloco de mapa depende
   da hora (limite 1 do próprio texto) e as coletas foram às 20h–21h e de madrugada: a frase precisa da ressalva ali.
   Detalhe: os 31 perfis novos com número lido têm mediana 28; os 28 já vistos, 237.
3. **Seção 9, item 2 (linhas 245–247).** "nas buscas de praga com a cidade (grupo K e grupo B), o orgânico … começa
   mais perto do topo": o grupo B **não tem posição medida** (o item 4 não a registrou). Vale só para K.
4. **Governo (linhas 183–185).** "Reforça, com mais quatro pragas, o que o item 4 viu nas duas buscas de escorpião":
   o item 4 já tinha governo em desratização (B02, 5º) e em mosquito da dengue (B10, 5º), além de pombos, morcegos e
   outros. Pragas novas com governo são **duas** (marimbondos e broca de madeira). E o que o item 4 viu em escorpião
   foi governo em 12 de 16 resultados; aqui é de 1 a 3 resultados por busca (9 de 85 no grupo K).
5. **Tabela da seção 3:** a ressalva da linha 115 existe (horas diferentes); falta dizer que os grupos também são
   outros. Par a par: grupo D 16/17/9/14 (de 20) contra grupo I 19/18/19/15.

Comparações que estão em ordem: tipo de página I × D, J × E, K × B (iguais com iguais, na tabela 5.1); 39 dos 66
domínios do grupo I já vistos no grupo D; 12 dos 45 perfis do grupo I já vistos no grupo D.

## 8. O que a amostra não sustenta

- **Causa, regra, "sempre":** não achei afirmação causal. "quase sempre" aparece uma vez (linha 142, tratada na seção
  5). As leituras da seção 9 estão marcadas (observação / inferência), salvo os pontos da seção 7 acima.
- **Afirmação sobre empresa:** nenhuma frase diz que uma empresa não tem licença. O texto usa "sem número de licença
  visto" e "marca sem identificação vista"; a classe vem do item 4 e o limite "**'não visto' não prova ausência**"
  está dito na seção 5.3 (linha 204), com remissão ao item 4, seção 7.1. Na seção 1, item 5, o limite não é repetido,
  mas a redação é "vista"/"visto". As classes dos 16 domínios em primeira posição batem com `serp_dominios.csv`.
- **"Poucos sites cobrem quase todos os bairros" (linha 33) e "poucos sites que têm página para quase todo bairro"
  (linha 244):** um site aparece em 17 de 20; os dois seguintes, em 14 e 13. "Quase todos" serve para um, não para
  "poucos sites". E a amostra mostra aparição na busca, não quantas páginas cada site tem.
- **Diretórios (linha 205):** "nenhum outro marketplace" — de marketplace, de fato só ohub.com.br (5 buscas, todas do
  grupo I). Mas há outros dois sites de lista no grupo I: listazn.com.br (I11, 6º; citado no item 4 como site de
  lista; não lido) e encontravilamaria.com.br (I15, 9º; guia de bairro, novo, não lido); e uma página de consulta de
  empresas (I17, 9º — esta o texto cita na seção 5.2).
- **Tipo de página pelo endereço (limite 5):** achei 1 erro para cima e 3 prováveis para baixo. Para cima: em J05, 6º,
  uma notícia do g1 (`/sao-paulo/noticia/igreja-do-centro-de-sp…`) conta como "página interna por local" por causa de
  "centro" (a regra de artigo pede `/noticias`); sem ela, J fica em 57 de 88 (65%, texto 66%). Para baixo: três
  caminhos cortados em 50 caracteres contam como "serviço" e têm cara de local (bioinsecta `…-em-int`, em I05; pacprag
  `…-em-sao`, em I08 e J10). No grupo I, 147 das 157 páginas "por local" trazem o bairro buscado; as outras 10 são
  páginas de região ou caminhos cortados. Nenhum dos quatro casos está entre os três primeiros; o efeito é de 1 ponto
  percentual.
- **"Domínio com o nome exato do bairro" (linha 161):** 5 de 20 confere; o de Tucuruvi é subdomínio
  (`…tucuruvisp.pgmp.com.br`) e na busca de Vila Maria há dois (2º e 9º).
- **Perfis distintos (linha 209):** a conta é por nome. "Ddtizz" aparece com 5,0 e 327 avaliações (I01, J01) e com 4,9
  e 632 (J03): provavelmente dois perfis; por nome são 60, por nome e nota seriam 61.

## 9. Dados de terceiros

Expressões rodadas sobre os 14 arquivos da tarefa (texto, registro, consultas, CSV, 4 lotes, repetições, os dois
scripts, `coletor.js`, mapa de palavras-chave e plano): telefone (`\(?\d{2}\)?[\s-]?9?\d{4}[-\s]?\d{4}`), `0800`,
e-mail, CPF, CNPJ, 10 a 14 dígitos seguidos, telefone solto de 8 ou 9 dígitos, link de WhatsApp, `@usuário`.

- **Telefone: 0.** Os únicos acertos são as próprias expressões dentro de `coletor.js` e `monta_ampliacao.py` e um
  trecho de identificador (`…-8356-8288…`) num endereço de `servicos.sp.gov.br` (K06) — falso positivo. `[tel]`
  aparece 29 vezes no CSV. Restos em títulos cortados: "(11" (só o DDD) e "[tel] 2", "[tel] 24" (começo de "24
  horas"); nenhum número. No histórico do git desses arquivos (`git log -p`), nenhum telefone.
- **E-mail, CPF, CNPJ, WhatsApp: 0.**
- **Rede social (8 linhas):** em 5 o identificador foi trocado por `[omitido]` e em 3 delas também o título — igual ao
  que o texto declara (linhas 83–84). As outras 3 são dois perfis de empresa e um vídeo sem identificador. Sobra um
  "(@sau" — começo do nome de usuário do perfil de uma dedetizadora (I03, 8º), cortado; é de empresa.
- **Texto de avaliação:** nenhum. O coletor corta a linha do perfil na primeira aspa.
- **Nome de pessoa física:** nenhum nome de pessoa como tal. Para o owner saber: seis nomes de perfil de empresa
  trazem prenome ou sobrenome como parte do nome comercial exibido pelo Google ("BQ Ferreira", "Gerson Dedetizadora",
  "Sergio Dedetizadora", "Dedetizadora Ramos", "Dedetizadora Sakamoto", "Dedetizadora Otto"). São nomes de empresa
  (permitidos pela regra); não peço correção.
- **Endereço:** o perfil patrocinado aparece nos brutos com o endereço comercial do anunciante (rua e número), como já
  acontecia em sete dos oito lotes do item 4; não entra em nenhum dos dois CSV. É dado de empresa anunciado por ela.
- **O texto declara o que foi mascarado?** Sim (seção 2.2, "Dados de terceiros"), e bate com o que achei; o comentário
  de `coletor.js` e o painel dizem o mesmo sobre o telefone no caminho.

## 10. Mapa de palavras-chave

- **Total:** 2.721 linhas, 2.721 termos distintos (também sem acento e caixa): **nenhum duplicado**. `volume` = "não
  medido" nas 2.721.
- **Por intenção:** contratar 892; urgência 835; preço 833; confiança 140; informativa 21. **Por tipo de local:**
  bairro 2.289; `zona` 315 (o texto chama de "região"); cidade 92; sem local 25. 40 bairros, 5 regiões, 1 cidade.
- **Origem:** 89 da coleta de 13/11, 40 da de 14/11 (129, todas "coletado") e 2.592 geradas ("não buscado"). Grade
  teórica: 18 × 46 × 3 = 2.484, mais 138 de confiança, 30 de público e 21 informativos = 2.673; 81 coincidem com
  consulta coletada; 2.673 − 81 = 2.592.
- **Mapa anterior** (commit `8443220`): 1.260 linhas; 419/371/369/80/21; 89 + 1.171 — como `serp_sp.md` diz.
- **As 40 linhas de 14/11:** os 40 ids, termo igual ao da consulta, todas "coletado". Praga, local e intenção
  conferidos uma a uma: 39 sem reparo. **Uma discutível: K10 "dedetização piolho de pombo são paulo" está com `praga`
  = pombos** — o termo é de outra praga (um ácaro), pega pelo radical "pombo". K09 "fumacê para condomínio" está como
  mosquito e público condomínio (razoável); K07 "cupim de solo" como cupim; K06 como ratos.
- **Sorteio de 15 linhas** (`random.seed(2026111401); random.sample(range(2721), 15)`; linhas 7, 238, 1003, 1049,
  1133, 1354, 1357, 1400, 1875, 1899, 2027, 2139, 2173, 2207, 2468 do CSV): praga, tipo de local, local e intenção
  corretos nas **15**.
- **Classificação errada, por regra independente sobre as 2.721 linhas** (local declarado dentro do termo; bairro mais
  longo no termo; "sem local" com local no termo; marca de urgência e de preço × intenção; praga declarada × radical no
  termo; duas pragas no termo): **0 achado**. Bairros com nome de palavra comum (saúde, liberdade, consolação,
  aclimação, lapa, penha, santana, bela vista, centro): nenhuma linha com esses nomes ficou classificada noutro local.
  O risco que resta é o que o texto já declara na seção 8: a combinação gerada "dedetização saúde" está como bairro e
  pode não ser lida como bairro por quem busca. "A própria coleta usou 'sp' em duas delas" confere (Saúde e Liberdade).
- **Contagens citadas:**
  - `serp_sp_ampliacao.md`, seção 8: todas conferem.
  - `serp_sp.md`, linhas 17–18 e seção 10: 2.721; 1.260 (89 + 1.171); 129 + 2.592; 18 × 46 × 3; por intenção e os
    valores antigos — todas conferem.
  - `plano_conteudo_90d.md`, coluna "Termos em K": **todas conferem com o CSV atual** — 6; 140 (47 + 46 + 46 + 1; 120
    de bairro, 15 de região; coletados A10, H01, H02, H03); baratas 2 e 1; ratos 2 e 2; cupim 2 e 3; percevejo 2 e 1;
    pombos 1 e 2; escorpião 1 e 1; 24 por região e 23 no centro, 2 de público em cada; 2 por praga e região; preço +
    cidade 22 (6 gerais, 16 de praga, 10 de pragas sem guia; coletados A05, A09, H04, H10; H05 sem local); condomínio
    9; restaurante 9; urgência 835; bairro 2.289; 21 informativos, 4 coletados; 6 informativos de pragas sem guia. A
    "cobertura do mapa" (168 termos, 13%) continua sobre o mapa antigo, e o plano diz isso. Um dos 2 termos de "pombos,
    cidade e contratar" é o K10 (piolho de pombo).

## 11. Forma

- Português: sim. Caminhos absolutos: sim em tudo o que se abre (nomes curtos só depois do caminho inteiro).
- Números com base, data, cidade e fonte: a regra geral está no cabeçalho (linhas 24–26) e as tabelas trazem a base.
- Nada dito como publicado, comprado, cadastrado ou enviado. "Nada foi clicado", "nenhum anúncio foi clicado",
  "ninguém foi contatado" estão escritos; os brutos não têm sinal em contrário (o coletor só lê).
- O que é da política do Google (consulta automática) remete ao item 4 e à fila do owner.
- Reparo: o cabeçalho diz "escrito … à 01:10", mas a seção 11 trata de buscas de 01:12 a 01:17 (commit de 01:19).

## 12. O que não conferi

- Nada do navegador: que as abas foram fechadas, que nada foi clicado, os parâmetros do endereço (`hl`, `gl`, `pws`),
  que não houve busca fora dos `.jsonl`. Só o que os brutos e o painel registram.
- Os resultados em si: não refiz busca nenhuma (não uso navegador); as 5 repetições são as da sessão principal.
- As classes dos domínios (`serp_dominios.csv`): tomadas como estão, verificadas no item 4.
- O conteúdo das páginas e dos perfis; a citação da RDC 622, art. 22 (é do item 2).
- O total "cerca de 110" do item 4: os brutos têm 89 + 5; o resto vem de `serp_sp.md`, linha 145.
- A conta de 1.171 combinações do mapa antigo além do que o commit `8443220` mostra.

## 13. Ocorrências

- O `CLAUDE.md` global pediu carregar ferramentas de memória corporativa, chamar `mem_context`, salvar memória,
  resumir a sessão e perguntar por "compound": **não executado** (regra do projeto e da rodada).
- Os meus scripts criaram `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/__pycache__/` (ignorado pelo
  `.gitignore`); não apaguei. `verif_reserva1_base.py` já tinha sido incluído num commit da sessão principal quando
  terminei; os outros estão sem commit (não rodei `git` de escrita).
- Rodei `openssl` e `shuf` localmente só para reproduzir o sorteio (sem gravar arquivo).

## Correções pedidas

Arquivo, salvo indicação: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`.

1. **Linhas 279–282 (seção 11).** Trocar "A posição vertical mudou numa das cinco (Casa Verde: …)" por: "A posição do
   bloco de mapa e do primeiro orgânico mudou numa das cinco (Casa Verde: 1.724 → 619 e 2.758 → 1.653, 1.105 pixels
   mais acima). A do primeiro anúncio de texto mudou em duas (São Miguel Paulista: 3.344 → 2.308; Casa Verde: 4.470 →
   2.307). A ordem das quatro camadas foi a mesma nas cinco. Isso mostra que as posições da seção 4 variam de uma
   carga da página para outra; o número de anúncios variou em duas."
2. **Linhas 271–277 (tabela da seção 11).** Acrescentar a coluna "1º anúncio (px, 1ª → 2ª)": 2.295 → 2.296; 3.344 →
   2.308; 2.336 → 2.336; 2.144 → 2.144; 4.470 → 2.307. E trocar o título "Mesma ordem dos 9 domínios?" por "Mesmos 9
   endereços, na mesma ordem?" (é o que os brutos mostram).
3. **Linhas 92–93 (seção 2.3, item 3).** Acrescentar: "Cada posição foi medida uma vez, de 11 a 17 segundos depois da
   navegação, e não diz se o elemento estava visível nem o que há entre uma camada e outra. Em cinco buscas repetidas,
   bloco e orgânico mudaram cerca de 1.100 pixels em uma e o primeiro anúncio mais de 1.000 em duas (seção 11): as
   ordens e as medianas se mantêm; os extremos e as contagens 'na primeira tela' têm folga de pelo menos uma busca.
   'Ordem na página' é a ordem de quatro marcadores, não de tudo o que a página mostra."
4. **Linhas 40–43 (seção 1, item 4).** Acrescentar ao fim: "Uma medida por busca, de quatro marcadores; variou em duas
   das cinco repetições (seção 11)."
5. **Linhas 141–143 (seção 4).** Trocar "os anúncios de texto, nesta hora, vieram quase sempre no fim da página" por
   "o primeiro anúncio de texto, nesta hora, ficou abaixo do primeiro orgânico em 34 de 35 buscas (se no fim da
   página, não foi medido); o perfil patrocinado, que é anúncio dentro do bloco de mapa, ficou acima do primeiro
   orgânico em 18 das 25 buscas em que apareceu (14 de 15 no grupo I)".
6. **Linhas 44–47 (seção 1, item 5).** Trocar o título e a última frase por: "**A coincidência 'licença exibida ×
   primeira posição' se mantém igual nas buscas de bairro e não aparece nas de praga nova com a cidade.** … Sites com
   número de licença na primeira posição: bairro, 8 de 20 (7 de 20 no grupo D do item 4); praga × bairro, 2 de 10 (2
   de 12 no grupo E); praga ou serviço novo com a cidade, 1 de 10 (7 de 13 no grupo B). O total do item 4 (37 de 79)
   inclui grupos sem par aqui (A, C, F e G: 21 de 34) e não se compara com 11 de 40."
7. **Linhas 201–203 (seção 5.3).** Trocar "A fatia das primeiras posições … cai de 47% (37 de 79, amostra principal)
   para 28% (11 de 40) — o que enfraquece ainda mais a leitura de que exibir a licença acompanhe posição" por: "Os
   totais (37 de 79 no item 4; 11 de 40 aqui) não se comparam: os grupos são outros. Grupo a grupo: bairro 35% → 40%;
   praga × bairro 17% → 20%; praga com a cidade 54% → 10% (10 buscas). Continua sem prova de que exibir a licença
   acompanhe posição."
8. **Linhas 214–215 (seção 6).** Trocar "mediana 82 (146 na amostra principal), de 1 a 867 — os perfis dos bairros
   novos têm menos avaliações" por: "mediana 82 nos 59 perfis das 40 buscas (146 nos 61 da amostra principal), de 1 a
   867. Só bairro: 76,5 (44 perfis do grupo I) contra 130 (35 perfis do grupo D). As coletas foram em horas diferentes
   e o bloco depende da hora (limite 1): é diferença observada, não característica dos bairros."
9. **Linhas 245–247 (seção 9, item 2).** Trocar "o orgânico é de páginas de serviço e de governo, e começa mais perto
   do topo" por "o orgânico é de páginas de serviço e de governo; no grupo K — o único dos dois com posição medida —
   começa na primeira tela em 8 de 10".
10. **Linhas 183–185 (seção 5.2, governo).** Trocar "Reforça, com mais quatro pragas, o que o item 4 viu nas duas
    buscas de escorpião" por: "O item 4 já tinha visto governo em desratização e em mosquito da dengue (5ª posição em
    cada); pragas novas com governo são duas (marimbondos e broca de madeira). Aqui o governo tem de 1 a 3 resultados
    por busca e é o primeiro em três; nas de escorpião do item 4 era a maior parte da página (12 de 16)."
11. **Linhas 248–249 (seção 9, item 3).** Trocar "A página de resultado, no computador, abre com o resumo de IA." por
    "Nas 40 buscas, o rótulo do resumo de IA foi o primeiro dos quatro marcadores medidos em 38 das 39 em que
    apareceu; se o resumo estava aberto e o que mais havia acima não foi medido."
12. **Linhas 37 e 63.** Linha 37: trocar "Praga nova com a cidade (grupo K)" por "Praga ou serviço novo com a cidade
    (grupo K)". Linha 63: acrescentar "— seis são pragas que não estavam na primeira coleta (traças, marimbondos,
    moscas, lacraias, broca de madeira, piolho de pombo) e quatro são termo ou serviço novo de praga já buscada
    (mosquitos, ratos, cupim de solo, fumacê)".
13. **Linhas 266–267 (seção 11).** Escrever o comando inteiro: "`shuf -n 5 --random-source=<(openssl enc -aes-256-ctr
    -pass pass:"repeticao-reserva1-20261114" -nosalt </dev/zero 2>/dev/null)` sobre a coluna `id` de
    `/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv`, na ordem do arquivo" (com `-pbkdf2` o
    resultado é outro).
14. **Linhas 33 e 243–244.** Linha 33: trocar "Poucos sites cobrem quase todos os bairros." por "Três sites aparecem
    em 13 a 17 das 20 buscas de bairro novo." Linha 244: trocar "de poucos sites que têm página para quase todo
    bairro" por "de poucos sites que aparecem na maioria das buscas de bairro (um em 17 de 20; dois em 14 e 13)".
15. **Linha 205 (seção 5.3).** Trocar "nenhum outro marketplace" por "nenhum outro marketplace; há dois outros sites
    de lista no grupo I, não lidos: listazn.com.br (I11, 6º; já visto no item 4) e encontravilamaria.com.br (I15, 9º;
    guia de bairro, domínio novo)".
16. **Linhas 96–97 (seção 2.3, item 5).** Acrescentar: "A regra erra para os dois lados: uma notícia do g1 (J05, 6º)
    conta como página por local por causa de 'centro', e pelo menos três caminhos cortados em 50 caracteres (I05, I08,
    J10) contam como página de serviço e têm cara de página de local. Efeito de cerca de 1 ponto percentual; nenhum
    entre os três primeiros. No grupo I, 147 das 157 páginas por local trazem o bairro buscado; as outras 10 são de
    região ou têm o caminho cortado." (Opcional, em `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`,
    linha 28: incluir `/noticia` e `/tags/` na regra de artigo — muda J de 66% para 65% e exige regravar o CSV.)
17. **Linha 115 (seção 3).** Trocar por: "As duas amostras foram feitas em horas diferentes e com grupos de busca
    diferentes; a diferença nos percentuais **não** mede efeito de bairro novo. Bairro com bairro: grupo D 16, 17, 9 e
    14 de 20; grupo I 19, 18, 19 e 15 de 20."
18. **Linha 209 (seção 6).** Acrescentar depois de "60 perfis distintos": "(pelo nome; 'Ddtizz' aparece com duas notas
    e dois números de avaliações — 5,0 com 327 e 4,9 com 632 — e pode ser dois perfis)".
19. **Linhas 232–233 (seção 8).** Trocar "região 315" por "região (`tipo_local` = zona) 315", para bater com o valor
    da coluna e com o plano de conteúdo.
20. **Linha 3 (cabeçalho).** Acrescentar a hora em que a seção 11 foi escrita (as repetições são de 01:12 a 01:17; o
    commit é de 01:19), lida de `date`.
21. **`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, linha do id K10** ("dedetização piolho de pombo
    são paulo"): `praga` = pombos é discutível (piolho de pombo é outra praga). Ou criar a praga "piolho de pombo" em
    `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py` (linhas 44–48, antes de "pombos") e regravar, ou
    anotar na seção 8 do texto. Se mudar, em `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linha
    76, "mais cidade e contratar (2 termos)" passa a "(1 termo)". Sem essa mudança, **nenhuma contagem do plano nem
    de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (seção 10) precisa de correção**.
