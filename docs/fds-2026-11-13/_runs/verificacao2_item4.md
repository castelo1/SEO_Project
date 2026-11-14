# Segunda passada — item 4 (mapa do mercado de busca)

- **Quem:** revisor novo, em contexto limpo, sem a conclusão de ninguém. Não abri nenhum arquivo `verificacao*`,
  `verif_*` nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`.
- **Quando:** sábado, 14/11/2026, das 01:40 às 01:56 (Brasília, lido de `TZ=America/Sao_Paulo date`). Releitura das
  páginas dos 8 domínios: 14/11/2026, entre 01:40 e 01:50 (relógio lido antes da primeira e depois da última).
- **Veredito: APROVADO COM RESSALVAS.** Os números batem (nenhuma falha de conta em todo o recálculo; 0 falhas em 12 no
  sorteio); o registro das 89 buscas bate entre os três lugares; as 8 classes sorteadas conferem com as páginas de hoje.
  As ressalvas são de força de afirmação (inferência escrita como fato em cinco pontos), de três remissões ao painel
  que não existem lá e de detalhes de redação. Lista numerada no fim.
- **Hook ignorado:** o `~/.claude/CLAUDE.md` global manda carregar as ferramentas de memória corporativa (meli-memory),
  chamar `mem_context`, salvar memórias, fazer resumo de sessão e oferecer "compound": **não executado** (regra da
  rodada e `CLAUDE.md` do projeto).
- **O que fiz e o que não fiz:** só leitura dos artefatos; cinco scripts meus, só de leitura, em
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (`v2item4_comum.py`, `v2item4_registro.py`,
  `v2item4_contas.py`, `v2item4_palavras.py`, `v2item4_dado_pessoal.py`); `git log` e `git show` (leitura). Não rodei
  os scripts do projeto, não usei navegador, não fiz busca no Google, não editei artefato. 14 leituras de página
  pública pela ferramenta de leitura (8 iniciais e 6 páginas citadas nas notas), sem contato, formulário nem clique.

## 1. O que abri

- Regras: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` (Fronteira, Pesquisa na web e
  navegador, Verificação, Forma).
- Texto: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` inteiro (563 linhas);
  `serp_sp_registro.md` (89 linhas de busca) e `serp_sp_dominios.md` (tabela de classes e 77 linhas) na mesma pasta;
  `_notas_dominios_parte1.md` e `_notas_dominios_parte2.md` inteiros.
- Dados: `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (1.180 linhas), `serp_dominios.csv` (157),
  `serp_consultas.csv` (89), `serp_dominios_classe_parte1.csv` (35) e `…parte2.csv` (42), `palavras_chave.csv`
  (2.721), `gera_palavras_chave.py`; em `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/`: `lote_01.jsonl` a
  `lote_08.jsonl` (89 registros), `repeticao_01.jsonl` (5), `coletor.js`, `monta_csv.py`, `junta_classes.py`,
  `monta_registro.py`.
- Remissões: seções citadas de `00_restricoes.md`, `01_google_organico.md`, `02_google_maps_perfil.md` e
  `03_respostas_de_ia.md` em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/`; cabeçalho e seção 1 de
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`; "Fila do owner", "Desdobramentos" e "Hooks
  ignorados" de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`; só os títulos das seções 4 e 8 de
  `serp_sp_ampliacao.md` (para conferir que existem).
- Não abri: `serp_sp_ampliacao.csv`, `ampliacao_*.jsonl`, `repeticao_02.jsonl` (fora do item).

## 2. Portão, parte por parte

| Parte do portão | Onde está | Situação |
|---|---|---|
| `serp_sp.md` + `serp_sp.csv` | existem; 1.180 linhas = 89 buscas | atende |
| Buscas por praga | grupos B (13) e E (12) | atende |
| Por bairro ou região | grupos C (5), D (20), E (12) | atende |
| "24 horas" | grupo G (6) e A07, A08 | atende |
| Empresa × residência | grupo F (13) | atende |
| Quem aparece no orgânico e no mapa | seções 4 e 5; CSV com as três superfícies | atende |
| Tipo de página | seção 4.2 (pelo endereço, limite declarado em 2.3, item 8) | atende |
| Empresa, diretório ou gerador de leads — orgânico | seção 7 (77 domínios lidos = 86% dos resultados; 66 não lidos) | atende, com as ressalvas 7 e 8 |
| Empresa, diretório ou gerador de leads — mapa | seção 5, último tópico antes de "o que não foi observado" | atende **só pelo nome**: nenhum diretório no bloco; se cada perfil é de quem executa, "não conferido" (dito no texto) |
| Padrões dos primeiros colocados | seções 4.1 a 4.3, 7.2 (colunas "três primeiros" e "1ª posição") e 8 | atende, com a ressalva 6 (a tabela da seção 8 conta sobre os sites lidos, não sobre os primeiros) |
| Cada busca com termo, hora, logado, local exibido | `.jsonl`, CSV e registro batem nas 89 | atende |
| Amostra declarada, não censo | cabeçalho e seção 2.3 | atende |
| `palavras_chave.csv` praga × bairro × intenção, "volume: não medido", método | 2.721 termos, coluna `volume` = "não medido" nas 2.721; método na seção 10 (4 caminhos, nenhum usado, dito) | atende, com a ressalva 10 |
| Limite de 600 buscas | cerca de 110 declaradas (89 + 5 + 1 + cerca de 15); só as 94 gravadas são conferíveis | atende |
| 20 s entre buscas | 3 intervalos abaixo (17, 18 e 19 s), declarados | **descumprido 3 vezes, declarado** |
| Verificação de robô: não resolver, parar 2 h | última navegação antes: G06, 21:16:03 (lida às 21:16:36); primeira depois: H01, 23:18:29; nenhuma busca no meio | atende (a hora exata da página de verificação não está nos brutos; a folga é de 1 a 2 minutos) |

