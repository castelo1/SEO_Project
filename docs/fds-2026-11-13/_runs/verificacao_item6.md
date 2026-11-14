# Verificação independente do item 6 — `docs/desenho_v0.md`

- **Quando:** sexta, 13/11/2026, das 22:03 às 22:14 (Brasília, lido de `TZ=America/Sao_Paulo date`: início
  "Fri Nov 13 22:03:44 -03 2026"; depois de gravar, "Fri Nov 13 22:14:21 -03 2026").
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu. Só leitura de arquivo local; nenhuma
  página da web aberta, nenhum navegador, nenhum `git` de escrita. Nada editado além deste arquivo.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, 364 linhas, lido inteiro (alterado pela
  última vez às 21:57; `sha256` começa por `30d03436c09b8e47`). Os números de linha abaixo são dessa versão.
- **Arquivos abertos para conferir:**
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` [R] (inteiro, 499 linhas);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` [A] (linhas 35–509);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` [B] (linhas 71–115, 197–216, 326–510);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` [C] (linhas 58–147, 179–220, 336–495);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` [G] (linhas 1–112, 187–267, 405–589);
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` [S] (inteiro, 418 linhas);
  `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` [M] (linhas 1–680);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` (linhas 200–264);
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (inteiro).
  [S] e [M] não mudaram entre a escrita do desenho e esta leitura (21:45 e 21:50).

## Veredito

**APROVADO COM RESSALVAS.**

- O portão está coberto parte por parte (seção 1 abaixo).
- Sorteio de 12 ponteiros: **1 falha em 12** (limite: 2). Sorteio complementar de 12: 0 falha.
- O desenho **não depende** de prática marcada "vedado" em [R], nem de perfil fora da regra, endereço fictício,
  avaliação fabricada, link comprado ou consulta automática ao Google.
- As ressalvas são 21 correções (seção 8): dez de conteúdo (uma remissão que diz o contrário do arquivo citado, um
  dado contrário de [S] omitido, três contradições internas, uma afirmação sobre dado pessoal que o próprio texto
  desmente, uma lacuna no roteamento da Via B, a lista de premissas incompleta) e onze menores.

## 1. Portão, parte por parte

| Elemento exigido | Onde está no artefato | Confere? |
|---|---|---|
| Arquitetura do site (páginas por praga × região) | Seção 3.1, linhas 64–77 (doze tipos; T3 é praga × região); 3.2 e 3.3 | Sim |
| O que cada página precisa ter | 3.1 (coluna "Para que serve"), 3.4 (o que toda página tem, linhas 104–119), 4.1 (bloco "Quem executa") | Sim, com ressalva: não há lista de blocos por tipo de página; T8, T9 e T12 têm uma linha cada e nenhum ponteiro (correção 18) |
| Onde cada página exibe o que o item 2(b) exige | Seção 4: 4.1 (bloco acima do botão, em T3 a T7), 4.2 (faixa em todas), 4.3 (o que não dizer), 4.4 (norma silente) | Sim; falta dizer em que lugar da página fica a faixa fixa (correção 19) |
| Captação e roteamento por WhatsApp | 5.1 (Via A, botão), 5.2 (Via B, formulário), 5.3 (o que fica fora) | Sim, com lacuna: a Via B não diz por que canal o pedido chega à licenciada (correção 8) |
| Texto de consentimento | 5.2, linhas 199–218, com a tabela de origem de cada parte (linhas 222–232); aviso da Via A na linha 171 | Sim (conferido contra [R] na seção 5) |
| Para quantas empresas o contato vai | Linhas 38–40, 176–177 (Via A: uma) e 234–236 (Via B: uma por padrão, no máximo três) | Sim; as três passagens são coerentes entre si |
| Como a pessoa pede a exclusão | Linhas 178–179 (Via A) e 240–242 (Via B) | Sim, com ressalva na Via A (correção 6) |
| Medir posição, clique, lead, lead vendido | Seção 6, linhas 258–275 | Sim; "lead vendido" está definido de modo ambíguo (correção 13) |
| O que é automatizável | Seção 7, linhas 279–290 | Sim |
| Fases, com o que cada uma prova antes de gastar | Seção 8, linhas 297–304 | Sim, com duas contradições (correções 3 e 4). O artefato declara que os valores em reais não foram levantados (linhas 294–295) |
| "O que tornaria isto inviável", quatro restrições uma a uma | 9.1, linhas 320–325: (a) perfil, (b) propaganda, (c) LGPD, (d) WhatsApp, cada uma com "depende de quê", "o que tornaria inviável" e "como se saberia" | Sim |
| Cada escolha aponta para o trecho do estudo | 132 remissões contadas; quase todas batem | Sim, com as exceções das seções 3 e 4 |
| Premissa sem evidência A ou B marcada | Marcas no corpo e lista na seção 10 | Em parte: lista incompleta e marcas fora da legenda (correções 9, 10 e 16) |
| Não depende de perfil fora da regra, endereço fictício, avaliação fabricada, link comprado | Seção 2 (linhas 53–57), 9.3 (linhas 341–343) | Sim (seção 6 abaixo) |

## 2. Sorteio

**Lista sorteada:** uma entrada por par (linha do artefato, arquivo citado), a partir da linha 22: toda linha que
contém `[X]` ou `[X,` com X em R, A, B, C, G, S, M; mais as linhas 224–232 (tabela cuja base declarada é [R]); mais a
linha do roteiro. Total: 132 entradas, numeradas na ordem do arquivo. Comando que gera a lista (rodado na raiz do
projeto):

```
awk 'NR>=22 { for (i=1;i<=7;i++){ t=substr("RABCGSM",i,1); if ($0 ~ "\\[" t "[],]") print "L" NR ":" t }
  if (NR>=224 && NR<=232) print "L" NR ":R"; if ($0 ~ /03b_chatgpt_roteiro_de_teste/) print "L" NR ":roteiro" }' \
  docs/desenho_v0.md | cat -n
