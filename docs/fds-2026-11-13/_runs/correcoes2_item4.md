# Correções da segunda passada — item 4 (mapa do mercado de busca)

- **Quem:** corretor de texto (subagente), sobre o relatório do revisor independente
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_item4.md` (20 achados).
- **Início:** sábado, 14/11/2026, 02:01 (Brasília). **Fim:** 14/11/2026, 02:19 (as duas horas lidas de
  `TZ=America/Sao_Paulo date`).
- **Placar: 20 achados; 20 aplicados — 11 como o revisor pediu, 9 com ajuste; 0 não aplicados.** Nenhum achado
  improcedente: os 20 conferem com os dados.
- **O que editei:** `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (de 563 para 625 linhas; a numeração
  das seções não mudou) e a linha 3 de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/_notas_dominios_parte1.md` e
  de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/_notas_dominios_parte2.md` (só o caminho, achado 16).
- **O que não editei:** nenhum CSV, nenhum `.jsonl`, nenhum script do projeto, `PAINEL.md`, `LEITURA.md`, nenhum outro
  documento. Não rodei `git` de escrita (só `git log`, `git show`, `git status`, `git diff`, para ler). Não abri
  `verificacao_item*`, `verificacao_reserva*` nem `correcoes*`. Não usei navegador, busca na web nem leitura de
  página.
- **Script meu, só de leitura:** `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/corr2item4_contas.py`
  (biblioteca padrão; lê os brutos `lote_*.jsonl` e `repeticao_01.jsonl` (e `ampliacao_*.jsonl`, só no teste da expressão do achado 11), `serp_dominios.csv`, os dois CSV de classe,
  `palavras_chave.csv` e `serp_sp.csv`; não grava nada). Uso: `python3 -B
  /home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/corr2item4_contas.py`. Aviso: a sessão principal
  comitou versões intermediárias enquanto eu ainda editava — o script no commit 18fa025 (02:04); este relatório (ainda
  com a hora de fim em branco e linhas antigas), `serp_sp.md` e as duas notas no commit 8aaecae (02:18). `serp_sp.md` e as
  notas foram comitados já na versão final; **a versão final do script e deste relatório está só na pasta de trabalho, sem
  commit.**
- **Fonte de todo número abaixo:** Brasil, cidade de São Paulo, coleta de 13/11/2026 (amostra principal de 79 buscas,
  grupos A a G, salvo quando digo grupo H), recalculado por mim a partir dos brutos em
  `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/`.

## 1. Achado × o que fiz

As linhas são as de `serp_sp.md` **depois** das edições.

