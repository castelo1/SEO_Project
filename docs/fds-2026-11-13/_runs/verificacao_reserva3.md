# Verificação independente — fila de reserva, tarefa 3 (plano de conteúdo de 90 dias)

- **Quando:** sábado, 14/11/2026, 00:01 (Brasília, lido de `TZ=America/Sao_Paulo date`). A leitura começou às 23:57 de
  13/11.
- **Quem:** verificador independente, em contexto limpo, sem a conclusão de quem produziu.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` (118 linhas; versão do commit
  `c6fda27`, de 13/11/2026 23:47). Lido inteiro. **Não foi editado**; nenhum outro arquivo foi editado.
- **Portão (transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 73):** "Plano de
  conteúdo de 90 dias: quais páginas primeiro e por quê, apontando para o mapa de palavras-chave."
- **O que abri para conferir:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (inteiro);
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (inteiro);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` (seções 2, 3, 4, 8 e 9);
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` (inteiro);
  `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (1.260 linhas, lido com Python, só leitura);
  `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` e
  `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv`;
  `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_02.jsonl` (registro B04) e
  `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_01.jsonl` (registro B04r);
  `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` (só a linha do bloco
  "[A ESCREVER]").
- **Limite desta verificação:** o mapa de busca ("S") estava sendo conferido por outro verificador; aqui só se
  conferiu se o que o plano cita está em "S", na seção citada, com o mesmo número e a mesma força. Nenhuma busca ao
  vivo, nenhum uso da web, nenhum navegador. Nenhum script do projeto foi rodado.

## 1. Veredito

**REPROVADO**, pela regra dada ("reprova com mais de 2 falhas de conteúdo"): achei **6 falhas de conteúdo** e 13
ressalvas menores.

O que isso quer dizer e o que não quer dizer:

- **A estrutura do portão está cumprida.** O plano cobre 90 dias, diz quais páginas vêm primeiro e por quê, e cada
  linha do calendário aponta para o mapa de palavras-chave por um filtro de colunas que existe e devolve linhas. As
  contagens "79", "2", "2", "2", "2", "1", "1", "8" e "9" batem. Os 11 tipos de página existem no desenho com o nome e
  a função dados. A soma "de 19 a 23" fecha e cabe nas "19 a 29". Não há promessa de resultado. O aviso de que não há
  volume medido está no alto, em negrito.
- **As 6 falhas são de frases, não de desenho:** uma afirmação mais forte que a fonte, duas incoerências internas de
  datas, um identificador que não sai do filtro dado, uma afirmação sem base e uma remissão que não diz o que o plano
  diz. Todas se corrigem com troca de redação em seis linhas. Depois de aplicadas, basta reler as linhas corrigidas.

## 2. Falhas de conteúdo (6)

