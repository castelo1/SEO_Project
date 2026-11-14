# Verificação independente — fila de reserva, tarefa 2 (dez páginas × página-modelo)

- **Quando:** sexta, 13/11/2026, 23:05 (Brasília, lido de `TZ=America/Sao_Paulo date`).
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu.
- **Artefatos conferidos:** `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` (132 linhas, lido
  inteiro) e `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` (10 linhas, 37 campos cada).
- **Portão (de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, fila de reserva, item 2):**
  "Análise de 10 páginas que ranqueiam bem (estrutura, tamanho, dados estruturados, sinais locais), comparadas com a
  página-modelo do protótipo; ajuste o protótipo e diga o que mudou."
- **Modo:** conferência completa dos números (não por sorteio), mais uma reconferência externa por amostra sorteada.
  Nenhum artefato foi editado. Nenhum `git` de escrita. Nenhum telefone nem nome de pessoa gravado aqui.

## Veredito

**APROVADO COM RESSALVAS.** O portão está cumprido e todos os 100 valores da tabela da seção 3 batem com o `.jsonl`.
Há dois erros de número ("sete sites" é oito; "seis de dez" é sete), uma marcação que a leitura externa não confirmou
("garantia: não" na página 1) e quatro frases mais fortes do que os dados. Nenhum deles muda o que foi alterado no
protótipo nem a leitura central da seção 7 (itens 1 e 2); por isso não reprova. As correções estão no fim.

## 1. Portão

| Pergunta | Resultado |
|---|---|
| São dez páginas? | Sim: 10 linhas no `.jsonl`, 10 linhas na tabela da seção 3. São de **oito** sites, não de sete (ver 3.1). |
| Estrutura | Sim: h1, h2, h3, subtítulos em pergunta, links (total, internos, WhatsApp, telefone), formulários, imagens. |
| Tamanho | Sim: palavras do texto visível e KB do HTML. |
| Dados estruturados | Sim: tipos de JSON-LD por página, com contagens na seção 4. |
| Sinais locais | Sim, em parte: bairros citados (de 25), marcação de negócio local, mapa embutido, palavra de licença, "24 h". Endereço e telefone visíveis no texto não foram medidos como sinal local (o `.jsonl` só mostra `PostalAddress` dentro dos tipos); o arquivo não diz isso. |
| Comparação com a página-modelo | Sim: coluna própria na tabela da seção 4 e a seção 6 inteira. |
| Protótipo ajustado, e o arquivo diz o que mudou | Sim: seção 5. Conferido no `git` (ver item 4). |

## 2. A escolha das dez (regra da seção 1 refeita sobre `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`)

Refiz a conta: 1.060 linhas, 709 com `superficie` = "orgânico", 79 buscas, todas de 13/11/2026 (confere com a linha 14
do arquivo). Contei por `dominio` + `caminho` as aparições com `posicao` ≤ 3 e com `posicao` = 1.

| # | Página | No arquivo | Refeito | |
|---|---|---|---|---|
| 1 | `dedetizadora.srv.br/` | 16 (11) | 16 (11) | confere |
| 2 | `dedetizadora.srv.br/lapa/` | 2 (1) | 2 (1) | confere |
| 3 | `eccocleandedetizacao.com.br/dedetizadora-sp.php` | 6 (0) | 6 (0) | confere |
| 4 | `deltadedetizacao.com.br/dedetizacao-em-sao-paulo/` | 6 (0) | 6 (0) | confere |
| 5 | `keikodedetizadora.com.br/` | 4 (0) | 4 (0) | confere |
| 6 | `protecpragas.com.br/dedetizadora-osasco/` | 2 (2) | 2 (2) | confere |
| 7 | `biosp.com.br/dedetizacao-de-carrapatos-e-pulgas-sao-paulo/` | 2 (1) | 2 (1) | confere |
| 8 | `ecoservicos.com.br/dedetizadora-moema/` | 2 (1) | 2 (1) | confere |
| 9 | `keikodedetizadora.com.br/servicos/dedetizadora-na-mooca` | 2 (1) | 2 (1) | confere |
| 10 | `termitek.com.br/dedetizacao-de-condominios-sao-paulo/` | 2 (1) | 2 (1) | confere |

