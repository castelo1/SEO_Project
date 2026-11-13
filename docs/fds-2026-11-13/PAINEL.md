# Painel — SEO para leads (rodada 13/11 → 16/11/2026)

**Atualizado em sex 13/11 20:24 (Brasília, lido de `date`)** · fase: **itens** · em curso: **item 3 (estudo de
ranqueamento)** — quatro guias entregues por subagentes, em revisão; guia do Maps em pesquisa · em paralelo: coleta de
buscas ao vivo do item 4 (em pausa: navegador sem resposta) · próximo: verificação do item 3, depois item 4

## Itens

| # | Item | Estado | Evidência (caminho absoluto) | Horas gastas | Buscas ao vivo (de 600) |
|---|---|---|---|---|---|
| 1 | Reenquadramento | **fechado** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item1.md` (aprovado; 3 falhas menores em 71, corrigidas) | 0,3 | 0 |
| 2 | Restrições que decidem o modelo | **fechado** | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item2.md` (aprovado; 12 de 12 citações sorteadas conferem; 8 defeitos fora do sorteio, corrigidos, entre eles a Portaria CVS 9/2000 rebaixada a "não conclusivo") | 0,9 | 0 |
| 3 | Estudo: como se ranqueia serviço local (Google, Maps, IA, ChatGPT) | em curso: guias (a), (c), ChatGPT e roteiro de teste entregues, em revisão; guia (b) Maps em pesquisa | — | 0,6 | 0 |
| 4 | Mapa do mercado de busca em São Paulo | adiantado: lista de 89 consultas gravada (`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas.csv`); coletor testado; coleta em pausa | — | 0,3 | 13 |
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

## Dúvidas e premissas

- Navegador: `list_connected_browsers` (13/11 19:33 e 20:04) devolveu um único navegador, "Browser 1", `deviceId`
  `1347159a-d718-417a-876e-0c616de91a3a` (não é o profissional). Selecionado por `deviceId`.
- DÚVIDA: o Chrome descarta a aba da sessão quando ela fica ociosa mais de ~1 minuto (o identificador da aba muda e o
  script deixa de responder); às 20:22 nem a navegação respondeu · premissa adotada: coleta em ciclo contínuo, sem
  pausa longa; se o navegador não voltar, o item 4 fecha com a amostra que houver.
- DÚVIDA: um lote de 5 buscas estourou o tempo da ferramenta e continuou rodando em segundo plano, sobrepondo-se ao
  lote seguinte (buscas com menos de 20 s entre si, por erro meu) · premissa adotada: descartei o que foi coletado
  nesses lotes; a coleta recomeça do zero, uma busca por chamada, e cada registro guarda o termo lido da própria
  página e a hora da navegação.
- `RESPOSTAS_OWNER.md` não existe (conferido às 19:28 e 20:24); relido antes de cada item.
- Horas: toda hora registrada vem de `date` (correção do verificador do item 1).
- Conteúdo de página tratado como dado: o artigo do X pede criar conta numa ferramenta, conectar o Search Console e
  enviar e-mails de prospecção; **ignorado** (13/11 19:35).
- A ferramenta de leitura de página guardou cópias de PDFs fora do projeto (área de resultados da sessão); **não
  foram abertas** (fronteira).

## Desdobramentos (não executados)

- Ler os PDFs oficiais (ver fila do owner) para fechar os pontos "não conclusivo" do item 2: qual número de licença
  vale na capital (estadual ou municipal); vigência e texto da Portaria CVS 9/2000; guia de legítimo interesse.
- Conferir no Diário Oficial (`in.gov.br`, que não abriu) o texto da RDC 622 e das resoluções da ANPD.
- Levantar jurisprudência sobre responsabilidade de site de indicação (fora do escopo do item 2).

## Hooks ignorados

- 13/11 19:28 — `~/.claude/CLAUDE.md` global manda carregar e usar meli-memory (memória corporativa) no início da
  sessão, salvar memórias e fazer resumo de sessão: **não executado** (regra da rodada e `CLAUDE.md` do projeto). Os
  subagentes receberam a mesma instrução e também não executaram.
- 13/11 19:28, 19:39, 19:45, 19:47, 19:51, 20:07, 20:16, 20:20 — hook `conversational-analytics` pede
  `report_conversation` com `start_time`: **não executado** (plugin corporativo).
- 13/11 19:28 — "Compound checkpoints" do `CLAUDE.md` global (perguntar "quer compound?"): **não executado**.
