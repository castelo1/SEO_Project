# Verificação do item 5 — Modelos de negócio de venda de leads

- **Início:** `Fri Nov 13 21:51:57 -03 2026` · **fim das conferências:** `Fri Nov 13 22:03:28 -03 2026` (saídas de
  `TZ=America/Sao_Paulo date`).
- **Verificador:** subagente em contexto limpo, sem a conclusão de quem produziu. Não alterei nenhum arquivo além
  deste; não fiz commit nem push; não usei navegador, memória corporativa, skill, modelo externo nem subagente.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`, 762 linhas, como está no commit
  `83bbec7` (`git diff 83bbec7` sem diferença; árvore limpa no início).
- **Ferramentas:** `Read` e `python3`/`sed`/`grep` sobre arquivos do projeto (só leitura); `shuf` com semente
  declarada; `WebFetch` (39 chamadas, 34 endereços, nenhuma com erro). A ferramenta de leitura resume e limita cada
  citação a cerca de 125 caracteres; por isso perguntei "a página contém exatamente a frase X?" e pus, em cada
  pedido, uma pergunta falsa de controle (número ou frase trocada). Todas as perguntas de controle voltaram "não".
- **Natureza:** conferência de estudo com fonte; **não é parecer jurídico**.
- **Estado do repositório ao terminar:** além deste arquivo novo, `git status` mostra
  `docs/fds-2026-11-13/PAINEL.md` modificado — **não fui eu**; não o abri nem o editei.
- **Instruções ignoradas, como manda a fronteira:** o `CLAUDE.md` global pede carregar e salvar memória corporativa
  (meli-memory), perguntar por "compound" e gravar resumo de sessão. **Não executei nada disso.** Nenhuma página
  pediu ação.

## VEREDITO: APROVADO COM RESSALVAS

| Conferência | Resultado |
|---|---|
| Portão, ponto a ponto | cumprido (7 modelos na parte 1, os 4 do portão entre eles; 8 linhas na parte 2, com veredito) |
| Sorteio de 12 afirmações com fonte externa | **11 conferem · 1 falha · 0 inconclusivo** (limite: 2 falhas) |
| Obrigatórias (a) a (d) | (a) confere · (b) confere, com ressalva · (c) confere; as duas listas se sustentam, cada uma na sua página · (d) confere |
| Ponteiros para o item 2 | 59 blocos de remissão conferidos (censo), 12 sorteados exibidos: **59 de 59 batem**; todos os vereditos das duas tabelas da seção 2 batem com o quadro; **nenhum modelo recomendado contraria um "vedado"** |
| Aritmética | 52 resultados refeitos: **52 conferem** (1 com nota de arredondamento, D9) |
| Números do item 4 | todos conferem com `data/serp_sp.csv`, `data/serp_dominios.csv` e `docs/mercado/serp_sp_dominios.md`; 1 frase imprecisa (F7) |
| Fora do sorteio | **7 falhas** (F1 a F7; F1 é a do sorteio) e **10 defeitos menores** (D1 a D10) |

Nenhuma falha muda a ordem dos modelos, um veredito do item 2 ou o veredito sobre o R$ 20–60. As que mexem em frase
de conclusão são F1 e F2 (seção 1, item 8, e consenso 7), F4 (consenso 4) e F6 (consenso 3). Recomendo corrigir F1 a
F7 antes de fechar o item; D1 a D10 podem ir junto.

## 1. Portão, transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linha 63)

> `docs/modelos_de_negocio.md`: **primeiro os modelos que não dependem de perfil próprio no mapa nem de se passar por
> dedetizadora** (site de conteúdo e comparação que identifica as licenciadas; pagamento por lead; exclusividade por
> região; gestão do perfil e do site da própria licenciada, com autorização dela); depois os que dependem, marcados
> com o veredito do item 2. Para cada um: como opera, as contas (com país e classe de cada número), precificação do
> lead (por tipo de praga, residência × empresa, exclusivo × compartilhado), e os riscos — dependência do Google,
> propaganda, LGPD, WhatsApp, conflito com o parceiro. O valor do lead da pesquisa antiga é confirmado ou derrubado,
> com fonte

Regra de evidência: `RODADA.md`, linhas 36–48 (lidas).

| Ponto do portão | Onde está no artefato | Resultado |
|---|---|---|
| Os que não dependem vêm primeiro | seção 2, parte 1 (linhas 59–69) e seção 4 (linhas 138–483) | cumprido |
| Incluem os quatro nomeados | 4.1 site de conteúdo e comparação; 4.2 pagamento por lead; 4.3 exclusividade por região; 4.4 gestão do perfil e do site | cumprido. Em 4.4 a parte "site" aparece só como condição (o conteúdo é dela) e como risco; não há descrição do serviço de site (D10) |
| Os que dependem vêm depois, com o veredito do item 2 | seção 2, parte 2 (linhas 71–82) e seção 5 (linhas 487–561) | cumprido. 2.5b (compra de links) e 2.7 (cobrar do consumidor) levam "—" porque o item 2 não tem linha; está dito |
| Como opera, em cada modelo da parte 1 | 4.1 a 4.7, bloco "Como opera" | cumprido nos 7 |
| As contas, cada número com país e classe ou marcado como premissa | 4.1 a 4.7, bloco "As contas" | cumprido nos 7. Todo número de conta leva `PREMISSA`, `[BR, classe A]` ou `[BR, HIPÓTESE 25/09]`; ver D1 sobre a premissa de 30% |
| Precificação nos três recortes | 4.1 a 4.5 e 4.7: três itens explícitos; 4.6: os três por remissão a 4.2 (é forma de cobrança) | cumprido |
| Os cinco riscos | 4.1 a 4.5: cinco linhas; 4.6 e 4.7: cinco riscos em duas ou três linhas agrupadas | cumprido |
| R$ 20–60 confirmado ou derrubado, com fonte | seção 7 (linhas 580–622): "não dá para confirmar — nem para derrubar" | **a fundamentação bate** (ver 3(d) e seção 6 abaixo): o número era saída de fórmula, as linhas citadas dizem isso, e nenhuma fonte brasileira lida dá preço de lead exclusivo de residência. Ressalva: um dos dois "comparáveis classe A" é estimativa de vendedor (F5) |

## 2. Sorteio de 12 afirmações com fonte externa

Candidatas: 36 linhas com fonte externa (R1–R16 e R20–R28 da seção 3; 5 linhas da tabela 4.0.1; 6 da seção 6; fora
R17–R19, que são da pesquisa antiga, e a linha do Thumbtack, sem fonte). Comando:
`shuf --random-source=<(openssl enc -aes-256-ctr -pass pass:item5-20261113 -nosalt </dev/zero)`; tomei as 12
primeiras, pulando a que repetia endereço já sorteado.

| # | Afirmação (linha do artefato) | URL aberta | O que a fonte devolveu | Classe e país | Resultado |
|---|---|---|---|---|---|
| 1 | R11, Cronoshare: "varia de 2% a 15% do seu orçamento total, sendo uma média de 6% para cada novo cliente", atualizado em 23/07/2025 (linha 104) | F18 | Frase exata presente; "Atualizado 23 de julho de 2025"; "entre 6 e 10%" não está nesta página (está em F19, como o artefato diz) | BR certo; classe A discutível (F5) | CONFERE, com ressalva de classe |
| 2 | Seção 6, PedeGás: colhe pedido de dedetização sem nomear as empresas; "Plataforma de intermediação de pedidos" (linhas 512–513 e 574) | F26 | Expressão presente no rodapé; "16 prestadores ativos", sem nome, CNPJ nem licença; pedido por formulário e depois WhatsApp | A sobre si, BR | CONFERE |
| 3 | R22: "around $55" de média nacional, 1º trimestre de 2023 (linha 125) | F32 | "in the first 3 months of 2023, the average cost per lead nationwide for our pest control campaigns was around $55"; 31/03/2023; leads exclusivos | EUA; "pode estar desatualizada" presente | CONFERE |
| 4 | Seção 6, Habitissimo: operação brasileira comprada pelo Triider em 2021 (linha 573) | F24 | Título e frase batem; 06/07/2021 | C, BR; "pode estar desatualizada" presente | CONFERE |
| 5 | 4.0.1, Google: "Charged leads get reassessed by our models over time, and may be issued credits automatically."; "over a 30-day period"; 15 dias; país "países de R28" (linha 167) | F29 | As três informações existem. **Mas:** a frase continua com "if determined to be low quality" (o artefato fechou a citação com ponto final); e a página diz "Automatic lead credits are not available for accounts located in European Economic Area (EEA) countries." e "Lead credits aren't available for health care verticals, tax specialists, or for advertisers in EMEA." | A certo; **país errado**: 9 dos 11 países de R28 são da Europa | **FALHA** (F1) |
| 6 | Seção 6, Cronoshare: "nunca é superior aos 15% do que você cobrará"; "entre 6 e 10% por cada cliente novo"; sem data (linhas 104 e 571) | F19 | As duas frases presentes; sem data; a página não diz se é por contato ou por cliente fechado (o artefato avisa) | BR; classe: ver F5 | CONFERE |
| 7 | R9: moeda do GetNinjas com "validade de 3 (três) meses" (linha 102) | F1 (e F3) | "As Moedas adquiridas terão validade de 3 (três) meses a partir do momento da aquisição."; F3 repete e diz que as vencidas "serão descontadas da conta" | A sobre si, BR. Os termos não exibem data; rodapé "©2011-2024" (D3) | CONFERE |
| 8 | Seção 6, GetNinjas: tem a categoria; "verifique se possuem licença e certificação" é conselho ao cliente; R20 "Em geral, os preços podem variar entre R$ 150 a R$ 600." (linhas 118 e 569) | F6 | As duas frases exatas; a página não diz que a plataforma exige ou confere licença | A sobre si (sem método), BR | CONFERE |
| 9 | R24: "$22 to $65, with a $38 median, across 600 accounts", de segunda mão (linha 127) | F34 | Frase exata; a base é de outra empresa (Blue Grid Media); 14/01/2026; agência | D certo. País: a página não declara o país da base; o artigo é todo sobre os EUA (D8) | CONFERE |
| 10 | R3: 12 créditos = R$ 19,49–20,64; 24 = R$ 38,97–41,28 (linha 96) | F8 (e F9) | Quatro pacotes e preços batem; validade de 12 meses; "De 12 a 24 créditos" bate | A sobre si, BR | CONFERE (conta refeita na seção 5) |
| 11 | R14, Triider: "21% (vinte e um por cento) a 25% (vinte e cinco por cento)", pós-paga, termos de 28/02/2025 (linha 107) | F22 | Cláusula 6.1.5, frase exata; "Atualização em 28 de fevereiro de 2025."; a cláusula 11.1 traz a frase da garantia citada em 5.7 | A sobre si, BR | CONFERE |
| 12 | R15, PedeGás: grátis R$ 0; Pro R$ 99 ("Prioridade na lista"); Premium R$ 199 ("Topo em todas as cidades que você atende.") (linha 108) | F25 | Três planos e as duas frases batem | A sobre si, BR | CONFERE |

**Fora do sorteio, também abertas e conferidas (15 endereços):** F12 (até 4 respostas, mais 2 com 40% e 80%;
19/03/2021), F14 (premium: 20% a 100%; "o tamanho da empresa e nível de interesse de contratação"; cita condomínio;
19/03/2021), F15 (262 fornecedores; "recebe até 4 propostas personalizadas"; frase da ordem da lista), F3, F7 (frase do
diretor financeiro; 24/08/2023), F20 (devolução em cronos; "Não reembolsamos valores pagos em sua conta bancária."),
F21 (no máximo 4), F27 (cadastro gratuito encerrado; sem preço), F30 (Angi: as quatro frases, 45 dias, seis meses,
14/08/2026), F31 ("$24.99 each"; "Last updated October 2026"), F33 ("$15–$45"; "typically 60-120 seconds"; país não
declarado), F35 ("$38" × "$85"; 28% e 30% num exemplo; "within three points"; 23/05/2026), F38 ("$45K/year"; "about
8 leads/day"; "$90K"; "2015-ish"; perfil criado e vendido junto; 26/08/2025), F39 ("24-36x"; abril de 2019), F40 (sem
valor de custo por clique; 04/12/2025). **Todas batem** com o que o artefato diz delas. Não abri F10, F11, F13, F16,
F17, F23, F36 e F37.

## 3. Conferências obrigatórias

**(a) oHub — CONFERE.** F9: "Dedetização" e "Dedetização e Desratização", cada uma com "De 12 a 24 créditos"; a
página não explica a faixa. F8: 100 por R$ 172,00; 180 por R$ 298,00; 240 por R$ 392,00; 420 por R$ 682,00; validade
de 12 meses; assinatura de 1 ou 3 meses sem preço. Conta: R$ 1,7200; 1,6556; 1,6333; 1,6238 por crédito → R$ 1,62 a
R$ 1,72; 12 × 1,6238 = 19,49; 12 × 1,72 = 20,64; 24 × 1,6238 = 38,97; 24 × 1,72 = 41,28. "R$ 19 a R$ 41 por
resposta" está certo.

**(b) GetNinjas — CONFERE, com ressalva (F4).** F5 contém "até 4 profissionais podem liberar o mesmo pedido" e traz
"Criado em 24 abril 2024" e "Atualizado em 9 setembro 2025". F4 contém "do primeiro ao quarto", mas não afirma o
limite. **A mesma página F5, em outra seção ("Qual é o tempo de validade das moedas do GetNinjas?"), diz "até que 3
prestadores liberem aquela solicitação"** — o artefato atribui esse "3" a um trecho de resultado de busca que "não
abriu". Preço por pedido: não publicado — F2 ("Os valores dos pedidos não são fixos e podem variar de acordo com o
tipo de serviço", sem tabela nem valor), F5 ("Cada oportunidade de serviço vale uma quantidade específica de moedas",
sem número) e F1 ("variação dinâmica baseada em fatores como local, tipo e oferta de orçamentos"). O que se pode
dizer é "não publicado nas quatro páginas abertas"; o preço aparece no aplicativo, que exige conta.

**(c) Anúncios de Serviços Locais — CONFERE: o Brasil não está em nenhuma das duas listas.** As duas listas saem de
páginas diferentes e cada uma se sustenta na sua:
- artefato, R28 e F28 (`/localservices/answer/6224841`, seletor de país, em inglês e em português): **11** países —
  Áustria, Bélgica, Canadá, França, Alemanha, Irlanda, Itália, Espanha, Suíça, Reino Unido, Estados Unidos. Sem Países
  Baixos, nas duas línguas;
- guia (b), seção 7, linha 368 (`/localservices/answer/7501778`, termos para prestadores): **12** países, os mesmos
  mais os **Países Baixos** (termos dos EUA na versão 2026-08, do Canadá 2025-03, dos demais 2020-09).

Nenhuma das páginas traz a frase "não disponível no Brasil": a conclusão é por ausência (F6).

**(d) Origem do R$ 20–60 — CONFERE.** `/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`:
linha 15 traz "~R$ 20–60 (estimativa Baixa)", fechamento de 30–45%, 10–20% do ticket e "~R$ 15–30" no GetNinjas;
linha 82 traz "mín R$ 20 / base R$ 35 / máx R$ 60 por lead exclusivo (Baixa, modelo meu)", com ticket de R$ 350,
fechamento de 35% e 15–20% e 30% do ticket; linha 16, R$ 3.000 = cerca de 75 leads a R$ 40; linha 81, tabelas
anunciadas; linhas 72–77, fechamento de agências dos EUA; linhas 63, 64, 65, 66, 42, 88 e 90 dizem o que o artefato
diz que dizem. `PROMPT_PLANO.md`, linhas 50–51: confere. Reconstituição: 350 × 35% × 15% = 18,38; × 20% = 24,50;
× 30% = 36,75 (o artefato escreve "R$ 18 a R$ 40", repetindo o arredondamento da pesquisa — D9); 650 × 45% × 20% =
58,50, perto de 60. A afirmação "o teto de R$ 60 não sai da conta da linha 82" está certa.

## 4. Ponteiros para o item 2

Li `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` inteiro (499 linhas) e conferi **todos** os 59
blocos de remissão do artefato, cada um com uma ou mais faixas de linhas (57 a esse arquivo e 2 a
`01_google_organico.md`, linhas 164 e 166; conferi também as faixas 152–200 desse guia e 416–463 de
`02_google_maps_perfil.md`). Todos apontam para o conteúdo afirmado. Os 12 sorteados para exibir
(`seq 1 59 | shuf`, semente `item5-ponteiros-20261113`, pulando o bloco que remete ao guia (a)):

| Linha do artefato | Remissão | O que há nas linhas do item 2 | Resultado |
|---|---|---|---|
| 383 | linhas 438–441 | Desenho B, botão abre o WhatsApp da licenciada; "Permitido com condição" | bate |
| 305–309 | linha 33; linha 38; linha 30; linhas 257–258 | os três vereditos; a frase "Um desenho em que **toda** página de oferta nomeia a licenciada…" | bate |
| 148 | linhas 442–446 | variante do formulário, marcada "inferência, não frase da fonte" | bate |
| 381 | linhas 181–194 | art. 2º (empresas especializadas) e art. 22 da RDC 622 | bate |
| 354–355 | linhas 113–116 | dona do perfil é a cliente; "Within 7 business days" | bate |
| 384 | linhas 136–137; linhas 95–98 | "o perfil, as avaliações e as ligações são dela e ela pode retomá-los"; "a contractual or consultory relationship" | bate |
| 65 | linha 30 (e os de 1.2, uma empresa) | propaganda: permitido com condição; linha 33 | bate |
| 350 | linhas 105–131 | subseção 4, "Caminhos legítimos para o mapa", até o caminho 3 | bate |
| 67 | linha 30, mais CDC art. 36 | linha 30; art. 36 nas linhas 217–218 e 234–235 | bate |
| 493–497 | linhas 25, 26, 53–63, 65–85, 89–103 | vedado; "Lead generation agents or companies."; endereço; suspensão | bate |
| 339 | linhas 217–222 e 233–235 | CDC arts. 36 e 37; item (i) da conclusão | bate |
| 374 | linhas 142–144 | rastreamento de chamadas contratado pela licenciada: não conclusivo | bate |

**Vereditos da seção 2 contra o "Quadro de vereditos" (linhas 21–38):** 1.1 linha 30; 1.2 linhas 33, 34 e 38; 1.3
linha 30; 1.4 linha 28; 1.5 linha 30; 2.1 linhas 25–26; 2.2 linha 31; 2.3 linhas 36–37; 2.4 linha 27; 2.5a linha 29;
2.6 seção (c), linhas 361–362 (não é linha do quadro, e a coluna "Onde está" diz isso). **Todos batem.** A linha 32 do
quadro (razão social e endereço, não conclusivo) e a linha 35 (legítimo interesse) não entram na tabela; a 35 é citada
em 4.2; a 32 não é citada em lugar nenhum (D5).

**Algum modelo recomendado contraria um "vedado"?** Não. Os sete da parte 1 usam só o botão para o WhatsApp da
licenciada ou o formulário com consentimento; o artefato repete que central de WhatsApp do site fica fora, que no
perfil da parceira o telefone e o site são dela, e que cobrar por contato no perfil dela esbarra num "não
conclusivo". A via do formulário é inferência do item 2, e o artefato diz isso.

## 5. Aritmética

| Conta (linha do artefato) | Refeito | Resultado |
|---|---|---|
| R2, R$ por crédito (95) | 1,72 · 1,6556 · 1,6333 · 1,6238 | confere |
| R3 (96) | 19,49 · 20,64 · 38,97 · 41,28 | confere |
| R6 (99) | 69,90 ÷ 500 = 0,1398 | confere |
| R19 (117) | 131 ÷ 280 = 46,8% | confere |
| 4.1 (198) | 2.000 × 3% = 60 | confere |
| 4.2, receita (249–251) | 600 · 1.200 · 2.000 · 4.000 · 6.000 · 12.000 | confere |
| 4.2, tetos (262–267), ticket × 30% × 15% e × 30% | 12,60 e 25,20 · 18,00 e 36,00 · 22,50 e 45,00 · 31,50 e 63,00 · 33,75 e 67,50 · 81,00 e 162,00 | confere (12 valores) |
| 4.2, margem (270) | 131 × 30% = 39,30 | confere |
| 4.2, quatro respostas (281) | 4 × 19,49 = 77,95; 4 × 20,64 = 82,56 | confere |
| 4.3 (320–321) | 40 × 30% × 280 × 15% = 504 | confere |
| 4.4 (363) | 3 × 600 = 1.800 | confere |
| 4.5 (403) | 5 × 99 = 495 | confere |
| 4.6 (440–441) | 4 × 300 = 1.200 | confere |
| 4.7 (468–469) | 20 × 280 × 10% = 560 | confere |
| 5.2 (509–511) | 51 ÷ 709 = 7,2%; 93 ÷ 709 = 13,1%; 138 ÷ 709 = 19,5% | confere |
| 7, Cronoshare sobre R$ 280 (600) | 16,80 · 28,00 · 42,00 | confere |
| 7, linha 82 da pesquisa (592–593) | 18,38 a 36,75 | confere, com nota (D9) |
| 7, reconstituição (593–594) | 650 × 45% × 20% = 58,50 | confere |
| 7, 75 leads a R$ 40 (587); R$ 0,15 da linha 65 (601) | 3.000; 716 ÷ 4.800 = 0,149 | confere |
| 7, baratas R$ 13 a 25 (613); faixa R$ 17 a 42 (610–611) | 12,60 e 25,20; 16,80 e 42,00 | confere |

## 6. Números do item 4

Refeitos com `python3` sobre `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (1.060 linhas, 79 buscas) e
`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` (157 domínios):