- **A regra descrita é a aplicada?** Sim. As quatro de mais aparições, tirada a rentokil.com, são 16, 6, 6 e 4. A
  rentokil.com tem 4 aparições (2 na primeira posição) e o caminho está de fato cortado em 50 caracteres na planilha;
  a exclusão está explicada (linhas 18–19 e 128). A única página de governo com 2 aparições (prefeitura) foi tirada,
  como a regra diz. Máximo de duas páginas por site: respeitado (dedetizadora.srv.br e keikodedetizadora.com.br, duas
  cada).
- **Página com mais aparições que ficou de fora sem explicação?** Não: nenhuma página com 3 ou mais ficou de fora além
  da rentokil.com.
- **Entre as empatadas com 2:** são **17** páginas (tirada a de governo); seis entraram. O arquivo diz que a escolha é
  de quem escreveu (linha 24), o que basta para o portão, mas **não diz quantas eram nem que tipos ficaram de fora**.
  Ficaram de fora onze: três páginas de tabela de preço (uma delas com 2 aparições na primeira posição, igual à
  melhor das escolhidas), uma de certificado, uma de restaurantes, três de bairro, uma de zona e duas de serviço ou
  cidade. É ressalva, não erro.

## 3. Números das seções 3 e 4 contra o `.jsonl`

### 3.1 Tabela da seção 3 — as dez linhas, dez colunas cada (100 valores)

Conferi todos: palavras, KB, links internos, h2+h3 (somei `h2` e `h3`), links de WhatsApp, bairros, dados
estruturados, palavra de licença, "24 h" e "garantia". **Os 100 valores batem com o `.jsonl`.** Observações:

- Dados estruturados: "organização" na página 3 vem de `Corporation` e "negócio local" nas páginas 4 e 10 vem de
  `ProfessionalService` e `PestControl` (subtipos). A tradução é aceitável, mas o arquivo não avisa.
- Página 3: o campo `ld` do `.jsonl` termina em "erro" (um bloco de JSON-LD não foi lido). O arquivo não menciona.
- Página 9: o `<title>` gravado no próprio `.jsonl` traz "24h" e "Garantia", e a tabela marca "não" e "não". A marca
  vale só para o corpo do texto (a leitura externa confirmou: as duas expressões estão só no título e em atributos do
  cabeçalho). A seção 2 não diz que o título fica fora dessa conta.
- "dez páginas, de sete sites" (linha 9): **são oito** domínios (biosp.com.br, dedetizadora.srv.br,
  deltadedetizacao.com.br, eccocleandedetizacao.com.br, ecoservicos.com.br, keikodedetizadora.com.br,
  protecpragas.com.br, termitek.com.br).

### 3.2 Tabela da seção 4 — mínimo, mediana e máximo refeitos

| Medida | No arquivo | Refeito | |
|---|---|---|---|
| Palavras | 218 / 1.126 / 4.017 | 218 / 1.126,5 / 4.017 | confere (mediana truncada) |
| HTML (KB) | 59 / 230 / 993 | 59 / 229,5 / 993 | confere (mediana arredondada para cima) |
| Links internos | 37 / 164 / 524 | 37 / 164,5 / 524 | confere (mediana truncada) |
| h2 | 1 / 8 / 41 | 1 / 8 / 41 | confere |
| `<title>` (caracteres) | 27 / 57 / 67 | 27 / 57,5 / 67 | confere (mediana truncada) |
| Meta descrição | 121 / 150 / 163 | 121 / 150 / 163 | confere |
| Links de WhatsApp | 1 / 4 / 15 | 1 / 4 / 15 | confere |
| Imagens | 7 / 17 / 168 | 7 / 17,5 / 168 | confere (mediana truncada) |

