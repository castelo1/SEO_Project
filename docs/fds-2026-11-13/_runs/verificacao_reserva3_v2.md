# Verificação independente da fila de reserva, tarefa 3 — plano de conteúdo de 90 dias, segunda versão

- **Quando:** sábado, 14/11/2026, das 00:10 às 00:19 (Brasília; lido de `TZ=America/Sao_Paulo date`), já com a
  gravação deste relatório.
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu e **sem abrir**
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva3.md` (verificação da primeira
  versão).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, 127 linhas, 14.920 bytes, gravado às
  00:09:24 de 14/11/2026, no estado do commit `24e245b` (sha256 `ad5535b5…3a873b`). Conferi no fim que o arquivo não
  mudou enquanto eu lia.
- **Portão (transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 73):** "Plano de
  conteúdo de 90 dias: quais páginas primeiro e por quê, apontando para o mapa de palavras-chave."
- **Veredito: APROVADO COM RESSALVAS.** O portão está cumprido. No sorteio de 12 afirmações houve **1 falha** (o
  limite de reprovação é mais de 2) e 4 aprovações com ressalva. **Todas** as contagens e todos os identificadores da
  coluna "Termos em K" conferem (22 contagens, 11 identificadores), e todos os termos entre aspas da seção 4 existem
  no mapa, com a intenção dita. Fora do sorteio achei 6 incoerências internas (seção 5) e 2 pontos em que o plano é
  mais forte que a fonte ou cala evidência contrária (seção 6, itens 3 e 4); nenhum muda o que o leitor entende da
  ordem das páginas. Há 24 correções pedidas, no fim.
- **O que não fiz:** nenhuma busca ao vivo, nenhum navegador, nenhuma página da web, nenhum script do projeto rodado,
  nenhum arquivo editado além deste relatório, nenhum `git` de escrita. Um lembrete do `CLAUDE.md` global pedia para
  carregar ferramentas de memória corporativa, salvar memória, fazer resumo de sessão e oferecer "compound": **não
  executei** (fronteira desta verificação e exceção escrita no `CLAUDE.md` do projeto).

## 1. O que abri

| Arquivo | O que li |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | inteiro (portão e regra de evidência) |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D") | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` ("S") | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` ("P") | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` ("A") | seções 2, 2.1, 2.2, 3, 4, 7, 8 e 9 (linhas 143–266 e 329–398) |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` ("K") | as 1.260 linhas, por Python só de leitura |
| `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` e `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` | inteiros |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_01.jsonl` a `lote_08.jsonl` e `repeticao_01.jsonl` | registros A10, B04, B04r, B05, E05, H01 a H10 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` | quadro de vereditos (linhas 20–40), RDC 622 art. 22 (linhas 180–196), "Conclusão para o site" (linhas 236–262), ocorrências do art. 7º, § 5º |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/` | lista de arquivos; a linha 93 de `para-empresas/restaurantes/index.html` e a linha 84 de `LEIA-ME.md` |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item4.md` (cabeçalho) e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` (linhas sobre o item 4) | para conferir "S verificado em 14/11/2026" |

## 2. Portão

| Parte do portão | Situação | O que conferi |
|---|---|---|
| Plano de 90 dias | cumprido | Calendário dos dias 1 a 90, com três medições (28, 56, 84); as faixas de dias fecham (seção 5 deste relatório) |
| Quais páginas primeiro | cumprido | 19 a 23 páginas ordenadas em quatro blocos (base, guias, oferta, públicos) |
| Por quê | cumprido, com ressalva | A ordem **entre blocos** tem razão escrita (linhas 17–19: o que as outras precisam; o que não depende de licenciada; o que depende). **Dentro** do bloco dos guias, três posições (ratos, percevejo, pombos) trazem só "PREMISSA de ordem", sem razão nenhuma; é honesto (não há volume medido), mas o "por quê" ali é "não há" e o plano devia dizê-lo com essas palavras (correção 15) |
| Apontando para o mapa de palavras-chave | cumprido | Coluna "Termos em K" com filtro reproduzível em 13 das 15 linhas de página; as outras duas (política e exclusão; "para dedetizadoras") não têm termo, e o plano o diz. Refiz cada filtro (seção 3) |

## 3. Contagens e identificadores da coluna "Termos em K" — todos refeitos

