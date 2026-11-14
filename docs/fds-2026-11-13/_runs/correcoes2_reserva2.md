# Correções da segunda passada — fila de reserva, tarefa 2 (dez páginas × página-modelo)

## Quem e quando

- Corretor (subagente). Não usei navegador, busca ao vivo nem leitura de web. Não rodei `git` de escrita (só um
  `git show` e `git status`, de leitura). Nada instalado, nada em `/tmp`.
- Início: sábado, 14/11/2026, 02:20 (Brasília, lido de `TZ=America/Sao_Paulo date`). Artefato gravado às 02:28
  (idem; o placar do "Estado" foi acertado às 02:32). Relatório gravado às 02:35; fim da sessão do corretor:
  02:36 (idem).
- Achados do revisor: `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva2.md`
  (12 achados, lido inteiro).
- Arquivo editado: **só** `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` (de 144 para 266
  linhas). Não editei `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` nem
  `/home/ancastelo/pessoal/SEO_Project/prototipo/`.

## Placar

12 achados conferidos no artefato e nos dados; **12 procedem e foram aplicados**: 7 com o conteúdo que o revisor
propôs (alguns com acréscimo) e 5 com ajuste (1, 4, 5, 6 e 12). Nenhum "não aplicado". Um número do revisor não
procede e não entrou (achado 12: são três páginas sem link de telefone, não quatro).

## Achado por achado

Linhas = linhas de `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` depois da correção.

