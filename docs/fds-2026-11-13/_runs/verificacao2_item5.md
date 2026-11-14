# Segunda passada do item 5 — modelos de negócio (verificação independente)

- **Quem:** revisor em contexto limpo (subagente), sem acesso à conclusão de ninguém. Não abri nenhum arquivo de nome
  `verificacao*` nem `correcoes*` em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` e ignorei o que
  o próprio artefato diz sobre verificações anteriores (linhas 5–9).
- **Quando:** sábado, 14/11/2026, das 01:22 às 01:37 (Brasília, lido de `TZ=America/Sao_Paulo date`). Todas as páginas
  da web citadas abaixo foram lidas nessa janela.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (792 linhas, lido inteiro; última
  alteração no git: 13/11/2026, 22:20).
- **Como li a web:** só a ferramenta de leitura de página pública e a de busca (uma busca, termos genéricos). Sem
  navegador, sem busca ao vivo no Google, sem conta, sem formulário, sem contato. **Limite:** a ferramenta resume a
  página por um modelo pequeno e corta citação em cerca de 125 caracteres; "confere" abaixo quer dizer que o trecho
  pedido voltou com aquelas palavras, não que eu vi o HTML.
- **Natureza:** conferência de fonte e de conta. O que encosta em norma é levantamento com fonte, não parecer.

## Veredito: APROVADO COM RESSALVAS

- Sorteio: **0 falha em 12** (limite: 2).
- Fora do sorteio reabri 39 das 40 fontes da tabela da seção 9 (F1 a F35 e F37 a F40; só F36 ficou de fora, porque
  não tem uso no texto) e todas as remissões a arquivos do projeto. Nenhum número de preço está errado; todas as
  contas fecham.
- As ressalvas: duas de portão (achados 1 e 2), duas de classe de evidência (3 e 4), três de coerência com arquivos
  que mudaram depois das 22:20 de 13/11 (10, 11 e 12) e treze menores. Nenhuma muda a conclusão do artefato.

---

## 1. O que abri

**Arquivos do projeto (leitura):**
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` (linhas 29–118);
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linhas 33–47 e 63–64);
`/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (inteiro);
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (inteiro, 499 linhas);
`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (inteiro, 442 linhas);
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (inteiro, 563 linhas);
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md` (tabela "Resultados por classe");
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (linhas 1–45);
`/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` e
`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (contas refeitas em Python, só leitura);
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` (linhas 150–168 e títulos);
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` (linhas 362–370, 442 e títulos);
`/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md` (linhas 13–16, 42, 60–92, 102–108, 165, 167);
`/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md` (linhas 118–131, 138–146, 246–249);
`/home/ancastelo/pessoal/SEO_Project/research/04_mao_de_obra_custos_operacao.md` (linhas 226–240);
`/home/ancastelo/pessoal/SEO_Project/data/servicos.csv` (linhas 1, 2, 6–10, 17, 18);
`/home/ancastelo/pessoal/SEO_Project/arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` (linhas 48–53).
Histórico: `git log` (só leitura) dos arquivos acima.

**Páginas da web:** as da seção 4 deste relatório.

---

## 2. O portão, parte por parte

| Parte do portão | Situação | Onde |
|---|---|---|
| Primeiro os modelos que não dependem de perfil próprio nem de se passar por dedetizadora | **Cumprido.** Seções 2 (Parte 1) e 4.1 a 4.7 vêm antes da seção 5 | linhas 70–80 e 149–506 |
| Os quatro modelos nomeados no portão | **Cumprido:** 4.1 site de conteúdo e comparação; 4.2 pagamento por lead; 4.3 exclusividade por região; 4.4 gestão do perfil e do site da licenciada. Há três a mais (4.5 destaque pago, 4.6 forma de cobrança, 4.7 comissão) | linhas 192–506 |
| Depois os que dependem, marcados com o veredito do item 2 | **Cumprido.** 5.1 a 5.7, cada um com o veredito no título e a linha do item 2 | linhas 510–586 |
| Para cada um: como opera | Parte 1: **cumprido** nos sete. Parte 2: **só implícito** (ver achado 1) | — |
| Para cada um: as contas, com país e classe de cada número | Parte 1: **cumprido** nos sete, só do lado da receita (achado 16). Parte 2: **ausente**, salvo a remissão a R27 em 5.4 (achado 1) | — |
| Para cada um: precificação por praga, residência × empresa, exclusivo × compartilhado | Parte 1: **cumprido** nos sete, com os três recortes e "não sei" onde não há fonte. Parte 2: **ausente** (achado 1) | — |
| Para cada um: os cinco riscos (Google, propaganda, LGPD, WhatsApp, parceiro) | Parte 1: **cumprido** (tabela comum em 4.0 e uma por modelo). Parte 2: só o risco que o veredito traz (achado 1) | — |
| O valor do lead da pesquisa antiga é confirmado ou derrubado, com fonte | **Cumprido na fonte, não na letra.** A seção 7 reabre afirmação por afirmação, com fonte, e conclui "não dá para confirmar — nem para derrubar". O portão pede uma de duas respostas (achado 2) | linhas 605–648 |

### 2.1 Vereditos do item 2, comparados um a um