```

**Sorteio declarado (vale para o critério):** `... | shuf -n 12 --random-source=<(yes 20261113)`, semente 20261113.
Saiu: 8, 12, 19, 50, 51, 53, 54, 55, 56, 58, 59, 60.

**Aviso sobre o sorteio:** a fonte `yes` repete os mesmos bytes e concentrou nove das doze entradas na seção 4 do
artefato. Mantive o resultado (não troco sorteio depois de ver) e fiz um **segundo sorteio, complementar**, com fonte
melhor: `shuf -n 12 --random-source=<(openssl enc -aes-256-ctr -pass pass:20261113 -nosalt -md sha256 </dev/zero)`
(OpenSSL 3.5.5). Saiu: 6, 7, 8, 12, 14, 29, 52, 67, 80, 108, 121, 128. Os dois estão abaixo.

### 2.1 Sorteio declarado — 1 falha em 12

| # | Linha | Afirmação ou escolha | Ponteiro | O que o trecho diz | Confere? | Marca correta? |
|---|---|---|---|---|---|---|
| 8 | 51 | O site se declara intermediário em todas as páginas | [A], seção 3, "Transparência de um intermediário" | [A] linhas 231–236: o Google não tem regra para site que repassa contato; a recomendação de dizer quem é o site e a diretriz de não deturpar propósito "apontam na mesma direção" | Confere | Sim (INFERÊNCIA; [A] linha 46 dá "A (o pedido) + inferência (a aplicação)") |
| 12 | 55 | Sem número de WhatsApp que conversa, tria e repassa | [R], quadro, linhas 36–37 | Linha 36: vedado pela API (leitura literal); linha 37: não conclusivo pelo aplicativo | Confere | Sim; "classe A" vale para a API, e o próprio artefato escreve "não conclusivo pelo aplicativo" |
| 19 | 58 | Página "quem somos" | [G], seção 9, linha 10 | Linha 10 da tabela ([G] linha 480): "quem somos" verificável; "premissa marcada"; como fator de citação é hipótese | Confere | Sim (PREMISSA como fator de citação) |
| 50 | 132 | Exibir número da licença e órgão como constam no documento; qual número vale na capital é não conclusivo | [R], linhas 209–213 | Exatamente isso: CEVS ou CMVS não conclusivo; "exibe-se o número como consta na licença" | Confere | Sim |
| 51 | 133 | Razão social por extenso e endereço | [R], linhas 235–236 | "Por prudência, sem base conferida na fonte: razão social por extenso e endereço (indício da CVS 9/2000)" | Confere | Aceitável; "por prudência" não está na legenda do artefato (correção 16) |
| 53 | 135 | Campo "Área atendida, como a licenciada declarou" | [B], seção 6 | [B] linhas 347–349: inferência de que o perfil no mapa de uma parceira rende contatos da região da base dela. Fala do bloco de mapa, não do que a página do site exibe; [B] linhas 85–86 diz que a área declarada não estende alcance | **Falha**: o trecho existe e diz o que se cita, mas não sustenta a escolha | A marca INFERÊNCIA repete a de [B]; o defeito é o ponteiro (correção 11) |
| 54 | 136 | Marca "Publicidade" quando posição ou destaque for pago | [R], linhas 217–218 e 233–235 | CDC art. 36 (linhas 217–218); "a marca de publicidade onde a posição ou o destaque for pago" (linhas 234–235) | Confere | Sim (classe A) |
| 55 | 141 | Texto da faixa fixa | [R], linhas 246–251 | Item (iii), marcado em [R] como inferência: não é dedetizadora, não tem licença, não executa; contrato, nota e comprovante são da licenciada | Confere (a faixa omite "não tem licença": correção 19) | Sim (INFERÊNCIA) |
| 56 | 147 | Não usar texto ou imagem de medo | [R], linhas 188–189 e 239 | RDC 622 art. 22, I; item (ii) da conclusão | Confere | A tabela 4.3 não tem coluna de marca; a fonte é classe A |
| 58 | 149 | Não dizer "inócuo", "seguro", "atóxico", "produto natural", "sem risco para crianças e animais" | [R], linhas 193–194 e 241–242 | Art. 22, III; a linha 242 avisa que "sem risco para crianças e animais" é exemplo de quem escreveu, não texto da norma | Confere, com ressalva: o artefato lista a frase sem esse aviso (correção 15) | — |
| 59 | 150 | "24 horas", "garantia", "melhor preço" só com prova guardada | [R], linhas 243–244 | CDC art. 36, parágrafo único, e art. 38: não são vedadas; quem publica tem de poder provar | Confere | — |
| 60 | 151 | Não dizer "a melhor" sem critério exposto | [A], seção 3 (sistema de avaliações comparativas) | [A] linha 220: expor o critério e o que foi conferido; não se autodeclarar "a melhor" (classe A, 1 leitura) | Confere | — |

### 2.2 Sorteio complementar — 0 falha em 12

| # | Linha | Afirmação ou escolha | Ponteiro | O que o trecho diz | Confere? | Marca correta? |
|---|---|---|---|---|---|---|
| 6 | 42 | Posição e clique pelo Search Console; sem rastreador automático | [A], seção 8 | Linhas 360 e 367: as quatro métricas do relatório; consulta automática para checar posição é vedada | Confere | Fonte classe A |
| 7 | 51 | Declaração de intermediário | [R], seção (b), item (iii), linhas 246–251 | Como na entrada 55 acima | Confere | Sim |
| 8 | 51 | Idem | [A], seção 3 | Já conferido | Confere | Sim |
| 12 | 55 | Sem central de WhatsApp | [R], linhas 36–37 | Já conferido | Confere | Sim |
| 14 | 56 | Não pede, não compra, não exibe avaliação copiada; sem estrelas | [A], seção 5 | Linhas 278–279: não agregar avaliações de outros sites; entidade que controla as avaliações sobre si não tem estrelas; "na fase atual: sem estrelas" | Confere, com ressalva: "não pede" não está em [A] seção 5 nem em [R] linha 29; é escolha mais estrita (correção 17) | Classe A vale para "não compra", "não copia", "sem estrelas" |
| 29 | 99 | Página de bairro só com algo que só ela diz | [A], seção 2.2, linha 189 | Linha 189: "cada página tem algo que só ela pode dizer" | Confere | A seção 3.3 não marca; a tabela de [A] é inferência do guia (correção 16) |
| 52 | 134 | "Licença conferida em…" e link para a consulta pública | [S], seção 4.4 | Linhas 223–224: a consulta pública de licenças do estado apareceu uma vez | Confere | Sim (PREMISSA; o artefato diz que não leu como a consulta funciona) |
| 67 | 172 | Mensagem pronta no link | [R], linha 439 | Linhas 438–439: link `wa.me`, recurso oficial, com mensagem pré-preenchida, marcado [S] (só leitura do subagente) | Confere | Sim; o artefato repete a ressalva "leitura só do subagente" |
| 80 | 231 | Aviso às empresas na exclusão | [R], linhas 328–331 | LGPD art. 18, § 6º, texto literal | Confere | Sim |
| 108 | 287 | Nunca consultar o Google por robô | [A], seção 8 | Linha 367 | Confere | Sim |
| 121 | 323 | Restrição (b): depende de toda oferta nomear a licenciada | [R], seção (b) | Linhas 257–258 (veredito), 195–196 e 254 (quem "concorreu"), 200–213 (pontos não conclusivos do estado) | Confere | — |
| 128 | 334 | Dependência de uma licenciada | [M], seção 4.3, riscos | [M] linha 342: "se ela sai, a região fica sem receita e sem empresa para nomear" | Confere | — |

## 3. Varredura de todos os ponteiros

Conferi as 132 entradas, uma a uma, contra o arquivo citado (seção, linha, número).

### 3.1 O que bate (resumo, para constar)

- **[R], por linha:** 25, 29, 31, 36–37 (quadro); 186–187, 188–189, 190–192, 193–194, 209–213, 217–218, 223–224,
  225–229, 231–258, 233–235, 235–236, 239, 241–242, 243–244, 246–251, 250–251, 253–262, 257–258; 296–297, 298–302,
  305, 306–307, 324–325, 328–331, 332–334, 342–344, 346–356, 349–350, 350–351, 352, 353–355, 355, 356, 358–364,
  358–368, 360–361, 363–364, 368; 398, 432–446, 438–441, 439, 440–441, 442–446, 448–451; 468–477. Todas existem e
  dizem o que o artefato atribui.
- **[A], por seção:** 1.3 (atualização central aberta em 10/11/2026); 2.1 (página de entrada, conteúdo em escala,
  compra de link, `rel="sponsored"`); 2.2 (linhas 187–194, 189, 191–192; "dois limites honestos" nas linhas 196–198);
  3 (transparência, "quem, como e por quê", IA generativa, avaliações comparativas, YMYL); 4 (título, endereços, links,
  canônica, sitemap, celular, intersticiais, JavaScript, descrição por programa); 5 (`Organization`, `LocalBusiness`,
  estrelas, `BreadcrumbList`, fim do resultado rico de FAQ em 07/05/2026); 7 (fecho); 8; 9.
- **[B]:** seção 3.1 (resposta a avaliação só com aprovação), 6, 7 (inferência do guia sobre "garantido pelo
  Google"), 9 (grade), 10 e 10.2, e o fecho de "O que não cabe para um gerador de leads" (linhas 482–483).
- **[C]:** 1.1, 1.2, 1.3, 3, 7.1, 7.2, 7.3, "O que é disputado".
- **[G]:** seção 2; seção 9, linhas 1 a 4, 5, 6, 7, 10 e 15 da tabela.
- **Roteiro, seção 4:** 30 perguntas, rodada mensal, repetições obrigatórias — confere.
- **Números de [S]:** 79 buscas; 73, 68 e 60 de 79 (seção 3); 10 domínios com 39% (4.1); 13 domínios em 5 ou mais das
  20 buscas por bairro (4.2); 87% e 79% (4.2), "79% a 87%" (seção 8); 68% e 1% no grupo F (4.2); 12 de 67 (7.3);
  consulta pública numa busca (4.4); grupo H não feito. Todos estão em [S].
- **Números de [M]:** "até 4 ou 6 prestadores" (seção 6); "R$ 20 a 60" não confirmado nem derrubado (seção 7); modelo
  de uma licenciada por região (seção 1, item 9; 4.3; 4.6); "não sei" (seção 8). Todos estão em [M].
- **RODADA.md:** item 8 (pergunta fixa) e fila de reserva 4 e 5 existem como citados.

### 3.2 Ponteiros que não batem

| Linha | Ponteiro | Defeito | Gravidade |
|---|---|---|---|
| 262 | [S], seção 2, e "(como no item 4)" | O artefato chama a conferência de posição de "manual" e a compara ao item 4. [S] diz o contrário: a coleta foi feita por script, em lotes (2.2, linhas 83–87; `coletor.js`), [S] mesmo a classifica como "consulta automática" que a política de spam veda (2.3, item 9, linhas 109–112), a decisão de manter isso está na fila do owner, e houve verificação de robô na 80ª busca (2.4, linhas 116–118) | **Alta** (correção 1) |
| 135 | [B], seção 6 | Trecho sobre o bloco de mapa; não sustenta o campo "Área atendida" (falha do sorteio) | Média (correção 11) |
| 254 | [M], seção 4.2, riscos | O artefato diz "não levantado no item 2 nem no item 5". [M] linha 299 diz que o número do site que encaminha a ligação "só vale no site", com base em [R] linhas 155–157; não levantada é só a gravação da chamada | Média (correção 12) |
| 28–29 | [S], seções 4.2 e 7.3 | "Quase tudo… com uma página por bairro": o dado que sustenta isso (50 de 67 sites têm páginas por localidade) está em [S] seção 8, linha 334, não nas seções citadas; em 4.2, páginas por local são 13% e 4% nas buscas sem bairro | Baixa (correção 17) |
| 90 | [S], seção 4.2 | "Páginas de serviço ou de segmento": a coluna de [S] é "página interna de serviço ou outra" | Baixa (correção 17) |
| 111 | [A], seção 2.2 | "Sem lista de bairros no rodapé" com marca classe A: o texto classe A está em 2.1 (linha 163); a 2.2 é a tabela de inferência | Baixa (correção 17) |
| 115 | [G], seção 9, linhas 1 a 4 | A linha 2 da tabela de [G] (hospedagem, CDN e firewall sem bloqueio aos IPs publicados da OpenAI, classe A, "regra") não aparece no desenho | Baixa (correção 20) |
| 149 | [R], linhas 241–242 | Ver sorteio, entrada 58 | Baixa (correção 15) |
| 108 e 113 | [C] 7.1; [G] seção 9, linha 5 | As fontes levam "pode estar desatualizada" no estudo ([C] linha 343; [G] linha 475); o artefato escreve só "(fontes de 2025)" na 108 e nada na 113 | Baixa (correção 14) |

Nenhuma seção citada inexiste. Nenhum número citado difere do arquivo de origem.

## 4. Escolhas sem ponteiro, premissas não marcadas, números sem fonte

**Dado contrário omitido (o mais importante desta seção).** As linhas 28–31 e 88 apoiam a aposta do site em "o que
falta: licença conferida e visível" no número "12 de 67 sites" de [S] 7.3. A mesma seção de [S] (7.3, item 5, linhas
323–325; tabela 7.2, linha 284) diz que os 11 domínios que exibem número de licença ocupam **47% das primeiras
posições (37 de 79)** e 30% dos três primeiros. Ou seja: é minoria entre os sites, mas não falta no topo do resultado.
[S] avisa que isso não prova que exibir a licença melhore a posição. O desenho cita só a metade favorável (correção 2).

**Premissas marcadas no corpo que faltam na "lista única" da seção 10 (linhas 345–357):**
- linha 58: "quem somos" como fator de citação por IA;
- linha 108: fatos em texto visível, para o ChatGPT;
- linha 113: conteúdo sem dependência de script, para o ChatGPT;
- linha 290: ritmo de publicação.

**Premissas ou inferências sem marca:**
- linhas 306–307: "é o caso mais simples perante as quatro restrições". [M] seção 1, item 9 (linha 47) abre com
  "Leitura minha, não fato";
- linhas 97–100 (seção 3.3): as condições 2 e 3 vêm da tabela que [A] (linhas 183–185) marca como inferência do guia;
  a 3.3 não tem marca nenhuma (a 3.2, linha 86, tem);
- linhas 183–185: registrar o clique por um endereço do próprio site que redireciona. [R] descreve o Desenho B como
  botão que "abre direto" o WhatsApp da licenciada (linha 438); o salto intermediário não está em [R]. O artefato o
  chama de "decisão de implementação", sem marca;
- linha 56: "não pede" avaliação (escolha mais estrita que a regra citada).

**Números sem fonte nem marca:** "3 a 5 licenciadas" (linha 300); "1 a 3 licenciadas" (linha 301); "duas ou três
licenciadas" por página (linha 176); "68 e 60 das 79 buscas" sem ponteiro na célula (linha 322; o número está em [S]
seção 3).

**Escolhas sem ponteiro:** T8 "Como conferir a licença" (linha 73; coberta em parte pela premissa 10); T9 "Preços"
(linha 74); T12 "Para dedetizadoras" (linha 77); o código na mensagem (linha 172; a premissa de que a licenciada
aceite conferir está marcada).

**Marcas fora da legenda** das linhas 16–18: "escolha de desenho" (52), "por prudência" (133), "observação da
amostra" (87, 90), "requisito de medição" (119), "regra do projeto" (289). Pela legenda do próprio artefato, escolha
sem evidência A ou B é PREMISSA.

## 5. Conferência das restrições do item 2

Lido o quadro de vereditos de [R] (linhas 21–38) e a conclusão de cada seção.

| Ponto de [R] | Veredito em [R] | O que o desenho faz | Resultado |
|---|---|---|---|
| Perfil próprio, endereço de fachada, perfil da licenciada com site ou telefone do intermediário (linhas 25–27) | Vedado | Não usa (linhas 53, 341–342) | Sem dependência |
| Administrar o perfil da licenciada (linha 28) | Permitido com condição | Só na fase 5, remetendo a [B] seção 10 (linhas 312–314) | Confere; as condições não são repetidas, só apontadas |
| Avaliação comprada ou incentivada (linha 29) | Vedado | Não usa; sem estrelas (linhas 56, 288) | Sem dependência |
| Site de terceiro divulgar o serviço (linha 30) | Permitido com condição | Nomeia executora e licença, sem termos vedados, declara-se intermediário (seções 2 e 4) | Confere |
| Página que oferece sem nomear (linha 31) | Não conclusivo | Não tem essa página (linhas 160–162) | Tratado como risco, não como permitido |
| Razão social e endereço, CVS 9/2000 (linha 32) | Não conclusivo | Exibe, "por prudência", dizendo que a base não foi conferida (linha 133) | Marcado |
| Repasse a uma e a várias empresas (linhas 33–34) | Permitido com condição; nomear cada uma é não conclusivo | Nomeia cada uma, uma caixa por empresa (linhas 204–209) | Adota o lado mais seguro |
| Vender só com legítimo interesse (linha 35) | Não conclusivo | Não usa | Sem dependência |
| Número do site que tria e repassa (linhas 36–37) | Vedado (API); não conclusivo (aplicativo) | Fora (linhas 55, 250) | Sem dependência |
| Botão que abre o WhatsApp da licenciada (linha 38) | Permitido com condição | Via A | Confere, com a ressalva do redirecionamento (correção 7) |
| Qual número de licença vale na capital (linhas 209–213) | Não conclusivo | Exibe o que consta na licença (linha 132) | Marcado |
| Prazo de guarda da prova; caixa pré-marcada; prazo de resposta ao titular | Não conclusivo / não fixado | Marcados nas linhas 239, 226 e 242 | Marcado |
| Variante do formulário (linhas 442–446) | Inferência de [R] | O artefato diz que é inferência (linhas 191–192) | Marcado |

**Texto de consentimento (5.2) contra a "Conclusão operacional" de [R] (linhas 348–356):**

| O que [R] pede | No texto das linhas 199–218? |
|---|---|
| Finalidade (receber orçamento) | Sim: "só para que ela me mande um orçamento de controle de pragas por WhatsApp ou por ligação" |
| Autorização separada e destacada para o repasse | Sim: caixa própria, em negrito, não pré-marcada (linha 226) |
| Quem é o site e como falar com ele | Sim: responsável, razão social e CNPJ, e-mail |
| Para quais empresas e para quê, nomeadas | Sim: nome, número da licença e órgão; a segunda caixa traz nome e número, sem o órgão |
| Quais dados vão | Sim: nome, telefone, bairro, tipo de praga, tipo de imóvel (os mesmos campos da linha 194) |
| Pode recusar e o que acontece | Sim |
| Como revogar e pedir exclusão, de graça | Sim |
| Prova guardada (versão do texto, data e hora, o que marcou, a que empresas foi) | Sim, na linha 238, e o texto avisa a pessoa de que o registro da autorização fica |
| Aviso a cada empresa na exclusão | Sim: "avisamos na hora cada empresa que o recebeu" |
| Marketing é outra finalidade | Sim: "não são usados para propaganda"; linha 253 |
| Opt-in do WhatsApp nomeia quem vai falar ([R] linha 398) | Sim |

Nada do que a conclusão pede falta. Observação: a Via B não cita as obrigações do agente de pequeno porte que [R]
levantou (linhas 338–341: canal com o titular, registro simplificado, segurança básica), nem o ponto não conclusivo
"controladores independentes ou conjuntos" (linha 320). Entra na correção 8.

**Bloco "Quem executa" (4.1) contra a "Conclusão para o site" de [R] (linhas 231–262):**
- (i) identificação da executora, número da licença, órgão emissor "como constam no documento", marca de publicidade
  onde posição ou destaque for pago, e, por prudência, razão social e endereço: **todos presentes** (linhas 131–136).
  CNPJ, validade e responsável técnico não são exigidos na propaganda e o desenho não os impõe.
- (ii) o que não dizer: **presente** em 4.3 (linhas 147–150), nos quatro grupos.
- (iii) quem é o site: **presente** na faixa fixa (linhas 140–141) e na seção 2; falta "não tem licença".
- (iv) norma silente: **presente** em 4.4.
- Ponto aberto: T9 "Preços" (linha 74) mostra faixas "informadas pelas licenciadas do site" e está marcada como "não
  oferece o serviço", sem bloco "Quem executa". O artefato não diz se T9 nomeia as licenciadas nem se tem botão
  (correção 18).
- Consequência de [M] não trazida: com uma licenciada pagante por região (modelo previsto para a fase 4), [M] 4.3
  (linha 339) diz que a página "vira, na prática, publicidade de uma empresa" e "não pode parecer comparação isenta".
  A linha 136 cobre "posição ou destaque pago", mas o desenho não liga isso ao modelo da fase 4 (correção 10).

**Via A contra o "Desenho B" de [R] (linhas 438–441):** corresponde no que decide — a conversa é iniciada pela pessoa,
com a empresa que atende, no número dela; o site registra só o clique; mensagem pronta do link oficial (leitura só do
subagente, dito na linha 172). Diferenças que [R] não descreve: o clique passa por um endereço do site antes de ir ao
link oficial (linhas 183–185) e a mensagem leva um código de origem.

**Ponto tratado como resolvido sem estar levantado:** a linha 173 diz "Nenhum dado da pessoa" e a 178 diz "o site não
tem dado dela para excluir". As linhas 185–187 do próprio artefato admitem que o registro de acesso guarda endereço
IP, "que pode ser dado pessoal", e que isso não foi levantado no item 2; as linhas 119 e 263 exigem guardar esse
registro bruto. Em [R], o guia de cookies da ANPD consta como não lido (linhas 490–492). As duas frases afirmam mais
do que o levantamento permite (correção 6).

## 6. Dependências proibidas

| Prática | Há dependência? | Onde conferi |
|---|---|---|
| Perfil de empresa fora da regra | Não | Linhas 26, 53, 322, 341 |
| Endereço fictício ou de fachada | Não. O endereço exibido é o da licenciada (linha 133) | Linhas 133, 341 |
| Avaliação fabricada, comprada ou incentivada | Não | Linhas 56, 288, 341 |
| Link comprado | Não; link para parceira que paga leva `rel="sponsored"` | Linhas 57, 342 |
| Consulta automática ao Google | Não: "nunca por robô" (linhas 42, 260, 262, 287) | Ressalva: a linha 262 remete ao método do item 4, que [S] descreve como script (correção 1) |

Sugestão ligada a link: [A] 2.1 (linhas 165 e 167) avisa para não exigir link de volta da licenciada. T12 (linha 77)
fala do "que é exigido dela" sem dizer isso (correção 18).

## 7. Forma

- **Português:** sim.
- **Caminho absoluto:** os sete arquivos de base e o roteiro estão com caminho absoluto (linhas 9–15 e 264). Sem
  caminho: a fila de reserva (linhas 272–273 e 303) e o item 8 (linha 337), que estão em
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`; e o protótipo (linha 184) (correção 21).
- **Jurídico como levantamento:** sim (linhas 19–20; fase 1 manda os pontos não conclusivos e os textos das seções 4
  e 5 a advogado). Exceção de tom: as duas frases da correção 6.
