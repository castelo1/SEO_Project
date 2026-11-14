# Segunda passada — correções aplicadas ao plano de conteúdo de 90 dias (reserva 3)

- **Quem:** corretor (subagente), que não é o autor do plano nem o revisor.
- **Quando:** sábado, 14/11/2026. Início às 02:21:24; fim às 02:38:00 (Brasília, lidos de `TZ=America/Sao_Paulo date`).
- **Relatório aplicado:** `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva3.md`
  (15 achados e 2 sugestões).
- **Arquivo editado (o único):** `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` — de 150 para 204
  linhas; sha256 de `9e4cfca82e2a83fb` (o que o revisor leu) para `73486376398054b0` (lido às 02:38, com o plano já
  na forma final; a hora do cabeçalho dele, 02:35, é a da última leitura de `date` antes da última edição). Numeração
  das seções 1 a 7 preservada.
- **Script das contas (só leitura, biblioteca padrão):**
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/corr2res3_contas.py` — rodar com `python3 -B`.
  Última execução às 02:35. Usa `git log` e `git show` (leitura) para as versões antigas do mapa.
- **Placar:** 17 de 17 procedentes e aplicados — **11 como o revisor propôs, 6 com ajuste, 0 não aplicados**. Mais 4
  alinhamentos fora da lista (seção 3).

## 1. Achado por achado

Linhas = linhas do plano **depois** da correção.

| # | Achado do revisor | O que fiz | Linhas | Como conferi |
|---|---|---|---|---|
| 1 | Volume deixou de ser "se o owner quiser"; falta o roteiro do ChatGPT | **Aplicado.** A linha do volume passou a dizer que volume e roteiro são o passo (d) da fase 1, atos do owner com a conta dele (a sessão não mede nem roda), linha de base e não condição; que a ordem dos guias e a escolha das seis pragas são revistas se o volume existir no dia 1. "Hoje" no limite do cabeçalho. As três linhas de guia que diziam "o Planejador pode trocá-la" e a premissa 1 foram alinhadas | 49–53, 86, 104, 108, 110, 189–190 | `perguntas_owner.md`, linha 42 (opção padrão: "Sim", no passo (d) da fase 1, antes de escolher as páginas da fase 2) e linhas 55–57 (roteiro no mesmo passo); `desenho_v0.md`, seção 8, fase 1, letra (d) (linha 362: "linha de base…, não condição de passagem") |
| 2 | Lista de dados da licenciada atrás do desenho | **Aplicado.** Entraram "contato para pedidos sobre dados pessoais" e "validade da licença, se constar do documento", com as remissões | 87 | `desenho_v0.md`, seção 4.1 (última linha da tabela, linha 161), seção 3.1 (T7, linha 92), seção 7 (primeira linha, linha 343) e seção 10, premissa 22 |
| 3 | O plano não usa a ampliação (S2); K06 e K09 têm a prefeitura em primeiro | **Aplicado com ajuste.** S2 entrou em "Bases"; a linha de ratos ganhou K06 e a de condomínio, K09. Ajuste: como o texto de S2 estava em correção, a remissão é por seção (1, item 3, e 5.2) **e** pelo bruto (`ampliacao_04.jsonl`, ids K06 e K09); a linha de condomínio diz também que K09 é `praga` = mosquito, sem guia na versão 0 | 28–33, 104, 114 | script, parte 3: K06 1º `prefeitura.sp.gov.br`; K09 1º `sp156.prefeitura.sp.gov.br` (CSV e bruto); no grupo K, governo em 1º em 3 de 10 (K02, K06, K09) e presente em 5; seções de S2 reconferidas depois da regravação das 02:31 (numeração intacta) |
| 4 | Cobertura é do mapa antigo; o plano não diz o que K é | **Aplicado com ajuste.** Cobertura refeita: 235 a 239 de 2.721 (8,6% a 8,8%). K descrito como grade de combinações geradas em "Bases" e no parágrafo. Ajustes: (a) a decomposição dos 198 "outros" do revisor somava 184 — faltavam 13 termos de preço da própria região e "dedetizadora perto de mim"; escrevi os seis grupos, que somam 198; (b) acrescentei "um a menos sem o K10" e "só 37 são termos de fato buscados"; (c) a conta antiga (168, 13%) saiu do plano e ficou só aqui (seção 2) | 37–40, 122–134 | script, parte 1 (cobertura por região e por número de T3; decomposição do que fica sem página; 239 + 2.482 = 2.721) e parte 2 (mapas antigos) |
| 5 | A frase sobre H01 e H02 ficou mais forte que a fonte regravada | **Aplicado**, contra a versão final de S (02:14, com acertos até 02:22): 11 dos 28 resultados das três buscas de confiança são de dedetizadoras já classificadas; 1º de H01 é diretório; 11 anúncios de texto em duas (5 em H01, 6 em H02; H03 nenhum); a premissa "não foi testada". A coluna "Por que" da mesma linha, que dizia "não saiu confirmada no grupo H", também foi alinhada | 101 | `serp_sp.md`, seção 12.1 (tabela) e seção 12.3, item 4 (linhas 603–606); `desenho_v0.md`, seção 11 (linha 472, já alinhada por outro corretor às 02:23); script, parte 3: anúncios 5, 6 e 0; 28 orgânicos; pelas classes de `serp_dominios.csv`, 5 + 5 + 1 = 11 |
| 6 | Três remissões imprecisas | **Aplicado.** H03: S, seções 12.1 (1º resultado), 12.2 e 12.3, item 2 (consulta em 2º). "Excluir meus dados": D, seções 3.1 (T11) e 5.2; a 5.1 trata do pedido na Via A. Contagem da licenciada: D, seção 8, fase 3, e seção 10, premissa 5 | 101, 100, 169 | `serp_sp.md`, linhas 553, 581 e 595–597; `desenho_v0.md`, linhas 96, 204–207, 299, 364 e 425 |
| 7 | "As cinco primeiras são o que as demais precisam" dito como fato, com remissão errada (falha do sorteio) | **Aplicado com ajuste.** Virou INFERÊNCIA deste plano, com as remissões certas e sem a seção 4.2. Ajuste: na linha do calendário, "Toda outra página aponta para elas" também era mais forte que D, seção 3.4 (a trilha parte do início; nada diz que toda página aponta para "Quem somos" e "Como funciona"): reescrevi em vez de só acrescentar a remissão | 57–62, 99 | `desenho_v0.md`, seção 2 (última linha), seção 3.1 (T1, T10, T11), seção 3.4 (linha "Navegação e links"), seções 5.1 e 5.2 |
| 8 | A página de preços (T9) não é página de oferta | **Aplicado.** "Em uma página" separa as de oferta (ficha, região, praga × região) da de preços; a linha do calendário e o item do ritmo também | 69–72, 75–77, 112 | `desenho_v0.md`, seção 3.1, T9: "Oferece o serviço? Não"; "T9 não tem botão" |
| 9 | Duas escolhas sem marca na seção 4 | **Aplicado.** (a) "o que perguntar à empresa" numa página só: marcado "escolha deste plano (PREMISSA 7)", dizendo que no desenho é parte de cada guia e continua sendo; entrou a premissa 7 na lista. (b) "dedetização vale a pena": só "Como funciona" (T10) | 147–149, 202–204 | `desenho_v0.md`, seção 3.1 (T2: "o que perguntar à empresa") e seção 3.2 (uma busca, uma página: INFERÊNCIA) |
| 10 | Falta dizer que o jurídico é levantamento | **Aplicado.** Linha "Natureza" no cabeçalho; e a ressalva repetida onde o plano encosta em norma (CDC, RDC 622, norma de serviços de alimentação, obrigação de condomínio, "24 horas") | 45–48, 115, 147, 148, 152, 179 | `desenho_v0.md`, linhas 33–34 (mesma fórmula) e seção 4.3; existência de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (não reaberto) |
| 11 | Números de busca sem período, país e limite | **Aplicado com ajuste.** Em "Bases": 89 buscas de 13/11/2026 à noite (79 das 20:26 às 21:16; 10 das 23:18 às 23:31) e 40 da madrugada de 14/11/2026 (00:12 à 01:06), Brasil, cidade de São Paulo, uma conta logada, um ponto de acesso, computador, coleta por script; não é censo, posição média nem volume. Ajuste: além da nota, cada número de busca do plano leva a data e "São Paulo, Brasil" no próprio lugar, e a seção 3 abre com o limite da amostra | 24–33, 63–68, 92–95, 99, 101, 103, 104, 106, 110, 111, 112, 114, 154–156, 192–193 | script, parte 3: 89 buscas, todas de 2026-11-13, todas logadas, horas 20:26:51–21:16:03 e 23:18:29–23:30:54; 40 buscas de 2026-11-14, 00:12:10–01:06:01, todas logadas; `serp_sp.md`, seções 2.2 e 2.3 |
| 12 | Caminho absoluto do protótipo | **Aplicado** nas linhas de baratas, de praga × região e de restaurante (com a linha 95 do arquivo) | 103, 109, 115 | script, parte 4: os dois arquivos existem; "[A ESCREVER]" na linha 95 de `prototipo/para-empresas/restaurantes/index.html` |
| 13 | A seção 6 não tinha a escolha de não ter página de urgência; faltavam avaliação e depoimento | **Aplicado com ajuste.** Entrou a linha "Página para os termos de urgência". Ajustes: (a) marquei a escolha como INFERÊNCIA deste plano (o desenho não tem tipo de página de urgência; o que ele traz é a exigência de prova para "24 horas"); (b) "depoimento" **não** está escrito em D, seção 2 — a seção fala de avaliação copiada e de estrelas; quem liga depoimento a essa linha é o `LEIA-ME.md` do protótipo. Escrevi isso e marquei INFERÊNCIA, em vez de citar D, seção 2, para os dois | 179, 184 | `desenho_v0.md`, seção 2 (linha das avaliações), seção 3.1 e seção 4.3; busca por "depoimento" em `desenho_v0.md` (nenhuma ocorrência) e em `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` (linhas 20 e 115) |
| 14 | O filtro de pombos inclui K10 ("piolho de pombo") | **Aplicado**, pela segunda opção: a classificação ficou marcada como discutível, como o mapa faz ("2 termos: B09 e K10 … sem ele, 1 termo"); a cobertura diz "um a menos sem o K10" | 110, 125 | script: K10 = "dedetização piolho de pombo são paulo", `praga` = pombos, só no filtro do guia de pombos; `serp_sp_ampliacao.md`, seção 8 (linhas 323–324 da versão das 02:31) |
| 15 | Cabeçalho desatualizado | **Aplicado com ajuste.** Em vez de acrescentar "última alteração", reescrevi o "Estado" como quarta versão: histórico em três frases, segunda passada, caminho do relatório do revisor, achados aplicados, caminho deste relatório, hora lida de `date` (02:35), "não relida por terceiro". O estado de D, S, S2 e P em "Bases" foi atualizado | 3–16, 19–44 | cabeçalhos de `serp_sp.md`, `desenho_v0.md`, `serp_sp_ampliacao.md` e `paginas_top10.md`; `stat` dos quatro às 02:35 |
| 16 | (sugestão) Nenhuma medição olha `impressoes_em_ia` nem o roteiro do ChatGPT | **Aplicado**, sem medição nova: as duas coisas já estão em D, seção 6. Entraram nas linhas dos dias 56 e 84, com "só o owner roda, na conta dele" | 168, 169, 171 | cabeçalho de `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` (regravado às 02:31:48; as colunas `impressoes`, `posicao_media`, `impressoes_em_ia`, `visitas_*` e `leads_toque_no_botao` existem); `desenho_v0.md`, seção 6 (linhas 321 e 324). Não citei `medicao_modelo.md` por linha (em edição por outro corretor) |
| 17 | (sugestão) Faixas com o mesmo dia-limite | **Aplicado:** 41–55, 61–70, 71–80, 81–90; "Dias 61 a 90" em "Em uma página". As medições (28, 56, 84), "até o dia 60" e "desde o dia 55" não mudaram | 73, 109, 114, 115, 116 | leitura das seções 1, 3 e 5 do plano; `perguntas_owner.md`, linha 50, cita "linha do dia 84", que continua existindo |

## 2. Contagens: velhas → novas

Todas do script, sobre `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` (2.721 linhas, 2.721 termos
distintos, sha256 `7da42ee1f139fb6e`), salvo indicação.

| O que | Antes (terceira versão) | Agora |
|---|---|---|
| Cobertura dos filtros | "até 168 termos (13%)" dos 1.260 do mapa de 00:09, "não refeita" | **235 (1 página de praga × região) a 239 (5)** de 2.721: 8,6% a 8,8%. No centro: 234 a 238. Sem o K10: 234 a 238 |
| Termos sem página | "os de urgência (835) e quase todos os de bairro (2.289)" | 2.482 = 835 de urgência + 1.449 de bairro fora urgência e confiança + 198 outros (159 das quatro regiões sem licenciada; 13 de preço da própria região; 13 de contratar com a cidade para praga sem guia; 6 de público apartamento, empresa e escola; 6 informativos de praga sem guia; 1 "dedetizadora perto de mim") |
| Dentro da cobertura, o que o plano não tenta | não dizia | 52 (46 de "melhor" + 6 do início); dos outros 94 de confiança, 80 de bairro e 10 de região; 37 dos 239 são termos coletados |
| O que K é | "2.721 termos" | 129 consultas das duas coletas + 2.592 combinações geradas, nunca buscadas |
| Anúncios nas buscas de confiança | "11 anúncios nas três de confiança" | 11 anúncios de texto em duas (5 em H01, 6 em H02; H03 nenhum); 11 dos 28 orgânicos são de dedetizadoras já classificadas |
| Pombos, cidade + contratar | "2 termos" | "2 termos: B09 e K10"; sem o K10, 1 |
| Faixas de dias | 40–55; 60–70; 70–80; 80–90; "Dias 60 a 90" | 41–55; 61–70; 71–80; 81–90; "Dias 61 a 90" |
| Tamanho da amostra | não dizia | 89 buscas em 13/11/2026 (79 + 10); 40 em 14/11/2026 |

**Recontadas e iguais** (nenhuma mudou): 6 (início); 140 = 47 + 46 + 46 + 1, com 120 de bairro e 15 de região;
baratas 2 e 1; ratos 2 e 2; cupim 2 e 3; percevejo 2 e 1; pombos 1 e 2; escorpião 1 e 1; 24 por região e 23 no
centro, com 1 de condomínio e 1 de restaurante em cada; 2 por praga e região (80 pares, todos 1 + 1); preço + cidade
22 = 6 + 16, 10 de praga sem guia; H05 "sem local"; condomínio 9; restaurante 9; urgência 835; informativos 21 (4
coletados; 10 nos seis guias, 5 gerais, 6 sem guia); 12 de 16 no escorpião; grupo F: 13 buscas, 117 resultados, 79
de serviço ou outra (67,5%) e 1 por local (0,9%); a mesma página em 1º em H04, H05 e H10 e triider nas três; cupim,
2 de 3 perfis nas duas vezes; 7 de 10 páginas com subtítulo em pergunta; resumo de IA em 10 de 10 no grupo H; 19 a
23 páginas; 1,48 a 1,79 página por semana em 12,86 semanas.

**168 × 167 (pedido da tarefa: descobrir ou declarar).** No mapa de 1.260 termos (commit `8443220`, de 14/11/2026,
00:08:05), a união dos filtros dá **167** com cinco páginas de praga × região (166 se a região for o centro; 163 com
uma página) e **168 com seis** — uma para cada um dos seis guias. O plano limita a 5. Das variantes que testei (1, 5
e 6 páginas; cada uma das cinco regiões; sem o H05; sem os informativos gerais; sem o início; com todos os
informativos; soma simples sem tirar repetidos: 174), **só a de seis páginas dá 168**. É a explicação provável — a
conta antiga teria contado as seis pragas —, **não confirmada**: não abri o relatório que trouxe o 168, por
instrução. No mapa anterior a esse (commits `cfd2330` e `86af317`) a mesma conta dá 170. No mapa de hoje, com seis
páginas daria 240.

## 3. Alinhamentos fora dos 17 achados

1. **Subtítulos em pergunta (parágrafo final da seção 4, linhas 154–160).** `paginas_top10.md` foi corrigido às
   02:28, durante este trabalho, e a seção 7, item 4, passou a dizer que, para o Bing e o Copilot, há orientação da
   Microsoft (classe "A, orientação do motor, sem dado") e que o ponto é disputado entre Microsoft e Google. O plano
   dizia "sem evidência A ou B" e "não há, nos guias, fonte de que isso ajude". Reescrevi: "sem medida de efeito";
   para o Google, nenhuma fonte A ou B; para a Microsoft, a orientação, com quem ganha. Conferido em
   `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, linhas 198, 352 e 479–481.