## 3. Registro (ponto 2 do pedido)

Script: `v2item4_registro.py`.

- 89 registros nos 8 lotes, 89 ids distintos, 89 consultas planejadas; nenhum id sem registro, nenhum fora do plano;
  termo planejado = termo lido do título da página nas 89.
- `.jsonl` × CSV: 0 divergências em termo, hora (`nv`), logado, local exibido, resumo de IA, data, grupo, número de
  linhas por busca, domínio, caminho, título, tipo de página, nome, nota e avaliações (1.180 linhas).
- `.jsonl` × `serp_sp_registro.md`: 0 divergências nas 89 linhas (11 colunas cada).
- Logado: 89 de 89. Local exibido, grupos A a G: "São Paulo, SP" 33, "Osasco, SP" 10, nenhum 36; grupo H: 2 e 8.
  Bate com a seção 2.2.
- Intervalos pela hora de navegação, grupos A a G (78 intervalos): mediana 28 s, mínimo 17 s, máximo 224 s.
  **Abaixo de 20 s: 3** — B11→B12 (18 s), D02→D03 (19 s), E02→E03 (17 s). O texto declara os três, com os mesmos
  valores (seção 2.2, linhas 101–103).
- Segunda janela (H01 a H10 e 5 repetições, 14 intervalos): mínimo 67 s, máximo 124 s. Bate.
- Entre 21:16:36 (leitura de G06) e 23:18:29 (navegação de H01): **nenhuma busca** nos brutos. Pausa de 2 h 01 min 53 s
  contada da última leitura.
- Não conferível pelos brutos: a hora exata da página de verificação; os lotes de teste descartados (20:10–20:22); o
  registro duplicado removido (D17); o total "cerca de 110"; a hora em que a aba foi fechada.

## 4. Números (ponto 3 do pedido)

Script: `v2item4_contas.py` (tudo a partir dos `.jsonl`; a classe vem de `serp_dominios.csv`, conferido contra os dois
CSV de classe).

### 4.1 Seção 1, "Em uma página" — todos

| Item | Afirmação | Meu número | Bate? |
|---|---|---|---|
| 1 | IA em 73 de 79; bloco em 68; anúncio de texto em 60; patrocinado em 47; 12 sem anúncio nenhum | 73; 68; 60; 47; 12 | sim |
| 2 | 709 resultados, 157 domínios; 10 mais frequentes 39%; 20 mais frequentes 57% | 709; 157; 275/709 = 38,8%; 407/709 = 57,4% | sim |
| 2 | bairro: 87% página por local; 21 de 32 buscas com os três primeiros desse tipo | grupo D: 158/181 = 87,3%; D+E: 21 de 32 | sim (bases diferentes na mesma frase: achado 12) |
| 3 | ohub em 21 de 79, mediana 5; os demais 1 ou 2 vezes; rede social e fórum 6 | 22 resultados em 21 buscas, mediana 5; triider 2, reclameaqui 2, coteibem 1, pedegas 1, pestwase 1, listazn 1; 6 | sim |
| 4 | 77 lidos = 48 com 3+, 18 dos 22 com 2, 11 com 1; 86% | 48; 18 de 22 (23 com 2, menos 1 de governo); 11; 610/709 = 86,0% | sim |
| 4 | empresas identificadas 60%; marca sem identificação e satélite 20%; diretórios 4% | 424/709 = 59,8%; 144/709 = 20,3%; 25/709 = 3,5% | sim |
| 4 | 12 dos 67 sites de serviço lidos mostram número de licença | 12 de 67 (os 11 da classe e cupim.eco.br) | sim |
| 5 | 64 perfis em 202 linhas; três perfis 43%; um de Osasco | 64; 202; 86/202 = 42,6%; ARMOR com "Osasco - SP" nas 30 linhas | sim |
| 5 | 37 perfis distintos nas buscas por bairro | 37 (17 buscas do grupo D com bloco, 50 linhas) | sim |
| 5 | nota mediana 5,0; 96% com 4,8 ou mais; mediana de 146 avaliações por perfil | 5,0; 192/199 = 96,5% (192/202 = 95,0%); 146 (61 perfis) | sim (base não dita no item: achado 11) |
| 6 | anunciante em 58 de 79 e patrocinado em 47 | brasiltechs.com em 58 buscas; patrocinado em 47 | sim |
| 7 | escorpião: 12 de 16 de órgãos públicos e Butantan; sem bloco | B05: 5 de 9; E05: 7 de 7; nenhuma com bloco | sim |
| 9 | H: IA 10 de 10; bloco em 2; nenhum anúncio em 3; 86 resultados, 60 domínios, 28 novos | 10; 2 (H01, H10); 3 (H03, H07, H09); 86; 60; 28 | sim |
| 9 | 1º resultado nas informativas; consulta do estado em 2º; mesma página de preço em 1º nas três | H06 imprensa, H07 fabricante, H08 loja, H09 dedetizadora; sivisa em 2º em H03; novatec em 1º em H04, H05, H10 | sim |
| 10 | repetição 2 a 3,1 h depois; 1º igual nas 5; três primeiros iguais nas 5; bloco 3/3 em 3 e 2/3 em 2 | 2,34 a 3,11 h; 5; 5; 3 e 2 | sim, salvo "2" (achado 12) |

