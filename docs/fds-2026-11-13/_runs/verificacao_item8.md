# Verificação independente do item 8 — perguntas ao owner

- **Quando:** sexta, 13/11/2026, 22:29 (Brasília, lido de `TZ=America/Sao_Paulo date`). Leitura dos arquivos entre
  22:22 e 22:29.
- **Quem:** verificador em contexto limpo; não recebeu a conclusão de quem produziu.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` (34 linhas; gravado às 22:20, versão do
  commit `e0760ca`).
- **Portão (transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 66):**
  "`docs/perguntas_owner.md`: no máximo dez, em ordem de quanto mudam o desenho, cada uma com a opção adotada por
  padrão. Uma delas é fixa: "você conferiu a política do seu empregador sobre atividade paralela?" (só a pergunta; não
  pesquise)"
- **Veredito: REPROVADO** — pela regra desta verificação (mais de 2 perguntas com falha de conteúdo). São quatro
  falhas claras (perguntas 2, 4, 5 e 8) e quatro leves (3, 6, 9 e 10). Nenhuma pede refazer o arquivo: todas se
  corrigem trocando frases. A estrutura, a pergunta fixa e a lista "O que não virou pergunta" estão certas.
- **Natureza:** o que encosta em norma, aqui, é conferência do artefato contra o levantamento do projeto; não é
  parecer jurídico.

## 1. O que foi lido

| Arquivo (caminho absoluto) | O que li |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D") | inteiro (420 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` ("R") | inteiro (499 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` ("M") | linhas 1–96 (seções 1 e 2), 149–236 (4.0 e 4.1), 318–359 (4.3), 409–476 (4.5 e 4.6), 510–705 (5 a 8) |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` ("S") | seções 4 (inteira), 8, 9, 10 e 11 |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` | cabeçalho e contagem: 1.260 linhas, coluna `volume` = "não medido" em todas |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | linhas 1–70 e a seção 4 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` e as quatro páginas do protótipo | LEIA-ME inteiro; nas páginas, busca por formulário, botão, lista de pragas e página de bairro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` | inteiro ("Fila do owner": 5 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | inteiro (portão do item 8) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | seções 2.1 e 2.2 (linhas 150–200), para a frase da página de entrada |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` e `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | trechos sobre robôs de treino (03b: seções 2 e 9; 03: seções 1.2 e 3) |

Também comparei, só em leitura (`git log`, `git show`, `git diff`), a primeira versão do desenho (commit `e0a971b`)
com a atual, para entender a remissão das perguntas 3 e 4. Não usei a web, não abri navegador, não pesquisei nada
sobre política de empregador, não editei arquivo nenhum além deste.

## 2. Portão

| Exigência | Resultado | O que conferi |
|---|---|---|
| No máximo dez | **Cumpre** | São dez linhas numeradas de 1 a 10 |
| Pergunta fixa, com essas palavras | **Cumpre** | Linha 1: "Você conferiu a política do seu empregador sobre atividade paralela?" — igual ao portão (só muda a maiúscula inicial) |
| Só a pergunta, sem pesquisa | **Cumpre** | A linha não traz conteúdo de política de empregador nenhum nem nome de empregador; diz "Esta pergunta não foi pesquisada, por regra da rodada". Busca no arquivo por nome de empresa, salário e telefone: nada (a única ocorrência de "mercado" é o caminho `docs/mercado/serp_sp.md`) |
| Cada uma com a opção adotada por padrão | **Cumpre, com ressalva** | As dez têm a coluna preenchida. Ressalva: a coluna mistura dois sentidos — nas perguntas 1 e 9 diz o estado de hoje ("Não conferido", "Não feito"); nas 3 e 4 diz o caminho previsto ("Sim"), embora nada tenha sido feito. Ver correção 12 |
| Pergunta fechada (sim ou não) | **Cumpre** | As dez admitem "sim" ou "não" |
| Uma pergunta só | **Não cumpre em duas; ressalva em outras duas** | **8** cola quatro decisões (região de partida, seis pragas, número de páginas, sem página por bairro) e a coluna "se a outra" só trata de uma. **9** cola três medições, de fases diferentes (o Search Console só existe depois de publicar). **3** cola quem conversa, com quantas, sobre o quê e quando; **6** cola exclusividade e pagamento antecipado, que em M são eixos separados (4.3 e 4.6). A 2 também reúne atributos, mas é uma decisão só (o formato) e qualquer "não" tem a mesma consequência |
| Em ordem de quanto mudam o desenho | **Não cumpre em um ponto** | A pergunta 7 está abaixo de três que mudam menos (4, 5 e 6). Seção 4 abaixo |
| Nenhuma opção padrão publica, compra, cadastra, envia ou contata | **Cumpre** | Nenhum padrão é ato da sessão. As perguntas 3 (conversar com empresas) e 4 (advogado) são atos futuros do owner, e o texto diz que a sessão não contata ninguém |

## 3. Pergunta por pergunta

Legenda: **falha** = afirmação mais forte que a fonte, contrária a ela, ou remissão que não diz aquilo; **ressalva** =
imprecisão ou forma.

### Pergunta 1 — política do empregador (fixa)

- **Padrão** ("Não conferido… nada vai ao ar antes da sua resposta"): confere com D, seção 8, fase 0 (despesa
  nenhuma) e fase 1, letra (a).
- **Se a outra:** "o projeto para na fase 0". D põe a conferência como passo (a) da **fase 1** e diz que a fase 1 não
  passa "se… empregador vedar". É diferença pequena de rótulo (fase 0 × fase 1), sem efeito prático. A coluna só
  trata do caso "veda ou exige autorização"; falta meia frase para o caso "conferi e não há impedimento" (cai a
  trava (a) da fase 1). **Ressalva.**
- **Base:** D, seção 8, fase 1, letra (a): existe e diz isso. D, seção 9.2, última linha ("Política do empregador do
  owner — Só o owner confere"): existe.
- **Sem pesquisa:** confirmado.
- **Resultado: sem falha.**

### Pergunta 2 — intermediário declarado

- **Padrão:** "Sim" é o que D adota (seção 1, item 1; seção 2), e o protótipo segue (faixa fixa G3, sem perfil, sem
  telefone do site).
- **Afirmação "É o único formato que passa nas quatro restrições": mais forte que a fonte. FALHA.**
  - R dá ao formato o veredito **"permitido com condição"** (quadro, linha 30), "mesmo com os pontos não conclusivos
    em aberto" (linhas 257–258), e chama a lista final de "o que as quatro restrições, juntas, deixam de pé" (linha
    468). Não escreve "único" nem "passa".
  - Dois dos formatos alternativos são "não conclusivo", não "vedado" (página sem empresa nomeada, linha 31; central
    pelo aplicativo gratuito, linha 37): não "passam", mas também não foram reprovados pelo levantamento.
  - R dá "permitido com condição" também a administrar o perfil da licenciada (linha 28; M, 4.4), que é outro
    formato.
  - "Passa nas quatro restrições" lê-se como conclusão de conformidade; o cabeçalho do próprio arquivo diz que é
    levantamento, não parecer.
  - A pergunta 4 do mesmo arquivo chama "site de terceiro que nomeia a licenciada" de ponto "não conclusivo": as
    duas linhas se contradizem (uma diz mais que R, a outra diz menos).
- **Se a outra:** correto — os três formatos citados estão "vedado" ou "não conclusivo" (R, linhas 25, 31, 36–37; M,
  5.1 a 5.3), e a regra do item 6 impede desenhá-los.
- **Base:** R, quadro nas linhas 21–38: confere. D, seção 2: confere. M, seção 5: confere.

### Pergunta 3 — conversar com 3 a 5 licenciadas antes de gastar

- **Padrão:** confere com D, seção 8 (a primeira despesa só vem depois de uma licenciada aceitar) e com a seção 10,
  premissa 14. "3 a 5" é marcado **PREMISSA** em D; o artefato não repete a marca. **Ressalva.**
- **Se a outra:** "a fase 2 passaria a ser uma aposta sem parceira… o site sairia só com guias informativos". D não
  desenha esse cenário: diz que a fase 1 **não passa** se "nenhuma licenciada aceitar" e que a fase 2 é feita "com 1
  a 3 licenciadas nomeadas". A consequência descrita é coerente com D 4.4 (sem licenciada, sem página de oferta),
  mas é extrapolação do artefato; falta dizer que, pelo desenho, sem conversa não há fase 2. **Ressalva.**
- **Base — remissão errada. FALHA leve.** "D, seção 8 (fase 1, letra c)": na versão atual de D, a letra (c) é o
  advogado; as conversas são a letra **(b)**. A primeira versão do desenho tinha a ordem inversa; as letras foram
  trocadas na correção das 22:19 e o artefato não acompanhou. D, seção 4.4; D, seção 9.1 (linha da propaganda); M,
  seção 1, item 9: existem e dizem aquilo.
- **Forma:** quatro coisas numa pergunta (quem, quantas, o quê, quando); um "não" fica ambíguo.

### Pergunta 4 — advogado antes de publicar

- **Padrão:** "só depois de ao menos uma licenciada aceitar" confere com D, seção 8, fase 1, letra (c). "Sem essa
  revisão, o desenho não passa da fase 1" é leitura coerente com a coluna "O que prova" da fase 1.
- **Lista dos pontos "não conclusivo" — rótulos que não são os de R. FALHA.**
  - "site de terceiro que nomeia a licenciada": em R o veredito é **"permitido com condição"** (quadro, linha 30). O
    que R deixa aberto é outra coisa: se o dono do site pode ser autuado como quem "concorreu" ou "se beneficiou" e
    quais são os "dados essenciais" (linhas 253–255, "onde a norma é silente"); e a exigência estadual de razão
    social e endereço (linha 32).
  - "responsabilidade do intermediário": em R é "leitura de tribunal, **não levantada** aqui" (linhas 225–229), não
    "não conclusivo".
  - "endereço IP no registro do servidor": em D é "**não foi levantado** no item 2" (seção 5.1), não "não
    conclusivo"; e a base está em D, 5.1, não em R, seções (b) e (c).
  - "qual número de licença vale na capital" (R, linhas 209–213) e "prazo de guarda da prova" (R, linha 355):
    conferem.
- **Se a outra:** correto e na forma certa ("a sessão não emite parecer").
- **Base — remissão errada.** "D, seção 8 (fase 1, letra b)": o advogado é a letra **(c)**. Mesma causa da pergunta
  3. D, seção 9.1: confere (coluna "Como se saberia").

### Pergunta 5 — só o botão na primeira versão

- **Padrão:** "Sim" é o que D adota (seção 1, item 4; seção 5.1; formulário na fase 5) e o que o protótipo mostra
  (botão como link; formulário só como exemplo desativado na página de privacidade).
- **Afirmação "o site registra o clique e não guarda dado de ninguém": mais forte que a fonte. FALHA.** D, seção
  5.1, diz "nenhum dado **de contato** da pessoa (nome, telefone, conversa)" e, no item "Endereço IP", que o
  registro de acesso do servidor "guarda endereço IP, que pode ser dado pessoal", ponto **não levantado** e mandado
  ao advogado. R (linhas 440–441) só diz "não o telefone nem a conversa". O mesmo exagero aparece na coluna "se a
  outra" ("o site **passa a** tratar dado pessoal desde o primeiro dia"). A pergunta 4 do próprio arquivo cita o
  endereço IP: as duas linhas não batem.
- **Se a outra:** texto de consentimento, prova guardada e exclusão com aviso às empresas conferem com D, 5.2, e R,
  linhas 346–356. "Mais cara e mais arriscada" é leitura do artefato, sem número; D diz só que o formulário torna o
  site controlador "antes de se saber se alguém clica". Aceitável.
- **Base:** D, 5.1 e 5.2; R, seção (c), "Conclusão operacional" (linha 346); R, seção (d), "Os dois desenhos" (linha
  432): existem e dizem aquilo.

### Pergunta 6 — modelo de cobrança

- **Padrão:** confere com D, seção 8 ("modelo de cobrança previsto para a fase 4", marcado INFERÊNCIA) e com a fase 2
  ("1 a 3 licenciadas nomeadas, sem cobrança"; em D, "número PREMISSA", marca que o artefato não repete).
- **Afirmação "o 'R$ 20 a 60 por lead' da pesquisa antiga não se confirma nem se derruba":** mesma força de M, seção
  7 ("não dá para confirmar — nem para derrubar") e de D, seção 8. **Confere.** "O preço não tem fonte": confere com
  D ("o valor não tem fonte").
- **Incoerência dentro da linha. FALHA leve.** A pergunta opõe o padrão a "vender o mesmo contato a várias"; a
  coluna "se a outra" descreve outra alternativa (comparador com destaque pago ou clique, em que "o contato continua
  indo só à empresa que a pessoa escolher"). Com o botão da versão 0, o site não tem contato para vender a várias
  (D, 5.1; M, 4.1).
- **Se a outra:** marca de publicidade e critério de ordem conferem com M, 4.5. "Cresce o peso da marca
  'Publicidade'" é discutível: D, seção 8, diz que com uma só pagante a página inteira já é publicidade dela.
  **Ressalva.**
- **Base:** D, seção 8; M, 4.3, 4.5, 4.6 e 7: existem e dizem aquilo.
- **Forma:** exclusividade e pagamento antecipado são duas escolhas.

### Pergunta 7 — só parceiras autorizadas

- **Padrão:** é o que D adota **por implicação** (preço "informado por elas", área "como a licenciada declarou", fase
  1: "aceitam ser nomeadas?"). D não tem frase que diga "só quem autorizou" nem marca essa escolha como premissa.
- **Se a outra:** honesto — diz que o uso do cadastro público "não foi levantado", sem veredito. Confere: R não trata
  disso, e D diz que o funcionamento da consulta pública não foi lido.
- **Base fraca. Ressalva.** D, 3.1 (T3 e T7) e 4.1 sustentam só por implicação; S, seção 9, item 7, fala de
  candidatas a parceira, não de listar sem autorização. Os trechos de D que dizem aquilo são: seção 8, fase 1, letra
  (b); seção 9.1, linha da propaganda; seção 3.1, T12; seção 3.4, linha dos dados estruturados ("só com autorização
  dela").
- **Resultado: sem falha de conteúdo.** Está fora de ordem (seção 4).

### Pergunta 8 — região, pragas, páginas, sem bairro

- **Padrão:** seis pragas, 19 a 29 páginas e zero página de bairro conferem com D, 3.1, e com o protótipo (seis
  pragas no início; "não há uma página para cada bairro"). A marca de premissa confere com D, seção 10, premissa 3.
- **Afirmação "fora delas é o padrão que a política de spam do Google descreve como página de entrada": mais forte
  que a fonte. FALHA.**
  - S, seção 8, diz que o padrão dominante "**encosta** no que a política do Google descreve" e que "a aplicação é
    inferência do guia, não frase do Google".
  - D, 3.2, marca a mesma escolha como "classe A (texto da política) + **INFERÊNCIA** (aplicação)"; D, 3.3, marca as
    condições 2 e 3 como INFERÊNCIA.
  - O guia de busca orgânica (seção 2.2) diz que a tabela de sinais "não é regra do Google".
  - O texto da política fala de páginas voltadas a regiões ou cidades "que afunilam os usuários para uma página só";
    o artefato estende isso a qualquer página de bairro fora das três condições.
- **Forma: quatro perguntas numa.** A coluna "se a outra" só responde à do bairro.
- **Base:** D, 3.1, 3.2 e 3.3; S, 4.2 e 8: existem. "Como os concorrentes" confere (50 de 67 sites; 79% a 87% nas
  buscas com bairro).

### Pergunta 9 — três medições com as contas do owner

- **Padrão:** "Não feito… volume 'não medido'" confere (as 1.260 linhas do CSV). A sessão não pode fazer nenhuma das
  três: confere com D, seção 6, e S, seção 10.
- **Se a outra:** "a ordem das páginas da seção 3.1 pode mudar" — a seção 3.1 de D não tem ordem de páginas; tem
  tipos e quantidades. O que o volume poderia mudar é a premissa 3 (quais pragas, quantas regiões) e o plano de
  conteúdo, que é a tarefa 3 da fila de reserva. Nada é dito sobre o que muda com o resultado do roteiro do ChatGPT.
  **FALHA leve.**
- **Base incompleta. Ressalva.** O Planejador de palavras-chave não está em D, seção 6; está em D, seção 8, fase 1,
  letra (d), e em S, seção 10.
- **Forma:** três medições numa pergunta; o Search Console depende de publicar (fase 2) e não tem alternativa. "30
  perguntas" subestima o roteiro: a regra de medição pede 66 execuções por mês (seção 4 do roteiro).

### Pergunta 10 — robôs de treino

- **Padrão:** "Sim: liberar" é o que D adota (3.4, "liberados por padrão, DECISÃO DO OWNER"; seção 10, premissa 8) e
  o que o `robots.txt` do protótipo traz (`GPTBot` com `Allow: /`).
- **Afirmação "Não muda a presença na busca do ChatGPT":** sustentada, com a mesma força, em
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, seção 9, linha 4 da tabela (classe A) e seção 2.
  **Confere** — mas a fonte não está na coluna "Base", que só cita D e o `robots.txt`. **Ressalva.**
- **Se a outra: "troca-se uma linha… nada mais muda" vale só para o robô da OpenAI. FALHA leve.** A pergunta fala
  dos robôs de treino no plural. O arquivo do protótipo só nomeia o `GPTBot`; os demais (`Google-Extended`,
  `Applebot-Extended`, `ClaudeBot`) estão liberados pelo bloco geral, e bloqueá-los pede blocos novos. E o guia de
  respostas de IA (seção 1.2) registra que bloquear `Google-Extended` "pode tirar o site da fundamentação do
  aplicativo Gemini" (inferência do guia).
- **Base:** D, 3.4 e seção 10, premissa 8; `robots.txt`: existem e dizem aquilo.

### "O que não virou pergunta, e por quê"

| Item | Conferência | Resultado |
|---|---|---|
| Nome do site e domínio | D: nome de trabalho "EXEMPLO Guia"; comprar domínio é ato do owner (fase 2) | Confere |
| Gestão do perfil da licenciada | D, seção 8, fase 5: "gestão do perfil da licenciada como segundo serviço". "Depende do resultado do piloto" não é frase de D (a fase 5 prova "que o modelo se repete com outra licenciada"); decorre da ordem das fases | Confere, com ressalva |
| PDFs oficiais, limite de buscas e "demais decisões operacionais" | PAINEL, "Fila do owner": 5 linhas, todas com opção adotada. Duas são nomeadas; as outras três (histórico do repositório; duas escolhas do roteiro do ChatGPT) entram em "demais". Nenhuma muda o desenho | Confere |

## 4. Ordem

O que muda no desenho se a resposta for a contrária, pelo que D diz:

| # | Se a resposta for a contrária | Tamanho da mudança |
|---|---|---|
| 1 | Se a política vedar: tudo para (D, fase 1, "empregador vedar"; 9.2) | Tudo |
| 2 | Cai o desenho inteiro (D, 9.3; regra do item 6) | Tudo |
| 7 | Muda aquilo de que o desenho depende: deixa de valer "nenhuma licenciada aceitar" como trava da fase 1 e como causa de inviabilidade (9.1); mudam T3, T4, T7 e T9, o bloco "Quem executa" (sem preço informado nem área declarada), a contagem de leads com a licenciada (seção 6), o número de páginas e o modelo de cobrança; entra um ponto jurídico não levantado | Seções 3, 4.1, 6, 8 e 9 |
| 3 | Sem conversa não há fase 2 com página de oferta; a premissa "há licenciada disposta" fica sem teste | Seção 8 e a premissa central |
| 5 | A versão 0 passa a ter a Via B: o site vira controlador de dado de contato, com prova, exclusão, canal de entrega e mais texto para o advogado | Seção 5, T11, seção 9.1 (LGPD) |
| 4 | Nada muda nas páginas; os pontos em aberto viram risco assumido e cai uma trava da fase 1 | Uma trava da seção 8 |
| 8 | Entra T5 só dentro das três condições; mudam a contagem de páginas e a premissa 3 | Seção 3 (limitada por 3.3) |
| 6 | Muda o parágrafo do modelo de cobrança, que é da fase 4 e já é hipótese "para depois do piloto" | Um parágrafo da seção 8 |
| 9 | O mapa de palavras-chave ganha volume; pode mudar a premissa 3 | Dados; nada da estrutura |
| 10 | Uma linha do `robots.txt` (para o robô da OpenAI) | Uma linha |

**Ordem que eu defenderia: 1, 2, 7, 3, 5, 4, 8, 6, 9, 10.**

Onde difere da ordem do artefato (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):

- **A 7 sobe da sétima para a terceira posição. É a única troca que considero obrigatória.** Hoje ela está abaixo da
  6 (que troca um parágrafo da fase 4) e da 4 (que não muda página nenhuma). A resposta contrária à 7 muda a
  dependência central do desenho e também o sentido da 3: se o site pudesse listar quem não autorizou, a conversa
  deixaria de ser condição para haver página de oferta.
- **A 5 passa à frente da 4, e a 8 à frente da 6: trocas defensáveis, não obrigatórias.** A 4 pode ficar onde está
  se o critério declarado for "o que pode parar o projeto" (o resultado da revisão pode derrubar tudo), mas então o
  arquivo precisa dizer isso, porque a coluna "se a outra" da própria 4 não registra mudança nenhuma no desenho. Há
  ainda uma razão prática para a 5 e a 7 virem antes da 4: as respostas delas definem o que o advogado revê.
- **1, 2, 9 e 10:** no lugar certo. Não há pergunta que derrube o desenho abaixo de uma que troque uma linha.

## 5. Perguntas que faltam

Conferi em D as duas marcas "DECISÃO DO OWNER", as 17 premissas da seção 10, as seis fases da seção 8, as tabelas 9.1
e 9.2, e as 5 linhas da "Fila do owner" do painel.

| Decisão do owner | Onde está | Virou pergunta ou está na lista? | Avaliação |
|---|---|---|---|
| Robôs de treino | D, 3.4 (DECISÃO DO OWNER) | Pergunta 10 | Coberta |
| **Unidade de cobrança** (mensalidade, clique ou lead válido) | D, seção 8 (DECISÃO DO OWNER, "depois do piloto") | **Não** — nem pergunta, nem lista | Não precisa virar pergunta agora (o próprio D a adia), mas tem de entrar em "O que não virou pergunta", com o motivo. **Correção 9** |
| Criar conta numa plataforma de orçamentos para ver o preço de um pedido | M, seção 7 ("decisão do owner, fora da rodada") | Não | Baixo impacto no desenho; cabe uma linha na mesma lista |
| **O caminho até o mapa** (gestão do perfil da licenciada só na fase 5) | D, seção 8, fase 5 e último item; 9.1, linha do perfil | Está na lista | Não é falha do portão. Mas a decisão pesa mais que a pergunta 10: o owner definiu o projeto com "Google Maps" (RODADA, "O que o projeto é"), o bloco de mapa apareceu em 68 das 79 buscas (D, seção 8) e o desenho o deixa para a última fase. Se sobrar vaga, é a melhor candidata; se não, a linha da lista deve dizer isso. **Correção 10** |
| Em nome de quem o site responde (pessoa física ou jurídica) | D não marca como decisão nem como premissa; aparece em "quem somos" (seção 2) e no texto do formulário ("razão social e CNPJ do responsável", 5.2) | Não | É lacuna do desenho, mais do que do item 8. Toca a pergunta 1, o regime de agente de pequeno porte (5.2) e a cobrança da fase 4. Sugestão: uma linha em "O que não virou pergunta". Não conto como falha |
| Aprovar ou recusar o desenho como um todo | D, seção 8, fase 0 | Não, de propósito | As dez perguntas decompõem a aprovação. Sem reparo |
| Fila do owner do painel (5 linhas) | PAINEL | Na lista, duas nomeadas e três em "demais decisões operacionais" | Sem reparo |

Não achei decisão do owner que derrube o desenho e tenha ficado de fora. A única omissão formal é a unidade de
cobrança.

## 6. Afirmações de fato dentro das perguntas

| Afirmação | Onde | Fonte | Resultado |
|---|---|---|---|
| "É o único formato que passa nas quatro restrições" | 2 | R, linhas 30, 257–258 e 468–477; M, seção 1, item 1 | **Mais forte que a fonte** |
| Formatos alternativos "vedado" ou "não conclusivo" | 2 | R, linhas 25, 31, 36–37 | Confere |
| "o desenho trata 'há licenciada disposta' como premissa" | 3 | D, seção 8, fase 1; seção 10, premissa 14 | Confere |
| "o desenho não tem página de oferta sem empresa nomeada" | 3 | D, 4.4 | Confere |
| Lista dos pontos "não conclusivo" | 4 | R, linhas 30, 209–213, 225–229, 355; D, 5.1 | **Dois de cinco conferem; um contraria o veredito de R; dois são "não levantado"** |
| "não guarda dado de ninguém" | 5 | D, 5.1; R, linhas 440–441 | **Mais forte que a fonte** |
| "o texto já está pronto" | 5 | D, 5.2 | Confere |
| "R$ 20 a 60… não se confirma nem se derruba" | 6 | M, seção 7; D, seção 8 | Confere, mesma força |
| "de 1 a 3 licenciadas nomeadas" na fase gratuita | 6 | D, seção 8, fase 2 | Confere (falta a marca PREMISSA) |
| uso do cadastro público "não foi levantado" | 7 | R (ausência); D, 4.1 | Confere |
| "O número de páginas e a lista de pragas são premissas" | 8 | D, seção 10, premissa 3 | Confere |
| "é o padrão que a política de spam do Google descreve como página de entrada" | 8 | S, seção 8; D, 3.2 e 3.3; guia orgânico, 2.2 | **Mais forte que a fonte** |
| "O volume fica 'não medido'" | 9 | CSV, coluna `volume` | Confere |
| "Não muda a presença na busca do ChatGPT" | 10 | guia do ChatGPT, seções 2 e 9 | Confere, mesma força (fonte fora da coluna "Base") |
| "troca-se uma linha… nada mais muda" | 10 | guia do ChatGPT, seção 9; guia de IA, 1.2 e 3 | **Vale só para o robô da OpenAI** |

## 7. Forma

| Exigência | Resultado |
|---|---|
| Português | Cumpre |
| Caminhos absolutos | Cumpre: os nove caminhos escritos são absolutos; oito existem e o nono (`RESPOSTAS_OWNER.md`) é o arquivo a criar |
| Jurídico como levantamento | Cumpre no cabeçalho e nas perguntas 4 e 7. **Não cumpre na 2** ("passa nas quatro restrições") |
| Nenhum dado pessoal | Cumpre: sem nome de pessoa, de empregador, telefone ou salário |
| Número com fonte | Cumpre, com ressalva: "3 a 5" (pergunta 3) e "1 a 3" (pergunta 6) são PREMISSA em D e aparecem sem a marca |
| Linha de estado | Diz "escrita… às 22:12"; o arquivo foi alterado depois (perguntas 4 e 8, gravadas às 22:20) e a linha não registra. **Ressalva** |

## 8. Contagem e veredito

- **Falhas de conteúdo claras (4):** perguntas 2, 4, 5 e 8.
- **Falhas leves (4):** perguntas 3 (remissão a letra errada), 6 (pergunta e alternativa não batem), 9 (remete a uma
  "ordem das páginas" que a seção 3.1 não tem), 10 ("uma linha" só vale para um robô).
- **Sem falha de conteúdo (2):** perguntas 1 e 7.
- **Portão:** cumpre o limite de dez, a pergunta fixa sem pesquisa e a opção padrão; não cumpre "uma pergunta só"
  nas perguntas 8 e 9 nem a ordem na pergunta 7.

**REPROVADO**: quatro perguntas com falha de conteúdo clara, acima do limite de duas. As falhas são de redação, não
de substância: o que o arquivo pergunta é o que o desenho deixa em aberto, e nenhuma opção padrão faz algo que não
pode. Depois das correções abaixo, o arquivo precisa de nova conferência das linhas alteradas.

### Correções pedidas

1. **Pergunta 2:** trocar "É o único formato que passa nas quatro restrições" por texto da força de R — por exemplo,
   "é o formato que o levantamento deixa de pé, com o veredito 'permitido com condição'; os alternativos lidos estão
   'vedado' ou 'não conclusivo'".
2. **Pergunta 4, lista:** trocar "site de terceiro que nomeia a licenciada" pelo ponto que R deixa aberto (se o dono
   do site pode ser autuado como quem "concorreu"; exigência estadual de razão social e endereço) e separar o que é
   "não conclusivo" do que é "não levantado" (responsabilidade do intermediário; endereço IP).
3. **Perguntas 3 e 4, coluna "Base":** corrigir as letras da fase 1 — conversas são a letra (b), advogado é a letra
   (c). Na 4, acrescentar D, seção 5.1, como base do endereço IP.
4. **Pergunta 5:** trocar "não guarda dado de ninguém" por "não guarda dado de contato (nome, telefone, conversa); o
   registro do servidor guarda endereço IP, ponto não levantado", e ajustar "passa a tratar dado pessoal" na coluna
   "se a outra".
5. **Pergunta 8, afirmação:** rebaixar para a força da fonte — "pela leitura do guia (inferência, não frase do
   Google), encosta no que a política de spam descreve como página de entrada".
6. **Pergunta 8, forma:** deixar uma decisão só (sem página por bairro na versão 0) e levar região de partida, seis
   pragas e 19 a 29 páginas para a coluna do padrão, como premissas.
7. **Pergunta 9:** reduzir às duas medições da fase 1, letra (d) (Planejador e roteiro), ou dizer o que acontece com
   resposta parcial; trocar "a ordem das páginas da seção 3.1" por "a escolha das pragas e regiões (premissa 3)";
   acrescentar à base D, seção 8, fase 1, letra (d), e S, seção 10.
8. **Ordem:** subir a pergunta 7 para a terceira posição e renumerar, inclusive as remissões internas ("pergunta 3"
   na linha 4; "perguntas 1 a 4" na lista final). Se a 4 ficar acima da 5, escrever no cabeçalho o critério que a
   mantém ali.
9. **"O que não virou pergunta":** acrescentar a unidade de cobrança (D, seção 8, DECISÃO DO OWNER, adiada para
   depois do piloto).
10. **"O que não virou pergunta", linha do perfil:** dizer que o caminho ao mapa fica para a fase 5 embora o mapa
    esteja na definição do projeto e em 68 das 79 buscas; ou trocar essa decisão de lugar com a pergunta 10.
11. **Pergunta 6:** alinhar o parêntese da pergunta ("em vez de vender o mesmo contato a várias") com a alternativa
    descrita na coluna ao lado (comparador com destaque pago); marcar "1 a 3" como premissa.
12. **Pergunta 10:** restringir a pergunta ao robô de treino da OpenAI, ou corrigir "troca-se uma linha… nada mais
    muda" para os demais robôs; citar na base o guia do ChatGPT, seção 9.
13. **Menores:** marcar "3 a 5" como premissa (pergunta 3) e dizer que, pelo desenho, sem conversa não há fase 2;
    na pergunta 7, citar os trechos de D que dizem aquilo (seção 8, fase 1, letra (b); 9.1; T12); na pergunta 1,
    "fase 1" em vez de "fase 0" e meia frase para o caso "conferi e não há impedimento"; uniformizar o sentido da
    coluna "Adotado por padrão" (estado de hoje × caminho previsto); atualizar a linha de estado com a alteração das
    22:20.
