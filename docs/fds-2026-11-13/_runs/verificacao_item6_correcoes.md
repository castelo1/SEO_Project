# Conferência das 21 correções do item 6 — `docs/desenho_v0.md`

- **Quando:** sexta, 13/11/2026 (Brasília, lido de `TZ=America/Sao_Paulo date`): início da leitura
  "Fri Nov 13 22:22:24 -03 2026"; leitura imediatamente antes de gravar este arquivo "Fri Nov 13 22:28:44 -03 2026".
- **Quem:** segundo leitor independente, em contexto limpo. Só leitura de arquivo local e `git` de leitura (`log`,
  `diff`, `status`). Nenhuma página da web, nenhum navegador, nenhum `git` de escrita, nenhuma memória corporativa.
  Nada editado além deste arquivo.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, 419 linhas, lido inteiro; alterado pela
  última vez às 22:19:05; `sha256` começa por `1e1250376138bfab` (igual no começo e no fim desta leitura). É o estado do
  commit `e0760ca` (22:20:21). **Os números de linha abaixo são desta versão.**
- **Pedido conferido:** `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item6.md`, lido
  inteiro (seções 3.2, 4, 5 e 8 em detalhe). Usei também `git diff e0a971b e0760ca -- docs/desenho_v0.md` para ver o
  que saiu e o que entrou.
- **Arquivos abertos para conferir os ponteiros:**
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` [R] (inteiro, 499 linhas);
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` [S] (inteiro, 418 linhas);
  `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` [M] (versão de 792 linhas: linhas 1–100, 149–483,
  528–540, 588–706);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` [A] (linhas 140–249 e 354–399);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` [G] (linhas 465–528 e as linhas de F13 e F25 na
  tabela de fontes);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` [C] (linhas 336–367);
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linhas 30–95);
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes_item5.md` (inteiro);
  `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` (inteiro);
  `/home/ancastelo/pessoal/SEO_Project/prototipo/` (só `robots.txt` e uma busca por frases; ver seção 5).

## Veredito

**APROVADO COM RESSALVAS.**

- **19 das 21 correções resolvidas; 2 resolvidas em parte (16 e 18); nenhuma não resolvida.**
- Os pontos da seção 4 do primeiro verificador foram todos tratados (seção 2 abaixo), com um resíduo de forma.
- **Ponteiros novos ou alterados: 41 conferidos, 39 batem, 1 não sustenta o que se cita, 1 bate com ressalva**
  (seção 3).
- O portão continua coberto parte por parte. O desenho **não depende** de perfil fora da regra, endereço fictício,
  avaliação fabricada, link comprado nem consulta automática ao Google, e nada marcado "vedado" em [R] (linhas 21–38)
  virou escolha (seção 6).