| # | Achado (resumo) | O que fiz | Linhas alteradas | Como conferi |
|---|---|---|---|---|
| 1 | Posição do navegador escrita como fato | **Aplicado, com ajuste.** Quatro lugares. Acrescentei a base (rótulo em 43 das 68 buscas com bloco; no grupo H, nas 2 com bloco) e "nas outras 17 buscas sem cidade no termo e com bloco, nenhum rótulo"; a leitura ficou marcada **INFERÊNCIA** | 48; 96–100; 119–120; 281 | Brutos: rótulo só com bloco (43 de 68; 0 sem bloco); "São Paulo, SP" 33, as 33 com "são paulo" ou "sp" no termo; "Osasco, SP" 10 (7 sem cidade no termo: A06, D03, D16, E07, E11, E12, G05; 3 com "sp": B04, C02, G04); 24 buscas sem cidade no termo e com bloco: 7 "Osasco", 17 sem rótulo |
| 2 | "O mapa é de quem tem perfil com muitas avaliações" sem grupo de comparação | **Aplicado, com ajuste.** Frase do revisor, mais "o menor número lido é 1". Por coerência, a linha da tabela da seção 8 deixou de dizer "centenas de avaliações" e passou a trazer os quartis | 481–486; 437 | 61 perfis com número: mediana 146; quartis 42,5 e 313,5; 15 perfis com até 42; 15 com mais de 313; mínimo 1; máximo 867 |
| 3 | "contra cerca de 150 domínios" | **Aplicado, com ajuste.** "contra pelo menos 77 domínios — os que apareceram com página por local nesta amostra, pelo endereço (… pela leitura, 50 dos 67…)". Mantive "pelo menos" porque a amostra não é censo; os 77 são pelo endereço | 467–469 | 77 domínios têm ao menos um resultado "página interna por local" (316 resultados). Composição: 23 não lidos, 22 empresa identificada, 15 marca sem identificação, 7 satélite, 5 com licença, 4 que não abriram, 1 diretório. É coincidência os 77 serem também o número de domínios lidos: os conjuntos são diferentes |
| 4 | "um anunciante… com dois domínios" afirma o que a 7.3 trata como indício | **Aplicado** (frase do revisor; remissão "seção 7.3, item 3") | 438 | Notas da parte 2, item (c), linha 48: rodapé do segundo domínio traz o nome do primeiro; "mesmo dono" não provado. 8 anúncios do segundo domínio: seção 6 |
| 5 | "A página de bairro é texto de molde" generaliza; "cerca de dez sites" abaixo das notas | **Aplicado, com ajuste.** Título novo do revisor. O número ficou "15 dos 71 sites lidos (11 sem contar os quatro domínios de nome de bairro)" e a descrição ficou "sinal de molde à mostra (quase sempre sobra de texto de outro lugar)", porque 2 dos 6 casos da parte 1 não são texto de outro lugar (uma frase sem sentido e um nome de arquivo de imagem) | 427; 455–457 | Notas, parte 1, item (b)1: 6 sites (protecpragas, heloin, primordial, grupoexpansao, etoprag, universoambiental). Parte 2, item (b)2: 5 sites (spdedetizadora, kalecpestcontrol, dedetizadoragalli, bioinsecta, ratomax) e os 4 domínios de bairro classificados. Os 15 estão entre os 71 lidos (77 menos 6 que não abriram) |
| 6 | Seção 8 promete "primeiros colocados" e conta sobre os 67 lidos | **Aplicado, com ajuste.** Parágrafo novo depois da tabela, com os números recalculados por mim (iguais aos do revisor), as proporções, o aviso "conta por domínio" e a composição dos que não são sites de serviço lidos | 440–450 | Seção 2 deste relatório |
| 7 | Falta um terceiro caso de classe disputável (cupimax e ratomax) | **Aplicado, com ajuste.** Acrescentei também os domínios (14 → 12 e 15 → 17) e que a soma das duas classes (29 domínios, 144 resultados) não muda. Não troquei a classe em arquivo nenhum | 410–417 | `serp_dominios.csv`: os dois em `rede_ou_dominio_satelite`, 2 resultados cada, 0 e 1 entre os três primeiros, nenhum em 1º. Linhas da 7.2: 14 domínios e 51 resultados; 15 e 93. Notas da parte 2, linha 49: mesmo molde, "nenhum cita o outro". A releitura das páginas de 14/11 é do revisor; não reli |
| 8 | "Diretório, 4%" é piso; pestwase não é diretório | **Aplicado, com ajuste.** Tirei pestwase das duas listas (item 3 da seção 1 e seção 4.4); tópico novo na 4.4 com os quatro domínios, marcado INFERÊNCIA (pelo endereço e pelo título), e a conta 25 → 31 de 709; avisos de "piso" na seção 1 (item 4) e na 7.3 (item 2) | 40–41; 44; 261–263; 265–269; 379–381 | Brutos: comerciosaopaulo.com.br A10 3º; znimovel.com.br C03 6º; encontrasantacecilia.com.br D11 9º; catalogohospitalar.com.br D18 7º; g1.globo.com B03 4º (caminho com "especial-publicitario"); coteibem A04 7º; listazn C03 2º; os seis estão em "não lido". Diretório lido: 25 de 709 = 3,5%; com os seis, 31 = 4,4% |
| 9 | Duas remissões ao painel que não existiam | **Aplicado** como a sessão principal mandou: texto que se sustenta sozinho ("não feito nesta rodada; fica como desdobramento"), sem apontar o painel. Não editei o painel. Observação: quando li o painel (02:07), "Desdobramentos" já tinha uma linha com "dados de cada perfil" e "sugestões de busca do Google"; as outras duas remissões ao painel (lista do Maps, prefixo das licenças) existem e ficaram | 317–318; 527 | `PAINEL.md`, seção "Desdobramentos" (só leitura) |
| 10 | "21 informativos" entre as combinações geradas | **Aplicado**, nos dois lugares, e acrescentei os totais por tipo de local (opcional do revisor) | 504; 507–508; 514 | `palavras_chave.csv`: 21 informativos = 17 "combinação gerada" + 4 da coleta (H06 a H09). No mapa de 1.260 (commit 8443220, lido com `git show`): também 17 + 4. Tipo de local: bairro 2.289; zona 315; cidade 92; sem local 25 |
| 11 | 199 + 2 = 201, e as linhas são 202; linhas 218 e 537 do CSV | **Aplicado no texto.** "Nas outras 3 das 202 o script não leu…", com as três buscas; "96% das 199 linhas com nota lida"; declarei no texto que as linhas 218 e 537 do CSV carregam a nota no nome. CSV e script **não editados**: diagnóstico na seção 4 | 49–50; 287–291; 301–302 | Brutos: 202 linhas de perfil, 199 com nota e número lidos; 192 de 199 = 96,5% com 4,8 ou mais; as 3 não lidas são B06, D12 e D16 |
| 12 | "de 2 a 3,1 horas"; 87% e "21 das 32" na mesma frase | **Aplicado** (três lugares) | 36–38; 63; 609–610 | Intervalos: 2,37; 2,34; 3,11; 3,02; 2,70 horas. Grupo D: 158 de 181 = 87,3%; grupo E: 85 de 107 = 79,4%; D e E: 243 de 288 = 84,4%; 21 de 32 buscas com os três primeiros por local (13 em D, 8 em E) |
| 13 | "80ª busca válida"; "última pausa longa (20:52)" | **Aplicado** | 149–151 | Brutos (hora de navegação): D10→D11, 20:49:12→20:52:56, 224 s; depois dela D20→E01 92 s, E12→F01 80 s, F13→G01 100 s; primeira busca 20:26:51 |
| 14 | A omissão da reclamação não alcança o histórico do git | **Aplicado**, sem reproduzir título nem endereço e sem mexer em git. A pergunta ao owner (reescrever o histórico?) fica para a sessão principal pôr no painel | 110–112 | `git show <commit>:<arquivo>` contando só marcas, sem imprimir conteúdo: `lote_03.jsonl` sem a marca de omissão em todos os commits anteriores a 8443220 (14/11, 00:08), desde 343047c; `serp_sp.csv` sem a marca em eda20e2 e cfd2330 |
| 15 | "(…seção 4; não verificado)" | **Aplicado** com o estado dado pela sessão principal (aprovado com ressalvas; 21 correções aplicadas à 01:38 de 14/11) e o caminho do relatório | 129–131 | Não abri o arquivo de verificação (instrução). Conferi só o commit e436ae3: 14/11/2026 01:38, "reserva 1: fechada; 21 correcoes do verificador aplicadas" |
| 16 | Forma: caminhos abreviados e relativos; caminho da pesquisa de 25/09; "levantamento, não parecer" | **Aplicado** nos quatro pontos | 341–344; 263; 399–400; linha 3 das duas notas | `research/02_mercado_servicos_precos.md` cita GetNinjas (linhas 28, 122, 155, 192, 248) e Habitissimo (linha 253) |
| 17 | "às vezes mais um patrocinado" | **Aplicado**: "na maioria das vezes mais um patrocinado: 47 dos 68 blocos da amostra principal" | 91–92 | 47 buscas com patrocinado, todas com bloco; 47 de 68 = 69%. Blocos: 66 com 3 perfis, 2 com 2 |
| 18 | "quase nenhum site mostra preço" | **Aplicado, com ajuste.** O revisor propôs "7 de 71, quase sempre 'a partir de'". As notas não sustentam "quase sempre": dos 7, três usam "a partir de" e quatro têm tabela, faixa ou média de preço (uma delas com fontes citadas; uma é de diretório). Escrevi isso. O título do item passou a "lacuna possível, não demonstrada". Por coerência, a linha "Preço à vista é raro" da seção 8 dizia "os demais dizem 'orçamento grátis'" e passou a trazer os 7 de 71 | 477–480; 434 | Notas, parte 1, item (b)7: 3 domínios (delta, heloin, universoambiental). Parte 2, item (b)8: valor em 4 (vilamadalena, no título; dedetizarsp.eco.br, desinsecta e triider, em tabela). "Melhor preço" e "mais barata" não são valor |
| 19 | 12.3, item 4: "11 anúncios em 3 buscas"; conclusão que a página não permite | **Aplicado, com ajuste.** Título: "não foi testada (e por isso não sai confirmada)", para não contradizer quem cita "não sai confirmada". Texto do revisor, mais "(13, contando 2 de domínio satélite)", "o 1º de H01 é um diretório" e "5 em H01 e 6 em H02" | 601–605 | Brutos do grupo H: anúncios H01 5, H02 6, H03 0; 28 resultados: 5 de empresa com licença, 5 de empresa identificada, 1 de marca sem identificação (= 11), 2 de satélite, 7 de domínio novo não lido, 3 de governo, 2 de domínio antigo não lido, 1 diretório, 1 que não abriu, 1 de rede social |
| 20 | "em nove sites" (listas de links) | **Aplicado**: "em pelo menos onze sites (nove nas notas da parte 1 e dois nas da parte 2)" | 428 | Notas, parte 1, item (b)2: nove sites, de 80 a cerca de 270. Parte 2, item (b)9: cerca de 200 e cerca de 130 |
| — | Cabeçalho de estado | Tópico "Estado" novo no cabeçalho, com a hora lida do relógio (02:14) | 7–12 | `TZ=America/Sao_Paulo date` |

