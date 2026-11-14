# Segunda passada — fila de reserva, tarefa 2 (dez páginas que ranqueiam × página-modelo do protótipo)

## Quem e quando

- Revisor independente, em contexto limpo (subagente), sem acesso à conclusão de ninguém. Não abri nenhum arquivo
  `verificacao*` nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só listei os
  nomes) e desconsiderei o que o artefato diz sobre a verificação anterior (linhas 3–6 e 47–50).
- Início: sábado, 14/11/2026, 02:01 (Brasília, lido de `TZ=America/Sao_Paulo date`). Relatório gravado às
  02:16 do mesmo dia (idem).
- Não editei artefato nenhum. Não rodei `git` de escrita (só `git log`, `git show` e `git status`). Não usei o
  navegador nem busca ao vivo.

## O que abri

| Arquivo (caminho absoluto) | Como | Hora da leitura |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` e `RODADA.md` | inteiros | 02:01 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` (144 linhas; alterado às 01:54:58) | inteiro | 02:01 |
| `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` (10 linhas, 37 campos cada; de 13/11, 22:54:29) | inteiro | 02:01 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` (alterado às 01:54:32) | inteiro, e medido por script | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html`, `para-empresas/restaurantes/index.html`, `privacidade/index.html` | medidos por script | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` | inteiro | 02:04 |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (1.180 linhas; alterado às 01:11:49) | inteiro, por script | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | seções 1.1, 2.1 (linhas 160–166), 3, 4, 5 e 8 | 02:04 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | linhas 190–198, 346–353, 476–482 | 02:07 |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` | seções 2, 3, 4, 5.2, 6, 7, 8 e 10 (premissas 1 a 8) | 02:04 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (**outro agente o editava: alterado às 02:10:57**) | buscas por trecho | 02:04, 02:06 e 02:11 |
| Histórico do git do protótipo (commits `d4379c1`, `44fda30`, `4d03f22`, `49ff823`) | `git show`, só leitura | 02:03 |
| Três das dez páginas, pela ferramenta de leitura de web (páginas 1, 7 e 9) | cinco consultas | 02:05–02:06 |