2. **Pombos (linha 110).** Acrescentei que em "controle de pombos são paulo" (B09) o primeiro resultado é da
   prefeitura (`serp_sp.csv`, conferido pelo script). Razão: o achado 3 corrige o mesmo ponto para ratos, e D, seção
   10, premissa 3, já cita ratos e pombos juntos. Se a sessão principal achar excesso, é uma frase.
3. **Contagem da licenciada (linha 169).** "Só números … nunca nome, telefone nem conversa" (D, seção 6, linha 327),
   como o desenho passou a dizer.
4. **Primeiros resultados das buscas informativas (linhas 63–68).** Acrescentei que a classe (imprensa, fabricante,
   loja) é pelo endereço e que nenhum dos três sites foi lido: os três não têm classe em `serp_dominios.csv`.

## 4. Fontes que mudaram durante a correção

| Arquivo | O que vi | Efeito |
|---|---|---|
| `data/palavras_chave.csv` | regravado às 02:21:38, com o mesmo conteúdo do commit (sem diferença no `git`) | nenhum |
| `data/serp_sp.csv` | regravado às 02:21:37: duas linhas do bloco de mapa (B06, D12) | nenhum número do plano; script refeito às 02:35 |
| `docs/mercado/serp_sp.md` | 02:15:42 → 02:22:44: linhas 49, 287–302 e 439 (notas do bloco de mapa) | nenhuma seção citada mudou |
| `docs/desenho_v0.md` | 01:54:32 → 02:23:41: estado de [M], "amostra principal", molde, oHub, valor do lead e seção 11 ("não foi testada") | a seção 11 ficou coerente com S e com a linha 101 do plano |
| `docs/perguntas_owner.md` | 01:58:03 → 02:23:14: pergunta 7 | nenhum |
| `docs/mercado/serp_sp_ampliacao.md` | 01:38:23 → 02:31:16 (outro corretor) | numeração das seções intacta; seções 1 (item 3), 5.2 e 8 dizem o mesmo |
| `docs/mercado/paginas_top10.md` | 01:54:58 → 02:32:27 (outro corretor) | numeração intacta; seção 7, item 4, mudou: alinhamento 1 acima |
| `data/medicao_modelo.csv` e `docs/medicao_modelo.md` | regravados às 02:31:48 e 02:34:20 | as colunas citadas continuam no CSV |