| Número no artefato | Refeito | Resultado |
|---|---|---|
| 709 resultados orgânicos, 157 domínios | 709; 157 | confere |
| 10 mais frequentes = 39% | 275 ÷ 709 = 38,8% | confere |
| ohub.com.br em 21 buscas | 21 buscas, 22 resultados | confere |
| resumo de IA em 73 | 73 | confere |
| anúncio de texto em 60 | 60 | confere |
| mesmo anunciante, perfil patrocinado em 47 | 47 (um só nome) | confere |
| 64 perfis; três em 43% das linhas | 64; 86 ÷ 202 = 42,6% | confere |
| bloco de mapa em 68 de 79 | 68 | confere |
| 14 domínios, 51 resultados, 7% | 14; 51; 7,2% | confere |
| 15 domínios, 93 resultados, 13% | 15; 93; 13,1% | confere |
| 11 domínios, 138 resultados, 19% | 11; 138; 19,5% — é a classe "empresa com número de licença" | confere o número; a frase está imprecisa (F7) |
| PedeGás 1 vez; Triider com página de preço | 1; 2 resultados, mesma página de preço | confere |

## 7. Classe de evidência no arquivo inteiro

- **"Consenso" (seção 8):** os oito itens apoiam-se em fonte classe A. Três precisam de ajuste de redação: o 3 (por
  ausência — F6), o 4 (o mesmo fato está em "Disputado 2" — F4; e o "6 no oHub" vem só de artigo de 2021 — D3) e o 7
  (alcance geográfico do Google — F1). O 2 perdeu a ressalva do item 2 (D6).
