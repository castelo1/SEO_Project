# Dez páginas que ranqueiam bem × a página-modelo do protótipo (fila de reserva, tarefa 2)

- **Estado:** escrito pela sessão principal em sexta, 13/11/2026, às 22:57 (Brasília, lido de `date`). Primeira
  verificação independente: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva2.md`
  (aprovado com ressalvas; os 100 valores da tabela batem com o arquivo de dados; 12 correções pedidas, aplicadas às
  23:10 e não relidas por terceiro). Em sábado, 14/11/2026, às 01:54, a contagem de palavras da página-modelo
  (seções 4 e 6) passou de 856 para 910, porque a segunda passada do item 7 mexeu no protótipo.
  **Segunda passada:** revisor novo, em contexto limpo,
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva2.md` (aprovado com ressalvas;
  2 falhas em 12 afirmações sorteadas; 12 achados). Os 12 achados foram aplicados por um corretor em sábado,
  14/11/2026, às 02:28 (Brasília, lido de `TZ=America/Sao_Paulo date`): 7 como o revisor propôs e 5 com ajuste;
  relatório em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes2_reserva2.md`. Esta
  correção mexeu só neste arquivo (o protótipo e o arquivo de dados ficaram como estavam) e não foi relida por
  terceiro.
- **O que é:** leitura da estrutura de dez páginas que apareceram entre os três primeiros resultados orgânicos na
  amostra do item 4, comparada com a página-modelo do protótipo
  (`/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`), e o registro do que mudou no
  protótipo por causa disso.
- **Dados:** `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` (uma linha por página, com todas as
  medidas; 37 campos, descritos na seção 2.1).
- **O que não é:** não é prova de por que essas páginas ranqueiam. São dez páginas, de oito sites, lidas uma vez.
  Correlação numa amostra assim não sustenta regra (classe de evidência: observação própria, não estudo).

## 1. Como as páginas foram escolhidas

Regra, aplicada a `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` como ele estava às 22:57 de 13/11/2026:
**709 resultados orgânicos de 79 buscas, grupos A a G**, feitas em 13/11/2026, das 20:26 às 21:16 (Brasil; conta
logada; o Google exibiu "São Paulo, SP" ou "Osasco, SP" como local, quando exibiu; amostra, não censo). O arquivo
tem hoje 795 resultados orgânicos de 89 buscas (recontado em 14/11/2026, às 02:24): depois da escolha entrou o grupo
H — 86 orgânicos de 10 buscas, das 23:18 às 23:31 de 13/11/2026 —, que **não foi usado**.

1. Contar, para cada página (domínio + caminho), em quantas buscas ela ficou entre os três primeiros orgânicos.
2. Tirar páginas de governo e a página da multinacional (rentokil.com, 4 aparições, 2 em primeiro; **não lida**). O
   caminho dela está cortado em 50 caracteres na planilha, como o de toda página de endereço longo (seção 2,
   limites), e o domínio consta como "Não abriu" na leitura de sites do item 4
   (`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md`, linha de rentokil.com, lida em
   14/11/2026 às 02:24).
3. Ficar com as quatro de mais aparições (16, 6, 6 e 4) e, entre as empatadas com 2, escolher de modo a cobrir os
   tipos de página: três de bairro, uma de cidade vizinha, uma de praga × cidade e uma de segmento. No máximo duas
   páginas por site.

As empatadas com 2 aparições eram 18; tirada a de governo, 17. A escolha de seis entre elas é minha, e outra pessoa
poderia escolher outras. Ficaram de fora as outras onze: três páginas de tabela de preço, uma de certificado, uma de
restaurantes, uma de zona da cidade, três de bairro (duas do keikodedetizadora.com.br e uma do grupoexpansao.com),
uma de serviço, genérica (ecoservicos.com.br), e uma segunda página do termitek.com.br, de cidade pelo que se lê do
endereço (cortado na planilha). Quatro dessas onze são de sites que já tinham duas páginas entre as dez: as duas de
bairro do keikodedetizadora.com.br, e uma tabela de preço e a página de zona do dedetizadora.srv.br.

**O que muda com o grupo H (recontado em 14/11/2026, às 02:24; a escolha não foi refeita).** Contando as 89 buscas,
a página 1 passa de 16 para 17 aparições entre os três primeiros (11 em primeiro, como antes) e as páginas 3 e 4
passam de 6 para 7 (nenhuma em primeiro); as outras sete não mudam. Três páginas de preço que estavam empatadas com
2 e ficaram de fora sobem: a tabela de preço de dedetizadoranovatec.com.br vai de 2 para 5 aparições (as 5 em
primeiro); a tabela de preço médio de dedetizadora.srv.br, de 2 para 4 (nenhuma em primeiro); a página de preços de
primordialdedetizacao.com.br, de 2 para 3 (nenhuma em primeiro). Pela regra do passo 3 aplicada às 89 buscas, as
quatro de mais aparições seriam 17, 7, 7 e 5: a quarta seria a tabela de preço de dedetizadoranovatec.com.br, e a
página 5 (4 aparições) ficaria empatada com a tabela de dedetizadora.srv.br. As dez páginas lidas são, portanto, as
bem colocadas **nas 79 buscas dos grupos A a G**; as buscas de confiança, preço e informação do grupo H não entraram
na escolha, e nenhuma página de tabela de preço foi lida.

## 2. Como foram lidas

- No navegador pessoal (um só navegador conectado; não é o profissional), numa aba aberta por esta sessão, entre
  22:50 e 22:53 de 13/11/2026. Só leitura: cada endereço foi aberto direto e, quatro segundos depois, um trecho de
  script **leu** a estrutura da página (contagens). Nenhum clique, nenhum formulário, nenhum aviso de cookies aceito,
  nenhum botão de WhatsApp ou de telefone tocado.
- O que o script conta: palavras do texto visível; tamanho do HTML; links (total, internos, de WhatsApp, de telefone);
  títulos e subtítulos; imagens; formulários; tipos de dados estruturados (JSON-LD); e a presença de algumas palavras.
  Números de telefone foram mascarados antes de sair do navegador; nenhum foi gravado.
- **Limites:**
  - uma leitura por página, quatro segundos depois de abrir: texto carregado mais tarde não entra (a página inicial
    de um dos sites deu só 218 palavras, provavelmente por isso);
  - **o instrumento não foi guardado (limite de reprodutibilidade):** o trecho de script que leu as páginas e a lista
    dos 25 nomes de bairros não estão no repositório (a busca pelos nomes de campo `canonSelf` e `htmlKB` só acha o
    arquivo de dados; `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` é o coletor das buscas do item 4,
    não o leitor destas páginas). O arquivo de dados também não traz a hora de cada leitura: só se sabe o intervalo
    (22:50 a 22:53) e a hora em que o arquivo foi gravado (22:54). Sem o trecho e sem a lista, "palavras do texto
    visível" e "bairros citados (de 25)" **não podem ser refeitos por outra pessoa do mesmo jeito**;
  - "palavra de licença" quer dizer que o texto contém "CEVS", "SIVISA", "licença sanitária", "licença de
    funcionamento" ou "alvará" — **não** que haja um número, nem que ele confira;
  - "bairros citados" conta quantos de 25 nomes de bairros de uma lista minha aparecem no texto (a lista não foi
    guardada: ver acima);
  - a palavra "seguro" foi achada em 3 das 10 páginas, mas o contexto não foi lido: não afirmo que seja promessa de
    ausência de risco;
  - "24 h", "garantia", palavra de licença e "CNPJ" foram procuradas só no corpo do texto visível, na leitura dos
    quatro segundos, que **não cobriu perguntas frequentes nem rodapé carregados depois**. A página 9 traz "24 h" e
    "garantia" no `<title>` e saiu "não" nas duas colunas; na página 1, o verificador independente achou "garantia"
    no conteúdo (perguntas frequentes, rodapé) e a minha leitura saiu "não"; e, também na página 1, o revisor da
    segunda passada achou palavras de licença nesses mesmos trechos (nota abaixo da tabela da seção 3; não
    conferido no navegador). Por isso as contagens dessas quatro palavras são **"ao menos"**: são pisos, não totais;
  - um dos blocos de dados estruturados da página 3 não pôde ser lido (ficou "erro" no arquivo de dados);
  - na coluna de dados estruturados, "organização" inclui `Organization` e `Corporation`; "negócio local" inclui
    `LocalBusiness`, `ProfessionalService` e `PestControl`;
  - "página", na contagem da seção 1, é domínio + caminho **cortado em 50 caracteres** (o coletor das buscas guarda
    só os 50 primeiros caracteres do caminho e descarta o que vem depois de `?`; na planilha, 122 caminhos orgânicos
    distintos têm exatamente 50 caracteres, 19 deles de páginas que ficaram entre os três primeiros nos grupos A a
    G). Dois endereços longos com o mesmo começo contariam como uma página só; nenhuma das dez lidas está nesse
    caso (os dez caminhos têm menos de 50 caracteres);
  - posição no Google é a da amostra do item 4 (uma noite, uma conta, um ponto de acesso).

### 2.1 Dicionário dos campos do arquivo de dados

O arquivo `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` tem 37 campos por linha e não trazia
dicionário. A tabela abaixo foi escrita na segunda passada, **só com o que dá para afirmar lendo os valores e este
documento**; como o trecho de script não foi guardado, a regra exata de cada contagem fica "não documentada".

| Campo | O que dá para afirmar | Regra exata |
|---|---|---|
| `host`, `path` | Domínio e caminho da página lida | — |
| `title` | Texto do `<title>`; em três páginas (2, 4 e 6) um número de telefone foi trocado por `[num]` | como o telefone foi reconhecido: não documentado |
| `titleLen` | Caracteres do `<title>` **antes** da troca por `[num]` (nas três páginas mascaradas é maior que o tamanho do texto gravado: 34, 58 e 56 contra 26, 49 e 47) | — |
| `descLen` | Caracteres da meta descrição (linha da seção 4) | — |
| `h1`, `h2`, `h3` | Quantidade de títulos de cada nível; a coluna "Subtítulos (h2+h3)" da seção 3 é a soma dos dois últimos | — |
| `h1txt` | Texto de um título principal (vazio na página 6, que tem `h1` = 0) | qual deles, quando há dois (página 5): não documentado |
| `hq` | Subtítulos em forma de pergunta (7 páginas com ao menos um: seção 4) | que níveis de título entram e como a pergunta é reconhecida: não documentado |
| `words` | Palavras do texto visível | o que conta como visível e como palavra: não documentado |
| `htmlKB` | Tamanho do HTML, em KB | se é em bytes ou em caracteres, e se KB é 1.000 ou 1.024: não documentado |
| `links`, `internos` | Links ao todo e links internos (o segundo nunca passa do primeiro) | o que conta como interno: não documentado |
| `rodape` | Número inteiro, de 0 a 32; pelo nome, algo contado no rodapé | **não documentado**; não usado neste documento |
| `wa`, `tel` | Links de WhatsApp e links de telefone | que endereços contam: não documentado |
| `forms`, `iframes` | Quantidade de formulários e de quadros embutidos | — |
| `mapa` | Verdadeiro se há mapa embutido (falso nas dez) | como o mapa é reconhecido: não documentado |
| `imgs`, `imgsAlt` | Imagens; pelo nome, as que têm texto alternativo (nunca passa de `imgs`) | se texto alternativo vazio conta: não documentado; `imgsAlt` não é usado neste documento |
| `ld` | Tipos achados nos blocos de dados estruturados JSON-LD, separados por vírgula; "erro" marca bloco que não pôde ser lido (página 3) | a lista mistura tipos (`AggregateRating`) e um nome de propriedade (`aggregateRating`); a regra: não documentada |
| `micro` | Vazio em nove páginas; "WPFooter" na página 5; pelo nome, marcação do tipo microdados | **não documentado**; não usado |
| `canon`, `canonSelf` | Há endereço canônico; ele aponta para a própria página (verdadeiro nas dez) | como os endereços foram comparados: não documentado |
| `robots` | Conteúdo da meta tag `robots` | — |
| `viewport`, `lang` | Há meta tag `viewport`; valor do atributo `lang` (pt-BR nas dez) | — |
| `bairros` | Quantos dos 25 nomes da lista aparecem no texto | a lista não foi guardada |
| `lic`, `cnpj`, `h24`, `garantia` | Verdadeiro se a palavra foi achada no texto lido (limites acima: são pisos) | as grafias procuradas de "24 h": não documentado |
| `vedados` | Palavras de uma lista que foram achadas; só "seguro" aparece (páginas 4, 6 e 10) | a lista de palavras procuradas: não documentado |
| `estrelas`, `depo` | Verdadeiro ou falso; pelo nome, estrelas e depoimentos (`estrelas` só na página 10; `depo` só na página 4) | **não documentado**; **não usados nem conferidos** neste documento. O revisor da segunda passada, lendo a página 1 por ferramenta de resumo, viu um subtítulo "Depoimentos", e o campo `depo` dela está falso (não conferido no navegador) |

## 3. As dez páginas

Aparições entre os três primeiros (e na primeira posição), nas 79 buscas dos grupos A a G: 1 — 16 (11); 2 — 2 (1);
3 — 6 (0); 4 — 6 (0); 5 — 4 (0); 6 — 2 (2); 7 — 2 (1); 8 — 2 (1); 9 — 2 (1); 10 — 2 (1).

| # | Página | Tipo | Palavras | HTML (KB) | Links internos | Subtítulos (h2+h3) | Links de WhatsApp | Bairros citados (de 25) | Dados estruturados | Palavra de licença | "24 h" | "garantia" |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `dedetizadora.srv.br/` | página inicial | 466 | 105 | 69 | 8 | 3 | 0 | trilha, organização | não na leitura (ver a nota abaixo) | sim | não |
| 2 | `dedetizadora.srv.br/lapa/` | bairro | 771 | 90 | 44 | 7 | 3 | 3 | trilha, organização | sim | sim | sim |
| 3 | `eccocleandedetizacao.com.br/dedetizadora-sp.php` | cidade | 3227 | 447 | 462 | 7 | 3 | 5 | trilha, organização, negócio local, nota agregada, artigo | sim | não | não |
| 4 | `deltadedetizacao.com.br/dedetizacao-em-sao-paulo/` | cidade | 4017 | 384 | 227 | 78 | 8 | 10 | trilha, organização, negócio local, artigo | não | sim | sim |
| 5 | `keikodedetizadora.com.br/` | página inicial | 218 | 59 | 37 | 22 | 4 | 1 | trilha, organização, perguntas, serviço | não | sim | sim |
| 6 | `protecpragas.com.br/dedetizadora-osasco/` | cidade vizinha | 2287 | 235 | 249 | 52 | 14 | 25 | trilha, organização, nota agregada, perguntas, produto | não | sim | sim |
| 7 | `biosp.com.br/dedetizacao-de-carrapatos-e-pulgas-sao-paulo/` | praga × cidade | 1051 | 224 | 126 | 13 | 4 | 1 | trilha | sim | sim | não |
| 8 | `ecoservicos.com.br/dedetizadora-moema/` | bairro | 1326 | 97 | 47 | 12 | 5 | 2 | trilha, organização | não | sim | sim |
| 9 | `keikodedetizadora.com.br/servicos/dedetizadora-na-mooca` | bairro | 999 | 993 | 524 | 10 | 1 | 19 | trilha, organização, nota agregada, perguntas, serviço | não | não | não |
| 10 | `termitek.com.br/dedetizacao-de-condominios-sao-paulo/` | segmento (condomínio) | 1202 | 256 | 203 | 12 | 15 | 1 | trilha, organização, negócio local, nota agregada, perguntas | não | não | não |

**Nota à linha 1 (segunda passada, 14/11/2026).** O revisor da segunda passada, lendo a página 1 por uma ferramenta
que entrega o texto da página resumido por um modelo (não o HTML), achou "licença sanitária" e "alvará de
funcionamento" numa resposta das perguntas frequentes e, no rodapé, como rótulos seguidos de número
(`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva2.md`, "Releitura de três
páginas" e achado 1). **Não conferido no navegador:** é indício, não fato. A coluna segue o arquivo de dados, que
registra "não" para a leitura dos quatro segundos; o "não" das outras seis páginas tem o mesmo limite.

## 4. O que as dez têm em comum, e onde variam

As quatro dimensões pedidas na tarefa aparecem assim: **estrutura** (subtítulos, links internos, formulário,
subtítulo em pergunta), **tamanho** (palavras, KB), **dados estruturados** (coluna da seção 3 e contagens abaixo) e
**sinais locais** (bairros citados, marcação de negócio local, mapa embutido, palavra de licença, CNPJ, links de
telefone).

| Medida | Mínimo | Mediana | Máximo | Página-modelo do protótipo |
|---|---|---|---|---|
| Palavras no texto visível | 218 | 1.126,5 | 4.017 | 910 (eram 856 até 14/11/2026, 01:54, quando a segunda passada do item 7 trocou o parágrafo de bairros por uma remissão e acrescentou o campo "Dados pessoais" e o aviso completo ao lado do botão; contagem refeita com `html.parser`, texto do `body` sem `script`) |
| Tamanho do HTML (KB) | 59 | 229,5 | 993 | 11 (tamanho do arquivo em disco: 11.518 bytes em 14/11/2026; nas dez, o tamanho foi medido pelo script no navegador — as duas medidas não são a mesma) |
| Links internos | 37 | 164,5 | 524 | 14 links ao todo (todos internos; 3 deles são âncoras da própria página) |
| Subtítulos de segundo nível (h2) | 1 | 8 | 41 | 5 |
| Tamanho do `<title>` (caracteres) | 27 | 57,5 | 67 | era 98; agora 70 (acima do máximo das dez: seção 5) |
| Tamanho da meta descrição (caracteres) | 121 | 150 | 163 | era 195; agora 158 |
| Links de WhatsApp | 1 | 4 | 15 | nenhum link de WhatsApp de verdade: há 2 botões de EXEMPLO (um por empresa), cujo endereço é `#botao-de-exemplo` e não leva a lugar nenhum |
| Imagens | 7 | 17,5 | 168 | 0 |

