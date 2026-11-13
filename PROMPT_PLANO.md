# Prompt — Modo Plano: Validação e modelagem de negócio de controle de pragas urbanas (São Paulo)

## Papel
Atue simultaneamente como quatro especialistas, e deixe explícito quando cada um fala:
1. **Empreendedor experiente** (validação de demanda, go-to-market, operação enxuta, escala por estágios)
2. **Operador/RT de dedetizadora** (serviços, técnica, produtos, rotas, licenciamento RDC 622 / CVS SP)
3. **Especialista em SEO local e lead-gen** (cauda longa bairro × praga, Ads, call tracking, rank-and-rent)
4. **Analista de investimentos** (unit economics, cenários, sensibilidade, VPL/TIR/payback vs CDI,
   valuation por receita recorrente, compra de carteira, critérios go/no-go)

## Contexto e decisões do fundador (entrevista de 25/09/2026)
- **Objetivo:** construir uma **empresa para sair do CLT** (Mercado Pago), de forma **faseada**, continuando
  empregado até o risco sair. **Gatilho de saída do CLT: pró-labore sustentável ≥ salário líquido atual**
  (input do simulador, com N meses seguidos a definir).
- **Recursos por gatilho:** os mesmos do microverdes (≈ R$ 0 e poucas h/sem → se gerar dinheiro, até
  **10 h/sem e R$ 10k** → além disso só com cenário que justifique). Pode haver flexibilidade conforme o
  modelo de escala. **Sem sócio.**
- **Formação:** engenheiro civil, **CREA inativo**. Provavelmente não habilita como RT, mas é preciso confirmar.
  Modelar os dois cenários: **RT próprio** (se a atribuição existir e valer reativar o CREA) vs **RT contratado**.
- **SEO:** experiência **nenhuma** → o plano inclui a curva de aprendizado ou a terceirização, e o prazo realista do orgânico.
- **Geografia inicial:** centro expandido de SP (Santa Cecília, Higienópolis, Perdizes, Consolação, Bom
  Retiro, Barra Funda…).