- **Dado pessoal:** nenhum. Nomes, licença, endereço e e-mail são "EXEMPLO" ou colchetes. Nenhum telefone, nenhum
  nome de pessoa, nenhum domínio de empresa real.
- **Nada afirmado como feito:** a linha 4 diz que nada foi publicado, comprado, cadastrado nem enviado; publicar,
  comprar domínio e falar com empresa aparecem como atos futuros do owner (linhas 289, 300–301).
- **Unidade, período, país:** os números de [S] vêm com "na amostra de 79 buscas"; não trazem a data nem o limite
  "um ponto, uma hora, uma conta" de [S] 2.3. A linha 87 escreve "não verificada". Aceitável para um desenho que
  remete a [S]; registro.

## 8. Correções pedidas

### De conteúdo

1. **Linha 262** — tirar "(como no item 4)" ou dizer a verdade sobre ele: a coleta do item 4 foi por script, [S]
   (2.3, item 9) a chama de consulta automática e a decisão está na fila do owner. Definir "conferência manual" como
   pessoa digitando a busca, sem script, e dizer quem faz ("owner ou sessão" deixa aberto que a sessão repita o
   método do item 4).
2. **Linhas 28–31, 88 e 347** — citar também [S] 7.3, item 5: os 11 domínios com número de licença têm 47% das
   primeiras posições (37 de 79) e 30% dos três primeiros. Reescrever "o que falta" e a premissa 1 com os dois lados.
