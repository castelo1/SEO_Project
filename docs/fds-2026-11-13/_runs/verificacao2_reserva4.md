# Verificação 2 (segunda passada) — fila de reserva, tarefa 4: pontos de um contrato de venda de leads

- **Quem:** revisor independente, subagente em contexto limpo, sem acesso à conclusão de quem escreveu nem às
  verificações e correções anteriores (nenhum arquivo `verificacao*` ou `correcoes*` de `_runs/` foi aberto; só listei
  os nomes). O que o próprio artefato diz sobre verificações anteriores (linhas 5–9) foi desconsiderado.
- **Quando:** sábado, 14/11/2026, das 02:01 às 02:16 (Brasília; horas lidas de `TZ=America/Sao_Paulo date`: 02:01:25
  no início, 02:13:42 antes de gravar este arquivo, 02:16:21 no ajuste final). Leituras da web: entre as leituras de `date` das 02:02:54 e das
  02:13:42 (a ferramenta não grava a hora de cada página).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md`, 412 linhas, lido inteiro às 02:01, na
  versão gravada às 01:59:04 de 14/11/2026 (conferi às 02:13:42 que não mudou durante a revisão).
- **Portão (de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linhas 74–75):** "Levantamento dos
  pontos de um contrato de venda de leads (região, exclusividade, preço, disputa de lead inválido), com fonte;
  levantamento, não minuta para assinar."
- **Natureza desta verificação:** conferência de fonte e de forma. Não é parecer jurídico.

## Veredito

**APROVADO COM RESSALVAS.**

- Portão: cumprido nas cinco partes (tabela abaixo).
- Sorteio: **0 falha em 12** (semente 20261114). Limite de reprovação: mais de 2.
- Leis brasileiras: **todas** as citações de Código Civil, CDC, LGPD, Marco Civil e RDC 622 foram reabertas na fonte
  oficial; **nenhuma divergência** de artigo nem de texto. Reabri também, fora do pedido, as demais leis e normas (L4,
  L5, L6, L8 a L11, L13 a L15) e as 14 páginas de plataforma: sem divergência de texto (só pontuação: achado 6).
- Ressalvas: 12 achados. O principal é mecânico (47 remissões a `[D]` por número de linha ficaram defasadas com as
  correções de hoje no desenho). Dois são de conteúdo: a frase "crédito, não dinheiro" vai além do que as páginas
  dizem (achado 2), e a pergunta "amostra com autorização?" não acompanha o que o desenho e os modelos passaram a
  dizer hoje sobre conferência só por números (achado 3). Nenhum achado contraria uma restrição do item 2.

## O que abri

**Arquivos do projeto (inteiros, salvo indicação):**

| Arquivo | Versão lida | Observação |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` | 02:01 | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | 02:01 | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` | gravado às 01:59:04 | inteiro, com a tabela de fontes |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` [R] | lido às 02:01 (versão da 01:45); mudou às 02:03:33 | a mudança das 02:03 trocou marcas [S] por [N] em quatro linhas (36, 422, 424, 435), sem deslocar linha; reconferi pelo `git diff` |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` [D] | gravado às 01:54:32 | inteiro; comparei com as versões de 22:38 e 23:44 de 13/11 e de 01:49 de 14/11 (`git show`, só leitura) |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` [M] | **duas leituras: 02:02:54 (versão de 13/11 22:17) e 02:12:03 (em correção por outro agente; gravado às 02:11:39 e de novo às 02:12:51)** | só as linhas citadas pelo artefato; 792 linhas nas duas leituras (sem deslocamento) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` [B] | gravado às 01:55:36 | linhas 412–461 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` [A] | gravado às 01:55:36 | linhas 150–173 |

**Páginas da web reabertas (todas pela ferramenta de leitura; nenhuma pelo navegador):** L1 a L15 (as
15 abriram), P1 a P14 (as 14 abriram) e, de [M], F8, F25, F29 e F37; mais a página do Google que sustenta a frase de
[R], linhas 126–128 (`https://support.google.com/business/answer/7163406?hl=en`). Lista com resultado nas tabelas
abaixo. A ferramenta responde por um modelo pequeno e limita cada citação a cerca de 125 caracteres: pedi os artigos
em fragmentos literais consecutivos; onde só veio resumo, está escrito.

## Portão, parte por parte