Scripts meus, só de leitura: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res2_medidas.py`,
`v2res2_serp.py` e `v2res2_sorteio.py` (mesma pasta).

## Portão, parte por parte

Portão (`RODADA.md`, fila de reserva, 2): "Análise de 10 páginas que ranqueiam bem (estrutura, tamanho, dados
estruturados, sinais locais), comparadas com a página-modelo do protótipo; ajuste o protótipo e diga o que mudou."

| Parte do portão | Onde está | Cumprida? |
|---|---|---|
| Dez páginas | seção 3 (tabela) e o `.jsonl` (10 linhas) | sim |
| "que ranqueiam bem" | seção 1: entre os três primeiros orgânicos da amostra do item 4; contagens batem com o recorte de 79 buscas (grupos A a G) | sim, com a ressalva do achado 3 (o arquivo hoje tem 89 buscas) |
| Estrutura | subtítulos (h2, h2+h3), links internos, formulário, subtítulo em pergunta (seções 3 e 4) | sim |
| Tamanho | palavras e tamanho do HTML (seções 3 e 4) | sim |
| Dados estruturados | coluna da seção 3 e contagens da seção 4 | sim |
| Sinais locais | bairros citados, marcação de negócio local, mapa embutido, palavra de licença, CNPJ, "24 h" (seções 3 e 4). O documento não usa o nome "sinais locais" | sim, com ressalva (achado 12) |
| Comparação com a página-modelo | coluna da direita da tabela da seção 4; seção 6 | sim |
| Ajuste do protótipo | títulos e descrições encurtados em três páginas (commit `44fda30`, 13/11, 22:57) | sim: existe no HTML de hoje |
| "Diga o que mudou" | seção 5; `LEIA-ME.md`, linhas 13–15 e 48 | sim |

## O que conferi

### (b) Tabelas contra o `.jsonl`

- Tabela das dez páginas (seção 3, linhas 63–72): **110 valores conferidos por script** (11 por linha, contando o
  endereço), **0 divergência**. A coluna de dados estruturados foi refeita com a regra das linhas 52–53
  (`Organization`/`Corporation` = organização; `LocalBusiness`/`ProfessionalService`/`PestControl` = negócio local).
- Mínimo, mediana e máximo (seção 4, linhas 78–85), recalculados:

| Medida | Mínimo | Mediana | Máximo | Bate com o documento? |
|---|---|---|---|---|
| Palavras | 218 | 1.126,5 | 4.017 | sim |
| HTML (KB) | 59 | 229,5 | 993 | sim |
| Links internos | 37 | 164,5 | 524 | sim |
| h2 | 1 | 8 | 41 | sim |
| `<title>` (caracteres) | 27 | 57,5 | 67 | sim |
| Meta descrição (caracteres) | 121 | 150 | 163 | sim |
| Links de WhatsApp | 1 | 4 | 15 | sim |
| Imagens | 7 | 17,5 | 168 | sim |

- Contagens das linhas 87–94, refeitas no `.jsonl`: trilha 10; canônico para si 10; `viewport` 10; `pt-BR` 10; ao
  menos um link de WhatsApp 10; organização 9; negócio local 3; nota agregada 4; perguntas 4; "24 h" 7; "garantia" 5;
  palavra de licença 3; CNPJ 1; formulário 5; mapa 0; subtítulo em pergunta 7; "seguro" 3. **Todas batem com o
  arquivo de dados.** (Se o arquivo de dados bate com as páginas é outra pergunta: ver a releitura abaixo.)

### (c) Página-modelo, medida por mim no HTML de hoje (11.518 bytes, alterado às 01:54:32)

| Medida | Documento | Medido | Bate? |
|---|---|---|---|
| Palavras do texto do `body`, sem `script` nem `style` (`html.parser`, espaço entre os nós de texto) | 910 | 910 | sim |
| A mesma, na versão anterior às 01:54 (`git show 49ff823^`) | 856 | 856 | sim |
| Tamanho do HTML | 11 KB | 11.518 bytes (11,5 kB; 11,2 KiB) | sim |
| Links (`<a>`) | 14 ao todo | 14 (todos internos; 3 são âncoras da própria página) | sim |
| h2 | 5 | 5 | sim |
| `<title>` | era 98; agora 70 | 98 no commit `d4379c1`; 70 hoje | sim |
| Meta descrição | era 195; agora 158 | 195 no commit `d4379c1`; 158 hoje | sim |
| Links de WhatsApp | 2 (um por empresa) | 2 botões com `href="#botao-de-exemplo"`; nenhum `href` de WhatsApp | sim, com ressalva (achado 8) |
| Imagens | 0 | 0 | sim |

Outras contagens de palavra da mesma página, para dar a ordem do erro do método: 897 (só "palavras" com letra ou
número), 915 (expressão regular de palavra), 895 (nós de texto colados). O número do documento é reproduzível pelo
método que ele declara.

### (d) Critério de escolha contra o `serp_sp.csv`

O arquivo tem hoje 1.180 linhas, **795 resultados orgânicos de 89 buscas** (grupos A a H). O grupo H (10 buscas, 86
orgânicos, das 23:18:29 às 23:30:54 de 13/11) entrou depois da escolha das páginas (documento escrito às 22:57). No
recorte dos grupos A a G (709 orgânicos, 79 buscas, das 20:26:51 às 21:16:03), que é o que o documento descreve:

| # | Página | Entre os três primeiros (em primeiro), A a G | Documento | Bate? | Com o grupo H |
|---|---|---|---|---|---|
| 1 | `dedetizadora.srv.br/` | 16 (11) | 16 (11) | sim | 17 (11) |
| 2 | `dedetizadora.srv.br/lapa/` | 2 (1) | 2 (1) | sim | 2 (1) |
| 3 | `eccocleandedetizacao.com.br/dedetizadora-sp.php` | 6 (0) | 6 (0) | sim | 7 (0) |
| 4 | `deltadedetizacao.com.br/dedetizacao-em-sao-paulo/` | 6 (0) | 6 (0) | sim | 7 (0) |
| 5 | `keikodedetizadora.com.br/` | 4 (0) | 4 (0) | sim | 4 (0) |
| 6 | `protecpragas.com.br/dedetizadora-osasco/` | 2 (2) | 2 (2) | sim | 2 (2) |
| 7 | `biosp.com.br/dedetizacao-de-carrapatos-e-pulgas-sao-paulo/` | 2 (1) | 2 (1) | sim | 2 (1) |
| 8 | `ecoservicos.com.br/dedetizadora-moema/` | 2 (1) | 2 (1) | sim | 2 (1) |
| 9 | `keikodedetizadora.com.br/servicos/dedetizadora-na-mooca` | 2 (1) | 2 (1) | sim | 2 (1) |
| 10 | `termitek.com.br/dedetizacao-de-condominios-sao-paulo/` | 2 (1) | 2 (1) | sim | 2 (1) |

- As quatro de mais aparições, tiradas governo e rentokil.com: 16, 6, 6 e 4 — bate. rentokil.com: 4 aparições (2 em
  primeiro), caminho cortado — bate.
- Empatadas com 2 aparições: 18, das quais 1 é de governo (prefeitura.sp.gov.br); sobram **17** — bate com a linha 27.
- As seis escolhidas entre as 17: três de bairro (Lapa, Moema, Mooca), uma de cidade vizinha (Osasco), uma de praga ×
  cidade, uma de segmento — bate. Dez páginas de oito sites, no máximo duas por site — bate.
- As 11 que ficaram de fora: 3 de tabela de preço, 1 de certificado, 1 de restaurantes, 1 de zona da cidade, **3 de
  bairro, 1 de serviço genérica e 1 de cidade** — a linha 28 só cita as quatro primeiras classes (achado 7).
- Com o grupo H, `dedetizadoranovatec.com.br/tabela-de-preco-de-dedetizacao/` passa de 2 para 5 aparições entre os
  três primeiros, todas em primeiro (achado 3).

### (e) "O que mudou no protótipo" existe no protótipo?

| Mudança declarada (seção 5) | No HTML de hoje | No histórico |
|---|---|---|
| Página-modelo: `<title>` de 98 para 70; descrição de 195 para 158 | 70 e 158 | commit `44fda30` (13/11, 22:57): 98→70, 195→158 |
| Início: 69 e 158 | 69 e 158 | o mesmo commit: 92→69, 202→158 |
| Restaurantes: 70 e 157 | 70 e 157 | o mesmo commit: 132→70, 210→157 |
| "Nada mais mudou" | — | o commit `44fda30` só tocou, no protótipo, essas seis linhas e três linhas do `LEIA-ME.md` |

A página de privacidade (título de 58, descrição de 123 caracteres) não foi tocada, e o documento não diz que foi.

### Remissões aos guias e ao desenho (abri cada seção citada)

| Linha | O que o documento atribui | O que a seção diz | Bate? |
|---|---|---|---|
| 104 | Google pede título "descritivo e conciso", com a marca de forma breve — guia orgânico, seção 4, classe A | linha 246 do guia: diz isso, classe A | sim |
| 105 | Google não fixa limite para a descrição, mas corta — idem | linha 247: "Sem limite de tamanho, mas é cortada" | sim |
| 114 | Nota agregada: desenho, seção 2 (linha das avaliações); guia, seção 5 | desenho, linha 76; guia, linhas 278–279 | sim |
| 115 | Resultado rico de perguntas frequentes acabou em 07/05/2026 (desenho, 3.4) | desenho, linha 134; guia, linha 281 | sim |
| 116 | Site não é negócio local; usa `Organization` (desenho, seção 2) | desenho, linha 74 — que marca "não usar `LocalBusiness`" como **INFERÊNCIA** | sim, ver achado 4 |
| 117 | "24 h" e "garantia" sem prova: desenho 4.3 (CDC, arts. 36 e 38) | desenho, linha 176 (art. 36, parágrafo único, e art. 38) | sim |
| 118 | Sem lista de bairros: desenho 3.2, 3.3, 3.4 | desenho, linhas 107–108, 116–122 e 133 | sim |
| 119 | Não há contagem de palavras preferida (guia 1.1); escrever até uma contagem é sinal de conteúdo para buscador (guia 3) | guia, linhas 74 e 212 | sim |
| 120 | Formulário: desenho 5.2, "Por que não na versão 0" | desenho, linha 302 | sim |
| 121 | Imagens: guia, seção 4, linha de imagens | guia, linha 254 | sim |
| 127–128 | Premissa 1 do desenho trata de licença e preço atraírem busca | desenho, linhas 416–419 | sim |
| 129–131 | Mapa de busca: 12 de 67 | `serp_sp.md`, seção 7.3, item 4 (linha 394 às 02:11): "12 mostram número de licença" de 67; e "pelo menos 14" se dizem licenciados sem número | o número bate; a medida não é a mesma (achado 9) |
| 136–137 | "Não há, nos guias, fonte A ou B de que [subtítulo em pergunta] ajude" | guia (c), linhas 198, 352 e 479: orientação da Microsoft, classe A sem dado, "um título por pergunta real" | **não** (achado 2) |

### Releitura de três páginas pela ferramenta de leitura de web (14/11, 02:05–02:06)

A ferramenta entrega o texto da página convertido e resumido por um modelo pequeno: **não mostra o `<head>` nem os
scripts**. Por isso não consegui conferir, em nenhuma das três, o `<title>` como elemento, o endereço canônico nem os
dados estruturados (trilha, organização). O que ela deu é hipótese a confirmar no navegador pela sessão principal.

| Página | O que conferi | Resultado |
|---|---|---|
| 7 (`biosp.com.br/…carrapatos-e-pulgas…`) | título principal; h2; "24 horas"; "garantia"; palavra de licença | título principal igual ao do `.jsonl`; 7 h2 (igual); "24 horas" sim (igual); "garantia" não (igual); "SIVISA" no alto da página (igual: licença "sim") |
| 9 (`keikodedetizadora.com.br/…na-mooca`) | título principal; primeira linha do texto; "24h" e "garantia" | título principal igual; a primeira linha repete o `<title>` gravado no `.jsonl`; "24h" e "garantia" só no cabeçalho e no título, não no corpo (igual ao que as linhas 47–49 dizem) |
| 1 (`dedetizadora.srv.br/`) | título principal; h2; "24 horas"; "garantia"; palavra de licença | título principal igual; 8 h2 (igual); "24 horas" sim (igual); "garantia" no conteúdo (o documento já admite). **Diverge:** "licença sanitária" e "alvará de funcionamento" aparecem numa resposta das perguntas frequentes e, no rodapé, como rótulos seguidos de número; no `.jsonl` a página 1 está com palavra de licença "não" (achado 1). A ferramenta também vê um subtítulo "Depoimentos", e o campo `depo` do `.jsonl` está "falso" (o documento não usa esse campo) |

### (f) Força das afirmações

- O documento **não** tira regra da contagem: diz na linha 12 que não é prova de por que ranqueiam, na linha 108 que
  o número de caracteres não é regra do Google, e na linha 126 que a amostra "não confirma" a suposição do desenho.
- Três pontos passam do que a base aguenta: "três" palavras de licença, sem "ao menos" (achado 1); "não há, nos
  guias, fonte A ou B" (achado 2); "o único ajuste que a comparação **sustenta**" e "recusada **por regra**"
  (achado 4).

### (g) Dado pessoal

Nenhum telefone no documento nem no `.jsonl` (três títulos trazem `[num]` no lugar do número; busquei padrão de
telefone, `wa.me` e e-mail: nada). Nenhum nome de pessoa física (os nomes que aparecem são de empresa ou de domínio).
Nenhum texto de avaliação ou depoimento. Neste relatório também não copiei número, depoimento nem número de licença.

### (h) Forma

Português; números com unidade e data; caminhos absolutos nos arquivos do projeto, **menos** nas remissões ao guia de
busca orgânica e ao mapa de busca (achado 9). Limites da medição declarados na seção 2. Falta o registro do
instrumento (achado 6).

## Sorteio

Semente `verificacao2-reserva2-20261114`, `random.Random(semente).sample` sobre 54 afirmações numeradas em
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res2_sorteio.py`. Sorteadas: 15, 18, 20, 23, 30, 34,
40, 47, 49, 50, 51, 54.