- **Dez de dez** têm: trilha de navegação em dados estruturados; endereço canônico apontando para si; `viewport`;
  `lang="pt-BR"`; ao menos um link de WhatsApp.
- **Nove de dez** marcam organização em dados estruturados; **três** se marcam como negócio local; **quatro** trazem
  nota agregada de avaliações; **quatro** trazem marcação de perguntas e respostas.
- **Ao menos sete de dez** escrevem "24 h"; **ao menos cinco**, "garantia"; **ao menos três** trazem alguma palavra
  de licença no texto lido; **ao menos uma** traz "CNPJ". As quatro contagens são pisos (limites da seção 2).
- **Cinco de dez** têm formulário na página; **nenhuma** tem mapa embutido.
- **Sete de dez** têm ao menos um subtítulo em forma de pergunta.
- **Links de telefone** (medidos e não relatados até a segunda passada): de 0 a 14 por página, mediana 2,5; três
  páginas não têm nenhum (6, 7 e 9).
- Variam muito: tamanho do texto (de 218 a 4.017 palavras) e quantidade de links internos (de 37 a 524). Uma página
  de bairro tem 524 links internos e a de cidade vizinha cita os 25 nomes da minha lista de bairros. O destino desses
  links não foi medido, e **se isso se enquadra** no que a política de spam do Google chama de excesso de
  palavras-chave **não foi avaliado**. As duas páginas estão entre os três primeiros — nesta amostra, nesta noite.