| Parte do portão | Onde está no artefato | Tem fonte? | Resultado |
|---|---|---|---|
| Região | seção 2 (linhas 88–94): 2.1 delimitação, 2.2 contato de fora da área, 2.3 praga não atendida | Lei 4.886, art. 27, d; CC, art. 710; RDC 622, arts. 3º e 4º; CDC, arts. 30 e 37; termos da Angi (EUA), Service Direct (EUA), Google, oHub (BR); [R], [D], [M] | **cumpre** |
| Exclusividade | seção 3 (linhas 98–106): 3.1 a 3.5 | CC, arts. 421, 421-A, 598, 412, 413, 711, 726; Lei 4.886, arts. 27, e, e 31, parágrafo único; Lei 12.529, art. 36; 99 Calls (EUA, classe D, só como exemplo); [M] | **cumpre** |
| Preço | seção 4 (linhas 110–117): 4.1 forma de cobrança, 4.2 reajuste, 4.3 atraso, 4.4 nota fiscal | CC, arts. 394, 395, 406, 412, 476, 597; Lei 10.192, arts. 1º e 2º; LC 116/2003; oHub (BR, R$ 172 a R$ 682), PedeGás (BR), Service Direct (EUA), 99 Calls (EUA, classe D). Valor do lead: "sem fonte", dito | **cumpre** |
| Disputa de lead inválido | seção 5 (linhas 121–155): 5.1 motivo a motivo, 5.2 definição, prazo, prova, devolução, quem decide | termos da Angi (EUA), Service Direct (EUA), eLocal (EUA), Google, oHub (BR), Cronoshare (BR), GetNinjas (BR); CC, art. 421-A; LGPD, art. 8º, § 2º, via [R] | **cumpre**, com os achados 2, 7 e 8 |
| Levantamento, não minuta nem parecer | linhas 10–14 ("Não é minuta para assinar e não é parecer jurídico"); coluna "Em aberto para o advogado" em todas as tabelas; "não levantado", "silente", "não levantado: jurisprudência" e "leitura minha" onde cabem; seção "Não sei" com 13 itens | — | **cumpre**: não achei cláusula redigida nem texto pronto para assinar. A seção 14 ("O que não pode estar no contrato") tem título forte, mas a coluna do meio diz, linha a linha, se é veredito, inferência ou texto de lei cuja aplicação é do advogado |

O artefato vai além dos quatro pontos do portão (objeto, propaganda, LGPD, WhatsApp, consumidor, marca, saída,
medição, gestão de perfil). Isso não fere o portão; a fila de reserva pede "os pontos de um contrato", com os quatro
como mínimo.

## Sorteio de 12 afirmações com fonte externa

**Método:** população = as 142 ocorrências de código de fonte externa (`[L…]` ou `[P…]`) nas linhas 77 a 290 do
artefato, numeradas na ordem em que aparecem; sorteio com `random.seed(20261114)` e `random.sample(range(142), 12)`
em Python 3. A afirmação conferida é o texto que antecede o código na mesma célula.

| # | Linha | Fonte | Afirmação | O que a fonte devolveu (14/11/2026) | Classe e quem ganha | Resultado |
|---|---|---|---|---|---|---|
| 7 | 82 | P6 | Service Direct (EUA): "Any call that occurs when a New Potential Customer is seeking a service that your Service Category typically provides" ou que resulte em agendamento | frase literal igual; segue "or any call that results in a Booked Appointment."; rodapé "Copyright © 2026"; a página não nomeia país (o artefato diz isso) | A sobre si; ganha a Service Direct; país dito | **confere** |
| 17 | 93 | L1 | CDC, art. 30 (resumo) e art. 37, § 1º (resumo) | art. 30: "…obriga o fornecedor que a fizer veicular ou dela se utilizar e integra o contrato…"; art. 37, § 1º: "…mesmo por omissão, capaz de induzir em erro o consumidor…" | A; o Estado | **confere** |
| 34 | 114 | P5 (e [M], linha 106) | oHub (BR): crédito válido por "1 (um) ano a contar da confirmação do pagamento"; pacotes de R$ 172 a R$ 682 | cl. 6.3.1: "1 (um) ano a contar da confirmação do pagamento pelo oHub"; rodapé 2026. Preços: reabri F8 (`https://www.ohub.com.br/planos`): 100 créditos R$ 172,00; 180, R$ 298,00; 240, R$ 392,00; 420, R$ 682,00; 12 meses | A sobre si; ganha o oHub; preço em reais com fonte brasileira | **confere** |
| 40 | 116 | L3 | CC, arts. 394, 395, 406 (Lei 14.905/2024), 412, 476 | os cinco, em fragmentos literais; "os juros serão fixados de acordo com a taxa legal." com a marca da Lei 14.905/2024; art. 476: "…nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro." | A; o Estado | **confere** |
| 61 | 153 | P4 | oHub (BR) confere com o comprador e com reclamações de outros fornecedores; "Não serão aceitos pedidos de análise efetuados por e-mail, telefone ou qualquer outro canal." | critérios "Reclamações de outros fornecedores;", "Dados informados pelo potencial comprador; e" e "Confirmação de informações com o potencial comprador"; frase literal igual | A sobre si; ganha o oHub | **confere** |
| 62 | 154 | L1 | CDC, art. 2º: "destinatário final" | "Consumidor é toda pessoa física ou jurídica que adquire ou utiliza produto ou serviço como destinatário final." | A; o Estado. O artefato não conclui ("não levantado") | **confere** |
| 111 | 219 | L9 | Lei 9.610, art. 22 (literal) e art. 7º, I | art. 22 literal igual; art. 7º, I: "os textos de obras literárias, artísticas ou científicas;" | A; o Estado | **confere** |
| 113 | 220 | L8 | Lei 9.279, art. 129 (literal), arts. 130 e 139 (resumo), art. 140 (literal) | os quatro batem; art. 130, II: "licenciar seu uso;" | A; o Estado | **confere** |
| 124 | 233 | P3 | GetNinjas (BR): termos novos valem dez dias depois de publicados (cl. 4a) | "Os novos Termos entrarão em vigor 10 (dez) dias depois de publicados na Plataforma."; rodapé "©2011-2024" (o artefato marca "pode estar desatualizada") | A sobre si; ganha o GetNinjas | **confere** |
| 128 | 244 | P14 | Google, política para terceiros: compartilhar relatórios de custo e de desempenho de modo acessível ao cliente | "Share your Business Profile management cost and performance reports"…; título "Business Profile third-party policies"; "©2026 Google", sem data | A; ganha o Google (dono da plataforma) | **confere** |
| 130 | 246 | P4 | oHub (BR) confirma com o comprador | "Confirmação de informações com o potencial comprador"; o oHub "poderá tentar efetuar o contato", por "mera liberalidade" | A sobre si | **confere** (a mesma célula cita P7 e P9, reabertas: batem) |
| 142 | 287 | L3, L6 | CC, art. 412; Lei 10.192, art. 2º, § 1º | art. 412 literal igual; "É nula de pleno direito qualquer estipulação de reajuste ou correção monetária de periodicidade inferior a um ano."; DOU de 16.2.2001 | A; o Estado | **confere** |