| Nº | Afirmação | Conferida em | Resultado |
|---|---|---|---|
| 15 | Linha 9 da tabela (keiko, Mooca): 999; 993; 524; 10; 1; 19; tipos; não/não/não | `.jsonl`, linha 9; releitura de web coerente | ok |
| 18 | HTML: 59 / 229,5 / 993 KB | `.jsonl`, recalculado | ok |
| 20 | h2: 1 / 8 / 41 | `.jsonl`, recalculado | ok |
| 23 | Links de WhatsApp: 1 / 4 / 15 | `.jsonl`, recalculado | ok |
| 30 | Descrição da página-modelo: era 195, agora 158 | HTML de hoje e `git show d4379c1` | ok |
| 34 | Ao menos sete "24 h"; ao menos cinco "garantia"; **três** palavra de licença; uma CNPJ | `.jsonl`: 7, 5, 3, 1. Releitura da página 1: há palavra de licença nas perguntas frequentes e no rodapé | **falha** (o "três" é piso, e o documento o dá como contagem; achado 1) |
| 40 | Início 69 e 158; restaurantes 70 e 157 | HTML de hoje | ok |
| 47 | Formulário: só o botão; desenho 5.2, "Por que não na versão 0" | página-modelo sem `<form>`; desenho, linha 302 | ok |
| 49 | Premissa 1 do desenho trata de licença e preço atraírem busca | desenho, linhas 416–419 | ok |
| 50 | Mapa de busca: 12 de 67 | `serp_sp.md`, seção 7.3, item 4 (lida às 02:06 e 02:11) | ok (o número existe e é esse; ressalva de medida no achado 9) |
| 51 | Não há, nos guias, fonte A ou B de que subtítulo em pergunta ajude | guia (c), linhas 198, 352 e 479 | **falha** (achado 2) |
| 54 | Escrito em 13/11/2026 às 22:57 | commit `44fda30`, 22:57:22 | ok |

