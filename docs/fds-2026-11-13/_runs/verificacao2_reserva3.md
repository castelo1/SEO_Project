# Segunda passada — tarefa de reserva 3 (plano de conteúdo de 90 dias)

- **Quem:** revisor independente, em contexto limpo (subagente), sem acesso à conclusão de ninguém. Não abri nenhum
  arquivo `verificacao*` nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só
  listei os nomes) e desconsiderei o que o cabeçalho do plano diz sobre verificações anteriores.
- **Quando:** sábado, 14/11/2026. Início às 02:01:27; última leitura de `TZ=America/Sao_Paulo date` antes de gravar
  este arquivo: 02:10:19; conferência final e dois acertos de conta neste relatório: 02:13:07 (Brasília).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` (150 linhas; gravado em 14/11/2026,
  01:11:34; sha256 começa por `9e4cfca82e2a83fb`). Não foi editado por mim.
- **Portão** (`RODADA.md`, fila de reserva, 3): "Plano de conteúdo de 90 dias: quais páginas primeiro e por quê,
  apontando para o mapa de palavras-chave."
- **Veredito: APROVADO COM RESSALVAS.** Sorteio: **1 falha em 12** contra as fontes como eu as li (2 em 12 se a
  afirmação 15 for medida contra o `serp_sp.md` regravado às 02:09:53, depois da minha leitura). Todas as contagens de
  termos batem com o mapa de hoje. 17 achados, nenhum de conta; os que pesam são de coerência com o desenho e com as
  perguntas corrigidos nesta madrugada (achados 1 a 4).

## 1. O que abri

| Arquivo | Como | Hora da leitura |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` e `RODADA.md` | inteiros | 02:01 |
| `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` | inteiro | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (2.721 linhas; gravado 01:11:50) e `gera_palavras_chave.py` | script e leitura | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (gravado 01:54:32) | inteiro | 02:02 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` | inteiro, **na versão gravada às 01:11:49** (sha256 `bcb1d5c9fc908d75`) | **02:03** |
| o mesmo arquivo, regravado por outro agente às **02:09:53** | só o `git diff` (leitura), para ver se as seções citadas pelo plano mudaram | 02:10 |
| `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (1.180 linhas; gravado 01:11:49), `serp_sp_ampliacao.csv`, `serp_raw/lote_02.jsonl`, `serp_raw/repeticao_01.jsonl`, `paginas_top10.jsonl`, `medicao_modelo.csv` | script | 02:06–02:08 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` | seções 1 a 3 e 5 a 10 | 02:07 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`, `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` (gravado 01:58:03) | inteiros | 02:04 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | cabeçalho, "Em uma página", seções 2, 3, 7, 8 e 9 | 02:05 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` | linhas 186–194 e 239–246 (o que o desenho cita para "seguro" e para o CDC) | 02:08 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | seção 9, linha 15 da tabela | 02:08 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/` | busca por "[A ESCREVER]" e existência da página-modelo | 02:06 |