**Placar: 12 conferem, 0 falha, 0 "não confirmado".**

## Citações de lei brasileira — todas reabertas na fonte oficial

Código Civil, CDC, LGPD, Marco Civil (planalto.gov.br) e RDC 622/2022 (base de legislação da Anvisa, o mesmo endereço
de L12). "Literal" = o fragmento entre aspas no artefato veio igual, palavra por palavra (os acentos vêm corrompidos
na página do Planalto e a ferramenta os restaura); "resumo" = o artefato resume e o resumo corresponde ao texto.

| Lei | Dispositivos citados no artefato | Resultado |
|---|---|---|
| CDC (L1) | art. 2º; art. 3º e § 2º; art. 7º, parágrafo único; art. 14 e § 3º; art. 18; art. 20 e incisos; art. 25 e § 1º; art. 30; art. 34; art. 36 e parágrafo único; art. 37, § 1º; art. 38. Alteração mais recente vista: MP 1.393/2026, no art. 57 | **todos conferem** (citações literais e resumos) |
| LGPD (L2) | art. 5º, VI e VII; art. 6º, I; art. 7º, § 5º; arts. 15 e 16; art. 18, § 6º; art. 37; art. 42, caput, § 1º, I e II, e § 4º; art. 43; art. 48. A página escreve "Lei nº 15.452, de 2026" com link para `L15352.htm`, como o artefato registra | **todos conferem** |
| Código Civil (L3) | arts. 265, 283, 285, 394, 395, 406, 412, 413, 421, 421-A (caput, I e II), 422, 425, 473 e parágrafo único, 476, 594, 597, 598, 599 e parágrafo único, I (oito dias), 710, 711, 720, 722, 726, 934. Redações: Lei 13.874/2019 (421 e 421-A) e Lei 14.905/2024 (406) | **todos conferem** (li os trechos 0–100.000, 100.000–200.000 e 200.000–300.000 da página) |
| Marco Civil (L7) | art. 5º, VIII; art. 15, caput ("…pelo prazo de 6 (seis) meses, nos termos do regulamento.") e § 1º; art. 17 ("…não implica responsabilidade sobre danos decorrentes do uso desses serviços por terceiros."). Redações da MP 1.068/2021 marcadas "(Rejeitada)" | **todos conferem**; ver achado 11 (o link "Regulamento" é o Decreto nº 8.771) |
| RDC 622/2022 (L12) | art. 3º, III e VI; art. 4º e parágrafo único; art. 5º; art. 19 (inciso XI: "…números das licenças sanitária e ambiental com seus respectivos prazos de validade."); art. 21; art. 22, caput e I a III; art. 23. Data 09/03/2022, DOU 16/03/2022, "Vigente" | **todos conferem** |