Ressalva de forma: quatro medianas com ",5" foram cortadas para baixo e uma (KB) subiu. Não muda nada, mas o critério
deve ser um só.

### 3.3 Contagens da seção 4

| Afirmação | Refeito no `.jsonl` | |
|---|---|---|
| Dez de dez: trilha em dados estruturados | 10 | confere |
| Dez de dez: canônico para si, `viewport`, `lang="pt-BR"`, ao menos um link de WhatsApp | 10, 10, 10, 10 | confere |
| Nove de dez marcam organização | 9 (todas menos a 7; conta `Corporation`) | confere |
| Três como negócio local | 3 (páginas 3, 4, 10) | confere |
| Quatro com nota agregada | 4 (3, 6, 9, 10) | confere |
| Quatro com marcação de perguntas | 4 (5, 6, 9, 10) | confere |
| Sete escrevem "24 h" | 7 (1, 2, 4, 5, 6, 7, 8) | confere com o `.jsonl` |
| Cinco, "garantia" | 5 (2, 4, 5, 6, 8) | confere com o `.jsonl`; **ver item 5: a página 1 não confirmou na leitura externa** |
| Três com palavra de licença | 3 (2, 3, 7) | confere |
| Uma com "CNPJ" | 1 (página 8) | confere |
| Cinco com formulário | 5 (2, 3, 4, 8, 10) | confere |
| Nenhuma com mapa embutido | 0 | confere |
| **Seis** com subtítulo em forma de pergunta | **7** têm `hq` ≥ 1 (1, 3, 4, 5, 6, 7, 10) | **não confere** (linhas 83 e 123) |
| "seguro" em 3 das 10 (seção 2) | 3 (4, 6, 10) | confere |

## 4. Medidas do protótipo (medidas por mim no arquivo atual, com Python e `html.parser`; texto visível = corpo sem `<script>` e `<style>`)