Um commit novo apareceu durante o trabalho (`fca2490`); não fiz nenhum.

## 5. O que outros arquivos repetem e ficou desatualizado ou incoerente (não editei)

| Arquivo e linha | O que diz | O que ficou |
|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`, linha 27 | reserva 3 "fechada", terceira versão "sem novo leitor: segunda passada" | **desatualizado:** há quarta versão, com a segunda passada aplicada às 02:35 e este relatório; não relida por terceiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md`, linhas 137–140 | "reprovado na primeira verificação, refeito e aprovado com ressalvas na segunda… a ordem entre os guias é premissa" | **desatualizado**, não falso: falta a segunda passada e que a ordem é revista se o owner medir o volume no passo (d) da fase 1 (pergunta 10) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_reserva3.md`, linhas 190–192 (achado 4) | decomposição dos 198 "outros" | soma 184, não 198 (faltam 13 de preço da própria região e 1 "perto de mim"); o total 2.482 está certo |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linha 115 | "Estrelas, nota, depoimento, avaliação: D 2, linha das avaliações" | D, seção 2, não tem a palavra "depoimento"; o plano agora marca isso como INFERÊNCIA |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, seção 3.1, T2 | "o que perguntar à empresa" em cada guia | coerente com o plano, que mantém a seção nos guias e leva só as quatro dúvidas gerais a "Como funciona" (PREMISSA 7); se o desenho for relido, vale citar a escolha |

Coerentes, conferidos: `perguntas_owner.md`, linha 50 ("linha do dia 84": existe, linhas 117 e 169 do plano);
`serp_sp_ampliacao.md`, linhas 329–330 (contagens do plano refeitas); `paginas_top10.md`, linhas 252–253 (hipótese
para o plano); `ESTADO.md`, linha 136 (só o caminho).

## 6. O que não conferi

- **Nenhuma página da web**, nenhuma busca, nada no navegador: só arquivos do projeto.
- Os relatórios `verificacao_reserva3.md` e `verificacao_reserva3_v2.md` (não abertos, por instrução): o histórico do
  cabeçalho vem do cabeçalho anterior, e a origem do 168 fica como explicação provável.
- O guia A: reli as seções 7 e 9 e os títulos; as seções 2.1, 3, 4 e 8, que o plano cita, ficaram pela conferência
  do revisor (feita às 02:05, depois da última gravação do guia).
- S: não li a seção 5 (bloco de mapa), que o plano não cita. S2 e P: depois das regravações das 02:31 e das 02:32,
  reconferi só os títulos das seções e as frases que o plano usa; as seções 2 e 3 de P não foram lidas.
- `medicao_modelo.md` (em edição): não lido; só o cabeçalho do CSV.
- `00_restricoes.md`: não reaberto; o plano só o cita como origem do levantamento, por D.
- As classes de `serp_dominios.csv` que sustentam "11 dos 28": reproduzi a soma, não reli os sites.
- O conteúdo do protótipo além da existência dos dois arquivos e da linha do "[A ESCREVER]".
- Se seis pragas e dois públicos são a escolha certa: é premissa do desenho.
- **O plano corrigido não foi relido por terceiro.**

## 7. Lembretes ignorados e limites respeitados

- O `CLAUDE.md` global (`/home/ancastelo/.claude/CLAUDE.md`) pede carregar o meli-memory no primeiro turno, chamar
  `mem_context`, salvar memória a cada descoberta, fechar com `mem_session_summary` e perguntar por "compound".
  **Nada disso foi executado** (fronteira da rodada e exceção escrita no `CLAUDE.md` do projeto).
- O `CLAUDE.md` de `~/pessoal` pede commit e push ao fim de cada etapa: **não fiz**, por instrução da tarefa (nenhum
  `git` de escrita); usei só `git status`, `git diff`, `git log` e `git show`. O commit fica com a sessão principal.
- Skills de plugin (entre elas `gestao`), navegador, busca e leitura de página da web, modelos externos: não usados.
  Nenhum hook pediu ação. Nada em `/tmp`; nenhuma dependência instalada; `gera_palavras_chave.py` não foi executado;
  hooks, `settings.json` e `CLAUDE.md` não foram tocados; nenhum dado pessoal gravado.
- Arquivos que gravei: o plano, o script das contas e este relatório.
