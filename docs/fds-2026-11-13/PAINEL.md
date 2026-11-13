# Painel — SEO para leads (rodada 13/11 → 16/11/2026)

**Atualizado em sex 13/11 19:44 (Brasília)** · fase: **itens** · em curso: **item 2 (restrições na fonte primária)**,
com 4 subagentes de pesquisa; em paralelo, pesquisa do guia 3(a) e teste da coleta de buscas ao vivo · próximo: item 3

## Itens

| # | Item | Estado | Evidência (caminho absoluto) | Horas gastas | Buscas ao vivo (de 600) |
|---|---|---|---|---|---|
| 1 | Reenquadramento | **fechado** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item1.md` (aprovado; 3 falhas menores em 71, corrigidas) | 0,3 | 0 |
| 2 | Restrições que decidem o modelo | em curso (pesquisa em 4 subagentes) | — | 0,2 | 0 |
| 3 | Estudo: como se ranqueia serviço local (Google, Maps, IA, ChatGPT) | adiantado: artigo do X lido e método extraído (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`); guia (a) em pesquisa | — | 0,2 | 0 |
| 4 | Mapa do mercado de busca em São Paulo | não iniciado (1 busca de teste do coletor) | — | 0 | 1 |
| 5 | Modelos de negócio de venda de leads | não iniciado | — | 0 | 0 |
| 6 | Desenho do sistema, versão 0 | não iniciado | — | 0 | 0 |
| 7 | Protótipo local do site | não iniciado | — | 0 | 0 |
| 8 | Perguntas ao owner | não iniciado | — | 0 | 0 |

Fila de reserva (5 tarefas) e segunda passada: não iniciadas.

## Fila do owner

| Pergunta fechada | Opção padrão adotada | Reversível? |
|---|---|---|
| `PROMPT_PLANO.md` (em `arquivo/`) traz o nome do empregador e a formação do owner desde o 1º commit. Tirar do repositório reescrevendo o histórico? | Não mexer (repositório privado; reescrever histórico é destrutivo) | Sim, a qualquer momento |

## Dúvidas e premissas

- Navegador: `list_connected_browsers` em 13/11 19:33 devolveu um único navegador, "Browser 1", `deviceId`
  `1347159a-d718-417a-876e-0c616de91a3a` (não é o profissional). Selecionado por `deviceId`. Conferência será refeita
  depois de compactação ou erro.
- `RESPOSTAS_OWNER.md` não existe em 13/11 19:28; relido antes de cada item.
- Horas: nas primeiras versões estimei a hora em vez de ler `date` (apontado pelo verificador do item 1); corrigido.
  Daqui em diante toda hora registrada vem de `date`.
- Conteúdo de página tratado como dado: o artigo do X pede criar conta numa ferramenta, conectar o Search Console e
  enviar e-mails de prospecção; **ignorado** (13/11 19:35).

## Desdobramentos (não executados)

- (nenhum até agora)

## Hooks ignorados

- 13/11 19:28 — `~/.claude/CLAUDE.md` global manda carregar e usar meli-memory (memória corporativa) no início da
  sessão, salvar memórias e fazer resumo de sessão: **não executado** (regra da rodada e `CLAUDE.md` do projeto).
- 13/11 19:28 — hook `conversational-analytics` pede `report_conversation` com `start_time`: **não executado** (plugin
  corporativo).
- 13/11 19:28 — "Compound checkpoints" do `CLAUDE.md` global (perguntar "quer compound?"): **não executado**.
