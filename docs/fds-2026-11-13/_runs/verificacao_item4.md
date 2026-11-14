# Verificação independente do item 4 — mapa do mercado de busca

- **Quando:** de sexta, 13/11/2026, 23:44, a sábado, 14/11/2026, 00:00 (Brasília; lido de `TZ=America/Sao_Paulo date`).
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu.
- **Veredito: APROVADO COM RESSALVAS.** O portão está cumprido em todas as partes. Os dez itens da seção 1 conferem.
  No sorteio de 12 números houve 1 falha (o limite de reprovação é mais de 2). Nas conferências obrigatórias há 1
  número errado (seção 5, "anos no mercado": 98, o certo é 156) e 1 frase que contradiz a própria tabela (seção 4.3).
  A classe dos 8 domínios sorteados confere em 8 de 8. Há 22 correções pedidas, no fim.
- **O que não foi feito:** nenhuma busca ao vivo, nenhum uso do navegador, nenhum script do projeto rodado, nenhum
  artefato editado. Não conferi o que só existia na sessão de coleta (lotes de teste descartados, hora em que a aba
  foi fechada, queda de conexão).
- **Artefatos conferidos no estado do commit `cfd2330`** (sem diferença em `docs/mercado` e `data` até `c6fda27`).
- **Scripts meus, só de leitura,** em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`:
  `verif_item4_contas.py`, `verif_item4_extra.py`, `verif_item4_sorteio.py`. O primeiro foi incluído num commit da
  sessão principal (`c6fda27`) enquanto eu trabalhava; depois disso corrigi nele uma linha (busca do id das
  repetições), que está sem commit. Não rodei `git` de escrita.

## 1. Portão, parte por parte

| Parte do portão | Situação | O que conferi |
|---|---|---|
| Buscas por praga | cumprido | Grupos B (13) e E (12) em `serp_consultas.csv`; todas com registro |
| Por bairro ou região | cumprido | Grupos C (5 regiões), D (20 bairros), E (12 praga × bairro) |
| "24 horas" | cumprido | Grupo G (6) e A07, A08 |
| Empresa × residência | cumprido | Grupo F (13) |
| Orgânico: quem aparece, tipo de página, classe, padrões | cumprido | Seções 4, 7 e 8; contas refeitas (itens (d) e (g) abaixo) |
| Mapa: quem aparece e padrões | cumprido | Seção 5; contas refeitas (item (e)) |
| Mapa: "empresa, diretório ou gerador de leads" | **cumprido com lacuna** | A seção 5 diz o que não foi observado nos perfis, mas não tem uma frase que responda a pergunta para o mapa (correção 21) |
| Cada busca com termo, hora, logado e local | cumprido | As 89 linhas de `serp_sp_registro.md` batem com os `.jsonl` em termo (`q`), hora (`nv`), logado (`lg`), local (`loc`), resumo de IA, anúncios, perfis, orgânicos e lote: 89 de 89, zero divergência. Termo planejado igual ao termo lido em 89 de 89 |
| Amostra declarada, não censo | cumprido | Linhas 4 a 6 e seção 2.3 (nove limites) |
| `palavras_chave.csv`: praga × bairro × intenção | cumprido com erro em 3 linhas | 1.260 linhas, 10 colunas; 3 linhas com local errado e 2 com intenção discutível (correções 19 e 20) |
| Coluna de volume "não medido" | cumprido | 1.260 de 1.260 |
| Método para medir | cumprido | Seção 10, quatro métodos, com "nenhum destes foi usado" e "não foi conferido em fonte nesta rodada" |

`serp_sp.csv`: 1.180 linhas (1.060 de A a G, 120 de H), igual ao que os `.jsonl` geram; termo, hora, logado, local,
domínio e caminho batem em todas as buscas.

## 2. Seção 1 ("Em uma página"), todos os números

| Item | Valor no texto | Recalculado | Resultado |
|---|---|---|---|
| 1 | 79 buscas; IA em 73; bloco em 68; anúncio de texto em 60; perfil patrocinado em 47; 12 sem anúncio | 73; 68; 60; 47; 12 | confere |
| 2 | 709 resultados, 157 domínios; 10 mais frequentes 39%; 20 mais frequentes 57%; 87% por local; 21 de 32 | 709; 157; 38,8%; 57,4%; 87,3% (grupo D); 21 de 32 (D e E) | confere. Ressalva: o 87% é só do grupo D e o 21 de 32 é de D e E; nos dois juntos são 84% (243 de 288) |
| 3 | ohub em 21 de 79, posição mediana 5; outros uma ou duas vezes; rede social e fórum 6 em 709 | 21; mediana 5; triider 2, reclameaqui 2, coteibem 1, pedegas 1, pestwase 1, listazn 1; 6 | confere |
| 4 | 77 domínios (86%); empresas identificadas 60%; sem identificação e satélites 20%; diretórios 4%; 12 de 67 | 610 de 709 = 86,0%; 424 = 59,8%; 144 = 20,3%; 25 = 3,5%; 12 de 67 | confere. Ressalva na expressão "77 mais frequentes" (correção 7) |
| 5 | 64 perfis em 202 linhas; três perfis 43%; 37 perfis nas buscas por bairro; nota mediana 5,0; 96% com 4,8 ou mais; mediana 146 | 64; 202; 86 de 202 = 42,6%; 37 (17 buscas do grupo D com bloco); 5,0; 192 de 199 = 96,5%; 146 | confere |
| 6 | anunciante em 58 de 79; patrocinado em 47 | 58; 47 | confere |
| 7 | 12 dos 16 resultados; sem bloco de mapa | B05: 5 de 9; E05: 7 de 7; bloco ausente nas duas | confere (a frase generaliza; correção 13) |
| 8 | sem número | — | — |
| 9 | IA 10 de 10; bloco em 2; sem anúncio em 3; 86 resultados, 60 domínios; 28 domínios novos; consulta pública em segundo; mesma página em primeiro nas três de preço | 10; 2 (H01, H10); 3 (H03, H07, H09); 86; 60; 28; sivisa em 2º em H03; novatec em 1º em H04, H05 e H10 | confere |
| 10 | 1º igual nas cinco; três primeiros domínios iguais nas cinco; três perfis em 3 e dois de três em 2 | 5; 5; 3 e 2 | confere |

Falhas na seção 1: **nenhuma**.

## 3. Sorteio de 12 números do resto do texto

Método: `verif_item4_sorteio.py` numera as frases com número da linha 60 em diante (linha de tabela ou frase de
parágrafo; fora caminhos, remissões e datas): 170 frases. Sorteio:
`seq 1 170 | shuf -n 12 --random-source=<(openssl enc -aes-256-ctr -pass pass:"verif-item4-20261113" -nosalt </dev/zero)`.
A primeira versão do numerador contava o marcador de lista ("1.") como frase; corrigi antes de conferir qualquer valor
e o sorteio deu os mesmos doze números.

| Nº | Linha | Frase | Valor no texto | Recalculado | Resultado |
|---|---|---|---|---|---|
| 154 | 468 | Grupo H por classe | 27; 16; 12; 8; 6; 6; 4; 3; 2; 2 | 27; 16; 12; 8; 6; 6; 4; 3; 2; 2 (soma 86) | confere |
| 158 | 480 | dedetizadora.srv.br no grupo H | 7 de 86 resultados; 6 de 10 buscas | 7; 6 | confere |
| 48 | 183 | Grupo B, metade dos resultados | 9 de 45 domínios | 9 de 45 (59 de 116) | confere |
| 134 | 428 | Páginas lidas por domínio | de 1 a 3 | 1 em 11 domínios, 2 em 43, 3 em 23 | confere |
| 104 | 307 | Classe "não lido" | 66 domínios; 70 (10%); 18 (8%); 4 (5%) | 66 (62 de 1 aparição, 4 de 2); 70 = 9,9%; 18 = 7,6%; 4 = 5,1% | confere |
| 19 | 116 | Corte dos títulos | 60 nos lotes 1 e 2; 34 nos lotes 3 a 8; caminho 50 | 60; 34 nos lotes 4 a 8; **36 no lote 3** (3 títulos com 35 ou 36 caracteres, em D06 e D08); caminho 50 | **falha** (pequena) |
| 63 | 205 | Treze domínios em 5 ou mais das 20 buscas por bairro | 11; 10, 10, 10; 8; 7, 7; 6, 6, 6, 6; 5, 5 | iguais | confere nos números. A frase "cada vez com a página daquele bairro" tem 3 exceções (correção 5) |
| 66 | 220 | Telefone no título | 54 (8%); 20 (8%) | 54 = 7,6%; 20 = 8,4%, contando também a máscara cortada pelo limite do título ("[t", "[te", "[tel"); só "[tel]" inteiro dá 46 e 17 | confere |
| 143 | 452 | H07 | IA sim; 0 anúncios; sem bloco; br.envu.com | iguais | confere |
| 169 | 510 | Repetição de B04 | 20:34; 23:36; sim; sim; 9 de 9; 2; Osasco nas duas; 2 → 1 | iguais | confere |
| 113 | 350 | Texto de molde com nome trocado | cinco exemplos; notas parte 1 item (b)1 e parte 2 item (b)2 | os cinco estão nas notas, nesses itens | confere |
| 37 | 155 | Total da seção 3 | 79; 73 (92%); 68 (86%); 60 (76%); 47 (59%) | 73 = 92,4%; 68 = 86,1%; 60 = 75,9%; 47 = 59,5% | confere |

**Falhas no sorteio: 1 em 12** (nº 19). Não reprova.

## 4. Conferências obrigatórias

**(a) Seção 2.1 — confere.** Planejadas e feitas por grupo: A 10, B 13, C 5, D 20, E 12, F 13, G 6, H 10; total 89
e 89. Nenhuma busca planejada sem registro, nenhum registro fora do plano.

**(b) Seção 2.2, intervalos — confere.** Recalculado de `nv`, em ordem de hora:

| Janela | Buscas | Intervalos | Mediana | Mínimo | Máximo | Abaixo de 20 s |
|---|---|---|---|---|---|---|
| 20:26:51 a 21:16:03 (A a G) | 79 | 78 | 28 s | 17 s | 224 s | 3: B11→B12 (18 s), D02→D03 (19 s), E02→E03 (17 s) |
| 23:18:29 a 23:37:15 (H e repetições) | 15 | 14 | 76 s | 67 s | 124 s | 0 |

Os três intervalos e os valores são os que o texto declara. Localização exibida: 33, 10 e 36 na amostra principal;
2 e 8 no grupo H: confere. Logado em 89 de 89 e nas 5 repetições: confere.

**(c) Seção 3 — confere.** As sete linhas da tabela e o total batem (A 10/10/8/8; B 13/11/11/6; C 4/5/5/5;
D 16/17/9/14; E 11/8/10/6; F 13/12/11/6; G 6/5/6/2). As 6 buscas sem resumo de IA e as 11 sem bloco são as listadas.

**(d) Seções 4.1 e 4.2 — confere.** 709 resultados e 157 domínios; 5 mais frequentes 22,8%, 10 mais frequentes
38,8%, 20 mais frequentes 57,4%; 83 domínios com uma aparição; primeira posição 16, 12, 6, 6, 5, 4, 4; os dez
domínios com os três números de cada um; metade dos resultados por grupo (10 de 37, 9 de 45, 6 de 22, 12 de 66, 17 de
62, 7 de 47, 8 de 31). Tabela 4.2: os 42 percentuais batem com arredondamento. Três primeiros: 104, 85, 34, 10, 3, 1.
21 de 32; 249 de 316. Seção 4.3: os dez números batem com as regras "[t", "24 h" e "preç ou a partir" (que pegam
palavra cortada); a frase que vem depois da tabela não bate (correção 2). Seção 4.4: ohub 22 em 21, posições 1 a 8,
mediana 5; governo 23, 12 em escorpião; sivisa 1. Imprecisões: correções 4, 5 e 6.

**(e) Seção 5 — confere, com 1 número errado.** 202 linhas, 64 perfis, 68 buscas; 30, 29, 27 (42,6%); 10, 8, 6;
grupo D com 17 buscas e 37 perfis, líderes 5, 3, 3; cidade exibida 114, 32, 1 e 55 sem cidade; 199 linhas com nota
lida, mediana 5,0, mínima 4,3, 96,5% com 4,8 ou mais; 61 perfis com número, mediana 146, quartis 42,5 e 313,5, máximo
867; 51 de 64 nomes com palavra de serviço (regra "dedetiz, pragas ou cupi"). **"Anos no mercado": o texto diz 98 de
202; são 156 de 202** — 58 linhas dos lotes 1 e 2, onde está escrito "anos no mercado", e 98 dos lotes 3 a 7, onde o
script abreviou para "35a". A conta do texto só pegou a forma abreviada (correção 1). "12 nomes com local ou 24h":
inconclusivo, dá de 10 a 13 conforme a regra, que não está escrita (correção 10).

**(f) Seção 6 — confere.** 102 anúncios em 60 buscas; brasiltechs.com em 58 buscas; 8; 2; 1, 1, 1; 31 sem domínio;
patrocinado em 47 buscas, sempre o mesmo (4,3; 166); 12 buscas sem anúncio nenhum.

**(g) Seção 7.2 contra `serp_dominios.csv` — confere.** As dez linhas e as quatro colunas batem (domínios 27, 11,
15, 14, 3, 11, 3, 6, 1, 66 = 157; resultados somam 709; três primeiros somam 237; primeira posição soma 79). As
contagens de `serp_dominios.csv` batem com as dos `.jsonl` nos 157 domínios. 77 domínios lidos cobrem 610 de 709.
67 sites de serviço, 12 com número de licença (os 11 da classe e cupim.eco.br, que está em "satélite"); 50 com
páginas por local; 65 com WhatsApp; 35 de 71 com "24 horas" (20 de 34 na parte 1 e 15 de 37 na parte 2); 14 com
licença afirmada sem número; 28 das 37 primeiras posições em dois domínios. O anexo `serp_sp_dominios.md` traz a
mesma tabela.

**(h) Seção 12 contra `lote_08.jsonl` e `serp_sp.csv` — confere.** As dez linhas da tabela 12.1 (resumo de IA,
anúncios, bloco, primeiro resultado); 10 de 10, 2 de 10, 7 de 10; 26 anúncios, 11 e 8; 86 resultados, 60 domínios,
28 novos com 30 resultados (34,9%); tipos 46, 20, 8, 7, 3, 2; 316 de 709 = 44,6% contra 2 de 86; classes (dez
valores); tabela por tipo de busca (28, 26, 32 resultados; 11, 12, 3 anúncios; 11, 7 e 3; 14 e 5; 16 e 7);
dedetizadora.srv.br 7 e 6; H02 com 3, 5 e 1. Em `serp_sp.csv`, o grupo H tem 120 linhas (86, 26, 6, 2).

**(i) Seção 13 contra `repeticao_01.jsonl` — confere.** O sorteio das cinco se reproduz com a semente declarada
(`shuf -n 5` sobre os 79 ids de A a G, fonte aleatória `openssl enc -aes-256-ctr`): F10, G01, A03, B04, D16.

| Busca | Horas | 1º igual | Três primeiros domínios iguais | Domínios em comum | Perfis em comum | Local | Anúncios |
|---|---|---|---|---|---|---|---|
| F10 | 21:10:16 → 23:32:23 | sim | sim | 7 de 7 | 3 | São Paulo, SP nas duas | 2 → 2 |
| G01 | 21:13:20 → 23:33:41 | sim | sim | 8 de 9 | 3 | São Paulo, SP nas duas | 2 → 2 |
| A03 | 20:27:57 → 23:34:48 | sim | sim | 8 de 9 | 3 | São Paulo, SP nas duas | 2 → 2 |
| B04 | 20:34:51 → 23:36:05 | sim | sim | 9 de 9 | 2 | Osasco, SP nas duas | 2 → 1 |
| D16 | 20:55:18 → 23:37:15 | sim | sim | 9 de 9 | 2 | Osasco, SP nas duas | 0 → 2 |

Tudo igual ao texto. A03 foi repetida 3,1 horas depois; o texto diz "de 2 a 3 horas".

## 5. Classe de 8 domínios, relida na página

Sorteio: os 77 domínios com base "leitura" em `serp_dominios.csv`, na ordem do arquivo;
`shuf -n 8` com a semente "verif-item4-dominios-20261113". Li a página inicial de cada um com a ferramenta de leitura
de página, que resume por um modelo pequeno; pedi que dissesse se o rodapé veio. Nenhum telefone, nome de pessoa ou
número de CNPJ foi gravado.

| Domínio | Classe no arquivo | Licença / CNPJ no arquivo | O que a página inicial mostrou | Rodapé veio? | Resultado |
|---|---|---|---|---|---|
| santanadedetizadora.com.br | marca sem identificação vista | não visto / não visto | Dedetizadora; sem número de licença, sem CNPJ, sem endereço; links para um domínio de teste | não (texto parece cortado) | confere, com a ressalva do rodapé |
| eccocleandedetizacao.com.br | empresa com número de licença | sim / não visto | Dedetizadora; "CEVS" com número no rodapé; endereço em São Paulo; sem CNPJ | sim | confere |
| reclameaqui.com.br | não abriu | — | HTTP 403 também na minha tentativa | — | confere |
| higitec.com.br | empresa identificada, sem número visto | não visto / não visto | Desentupidora e dedetizadora; "devidamente licenciadas", sem número; endereço em São Paulo; "profissionais filiados" e "Seja Parceiro" | sim | confere |
| biosolucoes.app.br | rede ou domínio satélite | não visto / sim | Dedetizadora; licença afirmada sem número; CNPJ exibido; "Sites Parceiros" com 5 domínios; outro nome de empresa nos links | sim | confere |
| universoambiental.eco.br | empresa com número de licença | sim / não visto | Inicial: só "dedetizadora licenciada", sem número. O arquivo registra o número na página de preço de Osasco: abri essa página e ela mostra "CEVS" com número; sem CNPJ, sem endereço | sim | confere (o número não está na inicial) |
| exterminex.com.br | marca sem identificação vista | não visto / não visto | Empresa de controle de pragas; sem licença, CNPJ ou endereço; "Área do cliente" em outro domínio | sim | confere |
| triider.com.br | diretório ou marketplace | não visto / não visto | "conectando clientes e profissionais"; orçamento, contratação e pagamento no site | sim | confere |

**8 conferem, 0 não confere, 0 inconclusivo.** Uma observação de método: universoambiental.eco.br está em "empresa
com número de licença" sem CNPJ, razão social nem endereço vistos, e cupim.eco.br, que mostra o mesmo número, está em
"satélite". As notas da parte 1 chamam essa classe de disputável; o texto principal não diz (correção 22).

## 6. O que a amostra não sustenta

Li o texto inteiro atrás de causa, regra, "sempre" e afirmação sobre empresa.

- **Não achei** "ranqueia porque", "não tem licença" nem acusação a empresa. As classes dizem "sem número de licença
  visto"; a seção 7.1 diz que "não visto" não prova ausência; a seção 7.3, item 5, diz que não é prova de que exibir a
  licença melhore a posição.
- **Seção 4.3, linhas 226 e 227 — frase falsa pela própria tabela.** "Nenhum desses termos é mais frequente entre os
  três primeiros do que no conjunto": "24 horas" é 10,0% no conjunto e 11,8% nos três primeiros; "preço", 4,2% e
  5,5%; telefone, 7,6% e 8,4%. Só "melhor" e "orçamento" são menos frequentes no topo.
- **Seção 7.3, item 2, linha 318 — "Nenhum outro site da amostra diz que repassa pedidos a terceiros".** Só 77 dos
  157 domínios foram lidos, em 1 a 3 páginas. E as notas da parte 2 registram "Contamos com muitos profissionais
  filiados" e "Seja Parceiro" (higitec.com.br, que eu também vi) e "franquias" (jupitersp.com.br).
- **Seção 9, item 6, linha 388 — "quase sempre abre com resumo de IA".** A ordem vertical não foi registrada (seção
  2.3, item 4); o script só acha o rótulo em qualquer ponto da página.
- **Seção 1, item 7, linha 46 — "Busca informativa de risco à saúde é do governo".** São duas buscas, as duas de
  escorpião. Na de mosquito da dengue há 1 resultado de governo em 9.
- **Seção 1, item 5, linha 40 — "muda … com o lugar de quem busca".** Houve um só ponto de busca; a seção 5 marca
  isso como inferência, a seção 1 não.
- **"Páginas de entrada".** O texto não chama as páginas por bairro de "páginas de entrada": a seção 2.3, item 8, diz
  "não afirmo". Mas a seção 8 (linhas 363 a 369) diz que o padrão "encosta no que a política descreve como página de
  entrada" e que "essas páginas estão nos primeiros lugares", sem marca de inferência, e as duas leituras oferecidas
  partem de que as páginas são do tipo que a política veda. Falta a terceira: que não sejam. A base é texto de outro
  lugar visto em cerca de dez sites; duas páginas do mesmo site não foram comparadas. A seção 2.3, item 8, ainda diz
  "Não li as páginas", o que deixou de valer depois da seção 7.
- **Seções "Busca com bairro pede página do bairro" (linha 203) e "Busca de empresa pede página de segmento" (linha
  212).** Título em forma de regra; o corpo traz a contagem. Ressalva leve.
- **Seção 7.3, item 3, linha 327 — "uma só empresa em dois domínios".** A base é o rodapé do segundo site; a seção
  7.1 diz que "mesmo dono" não foi provado em caso nenhum. Ressalva leve: dizer "pelo rodapé".
- **Marcas das seções 9 e 12.3.** Seção 9: itens 1, 2, 4, 5, 6, 7 e 8 marcados. Item 3 marcado só "(observação)",
  mas "um comparador novo disputaria esse lugar" é inferência. Seção 12.3: os quatro itens marcados; no item 1, "é
  onde um guia de praga … disputaria lugar" é inferência sob a marca "(observação de 4 buscas)".

## 7. Regras de coleta

- **Limite de 600:** o texto declara cerca de 110 (89 válidas, 5 repetições, 1 barrada, cerca de 15 perdidas). As 94
  com registro eu contei; as 15 perdidas e a barrada não têm bruto e não são conferíveis.
- **20 segundos:** **a regra não foi cumprida em três intervalos** (17, 18 e 19 s), que o texto declara, e nos lotes
  de teste descartados das 20:10 às 20:22, que o texto declara sem dizer quantos. Fica para o owner saber; não
  esconde nada.
- **Verificação de robô:** declarada às 21:16, não resolvida. A última busca válida é G06, às 21:16:03 (lida às
  21:16:36). **Não há registro entre 21:17 e 23:17** nos lotes nem nas repetições. A retomada é H01, às 23:18:29: a
  pausa passou de 2 horas por cerca de 2 minutos. Uma só ocorrência.
- **"Cerca de 28 minutos de coleta contínua" (linha 129):** não reproduzi. A janela inteira tem 49 minutos; do fim
  do intervalo mais longo (D10→D11, 20:52:56) até 21:16 são 23 minutos (correção 8).
- **Anúncio clicado ou contato:** nenhum sinal. O coletor só lê atributos da página e não tem chamada de clique; as
  notas dizem que os dois anunciantes foram abertos pelo endereço digitado, pela ferramenta de leitura.
- **Telefone e nome de pessoa:** os dois padrões pedidos (`\(?\d{2}\)?\s?9?\d{4}[-\s]?\d{4}` e `0800`) dão zero
  ocorrência em `serp_sp.csv`, nos 9 `.jsonl`, em `serp_dominios.csv`, nas duas partes, em `palavras_chave.csv`, no
  texto, nos dois anexos e nas duas notas (a única ocorrência é a própria expressão dentro de `coletor.js`). Há 57
  "[tel]" nos `.jsonl`. Nenhum e-mail, CPF ou CNPJ. A coluna `responsavel_tecnico_citado` só tem "sim" e "não
  visto". Nomes de perfil são nomes de empresa. Os números de licença nas notas são de empresa.
- **Um caso de fronteira:** `serp_sp.csv` e `lote_03.jsonl` (busca D05, posição 7) guardam o título e o endereço de
  uma reclamação de consumidor no Reclame Aqui (duas palavras, sem nome de pessoa). Não é texto de avaliação copiado
  por inteiro; registro para a sessão principal decidir se mascara.

## 8. Mapa de palavras-chave

- 1.260 termos; 89 da coleta e 1.171 gerados; contratar 421, urgência 371, preço 368, confiança 79, informativa 21;
  89 coletados, com id e termo iguais aos dos `.jsonl`; volume "não medido" em 1.260: **confere**.
- 14 serviços, 26 locais (cidade, 5 regiões, 20 bairros), 21 informativos sem local: confere com o CSV e com
  `gera_palavras_chave.py`.
- Duplicados: nenhum, nem ignorando caixa, espaço e acento.
- Sorteio de 15 linhas (`seq 1 1260 | shuf -n 15`, semente "verif-item4-palavras-20261113"): linhas de dados 42,
  238, 249, 251, 274, 297, 428, 568, 622, 666, 775, 862, 1022, 1143, 1216. **15 de 15 coerentes** em praga, local e
  intenção.
- Fora do sorteio, li as 89 linhas da coleta e achei **3 com local errado** e 2 com intenção discutível:
  "dedetizadora zona sul sp" (C01), "dedetização lapa sp" (D06) e "dedetizadora penha sp" (D15) estão como cidade /
  são paulo, porque o script testa "são paulo" (pelo " sp" final) antes de "zona sul", "lapa" e "penha"; "quanto
  custa dedetização são paulo" (A09) está como contratar; "melhor dedetizadora são paulo" (A10) está como contratar,
  enquanto as combinações geradas "melhor dedetizadora …" estão como confiança.
- Os quatro métodos de medir volume estão descritos como não usados e não conferidos em fonte: confere.

## 9. Remissões

| Remissão no texto | Existe e diz aquilo? |
|---|---|
| `00_restricoes.md`, seção (b): RDC 622, art. 22 | sim (linhas 186 e 187: identificação nos órgãos licenciadores e número da licença) |
| `01_google_organico.md`: atualização central desde 10/11/2026 | sim (linhas 113 a 116) |
| `01_google_organico.md`, seção 8: consulta automática | sim (linha 367, na seção 8) |
| `01_google_organico.md`, seção 2.2: sinal "só muda o nome do bairro", inferência do guia | sim (linhas 181 a 190) |
| `02_google_maps_perfil.md`, seções 4.3 e 6: proximidade e horário | sim |
| `02_google_maps_perfil.md`, seção 8: nome com palavra-chave | sim |
| `02_google_maps_perfil.md`, seção 6: a região da base decide | sim ("Consequência para São Paulo") |
| `03_respostas_de_ia.md`, seção 2: Whitespark, 15% | sim (linha 165), com país (Estados Unidos) e ano no texto. As 540 buscas são o total do estudo, locais e informativas; o texto dá a entender que são todas de "serviço + cidade" (correção 18) |
| `03_respostas_de_ia.md`, seção 7: ser citável | sim (seção 7.1) |
| `PAINEL.md`: decisão sobre consulta automática | sim (linha 39) |
| `docs/mercado/paginas_top10.md` | existe |

## 10. Forma

Português; caminhos absolutos; números com base ("de 79", "de 709", "de 237"); país, cidade, data e fonte no
cabeçalho. Nada publicado, comprado, cadastrado ou enviado.

## 11. Tudo o que não bate

1. Seção 5: "anos no mercado" em 98 linhas; são 156.
2. Seção 4.3: a frase depois da tabela contradiz a tabela.
3. Seção 2.3, item 6: título em 34 caracteres nos lotes 3 a 8; no lote 3 há 3 títulos com 35 ou 36.
4. Seção 4.2: rentokil.com com "5 resultados" no grupo F; no grupo F são 3 (1 em A e 1 em B).
5. Seção 4.2: "cada vez com a página daquele bairro" tem 3 exceções em 98 resultados.
6. Seção 4.4: a lista das buscas com resultado de governo omite "desratização são paulo".
7. "Os 77 domínios mais frequentes": não são exatamente os mais frequentes.
8. Seção 2.4: "cerca de 28 minutos" não se reproduz.
9. Seção 5: "199 linhas com nota" são as 199 que o script leu; 2 das outras 3 têm nota à vista.
10. Seção 5: a regra dos "12 nomes com local ou 24h" não está escrita.
11. Seção 7.3, item 2: "nenhum outro site da amostra".
12. Seção 9, item 6: "abre com".
13. Seção 1, item 7: regra tirada de duas buscas.
14. Seção 1, item 5: inferência sem marca.
15. Seções 2.3 (item 8) e 8: "páginas de entrada".
16. Seção 7.3, item 3: seis domínios de bairro, dos quais 2 estão na classe "não lido".
17. Seção 8, linha 351: "cerca de 600 na inicial de um deles" — o site dos 600 não é um dos nove.
18. Seção 3: 540 buscas.
19. `palavras_chave.csv`: 3 linhas com local errado.
20. `palavras_chave.csv`: 2 linhas com intenção discutível.
21. Seção 5: falta a resposta "empresa, diretório ou gerador de leads" para o mapa.
22. Seção 7: classe disputável não dita no texto.

## 12. Correções pedidas

Arquivo, quando não dito: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`.