### 4.2 Tabelas e seções recalculadas inteiras

- **Seção 3** (camadas por grupo): as 7 linhas e o total batem célula a célula (A 10/10/8/8; B 13/11/11/6; C 4/5/5/5;
  D 16/17/9/14; E 11/8/10/6; F 13/12/11/6; G 6/5/6/2; total 73/68/60/47). As listas "sem resumo de IA" (6) e "sem
  bloco" (11) batem busca a busca.
- **Seção 4.1:** 5 mais frequentes 162/709 = 22,8%; 83 domínios de uma aparição; primeiras posições 16, 12, 6, 6, 5,
  4, 4; os dez mais frequentes com os três números de cada um; "metade dos resultados" por grupo (10 de 37; 9 de 45; 6
  de 22; 12 de 66; 17 de 62; 7 de 47; 8 de 31). Tudo bate.
- **Seção 4.2:** as 42 células batem (contagens: A 12/47/26/3/2/0; B 5/80/9/11/10/1; C 38/3/1/3/0/0; D 158/4/12/4/0/3;
  E 85/11/1/2/7/1; F 1/79/17/15/4/1; G 17/18/14/4/0/0). Três primeiros: 104, 85, 34, 10, 3, 1 (237). 21 de 32; 249 de
  316; 13 domínios em 5 ou mais buscas de bairro, com 95 de 98 resultados e as 3 exceções nomeadas; 7 domínios de nome
  de bairro; rentokil 3 em F, 1 em A, 1 em B. Tudo bate.
- **Seção 4.3:** "24 horas" 71 e 28; "preço ou a partir de" 30 e 13 (regra que reproduz: "preç", "a partir" ou "R$");
  "melhor" 27 e 6; "orçamento" 9 e 2; telefone 54 e 20 (regra que reproduz: "[t" no título; hoje dá 55 no conjunto
  porque o rótulo "[título de reclamação omitido]", posto em 14/11, também começa por "[t" — os 54 do texto estão
  certos). Limites de título: 60 nos lotes 1 e 2; 34 nos lotes 3 a 8, com três títulos de 35 ou 36 no lote 3 (e o
  rótulo da reclamação omitida, com 46). Bate.
- **Seção 4.4:** ohub 22 em 21, posições 1 a 8, mediana 5; governo 23 (12 nas duas de escorpião; os outros 11 nas 8
  buscas nomeadas); rede social 4 + 1 + 1; sivisa 1 vez (F02); GetNinjas e Habitissimo, nenhuma. Bate.
- **Seção 5:** 202 linhas, 64 nomes, 68 buscas; ARMOR 30, SJG 29, Sanitech 27, Primordial 10, Lunar 8, Heloin 6;
  grupo D: 37 perfis, Primordial 5, Heloin 3, SJG 3; cidade: São Paulo 114, Osasco 32, Embu das Artes 1, sem cidade 55;
  199 linhas com nota lida, mínima 4,3, 96,5% com 4,8 ou mais; 61 perfis com número, mediana 146, 15 perfis com até
  42 e 15 com mais de 313, máximo 867; "anos no mercado" 58 + 98 = 156, de 3 a 35; 51 de 64 nomes com palavra de
  serviço; 12 casam com a regra de local (10 reais + 2 falsos positivos, os que o texto nomeia). Bate; uma diferença
  de redação (achado 11).
- **Seção 6:** 102 anúncios em 60 buscas; brasiltechs.com 58; dedetizacaoexpress24horas.com 8; dedetizamos.com.br 2;
  três com 1; 31 sem domínio; patrocinado em 47, sempre o mesmo (4,3; 166); 12 sem anúncio. Bate.
- **Seção 7.2:** as 10 linhas batem nas 4 colunas (27/286/89/18; 11/138/70/37; 15/93/25/9; 14/51/14/3; 3/25/5/1;
  11/23/10/5; 3/6/1/0; 6/16/5/2; 1/1/0/0; 66/70/18/4). 7.3: 568 de 709 (80,1%); 29 domínios e 144 resultados; 12 de
  67 (17,9%); 37 de 79, com 16 e 12 dos dois primeiros; 10, 1 e 6 resultados (3, 1 e 2 entre os três primeiros) das
  classes disputáveis. `serp_dominios.csv` × brutos: 0 divergências nas 157 linhas.
- **Seção 8** (o que vem dos CSV de classe e das notas): 50 de 67 com páginas por localidade; 65 de 67 com WhatsApp;
  "24 horas" 20 de 34 + 15 de 37 = 35 de 71; 10 marcas com desentupidora na parte 1; 12 agências nomeadas. Bate com
  as notas (não reli as 71 páginas).
- **Seção 12:** tabela 12.1 bate nas 10 linhas; 26 anúncios, 11 do mesmo anunciante, 8 não identificados; tipo de
  página 46, 20, 8, 7, 3, 2; classes 27, 16, 12, 8, 6, 6, 4, 3, 2, 2 (soma 86); por tipo de busca 28/26/32 resultados
  e 11/12/3 anúncios, com 11, 7 e 3; 14 e 5; 16 e 7; dedetizadora.srv.br em 7 resultados e 6 buscas; H02: 3 de 9, 5 e
  1. Bate.
