# Segunda passada — fila de reserva, tarefa 1 (ampliação da amostra de buscas e do mapa de termos)

- **Quem:** revisor independente (subagente em contexto limpo), sem a conclusão de ninguém. Não abri nenhum arquivo
  `verificacao*` nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só listei os
  nomes) e desconsiderei o que os artefatos dizem sobre verificações anteriores.
- **Quando:** sábado, 14/11/2026, das 02:01 às 02:14 (Brasília; horas lidas de `TZ=America/Sao_Paulo date`: início
  02:01:25; última leitura, com este arquivo já gravado, 02:14:45).
- **Veredito: APROVADO COM RESSALVAS.** Portão cumprido nas três partes. Sorteio: **0 falha em 12** (duas com
  ressalva de redação). Resumo: todos os números do resumo e do cabeçalho (28 linhas na tabela da seção 4) batem com
  o bruto e com o CSV pelo método do documento; um deles (96 perfis) está 1 acima do real por um nome mal separado. Fora do sorteio há **uma afirmação falsa** no corpo
  (achado 1) e 13 achados de leitura.
- **Buscas ao vivo:** não repeti nenhuma. Só a sessão principal usa o navegador; não usei navegador, busca na web nem
  ferramenta externa. Tudo o que está aqui vem dos arquivos locais.

## 1. O que abri

| Arquivo | Como |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | inteiros |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (314 linhas) | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md` (40 linhas de busca) | inteiro, e por script |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/ampliacao_01.jsonl` a `ampliacao_04.jsonl` (40 registros) e `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_02.jsonl` (5) | por script, todos os registros |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv` (537 linhas) e `/home/ancastelo/pessoal/SEO_Project/data/serp_consultas_ampliacao.csv` (40) | por script, todas as linhas |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py` e `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` (funções `fx` e `fx2`) | lidos; **não rodei** o primeiro, porque ele regrava o CSV e o registro |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (2.721 termos) e `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py` | por script e lido; não rodei o gerador (ele regrava o CSV) |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, `/home/ancastelo/pessoal/SEO_Project/data/serp_consultas.csv`, `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`, `lote_*.jsonl` e `repeticao_01.jsonl` | por script, para as comparações com o item 4 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` | só os trechos citados (seções 2.2 a 2.4, títulos de seção, linhas com os números comparados) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` | só as linhas sobre o limite de buscas |
| histórico do git (`git log`, `git show`, só leitura) | datas dos lotes brutos, versões antigas do mapa de termos, telefone em versão antiga |