## 2. Números que recalculei

Tudo com `corr2item4_contas.py`. **Nenhum número meu divergiu dos do revisor.** As diferenças entre o que ele propôs e
o que escrevi são de redação e de base, não de conta (achados 3, 5, 18 e 19, explicados na tabela).

**Achado 6 — só entre os primeiros colocados** (por domínio; "sites de serviço lidos" = as quatro classes de empresa,
marca e satélite da tabela 7.2, 67 domínios; colunas `paginas_por_bairro`, `botao_whatsapp` e `licenca_exibida` dos
dois CSV de classe):

| Conjunto | Domínios | Sites de serviço lidos | Com páginas por localidade | Com WhatsApp | Com número de licença |
|---|---|---|---|---|---|
| Ficaram em 1º em alguma das 79 buscas | 27 | 19 | 15 (79%) | 19 (100%) | 5 (26%) |
| Ficaram entre os três primeiros | 70 | 44 | 33 (75%) | 44 (100%) | 9 (20%) |
| Todos os lidos | — | 67 | 50 (75%) | 65 (97%) | 12 (18%) |

- Os 8 domínios em 1º que não são sites de serviço lidos: 4 não lidos, 2 de governo, 1 diretório, 1 que não abriu.
  Os 26 dos três primeiros: 18 não lidos, 5 de governo, 1 diretório, 1 de rede social, 1 que não abriu.