Comparei cada veredito citado no artefato com o "Quadro de vereditos" e as seções de
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` como está hoje (499 linhas, a mesma contagem que o
artefato declara na linha 26).

| Modelo (artefato) | Veredito que o artefato dá | Item 2 hoje | Confere? |
|---|---|---|---|
| 1.1 / 4.1 site que identifica as licenciadas | Permitido com condição (linha 30) | linha 30: "**Permitido com condição** (identificar a executora e a licença; sem termos vedados; site declarado intermediário)" | sim, literal |
| 1.2 / 4.2 pagamento por lead | LGPD uma empresa e várias: permitido com condição (33 e 34); botão: permitido com condição (38) | linhas 33, 34 e 38: os três "Permitido com condição"; 34 com "as mesmas, mais: dizer a quantas…" | sim |
| 1.2, via B (formulário) | "o item 2 marca isso como inferência" (linhas 442–446) | linhas 442–446: "Variante … (inferência, não frase da fonte)" | sim |
| 1.3 / 4.3 exclusividade | linha 33 + 38 + 30; citação das linhas 257–258 | linhas 257–258: "Um desenho em que **toda** página de oferta nomeia a licenciada que atende aquela região cumpre as condições" | sim, literal |
| 1.4 / 4.4 gestão do perfil | Permitido com condição (linha 28) | linha 28: "**Permitido com condição**" | sim, literal |
| 1.5 / 4.5 destaque pago | linha 30 + marca de publicidade (linhas 233–235) | linhas 234–235: "a marca de publicidade onde a posição ou o destaque for pago (CDC, art. 36)" | sim, literal |
| 1.6 e 1.7 | "os de 1.2"; item 2 sem linha para forma de cobrança e para comissão | o quadro não tem linha para isso | sim |
| 2.1 / 5.1 perfil próprio | Vedado (linhas 25–26) | linhas 25 e 26: "**Vedado**" | sim |
| 2.2 / 5.2 site com cara de dedetizadora | Não conclusivo, "é o ponto de maior risco" (linha 31) | linha 31: "**Não conclusivo** (norma silente; é o ponto de maior risco)" | sim, literal |
| 2.3 / 5.3 central de WhatsApp | API: vedado; aplicativo: não conclusivo (36–37) | linha 36: "**Vedado** pela letra dos termos da Meta (leitura literal…)"; linha 37: "**Não conclusivo**" | sim |
| 2.4 / 5.4 aluguel de site com perfil | Vedado (linha 27; linhas 133–134) | linha 27: "**Vedado**"; linha 134: "perfil "alugado" cuja propriedade fica com o intermediário" | sim |
| 2.5a / 5.5 compra de avaliações | Vedado (linha 29; 95–100) | linha 29: "**Vedado**"; linhas 95–100 | sim |
| 2.5b compra de links | fora do item 2; política de spam, classe A | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, linha 164: "Buying or selling links for ranking purposes." | sim, literal |
| 2.6 / 5.6 mesmo contato a várias sem a pessoa saber | Vedado pela letra da lei (linhas 358–364) | linhas 361–362: "**Vedado** pela letra da lei: repassar sem informar; repassar com autorização genérica ("aceito os termos")" | sim, literal |
| 2.7 / 5.7 cobrar do consumidor e subcontratar | sem linha no quadro; arts. 5º e 21 apontam contra (184–185; 246–251) | linhas 184–185 e 246–251 | sim; o artefato diz que é leitura dele ("trato como não conclusivo") |

As 14 linhas do quadro (25 a 38) aparecem no artefato, cada uma no modelo certo (a 32 em 4.0, a 35 em 4.2). **Nenhum
veredito foi trocado, amolecido nem endurecido.** Conferi também, uma a uma durante a leitura, as remissões a
intervalos de linhas do item 2 espalhadas pelas seções 4 e 5: todas caem no trecho que dizem.

---

## 3. Sorteio de 12 afirmações com fonte

**Como sorteei:** numerei 68 afirmações com fonte, na ordem em que aparecem (R1 a R28 da seção 3, desdobradas onde a
linha traz duas fontes; as linhas da tabela 4.0.1; as citações soltas das seções 4 a 8; as datas da tabela da seção
9). Semente `verificacao2-item5-20261114`, em Python: `random.seed(semente); sorted(random.sample(range(1, 69), 12))`.
Saíram 11, 12, 15, 19, 23, 35, 37, 38, 48, 52, 58 e 65.

| Nº | Afirmação (linha do artefato) | Fonte reaberta | Existe? | Diz aquilo? | Data, país, número | Resultado |
|---|---|---|---|---|---|---|
| 11 | R9: moeda do GetNinjas vale 3 meses (linha 113) | F1 https://www.getninjas.com.br/termos-de-uso e F3 https://www.getninjas.com.br/central-de-ajuda/profissional/pagamento/o-que-sao-moedas | sim | sim: cláusula 9.b, "validade de 3 (três) meses a partir do momento da aquisição"; a ajuda diz 3 meses | sem data; rodapé dos termos "©2011-2024"; Brasil | confere |
| 12 | R10: "se um lead já foi comprado por outros profissionais, nós cobramos menos" (linha 114) | F7 https://monitormercantil.com.br/getninjas-ninj3-modelo-de-negocio-operacao-e-perspectivas/ | sim | sim, literal; o entrevistado é o diretor financeiro | 24/08/2023 (atualizada em 25/08); Brasil | confere |
| 15 | R13: Cronoshare devolve a parte de comissão em saldo; "Não reembolsamos valores pagos em sua conta bancária."; sem percentual nem prazo (linha 117) | F20 https://www.cronoshare.com.br/devolucoes | sim | sim: "recuperar a comissão, que faz parte do saldo investido em cada contato"; a frase do reembolso é literal; gastos de gestão "só … em alguns casos" | sem data (rodapé 2012-2026); Brasil; sem percentual e sem prazo | confere |
| 19 | R17: tickets por praga, mínimo / base / máximo (linha 126) | `/home/ancastelo/pessoal/SEO_Project/data/servicos.csv`, linhas 2 e 6–10; `/home/ancastelo/pessoal/SEO_Project/research/02_mercado_servicos_precos.md`, linhas 124–128 e 248 | sim | sim: 150/280/450; 200/400/700; 250/500/900; 300/700/1.200; 400/750/1.500; 800/1.800/4.000; a linha 248 diz que são "material de SEO … não preço efetivamente praticado" | pesquisa de 25/09; Brasil, São Paulo | confere |
| 23 | R21: "$24.99 each — inbound and never shared with another company" (linha 135) | F31 https://99calls.com/locations/Minnesota/Pest-Control-Leads.htm | sim | sim, literal | "Last updated October 2026" (outra seção da página traz "June 2026"); EUA | confere |
| 35 | Angi: crédito abatido de "future lead charges"; a página não fala em pagamento adiantado (linha 187) | F30 https://intercom.help/angi/en/articles/11403440-how-to-request-a-lead-credit-for-an-invalid-lead | sim | sim: "Credits issued to an account are automatically applied toward future lead charges."; nenhuma menção a pagamento adiantado | 14/08/2026; EUA | confere |
| 37 | oHub: "A ordem desta lista considera fatores como volume de respostas na plataforma" (linha 229) | F15 https://www.ohub.com.br/empresas/dedetizacao/sp/sao-paulo | sim | sim, literal (a frase segue com tempo de cadastro e avaliações) | a página traz "com dados atualizados em Novembro de 2026" — o artefato diz "sem data" (achado 7, fora da afirmação sorteada); Brasil | confere |
| 38 | Agência dos EUA dá cupim e percevejo acima de pragas gerais, sem fonte (linhas 291–292) | F34 https://cubecreative.design/blog/pest-control-marketing/cost-per-lead-2026 | sim | sim: faixas maiores para cupim e percevejo que para pragas gerais; o artigo não cita fonte para elas ("our estimates from client accounts and public data") | 14/01/2026; EUA | confere |
| 48 | GetNinjas desconta as moedas vencidas (linha 474) | F3 (endereço acima) | sim | sim: "as Moedas vencidas serão descontadas da conta do Anunciante" | sem data; Brasil | confere |
| 52 | O caso de Nova York incluiu um perfil no mapa criado pelo dono do site e vendido junto (linhas 554–555) | F38 https://mikebonadio.com/rank-and-rent/ | sim | sim: a venda incluiu "the site and a supplementary GMB I built in the latter months" | 26/08/2025; caso "from 2015-ish"; EUA, Nova York | confere |
| 58 | PedeGás: o pedido vai direto ao WhatsApp do parceiro (linha 599) | F25 https://pedegas.com/parceiro | sim | sim: "WhatsApp direto com o cliente"; o campo de WhatsApp é o "Número que recebe os pedidos" | sem data (rodapé 2026); Brasil | confere |
| 65 | F13 traz "Última atualização em Outubro 17, 2024" (linha 727) | https://ajuda.ohub.com.br/article/58-o-que-sao-os-creditos-do-ohub | sim | sim | 17/10/2024; Brasil | confere |

**Falhas: 0 em 12.**

---

## 4. Fontes de preço de lead e de plataforma brasileira reabertas (todas)

Leitura em 14/11/2026, entre 01:23 e 01:33 (Brasília).

| Fonte | Endereço | O que o artefato tira dela | Reaberta: o que voltou | Resultado |
|---|---|---|---|---|
| F1 | https://www.getninjas.com.br/termos-de-uso | validade de 3 meses; preço varia por "local, tipo e oferta de orçamentos"; "pelo insucesso de uma eventual negociação"; rodapé "©2011-2024" | tudo literal (cláusulas 9.b, 7.d, 5.c). A mais: cláusula 9.a, moedas adquiridas "não serão devolvidas ao Anunciante ou convertidas em moeda corrente"; cláusula 15.b.i, devolução de moedas quando uma suspensão é revertida (resumo da ferramenta) | confere; dado a mais no achado 8 |
| F2 | https://www.getninjas.com.br/central-de-ajuda/profissional/pedidos-sou-profissional/como-funciona-a-precificacao-dos-pedidos | "Os valores dos pedidos não são fixos e podem variar de acordo com o tipo de serviço"; sem valor | literal; nenhum valor em moedas ou reais; sem data | confere |
| F3 | https://www.getninjas.com.br/central-de-ajuda/profissional/pagamento/o-que-sao-moedas | 3 meses; moedas vencidas descontadas | confere (sorteio 11 e 48) | confere |
| F4 | https://www.getninjas.com.br/central-de-ajuda/profissional/pedidos/como-funcionam-os-pedidos | "do primeiro ao quarto", sem afirmar o limite | "Ordem de liberação (Podendo ser do primeiro ao quarto)"; o artigo não diz o máximo | confere |
| F5 | https://blog.getninjas.com.br/como-funcionam-as-moedas-do-getninjas/ | 500 moedas por R$ 69,90; até 4.800 moedas; 4 profissionais numa seção e 3 em outra; criado em 24/04/2024, atualizado em 09/09/2025 | as quatro frases literais; as duas datas | confere |
| F6 | https://www.getninjas.com.br/reformas-e-reparos/dedetizador/sp/sao-paulo | "Em geral, os preços podem variar entre R$ 150 a R$ 600."; "verifique se possuem licença e certificação" é conselho ao cliente | literal; a página não exige licença | confere; classe no achado 4 |
| F7 | https://monitormercantil.com.br/getninjas-ninj3-modelo-de-negocio-operacao-e-perspectivas/ | sorteio 12 | confere | confere |
| F8 | https://www.ohub.com.br/planos | pacotes 100 / 180 / 240 / 420 créditos por R$ 172 / 298 / 392 / 682; 12 meses; devolução de 100%; premium de 20% a 100%; assinatura de 1 ou 3 meses sem preço | tudo literal. **A mais:** a seção de perguntas frequentes da própria página diz "O limite de respostas de cada pedido de orçamento são 4 respostas mas é possível chegar até a 6", com adicional "de 40% se for a 5a resposta e 80% se for a 6a resposta" | confere; achado 5 |
| F9 | https://www.ohub.com.br/creditos_por_categoria.php | "Dedetização" e "Dedetização e Desratização": "De 12 a 24 créditos" | literal nas duas. A página traz também "De 10 a 20 respostas no plano G" para as duas categorias — bate com o pacote de 240 créditos (240 ÷ 24 = 10; 240 ÷ 12 = 20): confirma que os créditos são por resposta | confere |
| F10 | https://www.ohub.com.br/ajuda | "empresas que estão precisando de um fornecedor de serviço B2B" | literal | confere |
| F11 | https://ajuda.ohub.com.br/article/150-planos | data de 09/01/2026; assinatura "de 1 ou 3 meses" (linha 458) | data confere. O artigo **não** diz 1 ou 3 meses: diz que a assinatura ("oHub Plus") tem "recorrência mensal, bimestral, trimestral e semestral"; planos pré-pagos P, M, G e GG; saldo válido por 365 dias; sem preço | data confere; texto diverge (achado 6) |
| F12 | https://ajuda.ohub.com.br/article/61-qual-o-limite-de-respostas-por-oportunidade | "até 4 (quatro) respostas na quantidade original de créditos"; "mais 2 fornecedores podem responder com um adicional de 40% e 80%"; 19/03/2021 | literal; data confere | confere |
| F13 | https://ajuda.ohub.com.br/article/58-o-que-sao-os-creditos-do-ohub | sorteio 65 | confere | confere |
| F14 | https://ajuda.ohub.com.br/article/63-o-que-e-uma-oportunidade-premium | 20% a 100%; "tamanho da empresa e nível de interesse de contratação"; empresa ou condomínio; 19/03/2021 | "um adicional de 20%, 40%, 60%, 80% ou 100%"; "o tamanho da empresa e nível de interesse de contratação"; "seja empresa ou condomínio"; data confere | confere |
| F15 | https://www.ohub.com.br/empresas/dedetizacao/sp/sao-paulo | ordem da lista; "recebe até 4 propostas personalizadas"; 262 fornecedores; lista sem número de licença; "sem data" | os quatro conferem; a página traz "com dados atualizados em Novembro de 2026" | confere, salvo a data (achado 7) |
| F16 | https://www.ohub.com.br/anunciar | (só entra no intervalo "F8–F16" da linha 595) | cadastro gratuito, compra de créditos, "Não é necessário pagar mensalidade"; nenhuma menção a destaque pago | coerente com a linha 427 |
| F17 | https://monitormercantil.com.br/ohub-marketplace-b2b-de-servicos-e-modelo-de-operacao/ | 20/09/2023; "de R$ 10 a R$ 340" por pedido; não usado nas contas | literal; entrevistado é o fundador; data confere | confere |
| F18 | https://suporte.cronoshare.com.br/hc/pt-br/articles/360006135593-Quanto-custa-em-cronos-contatar-um-cliente | "varia de 2% a 15% do seu orçamento total, sendo uma média de 6% para cada novo cliente"; 23/07/2025 | literal; data confere. **A mais:** exemplo da página — limpeza pontual, "Custo do serviço total = R$120 . Comissão em cronos estimada: 50 cronos, R$ 5,00 (uns 4% aproximadamente)" | confere; dado a mais no achado 9 |
| F19 | https://www.cronoshare.com.br/atencao-ao-cliente/cronos-para-contactar-clientes | "nunca é superior aos 15% do que você cobrará"; "entre 6 e 10% por cada cliente novo" | literal nas duas; sem data | confere |
| F20 | https://www.cronoshare.com.br/devolucoes | sorteio 15 | confere | confere |
| F21 | https://www.cronoshare.com.br/como-trabalhar | "Podem contactar no máximo 4 profissionais para cada solicitação." | literal | confere |
| F22 | https://www.triider.com.br/termos-e-condicoes/ | 21% a 25% na modalidade pós-paga; cliente paga pela plataforma; "em nenhuma hipótese será responsável solidário ou subsidiário pela garantia"; 28/02/2025 | cláusula 6.1.5 literal; cláusula 6.1.1 (pagamento "exclusivamente através dos meios de pagamento disponíveis na PLATAFORMA"); cláusula 11.1 literal; data confere | confere |
| F23 | https://www.triider.com.br/seja-um-profissional/ | dedetização não consta | não consta. A página cita também uma modalidade pré-paga, sem detalhe | confere; achado 17 |
| F24 | https://startups.com.br/negocios/triider-da-juntos-somos-mais-compra-a-operacao-da-habitissimo-no-brasil/ | compra da operação brasileira em 2021; 06/07/2021 | confere | confere |
| F25 | https://pedegas.com/parceiro | R$ 0, R$ 99 e R$ 199 por mês; "Prioridade na lista"; "Topo em todas as cidades que você atende." | literal; a página lista "Dedetização e Controle de Pragas" e "Dedetização Comercial" entre os serviços | confere |
| F26 | https://pedegas.com/orcamento/dedetizacao-comercial/sao-paulo-sp/ | "Plataforma de intermediação de pedidos"; não nomeia as empresas | literal; nenhuma empresa nomeada; nenhum número de licença | confere |
| F27 | https://www.guiamais.com.br/institucional/ajuda | "O GuiaMais não está trabalhando mais com cadastros gratuitos"; sem preço | literal; sem preço | confere |
| F28 | https://support.google.com/localservices/answer/6224841?hl=en e `?hl=pt-BR` | seletor com 11 países; o Brasil não está; sem frase de indisponibilidade | os mesmos 11 nas duas línguas; Brasil ausente; Países Baixos ausentes; nenhuma frase de indisponibilidade por país | confere |
| F29 | https://support.google.com/localservices/answer/7195435?hl=en | "You're charged for each valid lead…"; reavaliação e crédito automático; "over a 30-day period"; 15 dias; exclusão do Espaço Econômico Europeu e da região EMEA | as cinco frases conferem | confere |
| F30 | https://intercom.help/angi/en/articles/11403440-how-to-request-a-lead-credit-for-an-invalid-lead | motivos de crédito e de recusa; 45 dias; seis meses; 14/08/2026 | tudo literal; data confere | confere |
| F31 | https://99calls.com/locations/Minnesota/Pest-Control-Leads.htm | sorteio 23 | confere | confere |
| F32 | https://blog.servicedirect.com/how-much-do-service-direct-pest-control-leads-cost | "around $55", média nacional, 1º trimestre de 2023, ligação exclusiva; 31/03/2023 | literal; "we only offer exclusive phone leads"; data confere | confere |
| F33 | https://callscaler.com/marketplace/pest-control | "$15–$45 per qualified inbound call"; "typically 60-120 seconds"; país não declarado | literal; a página fala do mercado dos EUA sem dizer onde opera | confere |
| F34 | https://cubecreative.design/blog/pest-control-marketing/cost-per-lead-2026 | "$22 to $65, with a $38 median, across 600 accounts", de segunda mão; 14/01/2026 | literal; o artigo atribui o número à base de outra empresa | confere |
| F35 | https://elevarus.com/buy-pest-control-leads-exclusive-vs-shared-attach-rate/ | "A $38 shared pest lead and an $85 exclusive lead"; "within three points"; 28% e 30%; "worked example"; 23/05/2026 | tudo literal; nenhum número do exemplo tem fonte | confere |
| F37 | https://www.brightlocal.com/local-seo-services/ | "$499 per location/month" e "$1,299 per location/month"; EUA, Reino Unido, Canadá, Austrália | literal; os quatro países | confere |
| F38 | https://mikebonadio.com/rank-and-rent/ | "$45K/year"; "about 8 leads/day"; venda por 90 mil dólares; "He stopped paying, so I stopped sending."; 26/08/2025 | tudo confere (a página escreve "$90,000") | confere |
| F39 | https://raventools.com/blog/rank-and-rent-seo/ | "24-36x the average monthly rental amount"; abril de 2019 | literal; data confere; país não declarado | confere |
| F40 | https://advivo.com.br/marketing/google-ads-para-dedetizadora/ | sem valor de custo por clique; 04/12/2025 | nenhum valor em reais; data confere | confere |

**Fontes da seção 10 que testei de novo:** a página de reembolso de moedas do GetNinjas devolveu erro 500 outra vez; a
ajuda da Bark devolveu erro 403 outra vez; `https://www.habitissimo.com.br/` devolveu de novo erro de certificado (o
certificado apresentado é de outro domínio — pode ser efeito da rede desta máquina; não testei de outra rede).