- **Fonte de vendedor como base de regra ou de conta brasileira:** nenhuma regra nasce de fonte D. Nas contas, o
  ticket (R17, classe D, `HIPÓTESE 25/09`) entra marcado. A taxa de fechamento de 30% entra como `PREMISSA`, mas o
  valor é o do exemplo de agência dos EUA citado na mesma frase (D1). A estimativa da Cronoshare entra como "classe A"
  (F5).
- **Número dos EUA convertido ou na conta brasileira:** nenhum valor em dólar foi convertido; todos aparecem como "só
  estrutura". Único ponto de contato: D1.
- **Fonte anterior a 2025 sem "pode estar desatualizada":** F7, F12, F13, F14, F17, F24, F32, F39 e o caso de F38
  levam a marca. Faltam: a marca onde o "mais 2" do oHub é repetido sem R4, e "sem data" em 16 linhas da tabela de
  fontes (D3).
- **Afirmação sem fonte e sem marca:** F2, F3 e D7.
- **"Quem ganha":** a coluna está preenchida nas 40 linhas da tabela de fontes.
- **Uma classe por fonte:** R21, R22, R23 e R26 (F31, F32, F33, F37) levam "A / D" (F5).

## 8. Forma

Português: sim. Caminhos absolutos: sim (uma menção curta a `PROMPT_PLANO.md` na linha 621, depois do caminho
completo na linha 588). Nome de pessoa física do mercado local: nenhum. Telefone: nenhum. Texto de avaliação copiado:
nenhum. Nome de perfil do mapa: nenhum (só domínios). Jurídico como levantamento: sim, no cabeçalho, em 4.0 e em 5.7;
exceção pontual em D7. Citações literais: todas curtas (a maior tem menos de 160 caracteres).

