# Segunda passada — item 6 (desenho do sistema, versão 0)

- **Quem:** revisor novo, em contexto limpo, sem a conclusão de ninguém. Não abri nenhum arquivo `verificacao*` nem
  `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` e ignorei o que o próprio artefato
  diz sobre verificações anteriores.
- **Quando:** sábado, 14/11/2026, das 01:21 às 01:31 de leitura e conferência; relatório gravado e revisto até
  01:34 (Brasília, horas lidas de `TZ=America/Sao_Paulo date`).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (442 linhas; último commit do arquivo:
  `39952c0`, 13/11 23:44). "L" neste relatório = linha do artefato.
- **Natureza:** conferência de arquivo contra arquivo. Não usei a web, o navegador nem busca ao vivo. O que encosta em
  norma é conferência de levantamento com fonte, **não parecer jurídico**.
- **Hooks e lembretes ignorados (1 linha):** o `CLAUDE.md` global pede carregar as ferramentas do meli-memory, chamar
  `mem_context`, salvar memória, resumir a sessão e perguntar por compound — **não executei nada disso** (regra da
  rodada e `CLAUDE.md` do projeto).

## Veredito

**APROVADO COM RESSALVAS.**

- Sorteio: **0 falha em 12** (semente e lista abaixo).
- Remissões: conferi as 140 que identifiquei. **Nenhuma aponta para trecho inexistente e nenhum número diverge da
  fonte**; 128 conferem sem ressalva e 12 conferem em parte (força ou classe um pouco acima da fonte, ou remissão
  incompleta). As linhas de `00_restricoes.md` citadas batem uma a uma.
- `serp_sp.md` foi corrigido depois do desenho (commit `8443220`, 14/11 00:08, e `d2f5b35`, 01:11): comparei a versão
  de 13/11 23:42 com a atual. **Nenhum número citado pelo desenho mudou e nenhuma seção citada mudou de lugar.** Mudou
  a força de uma frase (seção 8: a base do "texto de molde" passou a ser chamada de fraca) e o estado do item (fechado).
- O portão está cumprido parte por parte, e o desenho não depende de perfil fora da regra, endereço fictício,
  avaliação fabricada, link comprado, repasse sem consentimento específico nem API do WhatsApp.
- As ressalvas que pesam são de conteúdo, não de citação: o que o aviso e o texto de consentimento dizem sobre o que
  o site guarda (achados 1 a 5), premissas que faltam na lista única (achado 6), estado desatualizado (achado 7) e a
  ampliação da amostra, que enfraquece dois trechos (achado 8).

## O que abri

| Arquivo (em `/home/ancastelo/pessoal/SEO_Project/`) | Quanto li |
|---|---|
| `docs/fds-2026-11-13/SISTEMA.md` | seções "Como trabalhar" a "Forma" (linhas 15–118) |
| `docs/fds-2026-11-13/RODADA.md` | inteiro (portão do item 6, regra de evidência, fila de reserva) |
| `docs/desenho_v0.md` | inteiro |
| `docs/estudo/00_restricoes.md` | inteiro (499 linhas) |
| `docs/estudo/01_google_organico.md` | linhas 1–400 (cabeçalho, seções 1 a 9) |
| `docs/estudo/02_google_maps_perfil.md` | seções 3.1, 7, 8, 9, 10 e "O que não cabe para um gerador de leads" (linhas 197–216 e 360–486) |
| `docs/estudo/03_respostas_de_ia.md` | seções 1.1 a 1.6, 3, 7.1 a 7.3, "consenso" e "disputado" (linhas 58–145, 179–218, 336–494) |
| `docs/estudo/03b_chatgpt.md` | seção 2 (linhas 187–228), seção 9 (linhas 467–527), tabela de fontes (F13, F25) |
| `docs/estudo/03b_chatgpt_roteiro_de_teste.md` | seção 4 (linhas 207–260) |
| `docs/mercado/serp_sp.md` | inteiro (563 linhas) e o `git diff` entre `cfd2330` (13/11 23:42) e a versão atual |
| `docs/mercado/serp_sp_ampliacao.md` | inteiro (283 linhas) |
| `docs/modelos_de_negocio.md` | linhas 1–64, 149–189, 236–359, 448–475, 590–705 |
| `docs/contrato_pontos.md` | seção 7 (linhas 172–184) e buscas pontuais (seções 5.2 e 12.3) |
| `docs/perguntas_owner.md` | tabela das 10 perguntas e "O que não virou pergunta" |
| `docs/fds-2026-11-13/PAINEL.md` | linhas 1–60 (estado dos itens) |
| `data/serp_dominios.csv` | contagem por classe e pela coluna `licenca_exibida` |
| `prototipo/` | só o `href` do botão, o aviso ao lado dele e o `robots.txt` (para a frase de L210–211) |
| `git log` de cada arquivo citado | datas do último commit; `git diff` das edições do desenho de 22:38 e de 23:44 |

## Tabela de remissões (todas)

Legenda: **C** = confere (o trecho existe, diz aquilo, com o mesmo número e a mesma força; a classe dita é a certa);
**P** = confere em parte (explicado). Não há nenhuma linha "não confere". [R] `00_restricoes.md`, [A]
`01_google_organico.md`, [B] `02_google_maps_perfil.md`, [C] `03_respostas_de_ia.md`, [G] `03b_chatgpt.md`, [S]
`serp_sp.md`, [M] `modelos_de_negocio.md`.