**Outras leis e normas, reabertas por conta própria:** Lei 4.886 (arts. 1º, 2º, 27, d, e, j, 31 e parágrafo único,
34; redação da Lei 8.420/1992); Lei 12.529 (art. 36, I e IV, § 2º, § 3º, I, c, e VI); Lei 6.437 (art. 3º e § 1º;
art. 10, V, com redação da MP 2.190-34/2001); LC 116 (art. 1º; subitens 1.09, 10.02, 10.08, 17.06, 17.25); Lei 10.192
(arts. 1º e 2º); Lei 9.610 (arts. 4º, 7º, I e VII, 22, 29, 50, 79, § 1º); Lei 9.279 (arts. 129, 130, 139, 140, 195,
XI); Resolução CD/ANPD 2/2022 (arts. 9º, 11 e § 1º, 14, II; publicada em 26/04/2024, modificada em 16/09/2026);
página da ANPD sobre incidente (três dias úteis; publicada em 23/12/2022, modificada em 26/08/2026); glossário da
ANPD (publicado em 29/04/2024, modificado em 23/01/2025; cita guia de 2022). **Todas conferem**, inclusive as datas da
tabela de fontes.

## Páginas de plataforma reabertas fora do sorteio

| Fonte | O que conferi | Resultado |
|---|---|---|
| P1 Política de Mensagens do WhatsApp | as três frases citadas (linhas 192 e 193); "Last updated: September 23, 2026" | confere, literal |
| P2 Termos do aplicativo WhatsApp Business | as seis frases citadas (linhas 191 a 193); "Effective September 23, 2026" | confere o texto; duas citações terminam com ponto onde a fonte tem vírgula e continua (achado 6) |
| P3 GetNinjas (BR) | cl. 4a, 5c, 7d, 9a, 13c, 15b, 16b, 17b, foro; rodapé "©2011-2024"; os termos não preveem contestação de pedido inválido | confere |
| P4 oHub, contato garantido (BR) | três motivos de devolução; 5 dias úteis e 3 mensagens; três casos sem devolução; 3 e 10 dias úteis; sem prazo para pedir; decide o oHub, sem recurso | confere |
| P5 oHub, termos (BR) | considerando (iii); cl. 3.7, 4.4, 6.3.1, 11.1, 13.1 ("sem qualquer ônus"), 13.2.1, 14.1; sem licença de marca; rodapé 2026 | confere |
| P6 Service Direct (EUA) | lista de ligações não cobráveis; "Unanswered calls are always Billable."; 20 segundos | confere; ver achados 6 e 8 |
| P7 Service Direct, revisão | 7 dias; 2 a 3 dias úteis; gravação ativada; equipe de qualidade; "a credit will be applied to your account." | confere |
| P8 Service Direct, cobrança | frase do limiar; "typically $100"; cartão secundário | confere |
| P9 eLocal (EUA) | 4 dias; caixa postal e ligação perdida; "A valid call is never a guaranteed customer."; pesquisa de preço; gravação; "© 2026 eLocal USA LLC" | confere; a página **não diz** se o crédito é saldo ou dinheiro (achado 2) |
| P10 Google, créditos automáticos | título; "Google no longer supports credits for "job type not serviced" and "geo not serviced" leads."; EMEA; 30 dias | confere |
| P11 Angi (EUA) | cinco motivos de crédito; cinco de não crédito; "The lead must be less than 45 days old."; crédito vence em seis meses; 14/08/2026; não nomeia país | confere; ver achado 12 |
| P12 Cronoshare (BR) | as duas frases; sem prazo nem percentual; só em cronos; "© Cronoshare 2012-2026" | confere |
| P13 99 Calls (EUA, classe D) | exclusividade; US$ 24,99; "$99 per month"; "There is no long-term contract."; duplicadas e spam; "Last updated October 2026" (há também "Last updated June 2026" noutra seção) | confere; classe D correta |
| P14 Google, política para terceiros | as oito frases citadas na seção 13 | confere, literal |
| F8 oHub, planos (BR) | preços dos quatro pacotes; pergunta frequente: 4 respostas, "é possível chegar até a 6", 40% e 80% | confere; muda a ressalva da linha 102 (achado 4) |
| F25 PedeGás (BR) | R$ 0, R$ 99 e R$ 199 por mês; "Topo em todas as cidades que você atende."; "© 2026" | confere |
| F29 Google, como os leads funcionam | "You're charged for each valid lead you receive through your Local Services ad."; 15 dias | confere |
| F37 BrightLocal | "$499 per location/month" e "$1,299 per location/month"; EUA, Reino Unido, Canadá e Austrália | confere; ver achado 5 (classe) |
| Google 7163406 | "Third parties can’t promise nor directly influence your business’s ranking on Google Search or Maps through any special means." | confere (o artefato dizia "não relida aqui") |

## Classe de evidência e "quem ganha"

- A tabela de fontes tem as colunas "Classe" e "Quem ganha" preenchidas para as 29 fontes; a contagem do rodapé (28 de
  classe A, sendo 15 de lei, norma ou órgão e 13 de plataforma sobre si; 1 de classe D) bate com a tabela.