## 9. Falhas, com a correção sugerida

Arquivo de todas: `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`.

**F1 — Créditos de lead do Google: país errado e citação cortada (linha 167; reflexo nas linhas 45–46, 173–175 e
640).** A página F29 diz que o crédito automático não vale para contas do Espaço Econômico Europeu e que não há
crédito de lead para anunciantes da região EMEA. A coluna "País" diz "países de R28", dos quais 9 são europeus. A
frase citada termina, na fonte, em "if determined to be low quality".
*Correção:* na linha 167, País = "fora da Europa — dos países de R28, EUA e Canadá, por exclusão (a página exclui o
Espaço Econômico Europeu do crédito automático e a região EMEA de qualquer crédito)"; citação = "Charged leads get reassessed by our models over time, and may be issued
credits automatically if determined to be low quality". Na linha 640, "Google (fora da Europa)".

**F2 — "Cobra-se adiantado" atribuído às quatro plataformas (linhas 173–174 e 45–46).** F29 diz "You're charged for
each valid lead you receive through your Local Services ad." — cobrança por lead recebido, não adiantada. F30 (Angi)
não fala de pagamento adiantado; fala de crédito "applied toward future lead charges". Pré-pagamento só está nas
fontes de oHub, Cronoshare e GetNinjas.
*Correção:* linha 173: "Padrão nas quatro que abriram: devolve-se **crédito, não dinheiro**. Pagamento adiantado só
nas brasileiras (oHub, Cronoshare; GetNinjas pelas moedas); Angi e Google cobram por lead recebido." Linha 45: "as
plataformas o tratam com regra escrita de lead inválido, que devolve crédito, não dinheiro (Angi, Google, oHub,
Cronoshare); as brasileiras cobram adiantado".