| # | L | Remissão | O que o desenho apoia nela | Res. | Nota |
|---|---|---|---|---|---|
| 1 | 33–36 | [R] "O que as quatro restrições… deixam de pé", 468–477 | site intermediário, nomeia executora, licença e órgão; sem perfil; sem central de WhatsApp | C | itens 1 a 4 das linhas 470–477 |
| 2 | 37 | [S] 7.3, item 1 | 568 de 709 (80%) | C | linhas 341–342 de [S] |
| 3 | 37–38 | [S] seção 8 | 50 dos 67 sites têm página por local | C | linha 387 |
| 4 | 38–39 | [S] 7.3, item 4 | 12 de 67 mostram o número | C | linha 364 |
| 5 | 39–41 | [S] 7.2 e 7.3, item 5 | 11 domínios, 37 de 79 (47%), 28 de dois, 30% dos três primeiros; "não prova" | C | 70 de 237 = 29,5%; ver achado 14 (11 × 12) |
| 6 | 44–45 | [A] 2.1 e 2.2 | "centenas de páginas por bairro com o nome trocado: é o exemplo de página de entrada da política" | P | a política exemplifica páginas por região ou cidade que afunilam (linha 157); "bairro com nome trocado" é inferência do guia (linhas 41 e 184–185). Falta a marca INFERÊNCIA (achado 9) |
| 7 | 47–49 | [R] (d) "Os dois desenhos", 432–446 | botão na versão 0; formulário depois | C | |
| 8 | 50–52 | [R] (c) "Vereditos", 358–364 | uma empresa; várias, nomeadas | C | "até mais duas" é escolha, marcada em 5.2 |
| 9 | 53–54 | [A] seção 8 | Search Console; sem rastreador automático | C | linhas 360 e 367 |
| 10 | 63 | [R] (b) (iii), 246–251; [A] seção 3 "Transparência de um intermediário" | site se declara intermediário — INFERÊNCIA | C | |
| 11 | 64 | [R] 250–251 | não usar "nossa equipe" — PREMISSA | C | "escolha de desenho" está na linha 250 |
| 12 | 65 | [R] quadro, linha 25 | sem perfil — classe A | C | |
| 13 | 66 | [A] seção 5 (`Organization`, `LocalBusiness`) | A (tipo) + INFERÊNCIA | C | linhas 275–276 |
| 14 | 67 | [R] quadro, 36–37 | sem número que conversa e repassa — "classe A" | P | pelo aplicativo é não conclusivo; pela definição do próprio desenho (L22–24) essa parte é PREMISSA de prudência (achado 10) |
| 15 | 68 | [R] quadro, 29; [A] seção 5 | não comprar, não copiar avaliação, sem estrelas — classe A | P | a linha 29 de [R] trata de avaliação no perfil do Google; "sem estrelas" é a recomendação do guia (linha 279, "Na fase atual"), mais ampla que a regra A (achado 11) |
| 16 | 69 | [A] 2.1; [C] 7.2 | não compra link nem menção; `rel="sponsored"` — A | C | [A] 164 e 166; [C] 358 |
| 17 | 70 | [A] seção 3; [C] 7.1; [G] seção 9, linha 10 | "quem somos" — A para a recomendação; PREMISSA para citação | C | |
| 18 | 85 | [S] 4.4 | consulta pública do estado apareceu numa busca | C | linhas 250–251 |
| 19 | 86 | [R] 243–244 | afirmação de preço pede prova guardada | C | |
| 20 | 89 | [A] 2.1, linhas 165 e 167 | não exigir link de volta | C | |
| 21 | 89 | [M] 4.2, 4.3, 4.6 | como a licenciada é cobrada | C | |
| 22 | 93 | [A] 2.2, "dois limites honestos" | não há número de páginas em fonte A ou B | C | a fonte fala de "páginas por bairro" (linhas 196–198) |
| 23 | 99 | [A] 2.1; [A] 2.2, 187–194 | A (texto) + INFERÊNCIA (aplicação) | C | |
| 24 | 100 | [S] 4.2 e 8 | 79% a 87%; "texto de molde com o nome trocado" | P | números conferem; [S] corrigido diz que a base é fraca ("cerca de dez sites", linhas 404–405) (achado 13) |
| 25 | 101 | [R] 186–187; [S] 7.3, itens 4 e 5 | art. 22; 12 de 67; 37 de 79 | C | |
| 26 | 102 | [A] seção 7, fecho | dúvida e comparação valem mais — PREMISSA | C | linhas 347–352 |
| 27 | 103 | [S] 4.2, grupo F | 68% e 1% | C | linhas 204 e 220–221 |
| 28 | 104 | [A] seção 4 (duplicidade) | uma busca e variações na mesma página — INFERÊNCIA | C | linha 255 |
| 29 | 111 | [R] (b) veredito, 257–258 | licenciada nomeada | C | |
| 30 | 113 | [A] 2.2, linha 189 | algo que só a página diz | C | |
| 31 | 114 | [A] 2.2, 191–192 | navegação região → bairro | C | |
| 32 | 120 | [A] seção 4 (link de título) | A | C | |
| 33 | 121 | [G] seção 9, linha 6 | abertura da página — PREMISSA | C | |
| 34 | 122 | [C] 7.1; [G] seção 9, linha 7 | fatos em texto visível | C | |
| 35 | 123 | [C] 7.1 | data de revisão — A (orientação, sem dado) | C | a orientação é sobretudo da Microsoft (10/02/2026) |
| 36 | 124 | [A] seção 4 (endereços) | "legíveis, minúsculas, sem acento, hífen" — classe A | P | o Google diz legível, hífen, idioma do público e acento codificado; "minúsculas e sem acento" é escolha do guia (linha 249) (achado 12) |
| 37 | 125 | [A] seção 4; 2.1, linha 163 | links internos; sem lista de bairros | C | |
| 38 | 126 | [A] seção 5 | `Organization`, `BreadcrumbList`, fim do `FAQPage` em 07/05/2026, `LocalBusiness` de terceiro | C | |
| 39 | 127 | [A] seção 4; [G] seção 9, linha 5 | sem dependência de script | C | |
| 40 | 128 | [A] seção 4 (celular; intersticiais) | A | C | |
| 41 | 129 | [G] seção 2 e seção 9, linhas 1–4; [C] 1.2 e 3 | `robots.txt` | C | linha 3 de [G] é A + B; linha 4 é premissa (marcada em L129 e na premissa 8) |
| 42 | 130 | [G] seção 9, linha 2 | IPs publicados | C | |
| 43 | 131 | [C] 1.2 | sem `nosnippet`; "Incluir" | C | |
| 44 | 132 | [A] seção 4 | sitemap; canônica | C | |
| 45 | 133 | [C] 1.1 e 7.2 | sem `llms.txt`, sem texto escondido | C | |
| 46 | 134 | [G] seção 9, linha 15 | registro de acesso bruto | C | |
| 47 | 135 | [R] "O que não foi lido", 488–493 | guia de cookies não lido | C | |
| 48 | 139 | [R] (b) (i)–(iv), 231–258 | base da seção 4 | C | |
| 49 | 147 | [R] 186–187 | nome como consta na licença — A | C | |
| 50 | 148 | [R] 209–213 | número como consta no documento | C | |
| 51 | 149 | [R] 235–236 | razão social e endereço — PREMISSA | C | |
| 52 | 150 | [S] 4.4 | consulta pública; funcionamento não lido | C | |
| 53 | 151 | [R] 257–258 | área atendida — PREMISSA | C | |
| 54 | 152 | [R] 217–218 e 233–235 | marca "Publicidade" — A | C | "pela presença" vai além de "posição ou destaque" (mais estrito; ver achado 6) |
| 55 | 157 | [R] 246–251 | faixa fixa — INFERÊNCIA | C | |
| 56 | 164 | [R] 188–189 e 239 | medo | C | |
| 57 | 165 | [R] 190–192 | "Aprovado" etc. | C | |
| 58 | 166 | [R] 193–194 e 241–242 | "inócuo" etc.; exemplo próprio | C | |
| 59 | 167 | [R] 243–244 | prova guardada | C | |
| 60 | 168 | [A] seção 3; [C] 7.2 | "a melhor" | C | [A]: 1 leitura; [C]: B fraca + restrição |
| 61 | 169 | [B] seção 7 | "garantido pelo Google" — inferência do guia | C | linha 370 |
| 62 | 170 | [B] 10.2 | promessa de posição | C | linha 451 |
| 63 | 173 | [A] seção 3, "Dedetização é YMYL?" | inferência do guia | C | |
| 64 | 177 | [R] quadro, 31; 253–262 | página sem empresa nomeada | C | |
| 65 | 188 | [R] (d) Desenho B, 438–441 | botão; link oficial | C | |
| 66 | 189 | [R] linha 439 (leitura só do subagente) | mensagem pré-preenchida | C | a marca [S] está na linha 439 |
| 67 | 190 | [R] 440–441 | citação "o site só registra o clique…" | C | literal; é limite descrito pelo estudo, não frase de norma |
| 68 | 191 | [R] 246–251 | conversa e contrato são da licenciada — INFERÊNCIA | C | |
| 69 | 203–204 | [R] linha 438 | botão abre direto | C | |
| 70 | 219–220 | [R] 488–493 | IP não levantado | C | |
| 71 | 221–223 | `contrato_pontos.md`, 7.1 | Marco Civil, art. 15, 6 meses, regulamento não lido | C | |
| 72 | 228–229 | [R] (c) 346–356; (d) 442–446 | base da Via B; variante é inferência | C | |
| 73 | 231 | [R] 342–344 | sem campo livre; nada de saúde | C | |
| 74 | 262 | [R] 349–350 | art. 9º, III e IV | C | |
| 75 | 263 | [R] 296–297 e 305 | art. 5º, XII; art. 8º, § 4º | C | |
| 76 | 264 | [R] 298–302; 363–364 | art. 7º, § 5º; art. 8º, § 1º; caixa pré-marcada | C | |
| 77 | 265 | [R] 350–351; 398 | art. 9º, V; opt-in nomeia quem envia | C | |
| 78 | 266 | [R] 352 | art. 6º, III | C | |
| 79 | 267 | [R] 352 | art. 18, VIII | C | |
| 80 | 268 | [R] 306–307 e 324–325 | art. 8º, § 5º; art. 18, VI | C | |
| 81 | 269 | [R] 328–331 | art. 18, § 6º | C | |
| 82 | 270 | [R] 360–361 | sem repasse posterior — inferência | C | |
| 83 | 273 | [R] linha 368 | a lei não fixa número máximo | C | |
| 84 | 273–274 | [M] seção 6 e seção 8, "Disputado" | 4 prestadores; 6 no oHub (2021); 4 × 3 no GetNinjas | C | [M] 594–596 e 675–677 |
| 85 | 275 | [R] 442–446 | a licenciada chama | C | |
| 86 | 278 | [M] 4.2 | o canal é escolha do item 6 | C | [M] linha 248 |
| 87 | 281–282 | [R] (c) 338–341 | Resolução 2/2022, arts. 9º, 11 e 13 | C | |
| 88 | 283 | [R] linha 320 | controladores: não conclusivo | C | |
| 89 | 284–285 | [R] 353–355; 355 | prova guardada; prazo não conclusivo | C | |
| 90 | 288 | [R] 332–334 | prazo de resposta não fixado | C | |
| 91 | 296 | [R] quadro 36–37; 448–451 | central de WhatsApp fora | C | |
| 92 | 297 | [R] 358–368 | sem envio a quem não foi marcado | C | |
| 93 | 298 | [R] 342–344 e 352 | não guardar conversa; sem CPF; nada de saúde | P | saúde e mínimo necessário estão lá; "guardar a conversa" está em 440–441, não citadas (achado 16) |
| 94 | 299 | [R] linha 356 | marketing é outra finalidade | C | |
| 95 | 300 | [R] 155–157; [M] 4.2, riscos, "Parceiro" | telefone do site | C | [M] linha 314 |
| 96 | 306 | [A] seção 8 | relatório de desempenho | C | |
| 97 | 307 | [C] 1.3 e 7.3 | relatório de IA, só impressões | C | |
| 98 | 308 | [A] seção 8; [S] 2.2, 2.3 (item 9), 2.4 | conferência manual; coleta por script; 80ª busca | C | |
| 99 | 309 | [G] seção 9, linha 15 | visitas dos robôs | C | |
| 100 | 310 | roteiro, seção 4 | 30 perguntas, mensal, repetições obrigatórias | C | |
| 101 | 311 | [R] 440–441 | lead = toque | C | |
| 102 | 313 | [M] 4.0.1 | lead inválido por regra escrita | C | |
| 103 | 314 | [M] 4.2 e 4.6 | lead vendido; mensalidade da região | P | a mensalidade por região está em 4.3; 4.6 trata da forma de cobrança (achado 17) |
| 104 | 315 | [M] seção 7 | taxa de fechamento sem fonte brasileira | C | [M] linha 628 |
| 105 | 316 | [M] 4.2 e 4.6 | receita por página | P | o mesmo da linha 103 |
| 106 | 318–319 | [A] seção 8 | 28 dias contra 28; esperar o fim da atualização | P | a fonte diz "ao menos uma semana depois do fim" (linha 365) (achado 15) |
| 107 | 322 | [B] seção 9 | não medir por grade | C | linhas 402–403 |
| 108 | 323 | [A] seção 8 | nota de "autoridade" | C | linha 366 |
| 109 | 329 | [A] 2.1 | conteúdo em escala | C | |
| 110 | 330 | [A] seção 4 | descrição por programa | C | linha 247 |
| 111 | 331 | [R] 223–224 | CDC, art. 38 | C | |
| 112 | 333 | [A] seção 3 | IA generativa | C | linha 218 |
| 113 | 335 | [A] seção 8 | nunca por robô | C | |
| 114 | 336 | [R] quadro 29; [B] 3.1 | "pedir, premiar ou escrever avaliação: nunca" | P | [B] 3.1 permite pedir sem incentivo (linha 208); o "nunca pedir" é a premissa 17, não a fonte (achado 18) |
| 115 | 338 | [A] 2.2 | ritmo não documentado — PREMISSA | C | linha 193 |
| 116 | 349 | [A] seção 9 | o Google não dá prazo | C | linha 386 |
| 117 | 350 | [M] seção 7 | taxa de fechamento que ninguém tem | C | |
| 118 | 354–356 | [M] seção 1, item 9; 4.3; 4.6 | "leitura minha, não fato" — INFERÊNCIA | C | [M] linha 58 |
| 119 | 357 | [M] 4.3, riscos, "Propaganda" | página vira publicidade | C | [M] linha 355 |
| 120 | 360 | [M] 4.2 | toque como unidade na Via A | C | [M] linhas 245–246 |
| 121 | 363 | [M] seção 7 | R$ 20 a 60 não se confirma nem se derruba | C | [M] linha 633 |
| 122 | 364–365 | [A] seção 9 | semanas; 6 a 12 meses — PREMISSA do guia | C | linhas 391–393 |
| 123 | 366–367 | [S] seção 3 | bloco de mapa em 68 de 79 | C | |
| 124 | 367 | [B] seção 10 | roteiro e limites | C | |
| 125 | 368 | [B] "O que não cabe…", fecho | o perfil é dela | C | linhas 482–483 |
| 126 | 376 | [R] (a); [S] seção 3 | 68 e 60 de 79 | C | |
| 127 | 377 | [R] (b) | "concorre"; CVS 9/2000; número na capital | C | [R] 195–196, 200–203, 209–213, 254 |
| 128 | 378 | [R] (c) | art. 42; agenda da autoridade | C | [R] 310–311 e 317 |
| 129 | 379 | [R] (d) | termos de 23/09/2026 | C | [R] 383 e 386 |
| 130 | 385 | [M] seções 7 e 8 | sem fonte brasileira de preço, fechamento, disposição de pagar | C | |
| 131 | 386 | [S] 4.1 e 4.2 | 10 domínios, 39%; 13 domínios em 5 ou mais de 20 | C | |
| 132 | 387 | [S] seção 3; [C] "O que é disputado" | IA em 73 de 79; efeito disputado | C | |
| 133 | 388 | [M] 4.3, riscos | dependência de uma licenciada | C | [M] linha 358 |
| 134 | 389 | [A] 1.3 | atualização central em curso | C | linhas 113–118 |
| 135 | 390 | [R] 225–229 | responsabilidade: não levantada | C | |
| 136 | 391 | `perguntas_owner.md`, pergunta 1 | política do empregador | C | |
| 137 | 401–403 | [S] 7.3, itens 4 e 5 | premissa 1 | C | |
| 138 | 436–441 | [S] seção 12 | grupo H | P | nas três buscas de preço é **a mesma página de uma dedetizadora** em primeiro, não "páginas de dedetizadoras" (achado 19) |
| 139 | 20–21, 25–26, 430–437 | estado de [S] e de [M] | "[S] em verificação" | P | o item 4 está fechado desde 14/11 00:06 (`PAINEL.md`); desatualizado (achado 7) |
| 140 | 321 e 351 | `RODADA.md`, fila de reserva 5 e 4 | planilha e contrato | C | os dois arquivos já existem (achado 24) |