| # | Linha do artefato | O que está escrito | O que a fonte diz | Por que é falha |
|---|---|---|---|---|
| F1 | 22–24 | as buscas informativas "são as únicas da amostra em que o primeiro resultado nem sempre é de dedetizadora (S, seção 12)" | Em S, seção 12.1, o primeiro resultado de H01 (busca de **confiança**) é ohub.com.br, um diretório; H03 (confiança) abre com um domínio "não lido". Na amostra principal, S, seção 7.2, põe governo em 5 das 79 primeiras posições e diretório em 1; S, seção 4.1, põe prefeitura.sp.gov.br em primeiro em 4 buscas. E H09, que é informativa, abre com uma dedetizadora. O que S afirma (seção 12.3, item 1) é só: "nas buscas de informação há resultado que não é de dedetizadora (…) *(observação de 4 buscas)*" | "As únicas" não está em S e é contrariado pela própria seção 12.1 |
| F2 | 22 | "Dias 15 a 45 — seis guias de praga, um por semana" | O calendário do próprio plano (linhas 53 a 61) põe os guias nos dias 15–21, 22–28, 29–35, 36–42, 43–49 e 50–56 | Seis semanas a partir do dia 15 terminam no dia 56, não no 45. O resumo de uma página contradiz o calendário |
| F3 | 62 | Termos em K: "`intencao` = preço e `tipo_local` = cidade; os 3 coletados: H04, H05 e H10"; e, na justificativa, "nas três buscas de preço coletadas" | O filtro devolve 17 linhas; as coletadas entre elas são **A05, H04 e H10**. H05 ("tabela de preço dedetização") tem `tipo_local` = "sem local" e fica fora do filtro. Em K há **quatro** termos coletados com `intencao` = preço (A05, H04, H05, H10) | O identificador citado não sai do filtro descrito; e "as três buscas de preço coletadas" são as três do grupo H, não todas as coletadas |
| F4 | 51 | "É o conteúdo que só este site se propõe a ter." | S, seção 12.1: o primeiro resultado de H03 é uma página "como conferir" (não lida); S, seção 12.3, item 2: "já tem resposta oficial em segundo lugar (…) e um site de conteúdo em primeiro"; S, seção 9, item 2: algumas dedetizadoras já têm páginas com esses termos (3 de 9 resultados em H02). O desenho trata o diferencial como PREMISSA (D, seção 1, item 2, e seção 10, premissa 1) | Afirmação de fato sem base, contrariada pela frase seguinte da mesma célula |
| F5 | 52 | "Para dedetizadoras (T12) (…) precisa existir antes da segunda conversa do owner (D, seção 3.1)" | D, seção 3.1, diz para que serve T12 (como uma licenciada entra, o que é exigido dela, como é cobrada). Não fala em "segunda conversa". Em D, seção 8, as conversas com licenciadas são da fase 1, "validar sem site", antes de o site existir | A remissão não diz aquilo, e a razão dada não combina com a ordem das fases do desenho |
| F6 | 94 | Dia 56: "Reordenar os guias que faltam pelo que apareceu" | Pelo calendário do plano, o sexto e último guia (escorpião) fecha no dia 56. No dia 28 é que ainda faltam quatro (cupim, percevejo, pombos, escorpião) | No dia 56 não falta guia nenhum: a ação não tem objeto |

## 3. O portão, ponto a ponto

| Pergunta | Resultado |
|---|---|
| Cobre 90 dias? | Sim: dias 1 a 90, com paradas nos dias 28, 56 e 84 (linhas 20 a 32 e 47 a 67). Ressalva: F2 |
| Diz quais páginas vêm primeiro e por quê? | Sim: regra geral nas linhas 14 a 16 (base; depois o que não depende de licenciada; depois o que depende) e coluna "Por que nesta ordem" em cada linha. Ressalvas: F1, F4, F5 e R10 |
| Cada página aponta para o mapa de um jeito que dá para seguir? | Sim: os filtros usam colunas e valores que existem em K e devolvem linhas. Três linhas dizem "—" com o motivo (página obrigatória; página que não é de busca; revisão). Ressalva: F3, R1 e R2 |

## 4. Tabela dos filtros (aplicados em `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, só leitura)

Colunas do arquivo: `termo`, `praga`, `tipo_local`, `local`, `intencao`, `publico`, `volume`, `origem_do_termo`,
`id_na_coleta`, `situacao_na_coleta`. 1.260 linhas; `volume` = "não medido" nas 1.260 (confere com a linha 13 do plano).
Valores que o plano usa e que existem: `praga` = geral, baratas, ratos, cupim, percevejo, pombos, escorpião;
`tipo_local` = cidade, zona; `local` = zona leste, zona norte, zona oeste, zona sul, centro de são paulo; `intencao` =
contratar, preço, confiança, informativa; `publico` = condomínio, restaurante.