## 5. O que mudou no protótipo, e por quê

| Mudança | Onde | Por quê | Base |
|---|---|---|---|
| `<title>` encurtado de 98 para 70 caracteres | `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | O Google pede título "descritivo e conciso", com a marca de forma breve. As dez páginas ficam entre 27 e 67 caracteres: **com 70, o título novo continua acima do máximo das dez** | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 4, linha "Link de título" (classe A; o Google não fixa número de caracteres); esta amostra, só como referência |
| Meta descrição encurtada de 195 para 158 caracteres | a mesma página | As dez ficam entre 121 e 163; o Google não fixa limite, mas corta | o mesmo guia, seção 4, linha "Trecho (snippet) e meta descrição" (classe A); esta amostra |
| O mesmo corte nos títulos e descrições das outras páginas (início: 69 e 158; restaurantes: 70 e 157) | `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` e `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | Coerência | idem |

Nada mais mudou por causa desta comparação. (O protótipo voltou a mudar em 14/11/2026, às 01:54, por outra razão — a
segunda passada do item 7 —, e é daí que vem a contagem de 910 palavras da seção 4.) O número de caracteres não é
regra do Google: é o que se viu em dez páginas.

**Ponto em aberto (segunda passada).** Os três títulos novos têm 70, 69 e 70 caracteres; o máximo visto nas dez é
67. A faixa das dez não foi atingida, e a base que resta para o corte é o "conciso" do Google, que não dá número. O
protótipo não foi mexido nesta correção: encurtar mais, ou deixar como está, fica para a sessão principal.