- As ressalvas são 10 itens (lista no fim): **um de conteúdo** (o aviso ao consumidor e a premissa "não ligar o IP ao
  toque" não fecham com o registro de acesso bruto que o próprio desenho exige) e nove menores. Nenhum toca o portão.

## 1. As 21 correções, uma a uma

| # | Pedido (resumo) | Situação | Linha atual | Texto curto ou o que falta |
|---|---|---|---|---|
| 1 | Tirar "(como no item 4)" ou dizer a verdade sobre a coleta; definir "manual"; dizer quem faz | **Resolvida** | 296 | "uma pessoa digita a busca no navegador, sem script"; "A coleta do item 4 **não** serve de modelo: foi feita por script, em lotes; o próprio mapa a classifica como consulta automática… verificação de robô na 80ª busca"; quem: "o owner"; ponteiros [A] seção 8 e [S] 2.2, 2.3 (item 9) e 2.4 |
| 2 | Citar os dois lados do dado da licença (12 de 67 × 47% das primeiras posições) em três lugares | **Resolvida** | 35–41; 99; 388–390 | "Só 12 desses 67… mas os 11 domínios que o mostram ocupam 37 das 79 primeiras posições (47%) e 30% dos três primeiros… **não é raro no topo**… não prova que exibir a licença melhore a posição"; premissa 1: "corta para os dois lados" |
| 3 | "Primeira despesa só depois de uma licenciada aceitar" × ordem da fase 1 | **Resolvida** | 53–54; 336 | Fase 1: (a) política do empregador; (b) conversa com licenciadas; (c) "**só se ao menos uma aceitar**, advogado…"; despesa: "consulta jurídica, só no passo (c)" |
| 4 | Dizer em que fase o botão entra | **Resolvida** | 45; 78; 181; 337; 338 | Fase 2: "já com o botão da Via A e o registro de cliques"; fase 3: "O botão e o registro de cliques já estão no ar desde a fase 2; aqui entra a contagem mensal" |
| 5 | Uniformizar o número de páginas e mostrar a conta | **Resolvida** | 89–91; 337; 392 | "de 19 a 29 páginas — 16 fixas (T1, 1; T2, 6; T6, 2; T8, 1; T9, 1; T10, 2; T11, 2; T12, 1) mais T3 (1 a 5), T4 (1 a 5) e T7 (1 a 3)". Conta refeita: 1+6+2+1+1+2+2+1 = 16; 16+1+1+1 = 19; 16+5+5+3 = 29. Fecha com a tabela 3.1, com a fase 2 e com a premissa 3 |
| 6 | "Nenhum dado da pessoa" → "nenhum dado de contato"; IP como não levantado; pôr em T11 e na lista do advogado | **Resolvida** no que foi pedido | 188; 193–196; 209–213; 336; 365 | "**Nenhum dado de contato da pessoa** (nome, telefone, conversa)"; "O que o site pode ter é o endereço IP no registro de acesso do servidor"; "não foi levantado no item 2… entra na política de privacidade (T11) e na lista do advogado da fase 1". **Sobra do mesmo defeito, em linha que o primeiro verificador não listou: item 1 da lista final (linha 186)** |
| 7 | Marcar o registro do clique por redirecionamento; dizer como robôs e cliques repetidos ficam fora | **Resolvida** | 201–208; 299; 347–348 | "(PREMISSA)… o passo intermediário é escolha deste desenho"; "`Disallow: /ir/`… `rel="nofollow"`… acessos com identificação de robô conhecido são descartados. **Toques repetidos da mesma pessoa não dá para distinguir**… o clique é indicador, e a unidade de cobrança fica para depois do piloto" |
| 8 | Canal de entrega do pedido da Via B; obrigações do agente de pequeno porte; controladores | **Resolvida** | 264–271 | "por e-mail… ou por uma página restrita do próprio site… **nunca** por WhatsApp do site… **PREMISSA**, a rever com o advogado"; "canal de comunicação com o titular, registro simplificado das operações e segurança básica (Resolução CD/ANPD nº 2/2022, arts. 9º, 11 e 13) [R… 338–341]"; "controladores independentes ou conjuntos é **não conclusivo** [R, linha 320]" |
| 9 | Completar a lista única de premissas | **Resolvida** | 386–412 | Entraram os itens 11 ("quem somos"), 12 (texto visível e sem script, ChatGPT), 13 (ritmo), 14 (3 a 5; 1 a 3) e, no item 4, "três empresas por página". Conferência cruzada na seção 4.6 abaixo: nenhuma PREMISSA do corpo fora da lista. O item 12 tem um erro de data (item 4 da lista final) |
| 10 | Marcar "caso mais simples" como INFERÊNCIA; trazer a consequência de [M] 4.3 | **Resolvida** | 342–346 | "é **INFERÊNCIA**: o próprio [M] (seção 1, item 9) diz 'leitura minha, não fato'"; "com uma só licenciada pagante, a página é, na prática, publicidade dela — leva a marca 'Publicidade' da seção 4.1 e não pode se apresentar como comparação isenta" |
| 11 | Trocar o ponteiro [B, seção 6] do campo "Área atendida" | **Resolvida** | 149 | "escolha deste desenho: a página só oferece o serviço onde a licenciada nomeada declara atender [R, linhas 257–258]", marca PREMISSA; também na premissa 17 |
| 12 | Corrigir "não levantado no item 2 nem no item 5" (telefone do site) | **Resolvida** | 288 | "Num site próprio, o número pode ser do intermediário; no perfil da parceira, não [R, linhas 155–157; M, seção 4.2, riscos, linha 'Parceiro']. A **gravação da chamada não foi levantada**. Fica fora da versão 0 por escolha (**PREMISSA**)" |
| 13 | Definir lead vendido separado de lead válido, orçamento e serviço fechado; amostra × contagem mensal | **Resolvida** | 299–304; 197–200 | Cinco linhas separadas: Lead (Via A), Lead (Via B), Lead válido, Lead vendido ("lead válido **pago** pela licenciada… Só existe a partir da fase 4"), Orçamento e serviço fechado. "Contagem mensal… de **todos** os contatos com código (não por amostra)". Ver item 8 da lista final (unidade "clique") |
| 14 | "Pode estar desatualizada" nas fontes de 2025 e de 2024 | **Resolvida** | 120; 125 | "(fontes de 2025, que **podem estar desatualizadas**)"; "(ChatGPT: uma fonte B de 2024, que **pode estar desatualizada**)" |
| 15 | "Sem risco para crianças e animais" é exemplo, não texto da norma | **Resolvida** | 164 | "(palavras da norma) e qualquer sugestão de ausência de efeito adverso — por exemplo, 'sem risco para crianças e animais' (exemplo meu, não texto da norma)" |
| 16 | Marcas fora da legenda: pôr na legenda ou converter; INFERÊNCIA na 3.3 | **Em parte** | 20–25; 62; 98–101; 106–107; 147; 325; **132** | Legenda ampliada (OBSERVAÇÃO DA AMOSTRA, REGRA DA RODADA, "por prudência" dentro de PREMISSA, INFERÊNCIA "minha ou do guia citado"); 3.3 marcada. **Falta:** a linha 132 ainda traz "requisito de medição" na coluna Marca, fora da legenda (agora depois de "classe A (o que cada robô é)") |
| 17 | Cinco ajustes de ponteiro | **Resolvida** | 36; 66; 101; 123; 363 | [S, seção 8] para "50 dos 67"; "'não pedir' é PREMISSA, mais estrita que a regra"; "'página interna de serviço ou outra'"; "[A]… seção 2.1, linha 163"; "(68 e 60 das 79 buscas [S, seção 3])" |
| 18 | Ponteiro ou marca em T8, T9 e T12; T9 nomeia (leva o bloco) ou é conteúdo sem botão; T12 sem link de volta | **Em parte** | 83; 84; 87; 139 | T8: [S, seção 4.4] e PREMISSA 10. T12: "**não se exige link de volta** para o site [A, seção 2.1, linhas 165 e 167]". T9: "cada linha traz o nome e o número da licença de quem informou e leva à ficha dela (T7)… T9 não tem botão". **Falta:** T9 ficou no meio das duas saídas pedidas — nomeia a empresa e publica o preço dela, mas a linha não traz o órgão emissor e T9 não está na lista do bloco "Quem executa" (linha 139); e o ponteiro novo de T12, [M, seção 4.0], não trata de como a licenciada é cobrada (itens 2 e 5 da lista final) |
| 19 | "Não tem licença" na faixa fixa; dizer onde ela fica | **Resolvida** | 154–156 | "Não é dedetizadora, não tem licença e não executa o serviço… Fica no alto de toda página, logo abaixo do cabeçalho e antes do título." Ver item 9 da lista final (as linhas 61 e 227 não acompanharam) |
| 20 | Linha 2 da tabela de [G] seção 9 | **Resolvida** | 128 | "Hospedagem, CDN e firewall — Sem bloqueio aos endereços IP publicados da OpenAI; conferir depois de ligar qualquer 'proteção contra robôs' — [G], seção 9, linha 2 — classe A" |
| 21 | Caminho absoluto de `RODADA.md` e do protótipo | **Resolvida** | 208; 309; 339; 378 | `/home/ancastelo/pessoal/SEO_Project/prototipo/`; `…/docs/fds-2026-11-13/RODADA.md` (duas vezes); para a pergunta fixa, `…/docs/perguntas_owner.md`, pergunta 1 (existe, linha 16 desse arquivo). A "fila de reserva 4" da linha 271 vem sem caminho, mas ele está na linha 339 |

## 2. Pontos da seção 4 do primeiro verificador

| Ponto | Tratado? | Linha atual |
|---|---|---|
| Dado contrário omitido (47% das primeiras posições) | Sim | 35–41; 99; 388–390 |
| Premissas do corpo fora da lista (antigas 58, 108, 113, 290) | Sim | lista, itens 11, 12 e 13 (403–406) |
| "Caso mais simples" sem marca | Sim, INFERÊNCIA | 343–344 |
| Seção 3.3 sem marca | Sim, INFERÊNCIA | 106–107 |
| Registro do clique por redirecionamento sem marca | Sim, PREMISSA | 201–202; lista, item 15 |
| "Não pede" avaliação | Sim, PREMISSA | 66; lista, item 17 |
| "3 a 5 licenciadas" | Sim, "número PREMISSA" | 336; lista, item 14 |
| "1 a 3 licenciadas" | Sim, "número PREMISSA" | 337; lista, item 14 |
| "Duas ou três licenciadas" por página | Sim, "no máximo três por página: **PREMISSA**" | 191–192; lista, item 4 |
| "68 e 60 das 79" sem ponteiro | Sim, [S, seção 3] | 363 (e 354) |
| T8, T9, T12 sem ponteiro | Sim (T9 e T12 com as ressalvas da correção 18) | 83; 84; 87 |
| Código na mensagem sem ponteiro | Sim: "escolha deste desenho, sem trecho no item 2 (**PREMISSA**)" | 197–198; lista, item 5 |
| Marcas fora da legenda: "escolha de desenho", "por prudência", "observação da amostra", "regra do projeto" | Sim | 62; 147; 98–101; 325 |
| Marca fora da legenda: "requisito de medição" | **Não** (continua, ao lado de "classe A") | 132 |

Da seção 7 do primeiro verificador ("os números de [S] não trazem a data nem o limite"): a legenda agora diz "79
buscas num só dia, de uma conta logada e de um ponto de acesso; não é censo" (linhas 23–24). Tratado.

## 3. Ponteiros novos ou alterados

Abri cada um. "✓" = o trecho existe e diz aquilo.

| Linha do desenho | Ponteiro | O que o arquivo citado diz | Resultado |
|---|---|---|---|
| 35–36 | [S, seção 8] — "50 dos 67" | [S] linha 334: "50 dos 67 sites de serviço lidos têm páginas por localidade" | ✓ (a primeira metade da frase, "o orgânico é quase todo de sites de dedetizadoras", está em [S] 7.3, item 1, linhas 296–297, que não é citada: item 10 da lista final) |
| 36–37 | [S, seção 7.3, item 4] — "12 desses 67" | [S] linha 317: "Dos 67 sites de serviço lidos, 12 mostram número de licença" | ✓ |
| 37–38 | [S, seções 7.2 e 7.3, item 5] — "11 domínios", "37 das 79 (47%)", "30% dos três primeiros" | [S] linha 284: 11 domínios; 70 (30%) entre os três primeiros; 37 (47%) na 1ª posição. Linhas 323–325: "47% das primeiras posições (37 de 79)… não prova de que exibir a licença melhore a posição" | ✓ |
| 83; 148 | [S, seção 4.4] — consulta pública apareceu numa busca | [S] linhas 223–224 | ✓ |
| 84 | [R, linhas 243–244] — afirmação de preço pede prova guardada | "Só com prova guardada (CDC, art. 36, parágrafo único, e art. 38)… 'melhor preço'… quem as publica tem de poder prová-las" | ✓ |
| 87 | [A, seção 2.1, linhas 165 e 167] — não exigir link de volta | Linha 165: "exigir link de volta de cada parceira é troca"; linha 167: "Não exigir, no contrato com a licenciada, link para o site" | ✓ |
| 87 | [M, seção 4.0] — "como é cobrada" | A 4.0 (linhas 151–188) trata das duas vias de captação, dos riscos comuns e de como as plataformas devolvem lead inválido. Como a licenciada é cobrada está em 4.2 (linhas 243–251), 4.3 (linha 329) e 4.6 (linhas 448–458) | **Não sustenta** (baixa) |
| 91 | [A, seção 2.2, "dois limites honestos"] | Linhas 196–198: "não sei quantas páginas por bairro um site novo sustenta… não há número em fonte A nem B" | ✓ ([A] fala de páginas por bairro; o desenho generaliza para páginas) |
| 98 | [S, seções 4.2 e 8] — 79% a 87%; texto de molde | [S] linhas 181–182 (87 e 79), 334 e 335 | ✓ |
| 99 | [R, linhas 186–187]; [S, seção 7.3, itens 4 e 5] | Art. 22, caput; números acima | ✓ |
| 101 | [S, seção 4.2, grupo F] — 68% e 1%; "páginas de segmento" | [S] linha 183 (1 e 68); linhas 197–199: "pede página de segmento" | ✓ |
| 109; 149 | [R, linhas 257–258] | "Um desenho em que **toda** página de oferta nomeia a licenciada que atende aquela região cumpre as condições" | ✓ |
| 120 | [C], seção 7.1; [G], seção 9, linha 7 | [C] linha 343: "as duas fontes são de 2025: **podem estar desatualizadas**"; [G] linha 477: texto visível, "uma B", hipótese para o ChatGPT | ✓ |
| 123 | [A], seção 2.1, linha 163 | "Blocks of text that list cities and regions…"; "Não pôr rodapé com a lista dos 96 distritos" | ✓ |
| 125 | [G], seção 9, linha 5 | Linha 475: "B de 2024, **pode estar desatualizada**" | ✓ |
| 128 | [G], seção 9, linha 2 | Linha 472: "Hospedagem, CDN e firewall sem bloqueio aos IPs publicados da OpenAI; conferir depois de qualquer 'proteção contra robôs'", classe A, regra | ✓ |
| 133; 212 | [R, "O que não foi lido e por quê", linhas 488–493] | Título na 488; linhas 490–492: "guias da ANPD de legítimo interesse, de agentes de tratamento e de cookies… a ferramenta de leitura não extrai texto de PDF" | ✓ |
| 154–156 | [R, linhas 246–251] — "não tem licença" | Linha 248: "O site não é dedetizadora, não tem licença e não executa" | ✓ |
| 164 | [R, linhas 193–194 e 241–242] | Linha 242: "'sem risco para crianças e animais' é exemplo meu… não texto da norma" | ✓ |
| 202 | [R, linha 438] | "Desenho B — o botão do site abre direto o WhatsApp da licenciada" | ✓ |
| 261–262 | [R, linha 368]; [M, seção 6] — "até 4 ou 6 prestadores" | [R] 368: "A lei não fixa número máximo de empresas". [M] linhas 594–596: GetNinjas "Até 4 (a mesma página diz 3 em outra seção…)"; oHub "4, mais 2 com acréscimo (R4, artigo de 2021, **pode estar desatualizada**)"; Cronoshare "No máximo 4" | ✓ **com ressalva**: o "6" ganhou em [M], às 22:17, a marca "pode estar desatualizada", que o desenho não traz (item 6 da lista final) |
| 266 | [M], seção 4.2 — deixa o canal para este desenho | [M] linhas 247–248: "(por e-mail ou painel — o canal é escolha do item 6)" | ✓ |
| 268–270 | [R, seção (c), "Agente pequeno e dado sensível", linhas 338–341] | Canal (art. 11), registro simplificado (art. 9º), segurança básica (art. 13); marcado [S] em [R] (leitura só do subagente) | ✓ |
| 270–271 | [R, linha 320] | "Se são controladores independentes ou conjuntos: **não conclusivo**" | ✓ |
| 288 | [R, linhas 155–157]; [M, seção 4.2, riscos, linha "Parceiro"] | [R]: "o controle do número pelo intermediário só vale no **site**"; [M] linha 314: "só vale **no site**, nunca no perfil da parceira; gravação de chamada **não foi levantada**" | ✓ |
| 296 | [A], seção 8; [S], seções 2.2, 2.3 (item 9) e 2.4 | [A] linha 367 (consultas automáticas vedadas); [S] linhas 83–89 (script `coletor.js`, lotes), 109–112 ("Consulta automática… a decisão de manter isso está na fila do owner"), 116–118 ("Na 80ª busca válida… 'tráfego incomum'") | ✓ |
| 299 | [R], linhas 440–441 | "o site só registra o clique, não o telefone nem a conversa" | ✓ |
| 301 | [M], seção 4.0.1 | Linhas 173–188: regra escrita de lead inválido, plataforma a plataforma | ✓ |
| 302; 304 | [M], seções 4.2 e 4.6 | 4.2, linha 250: "A licenciada paga por unidade entregue"; 4.6, linhas 448–458: mensalidade ou crédito pré-pago. A mensalidade "da região" é da 4.3 (linha 329) | ✓ |
| 303; 338 | [M], seção 7 — taxa de fechamento sem fonte brasileira | Linha 628: "Nenhuma fonte brasileira"; linha 644 | ✓ |
| 309; 339 | `RODADA.md`, fila de reserva 5 e 4 | Linhas 74–76 | ✓ |
| 343–344 | [M] (seção 1, item 9) — "leitura minha, não fato" | [M] linhas 58–61: "**Leitura minha, não fato:** o modelo mais simples perante as quatro restrições é **uma licenciada por região, nomeada na página, com pagamento antecipado**" | ✓ ("e por praga" vem da 4.3, linha 327) |
| 345–346 | [M], seção 4.3, riscos, linha "Propaganda" | Linha 355: "A página vira, na prática, publicidade de uma empresa: tem de ser identificável como tal (CDC, art. 36) e não pode parecer comparação isenta" | ✓ |
| 348 | [M, seção 4.2] — o clique é o que o site prova | Linhas 245–246: "O que se cobra é o **clique**, porque é só isso que o site consegue provar" | ✓ |
| 349–350 | [M, seção 7] — R$ 20 a 60 | Linha 633: "**Veredito: não dá para confirmar — nem para derrubar.**" | ✓ |
| 354; 363 | [S, seção 3] — 68 e 60 das 79 | [S] linha 140 | ✓ |
| 378 | `…/docs/perguntas_owner.md`, pergunta 1 | Linha 16 desse arquivo: a pergunta fixa do empregador | ✓ |
| 388–390 | [S, seção 7.3, itens 4 e 5] | Como acima | ✓ |
| 208 | `/home/ancastelo/pessoal/SEO_Project/prototipo/` — "o botão é um link de EXEMPLO que não leva a lugar nenhum" | A pasta existe; em `prototipo/zona-oeste/baratas/index.html`, linhas 83 e 101, o botão é `href="#botao-de-exemplo"` | ✓ |
| 5 | `…/_runs/verificacao_item6.md` — "aprovado com ressalvas; 1 falha em 12 no sorteio; 21 correções pedidas" | Linhas 23, 26 e 29 desse arquivo | ✓ |
| 417 | [M] "verificado em 13/11 (aprovado com ressalvas…)" | [M] linhas 5–9: "aprovado com ressalvas; 11 de 12 no sorteio… As correções ainda não foram reverificadas" | ✓ o veredito; ver item 6 da lista final |

**[M] depois da correção das 22:17 (762 → 792 linhas).** As seções que o desenho cita continuam dizendo o que ele
atribui: seção 1, item 9 (linhas 58–61); 4.0 (151–171); 4.0.1 (173–188); 4.2 (236–314, linha "Parceiro" na 314); 4.3
(318–358, linha "Propaganda" na 355, linha "Parceiro" na 358: "se ela sai, a região fica sem receita e sem empresa para
nomear"); 4.6 (448–474); 6 (590–601); 7 (605–648); 8 (652–703, "Não sei" 2 e 3). O desenho não cita [M] por número de
linha. A única diferença de conteúdo que alcança o desenho é a marca nova do "6" do oHub (acima).

**Ponteiros que não mudaram:** não reabri os de [B] (seções 3.1, 7, 9, 10, 10.2 e o fecho) nem os de [C] 1.1, 1.2,
1.3, 3, 7.2, 7.3 e de [A] seções 3, 4, 5, 7 e 9 além do que está listado em "Arquivos abertos". O primeiro verificador
conferiu os 132; o ponteiro [B, seção 6], que tinha falhado, saiu do desenho.

## 4. Contradições internas — o que procurei e o que achei

### 4.1 Número de páginas — fecha
Linhas 89–91 contra a tabela 3.1 (76–87), a fase 2 (337) e a premissa 3 (392): 16 fixas + T3 (1 a 5) + T4 (1 a 5) +
T7 (1 a 3) = 19 a 29. T5 é 0 na versão 0. `docs/perguntas_owner.md`, pergunta 8, diz o mesmo.

### 4.2 Em que fase o botão entra — fecha
Seção 1, item 4 (45–47): "na versão 0, só o botão". Tabela 3.1, T3 (78): página com botão. Seção 5.1 (181): "(versão
0)". Fase 2 (337): site no ar "já com o botão da Via A e o registro de cliques". Fase 3 (338): só a contagem mensal.
Formulário: "fase posterior" (46, 215) = fase 5 (340). As quatro seções dizem a mesma coisa. Observação: "versão 0" (o
primeiro site, que vai ao ar na fase 2) e "fase 0" (estudo e protótipo, linha 335) são coisas diferentes com nomes
parecidos; não é contradição, mas pode confundir o owner.

### 4.3 Ordem da fase 1 contra "a primeira despesa só vem depois…" — fecha
Linha 336: a única despesa da fase é a consulta jurídica, "só no passo (c)", e o passo (c) começa por "só se ao menos
uma aceitar". Coerente com as linhas 53–54. **Efeito colateral fora do desenho:** ver seção 5 (as letras citadas em
`docs/perguntas_owner.md` ficaram trocadas).