- Nenhuma fonte de classe B ou C. A única D (99 Calls) é usada como exemplo do que **não** copiar e como ilustração de
  preço dos Estados Unidos; nenhuma regra se apoia nela. BrightLocal (via [M]) aparece só como preço de vendedor.
- País: dito na tabela de fontes e na maior parte das células. Faltam em algumas menções (achado 7). O cabeçalho
  (linhas 26–27) diz que regra de outro país "não vira regra do Brasil" e que o que a plataforma faz "não é o que a lei
  manda". Não achei termo dos Estados Unidos tratado como prática brasileira.
- A classe "A (sobre si)" para termos de plataformas privadas é extensão da tabela do `RODADA.md` (que lista Google,
  Meta, lei, norma e órgão regulador). O artefato a usa só para "o que os termos dela dizem", o que é defensável; mas
  [M] passou hoje a marcar essas fontes como "A\*" e o item 9 do "Consenso" apoia-se nelas (achado 5).

## O que procurei e o que achei

| Procurei | Resultado |
|---|---|
| Afirmação sem fonte | Não achei afirmação de fato sem fonte. As leituras de quem escreveu estão marcadas ("leitura minha", "observação de quem escreveu, sem fonte", "não levantado") |
| Regra apoiada só em relato ou em vendedor | Não há |
| Preço em reais sem fonte brasileira | Não há: R$ 172 a R$ 682 (oHub, BR) e R$ 0, R$ 99 e R$ 199 por mês (PedeGás, BR), ambos reabertos; valor do lead: "sem fonte", dito na linha 114 |
| Conclusão jurídica dita como certa | Não achei. Responsabilidade do intermediário, enquadramento do contrato, "concorre", "patrocinador", CDC entre as partes, defesa da concorrência e Marco Civil estão como "não levantado", "silente" ou "pergunta para o advogado" |
| Vender o mesmo contato a várias empresas sem a pessoa saber | Fora (linha 281 e seção 7.3). A linha 102 descreve o que as plataformas brasileiras fazem, sem adotar |
| Repassar dado obtido pela API do WhatsApp | Fora (linhas 193 e 277) |
| Reter o perfil do Google da licenciada | Fora (linhas 258 e 275) |
| Prometer posição | Fora (linhas 83, 260 e 278) |
| Avaliação comprada ou incentivada | Fora (linhas 261 e 279) |
| Relatório da licenciada com nome, telefone ou conversa | O artefato não prevê isso e avisa que captura de tela da conversa é compartilhamento que a via A prometeu não fazer (linha 153). Mas as linhas 245 e 246 não trazem o que o desenho diz hoje ("só números") e deixam aberta a "amostra com autorização" sem dizer que ela só cabe na via B (achado 3) |
| Dado pessoal no artefato | Não há nome de pessoa física, telefone nem avaliação copiada |

## Remissões internas

Abri **todas** as remissões com número de linha (cerca de 130: R, 41; D, 47; M, 29; B, 8; A, 5) e as remissões por
seção.

| Arquivo | Resultado |
|---|---|
| [R] `00_restricoes.md` (corrigido à 01:45; marcas trocadas às 02:03) | **41 de 41 ainda dizem aquilo.** Conferidas: quadro 27–31 e 36–37; 73–74; 78–80; 95–100; 110–116; 126–128; 133–134; 165; 170–174; 186–194; 200–203; 217–218; 223–229; 253–258; 286; 298–304; 317; 320; 328–331; 353–356; 358–368; 395–397; 411–427; 438–441 |
| [D] `desenho_v0.md` (corrigido à 01:49; gravado às 01:54) | **47 de 47 remissões por número de linha estão defasadas** (achado 1): o artefato usa a numeração de D das 22:38 de 13/11; D ganhou linhas às 23:44 e à 01:49. O **conteúdo** citado existe em D e diz aquilo em todos os casos; só o número mudou (de 8 a 19 linhas adiante). As remissões por seção, passo ou premissa ("seção 4.3, última linha", "seção 5.1, passo 3", "seção 10, premissa 5", "seção 8, fase 3" etc.) continuam certas |
| [M] `modelos_de_negocio.md` (em correção) | Na leitura das 02:02:54 (versão de 13/11 22:17): **29 de 29 dizem aquilo**. Na leitura das 02:12:03 (em correção): as linhas não se deslocaram, mas o texto mudou em pontos que o artefato repete — linhas 108 e 595 (o "6" do oHub deixou de ser só do artigo de 2021), 140 (BrightLocal passou de D para "A\*"), 173 e 184–185 ("crédito ou saldo"; só a Cronoshare diz que não reembolsa em dinheiro), 486–487 (conferência por amostra "só possível na via B"). Ver achados 2 a 5 |
| [B] `02_google_maps_perfil.md` | **8 de 8 dizem aquilo** (418–424, 444, 445, 451, 453, 458, 461; seção 10 em 416–461) |
| [A] `01_google_organico.md` | **5 de 5 dizem aquilo** (164–167; seção 2.1 em 152–173) |
| `RODADA.md`, linha 65 (linha 221 do artefato) | diz aquilo |