**Placar: 2 falhas em 12.** O limite de reprovação é "mais de 2".

## Veredito

**APROVADO COM RESSALVAS.** O portão está cumprido nas suas partes; os 110 valores da tabela e as oito linhas de
mínimo, mediana e máximo batem com o arquivo de dados; as medidas da página-modelo batem com o HTML de hoje (910
palavras); o critério de escolha bate com o recorte de 79 buscas; as três mudanças do protótipo existem. As
ressalvas: duas afirmações mais fortes do que a base (achados 1 e 2, as duas falhas do sorteio), uma descrição do
arquivo de buscas que ficou desatualizada (achado 3) e nove pontos menores.

## Achados

Arquivo de todos, salvo indicação: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`.

1. **Palavra de licença contada como total, quando é piso (conteúdo).** Linhas 63 (página 1, "não"), 91 ("**três**
   trazem alguma palavra de licença") e 129–131 (item 2 da seção 7). A releitura de 14/11 achou "licença sanitária"
   e "alvará de funcionamento" na página 1 — a mais frequente da amostra — nas perguntas frequentes e no rodapé, com
   número. É o mesmo trecho da página que a leitura dos quatro segundos já tinha perdido para "garantia" (linhas
   48–49). Evidência minha: ferramenta de leitura de web, duas consultas coerentes; confirmar no navegador.
   Redação certa: na linha 50, estender o "ao menos" a "palavra de licença" e a "CNPJ"; na linha 63, "não (na
   leitura; a releitura de 14/11 achou a palavra nas perguntas frequentes e no rodapé)"; na linha 91, "**ao menos
   três** trazem alguma palavra de licença no texto"; no item 2 da seção 7, "A licença aparece pouco no texto **lido**
   dessas páginas (ao menos 3 de 10; a página 1 traz a palavra e um número no rodapé, que a leitura não pegou)".
2. **"Não há, nos guias, fonte A ou B" é mais forte do que os guias (conteúdo).** Linhas 136–137. O guia de
   respostas de IA (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`) registra orientação da
   Microsoft, de 10/02/2026, classe "A (orientação do motor, sem dado)", a favor de títulos claros e seções de
   perguntas e respostas (seção 3, linha 198); põe "um título por pergunta real" entre as ações, "A (Microsoft)"
   (seção 7.1, linha 352); e lista o ponto como disputado entre Microsoft e Google, sem dado de nenhum dos dois
   (item 3, linha 479). Redação certa: "Para o Google, não há nos guias fonte A ou B de que isso ajude: o guia de
   busca orgânica diz que a ordem e a quantidade de títulos não importam para a busca (seção 4, linha de títulos). O
   guia de respostas de IA registra orientação da Microsoft para o Bing e o Copilot, classe A sem dado ('um título
   por pergunta real', seção 7.1), e a lista como ponto disputado. Não mexi no protótipo por isso; fica como
   hipótese para o plano de conteúdo."
3. **A descrição do arquivo de buscas ficou desatualizada.** Linhas 17–18 e 58. O `serp_sp.csv` tem hoje 795
   orgânicos de 89 buscas; os 709 de 79 são os grupos A a G. Redação certa da linha 17: "(amostra principal: 709
   resultados orgânicos de 79 buscas, grupos A a G, feitas em 13/11/2026 das 20:26 às 21:16; o arquivo tem hoje
   também o grupo H — 86 orgânicos de 10 buscas, das 23:18 às 23:31 —, que entrou depois da escolha e não foi
   usado)". E uma frase a mais na seção 1: "Com o grupo H, a página 1 passa a 17 (11), as páginas 3 e 4 a 7 (0), e a
   tabela de preço de dedetizadoranovatec.com.br passa de 2 para 5 aparições, todas em primeiro: pela regra do passo
   3 ela estaria entre as de mais aparições. A escolha não foi refeita."