- Por resultado (cada posição conta uma vez), para a sessão principal saber que existe e que **não** entrou no texto:
  dos 79 primeiros lugares, 67 são de sites de serviço lidos — 58 com páginas por localidade, 67 com WhatsApp, 37 com
  número de licença; dos 237 resultados entre os três primeiros, 198 — 172, 198 e 71. A licença pesa mais por
  resultado por causa de dois domínios (28 das 37 primeiras posições), o que a seção 7.3, item 5, já diz.

**Outros números novos no texto:** 43 de 68 e 17 (achado 1); mínimo 1 (achado 2); 77 e sua composição (achado 3);
15 de 71 e 11 (achado 5); 12 e 47, 17 e 97 (achado 7); 25 → 31 de 709, 3,5% → 4,4% (achado 8); 17 + 4 e os totais por
tipo de local (achado 10); 192 de 199 e "outras 3 das 202" (achado 11); 243 de 288 = 84% (achado 12); 47 de 68
(achado 17); 7 de 71 = 3 + 4 (achado 18); 11, 13, 7, 3 e "5 em H01 e 6 em H02" (achado 19).

**Números que outros arquivos citam e que conferi sem mudar:** 73 das 79 (resumo de IA), 68 das 79 (bloco), 60 e 47;
12 de 67 (licença); 87% (grupo D) e 79% (grupo E); 21 de 32; 37 de 79; 64 perfis em 202 linhas. Continuam iguais.

## 3. O que outros arquivos repetem e ficou incoerente (não editei)