## Sorteio de 12 afirmações

Semente: `verificacao2-item6-20261114`, em `random.seed()` do Python 3, `random.sample(range(1, 141), 12)` sobre a
numeração da tabela acima. Saíram: 7, 8, 11, 31, 40, 46, 86, 95, 100, 113, 118, 130.

| # | L | Afirmação | Fonte aberta | Resultado |
|---|---|---|---|---|
| 7 | 47–49 | Versão 0 só com o botão; formulário desenhado para depois | [R] 432–446: Desenho B (438–441) e variante do formulário (442–446) | confere |
| 8 | 50–52 | Botão: uma empresa; formulário: a da página e até mais duas, nomeadas | [R] 358–364: uma — permitido com condição; várias — "dizer a quantas, e a quais ou onde ver a lista" | confere (o desenho é mais estrito) |
| 11 | 64 | Não usar "nossa equipe" — PREMISSA | [R] 250–251: "é **escolha de desenho** para não induzir a erro" | confere; classe certa |
| 31 | 114 | Bairro na navegação, não só destino de busca — INFERÊNCIA | [A] 191–192; o guia marca a tabela como inferência (184–185) | confere; classe certa |
| 40 | 128 | Celular primeiro; sem janela que cubra a tela — classe A | [A] 259 (indexação pelo celular, 2 leituras) e 261 (intersticiais, 1 leitura) | confere |
| 46 | 134 | Registro de acesso bruto — classe A, requisito de medição | [G] seção 9, linha 15: F1, A, "requisito de medição" | confere |
| 86 | 278 | [M] 4.2 deixa o canal de entrega para o desenho — PREMISSA | [M] linha 248: "por e-mail ou painel — o canal é escolha do item 6" | confere |
| 95 | 300 | Telefone do site só vale no site; gravação não levantada | [R] 155–157; [M] linha 314 | confere |
| 100 | 310 | Roteiro de 30 perguntas, mensal, com repetições obrigatórias | roteiro, seção 4, itens 1 e 2 (6 perguntas × 5 repetições, mais subamostra deslogada) | confere |
| 113 | 335 | Consultar o Google para saber a posição: nunca por robô | [A] linha 367 (tráfego gerado por máquina) | confere |
| 118 | 354–356 | Uma licenciada por região e por praga é "leitura minha, não fato" de [M] | [M] linha 58 (item 9) e linha 327 ("e, se quiser, por praga") | confere |
| 130 | 385 | Sem fonte brasileira de preço de lead exclusivo, fechamento e disposição de pagar | [M] linhas 625 e 628; "Não sei" 2 e 3 (691–692) | confere |