**Uma busca na web** ("quantas moedas custa liberar pedido de dedetização no GetNinjas", termos genéricos): nenhum
resultado traz o preço em moedas ou em reais de um pedido de dedetização. Coerente com R7 ("não publicado").

**Segunda fonte do custo por clique da pesquisa antiga, que o artefato não reabriu:**
https://www.digitallevolution.com.br/blog/google-ads-cpc-o-que-e-como-funciona-e-como-reduzir-seus-custos-em-2025
(28/05/2025; agência; classe D; Brasil). Só traz valores ilustrativos num exemplo de "advogado em São Paulo"
("R$ 0,50, R$ 5,00 ou até R$ 50,00"); nada sobre dedetização. Reforça o "não confirmado" da linha 629 (achado 15).

---

## 5. Classe de evidência e "quem ganha"

- **Toda fonte tem classe e "quem ganha"** (tabela da seção 9, 40 linhas). Nenhuma fonte sem classe.
- **Regra apoiada só em C ou D:** não achei. Os números D (EUA) aparecem como "só estrutura", fora das contas; os
  dois C (entrevistas de executivos, F7 e F17) não sustentam nenhuma conta nem nenhum item de "Consenso"; a única
  recomendação de desenho ("de preferência adiantado", linha 250) apoia-se em páginas das próprias plataformas.