- **Público: híbrido.** O B2C avulso gera caixa e leads. O B2B recorrente (restaurantes, pela Lei 12.268/96;
  condomínios, pela caixa d'água) é o ativo que dá valor à empresa. O SEO nasce com páginas B2B desde o início.
- **Validação (E0): três caminhos em paralelo**, medidos separadamente: (a) Google Ads pago, (b) SEO
  orgânico, (c) prospecção direta B2B (visitas/ligações a restaurantes e síndicos).
- **Rota do E3 (virar operador): decidir pelo simulador.** Comparar lado a lado (i) abrir do zero,
  (ii) comprar uma dedetizadora pequena (licença + RT + carteira), (iii) sociedade com licenciada
  (demanda em troca de participação).
- **Lead-gen vs intermediação:** decidido pela pesquisa. **Só lead-gen/diretório** (cobrança por lead,
  mensalidade ou comissão, com a **licenciada emitindo a NF**). Revender com marca própria e subcontratar está
  fora (RDC 622, arts. 5 e 21, e responsabilidade solidária pelo CDC).

## Material de partida (já pesquisado — ler antes de tudo)
- `research/01_regulacao_licencas.md` — RDC 622/2022, CVS 9/2000, licença Risco III/LTA, RT, MEI vs ME,
  Lei 12.268/96, caixa d'água sem licença VISA (CVS 9/2000 4.2), legalidade do lead-gen.
- `research/02_mercado_servicos_precos.md` + `data/servicos.csv` (21 serviços) + `data/concorrentes_sp.csv`.
- `research/03_modelos_negocio_escala.md` — modelos (a)–(h), preço de lead, SEO local, múltiplos, estágios.
- `research/04_mao_de_obra_custos_operacao.md` + `data/custos_operacao.csv` (79 itens) — CCT SINDPRAG,
  custo do técnico, RT, CAPEX de equipe, margem por serviço, equilíbrio.
- **Método de referência:** `~/Pessoal/microverdes/` — reaproveitar `gsheets.py` (cliente Sheets API),
  o padrão de `build_simulator.py` (abas geradas a partir de CSV curado, fórmulas vivas, named ranges),
  `curate.py` (research → `data/final/`), `check_model.py`/`stress_test.py` (checagem do modelo) e a
  estrutura dos docs (`dossie_pesquisa`, `parecer_go_no_go`, `playbook_30_dias`).

## Achados que o modelo tem de respeitar
1. **Não existe estágio "em casa".** A base operacional não pode ficar em prédio coletivo (RDC 622, art. 8). Operar exige
   imóvel exclusivo, depósito, área de diluição, vestiário, veículo com compartimento isolado, LTA e inspeção.
   Estimativa de R$ 25k / 69k / 137k e 3–6 (até 12) meses. **É o ponto de não-retorno.**
2. **O lead vale pouco** (R$ 20–60, Baixa). O Google Business Profile proíbe lead-gen e o LSA não existe no BR. Receita
   realista de lead-gen: R$ 3–10k/mês. O lead-gen é **ponte de validação e caixa, não o ativo final**.
3. **O ativo é a carteira recorrente:** 3,5–5x EBITDA para avulso contra 7–10x com mais de 80% recorrente (EUA). O conflito de
   canal tem de estar previsto nos contratos de lead desde o E1 (região, prazo, opção de compra da carteira).
4. **Margem fina com 1 técnico:** empate em ~42 serviços/mês (~80% da capacidade). A escala vem de densidade
   de rota, de contratos recorrentes e da diluição do RT e da base entre várias equipes.
5. **Regime:** o CNAE 8122-2/00 não é MEI → ME Simples **Anexo IV** (4,5% inicial + INSS patronal de 20% por fora),
   ISS 5%. O lead-gen usa outro CNPJ ou atividade (7319, MEI possível).

## Regras de pesquisa (inegociáveis — iguais ao microverdes)
- Nada entra sem confirmação: valor, unidade, fonte (URL), data, **confiança** (Alta ≥2 fontes
  independentes ou texto oficial / Média 1 fonte boa / Baixa estimativa). Divergência vira **faixa** mín/base/máx.
- **Relatório de subagente é hipótese, não fato:** fazer verificação cruzada nas fontes primárias antes de
  qualquer número entrar na planilha. Em especial:
  - o conflito entre research/04 ("intermediação declarada com repasse de 60–75%") e research/01 (a NF tem de ser da
    licenciada). Resolver como **comissão com a NF da licenciada**;
  - a faixa de 3x no contrato mensal de restaurante e condomínio;
  - quem licencia na capital: GVS estadual ou COVISA.
- **Lacunas a pesquisar nesta fase:**
  - **Volume de busca e CPC** de ~20 termos bairro × praga e B2B (Keyword Planner via conta Ads, Google
    Trends, ferramentas gratuitas);
  - **custo real do lead no GetNinjas** (moedas por pedido de "Dedetizador" em SP);
  - **notas e volume de avaliações no Google Maps** dos concorrentes do centro;
  - **engenharia civil como RT** (CREA-SP / Resolução CONFEA / CVS 9/2000) e custo de reativar o CREA;
  - **dedetizadoras pequenas à venda** em SP (preço pedido, faturamento, múltiplo) para a rota (ii);
  - termos típicos de **sociedade/parceria** com licenciada para a rota (iii);
  - texto da CVS 33/2008 e do anexo de 2026 da CVS 1; dispensa da CETESB; TFE municipal; prêmio do seguro de RC;
  - **preço de sala/galpão de uso exclusivo** (térreo/casa comercial) no centro expandido e na zona oeste, para a base do E3;
  - modelo de contrato de lead com cláusula anti-conflito de canal.

## Estágios (hipótese — o simulador pode refinar)
| Estágio | O que é | Capital / horas | Gatilho para avançar |
|---|---|---|---|
| **E0 Teste de demanda** | Site cauda longa + Ads pequeno + prospecção B2B; leads grátis para 2–3 licenciadas; cliente oculto de preços | R$ 1–3k · 3–5 h/sem | a definir: ex. custo por lead ≤ X, fechamento ≥ Y%, ≥ N parceiros dispostos a pagar, ≥ M contratos B2B interessados |
| **E1 Lead-gen pago** | MEI de publicidade; cobrança por lead ou comissão; contratos com cláusula de canal | ≤ R$ 10k · ≤ 10 h/sem | receita ≥ R$ Z/mês por K meses; volume B2B mensurável |
| **E2 Ativo de demanda** | Mensalidade por região (rank-and-rent) + caixa d'água como 1º serviço próprio (sem licença VISA) | idem | demanda B2B confirmada que justifique o E3 |
| **E3 Virar operador** | Rota (i) zero / (ii) compra / (iii) sociedade — escolhida no simulador | R$ 25–137k+ · RT · base | EBITDA > 0 por N meses; carteira recorrente ≥ X% |
| **E4 Equipes e rotas** | 2+ equipes, densidade por região, portfólio ampliado | — | pró-labore ≥ salário por N meses → **sai do CLT** |
| **E5 Escala / venda** | Mais regiões ou roll-up; valuation por recorrência | — | — |

**Sequência de portfólio (pesquisa):** baratas e ratos (B2B mensal) → caixa d'água de condomínio → escorpião,
mosquito e pulgas → cupim de madeira seca → cupim subterrâneo, pombos e percevejo → (morcegos só exclusão; fumigação, evitar).

## Entregáveis
1. **Simulador no Google Sheets** (reusar `gsheets.py`, fórmulas vivas):
   - `Leia-me`, `Premissas` (dropdowns: estágio, rota E3, cenário pessimista/base/otimista, RT próprio vs
     contratado, mix B2C/B2B), cada input com fonte e confiança;
   - `Catálogo_Serviços` (de `servicos.csv`) e `Catálogo_Custos` (de `custos_operacao.csv`);
   - **Duas unidades econômicas:** o **lead** (custo por lead por canal: Ads/SEO/prospecção → fechamento → receita
     por lead) no E0–E2 e o **serviço/contrato** (receita, insumo, hora técnica, deslocamento, imposto → margem) no
     E3+;
   - **demanda separada da capacidade** (vendido ≤ min(capacidade das equipes, demanda confirmada));
   - carteira recorrente: aquisição de contratos, churn, reajuste, retorno em garantia, sazonalidade (pico out–mar);
   - **tempo do dono calculado por atividade** e custo de oportunidade R$/h → lucro contábil vs econômico;
   - **comparador das 3 rotas do E3** (capital, prazo até receita, risco, VPL/TIR, valuation em 3 anos);
   - P&L e fluxo de caixa mensal de 36 meses, capital de giro correto, depreciação, impostos por regime (MEI para
     o lead-gen; Simples Anexo IV + INSS para a operação);
   - **linha "saída do CLT"**: mês em que o pró-labore sustentável ≥ salário (input) por N meses;
   - break-even (leads/mês, serviços/mês, contratos), payback, VPL/TIR vs CDI, **tornado de sensibilidade**.
2. **Dossiê de pesquisa** (`docs/dossie_pesquisa.md`): fontes, faixas, confiança, mapa de concorrentes, verificação cruzada.
3. **Mapa comparativo de modelos de negócio** (`docs/mapa_modelos_negocio.md`): lead-gen, rank-and-rent,
   empresa própria, franquia (Unicontrol etc.), compra de carteira, sociedade — capital, horas, risco regulatório,
   valor do ativo, e onde cada um entra na jornada.
4. **Parecer go/no-go** (`docs/parecer_go_no_go.md`): tese, unit economics por estágio, riscos (regulatório,
   dependência do Google, conflito de canal, margem fina, reputação do setor), critérios de kill e de escala.
5. **Playbook de validação + plano de 30 dias** (`docs/playbook_30_dias.md`): os **3 canais em paralelo** com
   métricas próprias; lista de restaurantes e condomínios-alvo no centro; roteiro de prospecção; roteiro de cliente
   oculto; como recrutar 2–3 licenciadas parceiras e a proposta a elas; setup mínimo de site e Ads para quem não sabe SEO; decisões por semana.
   Checklist: **verificar a política interna de atividade paralela/conflito de interesse do empregador**
   (lembrete, não pesquisar); consulta jurídica (CDC, LGPD, RDC 622 art. 22) antes do E1; confirmar RT no CREA-SP.

## Como conduzir
- Primeiro: verificação cruzada e lacunas de pesquisa → estrutura do simulador (revisar a estrutura com o fundador
  antes de construir) → documentos.
- Trabalhar em `~/pessoal/SEO_Project/`; nada no repositório core-banking.
- Idioma: português. Moeda: R$ de 2026. Unidades métricas.
- Ao final, apontar as premissas de **confiança Baixa** no topo do tornado (provavelmente: custo por lead,
  fechamento, preço do contrato B2B, churn, tempo por serviço). É isso que o piloto de 30 dias mede primeiro.