**0 falha em 12.**

## As seis conferências pedidas

### 1. O portão, parte por parte

| Elemento do portão | Onde está | Está? |
|---|---|---|
| Arquitetura: páginas por praga × região | seção 3.1 (T3), 3.2, 3.3 | sim |
| O que cada página precisa ter | seção 3.4; seção 4.1 | sim |
| Onde cada página exibe o que o item 2(b) exige | seção 4 (4.1 a 4.4) | sim |
| Captação e roteamento por WhatsApp | seção 5.1 (Via A) e 5.3 | sim |
| Texto de consentimento | seção 5.2 (L236–256), com a origem de cada parte (L260–270) | sim, com ressalvas (achados 2 e 25) |
| Para quantas empresas vai o contato | L50–52, L193–194, L272–274 | sim |
| Como a pessoa pede a exclusão | L195–198 (Via A) e L286–288 (Via B) | sim, com ressalva (achado 5) |
| Como medir: posição, clique, lead, lead vendido | seção 6 | sim |
| O que é automatizável | seção 7 | sim |
| Fases, com o que cada uma prova antes de gastar | seção 8 | sim; valores em reais não levantados, e o desenho diz isso (L342–343); ver achados 6(d) e 21 |
| "O que tornaria isto inviável", quatro restrições uma a uma | seção 9.1 | sim |
| Cada escolha aponta para o trecho do estudo | tabelas com coluna "Base" | sim (140 remissões; 12 em parte) |
| Premissa sem evidência A ou B marcada | marcas no corpo e seção 10 | em parte (achado 6) |
| Não depende de perfil fora da regra, endereço fictício, avaliação fabricada, link comprado | seções 2 e 9.3 | sim |