| Linha do plano | Filtro | Linhas devolvidas | Contagem no plano | Confere? |
|---|---|---|---|---|
| 49 (Início, T1) | `tipo_local` = cidade, `praga` = geral, `intencao` = contratar | 24 | não dá número | Filtro válido. Ver R1: 13 das 24 são de público (restaurante 4, condomínio 3, empresa 3, escola 2, apartamento 1) |
| 50 (T11) | — | — | — | Sem termo, com motivo |
| 51 (T8) | `intencao` = confiança | 79 | "79 termos" | **Sim** |
| 51 (T8) | os coletados dentro do filtro | 3: H01, H02, H03 | "os 3 coletados: H01, H02 e H03" | **Sim** |
| 52 (T12) | — | — | — | Sem termo, com motivo |
| 53 (baratas) | `praga` = baratas, `intencao` = informativa | 2 | "2 termos" | **Sim** |
| 53 (baratas) | `praga` = baratas, `tipo_local` = cidade | 3 (contratar, urgência "24 horas", preço) | não dá número | Filtro válido. Ver R2 |
| 54 (ratos) | `praga` = ratos, `intencao` = informativa | 2 | "2 termos" | **Sim** |
| 56 (cupim) | `praga` = cupim, `intencao` = informativa | 2 | "2 termos" | **Sim** |
| 57 (T7 e T4) | `tipo_local` = zona, `local` = a região, `intencao` = contratar | 98 nas cinco regiões; por região: zona leste 20, zona norte 20, zona oeste 20, zona sul 19, centro de são paulo 19 | não dá número | Filtro válido |
| 58 (percevejo) | `praga` = percevejo, `intencao` = informativa | 2 | "2 termos" | **Sim** |
| 59 (T3) | `praga` = a da página, `tipo_local` = zona, `intencao` = contratar e preço | 10 por praga nas cinco regiões; 2 por praga × região (testado nas seis pragas, com zona oeste) | não dá número | Filtro válido |
| 60 (pombos) | `praga` = pombos, `intencao` = informativa | 1 | "1 termo" | **Sim** |
| 61 (escorpião) | `praga` = escorpião, `intencao` = informativa | 1 | "1 termo" | **Sim** |
| 62 (T9) | `intencao` = preço, `tipo_local` = cidade | 17 | não dá número | Filtro válido |
| 62 (T9) | os coletados dentro do filtro | 3: **A05**, H04, H10 | "os 3 coletados: H04, H05 e H10" | **Não** (F3): H05 tem `tipo_local` = sem local |
| 64 (condomínio) | `publico` = condomínio | 8 | "8 termos" | **Sim** |
| 65 (restaurante) | `publico` = restaurante | 9 | "9 termos" | **Sim** |

**Identificadores H01 a H10 e a intenção de cada um em K:** H01, H02, H03 = confiança; H04, H05, H10 = preço; H06,
H07, H08, H09 = informativa. O plano usa as mesmas intenções. Confere (a falha de F3 é no `tipo_local` de H05, não na
intenção).

**Termos entre aspas da seção 4 (linhas 79 a 83):** os nove existem em K com `intencao` = informativa.

| Termo | `praga` | Coletado? |
|---|---|---|
| como acabar com baratas em apartamento | baratas | sim (H07) |
| barata de esgoto como eliminar | baratas | não buscado |
| quanto tempo dura dedetização | geral | sim (H09) |
| de quanto em quanto tempo dedetizar apartamento | geral | não buscado |
| dedetização é segura para pets | geral | sim (H08) |
| dedetização vale a pena | geral | sim (H06) |
| como saber se tem cupim | cupim | não buscado |
| como identificar percevejo de cama | percevejo | não buscado |
| apareceu escorpião em casa o que fazer | escorpião | não buscado |

Só 4 dos 9 foram coletados no grupo H; a frase da linha 74 ("as dúvidas coletadas no grupo H") vale para esses 4 (R3).
Dos 21 termos informativos de K, 7 não têm destino no plano: os de formigas, pulgas, mosquito, carrapatos, aranhas e
traças (pragas sem guia na versão 0) e "dedetização condomínio é obrigatória" (R4).

## 5. Calendário, linha por linha