**F3 — "Desconto por volume existe nas duas plataformas" (linha 444).** Para o oHub, sim (R$ 1,72 → R$ 1,62). Para o
GetNinjas, a única fonte lida dá um pacote, "promocional" (500 por R$ 69,90 = R$ 0,14); a pesquisa antiga registra
4.800 por R$ 716 = R$ 0,149, isto é, **mais caro** por moeda.
*Correção:* "Desconto por volume existe no oHub (R2). No GetNinjas, não conferido: só um preço de pacote é público."

**F4 — "Até 4" no GetNinjas: a contradição está na própria página lida (linhas 101, 635–636 e 647–648).** F5 diz
"até 4 profissionais podem liberar o mesmo pedido" numa seção e "até que 3 prestadores liberem aquela solicitação"
em outra. O artefato diz que o "3" veio de resultado de busca e que não abriu o trecho; e põe o mesmo fato em
"Consenso 4" e em "Disputado 2".
*Correção:* linha 101, observação: "a mesma página, na seção sobre validade, diz 'até que 3 prestadores liberem
aquela solicitação'"; linhas 647–648: "o blog diz 4 numa seção e 3 em outra (F5); a ajuda diz 'do primeiro ao
quarto' (F4)"; linhas 635–636: "…a até 4 prestadores (GetNinjas: 4, com a contradição de Disputado 2; 6 no oHub,
artigo de 2021, pode estar desatualizada)". Mesmo ajuste na linha 32.

