# Painel — SEO para leads (rodada 13/11 → 16/11/2026)

**Atualizado em sex 13/11 21:21 (Brasília, lido de `date`)** · fase: **itens** · em curso: **item 3 (estudo de
ranqueamento)** — os dois verificadores aprovaram com correções pendentes; dois corretores aplicam as correções; depois
conferência minha e fechamento · em paralelo: item 4 — **buscas ao vivo em pausa até 23:17** (verificação de robô do Google às 21:16, 1ª ocorrência, não resolvida); 79 de 89 consultas gravadas; análise e classificação dos domínios em curso · próximo:
fechar o item 3, terminar a coleta e escrever o item 4

## Itens

| # | Item | Estado | Evidência (caminho absoluto) | Horas gastas | Buscas ao vivo (de 600) |
|---|---|---|---|---|---|
| 1 | Reenquadramento | **fechado** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item1.md` (aprovado; 3 falhas menores em 71, corrigidas) | 0,3 | 0 |
| 2 | Restrições que decidem o modelo | **fechado** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item2.md` (aprovado; 12 de 12 citações sorteadas conferem; 8 defeitos fora do sorteio, corrigidos) | 0,9 | 0 |
| 3 | Estudo: como se ranqueia serviço local (Google, Maps, IA, ChatGPT) | em curso: cinco arquivos entregues; verificação aprovou as duas metades (12 de 12 e 11 de 12 no sorteio) e listou 26 falhas fora do sorteio, **em correção** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_a_b.md` e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_ia_chatgpt.md` | 1,3 | 0 |
| 4 | Mapa do mercado de busca em São Paulo | em curso: 79 de 89 consultas gravadas (`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/`, lotes 1 a 7); `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` montado (1.060 resultados, 157 domínios); faltam as 10 consultas do grupo H, a classificação dos domínios e o texto | — | 1,2 | ≈ 95 (79 válidas, 1 barrada, ≈ 15 perdidas em testes e lotes descartados) |
| 5 | Modelos de negócio de venda de leads | não iniciado | — | 0 | 0 |
| 6 | Desenho do sistema, versão 0 | não iniciado | — | 0 | 0 |
| 7 | Protótipo local do site | não iniciado | — | 0 | 0 |
| 8 | Perguntas ao owner | não iniciado | — | 0 | 0 |

Fila de reserva (5 tarefas) e segunda passada: não iniciadas.

## Fila do owner

| Pergunta fechada | Opção padrão adotada | Reversível? |
|---|---|---|
| `PROMPT_PLANO.md` (em `arquivo/`) traz o nome do empregador e a formação do owner desde o 1º commit. Tirar do repositório reescrevendo o histórico? | Não mexer (repositório privado; reescrever histórico é destrutivo) | Sim, a qualquer momento |
| Normas que só existem em PDF (Portaria CVS 1/2024, anexo municipal, guias da ANPD, diretrizes dos avaliadores do Google) não foram lidas: a ferramenta não extrai texto de PDF e baixar arquivo para o projeto não foi autorizado. Autoriza baixar esses PDFs oficiais para `docs/fontes/`? | Não baixar; o que depende deles fica "não conclusivo" | Sim |
| O Google lista "consultas automáticas" entre as práticas vedadas (guia 3a, seção 8). A rodada autoriza até 600 buscas ao vivo com 20 s de intervalo. Mantém? | Manter o limite da rodada; parar no primeiro sinal de verificação de robô | Sim |
| O roteiro de teste do ChatGPT tinha 5 perguntas de dono de bar ou restaurante; o portão pede "morador ou síndico". Manter as 5 dentro das 30? | Não: as 30 ficam só de morador e síndico; as 5 de comerciante vão para um apêndice opcional | Sim |

## Dúvidas e premissas

- Navegador: `list_connected_browsers` (13/11 19:33, 20:04, 20:52 e 20:56) devolveu um único navegador, "Browser 1",
  `deviceId` `1347159a-d718-417a-876e-0c616de91a3a` (não é o profissional). Selecionado por `deviceId`.