| Linha | Página | Tipo existe em D 3.1 com esse nome e função? | Razão e remissões | Resultado |
|---|---|---|---|---|
| 49 | Início (T1); Quem somos e Como funciona (T10) | Sim (T1, 1 página; T10, 2 páginas) | D, seção 2: o site se declara intermediário; "quem somos" diz quem responde. A, seção 3: "quem, como e por quê" e "transparência de um intermediário". S, seção 3: grupo A com bloco de mapa em 10 de 10 e anúncio em 8 de 10. Que o orgânico é de dedetizadoras está em S, seções 1 (item 2) e 7.3 (item 1), não na seção 4 | Confere; R5 |
| 50 | Política de privacidade; Excluir meus dados (T11) | Sim (2 páginas) | D, seção 5.1: o aviso ao lado do botão manda ver a política; D, seção 5.2: página "Excluir meus dados". "O botão só pode existir com…" é leitura do plano, coerente com as duas seções | Confere |
| 51 | Como conferir a licença (T8) | Sim | "O segundo resultado é a consulta pública do estado e o primeiro é uma página de conteúdo": S, seção 12.2 (tabela, linha Confiança) e 12.3, item 2. Mesmo número, mesma força. "Passo a passo ainda não lido": S 12.3, item 2, e D, premissa 10. A primeira frase da célula não tem base | **F4** |
| 52 | Para dedetizadoras (T12) | Sim | A remissão a D, seção 3.1, não sustenta "antes da segunda conversa do owner" | **F5** |
| 53 | Guia de baratas (T2) | Sim (T2 lista as seis pragas do plano) | Marcado PREMISSA de ordem. Página-modelo do protótipo é de baratas (P, linha 9). H07: primeiro resultado br.envu.com, 0 anúncio (S, seção 12.1). S ressalva "não lido; pelo endereço, site de fabricante"; o plano tira a ressalva | Confere; R6 |
| 54 | Guia de ratos (T2) | Sim | PREMISSA de ordem | Confere |
| 55 | Primeira medição (dia 28) | — | Seção 5 | Ver seção 9 abaixo |
| 56 | Guia de cupim (T2) | Sim | PREMISSA de ordem. Frase do bloco de mapa conferida nos brutos (seção 7 abaixo): confere. O plano cita só `repeticao_01.jsonl`; a primeira vez está em `lote_02.jsonl` | Confere; R7 |
| 57 | Ficha da licenciada (T7) e região (T4) | Sim | D, seção 4.1 (bloco "Quem executa", obrigatório em T3, T4, T5, T6, T7) e 4.4 (não há página de oferta sem empresa nomeada) | Confere |
| 58 | Guia de percevejo (T2) | Sim | PREMISSA de ordem | Confere |
| 59 | Praga × região (T3), 1 a 5 | Sim ("meta inicial: 1 a 5") | T2 "leva às páginas T3" (D 3.1). P, seção 5: título de 98 para 70 caracteres e descrição de 195 para 158 | Confere |
| 60 | Guia de pombos (T2) | Sim | PREMISSA de ordem | Confere |
| 61 | Guia de escorpião (T2) | Sim | "12 de 16 resultados são de órgãos públicos e do Instituto Butantan": S, seção 1, item 7, mesmo número. "O guia que mais depende de fonte oficial" é juízo do plano, sem marca | Confere; R8 |
| 62 | Preços (T9) | Sim (preços informados por escrito, com data) | S, seção 12.1: nas três buscas de preço do grupo H o primeiro resultado é **a mesma página** de "tabela de preço" de **uma** dedetizadora; S 12.2: "triider nas três". O plano põe no plural e diz "não porque haja lacuna"; S diz que a hipótese da lacuna "fica mais fraca" | **F3** (filtro); R9 (redação) |
| 63 | Segunda medição (dia 56) | — | Seção 5 | **F6** |
| 64 | Público: condomínio (T6) | Sim | "68% … 1%": S, seção 4.2, grupo F: 68 em "página interna de serviço **ou outra**" e 1 em "página interna por local". O plano omite "ou outra". Página de segmento: S 4.2, último item | Confere; R9 |
| 65 | Público: restaurante (T6) | Sim | O bloco "[A ESCREVER, com fonte oficial]" existe em `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 93 | Confere |
| 66 | Revisão (dias 80–90) | — | D, seção 7 (aviso de licença perto de vencer: "mantém verdadeiro o que a página afirma"); as duas frases entre aspas vêm de D, seção 3.4 | Confere |
| 67 | Terceira medição (dia 84) | — | Seção 5 | Ver R12 |

**Contagem (linhas 69–70):** base = T1 (1) + T10 (2) + T11 (2) + T8 (1) + T12 (1) = 7. 7 + 6 + 1 + 1 + (1 a 5) + 1 + 2 =
19 a 23. Fecha. D, seção 3.1: 16 fixas + T3 (1 a 5) + T4 (1 a 5) + T7 (1 a 3) = 19 a 29; com uma licenciada, T4 = 1 e
T7 = 1, logo 19 a 23. Cabe. As 16 fixas do desenho são as 7 + 6 + 1 (T9) + 2 (T6) do plano. Confere.

**Ritmo (linha 29):** 19 a 23 páginas até o dia 80 dão de 1,7 a 2,0 por semana. "Cerca de duas" confere como média;
a primeira semana tem 5 páginas e as semanas 3 e 4 têm 1 cada. Não contraria D, seção 7 ("dezenas de uma vez").

## 6. Contra o desenho

| Ponto | Resultado |
|---|---|
| Ordem das fases | O plano começa na fase 2 e põe a fase 1 como condição (linhas 4–5 e 34–41). Confere com D, seção 8. Duas ressalvas: F5 (conversa com licenciada depois do site no ar) e R12 (contagem da licenciada, que D põe na fase 3, aparece no dia 84) |
| Página de oferta sem licenciada | Não há. Linhas 25, 57, 59, 62 e 107. Confere com D 4.4 |
| Página por bairro | Não há (linhas 29–30, 94 e 103). Confere com D 3.1 (T5 = 0) e 3.3. Ressalva R11 na redação da linha 103 |
| Formulário | O plano não menciona formulário; só o botão (linha 94). Confere com D 5.2 |
| O que cada página exibe | O plano não detalha e não contradiz. Linha 57 repete D 4.1 |
| Ritmo de publicação | Confere (D, seção 7 e premissa 13); marcado PREMISSA nas linhas 105 e 114 |
| Critério de parada | Linha 95: "cerca de 3 meses sem impressão nenhuma (prazo PREMISSA)". D, seção 8, fase 2: "em cerca de 3 meses não houver impressão nenhuma (prazo PREMISSA…)". Confere; as aspas do plano são paráfrase, não citação literal |

**Remissões "D, seção X" conferidas (todas existem):** 2; 3.1; 3.2 (última linha: uma página por busca e variações
próximas); 3.3 (três condições); 4.1; 4.3 (inclusive o último parágrafo, sobre fonte oficial nas páginas T2); 4.4;
5.1; 5.2; 7; 8 (fase 1, letra d: volume no Planejador; fase 2); 10 (premissa 13). Dizem o que o plano diz, salvo:
linha 52 (F5); linha 40 ("pragas, preços com data" estão em D 3.1 e 7, não em 4.1 — R13); linha 80 (R13).

## 7. Contra o mapa de busca ("S") e os brutos

| Afirmação do plano | Onde está em S | Mesmo número e força? |
|---|---|---|
| Linha 22–24: informativas são "as únicas…" | S 12.1 e 12.3, item 1 | **Não** (F1) |
| Linha 49: dedetizadoras, mapa e anúncios nos termos de cidade | S, seção 3 (grupo A: mapa 10/10, anúncio 8/10); "dedetizadoras" em S 1 (item 2) e 7.3 (item 1) | Sim; seção citada incompleta (R5) |
| Linha 51: consulta pública em segundo, página de conteúdo em primeiro | S 12.2 e 12.3, item 2 | Sim |
| Linha 53: primeiro resultado de fabricante, nenhum anúncio | S 12.1, H07: "0" anúncios; "não lido; pelo endereço, site de fabricante de produto" | Número sim; força maior no plano (R6) |
| Linha 61: 12 de 16 resultados de órgãos públicos e do Instituto Butantan | S, seção 1, item 7 | Sim |
| Linha 62: "tabela de preço" em primeiro; marketplace nas três | S 12.1 (H04, H05, H10: a mesma página de uma dedetizadora) e 12.2 ("triider nas três") | Sim no fato; plural e "não porque haja lacuna" são mais fortes que S (R9) |
| Linha 64: 68% e 1% | S, seção 4.2, grupo F | Sim; falta "ou outra" (R9) |
| Linha 39: volume pelo Planejador | S, seção 10 | Sim |
| Linha 115–116: "observação de dez buscas" | S, seção 12 (10 buscas; as informativas são 4) | Sim |

**Frase do cupim (linha 56), conferida nos brutos, sem contar o perfil "Patrocinado":**

| Vez | Arquivo e id | Hora | Perfis do bloco (sem o patrocinado) | Com "cupim" ou "cupins" no nome |
|---|---|---|---|---|
| 1ª | `lote_02.jsonl`, B04 | 20:34 | Cupins SP; Oeste Pragas Dedetizadora de cupim; ARMOR Dedetizadora e Desentupidora | 2 de 3 |
| 2ª | `repeticao_01.jsonl`, B04r | 23:36 | Cupins SP; ARMOR Dedetizadora e Desentupidora; Prime Cupins | 2 de 3 |

**Confere:** dois de três, nas duas vezes. (Na primeira vez havia um quarto item, "Patrocinado", não contado. Na
primeira vez o nome do segundo perfil foi lido de uma linha que junta nome e categoria; tomei "Oeste Pragas
Dedetizadora de cupim" como nome.)

## 8. Contra os guias "A" e "P"

| Afirmação do plano | Onde | Resultado |
|---|---|---|
| "O Google não dá prazo; o guia trabalha com 6 a 12 meses como premissa" (linha 109) | A, seção 9: "O Google não dá prazo para SEO 'dar resultado'" (classe A) e "de 6 a 12 meses (…) número meu, premissa de desenho" | Confere |
| "Comparar sempre períodos iguais de 28 dias e marcar atualização central" (linha 97) | A, seção 8: "comparar semana ou 28 dias contra período igual anterior"; esperar ao menos uma semana após o fim de atualização central. A coluna `atualizacao_central_no_periodo` existe na planilha | Confere |
| "Sete das dez páginas (…) têm ao menos um subtítulo assim" (linhas 85–87) | P, seção 4: "Sete de dez têm ao menos um subtítulo em forma de pergunta"; P, seção 7, item 4: sem fonte A ou B de que ajude | Confere, com a marca de hipótese |
| "título e descrição curtos" (linha 59) | P, seção 5 | Confere |
| "24 horas", "garantia", estrelas, lista de bairros (linha 108) | P, seção 6; D 4.3, 2 e 3.4 | Confere |
| IA sem revisão; página sem dado próprio (linha 106) | A, seção 2.1 (conteúdo em escala; exemplo de IA) e seção 3 (IA generativa); D, seção 7 | Confere |
| "quem responde pelo site e que ele é intermediário" (linha 49) | A, seção 3 | Confere |

## 9. Evidência, medição e forma

**Evidência**

- Aviso de que não há volume medido e de que a ordem não é por volume: linhas 13 a 16, em negrito. Confere.
- PREMISSA de ordem marcada nos guias de baratas, ratos, cupim, percevejo e pombos, e na lista da seção 7. Não está
  marcada no escorpião (linha 61) nem na ordem dentro do bloco que depende de licenciada (R8, R10).
- Promessa de resultado (posição, tráfego, prazo): **nenhuma**. A linha 109 a recusa de modo expresso.
- Afirmação de fato sem base: F4 (linha 51); juízo sem marca na linha 61 (R8). Sobre praga, saúde e norma, o plano não
  afirma fato novo: manda levantar a norma de alimentação antes (linha 65) e pede fonte oficial (linhas 41 e 83).
- Seção 4 contra D 4.3: "seguro" vedado, com a instrução de não responder "é segura" (linha 81); sem texto de medo
  (linha 82); sem promessa de prazo (linha 80). Respeita. A extensão do art. 38 do CDC à duração do efeito é leitura do
  plano (R13).

**Medição (seção 5)**

- Colunas citadas: `impressoes` e `visitas_*` (`visitas_googlebot`, `visitas_bingbot`, `visitas_oai_searchbot`,
  `visitas_chatgpt_user`) existem em `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv`. Também existem as
  que o plano usa sem nomear: `posicao_media`, `leads_toque_no_botao`, `leads_validos`,
  `atualizacao_central_no_periodo`. Confere.
- Critérios contra a fase 2 do desenho ("páginas indexadas, impressões, visitas dos robôs de busca, se alguém toca no
  botão"; parada em "cerca de 3 meses" sem impressão): batem. Ressalvas: F6 e R12.
- Dias 28, 56 e 84 = três períodos de 28 dias. Coerente com a planilha.

**Forma**

- Português: sim. Caminhos absolutos: sim, em todas as ocorrências (linhas 8 a 12, 32 e 56).
- Nada afirmado como publicado, comprado, cadastrado ou enviado: confere (linhas 3 a 5).
- O que depende do owner dito como ato dele: confere nas linhas 4, 38 a 40 ("owner pede; licenciada fornece").
  Ressalva R12: na seção 5 falta dizer que quem abre o Search Console é o owner, e a linha 95 diz "decidir, com o
  owner", quando a decisão é dele.
- Data do cabeçalho: "sexta, 13/11/2026, às 23:46" é coerente com o commit de 23:46:52.

## 10. Ressalvas menores (13)

| # | Linha | Ressalva |
|---|---|---|
| R1 | 49 | O filtro devolve 24 termos; 13 são de público (restaurante, condomínio, empresa, escola, apartamento), que o plano destina a T6. Acrescentar `publico` = residencial/geral (11 termos) |
| R2 | 53 | Só o guia de baratas tem o segundo filtro (`tipo_local` = cidade), que devolve 3 termos, um deles de urgência "24 horas". Os outros cinco guias não o têm |
| R3 | 74 | "As dúvidas coletadas no grupo H": só 4 dos 9 termos citados foram coletados; os outros 5 são combinações geradas, não buscadas |
| R4 | 83 | "E as demais → o guia da praga correspondente": 6 termos informativos são de pragas sem guia (formigas, pulgas, mosquito, carrapatos, aranhas, traças) e "dedetização condomínio é obrigatória" não tem destino |
| R5 | 49 | "S, seções 3 e 4": a parte "lá estão as dedetizadoras" está em S, seção 1 (item 2) e 7.3 (item 1) |
| R6 | 53 | "Primeiro resultado de fabricante": S diz "não lido; pelo endereço". "A busca informativa coletada": foram quatro; esta é a única de praga |
| R7 | 56 | Os brutos da primeira vez estão em `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_02.jsonl` (id B04); o plano cita só o da repetição |
| R8 | 61 | "Por último entre os seis" é escolha (o dado de S não impõe a posição) e "o guia que mais depende de fonte oficial" é juízo: marcar PREMISSA |
| R9 | 62 e 64 | Linha 62: é a mesma página de uma dedetizadora nas três buscas; S diz que a hipótese da lacuna "fica mais fraca", não que não há lacuna. Linha 64: a coluna de S é "página interna de serviço ou outra" |
| R10 | 57 a 65 e 111 a 118 | A ordem dentro do bloco que depende de licenciada (ficha e região; praga × região; preços; públicos por último; condomínio antes de restaurante) é escolha e não está na lista de premissas |
| R11 | 103 | "Nenhuma existe nos primeiros 90 dias": a condição 1 de D 3.3 (licenciada que declara atender o bairro) pode valer a partir do dia 30. O certo é que as três não valem juntas e que D 3.1 fixa T5 = 0 na versão 0 |
| R12 | 93 a 95 | Falta dizer que quem abre o Search Console é o owner (D, seção 6). Linha 95: a contagem da licenciada é da fase 3 do desenho e depende de ela aceitar contar (D, premissa 5); "decidir, com o owner" deve ser "o owner decide" |
| R13 | 40 e 80 | Linha 40: "pragas" e "preços com data" vêm de D, seções 3.1 (T7 e T9) e 7, não de 4.1. Linha 80: D 4.3 cita o CDC, art. 38, para "24 horas", "garantia" e "melhor preço" sem prova; aplicá-lo à duração do efeito é INFERÊNCIA do plano |

## 11. Correções pedidas (numeradas; linha do artefato e redação certa)

**De conteúdo (as seis que decidem o veredito)**

1. **Linhas 22–24 (F1).** Trocar "que são as únicas da amostra em que o primeiro resultado nem sempre é de
   dedetizadora (S, seção 12)" por: "onde, em três das quatro buscas coletadas, o primeiro resultado não é de
   dedetizadora (imprensa, um site que pelo endereço é de fabricante, uma loja) — S, seção 12.1; observação de 4
   buscas".
2. **Linha 22 (F2).** Trocar "Dias 15 a 45" por "Dias 15 a 56".
3. **Linha 62 (F3).** Em "Termos em K", trocar "os 3 coletados: H04, H05 e H10" por "os coletados nesse filtro: A05,
   H04 e H10; mais H05 ('tabela de preço dedetização'), que tem `tipo_local` = sem local". Na justificativa, trocar
   "Nas três buscas de preço coletadas" por "Nas três buscas de preço do grupo H (H04, H05 e H10)".
4. **Linha 51 (F4).** Trocar "É o conteúdo que só este site se propõe a ter." por "É o conteúdo em que o desenho
   aposta (D, seção 1, item 2: PREMISSA). Não é exclusivo:" e seguir com a frase que já está lá.
5. **Linha 52 (F5).** Trocar "precisa existir antes da segunda conversa do owner (D, seção 3.1)" por "diz o que é
   exigido dela e como ela entra (D, seção 3.1). Pô-la na segunda semana é PREMISSA de ordem; as conversas do owner
   com licenciadas são da fase 1, antes do site (D, seção 8)".
6. **Linha 94 (F6).** Trocar "Reordenar os guias que faltam pelo que apareceu" por "Rever a ordem das páginas que
   faltam (praga × região e públicos) pelo que apareceu"; e, se a intenção for reordenar guias, levar essa ação para a
   linha 93 (dia 28), quando ainda faltam cupim, percevejo, pombos e escorpião.

**Menores**

7. **Linha 49 (R1, R5).** Acrescentar ao filtro "`publico` = residencial/geral (11 termos)" e trocar "S, seções 3 e 4"
   por "S, seções 1 (item 2), 3 e 7.3 (item 1)".
8. **Linha 53 (R2, R6).** Tirar o segundo filtro ou restringi-lo a "`intencao` = contratar (1 termo)" e dá-lo também
   aos outros cinco guias; trocar "primeiro resultado de fabricante" por "primeiro resultado de um site que, pelo
   endereço, é de fabricante (não lido)"; trocar "da busca informativa coletada" por "da única busca informativa de
   praga coletada".
9. **Linha 56 (R7).** Citar os dois brutos: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/lote_02.jsonl` (id B04)
   e `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/repeticao_01.jsonl` (id B04r).