## 6. O que as dez fazem e o protótipo **não** copia, e por quê

| O que fazem | Quantas | O protótipo | Base da recusa |
|---|---|---|---|
| Nota agregada de avaliações em dados estruturados | 4 | Não tem estrela nem avaliação | `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, seção 2 (linha das avaliações: classe A para não agregar avaliação de outros sites e não marcar estrelas sobre si; "não mostrar estrela nenhuma" é PREMISSA do desenho, mais estrita que a regra), e `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 5 (estrelas e origem das avaliações) |
| Marcação de perguntas e respostas | 4 | Não usa | o resultado rico de perguntas frequentes deixou de existir em 07/05/2026 (desenho, seção 3.4) |
| Marcar-se como negócio local | 3 | O site não é negócio local; usa `Organization` | desenho, seção 2 (classe A para o tipo `Organization`; não usar `LocalBusiness` é INFERÊNCIA do desenho) |
| "24 h" e "garantia" | ao menos 7 e ao menos 5 | Não escreve, sem prova dada pela licenciada | desenho, seção 4.3 (CDC, arts. 36 e 38) |
| Dezenas ou centenas de links internos (destino não medido) | mediana de 164,5 links internos | 14 links; sem lista de bairros | desenho, seções 3.2, 3.3 e 3.4 (a política de spam do Google, lida na fonte, dá o bloco de texto que lista cidades e regiões como exemplo de excesso de palavras-chave; aplicar isso a "não fazer página por bairro" é classe A + INFERÊNCIA no desenho) |
| Texto longo (mediana de 1.126,5 palavras) | — | 910 palavras (856 antes da segunda passada), sem enchimento | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` registra que não há contagem de palavras que o Google prefira (seção 1.1) e que escrever até atingir uma contagem de palavras é sinal de conteúdo feito para o buscador (seção 3) |
| Formulário de orçamento na página | 5 | Só o botão (via A) | desenho, seção 5.2 ("Por que não na versão 0") |
| Imagens (mediana de 17,5) | — | Nenhuma | o protótipo é só HTML e CSS; foto real da licenciada pode entrar depois, com descrição verdadeira (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 4, linha de imagens) |

## 7. O que isto diz ao projeto (leitura minha, marcada)

1. **Parte das páginas que estão no topo faz o que o desenho recusa:** "24 h" em ao menos 7 das 10, "garantia" em
   ao menos 5, nota agregada em 4, lista extensa de bairros ou de links em 2. O desenho supõe que dá para aparecer sem
   isso; esta amostra **não confirma** a suposição, e ela não está na lista de premissas do desenho com essas
   palavras (a premissa 1 de lá trata de a licença e o preço atraírem busca). Fica registrada aqui como premissa.
2. **Na leitura, a licença apareceu em poucas dessas páginas:** ao menos 3 de 10 trazem alguma palavra de licença no
   texto lido. É piso: pode ser mais (nota da seção 3, sobre a página 1). O mapa de busca
   (`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, seção 7.3, item 4) registra, sobre os sites
   inteiros, que 12 de 67 sites de serviço lidos mostram um número de licença e que pelo menos outros 14 se dizem
   licenciados sem número. **As duas medidas não são a mesma** — aqui é palavra achada numa página, lá é número
   visto no site —, e em nenhuma das duas o número foi conferido.