| Medida | No arquivo | Medido | |
|---|---|---|---|
| Página-modelo: palavras | 856 | 856 (separando por espaço) | confere |
| Página-modelo: tamanho | 11 KB | 10.985 bytes = 10,7 KB | confere (arredondado) |
| Página-modelo: links | 14 ao todo | 14 | confere |
| Página-modelo: h2 | 5 | 5 | confere |
| Página-modelo: `<title>` agora | 70 | 70 | confere |
| Página-modelo: meta descrição agora | 158 | 158 | confere |
| Página-modelo: `<title>` antes | 98 | 98 (versão anterior no `git log -p`) | confere |
| Página-modelo: meta descrição antes | 195 | 195 (idem) | confere |
| Página-modelo: links de WhatsApp | 2 (um por empresa) | 2 botões de EXEMPLO (`href="#botao-de-exemplo"`) | confere |
| Página-modelo: imagens | 0 | 0 | confere |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` | 69 e 158 | 69 e 158 | confere |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | 70 e 157 | 70 e 157 | confere |

- "Nada mais mudou" (linha 98): conferido no último registro do `git` que tocou o protótipo — só `<title>` e meta
  descrição nas três páginas, mais três linhas de nota no `LEIA-ME.md`. A página de privacidade não foi tocada (o
  título dela já era curto); o arquivo não a cita, e não precisa.
- Observação: o novo `<title>` da página-modelo (70) fica acima do máximo visto nas dez (67). O arquivo não diz que
  ficou dentro da faixa, então não há erro; só registro.

## 5. Reconferência externa por amostra

- **Sorteio:** `random.seed(20261113); random.sample(range(1, 11), 4)` → páginas **1, 3, 8 e 10**.
- **Ferramenta:** leitura de página (WebFetch), em 13/11/2026, entre 22:59 e 23:04. A ferramenta converte a página em
  texto e resume; **não mostrou JSON-LD em nenhuma das quatro** e lê também o que fica recolhido na tela. Nenhuma
  página pediu ação. Nenhum telefone foi gravado.

| Página | `<title>` | Primeiro `<h1>` | "24 horas"/"24h" | "garantia" | Tipos de JSON-LD |
|---|---|---|---|---|---|
| 1 `dedetizadora.srv.br/` | confere | confere (na segunda leitura, com os níveis de título) | confere (sim) | **não confere**: o `.jsonl` diz que não; a leitura externa achou a palavra no bloco de perguntas frequentes, no rodapé e em depoimentos | inconclusivo |
| 3 `eccocleandedetizacao.com.br/dedetizadora-sp.php` | confere | confere | confere (não) | confere (não) | inconclusivo |
| 8 `ecoservicos.com.br/dedetizadora-moema/` | confere | confere (difere só em maiúsculas) | confere (sim) | confere (sim) | inconclusivo |
| 10 `termitek.com.br/dedetizacao-de-condominios-sao-paulo/` | confere | confere (difere só em maiúsculas) | confere (não) | confere (não; há "garantindo") | inconclusivo |

Placar: 16 itens conferíveis, 15 conferem, **1 não confere**; 4 inconclusivos (dados estruturados).

Sobre o item que não confere: a página 2 (`/lapa/`), do mesmo site e com o mesmo rodapé de 20 links, está marcada
"garantia: sim". A causa provável é a que o próprio arquivo aponta como limite (leitura única, quatro segundos depois
de abrir, só texto visível), mas o limite só é citado para a página de 218 palavras. Com a página 1, "garantia" seria
6 de 10, não 5. Não muda a leitura (reforça o item 1 da seção 7), mas o número da tabela está em dúvida.

**Fora do sorteio**, para o item 7 desta verificação, abri também as páginas 9 e 6 (as duas que a seção 4 chama de
"formato lista de bairros"): resultado no item 7.

## 6. Remissões ao desenho e ao guia

| Trecho do arquivo | Onde deveria estar | Resultado |
|---|---|---|
| "o Google pede título 'descritivo e conciso', com a marca de forma breve" | guia de busca orgânica, seção 4, linha do link de título | existe e sustenta (linha 246 do guia) |
| "o Google não fixa limite, mas corta" | guia, seção 4, linha do trecho e meta descrição | existe e sustenta (linha 247: "Sem limite de tamanho, mas é cortada") |
| "o resultado rico de perguntas frequentes deixou de existir em 07/05/2026 (desenho, seção 3.4)" | desenho, seção 3.4, linha de dados estruturados | existe e sustenta (linha 126 do desenho; também guia, seções 1.3 e 5) |
| "lista de bairros … exemplo de excesso de palavras-chave (guia, seção 2.1)" | guia, seção 2.1, linha de excesso de palavras-chave | o trecho existe (linha 163: "blocos de texto listando cidades e regiões"). **A aplicação às páginas 9 e 6 vai além do que foi medido** (item 7) |
| Nota agregada: desenho, seção 2 (linha das avaliações) e seção 3.4 | desenho | seção 2 sustenta (linha 68). **A seção 3.4 não fala de avaliação nem de estrela** (só "só o que está visível"); a base certa é o guia, seção 5 |
| Negócio local: desenho, seção 2 | desenho, linha 66 | sustenta |
| "24 h" e "garantia": desenho, seção 4.3 (CDC, arts. 36 e 38) | desenho, linha 167 | sustenta ("sem prova guardada dada pela licenciada") |
| Links internos e bairros: desenho, seções 3.2, 3.3 e 3.4 | desenho | as três existem e sustentam a recusa de lista de bairros e de página por bairro |
| Formulário: desenho, seção 5.2 ("Por que não na versão 0") | desenho, linha 285 | sustenta |
| Imagens: guia, seção 4, linha de imagens | guia, linha 254 | sustenta |
| Texto longo: "não há, no guia, tamanho de texto que o Google prefira; alongar sem dado próprio é o que a política chama de conteúdo em escala (guia, seção 2.1)" | guia | a primeira metade é verdadeira e o guia diz até mais (seção 1.1: "não há contagem mágica de palavras"; seção 3: "escrever até uma contagem de palavras" é sinal de conteúdo feito para o buscador). **A segunda metade não se sustenta:** a política de conteúdo em escala da seção 2.1 trata de **muitas páginas**, não do tamanho do texto de uma página |
| "É a premissa 1 da seção 10 do desenho" (seção 7, item 1) | desenho, seção 10 | a premissa 1 existe, mas diz outra coisa: "que mostrar a licença conferida e o preço com origem atrai busca, clique ou citação por IA". Não é a aposta de "aparecer sem lista de bairros, '24 h', 'garantia' e estrelas". **Sustenta só em parte** |
| "12 de 67" (seção 7, item 2) | `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, seção 7.3 | o número existe (linha 361; desenho, linha 101). Lá é "sites que mostram **o número**"; aqui é "palavra de licença no texto". O arquivo avisa da diferença com "palavra achada não é número conferido" |