10. **Linha 61 (R8).** Abrir a célula com "PREMISSA de ordem." e trocar "é também o guia que mais depende de fonte
    oficial de saúde" por "é guia em que toda afirmação de saúde pede fonte oficial (D, seção 4.3, último parágrafo)".
11. **Linha 62 (R9).** Trocar "páginas de 'tabela de preço' de dedetizadoras estão em primeiro" por "a mesma página de
    'tabela de preço' de uma dedetizadora está em primeiro"; trocar "não porque haja lacuna" por "a hipótese de que
    preço com origem é lacuna ficou mais fraca (S, seção 12.3, item 3)".
12. **Linha 64 (R9).** Trocar "páginas internas de serviço" por "páginas internas de serviço ou outra".
13. **Linha 74 (R3).** Trocar "as dúvidas coletadas no grupo H" por "as dúvidas do mapa (21 termos informativos, 4
    deles coletados no grupo H)".
14. **Linha 83 (R4).** Acrescentar: "Os termos de formigas, pulgas, mosquito, carrapatos, aranhas e traças ficam sem
    página nos 90 dias (não há guia dessas pragas na versão 0); 'dedetização condomínio é obrigatória' vai para a
    página de condomínio (T6)".
15. **Linha 103 (R11).** Trocar "três condições; nenhuma existe nos primeiros 90 dias" por "três condições que têm de
    valer juntas; não valem nos primeiros 90 dias, e D, seção 3.1, fixa T5 = 0 na versão 0".
