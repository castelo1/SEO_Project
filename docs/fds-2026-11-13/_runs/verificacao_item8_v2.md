# Verificação independente do item 8 — perguntas ao owner (segunda versão)

- **Quando:** sexta, 13/11/2026, 22:43 (Brasília, lido de `TZ=America/Sao_Paulo date`). Leitura dos arquivos entre
  22:35 e 22:43; arquivo gravado às 22:45.
- **Quem:** verificador em contexto limpo; não recebeu a conclusão de quem produziu. Não é o mesmo leitor da primeira
  verificação (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item8.md`), que li inteira
  e não editei.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` — 48 linhas, gravado às 22:34:57, igual
  ao do commit `b5474b2`; não mudou durante a leitura (mesma soma de conferência às 22:35 e às 22:43).
- **Portão (transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 66):**
  "`docs/perguntas_owner.md`: no máximo dez, em ordem de quanto mudam o desenho, cada uma com a opção adotada por
  padrão. Uma delas é fixa: "você conferiu a política do seu empregador sobre atividade paralela?" (só a pergunta; não
  pesquise)"
- **Veredito: APROVADO COM RESSALVAS.** Uma pergunta com falha de conteúdo clara (a 8) e uma com falha leve (a 6);
  o limite da regra é duas. Há ainda um erro de fato na lista "O que não virou pergunta" (o roteiro do ChatGPT) e
  ressalvas em outras seis perguntas. Das 13 correções do primeiro verificador: 10 resolvidas, 3 resolvidas em parte,
  nenhuma ignorada. São 14 correções pedidas, no fim deste arquivo; nenhuma pede refazer o arquivo.
- **Natureza:** o que encosta em norma, aqui, é conferência do artefato contra o levantamento do projeto; não é
  parecer jurídico.
- **Aviso sobre o desenho:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` foi regravado às 22:38, durante
  esta leitura (eu o tinha lido na versão das 22:33). Comparei as duas versões com `git diff` (só leitura): mudaram
  quatro linhas (seção 3.4, "Celular primeiro"; seção 4.1, marca "Publicidade"; seção 5.1, passo 2; seção 5.2, segunda
  caixa do formulário). Nenhuma altera o que o artefato cita; a frase "o servidor registra o acesso com o endereço
  IP" continua lá.

## 1. O que foi lido

| Arquivo (caminho absoluto) | O que li |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` | inteiro (48 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item8.md` | inteiro (349 linhas; as 13 correções estão nas linhas 316–349) |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D") | inteiro (430 linhas), mais a diferença para a versão das 22:38 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` ("R") | linhas 1–60 (cabeçalho e quadro de vereditos) e 140–499 (seções (b), (c), (d), "O que as quatro restrições, juntas, deixam de pé", "O que não foi lido") |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` ("M") | linhas 1–96 (seções 1 e 2), 149–405 (4.0 a 4.4), 405–704 (4.5 a 8) |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` ("S") | seções 3, 4.1, 4.2, 8, 9, 10 e 11 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` ("B") | seção 10 (10.1 e 10.2) e "O que não cabe para um gerador de leads" (linhas 416–483) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | seção 2 (tabela dos robôs) e seção 9 (tabela e bloco do `robots.txt`) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md` | linhas 1–70 e seção 4 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | seções 2.1 e 2.2 (linhas 145–200), para a frase da página de entrada |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | só as linhas sobre robôs de treino (seção 1.2, linhas 103–109; seção 3, linhas 194–197) |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` | cabeçalho e contagem: 1.260 linhas, coluna `volume` = "não medido" em todas |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` e as quatro páginas | busca por botão, formulário, página de bairro, lista de pragas e endereço IP |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` | inteiro na versão das 22:23; "Fila do owner" relida na versão das 22:39 (as mesmas 5 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | inteiro (portão do item 8; "O que o projeto é") |

Também li, só em leitura (`git show`, `git diff`, `git log`), a primeira versão do artefato (commit `e0760ca`), para
comparar frase a frase. Não usei a web nem o navegador, não pesquisei nada sobre política de empregador, não rodei
`git` de escrita, não editei arquivo nenhum além deste.

## 2. Portão

| Exigência | Resultado | O que conferi |
|---|---|---|
| No máximo dez | **Cumpre** | Dez linhas, numeradas de 1 a 10 (linhas 22–31), cinco colunas em todas |
| Pergunta fixa, com essas palavras | **Cumpre** | Linha 22: "Você conferiu a política do seu empregador sobre atividade paralela?" — igual ao portão (só muda a maiúscula inicial) |
| Só a pergunta, sem pesquisa | **Cumpre** | A linha não traz conteúdo de política nenhuma nem nome de empregador; as colunas falam só em hipótese ("se a política vedar ou exigir autorização") e a base diz "Esta pergunta não foi pesquisada, por regra da rodada". Busca no arquivo por nome de empresa, salário, telefone, CNPJ e endereço de e-mail: nada |
| Cada uma com a opção adotada por padrão | **Cumpre** | As dez têm a coluna, agora começando por "Sim" ou "Não" entre aspas. O cabeçalho (linhas 11–12) define a coluna: "que resposta a sessão supõe enquanto você não responde". Ressalva nas perguntas 1 e 10: o "Não" é o estado de hoje, e o desenho prevê o contrário na fase 1 (seção 4 abaixo) |
| Pergunta fechada (sim ou não) | **Cumpre** | As dez admitem "sim" ou "não" |
| Uma pergunta só | **Não cumpre na 8; ressalva na 4** | **8** cola três escolhas: exclusividade (uma licenciada por região e por praga), unidade (mensalidade) e momento (paga antes); a coluna "se a outra" trata de duas alternativas diferentes (lead válido; várias pagando por destaque), sinal de que um "não" fica ambíguo. **4** ainda reúne quem conversa, com quantas, sobre o quê e quando, mas é um ato só e o "não" tem uma consequência só. As demais (2, 3, 5, 6, 7, 9, 10) são uma decisão cada |
| Em ordem de quanto mudam o desenho | **Cumpre, com ressalva** | A ordem declarada (linhas 8–9) é a que a tabela segue. A única posição discutível é a 6 acima da 7 e da 8 (seção 6 abaixo) |
| Nenhuma opção padrão publica, compra, cadastra, envia ou contata | **Cumpre, com ressalva de redação** | Nenhum padrão é ato da sessão e nada é executado. Mas os padrões das perguntas 4 ("é você quem conversa") e 6 (advogado) supõem atos futuros do owner — contatar empresas e pagar uma consulta. A frase da linha 12 ficaria exata se dissesse isso |

## 3. As 13 correções do primeiro verificador

| # | O que foi pedido | Situação | Linha atual e o que conferi |
|---|---|---|---|
| 1 | Pergunta 2: tirar "único formato que passa nas quatro restrições" | **Resolvida** | Linha 23: "É o formato que o levantamento deixa de pé: as peças dele estão marcadas 'permitido com condição' no quadro de vereditos…". Confere com R, linhas 30, 33–34, 38 e 468–477 |
| 2 | Antiga pergunta 4 (advogado): trocar "site de terceiro que nomeia a licenciada" pelo ponto que R deixa aberto (autuação de quem "concorreu"; razão social e endereço) e separar "não conclusivo" de "não levantado" | **Resolvida em parte** | Linha 27: o rótulo errado saiu; os quatro pontos "não conclusivos" e os três "não levantados" estão com o rótulo certo (seção 4, pergunta 6). **Falta** o ponto que a correção nomeava: se o dono do site pode ser autuado como quem "concorreu" ou "se beneficiou" (R, linhas 253–255; D, seção 9.1, linha da propaganda) |
| 3 | Letras da fase 1 na coluna "Base"; acrescentar D, seção 5.1 | **Resolvida** | Linha 25: "fase 1, letra b" (conversas); linha 27: "fase 1, letra c" (advogado) e "seção 5.1 (item 'Endereço IP')". Conferem com D, seção 8, na versão atual |
| 4 | Antiga pergunta 5: tirar "não guarda dado de ninguém"; ajustar "passa a tratar dado pessoal" | **Resolvida** | Linha 26: "o site registra o toque e não recebe nome, telefone nem conversa; o servidor registra o acesso com o endereço IP" e "passa a tratar dado de contato (nome e telefone)". Conferem com D, seção 5.1, passos 2 e 4 |
| 5 | Antiga pergunta 8: rebaixar a frase da página de entrada | **Resolvida** | Linha 28: "encosta no que a política de spam do Google descreve como página de entrada — leitura do guia, não frase do Google". Mesma força de S, seção 8 (linhas 348–351) |
| 6 | Antiga pergunta 8: deixar uma decisão só | **Resolvida** | Linha 28: a pergunta é só "sem página por bairro"; região, seis pragas e 19 a 29 páginas foram para a coluna do padrão, como premissas |
| 7 | Antiga pergunta 9: reduzir as três medições; trocar "ordem das páginas"; completar a base | **Resolvida, com defeito novo ao lado** | Linha 31: ficou só o Planejador; "premissa 3 do desenho"; base com D, seção 8 (fase 1, letra d), e S, seção 10. O roteiro e o Search Console foram para a lista (linhas 37–39) — solução aceitável, mas o motivo escrito ali está errado para o roteiro (seção 5 abaixo) |
| 8 | Ordem: subir "só parceiras" para a terceira posição e renumerar as remissões | **Resolvida** | "Só parceiras" é a linha 24 (pergunta 3). Remissões internas conferem: "pergunta 4" na linha 27; "perguntas 1 a 6" na linha 35; "pergunta 8" na linha 45. O advogado (6) ficou abaixo do botão (5), então a condição "se a 4 ficar acima da 5, escrever o critério" não se aplica mais; o cabeçalho ganhou o critério por grupos (linhas 8–9) |
| 9 | Lista: acrescentar a unidade de cobrança | **Resolvida em parte** (a linha entrou, mas em choque com a pergunta 8) | Linhas 44–45. O texto confere com D, seção 8. Só que a pergunta 8 pergunta justamente "com mensalidade paga antes?" (seção 4, pergunta 8) |
| 10 | Lista, linha do perfil: dizer do mapa, ou trocar de lugar com a antiga pergunta 10 | **Resolvida** (pela troca) | Linha 30: a gestão do perfil virou a pergunta 9; os robôs de treino foram para a lista (linhas 40–43). Troca aceitável: era a alternativa oferecida pelo primeiro verificador, e a decisão dos robôs, marcada DECISÃO DO OWNER em D, seção 3.4, continua visível, com o padrão |
| 11 | Antiga pergunta 6 (cobrança): alinhar o parêntese com a alternativa; marcar "1 a 3" como premissa | **Resolvida, com defeito novo** | Linha 29: o parêntese saiu; a coluna "se a outra" traz as alternativas; "de 1 a 3 licenciadas (premissa)". Defeito novo: "pagamento antecipado" virou "mensalidade paga antes" |
| 12 | Antiga pergunta 10 (robôs): restringir ao robô da OpenAI ou corrigir "uma linha"; citar o guia do ChatGPT | **Resolvida** | Linhas 40–43: "Bloquear o robô de treino da OpenAI troca uma linha…"; "outros robôs de treino teriam cada um a sua linha"; cita `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, seção 9, linha 4 da tabela, que diz aquilo. Ressalva menor na seção 5 |
| 13 | Menores (seis pedidos) | **Resolvida em parte** | "3 a 5" marcado como premissa (linha 25): feito. Trechos de D na base de "só parceiras" (linha 24): feito. "Fase 1" em vez de "fase 0" (linha 22): feito. Sentido da coluna do padrão (linhas 11–12): feito. Linha de estado (linhas 3–7): feita. **Faltam:** a meia frase para "conferi e não há impedimento" (linha 22) e dizer que, pelo desenho, sem conversa não há fase 2 (linha 25) |

Contagem: 10 resolvidas (1, 3, 4, 5, 6, 7, 8, 10, 11, 12 — a 7 e a 11 com defeito novo ao lado), 3 em parte (2, 9 e
13 — a 9 por contradizer a pergunta 8), nenhuma não resolvida.

## 4. Pergunta por pergunta

Legenda: **falha** = afirmação mais forte que a fonte, contrária a ela, ou remissão que não diz aquilo; **ressalva** =
imprecisão, omissão ou forma.

### Pergunta 1 — política do empregador (linha 22)

- **Padrão** ("Não": tratado como não conferido; projeto em estudo e protótipo local): confere com D, seção 8, fase 0,
  e com o estado do projeto.
- **Se a outra:** "não passa do passo (a) da fase 1, ou espera a autorização". Confere com D, seção 8, fase 1 ("não
  passa de fase se… empregador vedar"). A coluna só trata de "vedar ou exigir autorização"; falta o caso "conferi e
  não há impedimento" (cai a trava (a); nada mais muda). **Ressalva** — pendência da correção 13.
- **Base:** D, seção 8, fase 1, letra (a): existe e diz aquilo. D, seção 9.2, última linha: existe.
- **Sem pesquisa:** confirmado.
- **Resultado: sem falha.**

### Pergunta 2 — intermediário declarado (linha 23)

- **Padrão:** "Sim" é o que D adota (seção 1, item 1; seção 2) e o protótipo segue (faixa fixa; sem perfil).
- **"É o formato que o levantamento deixa de pé":** R, linhas 468–477. Confere, mesma força.
- **"as peças dele estão marcadas 'permitido com condição' no quadro de vereditos":** site de terceiro que nomeia a
  executora — R, linha 30; repasse com consentimento — linhas 33 e 34; botão que abre o WhatsApp da licenciada — linha
  38. As três conferem. "ele não usa perfil": D, seção 2.
- **Se a outra — "têm ao menos um ponto 'vedado' ou 'não conclusivo'":** perfil próprio, vedado (linha 25); site que
  não nomeia quem executa, não conclusivo (linha 31); central de WhatsApp, vedada pela API e não conclusiva pelo
  aplicativo (linhas 36–37). Confere, mesma força. **Ressalva:** a frase é verdadeira mas não distingue os formatos —
  o formato adotado também tem pontos não conclusivos (os quatro da pergunta 6). O que separa os alternativos é que a
  **peça central** deles é que está vedada ou não conclusiva.
- **Base:** R, linhas 21–38 e 468–477; D, seção 2; M, seção 5: existem e dizem aquilo.
- **Resultado: sem falha.**

### Pergunta 3 — só parceiras autorizadas (linha 24)

- **Padrão:** é o que D adota, por implicação em vários trechos: T3 ("preço informado por elas"), T12 ("como uma
  licenciada entra"), 4.1 ("área atendida, como a licenciada declarou"), fase 1, letra (b) ("aceitam ser nomeadas?"),
  9.1 ("se nenhuma licenciada aceitar ser nomeada"). O protótipo fala em "empresas indicadas" e "empresa parceira".
- **Se a outra:** "não foi levantado" confere (R não trata; D diz que o funcionamento da consulta pública não foi
  lido). "Iria ao advogado" é proposta do artefato, coerente. Os tipos de página citados (T3, T7, T12) mudam de fato;
  mudam também T4 (lista da região) e T9 (preços informados por elas), que a linha não cita. **Ressalva.**
- **Base:** D, 3.1, 4.1, seção 8 (fase 1, letra b) e 9.1: existem e dizem aquilo. S, seção 9, só sustenta de lado
  (item 7: lista de candidatas a parceira, "ninguém foi contatado"). **Ressalva.**
- **Resultado: sem falha.**

### Pergunta 4 — conversar com licenciadas antes de gastar (linha 25)

- **Padrão:** "Sim, e é você quem conversa" confere com D, seção 8 (fase 1, letra b; "contato com empresa é ação do
  owner", seção 7). "3 a 5; o número é premissa": D marca "número PREMISSA". Confere.
- **Se a outra:** "não há licenciada para nomear, e o desenho não tem página de oferta sem empresa nomeada" confere
  com D, 4.4. "O site sairia só com guias informativos, sem botão e sem receita" é cenário que D não desenha: pelo
  desenho, a fase 1 **não passa** se "nenhuma licenciada aceitar", e a fase 2 é feita "com 1 a 3 licenciadas
  nomeadas". Falta dizer isso. **Ressalva** — pendência da correção 13.
- **Base:** D, seção 8 (fase 1, letra b), 4.4 e 9.1 (linha da propaganda); M, seção 1, item 9: existem e dizem aquilo.
- **Resultado: sem falha.**

### Pergunta 5 — só o botão na primeira versão (linha 26)

- **Padrão:** "Sim" é o que D adota (seção 1, item 4; 5.1) e o protótipo mostra (botão como link; formulário só como
  exemplo desativado).
- **"o site registra o toque e não recebe nome, telefone nem conversa; o servidor registra o acesso com o endereço
  IP":** D, seção 5.1, passo 2 ("não recebe o seu nome, o seu número nem a conversa… o servidor registra o acesso com
  o endereço IP") e passo 4. Confere, mesma força. No protótipo, a frase do IP está na página de privacidade; o aviso
  ao lado do botão ainda não a traz (assunto do item 7, não deste).
- **Se a outra:** texto de consentimento, prova guardada, exclusão com aviso e canal de entrega conferem com D, 5.2,
  e R, linhas 346–356. "A fase 2 fica mais cara" não tem número (D diz que os valores não foram levantados);
  aceitável como leitura.
- **Base:** D, 5.1 e 5.2; R, seção (c), "Conclusão operacional" (linha 346), e seção (d), "Os dois desenhos" (linha
  432): existem e dizem aquilo.
- **Resultado: sem falha.**

### Pergunta 6 — advogado antes de publicar (linha 27)

- **Padrão:** "só depois de ao menos uma licenciada aceitar" confere com D, seção 8, fase 1, letra (c). A remissão
  "pergunta 4" está certa.
- **Pontos "não conclusivos", um a um:**
  - qual número de licença vale na capital — R, linhas 209–213: "não conclusivo". Confere.
  - razão social e endereço pedidos pela norma estadual — R, quadro, linha 32, e linhas 200–203: "não conclusivo".
    Confere; "pedidos pela norma" é um pouco mais firme que R, que só tem indício de cópia de terceiro, com vigência
    não confirmada.
  - prazo de guarda da prova — R, linhas 355 e 363. Confere.
  - controladores independentes ou conjuntos — R, linha 320; D, 5.2. Confere.
- **Pontos "não levantados", um a um:**
  - responsabilidade do intermediário por serviço mal feito — R, linhas 225–229 ("não levantada aqui"); D, 9.2.
    Confere. Observação: D não põe esse ponto na lista do advogado da fase 1; incluí-lo é escolha do artefato.
  - endereço IP no registro do servidor — D, 5.1 ("não foi levantado no item 2"). Confere.
  - se a página de preços conta como propaganda — D, 3.1, T9 ("não foi levantado"). Confere.
- **Omissão. FALHA leve.** A lista, que se lê como completa, deixa de fora o ponto que a correção 2 pedia: se o dono
  do site pode ser autuado como quem "concorreu" ou "se beneficiou" (R, linhas 253–255, "onde a norma é silente"). É
  o ponto que D, seção 9.1, põe entre o que tornaria o desenho inviável, com "advogado" na coluna "como se saberia".
- **Se a outra:** "risco aberto… a sessão não emite parecer" está certo. Falta dizer o que muda no desenho: sai o
  passo (c) da fase 1, com a despesa dele e a condição "parecer contrário". **Ressalva.**
- **Base:** D, seção 8 (fase 1, letra c), 5.1 (item "Endereço IP"), 3.1 (T9), 9.1 e 9.2; R, seções (b) e (c): existem
  e dizem aquilo.

### Pergunta 7 — sem página por bairro (linha 28)

- **Padrão:** zero página de bairro confere com D, 3.1 (T5), e com o protótipo ("não há uma página para cada
  bairro"). "Seis pragas" e "de 19 a 29 páginas" conferem com D, 3.1; a marca de premissa confere com D, seção 10,
  premissa 3.
- **"os três números são premissas":** o texto traz duas quantidades (seis pragas; 19 a 29 páginas). A terceira da
  premissa 3 ("até 5 regiões") não aparece. **Ressalva.**
- **Se a outra:** "só nas três condições da seção 3.3" confere. "Encosta no que a política de spam do Google
  descreve como página de entrada — leitura do guia, não frase do Google": mesma força de S, seção 8, e de D, 3.2
  ("classe A (texto da política) + INFERÊNCIA (aplicação)"). Confere. "Como os concorrentes": 50 de 67 sites (S,
  seção 8).
- **Base:** D, 3.1, 3.2 e 3.3; S, 4.2 e 8: existem e dizem aquilo.
- **Resultado: sem falha.**

### Pergunta 8 — modelo de cobrança (linha 29)

- **"com mensalidade paga antes": mais forte que a fonte. FALHA.**
  - D, seção 8, "Modelo de cobrança previsto para a fase 4": "uma licenciada por região e por praga, nomeada na
    página, com **pagamento antecipado**". M, seção 1, item 9, diz o mesmo. Nenhum dos dois escreve "mensalidade".
  - D, seção 8, "Unidade de cobrança": "mensalidade da região ou lead válido — **DECISÃO DO OWNER**, depois do
    piloto". A linha da fase 4 repete: "preço por contato válido ou mensalidade por região, de preferência pré-paga".
  - Com o padrão "Sim", a sessão passa a supor mensalidade, que o desenho não adota.
  - O próprio artefato se contradiz: as linhas 44–45 dizem que a unidade de cobrança **não** virou pergunta e fica
    para depois do piloto.
  - A primeira versão dizia "pagamento antecipado"; a troca entrou nesta.
- **Forma: três escolhas numa pergunta** (exclusividade, unidade, momento do pagamento). A coluna "se a outra"
  responde a duas alternativas distintas.
- **Demais afirmações:**
  - "como hipótese para depois do piloto": D, seção 8 (INFERÊNCIA). Confere.
  - "a página passa a ser publicidade dela e leva essa marca": D, seção 8; M, 4.3, riscos. Confere.
  - "de 1 a 3 licenciadas (premissa)" na fase gratuita: D, seção 8, fase 2. Confere.
  - "o 'R$ 20 a 60 por lead' da pesquisa antiga não se confirma nem se derruba": M, seção 7 ("não dá para confirmar
    — nem para derrubar"); D, seção 8. Confere, mesma força. "O preço não tem fonte": D ("o valor não tem fonte").
- **Se a outra:** "lead válido depende da contagem feita pela licenciada" confere com D, seção 6. "Várias empresas
  pagando por destaque": M, 4.5. "Muda… a definição de lead vendido": impreciso — a definição de D, seção 6, já cobre
  os dois casos ("por unidade, ou coberto pela mensalidade da região"). **Ressalva.** "O contato vai só à empresa que
  a pessoa escolher": D, 5.1; M, 4.5. Confere.
- **Base:** D, seção 8 e seção 6; M, 4.3, 4.5, 4.6 e 7: existem. M, 4.3 e 4.6, tratam a mensalidade como uma das
  formas possíveis, não como a escolhida.

### Pergunta 9 — o caminho até o bloco de mapa (linha 30)

- **Padrão:** "Sim" é o que D adota (seção 8, fase 5).
- **"o bloco apareceu em 68 das 79 buscas da amostra":** S, seção 3 (68; 86%). Confere.
- **"o perfil é da licenciada e ela pode levá-lo embora":** D, seção 8, último item ("são dela e ela pode levá-los
  embora"); B, linhas 482–483 ("é da licenciada e ela pode retomá-lo"). Confere, mesma força. **Ressalva de
  remissão:** em B a frase está no fecho de "O que não cabe para um gerador de leads", não na seção 10, que é a
  citada.
- **"O mapa está na definição do projeto":** verdadeiro
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, "O que o projeto é": "Ranqueamento por
  Google, IA e Google Maps"), mas a fonte não está na coluna "Base". **Ressalva.**
- **Se a outra:** "serviço já na fase 2 ou 3" e "entra um segundo trabalho antes de se saber se o primeiro funciona"
  são leitura do artefato: D não desenha a antecipação. "Pelo roteiro e pelos limites do guia de Maps" confere com B,
  10.1 e 10.2. Ficam de fora dois riscos que M, 4.4, registra para esse serviço: conflito de interesse com as
  concorrentes da licenciada gerida, e o papel do gestor perante a LGPD, não levantado. **Ressalva.**
- **Base:** D, seção 8 (item "Gestão do perfil da licenciada"); B, seção 10; S, seção 3; R, linha 28 ("permitido com
  condição"): existem e dizem aquilo, com a ressalva acima.
- **Resultado: sem falha.**

### Pergunta 10 — volume de busca no Planejador (linha 31)

- **Padrão:** "Não: não medido" confere com o arquivo (as 1.260 linhas com `volume` = "não medido") e com D, seção
  10, premissa 3.
- **Ressalva — o padrão é o estado de hoje, não o caminho do desenho.** D, seção 8, fase 1, letra (d), prevê que o
  owner meça o volume **antes** da fase 2. Lido como resposta ("não vou medir"), o padrão tira essa parte do passo
  (d), e a linha não diz. A coluna "se a outra" descreve só o "sim", que é o que o desenho já prevê.
- **Se a outra:** "a escolha de pragas e regiões (premissa 3 do desenho) pode ser revista": confere.
- **"com a sua conta":** S, seção 10, diz que o Planejador exige a conta do owner e que o funcionamento da ferramenta
  não foi conferido em fonte. Se a conta de anúncios não existir, criá-la é ato do owner; a linha não avisa.
  **Ressalva.**
- **Base:** D, seção 8 (fase 1, letra d) e seção 10, premissa 3; S, seção 10; o arquivo de termos: existem e dizem
  aquilo.
- **Resultado: sem falha.**

## 5. "O que não virou pergunta, e por quê"

| Item (linhas) | Conferência | Resultado |
|---|---|---|
| Nome do site e domínio (35–36) | D: nome de trabalho "EXEMPLO Guia"; comprar domínio e publicar são atos do owner (fase 2). "Depois das perguntas 1 a 6": as seis são de fato anteriores à fase 2 | Confere |
| Roteiro do ChatGPT e Search Console (37–39) | "São medições de fases posteriores": vale para o Search Console (fase 2). **Não vale para o roteiro:** D, seção 8, fase 1, letra (d), põe "owner roda o roteiro do ChatGPT" no mesmo passo do Planejador. "Só você pode rodar" e "sem linha de base" conferem. O caminho citado existe | **Falha leve** (motivo errado para o roteiro) |
| Robôs de treino (40–43) | Padrão "liberar": D, 3.4 (DECISÃO DO OWNER) e seção 10, premissa 8; `robots.txt` do protótipo (`GPTBot` com `Allow: /`). "Não muda a presença na busca do ChatGPT": guia do ChatGPT, seção 9, linha 4 da tabela ("liberar ou bloquear **não muda** a presença na busca", classe A), e seção 2. Mesma força. "Troca uma linha": confere com o guia (linha 513) e com o arquivo. "Outros robôs de treino teriam cada um a sua linha": hoje eles caem no bloco geral `User-agent: *`; cada um pediria um bloco novo, não uma linha. O guia de respostas de IA (seção 1.2) registra que bloquear `Google-Extended` pode tirar o site da fundamentação do aplicativo Gemini (inferência do guia); a linha não avisa | Confere, com ressalva |
| Unidade de cobrança (44–45) | D, seção 8: "DECISÃO DO OWNER, depois do piloto". O texto confere. "A pergunta 8 cobre a hipótese de partida": a hipótese de partida de D é "pagamento antecipado", sem unidade; a pergunta 8 pôs "mensalidade" | Confere em si; em choque com a linha 29 |
| PDFs, limite de buscas e "demais decisões operacionais" (46–48) | "Fila do owner" do painel: 5 linhas, todas com opção adotada. Duas são nomeadas (PDFs; limite de buscas); as outras três (histórico do repositório; duas escolhas do roteiro do ChatGPT) entram em "demais". Nenhuma muda o desenho | Confere |

## 6. Ordem

O cabeçalho (linhas 8–9) declara: primeiro as que derrubam o desenho inteiro (1 e 2), depois as que decidem se há
página de oferta (3 e 4), depois as que mudam uma parte (5 a 8), por fim as que só acrescentam (9 e 10). A tabela
segue essa ordem. O que muda se a resposta for a contrária, pelo que D diz:

| # | Se a resposta for a contrária | Tamanho da mudança |
|---|---|---|
| 1 | Se a política vedar: a fase 1 não passa (D, seção 8; 9.2) | Tudo |
| 2 | Cai o desenho inteiro: seções 1, 2, 4 e 5 partem do intermediário declarado (D, 9.3) | Tudo |
| 3 | Muda a dependência central: "nenhuma licenciada aceitar" deixa de ser trava da fase 1 e causa de inviabilidade (9.1); mudam T3, T4, T7, T9 e T12, o bloco "Quem executa" (sem preço informado nem área declarada), a contagem com a licenciada (seção 6) e as fases 1 e 2; entra um ponto não levantado | Seções 3, 4.1, 6, 8 e 9 |
| 4 | Pelo desenho, sem licenciada que aceite não há fase 2; sem conversa, a premissa "há licenciada disposta" fica sem teste e não há página de oferta (4.4) | Seção 8 e a premissa central |
| 5 | A versão 0 passa a ter a Via B: o site trata dado de contato, com prova, exclusão, canal de entrega e mais pontos para o advogado | Seção 5, T11, 9.1 (LGPD) |
| 6 | Nenhuma página muda; sai o passo (c) da fase 1, com a despesa e a saída "parecer contrário"; os pontos abertos viram risco assumido | Uma célula da seção 8 |
| 7 | T5 deixa de ser zero, só dentro das três condições de 3.3; mudam a contagem de páginas e a premissa 3 (em D, bairro é assunto da fase 5) | Seção 3, limitada por 3.3 |
| 8 | Muda o parágrafo do modelo de cobrança, a linha da fase 4, "lead vendido" e "receita por página" (seção 6) e o uso da marca "Publicidade" (4.1); tudo para depois do piloto | Seções 8, 6 e 4.1, só a partir da fase 4 |
| 9 | O item da fase 5 sobe para a fase 2 ou 3; o site não muda; entra um segundo serviço (M, 4.4) | Uma linha da seção 8; trabalho novo |
| 10 | O mapa de termos ganha volume; a premissa 3 pode ser revista | Dados; nada da estrutura |

**Ordem que eu defenderia: 1, 2, 3, 4, 5, 7, 8, 6, 9, 10.**

- **Nenhuma troca é obrigatória.** Não há pergunta que derrube o desenho abaixo de uma que só acrescente, e a troca
  que o primeiro verificador exigia (subir "só parceiras") foi feita.
- **A única posição discutível é a 6 acima da 7 e da 8.** Pelo critério declarado, a 6 é a que menos muda o desenho
  entre as quatro do grupo: a coluna "se a outra" dela não registra mudança nenhuma. Ela se sustenta onde está por
  outro motivo — o resultado da revisão pode parar o projeto ("parecer contrário", D, seção 8) e alcança os textos
  das seções 4 e 5. Se ficar, o cabeçalho deve dizer isso em meia frase.
- **3 antes de 4:** certo. A resposta contrária à 3 muda o sentido da 4 (se o site pudesse listar quem não autorizou,
  a conversa deixaria de ser condição para haver página de oferta).
- **9 antes de 10:** certo. Antecipar a gestão do perfil acrescenta um serviço inteiro; medir o volume acrescenta um
  dado.

## 7. Perguntas que faltam

Conferi em D as duas marcas "DECISÃO DO OWNER" (seções 3.4 e 8), as seis fases da seção 8, as tabelas 9.1 e 9.2, a
lista 9.3 e as 17 premissas da seção 10; as marcas de decisão do owner em M, B e no guia do ChatGPT; e as 5 linhas da
"Fila do owner" do painel.

| Decisão do owner | Onde está | Virou pergunta ou está na lista? | Avaliação |
|---|---|---|---|
| Robôs de treino | D, 3.4 (DECISÃO DO OWNER); premissa 8 | Lista, linhas 40–43 | Coberta. Impacto baixo: uma linha do arquivo |
| Unidade de cobrança | D, seção 8 (DECISÃO DO OWNER, "depois do piloto") | Lista, linhas 44–45 | Coberta — e, por engano, também dentro da pergunta 8 |
| Caminho até o mapa | D, seção 8, fase 5 e último item | Pergunta 9 | Coberta |
| Comprar domínio e publicar | D, seção 8, fase 2 | Lista, linhas 35–36 | Coberta |
| Aprovar ou recusar o desenho como um todo | D, seção 8, fase 0 | Não, de propósito | As dez perguntas decompõem a aprovação. Sem reparo |
| Medições com as contas do owner (roteiro; Search Console) | D, seção 6 e seção 8, fase 1, letra (d) | Lista, linhas 37–39 | Cobertas, com o motivo errado para o roteiro |
| Fila do owner do painel (5 linhas) | PAINEL | Lista, linhas 46–48 | Coberta |
| Em nome de quem o site responde (pessoa física ou jurídica) | D não marca como decisão nem como premissa; aparece em "quem somos" (seção 2), no texto do formulário ("razão social e CNPJ do responsável", 5.2), no regime de agente de pequeno porte (5.2) e, por consequência, na cobrança da fase 4 | **Não** | Lacuna do desenho mais do que do item 8, como o primeiro verificador já anotou. Não derruba nada, mas é pré-condição da fase 2 e toca a pergunta 1. Pede uma linha na lista. Não conto como falha |
| Criar conta numa plataforma de orçamentos para ver o preço de um pedido | M, seção 7 ("decisão do owner, fora da rodada") | **Não** | Impacto baixo no desenho; cabe na mesma lista |
| Grade ou rastreador de posição no mapa | B, 10.1, passo 15 ("se o owner decidir usar, é decisão dele") | Não | O guia não recomenda e D, seção 6, manda não medir assim. Não precisa entrar |

**Não achei decisão do owner de impacto alto que tenha ficado fora das perguntas e da lista.** Nenhuma das ausentes
muda o desenho mais do que a pergunta 10.

## 8. Afirmações de fato dentro das perguntas e das opções

| Afirmação | Onde | Fonte conferida | Resultado |
|---|---|---|---|
| "É o formato que o levantamento deixa de pé" | 2 | R, linhas 468–477 | Confere, mesma força |
| "as peças dele estão marcadas 'permitido com condição' no quadro de vereditos" | 2 | R, linhas 30, 33–34 e 38 | Confere, mesma força |
| "têm ao menos um ponto 'vedado' ou 'não conclusivo'" | 2 | R, linhas 25, 31 e 36–37; M, 5.1 a 5.3 | Confere; não distingue do formato adotado (ressalva) |
| uso do cadastro público "não foi levantado" | 3 | R (ausência); D, 3.1 (T8) e 4.1 | Confere |
| "3 a 5; o número é premissa" | 4 | D, seção 8, fase 1; seção 10, premissa 14 | Confere |
| "o desenho não tem página de oferta sem empresa nomeada" | 4 | D, 4.4 | Confere |
| "o site sairia só com guias informativos" | 4 | — | Cenário que D não desenha (ressalva) |
| "o site registra o toque e não recebe nome, telefone nem conversa" | 5 | D, 5.1, passos 2 e 4; R, linhas 440–441 | Confere, mesma força |
| "o servidor registra o acesso com o endereço IP" | 5 | D, 5.1, passo 2 e item "Endereço IP" | Confere, mesma força |
| "O texto está pronto no desenho" | 5 | D, 5.2 | Confere (texto de EXEMPLO, com colchetes) |
| quatro pontos "não conclusivos" | 6 | R, linhas 32, 200–203, 209–213, 320, 355 e 363 | Os quatro conferem |
| três pontos "não levantados" | 6 | R, linhas 225–229; D, 5.1 e 3.1 (T9) | Os três conferem |
| lista dos pontos abertos como um todo | 6 | R, linhas 253–255; D, 9.1 | **Incompleta:** falta a autuação de quem "concorreu" |
| "de 19 a 29 páginas"; "seis pragas" | 7 | D, 3.1; seção 10, premissa 3 | Conferem |
| "os três números são premissas" | 7 | D, seção 10, premissa 3 | O texto só traz dois (ressalva) |
| "encosta no que a política de spam do Google descreve como página de entrada — leitura do guia, não frase do Google" | 7 | S, seção 8; D, 3.2 e 3.3; guia orgânico, 2.2 | Confere, mesma força |
| "com mensalidade paga antes" | 8 | D, seção 8; M, seção 1, item 9 | **Mais forte que a fonte** ("pagamento antecipado"; unidade em aberto) |
| "o 'R$ 20 a 60 por lead' da pesquisa antiga não se confirma nem se derruba" | 8 | M, seção 7; D, seção 8 | Confere, mesma força |
| "de 1 a 3 licenciadas (premissa)" | 8 | D, seção 8, fase 2 | Confere |
| "o bloco apareceu em 68 das 79 buscas da amostra" | 9 | S, seção 3 | Confere |
| "o perfil é da licenciada e ela pode levá-lo embora" | 9 | D, seção 8; B, linhas 482–483 | Confere, mesma força (remissão a B na seção errada) |
| "O mapa está na definição do projeto" | 9 | RODADA, "O que o projeto é" | Confere (fonte fora da coluna "Base") |
| "volume: não medido" | 10 | arquivo de termos, coluna `volume` | Confere |
| "são medições de fases posteriores" | lista | D, seção 8, fase 1, letra (d) | **Não vale para o roteiro do ChatGPT** |
| "não muda a presença na busca do ChatGPT" | lista | guia do ChatGPT, seção 9, linha 4 da tabela; seção 2 | Confere, mesma força |

## 9. Forma

| Exigência | Resultado |
|---|---|
| Português | Cumpre |
| Caminhos absolutos | Cumpre: os doze caminhos escritos são absolutos; onze existem e o décimo segundo (`RESPOSTAS_OWNER.md`) é o arquivo a criar, que ainda não existe |
| Jurídico como levantamento | Cumpre: linha 18; pergunta 2 ("o levantamento deixa de pé"); pergunta 6 ("a sessão não emite parecer"); pergunta 3 ("não foi levantado e iria ao advogado") |
| Nenhum dado pessoal | Cumpre: sem nome de pessoa, de empregador, telefone ou salário |
| Número com fonte | Cumpre: 68 de 79 (S, seção 3); 19 a 29 e seis (D, 3.1, como premissa); 3 a 5 e 1 a 3 (D, como premissa); R$ 20 a 60 (M, seção 7) |
| Linha de estado | Bate: "segunda versão… às 22:34" confere com a hora de gravação (22:34:57) e com o commit; "aguarda nova verificação" era verdade até este arquivo |

## 10. Contagem e veredito

- **Falha de conteúdo clara (1):** pergunta 8.
- **Falha leve em pergunta (1):** pergunta 6 (lista de pontos abertos incompleta).
- **Falha leve fora das perguntas (1):** lista, linhas 37–39 (roteiro do ChatGPT).
- **Só ressalvas (6):** perguntas 1, 2, 4, 7, 9 e 10. A pergunta 3 tem ressalva de base. A pergunta 5 não tem reparo.
- **Portão:** cumpre o limite de dez, a pergunta fixa sem pesquisa, a opção padrão e a ordem; não cumpre "uma
  pergunta só" na 8.

**APROVADO COM RESSALVAS.** Duas perguntas com falha de conteúdo, dentro do limite de duas. A que importa é a 8: se o
owner não responder, a sessão passa a supor uma unidade de cobrança que o desenho deixou para ele decidir depois do
piloto. As linhas alteradas pedem nova conferência depois das correções.

### Correções pedidas

1. **Pergunta 8 (linha 29):** trocar "com mensalidade paga antes" por "com pagamento antecipado" (D, seção 8; M,
   seção 1, item 9) e deixar a pergunta com uma decisão só — uma licenciada por região e por praga, ou várias. Tirar
   "cobrar por lead válido" da coluna "se a outra", porque a unidade de cobrança está fora das perguntas (linhas
   44–45).
2. **Lista, linhas 37–39:** o roteiro do ChatGPT é do passo (d) da fase 1 de D, o mesmo do Planejador; só o Search
   Console é de fase posterior. Trocar o motivo (por exemplo: "são linha de base, não mudam o desenho").
3. **Pergunta 6 (linha 27), lista:** acrescentar o ponto em que a norma é silente — se o dono do site pode ser
   autuado como quem "concorreu" ou "se beneficiou" (R, linhas 253–255; D, seção 9.1). É o que falta da correção 2 do
   primeiro verificador.
4. **Pergunta 6 (linha 27), coluna "se a outra":** dizer o que muda no desenho — sai o passo (c) da fase 1, com a
   despesa e a saída "parecer contrário".
5. **Pergunta 1 (linha 22):** meia frase para "conferi e não há impedimento" (cai a trava (a) da fase 1; nada mais
   muda).
6. **Pergunta 4 (linha 25):** dizer que, pelo desenho, sem licenciada que aceite a fase 1 não passa e não há fase 2;
   marcar "site só com guias" como leitura da sessão.
7. **Pergunta 10 (linha 31):** dizer que o "Não" é o estado de hoje e que D, seção 8, fase 1, letra (d), prevê a
   medição antes da fase 2; avisar que o Planejador pede conta de anúncios, que só o owner cria.
8. **Pergunta 7 (linha 28):** "os três números" — o texto traz dois; ou acrescentar "até 5 regiões", ou escrever "os
   números".
9. **Pergunta 9 (linha 30):** na base, apontar B, "O que não cabe para um gerador de leads" (fecho), para a frase do
   perfil, e a RODADA para "o mapa está na definição do projeto"; marcar "fase 2 ou 3" como leitura da sessão e citar
   M, 4.4 (riscos).
10. **Pergunta 2 (linha 23):** trocar "têm ao menos um ponto 'vedado' ou 'não conclusivo'" por "têm a peça central
    'vedada' ou 'não conclusiva'", porque o formato adotado também tem pontos não conclusivos.
11. **Cabeçalho, linhas 8–9:** se a pergunta 6 ficar acima da 7 e da 8, meia frase com o motivo (o resultado da
    revisão pode parar o projeto); ou descê-la para depois da 8.
12. **Cabeçalho, linha 12:** precisar a frase — nenhuma opção padrão é ato da sessão; as das perguntas 4 e 6 supõem
    atos futuros do owner (conversar com empresas; contratar advogado).
13. **Lista, linhas 40–43:** "cada um a sua linha" → cada um pede um bloco novo no arquivo; registrar a ressalva do
    guia de respostas de IA (seção 1.2) sobre `Google-Extended`.
14. **Lista e pergunta 3 (linha 24):** acrescentar à lista "em nome de quem o site responde (pessoa física ou
    jurídica)" e "criar conta em plataforma de orçamentos" (M, seção 7); na pergunta 3, somar T4 e T9 aos tipos de
    página que mudam.