## Forma

- Português: sim. Citações em inglês curtas, entre aspas, de termos e políticas.
- Número com unidade, país e fonte: sim (US$ com "EUA"; R$ com "BR"; prazos com unidade). Período: as páginas de
  plataforma não têm data e o artefato diz "sem data" com o ano do rodapé; data de leitura na tabela de fontes.
- Caminho absoluto: sim, no cabeçalho e onde o owner precisa abrir arquivo.
- Texto longo copiado: não há; só fragmentos curtos.
- Jurídico como levantamento: sim, dito no cabeçalho e repetido nas seções 9 e 14.
- Linhas 143–145: quebra de linha no meio da frase do GetNinjas (só aparência).

## Achados

**1. Remissões a [D] por número de linha defasadas (47).** Arquivo:
`/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md`. Causa: o desenho mudou às 23:44 de 13/11 e à 01:49 de
14/11; o artefato ficou com a numeração das 22:38. Redação certa (linha do artefato: escrito → certo, na versão de D
gravada às 01:54:32):

| Linha do artefato | Escrito | Certo |
|---|---|---|
| 81 | seção 8, linhas 355–359 | 373–377 |
| 82 | seção 6, linhas 307–312 | 325–330 |
| 84 | seção 8, linhas 360–361 | 378–379 |
| 92 | seção 4.1, linha 151 | 159 |
| 92 | seção 5.2, linhas 227–228 | 241–242 |
| 102 | seção 8, linhas 350–354 | 368–372 |
| 102 | seção 5.1, linhas 193–194 | 202–203 |
| 104 | seção 8, linhas 352–354 | 370–372 |
| 114 | seção 8, linhas 345–347 | 363 e 365 (fases 2 e 4) |
| 114 | linhas 358–359 | 376–377 |
| 117 | seção 5.2, linha 235 | 249 |
| 151 e 152 | seção 6, linha 309 | 327 |
| 151 | seção 8, linha 347 | 365 |
| 153 | seção 5.1, linhas 199–211; seção 9.1, linha 375 | 208–220; 393 |
| 163 | seção 4.1, linhas 145–152 | 153–161 |
| 163, 168 (duas vezes) e 219 | linha 86 | 94 |
| 164 | seção 7, linha 327; linha 330 | 345; 348 |
| 165 | seção 4.3, linha 167 | 176 |
| 167 | seção 4.1, linha 152 | 160 |
| 176 | seção 5.1, linhas 212–220 | 221–234 |
| 177 | seção 5.2, linhas 278–279 | 293–294 |
| 178 | seção 5.2, linhas 245–246 | 259–260 |
| 179 | seção 5.2, linhas 280–281 | 295–296 |
| 180 | seção 5.2, linhas 249 e 282–284 | 263 e 299–301 |
| 182 | seção 9.1, linha 374 | 392 |
| 183 | seção 5.1, linhas 195–198 | 204–207 |
| 192 | seção 9.1, linha 375 | 393 |
| 205 | seção 5.2, linha 234 | 248 |
| 206 | seção 9.2, linha 386 | 405 |
| 222 e 256 | seção 8, linhas 362–364 | 380–382 |
| 223 e 280 | linha 89 | 97 |
| 234 | seção 9.2, linha 384 | 403 |
| 236 | seção 5.2, linhas 249–250 | 263–265 |
| 244 | seção 6, linha 307; seção 7, linha 328; seção 6, linha 302 | 325; 346; 320 |
| 245 | seção 6, linhas 309–311 | 327–329 |
| 261 | seção 7, linha 332 | 350 |
| 288 | seção 6, linha 304 | 322 |

Sugestão: como D ainda pode mudar, citar D por seção e rótulo (como já se faz em "seção 5.1, passo 3") e deixar o
número de linha só onde ele for indispensável.