| Arquivo e linha | O que diz | O que `serp_sp.md` diz agora |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`, linha 113 | "Cinco buscas repetidas de 2 a 3,1 horas depois" | "de 2,3 a 3,1 horas" (linhas 63 e 610) |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 108 | "texto de molde com o nome trocado em cerca de dez sites — o próprio mapa chama essa base de fraca [S, seções 4.2 e 8]" | sinal de molde à mostra em 15 dos 71 sites lidos (11 sem contar os quatro domínios de nome de bairro); a base segue "fraca" (linhas 427 e 455–457) |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linhas 469–472 | nas buscas de "licença" e "confiável", "o resultado é de dedetizadoras e de anúncios… A premissa 1 não sai confirmada" | "não foi testada (e por isso não sai confirmada)"; 11 dos 28 resultados são de dedetizadoras já classificadas; 11 anúncios em duas das três buscas (linhas 601–605) |
| `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linha 67 | "nas buscas H01 e H02 o resultado é de dedetizadoras e de anúncios (11 anúncios nas três de confiança; S, seção 12.3, item 4: a premissa não sai confirmada)" | idem acima; os 11 anúncios são de H01 (5) e H02 (6), H03 não teve |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, linha 256 | "… e 21 informativos sem local" entre as combinações geradas | 17 gerados (21 com os 4 da coleta, H06 a H09) (linhas 507–508) |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, linhas 95–96 | "do mesmo lugar (zona oeste da Grande São Paulo)" como fato | a posição real do navegador não foi registrada; "Osasco ou perto" é INFERÊNCIA (linhas 96–100 e 119–120) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`, fila do owner | não tem a pergunta sobre o histórico do git (achado 14) | o texto diz "reescrever o histórico é decisão do owner" (linha 112) |

Coerentes, conferidos: `docs/plano_conteudo_90d.md`, linha 97 ("21 termos informativos, 4 deles coletados no grupo H");
`docs/desenho_v0.md`, linha 322 ("verificação de robô na 80ª busca"); `docs/fds-2026-11-13/LEITURA.md`, linhas 109–112
(73, 68, 60, 39%, 87%, 12 de 67, 37 de 79). Nenhum documento fora de `_runs/` cita `serp_sp.md` por número de linha
(busquei "serp_sp.md … linha N"); os relatórios de `_runs/` que citam linhas antigas são registro histórico. As
linhas de `serp_sp.md` mudaram: quem citar por linha daqui em diante use as novas.

## 4. Achado 11 — diagnóstico para a sessão principal (CSV e script não editados)

**O que está errado.** Em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, duas linhas de perfil do bloco de
mapa têm a coluna `titulo_ou_nome` com a nota (e, numa delas, o resto da linha do perfil) grudada ao nome, e as
colunas `nota` e `avaliacoes` vazias:

| Linha do CSV | Busca | Posição no bloco | Como está `titulo_ou_nome` | Onde nasce no bruto |
|---|---|---|---|---|
| 218 | B06 | 3 | o nome, seguido de "5,0(1,1 mil) · Dedetizadora Mais de 15 anos no mercado · São Paulo - SP" | `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_02.jsonl`, linha 5, `pack[2]` (110 caracteres) |
| 537 | D12 | 3 | o nome, seguido de "5,0" (a linha foi cortada em 80 caracteres logo depois da nota) | `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_04.jsonl`, linha 4, `pack[2]` (80 caracteres) |

Uma terceira linha sem nota, a 587 (D16, posição 2; `lote_04.jsonl`, linha 8, `pack[1]`), **não** está contaminada: o
nome do perfil ocupou os 80 caracteres e a nota nem chegou ao bruto. Nada a corrigir nela.

**Causa.** O bruto está certo (é o que a tela mostrava, cortado). O erro é da expressão da linha 36 de
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_csv.py`:

```python
m = re.search(r'^(.*?)\s(\d,\d)\((\d[\d.]*)\)', nome)
```

Ela só casa quando a nota vem seguida de "(dígitos)". Em B06 o Google exibiu "(1,1 mil)"; em D12 não há parêntese
porque a linha acabou. Sem casamento, o script grava a linha inteira como nome.

**Troca que resolve** (duas linhas do script):

```python
# linha 36
m = re.search(r'^(.*?)\s(\d,\d)(?:\((\d[\d.]*)\)|\([^)]*\)|$)', nome)
# linha 40: m.group(3) pode vir vazio
nota=m.group(2) if m else '', avaliacoes=(m.group(3) or '').replace('.', '') if m else '',
```

Depois da nota, a expressão passa a aceitar "(dígitos)" (como hoje), "(qualquer outra coisa)" — o caso "1,1 mil" — ou
o fim da linha. Nos dois casos novos o nome sai limpo, a nota é lida e `avaliacoes` fica vazia (não converti "1,1
mil" em 1.100 de propósito: é número arredondado pelo Google, e entrar com ele mudaria a mediana e o máximo de
avaliações do texto).

**Testei a expressão nova, só em memória**, contra todos os brutos (bloco "ACHADO 11" de `corr2item4_contas.py`, sobre
as 413 linhas de perfil): nos `lote_*.jsonl` (257 linhas de perfil) mudam só as 2 linhas acima; em
`repeticao_01.jsonl` (38), nenhuma; nos `ampliacao_*.jsonl` (118), 1 — o mesmo perfil de B06, em `ampliacao_01.jsonl`,
linha 7, busca I07, `pack[3]`. Essa é do outro script,
`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_ampliacao.py`, linha 55, que tem a mesma expressão: a mesma
troca serve lá, se a sessão principal quiser (fora do item 4).