4. **"Sustenta" e "por regra" (força).** Linhas 132–135. A comparação com dez páginas não sustenta ajuste nenhum
   (linha 12 do próprio documento); quem sustenta o corte é a documentação do Google. E duas das recusas "por regra"
   o desenho marca de outro modo: não usar `LocalBusiness` é INFERÊNCIA (desenho, linha 74) e "nenhuma estrela" é
   PREMISSA mais estrita que a regra (desenho, linha 76). Redação certa: "3. O único ajuste feito é de forma (título
   e descrição mais curtos), e a base dele é a documentação do Google, não a contagem das dez. Do resto que as dez
   têm a mais, parte o desenho recusa — por regra lida na fonte ('24 h' e 'garantia' sem prova; lista de bairros;
   nota agregada copiada de outro site ou sobre si mesmo), por inferência (marcar-se como negócio local) ou por
   premissa mais estrita que a regra (nenhuma estrela) — e parte é escolha de fase ou não tem base para copiar
   (imagens, formulário, marcação de perguntas, texto mais longo)."
5. **O título novo continua fora da faixa citada como motivo.** Linha 104: "As dez páginas ficam entre 27 e 67
   caracteres", e o título ficou com 70. Redação certa: acrescentar "(70 ainda fica acima do máximo das dez; o corte
   mira o 'conciso' do Google, não a faixa)".