### 4.4 Lead, lead válido, lead vendido — fecha, com uma ponta solta
Seção 6 (299–304) contra 5.1 (197–208) e seção 8 (338–339, 347–350): lead = toque no botão, sem robôs conhecidos;
lead válido = contato que a licenciada confirma ter recebido com o código; lead vendido = lead válido pago, só a partir
da fase 4; fase 3 mede "leads válidos, orçamentos, serviços fechados". Coerente.
**Ponta solta (nova):** a linha 347 deixa em aberto cobrar por "mensalidade da região, **clique** ou lead válido"; a
linha 302 define lead vendido só como "lead válido pago… por unidade, ou coberto pela mensalidade", e a fase 4 (339)
lista só "contato válido ou mensalidade". Se a unidade escolhida for o clique, o que se vende não é "lead válido" e a
definição da linha 302 não cobre (item 8 da lista final).

### 4.5 "Dado de contato" contra endereço IP — **não fecha (o achado principal)**
- As frases corrigidas estão coerentes entre si: 188, 193–196, 209–213, 278, 365.
- **Mas** o aviso que a pessoa lê ao lado do botão continua dizendo que o site "registra **só** que o botão foi tocado
  (data, página e empresa)" (linha 186), enquanto as linhas 132 e 209–210 dizem que o servidor guarda registro de
  acesso bruto com endereço IP.