3. **O único ajuste feito é de forma** (título e descrição mais curtos), e a base dele é a documentação do Google,
   não a contagem das dez: dez páginas lidas uma vez não sustentam ajuste nenhum (ver "O que não é", no começo). Do
   resto que as dez têm a mais que o protótipo, parte o desenho recusa — por regra lida na fonte ("24 h" e
   "garantia" sem prova; nota agregada copiada de outro site ou sobre si mesmo; bloco de texto com lista de
   bairros), por inferência do desenho (marcar-se como negócio local; não fazer página por bairro) ou por premissa
   mais estrita que a regra (nenhuma estrela) — e parte é escolha de fase ou não tem base para copiar (imagens,
   formulário, marcação de perguntas, texto mais longo).
4. **Subtítulos em forma de pergunta** aparecem em 7 das 10. O que os guias dizem, por motor:
   - **Google:** não há nos guias fonte A ou B de que isso ajude. O guia de busca orgânica
     (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 4, linha "Títulos") registra,
     classe A, que os títulos ajudam o leitor e ajudam o Google a escolher o título do resultado, e que a ordem e a
     quantidade deles não importam para a busca.
   - **Bing e Copilot (Microsoft):** o guia de respostas de IA
     (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`) registra recomendação da Microsoft, de
     10/02/2026, de títulos claros, tabelas e seções de perguntas e respostas — classe "A (orientação do motor, sem
     dado)" (seção 3, linha 198); põe entre as ações "um título por pergunta real", classe "A (Microsoft)", com a
     nota de que no Google não é requisito, mas não conflita (seção 7.1, linha 352); e lista "estruturar o texto
     para IA" como ponto **disputado** entre Microsoft e Google, sem dado de nenhum dos dois ("O que é disputado",
     item 3, linhas 479–481). Quem ganha com a afirmação: a Microsoft.

   Ou seja: há orientação de um motor (classe A, sem dado) e nenhuma medida de efeito. Não mexi no protótipo por
   isso; fica como hipótese para o plano de conteúdo.

## 8. O que não foi feito

- A página da multinacional (rentokil.com) não foi lida: o caminho está cortado em 50 caracteres na planilha e o
  domínio não abriu na leitura de sites do item 4 (seção 1, passo 2).
- A escolha das dez não foi refeita com o grupo H (seção 1): nenhuma página de tabela de preço foi lida.
- O trecho de script da leitura e a lista dos 25 bairros não foram guardados no repositório (seção 2); os campos
  `rodape`, `micro`, `imgsAlt`, `estrelas` e `depo` do arquivo de dados não foram usados nem conferidos (seção 2.1).
- A palavra de licença na página 1 (nota da seção 3) não foi conferida no navegador.
- Os títulos do protótipo continuam acima do máximo das dez (seção 5, ponto em aberto).
- O texto das páginas não foi lido por pessoa: não digo se o conteúdo é bom, original ou de molde.
- Velocidade de carregamento, tamanho total com imagens e versão de celular não foram medidos.
- Não repeti a leitura em outro dia.