Meus scripts (biblioteca padrão, só leitura; não gravam nada):
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res1_comum.py`, `v2res1_registro.py`,
`v2res1_contas.py`, `v2res1_dado_pessoal.py` e `v2res1_palavras.py`, na mesma pasta. Eles refazem a transformação
bruto → linhas por conta própria e comparam com o CSV. Conferi por `git diff` que nenhum artefato mudou.

## 2. Portão, parte por parte

Portão (`RODADA.md`, fila de reserva 1): "Ampliar o mapa de palavras-chave e a amostra de buscas para mais bairros e
pragas, dentro do limite de buscas."

| Parte | Cumprida? | O que vi |
|---|---|---|
| Amostra com mais bairros | sim | 20 buscas de bairro (grupo I), uma por bairro; nenhum dos 20 nomes aparece em `data/serp_consultas.csv` (item 4). Mais 10 buscas de praga × bairro novo (grupo J) |
| Amostra com mais pragas | sim | 10 buscas do grupo K: seis pragas que não estavam nas consultas do item 4 (traças, marimbondos, moscas, lacraias, broca de madeira, piolho de pombo) e quatro termos novos de praga já buscada (mosquitos, ratos, cupim de solo, fumacê). Conferi por busca de texto em `data/serp_consultas.csv` |
| Mapa de palavras-chave ampliado | sim | de 1.260 para 2.721 termos (versões do git: 1.261 linhas até 14/11 00:08; 2.722 linhas em 14/11 01:11, com cabeçalho); 40 bairros (eram 20) e 16 pragas na grade (entraram moscas, lacraias, marimbondos e brocas); `volume` = "não medido" nas 2.721 |
| Dentro do limite: quantidade | sim | 40 buscas + 5 repetições nos brutos desta tarefa. Total declarado da rodada: cerca de 155 de 600. Nos brutos há 139 registros (89 + 5 do item 4, 40 + 5 daqui); os outros cerca de 16 (1 barrada e cerca de 15 perdidas em testes do item 4) não têm bruto e **não são conferíveis** |
| Dentro do limite: intervalo | sim | entre navegações: mínimo 72 s, mediana 77 s, máximo 190 s; nenhum abaixo de 20 s. Entre o fim de uma leitura e a navegação seguinte: mínimo 59 s. Repetições: 77, 76, 73 e 73 s; 403 s depois da última das 40. A última busca de 13/11 nos brutos foi às 23:37:15; a primeira daqui, à 00:12:10 |
| Verificação de robô | sem sinal nos arquivos | os 40 identificadores planejados estão nos brutos, na ordem, sem buraco; o coletor lança erro na página de "tráfego incomum". A única ocorrência da rodada é a do item 4 (21:16 de 13/11; retomada às 23:18, 2 horas depois). Que **não houve** ocorrência aqui é afirmação de quem coletou; pelos arquivos só dá para dizer que nada a contradiz |

## 3. Registro: bruto × CSV × registro × lista de consultas

Script `v2res1_registro.py`, para as 40 buscas, campo a campo:

| Conferência | Resultado |
|---|---|
| termo do bruto = termo da lista de consultas = termo do CSV = termo do registro | 40 de 40 |
| hora da navegação (hh:mm:ss) igual no bruto, no CSV e no registro | 40 de 40 |
| local exibido igual nos três ("São Paulo, SP" em 5, "Osasco, SP" em 5, nenhum em 30) | 40 de 40 |
| logado = sim; presença do resumo de IA; data 2026-11-14; grupo | 40 de 40 |
| número de anúncios, de perfis no bloco, de patrocinados e de orgânicos | 40 de 40 |
| conteúdo linha a linha (domínio, caminho, título, nome, nota, avaliações) do CSV = bruto | 537 de 537 linhas |
| ordem das camadas e os quatro valores em pixels do registro = bruto | 40 de 40 |
| tipo de página do CSV = regra do script reaplicada por mim | 352 de 352 |
| coerência interna do bruto (camada presente ↔ posição medida; janela de 945 pixels; leitura depois da navegação) | 40 de 40 |
| ordem do arquivo = ordem das horas | sim |
| intervalo abaixo de 20 s | nenhum |
| sorteio das 5 repetições: refiz o comando da seção 11 | deu J01, I08, I20, I04, I14 — as cinco repetidas, na mesma ordem |
| repetições: mesmo termo; 31,1 a 60,4 minutos depois da primeira vez | 5 de 5 |

Ressalva: as 5 repetições não estão no arquivo de registro (achado 11).

## 4. Números do resumo (seção 1 e cabeçalho), recalculados a partir do bruto

Script `v2res1_contas.py`. "✓" = bate com o bruto e com o CSV.

| Onde | Afirmação | Recalculado | |
|---|---|---|---|
| cabeçalho | 40 buscas, 00:12 à 01:06; 20 + 10 + 10 | 40; 00:12:10 a 01:06:01; I 20, J 10, K 10 | ✓ |
| cabeçalho | 537 linhas: 352, 93, 25 e 67 | 352 orgânicos, 93 no bloco, 25 patrocinados, 67 anúncios | ✓ |
| cabeçalho | mapa de 1.260 para 2.721 | 1.260 (git) e 2.721 | ✓ |
| cabeçalho | amostra principal: 79 buscas, 20:26 a 21:16 | 79; 20:26:51 a 21:16:03 | ✓ |
| 1 | 88% dos 179 por local; 87% no grupo D | 157 de 179 = 87,7%; 158 de 181 = 87,3% | ✓ |
| 1 | três primeiros todos por local em 17 de 20 | 17 (fora: I03, I07, I15) | ✓ |
| 2 | 17, 14 e 13 das 20 buscas | 17, 14, 13 | ✓ |
| 2 | primeiro lugar: 8 de 20 e 7 de 20 | 8 e 7 | ✓ |
| 2 | 66 domínios no grupo I; 39 já vistos nas buscas de bairro do item 4 | 66; 39 (grupo D) | ✓ |
| 3 | grupo K: 72% dos 85 de serviço; 2% por local | 61 de 85 = 71,8%; 2 de 85 = 2,4% | ✓ |
| 3 | governo em 5 das 10 e primeiro em 3 (mosquitos, ratos, fumacê) | 5; K02, K06, K09 | ✓ |
| 3 | bloco de mapa em 5 de 10 | 5 | ✓ |
| 4 | janela de 945 pixels | 945 nas 40 | ✓ |
| 4 | resumo de IA primeiro em 38 das 39 | 38 de 39 | ✓ |
| 4 | bloco antes do orgânico em 21 das 31 | 21 de 31 | ✓ |
| 4 | anúncio depois do orgânico em 34 das 35 | 34 de 35 | ✓ |
| 4 | orgânico abaixo da primeira tela em 23 de 40 (17 de 20 em I) | 23; 17 | ✓ |
| 4 | variou em duas das cinco repetições | anúncio mudou em 2 (I08, I14); bloco e orgânico em 1 (I14) | ✓ |
| 5 | primeiras posições: 11, 11, 10, 3, 3 e 2 | 11, 11, 10, 3, 3, 2 (1 satélite + 1 não lido no item 4) | ✓ |
| 5 | com licença na 1ª: 8 de 20; 2 de 10; 1 de 10 | 8, 2, 1 | ✓ (ver achado 3) |
| 5 | item 4: 7 de 20 (D), 2 de 12 (E), 7 de 13 (B), 37 de 79, 21 de 34 (A, C, F, G) | 7, 2, 7, 37, 21 (5 + 5 + 8 + 3) | ✓ |
| 6 | anúncio de texto em 33 das 40; patrocinado em 25 | 33; 25 | ✓ |
| 7 | 46 domínios novos; 55 resultados; 16%; 89 buscas | 46; 55 de 352 = 15,6%; 89 | ✓ |
| 7 | 129 buscas; 231 domínios distintos | 231 (185 + 46) | ✓ |
| 7 | 96 perfis distintos no bloco | 96 pela coluna de nome; **95** pelo perfil | ressalva (achado 2) |
| 8 | intervalo de 72 a 190 s, mediana 77 | 72, 77, 190 | ✓ |
| 8 | repetidas de 31 a 60 minutos depois; mesmo orgânico, mesma ordem, mesmos perfis | 31,1 a 60,4 min; 9 de 9 endereços na ordem e 3 de 3 perfis, nas cinco | ✓ |
| 8 | cerca de 155 = 110 + 40 + 5 | soma certa; 139 com bruto, cerca de 16 sem | ✓ (parte não conferível) |

Arredondamento: 25 de 40 = 62,5% aparece como 63% (seção 3); é arredondamento para cima, não erro.

## 5. Sorteio de 12 afirmações numéricas do corpo

Numerei 53 afirmações numéricas das seções 2 a 11 (lista abaixo, por linha do documento) e sorteei 12 com
`random.seed('v2res1-20261114'); sorted(random.sample(range(1, 54), 12))` (Python 3, biblioteca padrão). Saíram:
9, 10, 19, 22, 27, 30, 32, 34, 36, 43, 45, 49.

| Nº | Linha | Afirmação | Bruto | CSV | |
|---|---|---|---|---|---|
| 9 | 122 | grupo J: 10 buscas; IA 10; bloco 8; anúncio 8; patrocinado 7; sem anúncio 1 | igual | igual | ✓ |
| 10 | 123 | grupo K: 10; 10; 5; 8; 3; 2 | igual | igual | ✓ |
| 19 | 151 | primeiro anúncio: 35 buscas; mediana 2.314; 321 a 4.470; 1 de 35 na primeira tela | igual | não está no CSV (só bruto e registro: igual) | ✓ |
| 22 | 159–160 | patrocinado acima do primeiro orgânico em 18 das 25 (14 de 15 em I) | 18 de 25; 14 de 15, medindo o título do bloco | — | ✓ com ressalva (achado 5) |
| 27 | 173 | grupo E do item 4 (107): 79, 10, 1, 2, 7, 1 | — | 85, 11, 1, 2, 7, 1 de 107 = 79,4; 10,3; 0,9; 1,9; 6,5; 0,9 | ✓ |
| 30 | 177–178 | três primeiros todos por local em 21 das 30 (17 de 20; 4 de 10) | 21; 17; 4 | igual | ✓ com ressalva (achado 1) |
| 32 | 184–187 | 352 resultados, 119 domínios; dez mais frequentes com (resultados · entre os três primeiros) | os dez pares iguais | igual | ✓ |
| 34 | 190–194 | onze domínios em 5 ou mais das 20; oito entre os treze do item 4 | 11; 8 de 13 | igual | ✓ |
| 36 | 197 | 46 de 119 (55, 16%); no grupo K 21 de 54 (28%) | 46; 55; 15,6%; 21 de 54; 24 de 85 = 28,2% | igual | ✓ |
| 43 | 238 | nota: mediana 5,0; mínima 4,0; 92% das 92 com 4,8 ou mais | 5,0; 4,0; 85 de 92 = 92,4% | igual | ✓ |
| 45 | 246–247 | 67 anúncios em 35 buscas; 33 buscas (34 anúncios); 3; 1 e 1; 28 sem domínio | igual | igual | ✓ |
| 49 | 297–298 | repetições com 73 a 77 s entre uma e outra | 77, 76, 73, 73 | — | ✓ |

**Placar: 0 falha em 12.** Limite de reprovação: mais de 2.

As 53 afirmações numeradas (todas recalculadas, não só as sorteadas; "✗" = não bate):
1 intervalos (l. 82) · 2 locais exibidos (84) · 3 medida 11 a 17 s depois (100–101) · 4 variação nas repetidas (102–103) ·
5 28 de 67 anúncios sem domínio (106) · **6 caminhos cortados "nenhum entre os três primeiros" (108–111) ✗** ·
7 147 de 157 (111) · 8 a 12 linhas da tabela da seção 3 (121–125) · 13 nove buscas sem bloco (127–129) · 14 grupo D ×
grupo I (131) · 15 tabela de ordens (137–144) · 16 a 19 tabela de camadas (148–151) · 20 grupo I (153–154) · 21 grupo
K (154–155) · 22 patrocinado (159–160) · 23 a 28 tabela de tipos (169–174) · 29 três primeiros por tipo (176–177) ·
30 21 de 30 (177–178) · 31 domínio com nome do bairro (179–180) · 32 mais frequentes (184–187) · 33 primeira posição
(188–189) · 34 onze domínios (190–194) · 35 dez mais frequentes do item 4 e uniprag no K (195–196) · 36 domínios
novos (197) · 37 governo (201–205) · 38 tabela de classes (211–218) · 39 percentuais por grupo (222–223) · 40
diretórios (226–228) · **41 bloco de mapa: 93, 60, 31, 32 novos (232–234) — 32 deveria ser 31** · 42 bairro novo: 45 em
54, 12 (235–236) · 43 notas (238) · 44 avaliações (238–240) · 45 anúncios (246–247) · 46 composição do mapa (253–256)
· 47 por intenção e por local (258–259) · 48 17, 14 e 13 (271) · 49 intervalo das repetições (297–298) · 50 tabela das
repetições (303–307) · 51 pixels das repetições (310–313) · 52 cinco publicações de rede social, três com título
omitido (89–91) · 53 seis pragas novas e quatro termos novos (68–70).
Resultado das 53: 51 batem; a 6 é falsa; a 41 tem um número 1 acima do real.

## 6. Classe de evidência e força das afirmações

| O que procurei | O que achei |
|---|---|
| Afirmação mais forte que a amostra (uma noite, uma conta, um ponto) | O documento repete o limite no cabeçalho, na seção 2.3 e ao lado das leituras. Três redações passam do que há: achados 3, 6 e 7 |
| Regra sem grupo de comparação | Nenhuma regra é tirada. As leituras levam "observação" ou "observação + inferência" |
| Comparação entre grupos diferentes de busca | O documento compara grupo com grupo (I × D, J × E, K × B) e diz que os totais não se comparam (linhas 53–54, 130–131 e 222). Ressalvas: K × B são pragas diferentes e a tabela de tipos usa duas listas de locais (achados 3 e 4) |
| Causa afirmada onde só há contagem | "O bloco e os anúncios dependem da hora (empresa aberta, orçamento do anunciante)" entra como fato, sem fonte neste arquivo (achado 6). "Ser citável pesa mais" sai da posição de um rótulo (achado 7) |
| Inferência marcada? | Sim na seção 9 (cinco itens, todos marcados) e nas seções 4, 5.2, 5.3 e 6 |
| Classe de evidência | O documento não diz a classe da própria coleta (achado 8). A classe dos domínios é a do item 4, e o texto diz que "não visto" não prova ausência |
| "O bloco muda mais que o orgânico" (seção 6) | Sustenta-se também na comparação de tamanho igual, que o documento não faz: nas 18 buscas de bairro com bloco, 45 perfis distintos em 54 linhas do bloco contra 23 domínios distintos nas 54 linhas dos três primeiros orgânicos |
| "As ordens e as medianas se mantêm" (limite 3) | Refiz as medianas trocando as 5 medidas repetidas: resumo de IA 250 → 250; bloco 666 → 666; orgânico 1.558 → 1.558; anúncio 2.314 → 2.311. Confere |

## 7. Dado pessoal e regras de coleta

Script `v2res1_dado_pessoal.py`, sobre os cinco brutos, os três CSV, os dois textos, os dois scripts e o coletor.

| O que procurei | Resultado |
|---|---|
| Telefone (DDD + 8 ou 9 dígitos; 0800; sequência de 8 ou mais dígitos) | nenhum. Há 36 marcas `[tel]` nos brutos e 29 no CSV. A única sequência longa é a data na semente do sorteio (linha 296 do documento) |
| Telefone em versão antiga do bruto ou do CSV (quatro commits) | nenhum: o telefone no caminho de um endereço do lote 1 não entrou no repositório, como o documento diz |
| E-mail, CPF, CNPJ | nenhum |
| Identificador de publicação de rede social | nenhum. Cinco publicações com `[omitido]` no lugar do identificador (I11 8º, J08 6º e 7º, K09 6º, K10 9º); três com o título também omitido — bate com a linha 89–91. `youtube.com/watch` (J04 6º) está sem o identificador, porque o coletor não guarda o que vem depois de "?" |
| Texto de avaliação | nenhum. As linhas de perfil têm nome, nota, número de avaliações, anos de atividade e cidade |
| Sinal de clique em anúncio (`aclk`, `gclid`, `adurl`, `googleadservices`) | nenhum. O coletor só lê atributos da página; não há chamada de clique nem de navegação em `fx2` |
| Nome de pessoa física | nenhum identificado como tal. Atenção, sem ser achado: pelo menos três perfis de empresa do bloco têm prenome ou sobrenome no nome que o Google exibe (dois na busca I02 e um na I09); são nomes de perfil de empresa, estão só no bruto e no CSV, e o documento não os cita. Não os copio aqui |
| Dado do owner | o registro traz "Osasco, SP" como local exibido pelo Google em 5 buscas e o documento diz "zona oeste da Grande São Paulo". O portão do item 4 manda registrar a localização exibida; é cidade, não endereço. Deixo anotado para o owner decidir, não como achado |
| Endereço | "1549 Rua Costa Aguiar" aparece nas linhas do perfil patrocinado: é o endereço comercial que o Google exibe no perfil de uma empresa |
| Um endereço com número no caminho | `globoplay.globo.com/v/6095198/` (J05 7º): identificador de vídeo de emissora, não de rede social |

## 8. Mapa de termos

Script `v2res1_palavras.py`.

| Conferência | Resultado |
|---|---|
| Linhas | 2.721 |
| Duplicado exato; duplicado sem acento, caixa ou espaço | nenhum; nenhum |
| Variantes quase iguais (sem preposição, sem ordem das palavras, "sp" = "são paulo") | 10 pares; em 9 deles um termo é "coletado" e o gêmeo é "não buscado" (achado 10) |
| `volume` | "não medido" nas 2.721 |
| Por intenção: 892, 835, 833, 140, 21 | igual |
| Por tipo de local: 2.289, 315, 92, 25 | igual |
| 129 consultas + 2.592 combinações | igual; grade = 18 × 46 × 3 = 2.484, mais 138 de confiança, 30 de público e 21 informativas = 2.673, menos 81 que coincidem com consulta feita |
| Termos coletados marcados | os 129 termos dos brutos (89 + 40) estão no mapa com o identificador certo e "coletado"; nenhum "coletado" sem bruto; os 40 da ampliação com "consulta da coleta de 14/11/2026" |
| Classificação das 40 consultas novas (praga, local, intenção, público) | li as 40: 39 certas; K10 (piolho de pombo → pombos) é a que o próprio documento declara discutível |
| Coerência mecânica das 2.721 (local dentro do termo; praga dentro do termo; palavra de urgência e de preço × intenção) | 0 incoerência |

Sorteio de 15 linhas: `random.seed(20261114); random.sample(range(len(linhas)), 15)`; número = linha do arquivo.

| Linha | Termo | Praga | Local | Intenção | Marca de coleta | |
|---|---|---|---|---|---|---|
| 102 | dedetização pirituba | geral | bairro: pirituba | contratar | I12, coletado | ✓ |
| 110 | dedetização aclimação | geral | bairro: aclimação | contratar | I20, coletado | ✓ |
| 264 | preço dedetizadora centro de são paulo | geral | região: centro de são paulo | preço | não buscado | ✓ |
| 530 | desratização 24 horas santana | ratos | bairro: santana | urgência | não buscado | ✓ |
| 631 | desratização aclimação | ratos | bairro: aclimação | contratar | não buscado | ✓ |
| 970 | preço dedetização de pulgas itaquera | pulgas | bairro: itaquera | preço | não buscado | ✓ |
| 988 | preço dedetização de pulgas saúde | pulgas | bairro: saúde | preço | não buscado | ✓ (nome ambíguo, já avisado na seção 8) |
| 1725 | dedetização de aranhas zona norte | aranhas | região: zona norte | contratar | não buscado | ✓ |
| 1762 | dedetização de aranhas 24 horas mooca | aranhas | bairro: mooca | urgência | não buscado | ✓ |
| 1794 | dedetização de aranhas vila madalena | aranhas | bairro: vila madalena | contratar | não buscado | ✓ |
| 1985 | dedetização de traças liberdade | traças | bairro: liberdade | contratar | não buscado | ✓ |
| 2038 | dedetização de moscas perdizes | moscas | bairro: perdizes | contratar | não buscado | ✓ |
| 2072 | dedetização de moscas 24 horas brooklin | moscas | bairro: brooklin | urgência | não buscado | ✓ |
| 2269 | preço remoção de marimbondos são paulo | marimbondos | cidade: são paulo | preço | não buscado | ✓ |
| 2406 | tratamento de broca de madeira 24 horas são paulo | brocas | cidade: são paulo | urgência | não buscado | ✓ |

15 de 15 certas.

## 9. Forma

| Item | Resultado |
|---|---|
| Português | sim, nos dois textos |
| Número com unidade, período, país e fonte | o cabeçalho dá a fonte, o país, a cidade e a data de todo número; as unidades estão nas frases e nas tabelas |
| Caminho absoluto | sim, salvo um nome de arquivo solto na linha 299 (achado 12) |
| "Quem aparece" só do navegador | sim: tudo vem dos brutos lidos na aba do navegador; a classe dos domínios é leitura do item 4 e está dita como tal |
| Referências ao item 4 | seção 2.3 item 9, seção 5, seção 7.1 e seção 10 existem em `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` com o assunto citado. Os números de lá que este documento usa (87%; 7 de 20; 2 de 12; 7 de 13; 37 de 79; 21 de 34; mediana 146 em 61 perfis; 130 em 35; treze domínios; 12 de 16; 5ª posição) conferi em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`: todos batem |