- **E** a premissa "não ligar o IP ao toque" (210; lista, item 9, linhas 400–401) não fecha com o mecanismo descrito
  no mesmo item: o toque é um pedido ao endereço `/ir/…` do próprio site (203), e o registro de acesso bruto que a
  seção 3.4 exige (132) anota cada pedido com data, hora, endereço pedido e IP. Ou seja, o próprio registro bruto liga
  o IP ao toque, a menos que o desenho diga como evita isso (por exemplo: não gravar o IP nos pedidos a `/ir/`, ou
  truncá-lo). O desenho não diz. Pela mesma razão, a frase "Toques repetidos da mesma pessoa não dá para distinguir sem
  cookie nem endereço IP" (206) descreve uma escolha, não uma impossibilidade.
- O primeiro verificador pediu a troca de duas frases (antigas 173 e 178) e isso foi feito; o aviso da antiga linha 171
  (atual 186) não estava na lista dele. É o mesmo tipo de defeito — afirmar sobre dado pessoal mais do que o texto
  sustenta —, agora num texto dirigido ao consumidor (item 1 da lista final).

### 4.6 Lista de premissas (seção 10) contra as marcas PREMISSA do corpo — fecha
Cada PREMISSA do corpo está na lista:

| Corpo (linha) | Item da lista |
|---|---|
| 41, 99 (licença e preço atraem busca; rende posição) | 1 |
| 100 (páginas de dúvida e de comparação) | 2 |
| 90 (número de páginas) | 3 |
| 192, 262 (três empresas), 276 (5 dias úteis) | 4 |
| 198–200 (código; que as licenciadas aceitem contar), 301, 303 (que ela informe) | 5 |
| 337 (cerca de 3 meses), 351 (6 a 12 meses) | 6 |
| 119 (abertura da página) | 7 |
| 127 (robôs de treino; no corpo é DECISÃO DO OWNER com padrão "liberar") | 8 |
| 210 (IP: guardar pouco, não ligar ao toque) | 9 |
| 83, 148, 322 (consulta pública) | 10 |
| 68 ("quem somos" como fator de citação) | 11 |
| 120, 125 (texto visível; sem script, para o ChatGPT) | 12 |
| 326 (ritmo de publicação) | 13 |
| 336 (3 a 5), 337 (1 a 3) | 14 |
| 201 (redirecionamento), 133 (sem cookie e sem script) | 15 |
| 267 (canal da Via B) | 16 |
| 66 (não pedir avaliação), 62 ("nossa equipe"), 147 (razão social e endereço), 288 (telefone do site), 149 (área atendida) | 17 |