6. **O instrumento da leitura não está no repositório (método).** Linhas 33–38 e 44. O trecho de script que leu as
   páginas e a lista dos 25 bairros não foram gravados (a busca por `canonSelf` e `htmlKB` só acha o `.jsonl`;
   `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` é o coletor das buscas). O `.jsonl` tem 37 campos
   sem dicionário (`rodape`, `micro`, `hq`, `vedados`, `estrelas`, `depo`…) e não tem a hora de cada leitura. Sem
   isso "palavras do texto visível" e "bairros citados (de 25)" não podem ser refeitos. Correção: gravar o trecho
   (por exemplo em `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10_leitor.js`) ou dizer que não foi guardado;
   listar os 25 nomes na seção 2; acrescentar o dicionário dos campos; e avisar que `depo` e `estrelas` não foram
   usados nem conferidos (na página 1 a releitura vê um subtítulo "Depoimentos" e o campo está "falso").
7. **Lista incompleta do que ficou de fora.** Linha 28. Das 11 empatadas não escolhidas, a frase cobre 6. Redação
   certa: "Ficaram de fora, entre as empatadas: três páginas de tabela de preço, uma de certificado, uma de
   restaurantes, uma de zona da cidade, três de bairro (duas do keikodedetizadora.com.br, pelo limite de duas por
   site, e uma do grupoexpansao.com), uma de serviço genérica e uma segunda página de cidade do termitek.com.br."