Scripts meus, só de leitura, biblioteca padrão (rodados com `python3 -B`, sem gravar nada):
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res3_contagens.py`,
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res3_serp.py` (usa `git log` e `git show`, só leitura) e
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/v2res3_sorteio.py`.

## 2. Portão, parte por parte

| Parte | Cumpre? | Onde | Ressalva |
|---|---|---|---|
| "Plano de conteúdo de 90 dias" | Sim | seções 1 e 3: calendário do dia 1 ao 90, três medições (28, 56, 84), condições antes do dia 1 | — |
| "quais páginas primeiro" | Sim | seção 3: 19 a 23 páginas em ordem, por faixa de dias, com o tipo do desenho (T1 a T12) | faixas vizinhas compartilham o dia-limite (40, 60, 70, 80); sem efeito |
| "e por quê" | Sim, com ressalva | coluna "Por que nesta ordem": a ordem entre os blocos (base → guias → oferta → públicos) tem razão e remissão; dentro dos guias, ratos, percevejo e pombos trazem "não há razão para esta posição", marcado PREMISSA | o "porquê" que falta é o volume, e a opção padrão da pergunta 10 passou a ser medi-lo antes: o plano ainda diz "se o owner quiser" (achado 1) |
| "apontando para o mapa de palavras-chave" | Sim | coluna "Termos em K": filtros por `praga`, `tipo_local`, `local`, `intencao`, `publico`; refiz todos e batem (seção 3 abaixo) | a conta de cobertura (168, 13%) é do mapa antigo (achado 4); o plano não diz que K é grade de combinações geradas (achado 4) |

## 3. Contagens de termos refeitas (`v2res3_contagens.py`, contra o `palavras_chave.csv` de 01:11:50)

| Linha do plano | O que o plano diz | O que contei | Bate? |
|---|---|---|---|
| 20–23 | 2.721 termos; "não medido" em todas as linhas; colunas | 2.721 linhas, 2.721 termos distintos; `volume` = "não medido" em 2.721; colunas conferem | sim |
| 65 | cidade + geral + contratar + residencial/geral: 6 | 6 (A01, A02, A03, A04, F07, F13) | sim |
| 67 | confiança: 140 = 47 + 46 + 46 + 1 | 140 = 47 "com licença" + 46 "confiável" + 46 "melhor" + 1 "como saber" | sim |
| 67 | 120 de bairro e 15 de região | bairro 120; zona 15; cidade 4; sem local 1 | sim |
| 67 | coletados A10, H01, H02, H03 | os mesmos quatro | sim |
| 69 | baratas: 2 informativos; 1 de cidade + contratar | 2; 1 (B01) | sim |
| 70 | ratos: 2; 2 | 2; 2 (B02, K06) | sim |
| 72 | cupim: 2; 3 | 2; 3 (B03, B04, K07) | sim |
| 74 | percevejo: 2; 1 | 2; 1 (B06) | sim |
| 76 | pombos: 1; 2 | 1; 2 (B09, K10) | sim (ver achado 14) |
| 77 | escorpião: 1; 1 | 1; 1 (B05) | sim |
| 73 | zona + contratar: 24 por região; 23 no centro; 2 de condomínio e restaurante | zona leste, norte, oeste e sul: 24 cada; centro: 23; em cada uma, 1 de condomínio e 1 de restaurante (e 1 de apartamento, 1 de empresa, 1 de escola) | sim |
| 75 | praga × região: 2 termos (1 de contratar, 1 de preço) | 80 pares praga × região, todos 1 + 1 | sim |
| 78 | preço + cidade: 22; 6 gerais, 16 de praga, 10 de pragas sem guia (lista de 10) | 22; 6; 16; 10 (a mesma lista) | sim |
| 78 | coletados A05, A09, H04, H10; H05 tem `tipo_local` = sem local | os mesmos; H05 = "sem local", `intencao` = preço | sim |
| 80, 81 | `publico` = condomínio: 9; restaurante: 9 | 9 (4 de cidade, 5 de zona); 9 (4 e 5) | sim |
| 90–91 | urgência 835; bairro 2.289 | 835; 2.289 | sim |
| 96–97 | 21 informativos, 4 coletados no grupo H | 21; H06, H07, H08, H09 | sim |
| 108 | 6 termos de formigas, pulgas, mosquito, carrapatos, aranhas, traças | 6, um de cada | sim |
| 103–109 | os 21 informativos distribuídos pela tabela da seção 4 | 10 nos seis guias + 5 gerais + 6 sem guia = 21 | sim |
| 88–89 | cobertura: até 168 termos (13%) dos 1.260 de antes; "não refeita" | no mapa de 00:08 (commit `8443220`, 1.260 termos) a união dos filtros dá **167** (uma região, 5 páginas T3); no mapa de hoje dá **239 de 2.721 (8,8%)** com 5 T3 e 235 (8,6%) com 1; 238 e 234 se a região for o centro | número antigo, declarado como tal; **desatualizado** (achado 4) |

Por intenção, no mapa de hoje: contratar 892, urgência 835, preço 833, confiança 140, informativa 21 (soma 2.721).
Situação: 129 coletados, 2.592 não buscados.

## 4. Números de busca conferidos nos dados (`v2res3_serp.py`)

| Linha do plano | O que o plano diz | O que os dados dizem | Bate? |
|---|---|---|---|
| 34–37 | em 3 das 4 buscas informativas, o 1º resultado não é de dedetizadora | H06 imoveis.estadao.com.br; H07 br.envu.com; H08 petlove.com.br; H09 ecoservicos.com.br | sim |
| 67 | H03: 2º é a consulta pública do estado; 1º é site não lido | 1º dethetiza.com; 2º sivisa.saude.sp.gov.br | sim (remissão: achado 6) |
| 67 | 11 anúncios nas três de confiança | H01, 5; H02, 6; H03, 0 = 11 | sim (ver achado 5) |
| 69 | H07: nenhum anúncio; 1º de fabricante, não lido | 0 anúncio; br.envu.com | sim |
| 72 | cupim: 2 dos 3 perfis do bloco com "cupim(s)" no nome, nas duas vezes, fora o patrocinado | B04: "Cupins SP", "Oeste Pragas Dedetizadora de cupim", "ARMOR…" + patrocinado; B04r: "Cupins SP", "ARMOR…", "Prime Cupins" | sim |
| 77 | escorpião: 12 de 16 resultados de órgãos públicos e do Butantan | B05 e E05: 16 orgânicos, 12 "governo/universidade" (um deles é da USP) | sim |
| 78 | H04, H05, H10: a mesma página de "tabela de preço" em 1º; um marketplace nas três | dedetizadoranovatec.com.br `/tabela-de-preco-de-dedetizacao/` em 1º nas três; triider.com.br nas três | sim |
| 80 | grupo F: 13 buscas, 117 resultados, 68% serviço ou outra, 1% por local | 13; 117; 79 (67,5%); 1 (0,9%) | sim |
| 81 | bloco "[A ESCREVER]" no protótipo | `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 95 | sim |
| 111–112 | 7 das 10 páginas lidas têm subtítulo em forma de pergunta | `paginas_top10.jsonl`, campo `hq` > 0 em 7 de 10 | sim |
| 143–144 | resumo de IA nas 10 buscas do grupo H, 4 delas informativas | `visao_geral_ia` = sim em H01 a H10 | sim |