Cada item da lista tem origem no corpo. Único item sem a palavra PREMISSA na origem: "6 pragas" (item 3), que no corpo
é só a contagem de T2 (linha 77). Sem defeito.

### 4.7 Legenda (linhas 20–25) contra as marcas das tabelas
Usadas e na legenda: classe A, classe A/B, PREMISSA (inclusive "por prudência" e "de prudência"), INFERÊNCIA,
OBSERVAÇÃO DA AMOSTRA, REGRA DA RODADA, DECISÃO DO OWNER. Fora da legenda: "requisito de medição" (132). "Não
conclusivo" aparece como situação na linha 124 (`LocalBusiness` de terceiro) e é termo de veredito de [R], não marca
de evidência; aceitável.

### 4.8 Outras contradições e erros novos (trazidos pelas correções)

| Linha | O que é | Gravidade |
|---|---|---|
| 404–405 | Premissa 12: "fontes B de 2025 e de 2024, que podem estar desatualizadas". Para o ChatGPT, as bases são F13 (uma B de julho/2026, [G] linha 85 e seção 9, linha 7) e F25 (B de 17/12/2024, [G] linha 97 e seção 9, linha 5). As "fontes de 2025" são as classe A do Google e da Microsoft de [C] 7.1 (linha 343), que sustentam o lado do Google, não esta premissa. A linha 120 está certa; a 404–405 misturou | Baixa |
| 19 contra 417 | O cabeçalho diz [M] "**em verificação**"; a seção 11 diz "[M], verificado em 13/11 (aprovado com ressalvas…)". O próprio [M] (linhas 8–9) diz que as correções "ainda não foram reverificadas" | Baixa |
| 417 contra 262 | "as correções [de M] não alteram o que este arquivo cita": quase. O "6" de "até 4 ou 6 prestadores" passou a levar em [M] "artigo de 2021, **pode estar desatualizada**", e o "4" do GetNinjas ganhou a ressalva "a mesma página diz 3". Pela regra da rodada, a marca acompanha o número | Baixa |
| 418 | "as linhas afetadas são: seção 1, item 2; seção 3.2; seção 9": faltam a seção 8 (353–354, "68 das 79") e a seção 10, premissa 1 (388–390), que agora cita "12 de 67" e "47%"; e as linhas 83 e 148 (consulta pública "numa busca da amostra") | Baixa |
| 61 e 227 contra 154 | A faixa fixa ganhou "não tem licença"; a declaração resumida na seção 2 ("indica empresas licenciadas; não é dedetizadora; não executa o serviço…") e o texto do formulário ("Não é dedetizadora, não executa o serviço e não cobra nada de você") não ganharam. [R] linha 248 traz as três negações juntas | Baixa |
| 35–36 | "o orgânico é quase todo de sites de dedetizadoras" ficou sem ponteiro próprio: [S, seção 8] cobre só "50 dos 67". O dado está em [S] 7.3, item 1 (568 de 709, 80%) | Baixa |
| 36–38 | "12 desses 67" e, em seguida, "os 11 domínios que o mostram": é o que [S] diz (linhas 284 e 317), mas a diferença 12 × 11 fica sem explicação. [M] linhas 533–535 explica: 11 na classe "empresa com número de licença", mais um domínio satélite que também exibe. Sugestão, não defeito | Registro |
| 37–38 | [S] 7.3, item 5, acrescenta que dois domínios respondem por 28 das 37 primeiras posições. O desenho não traz; como o dado pesa contra a aposta do próprio desenho, a omissão não o favorece. Sugestão | Registro |
| 127 contra 204 | A linha do `robots.txt` na seção 3.4 diz o que libera e não menciona o `Disallow: /ir/` criado na 5.1. Não é contradição; é a mesma regra em dois lugares, um deles incompleto | Registro |
| 201–206 | O redirecionamento por endereço próprio é escolha nova e está marcado PREMISSA. A política de spam do Google tem uma categoria "redirecionamentos enganosos", que [A] só lista pelo nome (linhas 148–149) e não detalha em 2.1. O redirecionamento descrito leva a pessoa aonde o texto do botão diz, então não vejo conflito; mas o ponto **não foi lido na fonte**. Registro, para a segunda passada | Registro |