1. **Linha 256:** trocar "98 das 202 linhas" por "pelo menos 156 das 202 linhas" (58 nos lotes 1 e 2, 98 nos lotes
   3 a 7; é piso, porque a linha do perfil é cortada em 110 ou 80 caracteres). A faixa "de 3 a 35 anos" está certa.
2. **Linhas 226 e 227:** trocar a frase por: "'24 horas' (10% no conjunto, 12% nos três primeiros), 'preço' (4% e
   5%) e telefone (7,6% e 8,4%) são um pouco mais frequentes no topo; 'melhor' (4% e 3%) e 'orçamento', menos. As
   diferenças são de poucos resultados: nesta amostra não há sinal claro de que esses termos acompanhem posição
   melhor. É contagem, não teste." Dizer na legenda que a contagem inclui palavra cortada ("[t", "24 h", "preç").
3. **Linha 116:** "em 34 nos lotes 3 a 8 (três títulos do lote 3 têm 35 ou 36)".
4. **Linha 213:** "rentokil.com, 3 resultados no grupo F (5 na amostra, com 1 em A e 1 em B)".
5. **Linha 205:** trocar "cada vez" por "quase sempre"; as exceções são a página inicial de
   primordialdedetizacao.com.br na busca da Bela Vista e a página da cidade de ohub.com.br nas buscas do Ipiranga e
   de Campo Limpo.
6. **Linhas 237 e 238:** acrescentar "desratização" à lista das buscas com resultado de governo.
7. **Linhas 15 e 16, 36, 279 a 281:** trocar "os 77 domínios mais frequentes" por "77 domínios: os 48 com 3 ou
   mais aparições (fora governo e rede social, classificados pelo domínio), 18 dos 22 com 2 aparições e 11 com 1
   (domínios de bairro, diretórios e anunciantes)". A cobertura de 610 de 709 (86%) está certa.
8. **Linhas 129 e 130:** dizer de que hora a que hora vão os "cerca de 28 minutos", ou trocar por "49 minutos
   depois do início (20:26), 23 minutos depois da última pausa longa (20:52)".
9. **Linha 253:** "das 199 linhas em que o script leu nota e número (em outras 2 a nota aparece e o script não
   leu)".