3. **Linhas 43–44 contra a linha 300** — "a primeira despesa só vem depois de uma licenciada aceitar ser nomeada"
   contradiz a fase 1, cuja despesa (consulta jurídica) está na mesma fase que a conversa com as licenciadas e listada
   antes dela. Ordenar os passos da fase 1 ou corrigir a frase.
4. **Linhas 301 e 302 contra as linhas 35, 68 e 166** — dizer em que fase o botão entra. A versão 0 e o tipo T3
   incluem o botão; a fase 2 publica as páginas com licenciadas; a fase 3 lista "Botão da Via A" como o que se faz.
5. **Linhas 79, 301 e 349** — uniformizar o número de páginas ("cerca de 20 a 25" contra "cerca de 20"). A soma da
   tabela 3.1 dá de 18 a 29 com 1 a 3 licenciadas; mostrar a conta.
6. **Linhas 173 e 178–179 contra as linhas 119 e 185–187** — trocar "nenhum dado da pessoa" e "o site não tem dado
   dela para excluir" por "nenhum dado de contato"; marcar o tratamento de IP em registro de servidor como não
   levantado (o guia de cookies da ANPD não foi lido, [R] linhas 490–492); incluir o ponto na política de privacidade
   (T11) e na lista do advogado da fase 1.