| Achado | O que fiz | Linhas | Como conferi |
|---|---|---|---|
| 1. Palavra de licença contada como total | **Com ajuste.** As contagens de palavra de licença e de "CNPJ" viraram "ao menos"; o limite diz que a leitura dos quatro segundos não cobriu perguntas frequentes nem rodapé carregados depois. A releitura do revisor entrou como **indício, não fato**: "o revisor da segunda passada, lendo por ferramenta que entrega o texto resumido por um modelo, achou…; não conferido no navegador". A célula da página 1 ficou "não na leitura (ver a nota abaixo)", porque o arquivo de dados registra "não" | 84–90 (limite), 140 e 151–156 (célula e nota), 180–181 (contagens), 226–231 (seção 7, item 2), 262 | `paginas_top10.jsonl`: `lic` verdadeiro em 3 páginas (2, 3 e 7), `cnpj` em 1 (8), `h24` em 7, `garantia` em 5. A página 1 **não** foi reaberta (sem navegador) |
| 2. "Não há, nos guias, fonte A ou B" | **Aplicado**, escrevendo o que os guias dizem, por motor e com a classe: Google — sem fonte A ou B de que ajude; a ordem e a quantidade de títulos não importam para a busca (classe A). Microsoft — recomendação de 10/02/2026, "A (orientação do motor, sem dado)"; "um título por pergunta real", "A (Microsoft)"; ponto disputado entre Microsoft e Google, sem dado. Quem ganha: Microsoft | 239–253 | Abri `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, linhas 198, 352 e 479–481 (dizem o que o revisor atribui), e `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, linha 248 (linha "Títulos" da seção 4) |
| 3. Descrição do arquivo de buscas desatualizada | **Aplicado, com acréscimo.** A seção 1 diz que a escolha foi feita sobre 709 orgânicos de 79 buscas (grupos A a G, 20:26–21:16), antes do grupo H (86 orgânicos de 10 buscas, 23:18–23:31), e que o arquivo tem hoje 795 de 89. Parágrafo novo com o que muda contando o grupo H. **A escolha não foi refeita** | 26–30, 49–58, 135–136, 259 | Recontei em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` às 02:22 e às 02:24 (o arquivo foi regravado por outro agente às 02:21:37; as contagens não mudaram): 1.180 linhas; 795 orgânicos; 89 buscas; A a G = 709 de 79; H = 86 de 10. As dez páginas: A a G = 16 (11), 2 (1), 6 (0), 6 (0), 4 (0), 2 (2), 2 (1), 2 (1), 2 (1), 2 (1); com H, a página 1 vai a 17 (11) e as páginas 3 e 4 a 7 (0) |
| 4. "Sustenta" e "por regra" | **Com ajuste.** Item 3 da seção 7 reescrito: o ajuste é de forma e a base é a documentação do Google, não a contagem. As recusas ficaram em três grupos: regra lida na fonte, inferência do desenho, premissa mais estrita. Ajuste meu: a lista de bairros entrou nos dois primeiros (a política dá o bloco de texto com lista de cidades como exemplo — classe A; "não fazer página por bairro" é classe A + INFERÊNCIA no desenho). As linhas da seção 6 ganharam a marca de cada base | 211, 213, 215, 232–238 | `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linhas 74 e 76 (seção 2), 107 (seção 3.2), 133 (seção 3.4) e 176 (seção 4.3), lidas às 02:22 |
| 5. Título novo fora da faixa | **Com ajuste.** Escrito como está: 70 caracteres contra o máximo de 67 nas dez (os outros dois títulos: 69 e 70). Não atribuí intenção ao corte ("mirou o conciso"): escrevi que a faixa não foi atingida e que a base que resta é o "conciso" do Google, que não dá número. **Registrado como ponto em aberto**; protótipo não mexido | 171, 195, 203–205, 263 | Medi o `<title>` do HTML de hoje: 70 caracteres; `titleLen` das dez: de 27 a 67 |
| 6. Instrumento não está no repositório | **Com ajuste.** O documento agora diz que o trecho de script e a lista dos 25 bairros **não foram guardados** (limite de reprodutibilidade) e que não há hora por leitura. Não gravei script nem listei os 25 nomes (não existem no repositório). Acrescentei a seção 2.1, dicionário dos 37 campos, só com o que os valores e o documento permitem afirmar; o resto está "não documentado". `depo`, `estrelas`, `rodape`, `micro` e `imgsAlt`: não usados nem conferidos | 72–77, 82–83, 100–131, 260–261 | Busca por `canonSelf` e `htmlKB` no projeto: só o `.jsonl` e relatórios; `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js` é o coletor das buscas. Cada linha do dicionário conferida nos dados: `titleLen` é maior que o texto gravado nas três páginas com `[num]` (34, 58, 56 contra 26, 49, 47); `h2`+`h3` = coluna da seção 3; `internos` ≤ `links`; `imgsAlt` ≤ `imgs`; `estrelas` só na página 10; `depo` só na 4; `micro` só na 5; `vedados` = "seguro" nas páginas 4, 6 e 10 |
| 7. Lista incompleta do que ficou de fora | **Aplicado, com acréscimo.** As onze: 3 de tabela de preço, 1 de certificado, 1 de restaurantes, 1 de zona, 3 de bairro (2 do keikodedetizadora.com.br, 1 do grupoexpansao.com), 1 de serviço genérica (ecoservicos.com.br), 1 segunda página do termitek.com.br. Acrescentei: eram 18 empatadas antes de tirar a de governo; 4 das 11 são de sites que já tinham duas páginas entre as dez | 42–47 | `serp_sp.csv`, grupos A a G: 18 páginas com 2 aparições entre os três primeiros; 1 de governo; 6 escolhidas; 11 de fora, conferidas uma a uma pelo endereço |
| 8. Duas células medem outra coisa | **Aplicado.** WhatsApp: nenhum link de verdade; 2 botões de EXEMPLO com endereço `#botao-de-exemplo`, que não leva a lugar nenhum. KB: 11 = tamanho do arquivo em disco (11.518 bytes); nas dez, medido no navegador | 168, 173 (e 169: os 14 links são todos internos, 3 são âncoras) | HTML de hoje: 14 `<a>`, 2 com `href="#botao-de-exemplo"`, 1 com `#quem-executa`; nenhuma ocorrência de `wa.me` nem de `api.whatsapp`; 11.518 bytes |
| 9. Remissões sem caminho; comparação entre medidas diferentes | **Aplicado.** Caminho absoluto do guia de busca orgânica nas linhas da seção 5 e da seção 6, e do mapa de busca no item 2 da seção 7 (por seção e item, não por linha: o arquivo estava sendo editado). "As duas medidas não são a mesma"; tirei também o "é coerente com" | 195–196, 211, 216, 218, 226–231 | `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, seção 7.3, item 4 (linha 397 às 02:24): 12 de 67 mostram número; pelo menos 14 se dizem licenciados sem número |
| 10. "Estado" não registra 14/11 | **Aplicado.** O estado registra a alteração de 14/11/2026, 01:54 (856 → 910 palavras, pela segunda passada do item 7) e esta correção (relatório, placar, hora lida de `date`) | 3–14 | Contei 910 no HTML de hoje e 856 em `git show 49ff823^:prototipo/zona-oeste/baratas/index.html` (mesmo método: `html.parser`, texto do `body` sem `script` nem `style`) |
| 11. Corte do caminho não é só da rentokil | **Aplicado, com acréscimo.** Passo 2 e seção 8 reescritos; limite novo na seção 2 ("página" = domínio + caminho cortado em 50 caracteres). Acrescentei que nenhuma das dez lidas está nesse caso | 33–37, 93–97, 257–258 | `coletor.js`: `x.pathname.slice(0,50)` (nas duas versões da função). Planilha: nenhum caminho passa de 50; 122 caminhos orgânicos distintos com exatamente 50; 19 páginas nesse caso entre os três primeiros de A a G; os dez caminhos lidos têm de 1 a 46 caracteres. `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md`, linha 55 (02:24): rentokil.com "Não abriu" |
| 12. "Sinais locais" sem esse nome | **Com ajuste.** Frase nova no começo da seção 4 com as quatro dimensões. Links de telefone relatados: de 0 a 14, mediana 2,5; **três** páginas sem nenhum (6, 7 e 9) — o revisor escreveu "quatro" | 160–163, 184–185 | `.jsonl`, campo `tel`: 4, 4, 2, 7, 2, 0, 0, 3, 0, 14 |

## Números que mudaram no documento

| Onde | Antes | Depois |
|---|---|---|
| Palavra de licença | "três" (de 10) | "ao menos três" (piso) |
| "CNPJ" | "uma" | "ao menos uma" (piso) |
| Arquivo de buscas | "709 resultados orgânicos de 79 buscas" | o mesmo recorte, agora nomeado (grupos A a G), mais: arquivo de hoje com 795 de 89; grupo H = 86 de 10 |
| Empatadas com 2 | "eram 17" | 18; tirada a de governo, 17 |
| Com o grupo H (novo) | — | página 1: 17 (11); páginas 3 e 4: 7 (0); tabela de preço de dedetizadoranovatec.com.br: de 2 para 5 (5 em primeiro); tabela de dedetizadora.srv.br: de 2 para 4; preços de primordialdedetizacao.com.br: de 2 para 3 |
| Links de WhatsApp da página-modelo | "2 (um por empresa)" | nenhum de verdade; 2 botões de EXEMPLO |
| Tamanho da página-modelo | "11" KB | 11 KB = 11.518 bytes em disco |
| Links de telefone das dez (novo) | — | de 0 a 14; mediana 2,5; três páginas sem nenhum |
| Caminhos cortados (novo) | — | 122 caminhos orgânicos com exatamente 50 caracteres; 19 entre os três primeiros de A a G |

Não mudaram: a tabela das dez páginas (fora a célula de licença da página 1), mínimos, medianas e máximos, as
contagens de dados estruturados e as medidas da página-modelo (910 palavras, 14 links, 5 h2, 70 e 158 caracteres).

## O que outros arquivos repetem (não editei)

| Arquivo e linha (lidos entre 02:23 e 02:34) | O que diz | Situação |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`, linha 26 | Reserva 2 "fechada" só com a primeira verificação ("12 correções aplicadas às 23:10, sem novo leitor") | **Desatualizado:** falta a segunda passada (revisor, este relatório, ponto em aberto do título) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`, linhas 135–136 | "só mudou no protótipo o tamanho de títulos e descrições" | Verdadeiro, mas incompleto: não diz que os títulos seguem acima do máximo das dez (70, 69 e 70 contra 67), que a escolha foi feita antes do grupo H nem que a contagem de licença é piso |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linhas 13–15 | títulos e descrições "encurtados depois da comparação com dez páginas bem colocadas" | Coerente; não registra que a base do corte é a documentação do Google nem o ponto em aberto |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`, linha 6 (e os títulos de `prototipo/index.html` e `prototipo/para-empresas/restaurantes/index.html`) | `<title>` de 70, 69 e 70 caracteres | **Ponto em aberto:** acima do máximo das dez (67); decisão da sessão principal |
| `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl`, linha 1 | `lic` falso e `depo` falso na página 1 | Pode estar abaixo do real (indício do revisor, não conferido no navegador); dado não editado |
| `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linhas 35–36 e 153–160 | subtítulos em pergunta: Google sem fonte A ou B; Microsoft classe A sem dado; remete a "P, seção 7, item 4" | **Coerente:** outro corretor atualizou o arquivo às 02:32 e já cita esta correção (02:28) |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, linhas 535–537 | remete a este documento para "se exibem licença" | Coerente; não diz que a contagem daqui é piso |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva2.md`, achado 12 | "quatro páginas sem nenhum" link de telefone | Não procede: são três (relatório do revisor, não editado) |