## 5. Coerência de dias, de quantidades e com o desenho corrigido

| Ponto | Conferido | Resultado |
|---|---|---|
| Base | T1 (1) + T10 (2) + T11 (2) na semana 1 = 5; T8 (1) + T12 (1) na semana 2 = 2 | 7, como diz a linha 30 |
| Guias | 15–21, 22–28, 29–35, 36–42, 43–49, 50–56 | seis semanas, dias 15 a 56 |
| Oferta | 30–40 (T7, T4), 40–55 (T3), 50–60 (T9) | cabe em "dias 30 a 60" |
| Públicos e revisão | 60–70, 70–80, 80–90 | cabe em "dias 60 a 90"; a medição do dia 84 cai na revisão |
| Medições | 28, 56, 84 nas linhas 43, 47, 71, 79, 83, 119–121 e 148 | coerentes; três períodos de 28 dias, como a planilha (`medicao_modelo.md`, "Por que 28 dias") |
| Dia 28 | "quatro guias que faltam (cupim, percevejo, pombos, escorpião)" | certo: baratas e ratos já no ar |
| Dia 56 | T3 "no ar desde o dia 55"; preços "até o dia 60" | certo |
| Ritmo | 19 ÷ 12,86 = 1,48; 23 ÷ 12,86 = 1,79; 90 ÷ 7 = 12,86 | "de 1,5 a 1,8" e "12,9 semanas" certos |
| Total | 7 + 6 + 1 + 1 + (1 a 5) + 1 + 2 | 19 a 23 |
| Desenho, seção 3.1 | T1 1; T2 6; T6 2; T8 1; T9 1; T10 2; T11 2; T12 1 = 16 fixas; T3 1–5; T4 1–5; T7 1–3 | 19 a 29; o plano fica dentro, tipo por tipo |
| Zero página de bairro (T5 = 0) | linhas 45–46, 120 e 130 | coerente |
| Oferta só com licenciada nomeada | linhas 38–41, 73, 75, 80 e 134 | coerente (D, seção 4.4) |
| Passo (d) da fase 1 é linha de base | linha 55 | coerente com "não condição de passagem"; **desalinhado** da opção padrão da pergunta 10 e sem o roteiro do ChatGPT (achado 1) |
| Critério de parada | linha 121 × D, seção 8, fase 2, e seção 10, premissa 6 | coerente: "cerca de 3 meses", marcado PREMISSA; o plano não promete resultado (linha 136) |
| `perguntas_owner.md`, linha 50, cita "linha do dia 84" do plano | existe (linha 121) | coerente |