10. **Linhas 257 e 258:** escrever a regra das duas contagens (51 nomes: "dedetiz", "pragas" ou "cupi"; 12 nomes:
    quais palavras de local) ou listar os 12 nomes.
11. **Linha 318:** trocar por "Nenhum outro dos 71 sites lidos diz, nas páginas abertas, que repassa pedidos a
    terceiros; dois falam em 'profissionais filiados' e em 'franquias' sem dizer como funciona (higitec.com.br,
    jupitersp.com.br)."
12. **Linha 388:** trocar "quase sempre abre com resumo de IA (92%)" por "tem resumo de IA em 92% das buscas; a
    posição dele na página não foi registrada".
13. **Linha 46:** trocar o título por "Nas duas buscas de escorpião, o resultado é do governo".
14. **Linha 40:** acrescentar "(a parte do lugar de quem busca é inferência: houve um só ponto de busca)".
15. **Linhas 119 a 121 e 363 a 369:** na seção 2.3, item 8, trocar "Não li as páginas" por "A coleta não leu as
    páginas; a leitura da seção 7 abriu de 1 a 3 por domínio". Na seção 8, marcar o parágrafo como inferência, dizer
    a base (texto de outro lugar visto em cerca de dez sites; duas páginas do mesmo site não foram comparadas) e
    acrescentar a terceira leitura: as páginas podem não ser o que a política veda.