7. **Linhas 183–185** — marcar o registro do clique por endereço próprio com redirecionamento como INFERÊNCIA ou
   PREMISSA (não está no Desenho B de [R]); e dizer como robôs e cliques repetidos ficam fora da contagem: o botão é
   `<a href>` rastreável (linha 113), os robôs estão liberados (linha 115) e o clique é a unidade de lead (linha 265)
   e de cobrança (linha 303).
8. **Linhas 189–244** — dizer por que canal o site entrega o pedido do formulário à licenciada. [M] 4.2 (linha 235)
   deixa "o canal é escolha do item 6" e o desenho não escolhe. Acrescentar as obrigações do agente de pequeno porte
   ([R] linhas 338–341) e o ponto não conclusivo dos controladores ([R] linha 320).
9. **Linhas 345–357** — completar a "lista única": faltam as premissas das linhas 58, 108, 113 e 290 e os números
   sem marca das linhas 176, 300 e 301.
10. **Linhas 306–307** — marcar "é o caso mais simples perante as quatro restrições" como INFERÊNCIA ([M] diz
    "leitura minha, não fato"). Trazer a consequência de [M] 4.3 (linha 339): com uma licenciada pagante por região,
    a página é publicidade dela e leva a marca da linha 136, sem parecer comparação isenta.