### 2. As quatro restrições

| Restrição | Veredito de [R] | O desenho respeita? |
|---|---|---|
| (a) perfil próprio, endereço de fachada, perfil da parceira com dado do site, avaliação incentivada | vedado (quadro, 25–27 e 29) | sim: sem perfil (L65), sem `LocalBusiness` próprio (L66), sem avaliação copiada ou comprada (L68), sem telefone do site (L300) |
| (a) gestão do perfil da licenciada | permitido com condição (linha 28) | sim: só na fase 5, remetendo a [B] seção 10; sem promessa de posição (L170) |
| (b) site de terceiro que divulga licenciadas | permitido com condição (linha 30) | sim: bloco "Quem executa" obrigatório (4.1), faixa de intermediário (4.2), lista do que não dizer (4.3) |
| (b) página de oferta sem empresa nomeada | não conclusivo (linha 31) | sim: o desenho não tem essa página (4.4) |
| (b) razão social e endereço (CVS 9/2000) | não conclusivo (linha 32) | sim: exibe por prudência, marcado PREMISSA (L149) |
| (c) repasse a uma ou a várias empresas | permitido com condição (33–34) | sim: caixa separada e não pré-marcada por empresa, cada uma nomeada; aviso às empresas na exclusão |
| (c) vender só com legítimo interesse | não conclusivo (linha 35) | sim: não usa |
| (d) número do site que tria e repassa (API) | vedado (linha 36) | sim: fora (L67, L296); o pedido da Via B chega por e-mail ou página restrita, "nunca por WhatsApp do site" (L276–278) |
| (d) o mesmo pelo aplicativo | não conclusivo (linha 37) | sim: não usa (falta marcar como prudência: achado 10) |
| (d) botão que abre o WhatsApp da licenciada | permitido com condição (linha 38) | sim: Via A |