Método: `csv.DictReader` sobre `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, igualdade exata em cada
coluna que o plano nomeia. Total de linhas: **1.260**; `volume` = "não medido" em **1.260**. As cinco colunas citadas
existem (há mais cinco: `termo`, `volume`, `origem_do_termo`, `id_na_coleta`, `situacao_na_coleta`).

| Linha do plano | Filtro | Plano diz | Achei | Confere? |
|---|---|---|---|---|
| 15 | total de termos | 1.260 | 1.260 | sim |
| 53 | `tipo_local`=cidade, `praga`=geral, `intencao`=contratar, `publico`=residencial/geral | 6 | 6 (A01, A02, A03, A04, F07, F13) | sim |
| 55 | `intencao`=confiança | 80 | 80 | sim |
| 55 | coletados em confiança | A10, H01, H02, H03 | A10, H01, H02, H03 | sim |
| 57 | baratas, informativa / baratas, cidade, contratar | 2 / 1 | 2 / 1 (B01) | sim |
| 58 | ratos, informativa / cidade, contratar | 2 / 1 | 2 / 1 (B02) | sim |
| 60 | cupim, informativa / cidade, contratar | 2 / 2 | 2 / 2 (B03, B04) | sim |
| 62 | percevejo, informativa / cidade, contratar | 2 / 1 | 2 / 1 (B06) | sim |
| 64 | pombos, informativa / cidade, contratar | 1 / 1 | 1 / 1 (B09) | sim |
| 65 | escorpião, informativa / cidade, contratar | 1 / 1 | 1 / 1 (B05) | sim |
| 66 | `intencao`=preço e `tipo_local`=cidade | 18 | 18 | sim |
| 66 | coletados nesse filtro | A05, A09, H04, H10 | A05, A09, H04, H10 | sim |
| 66 | H05 "tabela de preço dedetização", `tipo_local`=sem local | sim | sim (`intencao`=preço) | sim |
| 68 | `publico`=condomínio | 8 | 8 | sim |
| 69 | `publico`=restaurante | 9 | 9 | sim |
| 78–79 | `intencao`=informativa | 21, 4 coletados no grupo H | 21; H06, H07, H08, H09 | sim |
| 88 | termos de formigas, pulgas, mosquito, carrapatos, aranhas e traças | 6 | 6 (1 cada) | sim |
| 60 | ids dos brutos | B04 em `lote_02.jsonl`; B04r em `repeticao_01.jsonl` | existem, com a mesma busca | sim |
| 66 | ids do grupo H de preço | H04, H05, H10 | existem em `lote_08.jsonl` | sim |

Linhas 61 e 63 (ficha, região, praga × região): o plano não dá contagem. Para registro: por região, `tipo_local`=zona
e `intencao`=contratar dá **20** termos (19 no centro); por praga e região, contratar + preço dá **2**.

**Termos entre aspas da seção 4 (linhas 83–89):** os dez termos citados existem em K, letra por letra, todos com
`intencao`=informativa: "como acabar com baratas em apartamento" (H07), "barata de esgoto como eliminar", "quanto
tempo dura dedetização" (H09), "de quanto em quanto tempo dedetizar apartamento", "dedetização é segura para pets"
(H08), "dedetização vale a pena" (H06), "como saber se tem cupim", "como identificar percevejo de cama", "apareceu
escorpião em casa o que fazer", "dedetização condomínio é obrigatória". A tabela cobre os 21 informativos sem sobra:
2 (baratas) + 2 (prazo) + 1 (pets) + 1 (vale a pena) + 8 ("e as demais" dos guias: ratos 2, cupim 2, percevejo 2,
pombos 1, escorpião 1) + 6 (pragas sem guia) + 1 (condomínio) = 21. Os outros termos entre aspas do plano também
existem em K: "como saber se dedetizadora é licenciada" (H03), "dedetização de cupim sp" (B04), "tabela de preço
dedetização" (H05). Detalhe: "dedetização condomínio é obrigatória" tem `publico`=residencial/geral, logo não está
entre os 8 de `publico`=condomínio — o plano não afirma que esteja.

**O que os filtros somam (conta minha, o plano não a faz):** com uma licenciada numa região, os filtros do calendário
apontam para **até 168 dos 1.260 termos (13%)**. Ficam sem página os 371 de urgência e 845 dos 905 de bairro; os 60
de bairro apontados são todos de confiança, entregues à página "como conferir a licença" (ver ressalva 6.3).

## 4. Sorteio de 12 afirmações

**Método:** numerei, na ordem do arquivo, 46 afirmações do plano que citam fonte ou número (lista abaixo, só as
sorteadas por extenso); sorteei com `random.Random('verificacao-reserva3-v2-20261114').sample(range(1, 47), 12)`
(Python 3). Saíram: **3, 12, 13, 16, 20, 22, 25, 26, 28, 29, 36, 42**. A numeração foi fechada antes do sorteio.

| Nº | Linha | Afirmação | Fonte aberta | Resultado |
|---|---|---|---|---|
| 3 | 26–28 | Em três das quatro buscas informativas coletadas, o primeiro resultado não é de dedetizadora (imprensa, site que pelo endereço é de fabricante, loja) | S, seção 12.1; `lote_08.jsonl`: H06 imoveis.estadao.com.br, H07 br.envu.com, H08 petlove.com.br, H09 ecoservicos.com.br (dedetizadora) | **Confere.** 3 de 4; marcada "observação de 4 buscas" |
| 12 | 55 | "Como conferir a licença" é "o conteúdo em que o desenho aposta (D, seção 1, item 2: PREMISSA)" | D, linhas 41–43 | **Confere com ressalva.** O desenho aposta em juntar **quatro** coisas numa página (licença conferida por terceiro e com data, quem executa, como a pessoa confere, preço com origem); "como conferir" é uma delas, não "o conteúdo". A marca PREMISSA está certa (correção 6) |
| 13 | 55 | Em "como saber se dedetizadora é licenciada", o segundo resultado é a consulta pública do estado e o primeiro é uma página de conteúdo; o passo a passo não foi lido | S, seções 12.1, 12.2 e 12.3 (item 2); `lote_08.jsonl`, H03: 1º dethetiza.com/conteudos/licenca-sanitaria-dedetizadora/, 2º sivisa.saude.sp.gov.br | **Confere com ressalva.** S diz que o primeiro é de site **não lido**; o plano omite (correção 6) |
| 16 | 57 | Baratas é a praga da página-modelo do protótipo e da única busca informativa de praga coletada; primeiro resultado de site que pelo endereço é de fabricante (não lido); nenhum anúncio; K 2 + 1 | `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` existe; H07 é a única das 4 informativas coletadas com `praga` ≠ geral; H07: 0 anúncios | **Confere** |
| 20 | 62 | Percevejo: 2 termos informativos; 1 de cidade e contratar | K | **Confere** (2; B06) |
| 22 | 64 | Pombos: 1 termo informativo; 1 de cidade e contratar | K | **Confere** (1; B09) |
| 25 | 68 | Nas buscas de empresa × residência, 68% dos resultados são páginas internas de serviço ou outra e 1% é página por local; predominam páginas de segmento; `publico`=condomínio, 8 termos | S, seção 4.2, linha do grupo F e último item | **Confere com ressalva.** Números e leitura iguais aos de S. Falta a base (117 resultados de 13 buscas), que o tipo foi lido **pelo endereço** e a marca de observação da amostra (correção 9) |
| 26 | 69 | O bloco da norma de serviços de alimentação está "[A ESCREVER]" no protótipo; `publico`=restaurante, 9 termos | `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 93; K | **Confere** |
| 28 | 78–79 | "O desenho pede uma página por busca e suas variações próximas (D, seção 3.2). Por isso as dúvidas do mapa (21 termos informativos, 4 deles coletados no grupo H) viram seções dos guias, não páginas soltas" | D, seção 3.2, última linha; A, seção 4 (linha da duplicidade) e seção 7 (linha "no máximo duas páginas") | **FALHA.** As contagens conferem (21; 4). A fonte não sustenta o "por isso": (a) D marca essa linha como **INFERÊNCIA** e A diz "inferência minha, não regra do Google"; o plano escreve "o desenho pede" e perde a marca; (b) a regra de D é não fazer **duas páginas para a mesma busca** ("dedetização" e "dedetizadora" na mesma página). Dúvidas diferentes ("como saber se tem cupim" e "cupim de madeira seca tratamento") não são variações próximas; lida ao pé da letra, a regra pediria uma página para cada uma — o contrário da conclusão; (c) o próprio plano a contraria nas linhas 84–85, onde a mesma resposta vira "seção comum aos guias", isto é, repetida em seis páginas. O que sustenta "seções, não artigos" é outra parte do desenho: seis guias, cada um com várias dúvidas (D, seção 3.1, T2), e poucas páginas (D, seção 1, item 3; total PREMISSA). A conclusão fica de pé; a base citada, não (correções 1 e 2) |
| 29 | 84 | "O site não promete prazo" é INFERÊNCIA a partir de D, seção 4.3, que cita o CDC, art. 38, para afirmação sem prova guardada | D, linha 167 | **Confere**; marcada INFERÊNCIA |
| 36 | 103 | Quem olha o Search Console é o owner, na conta dele (D, seção 6) | D, linha 306 ("só o owner (conta dele)") | **Confere** |
| 42 | 115 | O plano não escreve "24 horas", "garantia", "seguro", "a melhor"; estrelas; lista de bairros (D, seção 4.3; P, seção 6) | D, linhas 166–168; P, linhas 114–118; `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 243–244 | **Confere com ressalva.** D e as restrições vedam "24 horas" e "garantia" só **sem prova guardada** ("não são vedadas; quem as publica tem de poder prová-las") e "a melhor" só **sem critério exposto**; o plano tira a condição e cita a fonte como se vedasse. Estrelas e lista de bairros estão em D, seções 2 e 3.4, não em 4.3 (P, seção 6, cobre as duas) (correção 19) |

**Resultado do sorteio: 1 falha, 4 com ressalva, 7 sem reparo.**

## 5. Coerência interna

| O que conferi | Resultado |
|---|---|
| Resumo "Em uma página" × calendário | Bate em faixas e páginas: 1–14 (7 páginas); 15–56 (seis guias, um por semana, na mesma ordem: baratas, ratos, cupim, percevejo, pombos, escorpião); 30–60 (ficha e região 30–40; praga × região 40–55; preços 50–60); 60–90 (condomínio 60–70; restaurante 70–80; revisão 80–90); medições 28, 56, 84 |
| Contagem de páginas | 7 + 6 + 1 + 1 + (1 a 5) + 1 + 2 = **19 a 23**: confere. As 7 da base: início, quem somos, como funciona, política de privacidade, excluir meus dados, como conferir a licença, para dedetizadoras. Bate com D, seção 3.1: 16 fixas + T3 (1 a 5) + T4 (1) + T7 (1) = 19 a 23, dentro de 19 a 29 |
| Semanas dos guias | 15–21, 22–28, 29–35, 36–42, 43–49, 50–56: seis semanas de sete dias, sem buraco |
| Ritmo "cerca de duas páginas por semana" | **Arredondado para cima.** 19 a 23 páginas em 90 dias (12,9 semanas) dão de 1,5 a 1,8 por semana; o calendário põe 5 na primeira semana, 2 na segunda e 1 guia por semana depois (correção 12) |
| Medição do dia 28 | Tem objeto: 9 páginas no ar (7 da base, baratas, ratos); faltam exatamente os quatro guias que a ação cita |
| Medição do dia 56 | **Ação sem objeto em parte.** A ação manda "rever a ordem das páginas que faltam (praga × região e públicos)", mas o calendário termina praga × região no dia 55; no dia 56 faltam a página de preços (até o dia 60) e as duas de público. "Primeiros toques no botão" só tem objeto se houver licenciada (o botão nasce na ficha, dias 30–40) (correção 3) |
| Medição do dia 84 | Tem objeto; a contagem da licenciada está dita como condicional e como coisa da fase 3 |
| Revisão dos dias 80–90 "à luz da primeira medição" (linhas 31–32 e 70) | **Incoerente:** nessa data já houve a segunda (dia 56), e a terceira (dia 84) cai dentro da revisão (correção 11) |
| Dados da licenciada: "antes do dia 1" (linha 44) × "até o dia 30" (linha 124, premissa 4) | **Incoerente:** ou é condição do dia 1, ou é premissa de prazo até o dia 30. D, seção 8, exige antes do site só que uma licenciada **aceite** ser nomeada (correção 4) |
| "Sem elas, nenhuma outra página cumpre o desenho" (linha 24) × linha 56 e premissa 6 | **Mais forte que o próprio calendário:** a posição de "para dedetizadoras" é declarada PREMISSA de ordem, e nenhuma outra página depende de "como conferir a licença" para cumprir o desenho (o bloco "Quem executa" liga direto à consulta pública: D, seção 4.1) (correção 10) |
| Filtros de K sem sobreposição | **Sobrepõem-se.** O filtro da página da região (linha 61: zona, a região, contratar) pega os 20 termos da região, entre eles os 6 de praga que a linha 63 dá às páginas de praga × região e os 2 de público que as linhas 68–69 dão às páginas de público. Duas páginas para o mesmo termo é o que a regra citada na linha 78 manda evitar. O filtro da linha 63 não diz `local` (correções 7 e 8) |

## 6. Classificação de evidência, força e omissões

1. **Marcadas corretamente:** as sete ocorrências de "PREMISSA de ordem"; "observação de 4 buscas" (linha 28);
   INFERÊNCIA (linha 84); "Hipótese a testar, sem evidência A ou B" (linhas 91–93, igual a P, seção 7, item 4); os
   prazos de D e de A como premissa (linhas 101 e 116); a lista de seis premissas (seção 7).
2. **Sem marca, devendo ter:** linha 78 (ver sorteio, nº 28); linha 54 ("o botão só pode existir com o aviso e a
   política no ar" é leitura do plano sobre D, seção 5.1; a seção 5.2 citada trata do formulário, que não entra na
   versão 0); linha 68 (observação da amostra, sem base); a posição de "como conferir a licença" na segunda semana
   (não está na premissa 6).
3. **Mais forte que a fonte — página "como conferir a licença" e os 80 termos de confiança (linha 55).** Os 80 se
   dividem em 27 "dedetizadora com licença vigilância sanitária…", 26 "dedetizadora confiável…", 26 "melhor
   dedetizadora…" e 1 "como saber se dedetizadora é licenciada"; 60 são de bairro, 15 de região, 4 de cidade, 1 sem
   local. O plano destaca os quatro coletados (A10, H01, H02, H03) como termos a que a página responde, mas S só
   sustenta o H03. Em H01 e H02, S diz que "o resultado é de dedetizadoras e de anúncios (11 anúncios em 3 buscas)" e
   que a premissa "não sai confirmada" (S, seção 12.3, item 4; conferi: 5 + 6 + 0 anúncios). Em A10 ("melhor
   dedetizadora são paulo") os nove resultados são listas de "melhores" de diretório, de guia comercial e de
   dedetizadoras (`lote_01.jsonl`), e o desenho não deixa a página dizer "a melhor" sem critério exposto (D, seção
   4.3). Para o início, o plano faz a ressalva ("não tenta ranquear neles"); para esta página, não.
4. **Omissão de evidência contrária que está nas próprias fontes — premissa 3 (linhas 122–123).** O plano trata as
   buscas informativas como porta de entrada (marcado PREMISSA, certo), mas não diz que o resumo de IA apareceu nas
   10 buscas do grupo H (S, seção 12.1) nem que o guia registra, de um estudo dos Estados Unidos (Pew, 2025, classe
   B), menos clique em resultado tradicional quando há resumo de IA, com a leitura de que buscas informativas rendem
   menos visita (A, seção 7, linha do Pew: hipótese do guia, não medida no Brasil).
5. **"S (verificado em 14/11/2026)" (linha 12):** verdade, com força a mais. A verificação terminou às 00:00 de
   14/11 com "aprovado com ressalvas" e 22 correções, aplicadas pela sessão principal **sem nova leitura** (cabeçalho
   da verificação do item 4; painel, linha 96).
6. **Promessa de resultado:** nenhuma. O plano nega prazo e posição (linhas 116 e 125) e condiciona toda ação de
   medição a "se".
7. **Regra apoiada só em relato ou em vendedor:** nenhuma. Nenhuma fonte C ou D é citada; nenhum número de outro
   país entra no plano.
8. **Afirmação sem fonte:** "a página entra para ser honesta com quem chega" (linha 66) e "no escorpião, remeter ao
   serviço público de saúde" (linha 87) são escolhas do plano, sem marca; a ordem da página de preços está coberta
   pela premissa 6. Baixo peso.
9. **Observação que não justifica nada (linha 60):** os nomes dos perfis do bloco de mapa em "dedetização de cupim
   sp" conferem com os brutos (1ª vez: "Cupins SP" e "Oeste Pragas Dedetizadora de cupim"; 2ª vez: "Cupins SP" e
   "Prime Cupins"; dois de três nas duas), mas falam do bloco de mapa, onde o site não disputa, e não da posição do
   guia. Do jeito que está, parece razão e não é (correção 16).

## 7. Demais afirmações com fonte (conferidas uma a uma, fora do sorteio)

| Linha | Afirmação | Resultado |
|---|---|---|
| 42 | Fase 1: política do empregador, uma licenciada aceita, advogado (D, seção 8) | confere |
| 43 | Volume no Planejador (D, seção 8, letra d; S, seção 10) | confere |
| 44 | Dados da licenciada (D, seções 3.1, 4.1 e 7) | confere quanto aos campos; ver a incoerência de prazo (seção 5) |
| 45 | Fonte oficial para afirmação de saúde (D, seção 4.3, último parágrafo) | confere (em D é inferência do guia A; o plano não promove a regra) |
| 53 | Quem responde e intermediário (D, seção 2; A, seção 3) | confere |
| 53 | Nesses termos estão dedetizadoras, mapa e anúncios (S, seções 1 item 2, 3 e 7.3 item 1) | confere (grupo A: bloco em 10 de 10, anúncio em 8 de 10; 568 de 709) |
| 56 | "Para dedetizadoras" (D, seção 3.1); conversas na fase 1 (D, seção 8) | confere |
| 61 | Toda oferta nomeia quem executa (D, seções 4.1 e 4.4) | confere |
| 63 | Título e descrição curtos (P, seção 5) | confere (70 e 158 caracteres; "não é regra do Google") |
| 65 | Escorpião: 12 de 16 resultados de órgãos públicos e do Butantan (S, seção 1, item 7) | confere; recontei nos brutos: B05, 5 de 9; E05, 7 de 7 (um é da USP) |
| 66 | Preço: mesma página em primeiro em H04, H05 e H10; marketplace nas três; hipótese mais fraca (S, seções 12.1, 12.2 e 12.3 item 3) | confere (dedetizadoranovatec.com.br em 1º nas três; triider.com.br nas três) |
| 70 | Datas de conferência têm de continuar verdadeiras (D, seção 7) | confere |
| 85–86 | "Seguro" e ausência de efeito adverso; texto de medo (D, seção 4.3) | confere; bate com a RDC 622, art. 22, I e III, nas restrições, linhas 188–194 |
| 91–93 | Sete de dez páginas com subtítulo em pergunta (P, seção 4) | confere |
| 99 | Colunas `impressoes` e `visitas_*` | existem no CSV (`visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`, `visitas_chatgpt_user`) |
| 101 | Contagem da licenciada é da fase 3 (D, seção 10, premissa 5); critério de parada de cerca de 3 meses (PREMISSA) | confere; a frase entre aspas não é literal (correção 20) |
| 103–104 | Períodos iguais de 28 dias; marcar atualização central (A, seção 8) | confere |
| 110 | Página por bairro (D, seções 3.3 e 3.1) | confere |
| 112 | Não publicar tudo de uma vez (D, seção 7 e seção 10, premissa 13) | confere |
| 113 | IA sem revisão; página sem dado próprio (D, seção 7; A, seções 2.1 e 3) | confere |
| 114 | Sem oferta antes de licenciada (D, seção 4.4) | confere |
| 116 | O Google não dá prazo; 6 a 12 meses como premissa (A, seção 9) | confere |

## 8. Contra o desenho e contra as restrições do item 2

- **Tipos de página:** T1, T2, T3, T4, T6, T7, T8, T9, T10, T11 e T12 aparecem com o nome e a função de D, seção 3.1;
  T5 (bairro) fica em zero, como em D. As seis pragas dos guias são as seis de D.
- **Ordem das fases:** respeitada. O que é da fase 1 está em "Antes do dia 1"; o calendário é a fase 2; a contagem da
  licenciada (fase 3) aparece só como condicional no dia 84; bairro, formulário e gestão de perfil (fase 5) não
  aparecem. Tensão pequena: pelo desenho a fase 2 só começa com uma licenciada que aceitou ser nomeada, e o plano
  fala em "só se houver uma" (linha 29) — correção 22.
- **Página de oferta sem licenciada:** nenhuma. Ficha, região, praga × região e preços estão com "Sim"; as de público
  ficam "só o guia do que perguntar" sem licenciada, como T6 em D ("Sim, se houver licenciada").
- **Página por bairro:** nenhuma. **Formulário:** nenhum (só o botão; LGPD, art. 7º, § 5º, não é acionado).
- **Perfil de empresa do Google:** não aparece. **WhatsApp:** só o botão que abre o WhatsApp da licenciada.
- **RDC 622, art. 22:** "seguro" só aparece como palavra a não usar; toda oferta nomeia a licenciada; nenhum texto de
  medo. Nada vedado encontrado.

## 9. Forma

- Português: sim. Caminhos: absolutos em todos os arquivos do projeto citados.
- Números com base e fonte: sim, salvo a linha 68 (percentual sem base) e a linha 33 (ritmo arredondado).
- Nada dito como publicado, comprado, cadastrado ou enviado: confere ("Nada foi publicado"; verbos no condicional).
- Atos do owner ditos como dele: publicar, Search Console, Planejador, pedir dados à licenciada. Falta o sujeito na
  linha 99 (conferir sitemap, `robots.txt` e hospedagem) — correção 18.

## 10. O que não conferi

- O que o cabeçalho diz da primeira verificação ("6 afirmações mais fortes que a fonte ou incoerentes"; "19 correções
  pedidas"): não abri aquele relatório, por instrução.
- As fontes de segundo nível (o que A, S e P citam da web): não reabri nenhuma página.
- A seção 5 de A e os guias B, C e G do desenho: o plano não os cita.
- Se os termos de K são buscados por alguém: não há volume medido, e o plano o diz.

## 11. Correções pedidas

1. **Linhas 78–79.** Trocar por: "O desenho fixa seis guias de praga, cada um respondendo a várias dúvidas (D, seção
   3.1, T2), e pede poucas páginas, cada uma com algo próprio (D, seção 1, item 3; o total de páginas é PREMISSA).
   Daí — **INFERÊNCIA deste plano** — as dúvidas do mapa (21 termos informativos, 4 deles coletados no grupo H)
   viram **seções** dos guias, não páginas soltas. A regra de D, seção 3.2 ("uma página trata de uma busca e de suas
   variações próximas", marcada INFERÊNCIA) só manda não fazer duas páginas para a mesma busca:". **Linha 111**,
   coluna "Por quê": "D, seção 3.1 (seis guias, cada um com várias dúvidas) e seção 1, item 3 (poucas páginas);
   INFERÊNCIA deste plano".
2. **Linhas 84 e 85**, coluna "Onde entra". A mesma resposta em seis guias contraria a regra de D, seção 3.2. Trocar
   por: "Uma página só — "Como funciona" (T10), seção "o que perguntar à empresa"; os guias apontam para ela" e "Uma
   página só — "Como funciona" (T10), seção "cuidados que a empresa tem de informar"; os guias apontam para ela". Se
   a escolha for repetir nos guias, dizer por quê e marcar PREMISSA.
3. **Linha 100**, última coluna. Trocar "Rever a ordem das páginas que faltam (praga × região e públicos) pelo que
   apareceu" por: "Rever o que falta — a página de preços (até o dia 60) e as duas de público, e a ordem entre as
   duas — pelo que apareceu; as páginas de praga × região, se houver licenciada, já estão no ar desde o dia 55:
   rever o texto delas, não a ordem". Na coluna "O que olhar", depois de "primeiros toques no botão": "(só se houver
   página de oferta no ar)".
4. **Linha 44**, primeira coluna. Trocar o começo por: "Dados da licenciada por escrito, **antes das páginas de
   oferta (até o dia 30: premissa 4 da seção 7); não é condição do dia 1** — o desenho exige antes do site só que
   ela aceite ser nomeada (D, seção 8):".
5. **Linha 55**, coluna "Termos em K". Trocar por: "`intencao` = confiança (80 termos: 27 "dedetizadora com licença
   vigilância sanitária…", 26 "dedetizadora confiável…", 26 "melhor dedetizadora…" e 1 "como saber se dedetizadora é
   licenciada"; 60 são de bairro e 15 de região, e a página não tem conteúdo por local). A página responde ao H03;
   aos de "com licença" e "confiável", só por hipótese: nas buscas H01 e H02 o resultado é de dedetizadoras e de
   anúncios (11 anúncios; S, seção 12.3, item 4: a premissa não sai confirmada). **Não** tenta ranquear nos 26 de
   "melhor" (A10: listas de "melhores"; D, seção 4.3, não deixa dizer "a melhor" sem critério exposto). Coletados:
   A10, H01, H02 e H03".
6. **Linha 55**, coluna "Por que nesta ordem". Trocar "É o conteúdo em que o desenho aposta (D, seção 1, item 2:
   PREMISSA)" por "É um dos quatro elementos em que o desenho aposta — "como a pessoa confere" (D, seção 1, item 2:
   PREMISSA; D, seção 11: a premissa não saiu confirmada no grupo H)"; e "o primeiro é uma página de conteúdo" por
   "o primeiro é uma página de conteúdo de um site **não lido** (pelo endereço e pelo título; S, seção 12.1)".
   Acrescentar: "Pô-la na segunda semana é PREMISSA de ordem".
7. **Linha 61**, coluna "Termos em K". Trocar por: "`tipo_local` = zona, `local` = a região dela e `intencao` =
   contratar (20 termos por região; 19 no centro), **menos** os de praga que tiverem página de praga × região e os
   2 de `publico` = condomínio e restaurante, que são das páginas de público".
8. **Linha 63**, coluna "Termos em K". Acrescentar "`local` = a região da página" e a contagem: "(2 termos por praga
   e região: 1 de contratar, 1 de preço)".
9. **Linha 68.** Trocar "68% dos resultados são páginas internas de serviço ou outra e 1% é página por local (S,
   seção 4.2)" por "68% dos 117 resultados das 13 buscas do grupo F são páginas internas de serviço ou outra e 1% é
   página por local, pelo tipo lido no endereço (S, seção 4.2; observação da amostra)".
10. **Linhas 23–24.** Trocar "Sem elas, nenhuma outra página cumpre o desenho." por "As cinco primeiras são o que as
    demais precisam para cumprir o desenho (D, seções 2, 4.2 e 5.1); pôr "como conferir a licença" e "para
    dedetizadoras" na base é PREMISSA de ordem (premissa 6)." **Linhas 126–127 (premissa 6):** acrescentar "e a da
    página "Como conferir a licença"".
11. **Linhas 31–32 e 70.** Trocar "à luz da primeira medição" e "o que a primeira medição mostrou" por "à luz das
    medições dos dias 28 e 56 (a do dia 84 cai dentro da revisão)" e "o que as medições dos dias 28 e 56 mostraram".
12. **Linha 33.** Trocar "cerca de duas páginas por semana" por "em média, de 1,5 a 1,8 página por semana (19 a 23
    páginas em 12,9 semanas): 5 na primeira semana, 2 na segunda e, depois, 1 guia por semana mais as páginas de
    oferta". **Linha 121 (premissa 2):** "O ritmo: de 1,5 a 1,8 página por semana em média, com 5 na primeira
    semana".
13. **Linhas 122–123 (premissa 3).** Acrescentar ao fim: "Contra a premissa, nas mesmas fontes: o resumo de IA
    apareceu nas 10 buscas do grupo H, 4 delas informativas (S, seção 12.1), e o guia registra, de um estudo dos
    Estados Unidos (Pew, 2025, classe B), menos clique em resultado quando há resumo de IA, com a hipótese de que
    buscas informativas rendem menos visita (A, seção 7)".
14. **Linha 12.** Trocar "(verificado em 14/11/2026)" por "(verificado em 14/11/2026: aprovado com ressalvas; 22
    correções aplicadas pela sessão principal, sem nova leitura)".
15. **Linhas 58, 62 e 64.** Trocar "PREMISSA de ordem" por "PREMISSA de ordem: não há razão para esta posição; sem
    volume medido, qualquer ordem entre ratos, percevejo e pombos serve, e a medição do dia 28 ou o Planejador podem
    trocá-la".
16. **Linha 60.** Depois de "(brutos: … id B04r)", acrescentar: "— observação de uma busca e da repetição dela, sobre
    o bloco de mapa, onde o site não disputa; **não** é razão para a posição do guia". Ou tirar a frase.
17. **Linha 54.** Trocar "(D, seções 5.1 e 5.2)" por "(INFERÊNCIA a partir de D, seção 5.1: o aviso ao lado do botão
    remete à política, e o registro do servidor anota o endereço IP desde o primeiro acesso; a página "Excluir meus
    dados" está em D, seções 5.1 e 5.2)".
18. **Linha 99**, última coluna. Trocar "conferir sitemap" por "o owner confere (a hospedagem e o Search Console são
    dele) sitemap".
19. **Linha 115.** Trocar a primeira coluna por ""24 horas" e "garantia" sem prova guardada dada pela licenciada;
    "seguro"; "a melhor" sem critério exposto; estrelas; lista de bairros" e a segunda por "D, seções 2 (estrelas),
    3.4 (lista de bairros) e 4.3; P, seção 6".
20. **Linha 101.** Usar a frase literal do desenho: "em cerca de 3 meses não houver impressão nenhuma" (D, seção 8,
    fase 2), ou tirar as aspas.
21. **Linha 66**, coluna "Termos em K". Acrescentar: "dos 18, 6 são gerais e 12 são de praga, 6 deles de pragas sem
    guia (formigas, pulgas, mosquito, carrapatos, aranhas, traças): a página só responde aos que tiverem preço
    informado pela licenciada".
22. **Linha 29.** Trocar "(só se houver uma)" por "(pelo desenho, a fase 2 só começa com uma licenciada que aceitou
    ser nomeada — D, seção 8; estas páginas dependem ainda de os dados dela chegarem por escrito)".
23. **Linhas 7–8.** Acrescentar depois de "respostas dele": ", de ele aprovar o desenho, que é proposta e não plano de
    execução (D, cabeçalho),".
24. **Depois da linha 74** (opcional, é a conta que o portão sugere). Acrescentar: "Com uma licenciada numa região,
    os filtros acima apontam para até 168 dos 1.260 termos (13%). Ficam sem página, por escolha (seção 6), os 371 de
    urgência e 845 dos 905 de bairro."