### Menores

11. **Linha 135** — trocar o ponteiro [B, seção 6] por um que sustente o campo (por exemplo [R], linhas 257–258) ou
    marcar como escolha de desenho.
12. **Linha 254** — corrigir "não levantado no item 2 nem no item 5": só a gravação de chamada não foi levantada; o
    número do site que encaminha está em [R] linhas 155–157 e em [M] linha 299.
13. **Linhas 267–268 e 181** — definir "lead vendido" (contato cobrado da licenciada) separado de lead válido,
    orçamento e serviço fechado; e escolher entre conferência "por amostra" (linha 181) e contagem mensal (linha 267).
14. **Linhas 108 e 113** — acrescentar "pode estar desatualizada" (fontes de 2025 e de 2024), como pede a regra da
    rodada.
15. **Linha 149** — marcar "sem risco para crianças e animais" como exemplo, não texto da norma ([R] linha 242).
16. **Linhas 16–18, 52, 87, 90, 97–100, 119, 133 e 289** — pôr na legenda as marcas usadas fora dela ou convertê-las;
    marcar INFERÊNCIA na seção 3.3.
17. **Linhas 28, 56, 90, 111 e 322** — ajustar ponteiros: [S] seção 8 para "uma página por bairro"; "não pede" como
    escolha; nome da coluna de [S] 4.2; [A] 2.1 (linha 163) para a lista de bairros no rodapé; [S] seção 3 para
    "68 e 60 das 79".