## 7. Afirmações mais fortes que a amostra

- **Regra ou causa tirada de dez páginas?** Não. O arquivo diz que não é prova de por que ranqueiam (linhas 9–10),
  que o número de caracteres não é regra do Google (linha 98) e que a amostra "não confirma" a aposta do desenho
  (linha 116). Os limites estão na seção 2 e na seção 8.
- **"seguro":** o arquivo **não** afirma promessa de ausência de risco (linhas 41–42). Correto. Na leitura externa da
  página 6 a palavra aparece em frases como pergunta ("É seguro contratar…") e adjetivo de serviço; nada a corrigir.
- **Frases que passam do que os dados sustentam:**
  1. Linhas 84–88: as páginas 9 e 6 "são o formato 'lista de bairros' que o guia … aponta como exemplo de excesso de
     palavras-chave". O `.jsonl` só tem contagens (524 links internos; 25 de 25 nomes), e a seção 8 diz que o texto
     não foi lido. Na leitura externa: a página 9 tem cerca de 39 links "dedetizadora em/na/no bairro" no menu e
     outros tantos no corpo, e uma frase que cita cinco bairros; a página 6 tem cerca de 215 links de bairro e
     cidade, agrupados por região, perto do fim do corpo. São **listas de links**, não o "bloco de texto" do exemplo
     da política; e o próprio guia (seção 2.2, linha 192) separa "lista em bloco de texto" de "bairros como
     navegação real". Enquadrar duas empresas nomeadas num exemplo de política de spam pede mais do que contagem.
  2. Linha 108: "Dezenas ou centenas de links internos **para páginas de bairro**". O destino dos links internos não
     foi medido; o `.jsonl` só conta links internos. (A leitura externa mostra que, nas páginas 9 e 6, parte é de
     bairro; nas outras oito não se sabe.)
  3. Linhas 115–117: "As páginas que estão no topo fazem o que o desenho recusa (lista de bairros, '24 h',
     'garantia', estrelas)". Pelos números do próprio arquivo: "24 h" em 7, "garantia" em 5, nota agregada em 4
     (estrela visível em 1, campo `estrelas`), lista de bairros apontada em 2. A frase lê como se fossem todas.
  4. Linhas 121–122: "Tudo o mais que as dez têm a mais que o protótipo é o que as regras do item 2 ou a política de
     spam desaconselham." **Contradiz a seção 6 do mesmo arquivo:** imagens, formulário, marcação de perguntas e
     texto mais longo estão lá com outras bases (escolha de fase, resultado rico extinto, "pode entrar depois"),
     nenhuma delas regra do item 2 nem política de spam.

## 8. Forma

- Português: sim. Caminhos absolutos para arquivos do projeto: sim (as páginas externas aparecem como domínio +
  caminho, o que é adequado).
- Telefone: nenhum no `.md` nem no `.jsonl` (procurei por padrões de número; os títulos com número estão mascarados
  como "[num]"). Nome de pessoa: nenhum.