16. **Linhas 93 a 95 (R12).** Acrescentar, acima ou abaixo da tabela: "Quem olha o Search Console é o owner, na conta
    dele (D, seção 6)". Na linha 95, trocar "a primeira contagem da licenciada (contatos com código)" por "a primeira
    contagem da licenciada, se ela aceitar contar (no desenho, isso é da fase 3; D, premissa 5)" e "Decidir, com o
    owner, se a fase 2 continua" por "O owner decide se a fase 2 continua".
17. **Linha 40 (R13).** Trocar "D, seção 4.1" por "D, seções 3.1 (T7 e T9), 4.1 e 7".
18. **Linha 80 (R13).** Trocar "(CDC, art. 38 — D, seção 4.3)" por "(INFERÊNCIA a partir de D, seção 4.3, que cita o
    CDC, art. 38, para afirmação sem prova guardada)".
19. **Linhas 111 a 118 (R10).** Acrescentar premissa 6: "A ordem dentro do bloco que depende de licenciada (ficha e
    região; praga × região; preços; públicos por último; condomínio antes de restaurante)".

## 12. Achado fora do artefato (para quem cuida do mapa de palavras-chave)

Em `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, três consultas da coleta com região ou bairro no
termo estão com `tipo_local` = cidade: C01 ("dedetizadora zona sul sp"), D06 ("dedetização lapa sp") e D15
("dedetizadora penha sp"). E A09 ("quanto custa dedetização são paulo") está com `intencao` = contratar, não preço.
Isso não é erro do plano, mas entra no resultado dos filtros das linhas 49 e 62. Não mexi no arquivo.

## 13. O que não fiz

- Não conferi os números de "S" contra os brutos, salvo a frase do cupim (é tarefa do outro verificador).
- Não reli a seção 7 de A nem as seções de A fora das citadas pelo plano.
- Não abri as demais páginas do protótipo.
- Não executei memória corporativa, compound nem qualquer conector; não rodei `git` de escrita.