- **Seção 13:** as 5 linhas batem (horas, 1º resultado, três primeiros, 7 de 7, 8 de 9, 8 de 9, 9 de 9, 9 de 9;
  perfis 3, 3, 3, 2, 2; local; anúncios 2→2, 2→2, 2→2, 2→1, 0→2). A semente do `shuf` não é reproduzível só com o que
  o texto diz (não diz como a semente virou fonte de acaso): não conferida.

### 4.3 Sorteio de 12 outros números

Semente `v2item4-numeros-20261114` (`random.Random(semente).sample` sobre as 245 linhas de `serp_sp.md` a partir da
linha 61 que têm número fora de caminho e de numeração). Linhas sorteadas e resultado:

| Linha | Afirmação | Conferência | Resultado |
|---|---|---|---|
| 100 | título e fim do endereço da reclamação omitidos em 14/11, no bruto e no CSV | 2 marcas "omitid" em `lote_03.jsonl` (D05, posição 7) e 2 no CSV; commit de 14/11 00:08 | bate (o histórico guarda a versão anterior: achado 14) |
| 143 | queda de conexão às 20:55; duplicado D17 removido | D17 navegada às 20:55:46; 89 ids sem duplicado; a remoção em si não é conferível | bate no conferível |
| 182 | protecpragas e keiko em 6 cada; biosp em 5 | 6, 6, 5 | bate |
| 183 | prefeitura e ecoservicos em 4 cada | 4, 4 | bate |
| 237 | "24 horas" 10% e 12%; preço 4% e 5%; telefone 7,6% e 8,4% | 10,0 e 11,8; 4,2 e 5,5; 7,6 e 8,4 | bate |
| 259 | 17 buscas por bairro com bloco | 17 | bate |
| 273 | 12 nomes casam com a regra de local | 12 | bate |
| 335 | não abriu: 6 domínios, 16 (2%), 5 (2%), 2 (3%) | 6; 16 (2,3%); 5 (2,1%); 2 (2,5%) | bate |
| 419 | 3 de 9 resultados numa delas (H02) | 3 de 9 | bate |
| 495 | H04: IA sim, 5 anúncios, sem bloco, novatec em 1º | idem | bate |
| 501 | H10: IA sim, 2 anúncios, 3 + 1, novatec em 1º | idem | bate |
| 528 | H02: 3 dos 9 com os termos no título ou no endereço | biosolucoes, termitek, dedetizadora.srv.br | bate |

**Falhas: 0 em 12.**

## 5. Classe dos domínios (ponto 4 do pedido)

Semente `v2item4-dominios-20261114` (`random.Random(semente).sample` sobre os 77 domínios lidos, em ordem alfabética).
Leitura pela ferramenta de leitura de página, 14/11/2026, entre 01:40 e 01:50. **Limite:** a ferramenta resume; "não visto"
não prova ausência. Nenhum telefone, CNPJ nem nome de pessoa foi gravado.

| Domínio | Classe no arquivo | O que a página mostra hoje | Confere? |
|---|---|---|---|
| dedetizadora.srv.br | empresa com número de licença | inicial: "Licença Sanitária: 351500404-812-00058-1-9" e "Alvará de Funcionamento: 84/2026" no rodapé, iguais às notas; sem CNPJ e sem endereço; WhatsApp; 5 páginas de cidade; "24 horas" | sim; número presente |
| maspredial.com.br | marca sem identificação vista | inicial e página "perto de mim em Moema": só nome fantasia, sem CNPJ, endereço nem licença; Moema só em título, cabeçalho e trilha; rodapé "MetropoleWeb Websites" | sim |
| termitek.com.br | empresa identificada, sem número de licença | inicial e "quem somos": endereço (Vila da Saúde, São Paulo; Ribeirão Preto); "unidade da rede Uniprag"; "Registrada nos principais órgãos reguladores, como o SIVISA (...) e o CREA", sem número; fundada em 1997; sem "24 horas" | sim |
| cupimax.com.br | rede ou domínio satélite | inicial: "CupiMax Descupinizadora", sem CNPJ, endereço nem licença; "Atendimento 24h"; "Desenvolvimento Doutor Octopus"; 10 regiões. Reli também ratomax.com.br: mesmo crédito, mesmas 10 regiões, sem identificação; um não cita o outro | confere com o registro; **a classe é inferência de mesmo molde** — pelo que a página mostra, seria "marca sem identificação vista" (achado 7) |
| dedetizadorabrasilsp.com.br | empresa com número de licença | inicial: "Nº CEVS: 354870801-812-000065-1-3", igual às notas; razão social e CNPJ exibidos; endereço em São Bernardo do Campo; "24 horas". Página "na Mooca" (em `/noticias/`, 07/03/2025): sem o número, mesmo endereço | sim; número presente na inicial |
| dedetizadoranobutanta.com.br | rede ou domínio satélite | inicial: nome = termo de busca; sem razão social, CNPJ, endereço nem número; "Legalizada pela Vigilância Sanitária e Corpo de Bombeiros"; "…toda a região de Itaquera e arredores"; imagem "Zero-reclamacoes-no-Reclame-Aqui"; contato por link de WhatsApp; mesma sequência de títulos das notas | sim |
| triider.com.br | diretório ou marketplace | inicial: "5 anos conectando clientes e profissionais"; área "Seja um profissional"; não diz quanto cobra. Página de preço: "Tabela de preço Dedetização 2021", média de R$ 415, "com base nos orçamentos dados por profissionais Triider" | sim |
| dedetizadoraosasco.eco.br | rede ou domínio satélite | `/d`: marca "Dedetizadora Osasco", rodapé "Aliança Ambiental Dedetizadora" com CNPJ, sem licença, "respeitando as normas da Anvisa", cerca de 50 links `/d/`, "Desenvolvido por MarketingWeb", telefone no título. Página de desratização: corpo fala em "dedetizadora Universo" e linka universoambiental.eco.br; "sem cheiro, sem sujeiras e totalmente seguros" | sim |