18. **Linhas 73, 74 e 77** — dar ponteiro ou marca a T8, T9 e T12; dizer se T9 nomeia as licenciadas (então leva o
    bloco "Quem executa") ou é conteúdo sem botão; em T12, dizer que não se exige link de volta ([A] 2.1, linhas 165
    e 167).
19. **Linhas 140–141** — acrescentar "não tem licença" à faixa fixa ([R] linha 248) e dizer em que lugar da página
    ela fica.
20. **Linha 115** — incluir a linha 2 da tabela de [G] seção 9 (hospedagem, CDN e firewall sem bloqueio aos IPs
    publicados da OpenAI).
21. **Linhas 184, 272–273, 303 e 337** — pôr o caminho absoluto de `RODADA.md` e do protótipo.

## 9. O que não conferi

- Não reabri nenhuma fonte primária na web: a verificação é do artefato contra os arquivos do projeto. A exatidão de
  [R], [A], [B], [C] e [G] frente às fontes é das verificações dos itens 2 e 3; a de [S] e [M], das verificações dos
  itens 4 e 5, que estavam em curso.
- Não refiz as contas de [S] a partir dos CSVs; conferi só que os números citados no desenho estão em [S].
- Não li o protótipo (`/home/ancastelo/pessoal/SEO_Project/prototipo/`), que é do item 7 e estava sendo gravado
  durante esta leitura.
- De [B] li as seções citadas e o resumo, não o arquivo inteiro; de [C] e [G], as seções citadas e os fechos.
