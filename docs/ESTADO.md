# Estado do projeto — SEO para leads (ponto de retomada)

Escrito em 13/11/2026 (sexta), 19:55 Brasília, no item 1 da rodada `docs/fds-2026-11-13/RODADA.md`.
Raiz do projeto: `/home/ancastelo/pessoal/SEO_Project`. Os caminhos abaixo são relativos a ela, salvo indicação.

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
como **hipótese com endereço**, nunca como fato: cada ponto abaixo só vira regra depois de reconferido na fonte, no
item indicado.

### 2.1 Quatro afirmações que decidem o modelo (reconferidas no item 2, `docs/estudo/00_restricoes.md`)

| Afirmação antiga | Onde está | Item que reconfere |
|---|---|---|
| Quem só gera leads é inelegível ao perfil de empresa do Google; o perfil exige endereço real e contato presencial | `research/03_modelos_negocio_escala.md` linhas 13 e 102–108 | 2(a) |
| Propaganda de controle de pragas tem de identificar a executora e o número da licença, e não pode usar "atóxico", "seguro", "aprovado pela vigilância" (RDC 622/2022, art. 22) | `research/01_regulacao_licencas.md` linhas 44 e 157–159 (e 188) | 2(b) |
| Repasse do contato exige consentimento ("autorizo repassar meu contato a até N empresas licenciadas") | `research/03_modelos_negocio_escala.md` linha 167 (e linhas 91 e 165) | 2(c) |
| O lead vale R$ 20–60 e a receita realista de quem só gera leads é de R$ 3–10 mil por mês (confiança baixa) | `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` linha 50; conta em `research/03_modelos_negocio_escala.md` linhas 15–16 e 79–83 | 5 |

### 2.2 Regulação que atinge o site e o repasse (base do item 2 e do desenho)

- RDC 622/2022, artigo por artigo (contratação só com empresa especializada, comprovante, nota fiscal, propaganda,
  sanções): `research/01_regulacao_licencas.md` linhas 28–47.
- O que tornaria irregular a atuação de um intermediário e o "formato seguro" proposto (diretório ou comparador; o
  cliente contrata direto a licenciada; receita paga pela licenciada): `research/01_regulacao_licencas.md` linhas 153–160.
- Responsabilidade solidária na cadeia de consumo e a nota técnica do Procon-MG sobre intermediários:
  `research/01_regulacao_licencas.md` linhas 162–165; corrente contrária em
  `research/03_modelos_negocio_escala.md` linha 163.
- Quem licencia a dedetizadora na capital (estado × município), que define qual número de licença o site exibe:
  `research/01_regulacao_licencas.md` linhas 14 e 78–84 (conclusão marcada como interpretação).
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
  linhas 164–176. Volume de busca: **não obtido** (linha 173) — continua sendo lacuna.
- Medo de golpe ("golpe do cupim", cobrança sem orçamento) como ângulo de conteúdo e de confiança:
  `research/02_mercado_servicos_precos.md` linhas 153–160.

### 2.4 Concorrência na busca (hipóteses que o item 4 confere ao vivo)

- A busca por bairro seria dominada por sites da cidade inteira com uma página por bairro, não por empresas do bairro:
  `research/02_mercado_servicos_precos.md` linhas 26–30 e 180–198; lista em `data/concorrentes_sp.csv` (21 linhas).
- Redes de sites-satélite de dedetizadoras e a aposta em cauda longa (bairro × praga):
  `research/03_modelos_negocio_escala.md` linhas 14 e 97–111.
- Plataformas de pedidos de orçamento que já vendem contatos (GetNinjas e outras):
  `research/01_regulacao_licencas.md` linhas 167–171.

### 2.5 Preço do serviço e do lead (base do item 5)

- Preços anunciados do serviço avulso em São Paulo e contratos de empresa: `research/02_mercado_servicos_precos.md`
  linhas 12–24 e 118–150 (são tabelas anunciadas, não preço efetivo: linha 248).
- Preço do lead e do clique, fechamento, quanto uma dedetizadora poderia pagar, e como evitar que o parceiro deixe de
  pagar: `research/03_modelos_negocio_escala.md` linhas 53–91. Atenção: quase todos os números são dos Estados Unidos
  e vêm de agências que vendem leads (aviso na linha 6); não viram número do Brasil.
- Margem por serviço (teto do que a dedetizadora pode pagar por contato):
  `research/04_mao_de_obra_custos_operacao.md` linhas 228–250.
- Modelos (a) pagamento por lead e (b) aluguel de site ranqueado, e o caso único de Nova York (autor vende curso):
  `research/03_modelos_negocio_escala.md` linhas 29–30 e 41–44.
- Riscos do modelo de leads (dependência do Google, qualidade do parceiro, parceiro sem licença, propaganda, LGPD,
  inadimplência): `research/03_modelos_negocio_escala.md` linhas 156–168.

### 2.6 Lembrete que continua valendo

- Conferir a política do empregador sobre atividade paralela (só lembrete; não pesquisar):
  `arquivo/2026-09_foco_anterior/PROMPT_PLANO.md` linha 118. Vira pergunta fixa no item 8.

## 3. O que fica só como histórico

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
| Regras da rodada (cópia do prompt de sistema) | `docs/fds-2026-11-13/SISTEMA.md` |
| Itens e portões | `docs/fds-2026-11-13/RODADA.md` |
| Painel (estado dos itens) | `docs/fds-2026-11-13/PAINEL.md` |
| Leitura do owner | `docs/fds-2026-11-13/LEITURA.md` (a partir do fechamento do item 1) |
| Verificações independentes | `docs/fds-2026-11-13/_runs/verificacao_item<N>.md` |
| Restrições lidas na fonte (item 2) | `docs/estudo/00_restricoes.md` |
| Guias de ranqueamento (item 3) | `docs/estudo/01_…`, `02_…`, `03_…`, `03b_chatgpt.md`, `03b_chatgpt_roteiro_de_teste.md` |
| Mapa do mercado de busca (item 4) | `docs/mercado/serp_sp.md`, `data/serp_sp.csv`, `data/palavras_chave.csv` |
| Modelos de negócio (item 5) | `docs/modelos_de_negocio.md` |
| Desenho do sistema, versão 0 (item 6) | `docs/desenho_v0.md` |
| Protótipo local (item 7) | `prototipo/` |
| Perguntas ao owner (item 8) | `docs/perguntas_owner.md` |

Os arquivos dos itens 2–8 passam a existir conforme cada item avança; o painel diz o estado de cada um.

## 5. Como retomar

1. Ler `docs/fds-2026-11-13/SISTEMA.md`, `docs/fds-2026-11-13/RODADA.md` e `docs/fds-2026-11-13/PAINEL.md`.
2. Continuar do item em curso indicado no topo do painel.
3. Depois da rodada, este arquivo é o ponto de entrada: a seção 4 aponta os entregáveis; a `LEITURA.md` resume o que
   está fechado e as decisões que cabem ao owner.