## 6. Sorteio de 12 afirmações

Enumerei 46 afirmações com fonte citada (lista em `v2res3_sorteio.py`). Semente: `v2-reserva3-20261114`
(`random.seed` + `random.sample`, Python 3). Sorteadas: 2, 7, 11, 13, 15, 16, 18, 24, 35, 36, 41, 45.

| # | Linha | Afirmação | Fonte aberta | Existe e diz aquilo, com aquela força? | Classe ou marca |
|---|---|---|---|---|---|
| 2 | 30–33 | As cinco primeiras páginas são o que as demais precisam para cumprir o desenho (D, seções 2, 4.2 e 5.1) | `desenho_v0.md`, seções 2, 4.2 e 5.1 | **FALHA (força e remissão).** A seção 2 sustenta "Quem somos"; a 5.1, a política. A 4.2 é a faixa fixa, não uma página. Nada nas três seções faz do início e de "Como funciona" condição das demais. Dita como fato, sem marca | deveria ser INFERÊNCIA (achado 7) |
| 7 | 55 | Volume no Planejador, "se o owner quiser" (D, seção 8, fase 1, letra d; S, seção 10) | `desenho_v0.md`, linha 362; `serp_sp.md`, seção 10 (lida às 02:03) | Passa, com ressalva: as duas fontes dizem aquilo; o desenho diz "linha de base, não condição de passagem". A redação ficou atrás da opção padrão da pergunta 10 (achado 1) | ato do owner; certo |
| 11 | 66 | Aviso do botão remete à política; servidor anota o IP; "Excluir meus dados" em D, seções 5.1 e 5.2 | `desenho_v0.md`, seções 5.1 e 5.2 | Passa, com ressalva de remissão: a página "Excluir meus dados" está nomeada nas seções 3.1 (T11) e 5.2, não na 5.1 (achado 6) | INFERÊNCIA, marcada |
| 13 | 67 | H03: 2º resultado é a consulta pública; 1º é site não lido (S, seção 12.1) | `serp_sp.md`, seções 12.1, 12.2 e 12.3 (02:03); `serp_sp.csv` | Passa, com ressalva de remissão: a 12.1 só traz o 1º resultado; o 2º está nas seções 1 (item 9), 12.2 e 12.3 (item 2). O CSV confirma os dois | observação de 1 busca |
| 15 | 67 | Em H01 e H02 o resultado é de dedetizadoras e de anúncios; 11 anúncios nas três de confiança; a premissa não sai confirmada (S, seção 12.3, item 4) | `serp_sp.md`, seção 12.3, item 4 (02:03); `serp_sp.csv` | **Passa contra a versão lida às 02:03**, que dizia isso quase com as mesmas palavras. **Na versão regravada às 02:09:53 a frase mudou** (achado 5): contra ela, o plano fica mais forte que a fonte | "só por hipótese", marcado |
| 16 | 67 | D, seção 4.3, não deixa dizer "a melhor" sem critério exposto | `desenho_v0.md`, linha 177; `01_google_organico.md`, linha 220 (classe A, 1 leitura) | Passa | classe A, pela fonte do desenho |
| 18 | 69 | Baratas: praga da página-modelo e da única busca informativa de praga coletada; 1º de fabricante (não lido); nenhum anúncio (S, seção 12.1) | `serp_sp.md`, seção 12.1 (02:03); `serp_sp.csv`; `palavras_chave.csv`; `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | Passa | PREMISSA de ordem, marcada |
| 24 | 78 | preço + cidade: 22 termos; 6, 16, 10; coletados A05, A09, H04, H10; H05 sem local | `palavras_chave.csv` | Passa (recontado) | contagem |
| 35 | 111–113 | 7 das 10 páginas têm subtítulo em pergunta (P, seção 4); sem fonte de que ajude | `paginas_top10.md`, seções 4 e 7 (item 4); `paginas_top10.jsonl` | Passa | hipótese sem A ou B, marcada |
| 36 | 119 | colunas `impressoes` e `visitas_*` da planilha | `medicao_modelo.md`, linhas 32 e 39; `medicao_modelo.csv` | Passa | — |
| 41 | 132 | Não publicar tudo de uma vez: D, seção 7 e seção 10, premissa 13 (PREMISSA) | `desenho_v0.md`, linhas 352 e 438 | Passa | PREMISSA, marcada |
| 45 | 136 | O Google não dá prazo; 6 a 12 meses é premissa do guia (A, seção 9) | `01_google_organico.md`, linhas 386 e 391–395 | Passa | classe A (ausência de prazo) + premissa (6 a 12 meses), como o guia marca |

**Placar: 1 falha em 12** (a 2). Três passam com ressalva de remissão ou de atualidade (7, 11, 13). A 15 passa contra a
fonte que li e falharia contra a fonte regravada sete minutos depois: mesmo contando-a, são 2 em 12, dentro do limite.

## 7. O que procurei e não achei

- **Volume de busca afirmado:** nenhum. O plano repete "não medido" (linhas 22–26, 70, 74, 76, 140) e não ordena por demanda.
- **Promessa de posição, tráfego ou prazo dita como fato:** nenhuma. As medições estão no condicional; a linha 136 recusa
  prometer resultado; os dias 28, 56 e 84 são premissa 5.
- **Número de outro país usado como do Brasil:** nenhum. O único estudo de fora (Pew) vem com "Estados Unidos", ano e
  classe, sem número convertido (linhas 144–146).
- **Regra apoiada só em relato ou em vendedor:** nenhuma. As bases são o desenho, o mapa de busca, o guia (a) e a
  leitura das dez páginas; a única ideia sem fonte A ou B (subtítulo em pergunta) está marcada como hipótese.
- **Página que o desenho ou as restrições não permitem:** nenhuma página por bairro; nenhuma oferta sem licenciada
  nomeada; "24 horas", "garantia", "seguro", "a melhor" e estrelas estão na lista do que o plano não faz (linha 135).
  Avaliação e depoimento não aparecem em página nenhuma do plano (e faltam na lista: achado 13).
- **Ato que a sessão não pode fazer, dito como feito ou como passo dela:** nenhum. Publicar, conversar com licenciada,
  contratar advogado, Planejador, Search Console e hospedagem estão com "owner". "Nada foi publicado" (linha 10).
  A única tarefa com "sessão ou owner" é ler fonte oficial (linha 57), que a rodada permite.
- **Dado pessoal:** nenhum no plano nem neste relatório.

## 8. Achados

Caminho de todos, salvo indicação: `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`.

**De coerência com o desenho e as perguntas corrigidos em 14/11 (01:49 e 01:58)**

1. **Linha 55 (e 24–26, 70, 74, 76, 140): o volume deixou de ser "se o owner quiser".** A opção padrão da pergunta 10
   passou a ser "sim, no passo (d) da fase 1, antes de escolher as páginas da fase 2"
   (`/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`, linha 42), e o passo (d) inclui também o roteiro do
   ChatGPT (`/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 362), que o plano não cita. Redação certa
   da linha 55: "Volume de busca medido no Planejador de palavras-chave e roteiro do ChatGPT rodado uma vez — pela
   opção padrão da pergunta 10, o owner faz os dois no passo (d) da fase 1, antes do dia 1; são linha de base, não
   condição de passagem. Se o volume existir no dia 1, a ordem dos seis guias (premissa 1) e a escolha das seis
   pragas (D, seção 10, premissa 3) são revistas com ele antes de publicar; a ordem deste plano é a que vale sem a
   medição | owner | D, seção 8 (fase 1, letra d); S, seção 10;
   `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`, pergunta 10". Na linha 24, acrescentar "hoje" a
   "não há volume de busca medido".