Nada no desenho depende de perfil fora da regra, endereço fictício, avaliação fabricada, link comprado, repasse sem
consentimento específico ou uso da API do WhatsApp para repassar dados. Um ponto fica a descoberto: a conferência
mensal com a licenciada não diz que é só por número agregado (achado 4).

### 3. Aviso ao lado do botão e texto de consentimento

| Pergunta | Aviso do botão (L188) | Texto do formulário (L236–256) |
|---|---|---|
| Diz a verdade sobre o que o site registra? | Em parte. Diz o toque e o IP no registro do servidor. Lista "data, página e empresa", e o registro tem também hora e código (L190). Não diz a identificação do navegador, de que o próprio desenho depende (achados 1 e 22) | Em parte. Não diz que o envio do formulário também fica no registro do servidor com o IP, nem o que o site guarda como prova (L284–285). A frase "Guardamos só o registro de que a autorização foi dada e de que foi retirada" não diz o que esse registro contém (achado 2) |
| Para quantas e quais empresas vai? | Uma, a do botão, nomeada no próprio botão | A da página, nomeada com licença e órgão; até duas a mais, cada uma com a sua caixa, nomeada com licença e órgão |
| Como pede a exclusão? | O site não tem dado de contato; o pedido vai à empresa, "pelo canal que a licenciada informar" — nenhuma página tem campo para esse canal (achado 5). O e-mail do site está na política | Página "Excluir meus dados" ou e-mail; o site apaga, avisa cada empresa e anota a data |

### 4. Premissas

As 34 marcas PREMISSA das seções 1 a 9 (em 33 linhas, de L43 a L364) têm, cada uma, um item correspondente na lista
da seção 10 (conferi uma a uma). Faltam na lista, ou estão sem marca no corpo, as do achado 6.

### 5. Coerência interna

- Números repetidos batem: 568 de 709; 12 de 67 (L38, L101, L402); 37 de 79 e 47% (L39, L101, L402–403); 68 de 79
  (L366, L376); 60 e 73 de 79; 19 a 29 páginas (L91, L349, L405: 16 fixas + 1 a 5 + 1 a 5 + 1 a 3); no máximo três
  empresas (L194, L247, L272, L406); 3 a 5 e 1 a 3 licenciadas (L348–349, L421); 3 meses e 6 a 12 meses (L349,
  L364, L409).
- As fases dizem o que cada uma prova e a despesa de cada uma. Falta o que o passo (d) da fase 1 prova (achado 21).
- Nada é dito como já feito: "Nada aqui foi publicado, comprado, cadastrado nem enviado" (L9–10); o botão do
  protótipo aponta para `#botao-de-exemplo`, como L210–211 afirma.
- Contradições: L289–290 contra L212–214 (achado 3); 11 contra 12 domínios (achado 14); campo de validade (achado 20).

### 6. Forma

Português; caminhos absolutos em tudo o que o owner abre; nenhum número de outro país convertido. Falta data e lugar
na definição de "OBSERVAÇÃO DA AMOSTRA" (achado 23) e uma vírgula em L348 (achado 21).

## `serp_sp_ampliacao.md` (posterior ao desenho, não verificado) — contradiz ou enfraquece algo?

Não contradiz nenhuma escolha. Enfraquece ou muda a leitura de quatro trechos:

1. **Licença × primeira posição.** Nas 40 buscas novas, os sites com número de licença têm 11 das 40 primeiras
   posições (28%), contra 37 de 79 (47%) na amostra principal (seção 5.3 da ampliação). O "não é raro no topo" de L40
   e os 47% de L39, L101 e L402 valem só para a primeira amostra. A própria ampliação conclui (seção 9, item 4) que o
   argumento para exibir a licença é a norma, não a posição — o que confirma a cautela do desenho.
2. **Ordem na página.** L376 diz que "o bloco de mapa e os anúncios ocupam a página". Nas 40 buscas (madrugada,
   computador), o resumo de IA abre a página em 38 de 39, o bloco de mapa vem antes do orgânico em 21 de 31, e o
   anúncio de texto vem **depois** do primeiro orgânico em 34 de 35; o primeiro orgânico fica abaixo da primeira tela
   em 23 de 40 (seção 4). Quem empurra o orgânico, nessa amostra, é o resumo de IA e o mapa. Reforça o risco de L387.
3. **Buscas com bairro.** Mais 20 bairros repetem o padrão: 88% de páginas por local, e em 17 de 20 os três primeiros
   são todos desse tipo (seção 1, item 1). O desenho não faz página de bairro; **falta dizer que, com isso, ele abre
   mão dessas buscas na versão 0** (32 das 79 da amostra principal; volume não medido).
