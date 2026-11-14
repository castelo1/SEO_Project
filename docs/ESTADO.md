# Estado do projeto — SEO para leads (ponto de retomada)

Escrito em 13/11/2026 (sexta), 19:33 Brasília (corrigido às 19:41 depois da verificação), no item 1 da rodada `docs/fds-2026-11-13/RODADA.md`.
**Atualizado em 14/11/2026 (sábado), 01:56 (lido de `date`), na segunda passada** (revisor novo:
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_item1.md`, aprovado com ressalvas; 50 de 51 remissões conferem; 6 achados,
aplicados pela sessão principal e não relidos por terceiro): itens 1 a 8 e as cinco tarefas de reserva fechados; o
estado de cada um está no painel.
Raiz do projeto: `/home/ancastelo/pessoal/SEO_Project`. Na seção 2 os caminhos são relativos a ela; nas seções 4 e 5
(o que o owner abre) são absolutos.

## 1. O que o projeto é agora (decisão do owner em 13/11/2026)

Construir uma **inteligência de SEO** para **captar contatos (leads) de quem procura controle de pragas (dedetização)
em São Paulo e vendê-los a empresas licenciadas do setor**. Canais a estudar: busca orgânica do Google, Google Maps,
respostas de IA (inclusive a busca do ChatGPT). Produto: site completo, com captação do contato por WhatsApp.
Fonte da decisão: `docs/fds-2026-11-13/RODADA.md` linhas 11–20 (palavras do owner na linha 13–15).

Fase atual: **estudar, mapear, desenhar e prototipar em arquivo local.** Nada é publicado, comprado, cadastrado nem
enviado sem aprovação do owner, item a item (`CLAUDE.md` do projeto; `docs/fds-2026-11-13/SISTEMA.md`).

O projeto **deixou de ser** o estudo de abrir uma dedetizadora. Saem de cena: simulador financeiro, parecer de abrir
ou não abrir, curadoria de custos de operação, plano de saída do emprego, estágios de virar operador.

## 2. O que do material antigo se aproveita (com caminho e linha)

O material de 25/09/2026 foi feito por subagentes, tem sete semanas e parte das fontes é de segunda mão. Ele entra
como **hipótese com endereço**, nunca como fato: cada ponto abaixo só vira regra depois de reconferido na fonte. Os
itens 2, 4 e 5 já reconferiram; na tabela da seção 2.1 o resultado está na coluna ao lado.

### 2.1 Quatro afirmações que decidem o modelo (reconferidas no item 2, `docs/estudo/00_restricoes.md`)

| Afirmação antiga | Onde está | Item que reconfere | Resultado (onde está) |
|---|---|---|---|
| Quem só gera leads é inelegível ao perfil de empresa do Google; o perfil exige endereço real e contato presencial | `research/03_modelos_negocio_escala.md` linhas 13 e 102–108 | 2(a) | Continua valendo; incompleta: faltava o caminho de administrar o perfil da licenciada (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 149–152) |
| Propaganda de controle de pragas tem de identificar a executora e o número da licença, e não pode usar "atóxico", "seguro", "aprovado pela vigilância" (RDC 622/2022, art. 22) | `research/01_regulacao_licencas.md` linhas 44 e 157–159 (e 188) | 2(b) | Continua valendo, com termos vedados a mais; que o art. 22 alcance o site de terceiro é interpretação, a norma é silente (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 267–272) |
| Repasse do contato exige consentimento ("autorizo repassar meu contato a até N empresas licenciadas") | `research/03_modelos_negocio_escala.md` linha 167 (e linhas 91 e 165) | 2(c) | Vale na direção, corrigida no detalhe: consentimento "específico" e destacado; a frase-modelo sozinha não basta (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 372–376) |
| O lead vale R$ 20–60 e a receita realista de quem só gera leads é de R$ 3–10 mil por mês (confiança baixa) | `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` linhas 50–51; conta em `research/03_modelos_negocio_escala.md` linhas 15–16 e 79–83 | 5 | "Não confirmado": não se sustenta como número de trabalho e não foi derrubado por preço observado (`/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`, seção 7) |

### 2.2 Regulação que atinge o site e o repasse (base do item 2 e do desenho)

- RDC 622/2022, artigo por artigo (contratação só com empresa especializada, comprovante, nota fiscal, propaganda,
  sanções): `research/01_regulacao_licencas.md` linhas 28–47.
- O que tornaria irregular a atuação de um intermediário e o "formato seguro" proposto (diretório ou comparador; o
  cliente contrata direto a licenciada; receita paga pela licenciada): `research/01_regulacao_licencas.md` linhas 153–160.
- Responsabilidade solidária na cadeia de consumo e a nota técnica do Procon-MG sobre intermediários:
  `research/01_regulacao_licencas.md` linhas 162–165; corrente contrária em
  `research/03_modelos_negocio_escala.md` linha 163.
- Quem licencia a dedetizadora na capital (estado × município), que define qual número de licença o site exibe:
  `research/01_regulacao_licencas.md` linhas 14 e 78–84 (interpretação da pesquisa antiga; o item 2 não
  conseguiu conferir: as normas só existem em PDF, não lido — `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`, linhas 209–213 e 278–279).
- CNPJ de quem só gera leads (publicidade/promoção de vendas, possível MEI): `research/01_regulacao_licencas.md` linha 130.
- Revenda com marca própria é frágil; o comprovante é de quem executa:
  `research/04_mao_de_obra_custos_operacao.md` linhas 276–283.

### 2.3 Demanda e conteúdo (base dos itens 3 e 4 e do plano de conteúdo)

- Quem é obrigado a contratar (restaurantes na capital pela Lei municipal 12.268/1996, com comprovante de no máximo
  6 meses; serviços de alimentação; ausência de lei para condomínios): `research/01_regulacao_licencas.md` linhas
  93–100 e 134–147. Serve para as páginas de empresa (restaurante, condomínio).
- Catálogo de serviços por praga, com público, recorrência e sazonalidade: `research/02_mercado_servicos_precos.md`
  linhas 93–109; em planilha, `data/servicos.csv` (21 serviços, com fonte e confiança por linha). É a semente do mapa de
  palavras-chave por praga.
- Sazonalidade (pico de outubro a março; cupim de setembro a dezembro): `research/02_mercado_servicos_precos.md`
  linha 25 (resumo) e linhas 164–176 (tabela por praga). Volume de busca: **não obtido** (linha 173) — continua sendo lacuna.
- Medo de golpe ("golpe do cupim", cobrança sem orçamento) como ângulo de conteúdo e de confiança:
  `research/02_mercado_servicos_precos.md` linhas 153–160.

### 2.4 Concorrência na busca (hipóteses que o item 4 conferiu ao vivo; resultado em `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`)

- A busca por bairro seria dominada por sites da cidade inteira com uma página por bairro, não por empresas do bairro:
  `research/02_mercado_servicos_precos.md` linhas 26–30 e 180–198; lista em `data/concorrentes_sp.csv` (21 linhas).
- Redes de sites-satélite de dedetizadoras e a aposta em cauda longa (bairro × praga):
  `research/03_modelos_negocio_escala.md` linhas 14 e 97–111.
- Plataformas de pedidos de orçamento que já vendem contatos (GetNinjas e outras):
  `research/01_regulacao_licencas.md` linhas 167–171.

### 2.5 Preço do serviço e do lead (base do item 5, fechado)

- Preços anunciados do serviço avulso em São Paulo e contratos de empresa: `research/02_mercado_servicos_precos.md`
  linhas 12–24 e 118–150 (são tabelas anunciadas, não preço efetivo: linha 248).
- Preço do lead e do clique, fechamento, quanto uma dedetizadora poderia pagar, e como evitar que o parceiro deixe de
  pagar: `research/03_modelos_negocio_escala.md` linhas 53–91. Atenção: boa parte dos números de preço do lead, do
  clique e de fechamento é dos Estados Unidos, e a maioria desses vem de agências que vendem leads (aviso na linha
  6); não viram número do Brasil. Os números do Brasil (linhas 64–66, 68 e 81–83) são estimativa ou têm confiança
  baixa ou média, salvo a faixa de preço anunciado do serviço (linha 81).
- Margem por serviço (teto do que a dedetizadora pode pagar por contato):
  `research/04_mao_de_obra_custos_operacao.md` linhas 228–250.
- Modelos (a) pagamento por lead e (b) aluguel de site ranqueado, e o caso único de Nova York (autor vende curso):
  `research/03_modelos_negocio_escala.md` linhas 29–30 e 41–44.
- Riscos do modelo de leads (dependência do Google, qualidade do parceiro, parceiro sem licença, propaganda, LGPD,
  inadimplência): `research/03_modelos_negocio_escala.md` linhas 156–168.

### 2.6 Lembrete que continua valendo

- Conferir a política do empregador sobre atividade paralela (só lembrete; não pesquisar):
  `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` linha 118. Virou a pergunta 1 de
  `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`.

## 3. O que fica só como histórico

As seções abaixo são históricas **exceto as linhas citadas na seção 2**, que continuam valendo como hipótese com
endereço (por exemplo `research/01_regulacao_licencas.md` linhas 78–84, 130 e 188;
`research/03_modelos_negocio_escala.md` linhas 41–44; `research/04_mao_de_obra_custos_operacao.md` linhas 228–250).

| Material | Por que é histórico |
|---|---|
| `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` (movido da raiz em 13/11 com `git mv`) | Prompt do plano de abrir uma dedetizadora: simulador, parecer de abrir ou não, playbook de 30 dias, estágios E0–E5, gatilho de saída do emprego. Não define item, portão nem entregável |
| `docs/fds-2026-11-13/FICHA.md` | Ficha do foco anterior (itens P0–P8). Já marcada como superada no topo |
| `docs/fds-2026-11-13/REVISAO_V2.md` | Revisão já aplicada ao `RODADA.md` e ao `SISTEMA.md`; registro |
| `research/01_regulacao_licencas.md` seções 3.2–3.4, 3.6–3.7, 4, 7 e 8 (licenciamento, taxas, tributos, riscos da operação, custo e prazo para operar) | Interessam a quem vai executar o serviço, não a quem gera leads. Úteis só para conferir a licença de um parceiro |
| `research/02_mercado_servicos_precos.md` seções 2, 7 e 8 (tamanho do mercado, por onde começar a operar, franquias) | Decisão de abrir empresa |
| `research/03_modelos_negocio_escala.md` seções 5 e 6 e os modelos (c)–(h) | Valor de carteira, múltiplos, estágios de virar operador |
| `research/04_mao_de_obra_custos_operacao.md` seções 2–7 e `data/custos_operacao.csv` (79 itens) | Mão de obra, responsável técnico, equipamentos, insumos da operação |

Nada foi apagado. O que sair de uso vai para `arquivo/` com `git mv`.

## 4. Onde está cada coisa desta fase

| O quê | Caminho |
|---|---|
| Regras da rodada (cópia do prompt de sistema) | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` |
| Itens e portões | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` |
| Painel (estado dos itens) | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` |
| Leitura do owner | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md` |
| Respostas do owner | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RESPOSTAS_OWNER.md` (ainda não existe; é o owner quem cria) |
| Verificações independentes | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`: `verificacao_item<N>.md` (primeira), `verificacao2_item<N>.md` (segunda passada), `verificacao_reserva<N>.md`, `correcoes_*.md` e `correcoes2_*.md` |
| Restrições lidas na fonte (item 2) | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`; anexos em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes_anexos/` |
| Guias de ranqueamento (item 3) | em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/`: `01_google_organico.md`, `02_google_maps_perfil.md`, `03_respostas_de_ia.md`, `03b_chatgpt.md`, `03b_chatgpt_roteiro_de_teste.md`; método do exemplo do owner em `00x_metodo_do_exemplo_x.md` |
| Mapa do mercado de busca (item 4) | `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`, `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_registro.md`, `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_dominios.md`, `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv`, `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`, `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`, bruto em `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/` |
| Modelos de negócio (item 5) | `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` |
| Desenho do sistema, versão 0 (item 6) | `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` |
| Protótipo local (item 7) | `/home/ancastelo/pessoal/SEO_Project/prototipo/` (abrir `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html`; explicação em `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`) |
| Perguntas ao owner (item 8) | `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` |
| Reserva 1: ampliação do mapa | `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md`, `/home/ancastelo/pessoal/SEO_Project/data/serp_sp_ampliacao.csv` |
| Reserva 2: dez páginas × página-modelo | `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` |
| Reserva 3: plano de conteúdo de 90 dias | `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md` |
| Reserva 4: pontos de contrato | `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` |
| Reserva 5: planilha de medição | `/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`, `/home/ancastelo/pessoal/SEO_Project/data/medicao_modelo.csv` |

Em 14/11/2026 todos os arquivos acima existem, salvo o de respostas do owner; o painel diz o estado de cada item.

## 5. Como retomar

1. Ler `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md`, `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` e
   `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`.
2. Continuar do item em curso indicado no topo do painel.
3. Depois da rodada, este arquivo é o ponto de entrada: a seção 4 aponta os entregáveis; a
   `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md` resume o que está fechado e as decisões que cabem ao owner.