2. **Linha 56: a lista de dados da licenciada está atrás do desenho.** Faltam o "contato da empresa para pedidos sobre
   dados pessoais, como ela informou" (D, seção 4.1, última linha, e seção 3.1, T7; premissa 22) e a "validade da
   licença, se constar do documento" (D, seção 7, primeira linha). Redação: "…área atendida, pragas, preços com data,
   contato para pedidos sobre dados pessoais e validade da licença, se constar".
3. **Linhas 15–23, 70 e 80: o plano não usa a ampliação [S2], embora três filtros dele apontem para buscas dela**
   (K06, K07, K09, K10) e o desenho já a cite para os guias (D, seção 3.1, T2, e seção 10, premissa 3). Conferi em
   `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv`: em "controle de ratos são paulo" (K06) o 1º
   resultado é prefeitura.sp.gov.br; em "fumacê para condomínio são paulo" (K09), sp156.prefeitura.sp.gov.br. O plano
   põe o escorpião por último porque o resultado é de governo e diz que para ratos "não há razão". Redação: incluir
   em "Bases" «"S2" = `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (40 buscas de
   14/11/2026, madrugada)»; na linha 70, acrescentar "na busca 'controle de ratos são paulo' (K06), o primeiro
   resultado é da prefeitura (S2, seção 5.2; observação de 1 busca): parte deste guia disputa com página oficial (D,
   seção 3.1, T2)"; na linha 80, "o termo K09 ('fumacê para condomínio') tem a prefeitura em primeiro (S2, seção 5.2)".
4. **Linhas 88–91: a cobertura é do mapa antigo e o plano não diz o que K é.** No mapa de hoje, a união dos filtros da
   seção 3 dá até 239 de 2.721 termos (8,8%), não 168 (13%); no mapa antigo, refiz e deu 167. Redação: "Cobertura do
   mapa (K de 14/11/2026, 01:11): com uma licenciada numa região, os filtros acima apontam para 235 a 239 dos 2.721
   termos (8,6% a 8,8%; um a menos se a região for o centro). Desses, o plano não tenta 52 (os 46 de 'melhor' e os 6
   do início); dos outros 94 de confiança, 80 são de bairro e 10 de região, a que a página responde sem conteúdo
   por local. K é uma grade de combinações geradas, não lista de buscas reais: 2.592 dos 2.721 termos nunca foram
   buscados (S, seção 10). Ficam sem página, com cinco páginas de praga × região, 2.482 termos: os de urgência
   (835), os de bairro que não são de urgência nem de confiança (1.449) e 198 outros — quase todos das quatro
   regiões sem licenciada, mais 13 de praga sem guia com a cidade, os 6 informativos de praga sem guia e 6 de
   público apartamento, empresa e escola com a cidade." (Contas minhas, de 14/11/2026, feitas entre as leituras de `date` das 02:10:19 e das 02:13:07, com a zona oeste como
   região; 239 + 2.482 = 2.721.)
5. **Linha 67: a fonte mudou depois da minha leitura.** O `serp_sp.md` regravado às 02:09:53 trocou a seção 12.3,
   item 4, para "não foi testada (e por isso não sai confirmada)": nas três buscas de confiança, 11 dos 28 resultados
   são de dedetizadoras já classificadas, o 1º de H01 é um diretório, e os 11 anúncios estão em duas buscas (H01, 5;
   H02, 6; H03, nenhum). Redação: "nas buscas H01 e H02 há 11 anúncios (H03 não teve) e, nas três, 11 dos 28
   resultados são de dedetizadoras já classificadas; o primeiro de H01 é um diretório (S, seção 12.3, item 4: a
   premissa não foi testada)". Reconferir a frase contra a versão final de S, que ainda estava sendo corrigida.

**De remissão e de marca**

6. **Remissões imprecisas.** Linha 67: "(pelo endereço e pelo título; S, seção 12.1)" → "S, seções 12.1 (primeiro
   resultado), 12.2 e 12.3, item 2 (a consulta pública em segundo)". Linha 66: "está em D, seções 5.1 e 5.2" → "está
   em D, seções 3.1 (T11) e 5.2; a 5.1 trata do pedido de exclusão na Via A". Linha 121: "(no desenho, isso é da fase
   3; D, seção 10, premissa 5)" → "(D, seção 8, fase 3, e seção 10, premissa 5)".
7. **Linhas 30–33 (falha do sorteio).** Redação: "As cinco primeiras são o que as demais precisam — INFERÊNCIA deste
   plano: 'Quem somos' vem de D, seção 2; a política e 'Excluir meus dados', de D, seções 3.1 (T11), 5.1 e 5.2; o
   início e 'Como funciona' são os tipos T1 e T10 (D, seção 3.1), e a trilha parte do início (D, seção 3.4)". Tirar a
   seção 4.2 (é a faixa fixa, não uma página). O mesmo na linha 65: "Toda outra página aponta para elas" pede "(D,
   seção 3.4, trilha e links)".
8. **Linhas 38–41: a página de preços não é página de oferta.** No desenho, T9 não oferece o serviço e não tem botão
   (D, seção 3.1). Redação: "as páginas que dependem da primeira licenciada: as de oferta (ficha, região, de 1 a 5
   de praga × região) e a de preços, que não oferece o serviço nem tem botão".
9. **Linhas 104–106: duas escolhas sem marca.** (a) "o que perguntar à empresa" vai para "Como funciona", mas no
   desenho é parte de cada guia (D, seção 3.1, T2): marcar "escolha deste plano (PREMISSA)" ou devolver aos guias.
   (b) "Início ou 'Como funciona'" para "dedetização vale a pena": escolher uma — pela regra de D, seção 3.2, que o
   próprio plano cita, um termo tem uma página. Redação: "'Como funciona' (T10)".

**De forma**

10. **Falta dizer que o jurídico é levantamento.** O plano cita o CDC (linha 104), a RDC 622 pelo desenho (105), a
    norma de serviços de alimentação (81) e a obrigação de condomínio (109). Acrescentar ao cabeçalho: "Natureza: o
    que encosta em norma é levantamento com fonte, repetido de D e de
    `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`; não é parecer jurídico."
11. **Números de busca sem período, país e limite.** Linhas 34–37, 77, 78 e 80 dão contagens sem dizer de que amostra.
    Acrescentar em "Bases", depois de "S": "os números de S são observação de amostra — 89 buscas em 13/11/2026 (79
    nos grupos A a G, 10 no grupo H), cidade de São Paulo, Brasil, uma conta logada, um ponto de acesso, computador;
    não é censo, posição média nem volume".
12. **Caminho absoluto do protótipo.** Linhas 69 e 75: "página-modelo do protótipo" →
    `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`. Linha 81: "no protótipo" →
    `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` (linha 95).
13. **Linhas 90 e 135: a seção 6 não tem o que a linha 90 diz que tem.** A linha 90 manda à seção 6 para a escolha de
    não ter página de urgência; a seção 6 só fala de escrever "24 horas" sem prova. Acrescentar a linha: "Página
    para os termos de urgência ('24 horas', 'urgente') | Só com prova guardada dada pela licenciada (D, seção 4.3);
    sem ela, não há o que a página afirmar". E, na linha 135, depois de "estrelas": "avaliação copiada e
    depoimento (D, seção 2)".
14. **Linha 76: o filtro de pombos inclui K10, "dedetização piolho de pombo são paulo".** O próprio mapa chama a
    classificação de discutível: é outra praga
    (`/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, seção 8). Acrescentar: "um dos dois é
    'piolho de pombo' (K10), classificação discutível".