4. **Praga com a cidade.** No grupo K, governo é o primeiro resultado em 3 de 10 buscas e aparece em 5 (seção 1, item
   3); na amostra principal, 12 dos 16 resultados das duas buscas de escorpião são de órgãos públicos. As páginas T2
   de escorpião e de pombos disputam com governo; a escolha das 6 pragas (premissa 3) não menciona isso.

## O que não conferi

- As fontes da web por trás dos guias (política do Google, RDC 622, LGPD, termos da Meta): esta passada confere o
  desenho contra os arquivos do projeto, não os arquivos contra a web.
- Os arquivos `verificacao*` e `correcoes*` (por instrução) e, portanto, o que L3–9 diz sobre eles.
- Os anexos de `00_restricoes.md`, as seções 10 a 13 de `01_google_organico.md`, as seções 1 a 6 de
  `02_google_maps_perfil.md`, as seções 1 e 3 a 8 de `03b_chatgpt.md` e as seções 2 e 3 de `modelos_de_negocio.md`:
  não são citadas pelo desenho.
- As contas de `serp_sp.md` e de `serp_sp_ampliacao.md` nos dados brutos (refiz só a contagem de classes e de
  `licenca_exibida` em `data/serp_dominios.csv`).
- O protótipo, além do botão, do aviso e do `robots.txt`.
- A correção jurídica de qualquer leitura de norma.

## Achados, com a correção pedida

### De conteúdo

1. **L212–213, L188 e T11 — o registro bruto guarda mais do que o desenho diz.** O desenho descreve o registro como
   "data, hora, endereço pedido e endereço IP", mas depende da identificação do navegador para ver os robôs (L134) e
   para descartar "acessos com identificação de robô conhecido" (L207–208). Redação pedida em L212–213: "…anota cada
   pedido com data, hora, endereço pedido, endereço IP **e a identificação do navegador (user-agent); se a hospedagem
   também anotar a página de origem, a política diz isso**". Em L188, trocar o fim do aviso por: "…e o servidor
   registra o acesso com o endereço IP e a identificação do navegador; veja a política de privacidade."
2. **L253–254 e L284–285 — o que sobra depois da exclusão não está definido, e o texto não fala do registro do
   servidor.** O texto promete "apagamos o seu pedido" e "guardamos só o registro de que a autorização foi dada e de
   que foi retirada"; L284–285 diz que a prova inclui o que a pessoa marcou e a que empresas o pedido foi. Falta dizer
   se esse registro mantém o telefone (ou outro identificador) — sem isso a frase não é conferível. Pedido: (a) em
   L284–285, dizer o que a prova contém depois da exclusão e marcar "a rever com o advogado"; (b) em L254, redação:
   "Guardamos só o registro da autorização e da retirada — [o que ele contém: a definir com o advogado] — e o registro
   de acesso do servidor, com o endereço IP, pelo prazo da política de privacidade."
3. **L289–290 contradiz L212–214.** "O formulário torna o site controlador de dados pessoais" supõe que na Via A ele
   não é; L214 diz que o IP "pode ser dado pessoal". Redação pedida: "o formulário faz o site tratar dado de contato
   (nome e telefone), com todas as obrigações da seção (c), antes de se saber se alguém clica. Na Via A o site só
   trata o registro de acesso com o IP, ponto não levantado (seção 5.1)."