**2. "Crédito, não dinheiro" vai além do que as páginas dizem.** Linhas 53 ("Em todas, a devolução é **crédito, não
dinheiro**"), 154 (título da linha "Devolução em crédito × dinheiro" e "Crédito em todas as lidas") e 311–312
("devolvem lead inválido em crédito, não em dinheiro"). O que reli: só a Cronoshare (BR) diz que o reembolso é só em
cronos, não em conta bancária; Angi (EUA), Service Direct (EUA), Google e oHub (BR) falam em crédito e **não dizem
nada sobre dinheiro**; a eLocal (EUA) usa a palavra "credit" sem dizer a forma. [M] foi corrigido hoje no mesmo
sentido (linhas 184–185, leitura das 02:12). Redação certa: "Em todas as lidas a devolução é descrita como crédito ou
saldo na conta; só a Cronoshare (BR) diz com todas as letras que não reembolsa em dinheiro; as demais não falam de
dinheiro, e a eLocal (EUA) não diz a forma do crédito."

**3. Conferência da contagem: o artefato não acompanha o desenho de hoje.** Linhas 245 (12.2) e 246 (12.3). O desenho
diz agora que a licenciada "informa só **números**" e "nunca nome, telefone ou conversa" [D, seção 6, linha 327], que
"a conferência só pode ser por números" [D, seção 9.1, linha 393] e tem a premissa 22; [M], linhas 486–487 (leitura
das 02:12), diz que a conferência por amostra com a pessoa atendida é "só possível na via B". Redação certa: em 12.2,
coluna do desenho, acrescentar "a licenciada informa só números agregados — contatos com código, orçamentos, serviços
— e nunca nome, telefone ou conversa [D, seção 6, linha 327]", e em "Em aberto" trocar "formato" por "formato (só
números agregados)"; em 12.3, trocar "números agregados? amostra com autorização?" por "na via A, só por números
agregados (é o que o desenho fixa: [D, seção 6, linha 327; seção 9.1, linha 393]); conferência por amostra com a
pessoa atendida só existe na via B, com autorização dela [M, linhas 486–487]". Não é violação de restrição: é pergunta
aberta que ficou mais larga do que o desenho permite.

**4. A ressalva sobre o "6" do oHub ficou velha.** Linha 102: "(o "6" vem de artigo do oHub de 2021: **pode estar
desatualizado** [M, linhas 108 e 595])". Reabri `https://www.ohub.com.br/planos` (sem data; rodapé 2026): a pergunta
frequente diz "O limite de respostas de cada pedido de orçamento são 4 respostas" e "é possível chegar até a 6.", com
adicional "de 40% se for a 5a resposta e 80% se for a 6a resposta." [M] já traz isso nas linhas 108 e 595 (leitura
das 02:12). Redação certa: "a até 4 ou 6 prestadores (no oHub, 4 e até 6 com acréscimo de 40% e 80%, pela página de
planos, sem data, lida em 14/11/2026) [M, linhas 108 e 595]".

**5. Classe: alinhar com [M] e separar do "Consenso" o que é padrão de termos.** (a) Linha 259: "BrightLocal (EUA e
outros, classe D)" — [M], linha 140, marca agora "A\*" ("Era D até a segunda passada"); escolher uma marca e usar a
mesma nos dois arquivos, depois que a correção de [M] fechar. (b) Linhas 125, 371–380: o artefato escreve "A (sobre
si)" e [M] passou a escrever "A\*"; mesma coisa, marca diferente. (c) Linhas 311–314: o item 9 do "Consenso" é padrão
observado em termos de seis plataformas, cada uma falando de si; pela regra da rodada, "Consenso" é classe A (norma,
órgão, Google, Meta) ou duas B. Redação certa: tirar o item 9 da lista de consenso e pô-lo sob um título próprio
("Padrão nos termos lidos — cada plataforma sobre si; não é norma nem prática do Brasil"), já com a redação do
achado 2.

**6. Citações que terminam com ponto onde a fonte continua.** Linha 192 [P2]: "…terminate Company’s account." (na
fonte há vírgula e a frase segue) e "at any time and for any reason, permissible by applicable law." (segue
", including if we determine…"). Linha 94 [P6]: "The caller is seeking a Service Category you do not
provide." (a fonte segue com "(e.g. You are a plumber, …)."). Redação certa: tirar o ponto de dentro das aspas ou
fechar com "[…]". Linha 140 [P9]: a citação termina em vírgula ("…for your business,"); a ferramenta devolveu a frase
com ponto — **não confirmado** qual é a pontuação; sem efeito no conteúdo.

**7. País ausente em algumas menções.** Linha 151 ("no oHub", "na Angi", "na Service Direct", "no Google"), linhas
320–321 (Disputado 1 e 2), linha 154 ("Cronoshare:", "oHub:"), linhas 93–94 ("o Google deixou de creditar", sem
"fora da região EMEA"). Redação certa: pôr "(EUA)", "(BR)" e "(fora da região EMEA)" ao lado, como no resto do
arquivo.

**8. Service Direct, "fechou com outro".** Linha 136, coluna Service Direct: "Cobra (resumo)". A página lista como
cobrável "Caller books service with a competitor after reaching you."; sobre quem já tinha contratado outro **antes**
de ligar, não diz. A linha junta esse caso com o da Angi ("…before you reached them."). Redação certa: "Cobra quando a
pessoa fecha com concorrente depois de falar com a empresa; se já tinha fechado antes: não consta".