- Nada publicado: as mudanças são em arquivos locais do protótipo.
- Estado declarado "Não verificado" (linha 3): correto até esta verificação.

## Correções pedidas (todas em `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`, salvo indicação)

1. **Linha 9:** "de sete sites" → "de oito sites".
2. **Linhas 83 e 123:** "Seis de dez" / "6 das 10" → sete (o campo `hq` é ≥ 1 nas páginas 1, 3, 4, 5, 6, 7 e 10); ou
   dizer que critério dá seis.
3. **Linhas 52, 80 e 107:** a página 1 está "garantia: não", mas a leitura externa achou a palavra no conteúdo dela
   (perguntas frequentes, rodapé). Remedir a página 1 ou marcar a célula e as contagens "cinco" e "7 e 5" como
   "ao menos" e explicar; se remedir, corrigir também a linha 1 do
   `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` (campo `garantia`).
4. **Linhas 35–43 (limites):** acrescentar (a) que "24 h" e "garantia" são procuradas só no corpo do texto visível, e
   que a página 9 traz as duas no `<title>` (linha 60 da tabela); (b) que o limite da leitura aos quatro segundos
   pode ter afetado também a página 1, não só a de 218 palavras; (c) que um bloco de JSON-LD da página 3 não foi
   lido ("erro" no `.jsonl`); (d) que "organização" inclui `Corporation` e "negócio local" inclui
   `ProfessionalService` e `PestControl`.
5. **Linhas 84–88:** trocar "são o formato 'lista de bairros' que o guia … aponta como exemplo de excesso de
   palavras-chave" por descrição do que foi medido (524 links internos; 25 de 25 nomes) e dizer que o enquadramento
   na política não foi avaliado.
6. **Linha 108:** "links internos para páginas de bairro" → "links internos (destino não medido)".
7. **Linha 109:** tirar "é o que a política chama de conteúdo em escala (… seção 2.1)" e citar o que o guia de fato
   diz sobre tamanho: seção 1.1 ("não há contagem mágica de palavras") e seção 3 ("escrever até uma contagem de
   palavras").
8. **Linha 104:** trocar "e seção 3.4" por "e guia de busca orgânica, seção 5 (estrelas e origem das avaliações)".
9. **Linhas 115–117:** pôr os números ("24 h" em 7, "garantia" em 5, nota agregada em 4, lista de bairros em 2) no
   lugar de "as páginas que estão no topo fazem"; e ajustar "É a premissa 1 da seção 10": a premissa 1 é sobre a
   licença atrair busca, não sobre aparecer sem essas práticas.
10. **Linhas 121–122:** reescrever "Tudo o mais … desaconselham" para bater com a seção 6: parte é recusada por regra
    (nota agregada, negócio local, "24 h"/"garantia", lista de bairros) e parte é escolha de fase ou não tem base
    para copiar (imagens, formulário, marcação de perguntas, texto mais longo).
11. **Linhas 65–74:** um só critério para as medianas com ",5" (hoje: 229,5 → 230, mas 57,5 → 57; 17,5 → 17;
    164,5 → 164; 1.126,5 → 1.126); as linhas 108, 109 e 111 repetem esses valores.
12. **Linhas 20–24:** dizer que as empatadas com 2 eram 17 e que tipos ficaram de fora (tabela de preço, certificado,
    restaurantes, zona).

## O que não conferi

- Os tipos de dados estruturados das quatro páginas sorteadas (a ferramenta não mostra JSON-LD): inconclusivo.
- As medidas de palavras, KB, links e subtítulos das dez páginas na fonte: só conferi a tabela contra o `.jsonl`,
  não o `.jsonl` contra as páginas (exceto título, h1, "24 h" e "garantia" na amostra).
- Os tamanhos de `<title>` e de meta descrição das dez páginas: os títulos com número estão mascarados no `.jsonl`,
  então o comprimento gravado não pode ser refeito a partir dele.