15. **Cabeçalho, linhas 3–9 e 16–17.** Diz "terceira versão, de 14/11/2026, 00:26", e o arquivo foi alterado às 01:11
    (dito só na linha 21). Acrescentar "última alteração: 14/11/2026, 01:11 (contagens)". O estado de "S" na linha
    16 vai mudar quando a correção em curso do `serp_sp.md` terminar.

**Sugestões (não são erro)**

16. **Seção 5:** a premissa 3 lembra que o resumo de IA apareceu nas 10 buscas do grupo H, mas nenhuma medição olha a
    coluna `impressoes_em_ia` da planilha nem o roteiro mensal do ChatGPT (D, seção 6). Cabe nas linhas dos dias 56 e 84.
17. **Linhas 40–83:** as faixas compartilham o dia-limite (30–40 e 40–55; 50–60 e 60–70; 60–70 e 70–80; 70–80 e
    80–90). Sem efeito na conta; se for mexer, usar 41–55, 61–70, 71–80, 81–90.

## 9. O que conferi e o que não conferi

**Conferi:** o portão, parte por parte; todas as contagens de termos do plano (40 números, todos batem; a cobertura
refeita nos dois mapas); 11 números de busca contra os CSV e os brutos; as 12 afirmações do sorteio na fonte, e, fora
do sorteio, as outras remissões a D, S, A e P das seções 1 a 7 do plano (não achei remissão a seção inexistente);
dias, quantidades por tipo e critério de parada contra o desenho de 01:54; a linha do dia 84 citada em
`perguntas_owner.md`; as colunas da planilha de medição; os dois trechos de `00_restricoes.md` em que o desenho apoia
"seguro" e o CDC, art. 38 (linhas 193–194 e 243–244: dizem aquilo).