- **Número dos EUA em conta brasileira:** não há. As contas de 4.1 a 4.7 usam só `PREMISSA`, `HIPÓTESE 25/09` em reais
  e dois números brasileiros de página de plataforma (R3 e R15). Os dólares de 4.3 e 4.4 vêm marcados "só estrutura".
- **Dois problemas de classe** (achados 3 e 4):
  1. A classe A do artefato inclui "a página pública de preço ou de termos de uma plataforma sobre ela mesma"
     (linhas 18–19). Isso **não está** na regra da rodada
     (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 40: "Google, Meta/WhatsApp, lei,
     norma, órgão regulador"). A extensão é declarada e defensável (a tabela de preço de uma empresa é a fonte
     primária do preço dela), mas é aplicada de forma **desigual**: a tabela de preço do oHub, do PedeGás e do
     GetNinjas entra como A; a tabela de preço do vendedor de leads dos EUA (R21, F31) e a da empresa de gestão de
     perfil (R26, F37) entram como D, com a mesma descrição ("preço de tabela do próprio vendedor"). Quatro itens de
     "Consenso" (seção 8, itens 4 a 7) dependem dessa extensão.
  2. R20 (linha 129) e F6 (linha 720) classificam como A a faixa "R$ 150 a R$ 600" que o GetNinjas dá para o serviço
     de dedetização. Não é a plataforma falando do próprio preço: é uma estimativa dela sobre o preço de terceiros,
     sem método, numa página feita para captar busca. Pelo critério que o próprio artefato aplicou à Cronoshare (R11:
     "D — estimativa da plataforma…; não é tabela de preço"), é D.