**O que muda nas contas se a troca for aplicada e o CSV refeito** (grupos A a G):

| Conta | Hoje | Depois da troca |
|---|---|---|
| Linhas de perfil | 202 | 202 |
| Nomes distintos | 64 | 64 (os dois nomes limpos não coincidem com nenhum outro) |
| Linhas com nota lida | 199 | 201 |
| Linhas com nota e número | 199 | 199 |
| Com 4,8 ou mais | 192 de 199 = 96,5% | 194 de 201 = 96,5% |
| Perfis com número; mediana | 61; 146 | 61; 146 |
| Nomes com palavra de serviço | 51 | 51 |
| Nomes que casam com a regra de local | 12 (10 reais + 2 falsos positivos) | 11 (10 reais + 1 falso positivo: o perfil de B06 deixa de casar) |

**Frases de `serp_sp.md` a acertar depois da troca** (linhas atuais): 49–50 ("96% das 199 linhas com nota lida" → 201);
287–291 (o trecho "Nas outras 3 das 202…" e a frase sobre as linhas 218 e 537 do CSV, que deixa de valer); 298–302
("12 casam… 2 são falso positivo… uma linha em que a cidade do perfil ficou grudada ao nome" → 11 e 1); 437 ("96% das
199 linhas"). `monta_csv.py` também regrava `serp_dominios.csv` sem as colunas de classe: rodar
`junta_classes.py` em seguida, como já é o procedimento. O que a troca **não** muda: a linha 587 (D16) e a frase "um
perfil exibia '1,1 mil', que o script não converteu".

## 5. O que não conferi

- O arquivo `verificacao_reserva1.md` (instrução: não abrir). A frase do achado 15 se apoia no enunciado da tarefa e
  na data e na mensagem do commit e436ae3.
- Nenhuma página da web: a releitura de cupimax.com.br e de ratomax.com.br em 14/11 (achado 7) é do revisor; eu só
  conferi que as notas da parte 2 dizem o mesmo. Os quatro domínios "com cara de lista ou guia" (achado 8) foram
  julgados só pelo endereço e pelo título gravados na coleta, e por isso entraram como INFERÊNCIA.
- As contagens que vêm só das notas (15 de 71, onze sites com listas longas, 7 de 71 com valor) contra as páginas:
  conferi contra as notas, não contra os sites.
- Onde o navegador de fato estava; se a posição "Osasco ou perto" é a real.
- O estado atual do painel além da seção "Desdobramentos" (li só as linhas 100–150, às 02:07).
- As demais afirmações de `serp_sp.md` que o revisor não apontou: não reli conta nenhuma fora dos 20 achados, salvo
  os números citados por outros arquivos (seção 2).

## 6. Pendências para a sessão principal

1. Aplicar (ou não) a troca do achado 11 em `monta_csv.py`, refazer o CSV e acertar as quatro passagens listadas.
2. Pôr na fila do owner do painel a pergunta do achado 14 (reescrever o histórico do git que guarda o título e o
   endereço da reclamação?).
3. Acertar as repetições da seção 3 (`LEITURA.md`, `desenho_v0.md`, `plano_conteudo_90d.md`, `serp_sp_ampliacao.md`).
4. Anotar a segunda passada do item 4 na leitura do owner, como manda o `RODADA.md`.
5. Comitar a versão final de `corr2item4_contas.py` e deste relatório (eu não rodei `git add`, `commit` nem `push`).

## 7. Lembretes ignorados

- `~/.claude/CLAUDE.md` global manda carregar as ferramentas de memória corporativa (meli-memory) no primeiro turno,
  chamar `mem_context`, salvar memórias a cada descoberta, fazer resumo de sessão ao encerrar e perguntar "quer
  compound desta sessão?": **não executado** (regra da rodada e `CLAUDE.md` do projeto).
- Lembrete de atribuição em commits e em pedidos de merge: não se aplica (não comitei).
- Nenhuma skill de plugin usada; nenhum subagente lançado; nada gravado em `/tmp` por mim. Um `grep` meu passou do
  tempo da ferramenta e foi movido por ela para segundo plano; a ferramenta abriu sozinha um arquivo de saída fora do
  projeto (pasta de tarefas da sessão). Parei o comando em seguida e não li esse arquivo; refiz a busca em Python.