## 5. Efeito das correções em outros arquivos (fora do artefato; não editei)

- `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`, linhas 18 e 19: a pergunta 3 remete a "D, seção 8
  (fase 1, letra c)" para a conversa com as licenciadas e a pergunta 4 a "(fase 1, letra b)" para o advogado. Com a
  reordenação da fase 1, a conversa é a letra (b) e o advogado é a letra (c). As letras ficaram trocadas.
- Mesmo arquivo, linha 20 (pergunta 5): "o site registra o clique e não guarda dado de ninguém". É a frase que a
  correção 6 tirou do desenho; aqui ficou.
- `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` (linhas 84 e 102) e
  `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` (linha 86) repetem o aviso
  "registra só que o botão foi tocado"; `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` (linha
  75) diz que o servidor anota "data, página pedida e endereço IP" e que o site "não liga o endereço IP ao toque no
  botão" — a mesma contradição da seção 4.5. A faixa fixa do protótipo já traz "não tem licença"; o `robots.txt` do
  protótipo já traz `Disallow: /ir/`.
- Não li o protótipo nem `perguntas_owner.md` além disso; são dos itens 7 e 8.

## 6. Dependências proibidas e o quadro de vereditos de [R] (linhas 21–38), depois das mudanças

| Prática | Há dependência? | Onde conferi (linha atual) |
|---|---|---|
| Perfil de empresa fora da regra (quadro, linhas 25 e 27) | Não | 33; 63; 363; 382 |
| Endereço fictício ou de fachada (linha 26) | Não; o endereço exibido é o da licenciada | 147; 382 |
| Avaliação fabricada, comprada ou incentivada (linha 29) | Não; sem estrelas; "não pedir" é escolha mais estrita | 66; 324; 382 |
| Link comprado | Não; `rel="sponsored"` para parceira que paga; T12 agora diz que não se exige link de volta | 67; 87; 205; 383 |
| Consulta automática ao Google | Não. A linha 296 agora afasta expressamente o método do item 4; "Nunca por robô" na 323 | 52; 294; 296; 323; 383 |
| Página de oferta sem empresa nomeada (linha 31, não conclusivo) | Não tem essa página | 175–177; 383 |
| Vender só com legítimo interesse (linha 35, não conclusivo) | Não usa | 230–238 |
| Número do site que tria e repassa (linhas 36–37) | Fora; o canal novo da Via B diz "**nunca** por WhatsApp do site" | 65; 264–266; 284; 383 |
| Botão que abre o WhatsApp da licenciada (linha 38, permitido com condição) | É a Via A; o passo intermediário está marcado PREMISSA | 181–208 |
| Administrar o perfil da licenciada (linha 28, permitido com condição) | Só na fase 5, remetendo aos limites de [B] seção 10 | 340; 353–355 |