16. **Linhas 319 a 323:** dizer que, dos seis domínios de bairro, quatro foram classificados e dois (Higienópolis e
    Vila Mariana) foram abertos só para comparar e estão em "não lido" na tabela; os "29 domínios" incluem só os
    quatro.
17. **Linha 351:** trocar "na inicial de um deles" por "na inicial de outro site".
18. **Linhas 163 e 164:** "(540 buscas no total, locais e informativas, 6 ramos, 3 cidades…)".
19. **`/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`, linha 63, e
    `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, linhas 25, 35 e 44:** testar zona e bairro antes
    de "são paulo". Valores certos: linha 25, zona / zona sul; linha 35, bairro / lapa; linha 44, bairro / penha.
20. **`gera_palavras_chave.py`, linha 44, e `palavras_chave.csv`, linhas 10 e 11:** "quanto custa…" como preço e
    "melhor dedetizadora são paulo" como confiança, igual às combinações geradas. Depois de regerar, a seção 10
    (linha 409) passa a: contratar 419; urgência 371; preço 369; confiança 80; informativa 21.
21. **Seção 5 (depois da linha 260):** acrescentar a resposta do portão para o mapa: o bloco só mostra perfis de
    empresa (nenhum diretório); se cada perfil é de quem executa não foi conferido (perfis não abertos); quais dos
    perfis mais frequentes têm site classificado na seção 7.
22. **Seção 7.2 ou 7.3:** dizer que duas classes são disputáveis segundo as notas (universoambiental.eco.br, com
    número de licença e sem CNPJ, razão social ou endereço vistos; biosolucoes.app.br) e que cupim.eco.br mostra o
    mesmo número e está em "satélite".

Para o painel do owner, sem pedir mudança no texto: os três intervalos abaixo de 20 segundos e os lotes de teste
descartados são descumprimento declarado da regra de intervalo.