**Não conferi:**
- nenhuma página da web: não reabri as fontes do Google citadas pelo guia (a) nem refiz busca alguma; o que digo de S
  vem dos arquivos do projeto;
- os guias `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` e
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` (o plano não os cita; do segundo vi só a linha 15 da
  tabela da seção 9) e o resto de `00_restricoes.md`;
- o `serp_sp.md` regravado às 02:09:53: li só o `git diff` nas seções que o plano cita (os números de seção não
  mudaram; o texto da seção 12.3, item 4, mudou — achado 5). O arquivo ainda estava em correção;
- por que a conta antiga de cobertura dava 168 e a minha, com os mesmos filtros, 167;
- se as seis pragas e os dois públicos são a escolha certa: é premissa do desenho (seção 10, premissa 3), não do plano;
- o conteúdo das páginas do protótipo, além da presença de "[A ESCREVER]";
- o histórico de versões que o cabeçalho do plano relata (não abri as verificações anteriores, por instrução).

## 10. Lembretes ignorados

- O `CLAUDE.md` global (`/home/ancastelo/.claude/CLAUDE.md`) pede carregar as ferramentas do meli-memory no primeiro
  turno, chamar `mem_context`, salvar memória a cada descoberta, fechar com `mem_session_summary` e perguntar por
  "compound". **Não executei nada disso** (regra da fronteira e exceção escrita no `CLAUDE.md` do projeto).
- Skills de plugin (entre elas `gestao`), navegador, busca na web e modelos externos: não usados.
- Nenhum hook pediu ação durante a revisão. Nenhum `git` de escrita foi rodado; nada em `/tmp`; nenhum artefato editado.