- Coleta ao vivo: Google **logado** na conta do owner (só leitura), `hl=pt-BR&gl=br&pws=0`; local exibido pelo Google
  quando aparece: "São Paulo, SP" ou "Osasco, SP".
- **Verificação de robô ("tráfego incomum") às 21:16**, na 80ª consulta válida (H01), depois de ~28 minutos de coleta
  contínua a ~27 s por busca. **Não resolvida.** Buscas ao vivo paradas até 23:17; aba fechada. Na retomada: só as 10
  consultas do grupo H e as 5 repetições do verificador, a 60 s ou mais; na segunda ocorrência, paro de vez.
- DÚVIDA: três intervalos ficaram abaixo de 20 s por erro meu na montagem do lote (18 s, 19 s e 17 s) · premissa
  adotada: registros mantidos e os três casos declarados no documento do item 4; espera inicial reposta em todo lote.
- DÚVIDA: às 20:55 a conexão com o navegador caiu no meio de um lote, que seguiu rodando; um registro saiu duplicado
  (removido ao gravar) e uma busca pode ter sido enviada duas vezes · premissa adotada: conto 1 busca a mais no total.
- DÚVIDA: o Chrome descarta a aba da sessão quando ela fica ociosa mais de ~1 minuto · premissa adotada: coleta em
  ciclo contínuo; correções do item 3 delegadas a dois subagentes para não parar a coleta.
- DÚVIDA: os lotes de teste das 20:10–20:22 sobrepuseram buscas · premissa adotada: descartados (≈ 14 buscas perdidas).
- Roteiro do ChatGPT, medição: regra única adotada nos três arquivos — rodada mensal das 30 perguntas como amostra
  agregada, mais 6 perguntas repetidas 5 vezes em dias diferentes e uma subamostra deslogada; fica dito que isso não
  atinge as 60 a 100 repetições por pergunta que os autores do estudo citado sugerem.
- Medir posição no mapa com "grade de posição": o guia (b) passa a dizer que contraria a política do Google (consulta
  automática); alternativa: dados do próprio perfil (da licenciada) e conferência manual por amostra.
- `RESPOSTAS_OWNER.md` não existe (conferido às 19:28, 20:24 e 20:52); relido antes de cada item.
- Horas: toda hora registrada vem de `date`.
- Conteúdo de página tratado como dado: o artigo do X pede criar conta numa ferramenta, conectar o Search Console e
  enviar e-mails de prospecção; **ignorado** (13/11 19:35).
- A ferramenta de leitura de página guardou cópias de PDFs fora do projeto; **não foram abertas** (fronteira).

## Desdobramentos (não executados)

- Ler os PDFs oficiais (ver fila do owner) para fechar os pontos "não conclusivo" do item 2.
- Conferir no Diário Oficial (`in.gov.br`, que não abriu) o texto da RDC 622 e das resoluções da ANPD.
- Levantar jurisprudência sobre responsabilidade de site de indicação (fora do escopo do item 2).
- Coleta no Google Maps (lista completa, além do bloco de 3 empresas da busca): entra na fila de reserva 1.
- Reconferir a ajuda da OpenAI sobre a busca do ChatGPT por um segundo leitor (o verificador recebeu erro 403).

## Hooks ignorados

- 13/11 19:28 — `~/.claude/CLAUDE.md` global manda carregar e usar meli-memory (memória corporativa), salvar memórias e
  fazer resumo de sessão, inclusive depois de compactação: **não executado** (regra da rodada e `CLAUDE.md` do
  projeto). Os subagentes receberam a mesma instrução e também não executaram.
- 13/11 19:28, 19:39, 19:45, 19:47, 19:51, 20:07, 20:16, 20:20, 20:36, 20:59, 21:02 — hook `conversational-analytics`
  pede `report_conversation` com `start_time`: **não executado** (plugin corporativo).
- 13/11 19:28 — "Compound checkpoints" do `CLAUDE.md` global (perguntar "quer compound?"): **não executado**.
- 13/11 20:51 — hook de início de sessão (após compactação) pede usar a skill `gestao` e rodar `gestao propor` em
  `/home/ancastelo/work/gestao`: **não executado** (ferramenta da empresa e pasta fora da fronteira).