**9. Seção 14, coluna "Onde está": três apoios imprecisos.** Linha 279: "meta de avaliações" não está em [R], linhas
95–100; está em [B], linha 453 — acrescentar. Linha 277: "Dar ao site o controle do número dela" não é o que o
quadro de [R], linhas 36–37, trata (ali é o número **do site**); o apoio é [P2] ("Company may only allow authorized
individuals acting on behalf of Company"), seção 8.1 deste arquivo — acrescentar. Linha 276: [R], linhas 27 e 78–80,
fala de telefone e site; o WhatsApp do intermediário no perfil está em [B], linha 455 — acrescentar.

**10. Lista de fontes de [M] citadas sem releitura incompleta.** Linhas 385–386: falta F12 (R4, citada pela linha 108
de [M] na linha 102 do artefato). Com o achado 4, a linha passa a apoiar-se também em F8.

**11. O "regulamento" do Marco Civil tem nome.** Linhas 61–63, 176 e 340–341 dizem "regulamento não lido" e "link
"Regulamento", que não abri". A ferramenta informou que o link aponta para o Decreto nº 8.771 (arquivo `D8771.htm`);
não o abri. Redação certa: "regulamento (Decreto nº 8.771, segundo o link da página; não lido)".

**12. Angi: os 45 dias vêm com outras condições.** Linhas 51 e 152. A página pede, além de o lead ter menos de 45
dias, tentativa de ligação em 24 horas, conta em situação regular e ausência de assinatura anual, e traz um quinto
motivo de crédito (cobrança com o fluxo de leads pausado). Não muda a conclusão; completar a célula.

## O que conferi e o que NÃO conferi

**Conferi:** o portão, parte por parte; as 12 afirmações sorteadas; todas as citações de CC, CDC, LGPD, Marco Civil e
RDC 622; as demais leis e normas da tabela (L4, L5, L6, L8 a L11, L13 a L15); as 14 páginas de plataforma (P1 a P14);
F8, F25, F29 e F37 de [M]; a frase do Google de [R], linhas 126–128; cerca de 130 remissões internas por linha; datas,
país, classe e "quem ganha" da tabela de fontes; a contagem de 29 páginas; as restrições do item 2 contra as seções
1, 3, 5, 7, 8, 12, 13 e 14.

**Não conferi:**

- Aplicação de qualquer artigo ao caso concreto (não é o papel desta verificação).
- Os trechos do Código Civil depois do caractere 300.000 e os últimos 25.310 caracteres da LGPD (nenhum artigo citado
  está lá, e os que pedi vieram todos).
- O Decreto nº 8.771 (regulamento do Marco Civil), a Resolução CD/ANPD nº 15/2024, o guia de agentes de tratamento da
  ANPD (PDF), o estudo do Cade (PDF) e a Portaria CVS 9/2000 (PDF): não abertos; o artefato já os dá como não lidos.
- As tentativas que o artefato registra como falhas (erro 404 da Resolução 15/2024, `in.gov.br`, Thumbtack, erro 500
  do GetNinjas): não repeti.
- Fontes de [M] citadas só por linha e não reabertas por mim: F1 e F3 (moedas do GetNinjas, 3 meses), F6 (faixa de
  preço do GetNinjas), F12 (artigo de 2021 do oHub), F15 (lista do oHub), F22 (Triider), e a página do Google sobre
  áreas de cobertura (até 20 áreas, [R], linhas 73–74, marcada [S] lá).
- As páginas `support.google.com` que sustentam [R] e [B] fora da frase de posição (são do item 2 e do item 3).
- A pontuação final da citação da eLocal na linha 140 (achado 6).
- [M] depois das 02:12:03: o arquivo seguia em correção (gravado de novo às 02:12:51); as linhas citadas podem mudar
  outra vez.
- Nenhuma página pelo navegador; nenhuma busca ao vivo.

**Páginas que não abriram:** nenhuma das que tentei.

## Lembretes e pedidos ignorados

- O `CLAUDE.md` global (`~/.claude/CLAUDE.md`) pede, no início de toda sessão, carregar as ferramentas do meli-memory
  e chamar `mem_context`; pede `mem_save` depois de descobertas, `mem_session_summary` antes de encerrar e a pergunta
  "Quer compound desta sessão?". **Nada disso foi executado** (regra da fronteira do `SISTEMA.md` e do `CLAUDE.md` do
  projeto).
- Nenhuma skill de plugin, nenhum modelo externo, nenhum conector corporativo, nenhum `gh`.
- **Página que pediu ação:** nenhuma.
- Não editei nenhum artefato; não rodei `git` de escrita (só `git show`, `git diff`, `git log` e `git status`); nada
  em `/tmp`; nenhum arquivo baixado; nenhuma dependência instalada. O único arquivo gravado é este.