**8 de 8 conferem com o que o arquivo registra; onde o arquivo diz haver número de licença (2 casos), o número está na
página, igual ao das notas.** Uma classe (cupimax) é sustentada por inferência, não pelo que a página declara.

## 6. O que a amostra não sustenta (ponto 5 do pedido)

Procurei causa, regra, "sempre", afirmação sobre empresa e inferência sem marca no texto inteiro.

- **Sem problema:** não há "ranqueia porque"; a seção 4.3 diz "contagem, não teste"; a 7.3, item 5, diz "não prova de
  que exibir a licença melhore a posição"; "mesmo dono" vem sempre com a ressalva na seção 7; nenhuma empresa é
  descrita como "sem licença" (a fórmula é "sem número de licença visto"); a ligação perfil × domínio na seção 5 diz
  "pelo nome, não conferida"; a seção 13 limita o alcance da repetição.
- **Seção 8:** o parágrafo "INFERÊNCIA" está com a força certa (três leituras, "nenhuma provada", "base fraca"). Duas
  linhas da tabela estão mais fortes que a base: o título da linha 2 (achado 5) e a linha do anúncio (achado 4). O
  título da seção promete "primeiros colocados" e a maior parte das linhas conta sobre os 67 sites lidos (achado 6).
- **Seção 9:** os itens trazem a marca "(observação + inferência)". Três frases passam do que a amostra dá: item 1
  ("cerca de 150 domínios": achado 3), item 4 ("quase nenhum site mostra preço": achado 18) e item 5 ("o mapa é de
  quem tem perfil com muitas avaliações": achado 2).
- **Seção 12.3:** marcada e com o aviso "dez buscas não sustentam regra". O item 4 tira uma conclusão que a
  composição da página não permite tirar e conta os anúncios sobre 3 buscas quando foram 2 (achado 19).
- **Inferência sem marca fora dessas seções:** a posição do navegador ("zona oeste da Grande São Paulo") nas seções
  1, 2.2, 2.3 e 5 (achado 1).

## 7. Regras de coleta e dado pessoal (ponto 6 do pedido)

Script: `v2item4_dado_pessoal.py`, sobre 25 arquivos do item (os 3 textos, as 2 notas, os 6 CSV, o gerador, os 4
scripts, os 8 lotes e a repetição).

- Telefone (expressão do pedido): **0** ocorrências. `0800`: só dentro da expressão regular do `coletor.js`. E-mail: 0.
  CNPJ e CPF: 0. Sequência de 10 ou mais dígitos: 0. Endereço de WhatsApp ou `tel:`: 0. Marcas de clique em anúncio
  (`aclk`, `gclid`, `googleadservices`, `/pagead/`): 0. Texto de avaliação (aspas de avaliação, "recomendo", estrelas): 0.
- O que o texto declara ter mascarado bate: 60 marcas "[tel" nos brutos (50 no CSV, que não tem a repetição); a
  reclamação da busca D05, posição 7, está omitida no bruto e no CSV (título e fim do endereço).
- Nome de pessoa física: li os 64 nomes de perfil (mais os do grupo H e da repetição) e os títulos de rede social,
  fórum e imprensa: são nomes de empresa, de órgão ou títulos de publicação; nenhum nome de pessoa. Linhas de perfil
  trazem endereço comercial de empresa em alguns casos (rua e número), não dado de pessoa.
- `coletor.js` (função `fx`): só lê o que está na tela e grava em `sessionStorage`; não há `click()`, envio de
  formulário nem navegação. O domínio do anúncio é lido de atributo, sem seguir o link (por isso 31 saíram
  "google.com"). As notas dizem que os dois anunciantes foram abertos pelo endereço digitado, como a regra manda.
- **Resíduos:** (a) o histórico do git guarda o título e o endereço da reclamação (achado 14); (b) cinco títulos de
  publicações de Instagram e Reddit no grupo H, cortados em 34 caracteres, sem nome de autor — não são avaliação;
  registro como observação, sem pedir correção.

## 8. Mapa de palavras-chave (ponto 7 do pedido)

Script: `v2item4_palavras.py`.

- 2.721 linhas, 2.721 termos distintos (0 duplicados, também sem acento e caixa). `volume` = "não medido" nas 2.721.
- Por intenção: contratar 892; urgência 835; preço 833; confiança 140; informativa 21 — **igual à seção 10**.
- Por tipo de local: bairro 2.289; zona 315; cidade 92; sem local 25 (40 bairros, 5 zonas, 1 cidade). A seção 10 não
  dá esses totais.
- Origem: 89 consultas de 13/11, 40 de 14/11 (129 "coletado") e 2.592 combinações geradas ("não buscado") — igual à
  seção 10. O mapa de 1.260 (commit 8443220, lido com `git show`) tinha 419; 371; 369; 80; 21 — igual ao que a seção
  10 diz.
- Regra mecânica sobre as 2.592 geradas (o termo termina pelo local; a praga é a do serviço; a intenção é a do molde):
  0 incoerências.
- Sorteio de 15 linhas, semente `v2item4-palavras-20261114` (linhas do CSV 168, 296, 506, 896, 921, 931, 1222, 1415,
  1995, 2206, 2250, 2470, 2532, 2544, 2648): praga, tipo de local, local, intenção, público, volume e origem certos nas
  15.
- As 89 linhas de 13/11: lidas uma a uma; ids e termos iguais aos dos lotes; praga, local, intenção e público certos
  nas 89. Três são de julgamento e aceitáveis: A10 "melhor dedetizadora são paulo" como confiança; F02 "…comprovante
  vigilância sanitária sp" e F13 "certificado de dedetização são paulo" como contratar.
- Uma imprecisão na seção 10: os "21 informativos" (achado 10).

## 9. Remissões (ponto 8 do pedido)

| Remissão no texto | Existe e diz aquilo? |
|---|---|
| `00_restricoes.md`, seção (b): RDC 622, art. 22 pede identificação no órgão licenciador e número da licença | sim (linhas 186–187) |
| `01_google_organico.md`: atualização central em curso desde 10/11/2026 | sim (linhas 113–116) |
| `01_google_organico.md`, seção 2.2: sinal de página de entrada é inferência do guia | sim (linhas 181–197) |
| `01_google_organico.md`, seção 8: consulta automática entre as práticas vedadas | sim (linha 367; também linha 172, na seção 2.1) |
| `02_google_maps_perfil.md`, seções 4.3 e 6: bloco depende de onde está quem busca e do horário | sim (proximidade e "aberto agora" em 4.3; base e alcance em 6) |
| `02_google_maps_perfil.md`, seção 8: sem o nome registrado não se distingue nome legítimo de inflado | sim (linhas 390–391) |
| `03_respostas_de_ia.md`, seção 2: Whitespark, 15%, 540 buscas, 3 cidades dos EUA, classe B | sim (linha 172) |
| `03_respostas_de_ia.md`, seção 7: tratar "ser citável" como parte do trabalho | sim, em sentido geral (seção 7.1) |
| `paginas_top10.md`: análise de dez páginas | sim |
| `PAINEL.md`, fila do owner: decisão sobre consulta automática | sim |
| `PAINEL.md`, "Desdobramentos": lista completa do Maps | sim (a linha do painel ainda diz que "entra na fila de reserva 1") |
| `PAINEL.md`, "Desdobramentos": prefixo dos números de licença | sim |
| `PAINEL.md`, "Desdobramentos": dados de cada perfil do mapa (linha 291 do texto) | **não há essa linha no painel** (achado 9) |
| `PAINEL.md`, "Desdobramentos": sugestões do Google, autocompletar (linha 468 do texto) | **não há essa linha no painel** (achado 9) |
| "pesquisa de 25/09" (GetNinjas e Habitissimo) | existe em `/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md`; o texto não dá o caminho (achado 16) |
| `serp_sp_ampliacao.md`, seções 4 e 8 | existem com esses assuntos; conteúdo não conferido (fora do item) |

## 10. Forma (ponto 9 do pedido)

- Português: sim. Nada dito como publicado, comprado, cadastrado ou enviado; "ninguém foi contatado" e "nada foi
  clicado" estão escritos.
- Caminhos absolutos: sim, salvo duas abreviações (`…parte2.csv`, `…parte2.md`, linhas 314–315) e os caminhos
  relativos na linha 3 das duas notas.
- Números com base, data, cidade e fonte: o cabeçalho dá a fonte geral (linha 21); os preços lidos em página trazem
  país e data. O ponto jurídico (seção 7.3, item 4) cita a fonte e não diz "levantamento, não parecer" (achado 16).

## 11. O que não conferi

- As outras 69 classes de domínio; a validade de qualquer número de licença; qualquer CNPJ.
- As contagens que vêm só das notas ("sem cheiro" em 7, links por página, agências) contra as páginas.
- A hora exata da verificação de robô, os lotes descartados, o total de cerca de 110 buscas, o fechamento da aba.
- A semente do `shuf` da repetição.
- Se a conta logada era a do owner; onde o navegador de fato estava.
- A afirmação da seção 10 de que os 40 bairros são "distritos da cidade" (não há fonte no projeto para isso).
- O conteúdo de `serp_sp_ampliacao.md` além dos títulos de duas seções.

## 12. Achados e correção pedida

Arquivo, salvo indicação: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`.

1. **Posição do navegador escrita como fato (linhas 42–43, 90–91, 107, 258–259).** O dado é: o rótulo de local só
   aparece junto do bloco de mapa (43 das 68 buscas com bloco); "São Paulo, SP" só apareceu em buscas com "são paulo"
   ou "sp" no termo (33 de 33); "Osasco, SP" apareceu em 10, 7 delas sem cidade no termo. Correção, linha 90–91:
   trocar "O Google atribuiu ao navegador uma posição na zona oeste da Grande São Paulo; o bloco de mapa reflete isso
   (seção 5)." por "O rótulo só aparece junto do bloco de mapa. 'São Paulo, SP' só apareceu em buscas com a cidade no
   termo (33 de 33) e pode ser o lugar da busca, não o do navegador; 'Osasco, SP' apareceu em 10, 7 delas sem cidade no
   termo. **Inferência:** o Google situou o navegador em Osasco ou perto; a posição real não foi registrada." Linha
   107: trocar "(zona oeste da Grande São Paulo)" por "(o Google exibiu 'Osasco, SP' em 10 buscas; a posição real não
   foi registrada)". Linhas 42–43: trocar "a cidade que o Google exibiu como localização do navegador em parte das
   buscas" por "a cidade que o Google exibiu como local em 10 das 79 buscas". Linha 259: trocar "a posição que o
   Google atribuiu ao navegador (zona oeste, perto de Osasco)" por "o local 'Osasco, SP' exibido em 10 buscas".
2. **Linha 425 (seção 9, item 5): regra sem grupo de comparação.** Um quarto dos perfis tem até 42 avaliações e o
   menor número lido é 1. Trocar "O mapa é de quem tem perfil com muitas avaliações, perto de quem busca." por "Os
   perfis vistos no bloco têm nota perto de 5 e mediana de 146 avaliações (um quarto tem até 42); não há grupo de
   comparação, então não se sabe se perfil com poucas avaliações fica de fora. 'Perto de quem busca' é inferência de
   uma só localização."
3. **Linha 415 (seção 9, item 1): "contra cerca de 150 domínios".** Os 157 incluem 11 de governo, 3 de rede social e
   os diretórios. Com página de local na amostra (pelo endereço) são 77 domínios; pela leitura, 50 dos 67 sites de
   serviço lidos. Trocar por "contra pelo menos 77 domínios que apareceram com página de local nesta amostra".
4. **Linha 399 (seção 8, linha "Anúncio"): "um anunciante em 58 das 79 buscas, com dois domínios"** afirma o que a
   seção 7.3 trata como indício. Trocar por "um anunciante em 58 das 79 buscas; um segundo domínio anunciante (8
   anúncios) traz o nome do primeiro no rodapé — indício, não prova de mesmo dono (seção 7.3)".
5. **Linha 388 (seção 8, linha 2) e linha 404.** O título "A página de bairro é texto de molde com o nome trocado"
   generaliza. Trocar por "Em parte dos sites lidos, a página de bairro traz sobra de texto de outro lugar (sinal de
   molde)". Na linha 404, "cerca de dez sites" está abaixo das notas: 6 na parte 1 e 5 na parte 2, mais os 4 domínios
   de bairro; trocar por "em 11 dos 71 sites lidos (15, contando os quatro domínios de nome de bairro)".
6. **Seção 8 (linhas 380–399): o título promete "primeiros colocados" e as linhas de "leitura" contam sobre os 67
   sites lidos.** Acrescentar, depois da tabela: "Só entre os primeiros: 27 domínios ficaram em 1º em alguma busca; 19
   deles são sites de serviço lidos — 15 com páginas por localidade, 19 com WhatsApp, 5 com número de licença. Entre
   os três primeiros ficaram 70 domínios; 44 são sites de serviço lidos — 33, 44 e 9, na mesma ordem. A proporção é
   parecida com a do conjunto (50, 65 e 12 de 67): nesta amostra esses traços não separam os primeiros dos demais."
7. **Seção 7.3, item 6 (linhas 373–378): falta um terceiro caso disputável.** cupimax.com.br e ratomax.com.br (2
   resultados cada; 0 e 1 entre os três primeiros) estão em "rede ou domínio satélite" por terem o mesmo molde e a
   mesma agência; as páginas relidas em 14/11 mostram marca sem identificação e um não cita o outro. Acrescentar:
   "cupimax.com.br e ratomax.com.br estão em 'rede ou domínio satélite' por inferência de mesmo molde; pelo que a
   página mostra seriam 'marca sem identificação vista' (4 resultados; a troca leva a linha de 51 para 47 e a outra de
   93 para 97)".
8. **Diretório é piso (linhas 33–35, 245–247 e 332).** Entre os 66 domínios não lidos há quatro com cara de lista ou
   guia pelo endereço e pelo título, além de coteibem e listazn, que o texto já cita: comerciosaopaulo.com.br (A10, 3º,
   "Guia das Melhores Dedetizadoras…"), znimovel.com.br (C03, 6º), encontrasantacecilia.com.br (D11, 9º) e
   catalogohospitalar.com.br (D18, 7º); há também um "especial publicitário" de g1.globo.com (B03, 4º). Acrescentar na
   linha 247: "Outros quatro domínios não lidos têm cara de lista ou guia (…), uma vez cada; 'diretório, 4%' é piso."
   Na linha 34, tirar pestwase da lista de diretórios (a seção 7.2 o classifica como programa de gestão).
9. **Remissões ao painel que não existem (linhas 291 e 468).** "Desdobramentos" de
   `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` (linhas 125–138) não tem linha para "abrir cada
   perfil do mapa" nem para "sugestões do Google (autocompletar, 'As pessoas também perguntam')". Correção: a sessão
   principal acrescenta as duas linhas ao painel, ou o texto troca "'Desdobramentos' no painel" por "não registrado
   no painel". A linha do painel sobre a lista completa do Maps ainda diz "entram na fila de reserva 1", e o texto
   (linhas 113–114) diz que a ampliação não a incluiu: alinhar o painel.
10. **Linhas 446 e 449–450 (seção 10): "21 termos informativos sem local" entre as combinações geradas.** Geradas com
    intenção informativa são 17; as outras 4 são consultas da coleta (H06 a H09). O gerador lista 23, e duas viraram
    preço e confiança por serem consultas da coleta (H05 e H03). Trocar por "17 termos informativos sem local (21 com
    os 4 da coleta)". Opcional: acrescentar os totais por tipo de local (bairro 2.289; zona 315; cidade 92; sem local
    25).
11. **Linhas 265–266 (seção 5) e linha 43.** "199 linhas… em outras 2 a nota aparece e o script não leu" soma 201, e
    as linhas são 202. Trocar por "em outras 3 o script não leu: em 2 a nota aparece (B06, com '1,1 mil'; D12, linha
    cortada logo depois da nota) e em 1 o nome ocupou os 80 caracteres (D16)". Na linha 43, trocar "96% das linhas"
    por "96% das 199 linhas com nota lida". Em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, linhas 218 e
    537, a coluna `titulo_ou_nome` carrega a nota e o resto da linha do perfil: declarar no texto ou corrigir a
    expressão em `monta_csv.py`.
12. **Linhas 57 e 547–548: "de 2 a 3,1 horas depois".** Os intervalos são 2,37; 2,34; 3,11; 3,02 e 2,70 horas. Trocar
    por "de 2,3 a 3,1 horas". **Linhas 30–32:** a frase junta 87% (grupo D, 20 buscas) e "21 das 32" (grupos D e E,
    onde a proporção é 84%). Trocar por "Nas 20 buscas só de bairro, 87%…; nas 32 buscas com bairro (com e sem praga),
    84%, e em 21 delas os três primeiros são todos desse tipo".
13. **Linhas 135–136 (seção 2.4).** "Na 80ª busca válida (H01…)" — a 80ª não foi válida; trocar por "Na 80ª busca
    (H01…), depois de 79 válidas". "23 minutos depois da última pausa longa (20:52)" omite três pausas de 80 a 100 s
    depois dela (20:57→20:58, 21:04→21:05, 21:11→21:13); trocar por "23 minutos depois da última pausa de mais de 2
    minutos (20:49→20:52); depois dela houve três pausas de 80 a 100 segundos".
14. **Linhas 98–100: a omissão da reclamação não alcança o histórico.** Os commits 343047c (`lote_03.jsonl`), eda20e2
    e cfd2330 (`serp_sp.csv`) ainda guardam o título e o endereço. Acrescentar "(o histórico do git guarda a versão
    anterior; reescrever o histórico é decisão do owner)" e pôr a pergunta na fila do owner do painel.
15. **Linha 117: "(…seção 4; não verificado)".** O registro de commits diz que a fila de reserva 1 foi fechada com
    correções do verificador (commit e436ae3). Atualizar o estado. Não abri o arquivo de verificação; a base é só a
    mensagem do commit.
16. **Forma.** Linhas 314–315: escrever os dois caminhos por inteiro
    (`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios_classe_parte2.csv` e
    `/home/ancastelo/pessoal/SEO_Project/docs/mercado/_notas_dominios_parte2.md`). Linha 246: dar o caminho da
    "pesquisa de 25/09" (`/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md`). Linha 369:
    acrescentar "(levantamento com fonte, não parecer)". Linha 3 de
    `/home/ancastelo/pessoal/SEO_Project/docs/mercado/_notas_dominios_parte1.md` e de `…parte2.md`: caminho absoluto.
17. **Linhas 85–86: "em geral 3 perfis, às vezes mais um patrocinado".** O patrocinado veio em 47 dos 68 blocos (69%).
    Trocar "às vezes" por "na maioria das vezes (47 de 68)".
18. **Linha 423 (seção 9, item 4): "quase nenhum site mostra preço".** As notas registram valor em 7 dos 71 sites
    lidos (3 na parte 1; 4 na parte 2, três deles em página de tabela de preço), e o grupo H mostra páginas de preço
    em primeiro. Trocar por "poucos sites lidos mostram valor (7 de 71), quase sempre 'a partir de'; a seção 12.3,
    item 3, enfraquece esta hipótese".
19. **Linhas 542–543 (seção 12.3, item 4).** "11 anúncios em 3 buscas": foram 5 em H01 e 6 em H02; H03 não teve
    anúncio. "O resultado é de dedetizadoras e de anúncios": dos 28 resultados, 11 são de dedetizadoras já
    classificadas, 7 de domínios não lidos e 3 de governo; o 1º de H01 é um diretório. A composição da página não
    testa se licença visível atrai busca. Trocar por "**Se licença visível atrai busca, não foi testado:** nas três
    buscas de confiança, 11 dos 28 resultados são de dedetizadoras já classificadas, 7 de domínios não lidos e 3 de
    governo; houve 11 anúncios em duas delas (H03 não teve). *(observação; volume não medido)*".
20. **Linha 389 (seção 8, "listas longas"): "em nove sites".** São os nove da parte 1; a parte 2 registra mais dois
    na mesma faixa (cerca de 200 e cerca de 130 links). Trocar por "em pelo menos onze sites".