## O que não conferi

- **As dez páginas não foram reabertas** (sem navegador): a palavra de licença e o subtítulo "Depoimentos" da página
  1 continuam indício do revisor, lido por ferramenta de resumo. Precisa do navegador da sessão principal.
- Os dados estruturados, o `<title>` e o endereço canônico das dez: confiro só que o documento bate com o `.jsonl`.
- O dicionário da seção 2.1 descreve os campos pelo nome e pelos valores; a regra de cada contagem não é
  recuperável sem o trecho de script.
- Não abri a primeira verificação nem as correções anteriores; mantive no "Estado" o que o documento já dizia dela.
- As remissões ao desenho, ao mapa de busca e ao plano de conteúdo foram lidas em arquivos que outros agentes
  editavam (`desenho_v0.md` regravado às 02:23; `serp_sp.md` às 02:22; `plano_conteudo_90d.md` às 02:32): cito
  seção e item; os números de linha valem para a hora indicada.
- A correção não foi relida por terceiro.

## Lembretes ignorados e ocorrências

- O `CLAUDE.md` global (`~/.claude/CLAUDE.md`) manda carregar as ferramentas de memória corporativa (meli-memory),
  chamar `mem_context`, salvar memórias, fazer resumo de sessão e perguntar "quer compound?": **não executei nada
  disso** (regra da rodada e `CLAUDE.md` do projeto). Nenhuma skill de plugin, nenhum modelo externo.
- **Ocorrência:** ao procurar em que outros arquivos os dois artefatos são citados
  (`grep -rn 'medicao_modelo\|paginas_top10'`), o filtro que devia excluir a pasta `_runs` falhou e a saída mostrou
  linhas soltas, cortadas, de arquivos que eu não devia abrir: `verificacao_reserva2.md` (linhas 5, 6, 215 e 223),
  `verificacao_reserva5.md` (linhas 5, 6, 117, 121, 123, 125, 128 e 131), `verificacao_reserva3.md`,
  `verificacao_reserva3_v2.md`, `verificacao_item4.md` (linha 253), `correcoes2_item3_guias_a_b.md` (linha 243) e
  `correcoes2_item3_ia_chatgpt.md` (linha 207). Não abri esses arquivos e não usei o que apareceu em nenhuma
  correção.
- Outros agentes editavam o repositório ao mesmo tempo (`serp_sp.csv`, `serp_sp.md`, `desenho_v0.md`,
  `plano_conteudo_90d.md`, `contrato_pontos.md`): não toquei em nenhum deles.