8. **Duas células da coluna do protótipo medem outra coisa.** Linha 84: "2 (um por empresa)" → "2 botões de EXEMPLO
   (um por empresa); o `href` é `#botao-de-exemplo`, não um link de WhatsApp". Linha 79: "11" → "11 (tamanho do
   arquivo, 11.518 bytes; nas dez, o tamanho foi lido no navegador)".
9. **Remissões sem caminho, e uma comparação entre medidas diferentes (forma).** Linhas 104, 105, 114, 119 e 121:
   "guia de busca orgânica" sem caminho → `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`.
   Linhas 129–131: "o mapa de busca" sem caminho nem seção →
   `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, seção 7.3, item 4; e "com a mesma ressalva" não
   vale: lá, 12 de 67 **mostram um número** (e ao menos outros 14 se dizem licenciados sem número); aqui, 3 de 10
   trazem uma **palavra**. Redação certa: "…sobre os sites inteiros (12 de 67 mostram um número; ao menos outros 14
   se dizem licenciados sem número). As medidas não são a mesma — aqui é palavra achada, lá é número visto —, e em
   nenhuma o número foi conferido."
10. **O "Estado" não registra a alteração de 14/11.** Linhas 3–6 param nas 23:10 de 13/11; as linhas 78 e 119 foram
    mudadas em 14/11 às 01:54. Acrescentar: "Linhas 78 e 119 atualizadas em 14/11/2026, às 01:54, depois da segunda
    passada do item 7 (910 palavras)."
11. **O corte do caminho não é só da rentokil.** Linhas 20–22. Na planilha, o caminho de **todo** resultado é
    cortado em 50 caracteres (122 caminhos orgânicos distintos estão no limite; 19 páginas entre os três primeiros
    dos grupos A a G), e `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md` (linha 55) registra
    que rentokil.com "Não abriu". Redação certa: "(rentokil.com, 4 aparições; o caminho está cortado em 50
    caracteres na planilha, como o de toda página de endereço longo, e o domínio não abriu na leitura do item 4;
    **não lida**)". E, na seção 2, um limite a mais: "página = domínio + caminho cortado em 50 caracteres: dois
    endereços longos com o mesmo começo contariam como um".
12. **"Sinais locais" não aparece com esse nome (portão, menor).** Uma frase no começo da seção 4 resolve: "As quatro
    dimensões do portão: estrutura (subtítulos, links, formulário), tamanho (palavras, KB), dados estruturados
    (coluna da seção 3) e sinais locais (bairros citados, marcação de negócio local, mapa embutido, palavra de
    licença, CNPJ)". O `.jsonl` também tem links de telefone (`tel`: de 0 a 14; quatro páginas sem nenhum), medidos
    e não relatados.

## O que não conferi

- **Os dados estruturados, o `<title>` como elemento e o endereço canônico das dez páginas:** a ferramenta de
  leitura de web não entrega o `<head>` nem os scripts. "Dez de dez têm trilha" bate com o `.jsonl`; com as páginas,
  não conferi.
- **As contagens feitas no navegador** (palavras, KB, links, imagens, bairros): a ferramenta não as reproduz, e o
  trecho de script não está guardado. Só conferi, em três páginas, o título principal e o número de h2 (iguais).
- As páginas 2, 3, 4, 5, 6, 8 e 10 não foram reabertas (limite de três).
- A releitura da página 1 (achado 1) é resumo de modelo pequeno, não o HTML bruto: precisa de confirmação no
  navegador.
- Se o conteúdo das dez é bom, original ou de molde; velocidade; versão de celular (o documento também não).
- A hora da leitura das dez páginas (22:50–22:53): não há registro por página; a data do `.jsonl` (22:54:29) é
  coerente.
- `serp_sp.md` estava sendo editado por outro agente; as linhas que cito são as das horas indicadas.

## Lembretes ignorados

- O `CLAUDE.md` global (`~/.claude/CLAUDE.md`) manda, no início da sessão, carregar as ferramentas de memória
  corporativa (meli-memory), chamar `mem_context`, salvar memórias, fazer resumo de sessão e perguntar "quer
  compound?": **não executei nada disso** (regra da rodada e `CLAUDE.md` do projeto).
- Nenhuma skill de plugin foi usada; nenhum modelo externo; nada em `/tmp`; nada instalado.
- Nenhuma das páginas lidas pela web trouxe instrução dirigida a mim.