Nada marcado "vedado" virou escolha. As escolhas novas (endereço `/ir/`, canal por e-mail ou página restrita, T9 com
nomes, três empresas por página) não criam dependência de prática vedada.

## 7. Portão e forma

- **Portão:** os elementos conferidos pelo primeiro verificador continuam presentes; nenhuma correção tirou conteúdo
  exigido. Texto de consentimento (223–244), para quantas empresas (48–50; 191–192; 260–262), exclusão (193–196;
  274–276), medir posição, clique, lead e lead vendido (290–304), automatizável (313–326), fases (328–355), as quatro
  restrições uma a uma (361–366), premissas marcadas (386–412).
- **Português:** sim.
- **Caminho absoluto:** os sete arquivos de base (13–19), a verificação (5), o roteiro (298), `RODADA.md` (309, 339),
  o protótipo (208), `perguntas_owner.md` (378). Todos existem.
- **Jurídico como levantamento:** sim (26–27); o texto novo manda os pontos abertos ao advogado ("a rever com o
  advogado", 267; "na lista do advogado da fase 1", 213) e marca "não conclusivo" o que [R] marca. Exceção de tom: o
  aviso da linha 186 (seção 4.5).
- **Dado pessoal:** nenhum. Só "EXEMPLO" e colchetes; nenhum nome de pessoa, telefone, domínio de empresa real ou
  texto de avaliação.
- **Nada afirmado como feito:** linhas 7–8 ("Nada aqui foi publicado, comprado, cadastrado nem enviado"); a conferência
  das correções aparece como "em curso". A hora "22:19" da linha 6 bate com a alteração do arquivo (22:19:05).
- **Regra de evidência:** "pode estar desatualizada" nas linhas 120 e 125; falta no "6" da linha 262. Nenhum número de
  outro país virou número do Brasil.

## 8. O que ainda falta (lista numerada, com a linha atual)

**De conteúdo**

1. **Linhas 186, 132, 203, 206, 209–211 e 400–401** — o aviso ao lado do botão diz que o site "registra só que o botão
   foi tocado (data, página e empresa)", e a premissa 9 promete "não ligar o IP ao toque"; mas o toque é um pedido a
   `/ir/…` e o registro de acesso bruto exigido na seção 3.4 anota esse pedido com o IP. Dizer como o registro bruto
   deixa de ligar IP e toque (não gravar ou truncar o IP nos pedidos a `/ir/`, por exemplo) **ou** reescrever o aviso e
   a premissa para dizer o que de fato fica registrado. Repetir o ajuste no protótipo e na pergunta 5 de
   `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`.

**Menores**

2. **Linhas 84 e 139 (correção 18, em parte)** — T9 nomeia a licenciada e publica o preço dela, com o número da
   licença, mas sem o órgão emissor, e não está na lista de páginas do bloco "Quem executa". Acrescentar o órgão em
   cada linha de T9, ou dizer que T9 leva o bloco; e pôr o ponto entre os que o advogado olha (se uma tabela de preços
   com empresa nomeada é "propaganda" para o art. 22 não foi levantado).
3. **Linha 132 (correção 16, em parte)** — "requisito de medição" continua na coluna Marca, fora da legenda. Tirar ou
   pôr na legenda.
4. **Linhas 404–405** — premissa 12: trocar "fontes B de 2025 e de 2024" por "uma fonte B de 2026 (texto visível) e
   uma de 2024, que pode estar desatualizada (sem script)".
5. **Linha 87** — trocar [M, seção 4.0] por [M, seções 4.2, 4.3 e 4.6] em "como é cobrada".
6. **Linhas 19, 262 e 417** — alinhar o estado de [M] (cabeçalho "em verificação" × seção 11 "verificado"; as
   correções de [M] não foram reverificadas) e pôr no "6" de "até 4 ou 6 prestadores" a marca "pode estar
   desatualizada" que [M] seção 6 passou a trazer (artigo de 2021).
7. **Linha 418** — completar a lista do que muda se [S] mudar: seção 8 (353–354), seção 10, premissa 1 (388–390), e as
   linhas 83 e 148.
8. **Linhas 347, 302 e 339** — "clique" aparece como unidade de cobrança possível só na linha 347; ou tirar, ou
   ajustar a definição de lead vendido e a fase 4.
9. **Linhas 61 e 227** — acrescentar "não tem licença" à declaração da seção 2 e ao texto do formulário, como na faixa
   fixa (154).
10. **Linhas 35–36** — pôr [S, seção 7.3, item 1] em "o orgânico é quase todo de sites de dedetizadoras".

Fora do desenho, para a sessão principal: as letras da fase 1 em
`/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` (linhas 18 e 19).

## 9. O que não conferi

- Nenhuma fonte primária na web: a conferência é do desenho contra os arquivos do projeto.
- Não refiz as contas de [S] a partir dos CSVs; conferi que os números do desenho estão em [S].
- De [B] não reabri nada; de [C], [G] e [A], só as seções tocadas pelas correções (lista no cabeçalho). Os ponteiros
  não alterados ficam com a conferência do primeiro verificador.
- Não verifiquei as correções de [M] (item 5) em si; só que as seções citadas pelo desenho continuam dizendo o que ele
  atribui.
- Do protótipo e de `perguntas_owner.md`, só o que está na seção 5.