4. **L313, L315, L350 e L379 — a conferência com a licenciada não diz que é só por número.** Se, para contar ou para
   disputar um lead, a licenciada mandar ao site nome, telefone ou captura da conversa, o aviso do botão ("não recebe
   o seu nome, o seu número nem a conversa") deixa de ser verdade e há repasse sem autorização da pessoa.
   `contrato_pontos.md`, seção 12.3, deixa a pergunta aberta. Pedido: acrescentar em L313 "…a licenciada informa só
   **números** (quantos contatos com código, quantos orçamentos, quantos serviços); nunca nome, telefone ou conversa
   de quem a procurou. Como conferir a contagem sem ver dado de consumidor está em aberto: PREMISSA, a rever com o
   advogado" e repetir a regra em L379.
5. **L195–198 — o canal de exclusão da licenciada não tem lugar em página nenhuma.** O desenho manda a pessoa pedir a
   exclusão "pelo canal que a licenciada informar", mas nem o bloco "Quem executa" (4.1) nem a ficha T7 (L84) têm
   esse campo. Pedido: acrescentar à T7 e à tabela 4.1 a linha "Contato da empresa para pedidos sobre dados pessoais,
   como ela informou — PREMISSA (que ela informe)".
6. **Seção 10 — premissas que faltam na lista única ou estão sem marca.**
   (a) Que ao menos uma licenciada aceite ser nomeada num site de terceiro, de graça na fase 2, e pague na fase 4: é
   a premissa de que tudo depende e só aparece como risco (L377, L385).
   (b) Que a licenciada informe preço por escrito e aceite publicá-lo com data (T9, L86); [S], seção 8, diz que preço
   à vista é raro.
   (c) Não ter WhatsApp do site nem pelo aplicativo: prudência diante de ponto não conclusivo (L67).
   (d) Em nome de quem o site responde: L239 pede "razão social e CNPJ do responsável", o que supõe pessoa jurídica.
   Não está marcado como DECISÃO DO OWNER nem aparece como despesa nas fases (emitir nota para cobrar, na fase 4,
   também depende disso). `perguntas_owner.md` já diz que o ponto "não foi levantado".
   (e) Marca "Publicidade" também "pela presença" (L152), mais estrita que [R] 233–235.
   (f) Que a hospedagem entregue o registro bruto, permita truncar o IP e apagar cedo (L215–217 diz "se a hospedagem
   permitir", sem marca).
   (g) Os dois públicos de T6 e as seis pragas de T2 como escolha sem base de volume.
   Pedido: acrescentar à seção 10 os itens 18 a 22, com (a) em primeiro lugar, e incluir (c) e (e) no item 17.
7. **L3–10, L20, L25–26, L430–437 — estado desatualizado.** O item 4 está **fechado** (verificado; correções
   aplicadas em 14/11 às 00:06, segundo `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`). Trocar
   "em verificação" por "fechado em 14/11/2026; nenhum número citado aqui mudou". O cabeçalho "Estado" também omite
   as edições de 13/11 às 22:38 (aviso do botão, marca "Publicidade", atalho fixo, segunda caixa do consentimento:
   commit `d4379c1`) e às 23:44 (nota do Marco Civil e do grupo H: commit `39952c0`), feitas depois da última leitura
   independente.
8. **Seção 11, L37–43, L376, L387 e premissa 1 — falta a ampliação.** Acrescentar à seção 11 um parágrafo "Ampliação,
   feita depois (14/11, 00:12 a 01:06; não verificada)" com os quatro pontos da seção acima, e:
   - em L40, depois de "não é raro no topo": "(na ampliação de 14/11, 11 das 40 primeiras posições, 28%)";
   - em L376: "o resumo de IA e o bloco de mapa vêm antes do orgânico na maior parte das 40 buscas da ampliação; os
     anúncios de texto, naquela madrugada, vieram depois";
   - em 9.2, linha nova: "O desenho abre mão das buscas com bairro na versão 0 | nelas, 87% a 88% dos resultados são
     páginas de bairro; volume não medido | [S], seção 4.2; ampliação, seção 1".

### Menores (força, classe, remissão, forma)

9. **L44–45:** trocar por "A política de spam do Google dá como exemplo de página de entrada páginas voltadas a
   regiões ou cidades que afunilam o usuário; aplicar isso a centenas de páginas de bairro com o nome trocado é
   inferência do guia [A, seções 2.1 e 2.2] (INFERÊNCIA)". A linha 99 já faz essa distinção.
10. **L67, coluna Marca:** "classe A (pela API) + PREMISSA de prudência (pelo aplicativo, não conclusivo)".
11. **L68, coluna Marca:** "classe A (não agregar avaliação de outros sites; o site não marca estrelas sobre si);
    'não mostrar estrela nenhuma' e 'não pedir' são PREMISSA, mais estritas que a regra". Dizer que a linha 29 de [R]
    trata do perfil do Google.
12. **L124, coluna Marca:** "classe A (legível, com hífen); minúsculas e sem acento são escolha do guia".
13. **L100:** depois de "texto de molde com o nome trocado", acrescentar "em cerca de dez sites — o próprio mapa
    chama essa base de fraca".
14. **L39, L101 e L402:** "os 11 domínios que o mostram" → "os 11 domínios classificados como 'empresa com número de
    licença'". São 12 os sites que mostram o número; o 12º está na classe "rede ou domínio satélite" ([S], seção 7.3,
    item 6; `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`: `licenca_exibida` = "sim" em 12 linhas,
    classe com licença em 11).
15. **L318–319:** "esperar ao menos uma semana depois do fim de uma atualização central".
16. **L298:** acrescentar "[R, linhas 440–441]" para "guardar a conversa".
17. **L314 e L316:** acrescentar "[M], seção 4.3" (é onde está a mensalidade por região).
18. **L336:** "Pedir avaliação em nome da licenciada, premiar ou escrever avaliação" e, na base, "pedir sem incentivo
    é permitido à licenciada ([B], seção 3.1); o site não pede por escolha (premissa 17)".
19. **L439–440:** "nas três de preço, a mesma página de 'tabela de preço' de uma dedetizadora está em primeiro".
20. **L329 e L331:** o aviso de "licença perto de vencer" pede um campo de validade que não está na planilha de L329
    nem no bloco 4.1; se a licença traz validade não foi levantado. Acrescentar o campo "validade, se constar do
    documento" ou tirar "perto de vencer".
21. **L348:** falta a vírgula em "os textos das seções 4 e 5, o tratamento do endereço IP…". O passo (d) não tem o
    que prova nem critério na coluna "Não passa de fase se…"; dizer que é linha de base e que o Planejador pede conta
    de anúncios criada pelo owner.
22. **L188 contra L190 e L311:** o aviso lista "data, página e empresa"; o registro tem "data e hora, página, empresa,
    código". Alinhar o aviso: "(data e hora, página, empresa e o código da mensagem)".
23. **L25:** acrescentar data e lugar à definição: "79 buscas em 13/11/2026, cidade de São Paulo, Brasil…".
24. **L320–321 e L351:** os dois arquivos já existem; apontar para
    `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md` e
    `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md`.
25. **L238–239 e L152 — dois pontos para a lista do advogado (L348, passo c), sem mudar o texto agora:** se o
    formulário deve dizer que a empresa pode pagar ao site pelo pedido (o texto só diz "não cobra nada de você"); e
    se a página com licenciada nomeada de graça, na fase 2, já pede a marca "Publicidade".
26. **L79 e premissa 3:** anotar que as buscas de escorpião são dominadas por órgãos públicos ([S], seção 1, item 7)
    e que governo é o primeiro em 3 das 10 buscas de praga nova da ampliação.
27. **L395–397:** acrescentar "cadastro do site como negócio local em diretório" ([C], seção 7.2, linha 364).