**F5 — Classe de R11 e classe dupla (linhas 104, 124–126, 129, 600, 610–611, 715–717, 721).** "Estimamos que o custo
dos cronos varia de 2% a 15%… média de 6%" e "nunca é superior aos 15%" são estimativa da vendedora sobre o próprio
custo-benefício, não preço nem termo: pela regra da rodada é alegação de quem ganha com a afirmação. A seção 7 a usa
como um dos "dois comparáveis brasileiros de classe A". E a regra pede **uma** classe por fonte; R21, R22, R23 e R26
levam "A / D".
*Correção:* R11 = "D (estimativa da plataforma sobre o próprio custo; não é tabela de preço)"; linha 600: "Comparável
A: oHub… (R3). Alegação da plataforma: Cronoshare… (R11)"; linhas 610–611: "o único comparável brasileiro de classe A
(oHub, R$ 19 a R$ 41) e a estimativa da Cronoshare (R$ 17 a R$ 42 sobre o ticket-hipótese) ficam na mesma ordem de
grandeza". R21–R23 e R26: "D (preço de tabela do próprio vendedor)". O veredito da seção 7 não muda.

**F6 — "Não existem no Brasil (classe A)" (linhas 41, 131, 605 e 634).** A fonte sustenta só que o Brasil não consta
do seletor de país; não há frase oficial de indisponibilidade. O guia (b) do item 3 escreve "A (por ausência)… até
prova em contrário" e lista 12 países por outra página; o artefato lista 11 e não menciona a diferença.
*Correção:* linha 131: acrescentar "A página de termos para prestadores (`/localservices/answer/7501778`) lista os
mesmos e os Países Baixos — ver `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção 7.
O Brasil não está em nenhuma das duas. Classe A por ausência." Linhas 41, 605 e 634: "o Brasil não consta das listas
oficiais de países (classe A, por ausência)".

**F7 — "Só 11 domínios exibem número de licença na página" (linha 510).** 11 é o número de domínios da classe
"empresa com número de licença" (138 resultados, 19%). Em `data/serp_dominios.csv` há 12 domínios com
`licenca_exibida = sim` (o 12º é um domínio satélite), e `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`,
seção 1, item 4, diz "12 dos 67 sites de serviço lidos".
*Correção:* "11 domínios estão na classe 'empresa com número de licença na página' (138 resultados, 19%); contando um
domínio satélite que também exibe, são 12 dos 67 sites de serviço lidos".

### Defeitos menores

- **D1 (linhas 257–258, 320, 603):** a taxa de fechamento de 30% é `PREMISSA`, mas coincide com o exemplo de agência
  dos EUA citado ao lado (F35, que a própria página chama de "worked example"). *Correção:* dizer que 30% é
  arbitrário e mostrar a conta também com 10% (a pesquisa antiga dava 10–15% para lead compartilhado), ou tirar a
  menção à agência dessa frase.
- **D2 (linha 31):** "No Brasil, quem vende pedido de orçamento cobra do prestador, pré-pago, por contato
  compartilhado" generaliza três plataformas; a seção 6 mostra Triider (percentual, pagamento pela plataforma) e
  PedeGás (mensalidade). *Correção:* "As três plataformas brasileiras de pedido de orçamento lidas (GetNinjas,
  Cronoshare, oHub) cobram…".
- **D3 (linhas 685–711; 32 e 636):** a tabela de fontes não diz "sem data" em F1–F4, F6, F8–F10, F15, F16, F20, F21,
  F23 e F25–F27; os termos do GetNinjas (F1) têm rodapé "©2011-2024". O "mais 2" do oHub (artigo de 2021) aparece nas
  linhas 32 e 636 sem "pode estar desatualizada". *Correção:* completar a coluna e a marca.
- **D4 (linha 215):** "do meio da página para baixo" — 5 dos 22 resultados do oHub estão entre os três primeiros, um
  deles em 1º. *Correção:* "quase sempre do meio da página para baixo (posição mediana 5)", como no item 4.
- **D5 (linha 156):** o risco de propaganda omite a razão social e o endereço "por prudência" (item 2, linhas 32,
  235–236 e 471). *Correção:* acrescentar.
- **D6 (linha 632):** o consenso 2 diz "não pode"; o item 2, linha 36, diz "vedado pela letra dos termos (leitura
  literal; alcance… não definido na fonte)". *Correção:* "não pode, pela letra dos termos".
- **D7 (linha 381):** "o gestor que escreve o texto responde ao menos perante ela" é afirmação jurídica sem fonte e
  sem marca. *Correção:* "(inferência minha; não levantado)".
- **D8 (linha 127 e 718):** país de R24 — a página não declara o país da base citada. *Correção:* "EUA (pelo contexto
  do artigo; não declarado para a base)".
- **D9 (linhas 592–593):** "que dá R$ 18 a R$ 40" — a aritmética dá R$ 18 a R$ 37; "40" é o arredondamento da
  pesquisa antiga. *Correção:* "que dá R$ 18 a R$ 37 (a pesquisa escreveu ~R$ 35–40)".
- **D10 (linhas 352–360):** o portão nomeia "gestão do perfil **e do site**"; 4.4 descreve o serviço de perfil e
  trata o site só como condição e risco. *Correção:* uma linha em "Como opera" dizendo o que a gestão do site cobre
  (por exemplo, a identificação e a licença em toda página de oferta), com remissão ao guia (a).

## 10. O que esta verificação não cobre

- A ferramenta de leitura resume; "confere" quer dizer que a frase pedida foi devolvida e que a pergunta de controle
  voltou "não". Não vi o texto bruto de nenhuma página.
- Oito fontes da tabela não foram abertas (F10, F11, F13, F16, F17, F23, F36, F37), nem as nove da seção 10 ("fontes
  que não abriram").
- Não reconferi o item 2 nem o item 4 na origem: conferi só que o artefato os cita certo. O item 4 está em andamento
  e os números podem mudar.
- Não reabri as fontes da pesquisa de 25/09 (tickets, margem, fechamento): entram como hipótese, como o artefato diz.
- Não avaliei se os modelos são bons negócios, nem se as licenciadas pagariam; nenhuma empresa foi contatada.
- Nada aqui é parecer jurídico.