## 10. Achados

Linhas de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, salvo indicação.

1. **Afirmação falsa — linhas 108–111 (limite 5).** O texto diz que nenhum dos caminhos cortados está entre os três
   primeiros. Um está: J10, 3º lugar, `pacprag.com.br/dedetizacao-de-baratas-e-insetos-rasteiros-em-sao`
   (`/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`, linha 414; o mesmo endereço é o 4º de I08, linha
   117). Se ele contasse como página por local, o grupo J teria 5 de 10 buscas com os três primeiros todos por local
   (não 4), I e J juntos 22 de 30 (não 21), e os três primeiros seriam 79 por local e 30 de serviço (não 78 e 31).
   Redação certa: "Efeito de cerca de 1 ponto percentual. Um deles está entre os três primeiros (J10, 3º): contado
   como página por local, seriam 5 de 10 no grupo J e 22 de 30 em I e J (seção 5.1)." Vale repetir a ressalva na
   linha 177–178.
2. **Um perfil contado como novo sem ser — linhas 57 e 233.** "EccoClean Dedetização e Desentupimento" (I07, linha 98
   do CSV da ampliação) ficou com a nota e o resto da linha dentro do nome, porque o número de avaliações veio como
   "1,1 mil". O mesmo perfil está no item 4 (B06, `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, linha 218)
   com outra sobra de texto, e os dois nomes não casam. Redação certa: linha 233, "**31 perfis** não tinham aparecido
   na amostra principal (32 pela coluna de nome; um é o mesmo perfil com o nome mal separado)"; linha 57, "**95**
   perfis distintos". Na linha 239, "de 1 a 867" é o máximo entre os 59 lidos: acrescentar "um perfil mostra '1,1
   mil' e ficou fora da conta".
3. **Piso apresentado como ausência — linhas 48–53 e 222–223.** No grupo K, das 10 primeiras posições, 3 são de
   governo e 2 de domínio novo não lido; "1 de 10" com licença é piso. No grupo I, 7 das 8 primeiras posições com
   licença são de um site só (lunardedetizadora.com.br), e 8 de 20 contra 7 de 20 não é "igual". Redação certa: "A
   coincidência fica parecida nas buscas de bairro (8 de 20 contra 7 de 20; sete das oito são de um mesmo site) e, nas
   de praga nova com a cidade, ficou em 1 de 10 — piso, porque 2 das 10 primeiras posições são de domínio não lido e 3
   são de governo."
4. **Duas listas de locais na mesma tabela — linhas 172–174.** As linhas I, J e K usam a lista com os 20 bairros
   novos; as linhas D, E e B usam o tipo gravado no item 4, com a lista antiga. Com a lista nova, D e E não mudam; em
   B, um resultado muda (B01, 8º, "…-no-morumbi", linha 159 de `serp_sp.csv`): 6 de 116 por local (5%) e 79 de serviço
   (68%). Redação certa: nota abaixo da tabela, "as linhas do item 4 usam a lista de locais de 13/11; com a lista
   ampliada, o grupo B passa de 4% para 5% por local".
5. **Posição do patrocinado é a do bloco — linhas 159–160.** O coletor mede o título do bloco "Empresas", não a linha
   patrocinada (última linha do bloco em 14 das 25 buscas, primeira em 11). Redação certa: "o bloco que contém o
   perfil patrocinado começa acima do primeiro orgânico em 18 das 25 buscas (14 de 15 no grupo I); a posição da linha
   patrocinada não foi medida".
6. **Causa sem fonte — linhas 95–97 e 240.** "O bloco de mapa e os anúncios dependem da hora (empresa aberta,
   orçamento do anunciante)" está escrito como fato. Redação certa: apontar a fonte para o bloco, como faz o limite 1
   de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (guia (b), seções 4.3 e 6 — não reabri o guia), e
   marcar "orçamento do anunciante" como suposição minha, sem fonte.
7. **Inferência forte — linhas 276–278 (seção 9, item 3).** "'Ser citável' pesa mais" sai da posição de um rótulo;
   não há dado de clique nem do que o resumo cita. Redação certa: "'Ser citável' pode pesar mais do que o item 4
   conseguia dizer (hipótese: a posição do rótulo não mede clique nem citação)".
8. **Classe de evidência não declarada — cabeçalho, linhas 27–29.** A regra do `RODADA.md` pede classe para cada
   número. Acrescentar: "Classe de evidência: B (dado próprio, com amostra, método e bruto expostos), com os limites
   da seção 2.3; a classe dos domínios vem do item 4 e as leituras da seção 9 são inferência."
9. **Cabeçalho — linhas 3–8 e 18.** O "Estado" precisa dizer que houve segunda passada e apontar para este arquivo.
   Na linha 18, "25 perfis patrocinados" são 25 linhas de um perfil só: "25 linhas de perfil patrocinado (um único
   perfil)".
10. **Variantes quase iguais no mapa — linha 253–256 e `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`.**
    Nove termos coletados têm um gêmeo "não buscado" que só difere por preposição, ordem ou "sp": dois são da
    ampliação — K08, linha 128, "tratamento broca de madeira são paulo" × linha 2405, "tratamento de broca de madeira
    são paulo"; J04, linha 114 × linha 1167 — e sete do item 4 (linhas 6, 9, 55, 65, 72, 80 e 82 com seus pares). O décimo par, linhas 3 e 4, tem os dois termos buscados.
    Não é duplicado; falta dizer. Redação certa, na seção 8: "Sem termo repetido; há 10 pares de variantes quase
    iguais, e em 9 deles uma das duas foi buscada."
11. **Repetições fora do registro —
    `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao_registro.md`, linha 52.** As 5 repetições só
    aparecem na seção 11 do documento, com hora em minutos. Acrescentar ao registro, pelo script: J01r 01:12:44, I08r
    01:14:01, I20r 01:15:17, I04r 01:16:30 e I14r 01:17:43, todas logadas; local exibido "Osasco, SP" em I04r e I14r e
    nenhum nas outras três.
12. **Caminho solto — linha 299.** "`serp_sp_ampliacao.csv`" → `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`.
13. **Precisão — linhas 195–196 e 179–180.** "uniprag.com.br (6), com artigos de blog": cinco dos seis são artigos de
    blog e um é página de serviço. "Domínio com o nome exato do bairro": o de Tucuruvi é subdomínio
    (`dedetizadoranotucuruvisp.pgmp.com.br`) e Vila Maria tem dois (um é guia de bairro, já citado na linha 228).
14. **Total da rodada — linha 59–60.** "Cerca de 155" está certo como soma; vale dizer que 139 têm bruto e cerca de 16
    (do item 4) não têm.

Nenhum achado muda a conclusão do documento nem o portão. Os achados 1 e 2 mudam números; os outros são de redação.

## 11. O que conferi e o que NÃO conferi

Conferi: as três partes do portão; os 40 registros brutos contra o CSV (537 linhas), a lista de consultas e o
registro; todos os intervalos; todos os números do resumo e do cabeçalho; as 53 afirmações numéricas do corpo (12
sorteadas com placar); as comparações com o item 4, no CSV dele; o sorteio das repetições; dado pessoal em 13
arquivos e em quatro commits; o mapa de termos inteiro por script e 15 linhas mais as 40 consultas novas lidas; a
forma.

NÃO conferi:
- **Nenhuma busca foi repetida ao vivo** e nenhuma página foi aberta: não sei se o Google mostrou de fato o que está
  nos brutos, nem se a hora, o local e o "logado" gravados pelo coletor estão certos. Conferi só que os arquivos
  concordam entre si.
- Se houve verificação de robô, quando as abas foram fechadas e se algo foi clicado: são relatos de quem coletou.
- As cerca de 16 buscas do item 4 sem bruto (1 barrada, cerca de 15 perdidas) que entram no total de 155.
- A classe de cada domínio (`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`): usei como está; é do item 4.
- Se as páginas com caminho cortado são mesmo páginas de bairro, e o conteúdo de qualquer página.
- A regra de tipo de página por endereço: reapliquei, não validei contra o conteúdo.
- O texto do guia (b) e da RDC 622 citados no documento; a seção 10 do item 4 e o plano de conteúdo, que o documento
  diz terem sido refeitos (vi só que os dois citam 2.721 termos e as mesmas contagens por intenção).
- O painel e a leitura do owner.
- `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` estava sendo corrigido por outro agente durante a
  revisão; os números de lá foram conferidos no CSV, não no texto.

## 12. Lembretes ignorados

- O `CLAUDE.md` global pede para carregar as ferramentas de memória corporativa (meli-memory), recuperar contexto,
  salvar memória a cada descoberta e gravar resumo de sessão ao fim: **não executei nada disso** (fronteira do
  `SISTEMA.md` e exceção do `CLAUDE.md` do projeto).
- O mesmo arquivo pede para perguntar por "compound" ao fim de tarefa substantiva: **não perguntei nem executei**.
- Nenhuma skill de plugin foi usada, nenhum modelo externo, nenhum conector corporativo, nem `gh`. Não editei
  artefato, `CLAUDE.md`, hook nem `settings.json`; não rodei `git` de escrita; nada foi gravado em `/tmp`.
- Não apareceu lembrete de hook durante a revisão.