---

## 6. Contas refeitas

Todas refeitas em Python a partir dos números de entrada escritos no artefato. **Todas fecham.**

| Onde | Conta | Entradas ditas? | Refeita | Marca de ilustração? |
|---|---|---|---|---|
| R2 (linha 106) | preço do crédito do oHub | sim | 172 ÷ 100 = 1,72; 298 ÷ 180 = 1,656; 392 ÷ 240 = 1,633; 682 ÷ 420 = 1,624 → R$ 1,62 a R$ 1,72 | "cálculo meu" |
| R3 (linha 107) | resposta de dedetização no oHub | sim | 12 × 1,624 = 19,49; 12 × 1,72 = 20,64; 24 × 1,624 = 38,97; 24 × 1,72 = 41,28 | "cálculo meu" |
| R6 (linha 110) | preço da moeda do GetNinjas | sim | 69,90 ÷ 500 = 0,1398 → R$ 0,14 | "cálculo meu" |
| 4.1 (linha 211) | contatos por mês | sim | 2.000 × 3% = 60 | `PREMISSA` nos dois; "não é previsão" |
| 4.2 (linhas 260–264) | receita por unidade | sim | 30, 100 e 300 unidades × R$ 20 e R$ 40 = 600 / 1.200; 2.000 / 4.000; 6.000 / 12.000 | `PREMISSA`; R$ 20 e 40 marcados como R3 arredondado e "outro produto" |
| 4.2 (linhas 275–282) | teto por praga | sim | ticket × 30% × 15% e × 30%: 12,60 / 25,20; 18 / 36; 22,50 / 45; 31,50 / 63; 33,75 / 67,50; 81 / 162. Com 10%: baratas 4,20 / 8,40 | ticket `HIPÓTESE 25/09`, classe D; 30%, 15% e 10% `PREMISSA`, "arbitrário" |
| 4.2 (linhas 284–285) | margem zerada | sim | 131 × 30% = 39,30 → R$ 39 | `HIPÓTESE 25/09` |
| 4.2 (linhas 296–297) | quatro respostas de 12 créditos | sim | 4 × 19,49 = 77,94; 4 × 20,64 = 82,56 → R$ 78 a R$ 83 | "cálculo meu" |
| 4.3 (linhas 335–337) | mensalidade máxima | sim | 40 × 30% × 280 × 15% = 504; com 10%: 168 | `PREMISSA` ×3; ticket `HIPÓTESE 25/09` |
| 4.4 (linha 384) | gestão | sim | 3 × 600 = 1.800 | `PREMISSA` ×2 |
| 4.5 (linha 424) | destaque | sim | 5 × 99 = 495 | 5 é `PREMISSA`; R$ 99 é R15 (Brasil, página da plataforma, outro ramo), dito "não é preço de mercado de dedetização" |
| 4.6 (linhas 461–462) | pré-pago | sim | 4 × 300 = 1.200 | `PREMISSA` ×2 |
| 4.7 (linhas 490–491) | comissão | sim | 20 × 280 × 10% = 560 | `PREMISSA` ×2; ticket `HIPÓTESE 25/09` |
| 7 (linha 618) | conta da linha 82 da pesquisa antiga | sim | 350 × 35% × 15% = 18,38; × 20% = 24,50; × 30% = 36,75 → "R$ 18 a R$ 37" | reconstituição dita |
| 7 (linhas 618–619) | de onde sai o teto de R$ 60 | sim | 650 × 45% × 20% = 58,50 | "reconstituição minha" |
| 7 (linhas 625 e 636) | Cronoshare sobre R$ 280 | sim | 6% = 16,80; 10% = 28; 15% = 42 → "R$ 17 a R$ 28 e até R$ 42" | "cálculo meu"; ticket-hipótese |
| 7 (linha 639) | teto de baratas | sim | 12,60 e 25,20 → "R$ 13 a R$ 25" | ilustrativo |
| 4.0 e 1.7 | 39% dos orgânicos nos 10 domínios; 43% das linhas do mapa em três perfis | sim | 275 ÷ 709 = 38,8%; 86 ÷ 202 = 42,6% (refeito em `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, grupos A a G) | observação da amostra |
| 5.2 (linhas 532–534) | 7%, 13% e 19% dos 709 | sim | 51 ÷ 709 = 7,2%; 93 ÷ 709 = 13,1%; 138 ÷ 709 = 19,5% (o mapa de busca escreve 19%); 12 de 67 confere em `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` (11 da classe "empresa com número de licença" + 1 domínio satélite) | observação da amostra |

**Limite das contas, não erro:** nenhuma tem lado de custo (o artefato diz na linha 215 que domínio, hospedagem e
horas não foram levantados). São contas de receita e de teto de preço, não de resultado (achado 16).

**Uma conta que falta na seção 7:** o artefato mostra que o teto de R$ 60 só sai juntando os extremos da linha 15 da
pesquisa antiga; não diz que o **piso** de R$ 20 também não sai deles — o extremo de baixo dá 230 × 30% × 10% =
R$ 6,90 (achado 20).

---

## 7. O que a fonte não sustenta

Procurei promessa de receita, "o mercado paga", causa sem dado e afirmação sobre empresa nomeada.

- **Promessa de receita:** não há. Toda conta leva "não é previsão"; a receita "realista" da pesquisa antiga fica "sem
  confirmação" (linhas 647–648).
- **"O mercado paga":** não há. As linhas 60–61, 300–301, 385–386 e 691 dizem "não sei".
- **Empresa nomeada:** o que se diz de GetNinjas, oHub, Cronoshare, Triider, PedeGás, GuiaMais, Angi e Google está nas
  páginas delas (seção 4 acima). As linhas 574–575 dizem expressamente que nada se afirma sobre a conformidade de
  nenhuma plataforma; as linhas 585–586 separam cláusula do Triider de texto de lei. Nenhuma pessoa física é nomeada.
- **Frases sem apoio, todas pequenas** (achado 14): "O caso mais citado do método" (linha 554) — nenhuma fonte mede
  qual caso é o mais citado; "O risco que mais pesa" (linha 52) — é juízo, sem a marca "leitura minha" que o item 9
  da mesma lista leva; "quase todos de dedetizadoras" (linha 53) — dos 10 domínios, 9 são sites que se apresentam
  como dedetizadora, e só 2 deles mostram número de licença; o décimo é o diretório.
- **Afirmação mais forte que a fonte** (achado 19): "devolvem … em crédito ou saldo, não em dinheiro" (linhas 55–56,
  184 e 668). Que a devolução é em crédito está nas quatro páginas; que **não** é em dinheiro só a Cronoshare diz
  com todas as letras.
- **Conferência impossível na via A** (achado 13): 4.7 propõe conferir o fechamento "por amostra, com a própria pessoa
  atendida" (linhas 486–487), mas na via A o site não tem o contato da pessoa (linhas 156–157 do próprio artefato).
- **Gestão do site da licenciada** (achado 18): a frase que o item 2 cita é "Website content must be owned and
  managed by the business owner." (linha 117 do item 2). O artefato trata "o site continua sendo dela" como
  suficiente (linhas 372 e 375); se um terceiro autorizado escrever o conteúdo atende a "managed by the business
  owner" não foi levantado no item 2.

---

## 8. Coerência com o desenho e com o mapa de busca, como estão hoje

O artefato foi alterado pela última vez em 13/11/2026 às 22:20.
`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` e os dois CSV mudaram depois (14/11, 00:08 e 01:11);
`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` foi escrito depois do artefato (primeira versão às 22:02,
alterado até 23:44).

**Mapa de busca — números citados pelo artefato, conferidos no arquivo e refeitos nos CSV de hoje:**

| Número no artefato | Linha | No mapa de busca hoje | Confere? |
|---|---|---|---|
| 709 orgânicos, 157 domínios, 10 domínios com 39% | 52–53, 166 | seção 4.1; CSV, grupos A a G | sim |
| ohub.com.br em 21 buscas, posição mediana 5 | 166, 228 | seção 4.4; CSV | sim |
| resumo de IA em 73, anúncio de texto em 60, perfil patrocinado em 47, bloco de mapa em 68 | 166, 521 | seção 3; CSV | sim |
| um mesmo anunciante como perfil patrocinado em 47 | 53–54, 166 | seção 6 ("sempre o mesmo"); CSV | sim |
| 64 perfis, três com 43% das linhas | 166 | seção 5; CSV | sim |
| 14 domínios satélite (51; 7%), 15 marcas sem identificação (93; 13%), 11 com licença (138; 19%), 12 de 67 | 532–535 | seção 7.2 e `serp_sp_dominios.md`, linhas 8–19; CSV | sim |
| "seção 4.4" e "seção 1, item 4" | 228, 536 | existem e dizem aquilo | sim |
| coluna `volume` = "não medido" | 212–213 | 2.721 linhas, todas "não medido" | sim |

**O que ficou velho no artefato** (achados 10 e 11):
1. Linhas 531–532 e 759 dizem que o item 4 está "em andamento, não conferido por mim — os números podem mudar". O
   item 4 foi fechado em 14/11 às 00:08 e os números citados **não mudaram**.
2. O artefato fala em "amostra de 79 buscas". O mapa hoje declara 89 (79 dos grupos A a G, a amostra principal, mais
   10 do grupo H) e há uma ampliação de 40 buscas em
   `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (não verificada). Os números do artefato
   são os da amostra principal e continuam certos; falta dizer isso.
3. O grupo H traz dois fatos que tocam 4.1 e 4.5 e que o artefato não tem: em "dedetizadora confiável são paulo" o
   primeiro resultado orgânico é o diretório ohub.com.br; nas três buscas de preço aparecem marketplaces (triider nas
   três, pedegas e ohub numa) e a mesma página de "tabela de preço" de uma dedetizadora está em primeiro (seção 12 do
   mapa). A frase "um diretório aparece … quase sempre do meio da página para baixo" (linha 228) vale para a amostra
   principal, não para as buscas de confiança e preço. "PedeGás … apareceu 1 vez na amostra" (linha 119): 1 na
   amostra principal e mais 1 no grupo H.

**Desenho — o que o desenho cita do artefato e o que o artefato diz que toca o desenho:**

- As remissões do desenho a [M] (seções 4.0.1, 4.2, 4.3, 4.6, 6, 7, 8 e seção 1, item 9) caem em trechos que
  existem e dizem aquilo.
- "O canal é escolha do item 6" (linha 248): o desenho escolheu e-mail ou página restrita (seção 5.2). Coerente.
- "Uma licenciada por região, nomeada na página, com pagamento antecipado" (linhas 58–60): é o modelo previsto para a
  fase 4 do desenho (seção 8), que acrescenta "e por praga". Coerente.
- **Divergência não registrada no artefato** (achado 12): o artefato diz que, na via A, "o que se cobra é o **clique**"
  (linhas 34–36 e 245–246). O desenho, escrito depois, **não** adota o clique como unidade de cobrança, porque não
  distingue toques repetidos; trata o toque como indicador, define "lead válido" como o contato que a licenciada
  confirma ter recebido com o código do site e deixa a unidade como decisão do owner
  (`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linhas 208–209, 313 e 359–363). O desenho registra a
  divergência; o artefato, não.
- O desenho repete "6 no oHub (o 'mais 2' vem de artigo de 2021 e pode estar desatualizado)" (linha 274), apoiado no
  artefato. Se o achado 5 for aplicado, a frase do desenho também muda — fica para a sessão principal.

---

## 9. Forma

- Português: sim. Citações em inglês são trechos curtos de política ou de página, entre aspas.
- Caminhos absolutos: sim, em todas as remissões a arquivo. Uma menção solta a "`PROMPT_PLANO.md`" na linha 647, depois
  de o caminho completo ter sido dado na linha 613: aceitável.
- Números com unidade, período, país e fonte: sim nas tabelas da seção 3 e nas contas. Dois pontos pequenos: R$ 280
  aparece sem a classe em 4.3 e 4.7 (linhas 335 e 490), embora a tenha em 4.2 (achado 16).
- Datas e horas: as do cabeçalho vêm de `date`, segundo o próprio texto; não tenho como conferir a janela de leitura
  de 13/11.
- Nada dito como publicado, comprado, cadastrado ou enviado; nenhuma empresa contatada; o texto diz isso (linhas
  13–15) e nada no corpo o contradiz. Nenhum dado pessoal: os executivos entrevistados aparecem pelo cargo.
- Cópia de fonte: só trechos curtos entre aspas.
- Dever jurídico: "levantamento com fonte, não parecer" está no cabeçalho e é repetido onde importa (linhas 168,
  402, 575, 585).

---

## 10. O que não conferi

- O HTML das páginas (a ferramenta resume); a janela de leitura declarada pelo artefato para 13/11.
- As fontes que não abriram na seção 10 do artefato, salvo as três que testei de novo (continuam sem abrir).
- F36 (sem números e sem uso no texto).
- As páginas da ajuda do Google sobre perfil de empresa e as normas citadas pelo item 2: são do item 2, já fechado;
  conferi só que o artefato transcreve o item 2 como ele está.
- A página de termos de Anúncios de Serviços Locais (`/localservices/answer/7501778`): o artefato diz que não a
  reabriu; eu também não. Conferi a remissão no guia (b), linha 368.
- Os anexos e notas dos subagentes do item 4; a ampliação de 14/11 (não verificada), além das 45 primeiras linhas.
- O protótipo e os demais documentos (`perguntas_owner.md`, `contrato_pontos.md`, `plano_conteudo_90d.md`).

## 11. Lembretes e hooks ignorados

- O `CLAUDE.md` global pede, no início de toda sessão, carregar as ferramentas de memória corporativa, recuperar
  contexto, salvar memória a cada descoberta, resumir a sessão ao final e oferecer "compound". **Não executei nada
  disso** (regra da rodada: nada da empresa neste projeto). Nenhuma skill de plugin foi usada.
- Nenhuma página lida pediu ação. O resultado da ferramenta de busca traz um lembrete para listar as fontes: os
  endereços usados estão na seção 4.
- Não escrevi em nenhum arquivo além deste relatório; não rodei `git` de escrita; não usei `/tmp`.

---

## 12. Achados, com a correção pedida

Ordem: primeiro os que tocam o portão e a regra de evidência; depois os de fonte; depois os de coerência; por fim os
menores. "Linha" é a do artefato `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`.

1. **Portão — a Parte 2 não traz "como opera, contas, precificação e riscos" para cada modelo** (linhas 510–586). O
   portão diz "para cada um". As seções 5.1 a 5.7 dão o veredito e a remissão, e só 5.4 encosta em número.
   **Correção:** abrir a seção 5 (depois da linha 512) com uma tabela de uma linha por modelo e quatro colunas — "Como
   opera", "As contas", "Precificação do lead", "Riscos" — ou acrescentar essas quatro linhas a cada 5.x. Onde não há
   o que calcular, escrever isso, por exemplo: "As contas: não feitas — modelo vedado; a única cifra é a alegada por
   quem vende o método (R27, EUA, classe D), que não vira regra." e "Precificação: não se aplica; nada é vendido
   dentro da regra."

2. **Portão — "confirmado ou derrubado" recebe uma terceira resposta** (linhas 45–48 e 633–639). A resposta é honesta
   e tem fonte, mas o portão pede uma de duas e a regra da rodada manda não reescrevê-lo. **Correção:** dizer na linha
   633, com todas as letras, qual é a resposta ao portão e por que ela não é binária. Redação pedida: "**Resposta ao
   portão: não confirmado.** O portão pede 'confirmado ou derrubado'; com fonte pública, nenhuma das duas sai. (a) O
   R$ 20–60 **não se sustenta como número de trabalho**: nunca foi preço observado, é saída de fórmula com insumos sem
   fonte brasileira, e nem o piso (R$ 6,90 pelos extremos da linha 15) nem o teto (R$ 18 a R$ 37 pela conta da linha
   82) saem das próprias contas. (b) **Não foi derrubado por preço observado**: os comparáveis brasileiros de hoje
   ficam na mesma ordem de grandeza, para outro produto. O que derrubaria ou confirmaria está na lista abaixo e está
   fora da rodada." Ajustar a linha 45 no mesmo sentido. Se isso fecha o portão é decisão da sessão principal; na
   minha leitura, atende ao que o portão quer (fonte e conclusão), não à letra.

3. **Classe A estendida e aplicada de forma desigual** (linhas 18–20; R21, linha 135; R26, linha 140; F31, linha 745;
   F37, linha 751; título da linha 654). A regra da rodada não inclui página de plataforma na classe A.
   **Correção:** (i) na linha 18, trocar por: "A = documentação oficial (Google, Meta, lei, norma). **A\* = preço ou
   termo publicado pela própria empresa sobre ela mesma**: prova que ela publica aquele preço ou aquela regra; não
   prova que o mercado o pratique. Esta marca é minha, não está na regra da rodada."; (ii) usar A\* em R1 a R9, R12 a
   R16, na tabela 4.0.1 (Angi, oHub, Cronoshare, GetNinjas) e nas linhas F1 a F6, F8 a F16, F20 a F23, F25 a F27 e
   F30; (iii) dar a mesma marca A\* a R21 (F31) e R26 (F37), que são tabela de preço do próprio vendedor — ou, se a
   escolha for manter D para vendedor, rebaixar as brasileiras do mesmo tipo; o que não pode é a mesma espécie de
   fonte ter duas classes; (iv) na linha 654, trocar o título por "Consenso (classe A, ou duas B independentes) e
   fatos de tabela (A\*, cada plataforma sobre si)" e marcar os itens 4 a 7 como A\*.

4. **R20 e F6 não são classe A** (linhas 129 e 720). A faixa "R$ 150 a R$ 600" é estimativa do GetNinjas sobre o preço
   de terceiros, sem método. **Correção:** linha 129, coluna Classe: "D (estimativa da plataforma sobre o preço de
   terceiros, sem método; quem ganha: GetNinjas, que capta busca com a página)". Linha 720: "A\* para o que a página
   diz da própria plataforma (tem a categoria; não exige licença); D para a faixa de preço".

5. **O limite "4, mais 2 com acréscimo" do oHub está na página atual de planos; a ressalva "artigo de 2021, pode
   estar desatualizada" ficou velha** (linhas 39, 108, 267, 595 e 663–664). F8, lida em 14/11/2026 entre 01:26 e 01:32, traz nas
   perguntas frequentes: "O limite de respostas de cada pedido de orçamento são 4 respostas mas é possível chegar até
   a 6" e adicional "de 40% se for a 5a resposta e 80% se for a 6a resposta". **Correção:** em R4 (linha 108),
   coluna Fonte: "F8 (perguntas frequentes da página de planos, sem data, lida em 14/11/2026) e F12 (artigo de
   19/03/2021, que diz o mesmo)"; tirar "pode estar desatualizada" de R4 e das linhas 39, 267, 595 e 663–664,
   escrevendo "4, mais 2 com acréscimo de 40% e 80% (R4)". Avisar a sessão principal de que a linha 274 de
   `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` repete a ressalva.

6. **F11 não diz "1 ou 3 meses"** (linhas 457–458). O artigo (09/01/2026) fala em assinatura "oHub Plus" com
   "recorrência mensal, bimestral, trimestral e semestral"; "1 ou 3 meses" está só em F8. **Correção:** "assinatura
   sem preço público: de 1 ou 3 meses na página de planos (F8); mensal, bimestral, trimestral ou semestral no artigo
   de ajuda de 09/01/2026 (F11) — as duas páginas da plataforma não dizem o mesmo".

7. **F15 tem data** (linha 729). A página traz "com dados atualizados em Novembro de 2026". **Correção:** trocar
   "(sem data)" por "("com dados atualizados em Novembro de 2026"; sem dia)".

8. **Os termos do GetNinjas dizem algo sobre devolução** (linhas 181 e 699). O artefato dá a política de reembolso
   como "não conferida" porque a página de ajuda devolve erro 500 (continua assim). Mas F1, que o artefato já usa,
   traz: cláusula 9.a, moedas adquiridas "não serão devolvidas ao Anunciante ou convertidas em moeda corrente";
   cláusula 15.b.i, devolução de moedas quando uma suspensão é revertida; e nenhuma previsão de devolução por pedido
   inválido (os dois últimos pontos são resumo da ferramenta). **Correção:** linha 181, coluna "O que devolve": "Página
   de reembolso: não abriu (erro 500, de novo em 14/11/2026). Pelos termos (F1): moedas adquiridas "não serão
   devolvidas ao Anunciante ou convertidas em moeda corrente" (cláusula 9.a); devolução de moedas só aparece para
   suspensão revertida (cláusula 15.b.i, resumo da ferramenta — conferir na página)". Linha 699: "A política de
   reembolso do GetNinjas além do que está nos termos (a página de ajuda não abriu)…".

9. **Um preço de contato brasileiro que está em F18 e não foi aproveitado; e a ambiguidade de R11 não chega à seção
   7** (linhas 115, 625 e 635–637). F18 traz o exemplo "Custo do serviço total = R$120 . Comissão em cronos estimada:
   50 cronos, R$ 5,00 (uns 4% aproximadamente)" (limpeza; Brasil; 23/07/2025). **Correção:** em R11, acrescentar à
   Observação: "Exemplo da própria página (F18), para um serviço de limpeza de R$ 120: 50 cronos, R$ 5,00, cerca de
   4% — isto é, R$ 0,10 por crono (cálculo meu). É exemplo de outro serviço, não de dedetização." Na linha 625,
   depois de "(cálculo meu)": "— se o percentual for por cliente fechado e não por contato, o preço por contato é
   menor; a fonte não esclarece (R11)".

10. **O estado do item 4 ficou velho** (linhas 531–532 e 759). **Correção:** linha 531: "…arquivo do item 4, fechado em
    14/11/2026; os números abaixo foram conferidos de novo nesse arquivo e em
    `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` em 14/11/2026 e não mudaram". Linha 759: trocar
    "(item 4, em andamento)" por "(item 4, fechado em 14/11/2026)".

11. **"Amostra de 79 buscas" precisa do nome que o mapa lhe dá hoje, e o grupo H muda uma frase** (linhas 52, 166,
    228, 521 e 119). **Correção:** na primeira ocorrência (linha 52): "na amostra principal do mapa de busca (79
    buscas dos grupos A a G, 13/11/2026; o mapa tem hoje mais 10 buscas de confiança, preço e informação — grupo H —
    e uma ampliação de 40, não verificada)". Na linha 228, depois de "(posição mediana 5)": "nas buscas de confiança e
    de preço do grupo H o quadro é outro: o diretório é o primeiro resultado em "dedetizadora confiável são paulo" e
    há marketplace nas três buscas de preço
    (`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, seção 12; dez buscas não sustentam regra)". Na
    linha 119: "apareceu 1 vez na amostra principal e 1 no grupo H".

12. **A unidade de cobrança da via A diverge do desenho, e só o desenho diz isso** (linhas 34–36 e 245–246).
    **Correção:** acrescentar ao fim do passo 2 de 4.2 (linha 246): "O desenho, escrito depois
    (`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, seções 5.1, 6 e 8), **não** adota o clique como
    unidade de cobrança: o site não distingue toques repetidos da mesma pessoa. Lá o toque é indicador, o 'lead
    válido' é o contato que a licenciada confirma ter recebido com o código do site, e a unidade (lead válido ou
    mensalidade da região) é decisão do owner." E, na tabela de riscos de 4.2, linha "WhatsApp" (linha 313),
    acrescentar: "toque repetido e acesso de robô incham a contagem".

13. **A conferência de 4.7 só existe na via B** (linhas 486–487). **Correção:** "Conferência: por amostra, com a
    própria pessoa atendida — **só possível na via B**, em que o site tem o contato, e com autorização dela para esse
    contato (item 2, seção (c), linha 356: contato futuro é outra finalidade). Na via A o site não tem o contato da
    pessoa: a conferência depende só do que a licenciada declara."

14. **Três frases sem apoio** (linhas 52, 53 e 554). **Correção:** linha 52: "**Leitura minha:** o risco que mais pesa
    é…". Linha 53: trocar "quase todos de dedetizadoras" por "9 deles de sites que se apresentam como dedetizadora (2
    com número de licença visto) e 1 de diretório
    (`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`)". Linha 554: trocar "O caso mais citado do método"
    por "O caso que a pesquisa antiga citava".

15. **A pesquisa antiga citava duas páginas para o custo por clique; o artefato reabriu uma** (linha 629).
    **Correção:** "Das duas páginas citadas como fonte, nenhuma traz custo por clique de dedetização: F40 não traz
    valor nenhum; a outra
    (https://www.digitallevolution.com.br/blog/google-ads-cpc-o-que-e-como-funciona-e-como-reduzir-seus-custos-em-2025,
    28/05/2025, agência, classe D, lida em 14/11/2026) só traz valores ilustrativos num exemplo de outro ramo". Incluir
    essa página na tabela da seção 9 como F41.

16. **As contas não têm lado de custo, e o resumo não avisa** (linhas 49–50 e 215); R$ 280 sem classe em duas contas
    (linhas 335 e 490). **Correção:** no item 6 da seção 1, depois de "é ilustração": "e é só de receita ou de teto de
    preço — nenhum custo (domínio, hospedagem, horas, consulta jurídica) foi levantado". Nas linhas 335 e 490,
    escrever `[BR, HIPÓTESE 25/09, classe D]`, como na linha 270.

17. **O Triider cita uma modalidade pré-paga** (linhas 118 e 597). F23 a menciona, sem detalhe; os termos (F22) só
    descrevem a pós-paga. **Correção:** na Observação de R14: "A página para profissionais (F23) cita também uma
    modalidade pré-paga, sem preço nem regra; os termos só descrevem a pós-paga."

18. **Gestão do site da licenciada: a frase da fonte diz "owned and managed by the business owner"** (linhas 372 e
    375–379). **Correção:** acrescentar ao passo 5 de 4.4: "Se o conteúdo escrito por um terceiro autorizado atende a
    'managed by the business owner' (item 2, linha 117) **não foi levantado**; o desenho seguro é a licenciada aprovar
    e publicar o conteúdo."

19. **"Não em dinheiro" é mais forte que três das quatro fontes** (linhas 55–56, 184 e 668). **Correção:** "devolvem em
    **crédito ou saldo**; só a Cronoshare diz com todas as letras que não reembolsa em dinheiro (F20) — e os termos do
    GetNinjas dizem que moedas não são convertidas em moeda corrente (F1, cláusula 9.a)".

20. **Falta dizer que o piso de R$ 20 também não sai da conta** (linhas 617–619). **Correção:** depois de
    "(reconstituição minha)": "O piso de R$ 20 tampouco sai dos extremos da linha 15: 230 × 30% × 10% = R$ 6,90."

**Para a sessão principal, fora do artefato:** o cabeçalho (linhas 5–12) terá de registrar esta segunda passada; a
linha 274 do desenho depende do achado 5; `https://www.habitissimo.com.br/` devolve um certificado de outro domínio
nesta máquina, o que pode ser da rede e não do site.
