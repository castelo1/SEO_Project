# Verificação independente — item 1 (Reenquadramento)

- **Data e hora:** sexta, 13/11/2026, 19:37:40 -03 (saída de `TZ=America/Sao_Paulo date`).
- **Quem verificou:** subagente em contexto limpo, sem a conclusão de quem produziu. Só leitura dentro de
  `/home/ancastelo/pessoal/SEO_Project`; único arquivo escrito: este. Sem web, sem navegador, sem subagente, sem
  memória corporativa, sem commit.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/ESTADO.md` (129 linhas na leitura; 128 quebras de linha) e
  o estado do git no commit `70850b3`.

## Portão (texto do `RODADA.md`, linha 59, sem reescrever)

> `docs/ESTADO.md` novo: o que o projeto é agora, o que do material antigo se aproveita (com caminho e linha) e o que
> fica como histórico. `PROMPT_PLANO.md` movido para `arquivo/2026-09_foco_anterior/` com `git mv`. Nada apagado

## VEREDITO: APROVADO — 3 falhas menores em 71 conferências

Proporção: 3/71 = 4,2 % (o limite é mais de 2 em 12 = 16,7 %). Contagem por bloco: 6 + 42 + 4 + 9 + 7 + 3. Nas 42 referências "caminho + linha" da seção 2,
conferidas **todas** (não amostra): 41 OK (5 com ressalva) e 1 FALHA. O portão está cumprido nas quatro partes.
As três falhas não bloqueiam, mas devem ser corrigidas (lista no fim).

## 1. O que o projeto é agora (ESTADO.md seção 1 × RODADA.md linhas 11–20)

| # | Conferência | Resultado | Evidência |
|---|---|---|---|
| 1.1 | A definição bate com as palavras do owner | OK, com ressalva | `RODADA.md` 13–15: "inteligência de SEO para conseguir e depois vender leads para esse tipo de empresa que atua aqui em São Paulo… Google, IA e Google Maps, incluindo site completo, leads por WhatsApp". `ESTADO.md` 8–10 diz o mesmo. Ressalvas: "empresas **licenciadas**" não está nas linhas 13–15 (vem do `CLAUDE.md` do projeto, linha 3); "inclusive a busca do ChatGPT" vem da linha 61 do `RODADA.md`, não das linhas 11–20 citadas |
| 1.2 | Endereço da decisão ("linhas 11–20; palavras do owner na linha 13–15") | OK | `RODADA.md` 11 (título), 13–15 (citação), 17–20 |
| 1.3 | Fase atual ("estudar, mapear, desenhar e prototipar em arquivo local") | OK | `RODADA.md` 19–20, literal |
| 1.4 | "Deixou de ser" o estudo de abrir uma dedetizadora | OK, com ressalva | `RODADA.md` 17–18 lista simulador, parecer e curadoria de custos. `ESTADO.md` 16–17 acrescenta "plano de saída do emprego, estágios de virar operador": extensão coerente, mas não está nas palavras do owner |
| 1.5 | Algo do foco antigo apresentado como atual? | OK (nada) | Seção 2 inteira vem marcada como "hipótese com endereço, nunca como fato" (`ESTADO.md` 21–23); nenhum item do simulador, do parecer ou da operação aparece como entregável |
| 1.6 | Data e hora do cabeçalho ("13/11/2026 (sexta), 19:55 Brasília") | **FALHA** | 13/11/2026 é sexta (`date -d 2026-11-13 +%A`). Mas o arquivo foi gravado às 19:33:14 (`stat`), o commit é de 19:33:32 (`git log`) e esta verificação começou às 19:36. 19:55 ainda não tinha acontecido: a hora foi estimada, não lida de `date` |

## 2. Referências "caminho + linha" da seção 2 — todas as 42

Abri cada arquivo nas linhas citadas. `R01`…`R04` = `research/01_regulacao_licencas.md`,
`research/02_mercado_servicos_precos.md`, `research/03_modelos_negocio_escala.md`,
`research/04_mao_de_obra_custos_operacao.md`; `PP` = `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md`.

### 2.1 Quatro afirmações que decidem o modelo (11 endereços)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.1 | `R03` linha 13 | OK | Perfil de empresa: "lead generation agents or companies" inelegíveis; "exige contato presencial e endereço real" |
| 2.2 | `R03` linhas 102–108 | OK | 102: perfil "Proibido" para geração de leads, fonte primária; 103: endereço real, suspensão; 108: sem perfil, só orgânico e anúncios. As linhas 104–105 tratam de outro tema (concorrência, ganhos), mas o intervalo é o do `RODADA.md` |
| 2.3 | `R01` linha 44 | OK, com ressalva | Art. 22: identificação nos órgãos e número da licença; proíbe provocar temor, "aprovado/recomendado pela Vigilância Sanitária", e "inócuo", "seguro", "atóxico" **sem registro**. O `ESTADO.md` omite a ressalva "sem registro" e a proibição de provocar temor |
| 2.4 | `R01` linhas 157–159 | OK | 157: anunciar sem identificar a executora e a licença (art. 22); 158: comprovante com a marca do site; 159: "formato seguro" |
| 2.5 | `R01` linha 188 | OK | Violar o art. 22 é infração sanitária; CDC arts. 37–38 |
| 2.6 | `R03` linha 167 | OK | LGPD: "autorizo repassar meu contato a até N empresas licenciadas", literal |
| 2.7 | `R03` linha 91 | OK, com ressalva | Fala de consentimento para **contato futuro** da lista de clientes, não do repasse |
| 2.8 | `R03` linha 165 | OK, com ressalva | "opt-in LGPD" como ativo no conflito de canal; também não trata do repasse |
| 2.9 | `PP` linha 50 | OK, com ressalva | Linha 50: "O lead vale pouco (R$ 20–60, Baixa)… Receita"; o número "R$ 3–10k/mês" está na linha **51**. O arquivo movido é idêntico ao da raiz (mesmo blob `3a6d889`), então a numeração não mudou |
| 2.10 | `R03` linhas 15–16 | OK | 15: lead ~R$ 20–60 (estimativa Baixa); 16: conta de R$ 3.000/mês a R$ 40 por lead |
| 2.11 | `R03` linhas 79–83 | OK | 79: título 3.3; 82: faixa mín R$ 20 / base R$ 35 / máx R$ 60 (Baixa); 83: comissão |

### 2.2 Regulação (8 endereços)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.12 | `R01` linhas 28–47 | OK | Tabela da RDC 622 do cabeçalho (28) ao EPI (47); art. 5 (32), comprovante (41), nota fiscal (43), propaganda (44), sanções (45) |
| 2.13 | `R01` linhas 153–160 | OK | 153: título 6.1; 155–158: o que torna irregular; 159: formato seguro (diretório ou comparador, contratação direta, receita paga pela dedetizadora); 160: terceirização |
| 2.14 | `R01` linhas 162–165 | OK | 162: título 6.2; 163: CDC, solidariedade; 164: Nota Técnica Procon-MG 05/2025; 165: consequência |
| 2.15 | `R03` linha 163 | OK | "Há corrente contrária: a solidariedade não é automática…" (ConJur 2026, STJ 2021) |
| 2.16 | `R01` linha 14 | OK | "Na capital, quem licencia é o Estado… interpretação minha (Média)" |
| 2.17 | `R01` linhas 78–84 | OK | Seção 3.3 inteira; linha 82 marca a conclusão como interpretação |
| 2.18 | `R01` linha 130 | OK | "Veículo para gerar leads": CNPJ de publicidade pode ser MEI (7319-0/02, 7319-0/99) |
| 2.19 | `R04` linhas 276–283 | OK | 276: título 8; 280: art. 19, "revenda com a sua marca" conflita; 283: intermediação declarada, comprovante em nome da parceira |

### 2.3 Demanda e conteúdo (7 endereços)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.20 | `R01` linhas 93–100 | OK | 93: título 3.5; 94–98: Lei 12.268/1996, comprovante de no máximo 6 meses; 100: sem lei para condomínios |
| 2.21 | `R01` linhas 134–147 | OK | Seção 5 inteira, do título (134) à nota (147) |
| 2.22 | `R02` linhas 93–109 | OK | Tabela do catálogo, do cabeçalho (93) à fumigação (109), com público, recorrência e sazonalidade |
| 2.23 | `data/servicos.csv` "21 serviços, com fonte e confiança por linha" | OK | 21 registros + cabeçalho; colunas `fonte` e `confianca` preenchidas nos 21 (conferido com o módulo `csv`) |
| 2.24 | `R02` linhas 164–176 ("pico de outubro a março; cupim de setembro a dezembro") | **FALHA** | "Cupim, setembro a dezembro" está na linha 170. "Pico de outubro a março" **não está** no intervalo: 168 diz "+15 % na primavera/verão", 169 "outubro a maio" (dengue), 171 "set–mar" (escorpião). A frase está na linha **25** do mesmo arquivo |
| 2.25 | `R02` linha 173 | OK | "Não obtido" (volume de busca absoluto) |
| 2.26 | `R02` linhas 153–160 | OK | 153: título 4.3; 157: "golpe do cupim"; 158: cobrança sem orçamento; 160: leitura (medo de golpe) |

### 2.4 Concorrência na busca (6 endereços)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.27 | `R02` linhas 26–30 | OK | 27: quase não aparecem empresas do bairro; dominam sites da cidade inteira com página por bairro |
| 2.28 | `R02` linhas 180–198 | OK | Seção 6, do título (180) à lacuna do Maps (198) |
| 2.29 | `data/concorrentes_sp.csv` "21 linhas" | OK | 21 registros + cabeçalho |
| 2.30 | `R03` linha 14 | OK | Redes de sites-satélite; cauda longa bairro × praga |
| 2.31 | `R03` linhas 97–111 | OK | Tabela de SEO local (97–105) e "leitura" (107–111); cauda longa na 109 |
| 2.32 | `R01` linhas 167–171 | OK | 167: título 6.3; 168: GetNinjas; 169: Triider, Sindiconet; 170: anúncios de serviços locais fora do Brasil; 171: Habitissimo |

### 2.5 Preço do serviço e do lead (9 endereços)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.33 | `R02` linhas 12–24 | OK | 12–20: preços avulsos; 21–24: contratos de empresa |
| 2.34 | `R02` linhas 118–150 | OK | Seção 4 (título na 118) até o fim da tabela de contratos (149) |
| 2.35 | `R02` linha 248 | OK | "Tabelas de preço… são material de SEO, não preço efetivamente praticado" |
| 2.36 | `R03` linhas 53–91 | OK | 3.1 (53) preço do lead e do clique; 3.2 (70) fechamento; 3.3 (79) quanto pode pagar; 3.4 (85–91) como evitar o "furo" |
| 2.37 | `R03` linha 6 | OK | Aviso: números dos Estados Unidos vêm de agências que vendem leads |
| 2.38 | `R04` linhas 228–250 | OK | Seção 7, do título (228) à nota do auxiliar (249); 7.1 começa na 251 |
| 2.39 | `R03` linhas 29–30 | OK | Modelos (a) e (b) na tabela |
| 2.40 | `R03` linhas 41–44 | OK, com ressalva | 41: (a); 42: (b) e o caso de Nova York ("caso único, autor vende curso"). As linhas 43–44 são o modelo (c) e o art. 22 em sites de leads: o intervalo é mais largo que a descrição |
| 2.41 | `R03` linhas 156–168 | OK | Seção 7 (título na 156): Google (160), parceiro (161), sem licença (162), propaganda (164), inadimplência (166), LGPD (167) |

### 2.6 Lembrete (1 endereço)

| # | Endereço citado | Resultado | O que encontrei |
|---|---|---|---|
| 2.42 | `PP` linha 118 | OK | "verificar a política interna de atividade paralela/conflito de interesse do empregador"; "(lembrete, não pesquisar)" está na 119 |

## 3. As quatro afirmações que o `RODADA.md` manda reconferir (linhas 27–31)

| # | Afirmação | Resultado | Evidência |
|---|---|---|---|
| 3.1 | Perfil de empresa inelegível para quem só gera leads (`R03` 13 e 102–108) | OK | `ESTADO.md` linha 29, mesmo endereço |
| 3.2 | Propaganda identifica a executora e a licença (`R01` 44 e 157–159) | OK | `ESTADO.md` linha 30, mesmo endereço, mais a 188 |
| 3.3 | Repasse exige consentimento (`R03` 167) | OK | `ESTADO.md` linha 31, mesmo endereço, mais 91 e 165 |
| 3.4 | Lead de R$ 20–60 e receita de R$ 3–10 mil por mês (`PROMPT_PLANO.md` 50) | OK | `ESTADO.md` linha 32, já com o caminho novo; a linha 50 existe em `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` e é idêntica à da raiz |

## 4. Seção de histórico (ESTADO.md seção 3)

| # | Conferência | Resultado | Evidência |
|---|---|---|---|
| 4.1 | `PP` é do foco antigo | OK | `PP` 1 (título), 13 (gatilho), 80–88 (E0–E5), 94 (simulador), 113 (parecer), 115 (playbook de 30 dias) |
| 4.2 | `FICHA.md`: itens P0–P8, marcada como superada no topo | OK | `FICHA.md` 1–3 e 59–68 |
| 4.3 | `REVISAO_V2.md`: já aplicada, registro | OK | `REVISAO_V2.md` 1–2 |
| 4.4 | `R01` seções 3.2–3.4, 3.6–3.7, 4, 7 e 8 existem e são de quem opera | OK | Títulos nas linhas 67, 78, 86, 102, 113, 120, 175, 192 |
| 4.5 | `R02` seções 2, 7 e 8 | OK | Títulos nas linhas 40 (tamanho do mercado), 202 (por onde começar), 220 (franquias) |
| 4.6 | `R03` seções 5 e 6 e modelos (c)–(h) | OK | Títulos nas linhas 115 e 138; modelos nas linhas 31–37 e 43–47 |
| 4.7 | `R04` seções 2–7 e `data/custos_operacao.csv` (79 itens) | OK | Títulos nas linhas 47, 123, 144, 182, 211, 228; CSV com 79 registros + cabeçalho |
| 4.8 | As duas listas não se contradizem | **FALHA** | Cinco trechos citados como aproveitados na seção 2 estão dentro de seções que a seção 3 chama de "só histórico": `R01` 78–84 (seção 3.3), `R01` 130 (seção 4), `R01` 188 (seção 7), `R03` 43 (modelo c, dentro de 41–44), `R04` 228–250 (seção 7) |
| 4.9 | Material antigo relevante para o foco novo fora das duas listas | OK, com ressalva (não exigido pelo portão) | Ficaram sem menção: `R03` seção 8 (172–185: custo do clique em São Paulo "não confiável", preço por contato no GetNinjas, e a incerteza "se as dedetizadoras pagam por lead") e seção 9 (189–197); `R01` linha 227 (a legalidade é inferência, sem parecer; consulta a advogado) e linha 18; `R02` linha 255 (Maps, Trends e planejador não coletados); `R04` 284–285 (repasse estimado de 60–75 %, que o `PP` 64–65 aponta como conflito com `R01`); `R01` seção 3.1 e os resumos executivos não estão em lista alguma. `docs/fds-2026-11-13/EXEMPLOS_X.md` (insumo do item 3) não aparece na seção 4 |

## 5. Git

| # | Conferência | Resultado | Evidência (comando e saída) |
|---|---|---|---|
| 5.1 | O histórico segue a renomeação | OK | `git log --stat --follow -3 -- arquivo/2026-09_foco_anterior/PROMPT_PLANO.md`: `70850b3` "PROMPT_PLANO.md => arquivo/2026-09_foco_anterior/PROMPT_PLANO.md | 0", depois `2866541` (127 inserções) |
| 5.2 | É renomeação, não apagar + criar | OK | `git show --stat --summary HEAD`: "rename PROMPT_PLANO.md => arquivo/2026-09_foco_anterior/PROMPT_PLANO.md (100%)"; `git diff --name-status -M 1b8b202 HEAD`: `R100`. Mesmo blob nos dois lados (`3a6d88948a1f…`). O git não registra o comando usado; o resultado é o de um `git mv` |
| 5.3 | Nenhum arquivo apagado na história | OK | `git log --diff-filter=D --name-only`: vazio. Com `--no-renames` aparece só `PROMPT_PLANO.md` em `70850b3`, que é o lado de origem da renomeação |
| 5.4 | Os 15 arquivos de `1b8b202` continuam existindo | OK | 14 no mesmo caminho (`git cat-file -e HEAD:<arquivo>`); 1 movido com conteúdo idêntico. O commit acrescentou `docs/ESTADO.md` e `docs/fds-2026-11-13/PAINEL.md` |
| 5.5 | `git status --porcelain` | OK | Vazio às 19:36:12. Às 19:37:40 apareceu `?? docs/estudo/`: trabalho de outro item em andamento, criado por outro processo durante esta verificação; não pertence ao item 1 |
| 5.6 | `git rev-list --count @{u}..HEAD` | OK | `0`; ramo `main` segue `origin/main`. Conferido contra a referência local do remoto; não consultei o servidor |
| 5.7 | Remoto e identidade | OK | `origin git@github-pessoal:castelo1/SEO_Project.git`; autor do commit com o e-mail pessoal |

## 6. Forma

| # | Conferência | Resultado | Evidência |
|---|---|---|---|
| 6.1 | Português | OK | Arquivo inteiro em português; termos do ofício ("leads", "SEO") são os do owner |
| 6.2 | Dado pessoal do owner ou de terceiros no `ESTADO.md` | OK (nenhum) | `grep` por salário, empregador, telefone, e-mail, CPF, registro profissional: sem resultado. Só nomes de empresa e de norma |
| 6.3 | Afirmação factual nova sem endereço | OK, salvo a hora (1.6) | Os números do arquivo (R$ 20–60, R$ 3–10 mil, 21, 21, 79, 6 meses) trazem caminho e linha e conferem. "Sete semanas" confere (25/09 → 13/11) |

## Falhas e correção sugerida

1. **Hora do cabeçalho (1.6).** `ESTADO.md` linha 3 diz "19:55"; o arquivo é de 19:33. Trocar pela hora lida de
   `date` no momento da edição.
2. **Sazonalidade (2.24).** `ESTADO.md` linhas 57–58: acrescentar a linha 25 ao endereço
   ("`research/02_mercado_servicos_precos.md` linhas 25 e 164–176"), ou trocar o texto por "mais demanda na
   primavera e no verão".
3. **Sobreposição entre as seções 2 e 3 (4.8).** Na tabela da seção 3, dizer "exceto as linhas citadas na seção 2",
   ou ajustar os recortes: `R01` seções 3.2, 3.4, 3.6–3.7, 4 (menos a linha 130), 7 (menos a 188) e 8; `R03` modelos
   (d)–(h) e, do (c), só a linha 31; `R04` seções 2–6 e 7.1–7.2.

## Ressalvas (não contadas como falha; melhoram o arquivo)

- `ESTADO.md` linha 32: "linha 50" → "linhas 50–51"; linha 88: "linha 118" → "linhas 118–119". O `RODADA.md` cita só
  a 50, e o conteúdo começa nela.
- Linha 30: recuperar "sem registro" e a proibição de provocar temor (`R01` 44).
- Linha 31: as linhas 91 e 165 de `R03` tratam de consentimento para contato futuro, não do repasse.
- Linha 81: o endereço exato dos modelos (a) e (b) e do caso de Nova York é 41–42; a linha 44 (art. 22 em site de
  leads) caberia melhor na seção 2.2.
- Linha 11: a menção ao ChatGPT vem da linha 61 do `RODADA.md`; "licenciadas" vem do `CLAUDE.md` do projeto.
- Seção 2: uma linha de "divergências e lacunas" apontando os trechos listados em 4.9.

## Observações fora do portão (para o owner decidir)

- O arquivo movido, `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md`, está no git desde o primeiro commit (`2866541`)
  e traz o nome do empregador (linha 12), a formação e a situação do registro profissional do owner (linha 18) e o
  nome de um repositório do trabalho (linha 124). Não traz valor de salário. O item 1 não criou isso e a regra "nada
  apagado" impede removê-lo aqui; fica o registro, diante das regras "nada da empresa" e "dado pessoal fora do git".
- `docs/fds-2026-11-13/PAINEL.md` (mesmo commit) diz "atualizado em 19:40", mas foi gravado às 19:29: o mesmo
  problema de hora estimada do item 1.6.
- O `RODADA.md` (linhas 6 e 31) ainda cita `PROMPT_PLANO.md` na raiz. Não é para reescrever o portão; o
  `ESTADO.md` já dá o caminho novo.

## Limites desta verificação

- Conferi se cada linha citada diz o que o `ESTADO.md` descreve. **Não** conferi se a pesquisa de 25/09 está certa
  na fonte externa: isso é o item 2.
- A sincronia com o remoto foi conferida pela referência local (`@{u}`), sem consultar o servidor.
