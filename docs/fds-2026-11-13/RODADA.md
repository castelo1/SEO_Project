# Raia de SEO para leads (L4b) — sessão em `/home/ancastelo/pessoal/SEO_Project`

As regras da rodada estão no prompt de sistema (cópia em
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md`). Valem também o `CLAUDE.md` de `~/pessoal` e o
deste projeto. Este arquivo define **o que o projeto é, os itens e os portões**, e basta sozinho: a `FICHA.md` ao lado
e o `PROMPT_PLANO.md` da raiz são do foco anterior, só histórico; não definem item, portão nem entregável.

A rodada vai até segunda 16/11 às 06:00 (Brasília) e roda ao mesmo tempo que outra raia pessoal, que pode usar o
mesmo navegador. Há tempo: prefira ir fundo a terminar cedo.

## O que o projeto é (decisão do owner em 13/11/2026)

Nas palavras dele: "construir uma inteligência de SEO para conseguir e depois vender leads para esse tipo de empresa
que atua aqui em São Paulo. Primeiro vamos precisar estudar, aprender, e criar um sistema de SEO focado nesse mercado.
Ranqueamento por Google, IA e Google Maps, incluindo site completo, leads por WhatsApp."

"Esse tipo de empresa" são as de controle de pragas (dedetização). O projeto **deixou de ser** o estudo de abrir uma
dedetizadora: nada de simulador, parecer de abrir ou não abrir, curadoria de custos de operação. O owner não tem
experiência em SEO e ainda não deu mais contexto. Nesta rodada: **estudar, mapear, desenhar e prototipar em arquivo
local**. Nada é publicado, comprado, cadastrado ou enviado.

## O que já existe na pasta (25/09/2026, foco anterior)

`research/01_regulacao_licencas.md`, `research/02_mercado_servicos_precos.md`, `research/03_modelos_negocio_escala.md`,
`research/04_mao_de_obra_custos_operacao.md` e três CSVs em `data/`. Use como **hipóteses com endereço**, não como
fato: a pesquisa tem sete semanas, foi feita por subagentes e parte das fontes é de segunda mão. Em especial, ela
afirma quatro coisas que decidem este projeto e que o item 2 reconfere na fonte primária:
- quem só gera leads é inelegível ao perfil de empresa do Google (`research/03…` linhas 13 e 102–108);
- propaganda de controle de pragas tem de identificar a executora e a licença (`research/01…` linhas 44 e 157–159);
- repasse de contato exige consentimento (`research/03…` linha 167);
- o lead vale R$ 20–60 e a receita realista é de R$ 3–10 mil por mês, com confiança baixa (`PROMPT_PLANO.md` linha 50).

## Regra de evidência

SEO é um assunto cheio de afirmação sem prova. Cada prática, tática ou número entra com fonte (URL), data da fonte,
data da leitura e **uma** destas classes:

| Classe | O que é | Pode virar regra do sistema? |
|---|---|---|
| A — documentação oficial | Google, Meta/WhatsApp, lei, norma, órgão regulador, lida na fonte | sim |
| B — estudo com dado | amostra, método e dado expostos; dá para conferir | sim, citando o limite da amostra |
| C — relato de praticante | caso com site, busca e data que você consegue abrir; autor não vende o método | só como hipótese a testar, marcada |
| D — vendedor de curso, ferramenta ou agência | quem ganha com a afirmação, mesmo com caso mostrado | não; entra como "alegação", e só sobe de classe se A ou B confirmar |

- Para cada fonte, anote **quem ganha com a afirmação**.
- "Consenso" exige classe A, ou duas fontes B independentes. Onde as fontes se contradizem, diga.
- Prática apoiada só em fonte anterior a 2025 leva "pode estar desatualizada"; sobre respostas de IA, anterior a 2026.
- Número de outro país entra com o país ao lado e não é convertido para a conta brasileira.

**Exemplos do owner:** `docs/fds-2026-11-13/EXEMPLOS_X.md`. Leia pelo navegador pessoal o link da seção "Base do
estudo" antes do item 3 e extraia o método, tática por tática, cada uma classificada (o autor vende curso: classe D
até prova em contrário). Não copie o texto para o repositório. Se o navegador estiver bloqueado, siga sem ele e deixe
o lugar reservado na leitura.

## Itens, na ordem

| Ordem | Item | Portão | Horas |
|---|---|---|---|
| 1 | Reenquadramento | `docs/ESTADO.md` novo: o que o projeto é agora, o que do material antigo se aproveita (com caminho e linha) e o que fica como histórico. `PROMPT_PLANO.md` movido para `arquivo/2026-09_foco_anterior/` com `git mv`. Nada apagado | 1 |
| 2 | **Restrições que decidem o modelo, lidas na fonte atual** | `docs/estudo/00_restricoes.md` com quatro seções, cada uma com a URL da fonte primária, a data de leitura, o trecho curto que decide, e o veredito para um gerador de leads: **permitido / permitido com condição / vedado / não conclusivo**. (a) **Perfil de empresa do Google:** diretrizes e regras de elegibilidade vigentes, na página do Google — gerador de leads pode ter perfil? o que conta como endereço e atendimento? o que acontece com perfil fora da regra? quais caminhos legítimos para o mapa sobram (por exemplo, o perfil ser da empresa licenciada parceira)? (b) **Propaganda de controle de pragas:** texto da RDC 622/2022 na fonte oficial e a norma da vigilância sanitária de São Paulo (estado e município) — o que um site que anuncia o serviço tem de exibir e o que não pode dizer; e o que o Código de Defesa do Consumidor diz de publicidade enganosa. (c) **LGPD:** base legal e consentimento para captar um contato e repassá-lo a uma ou mais empresas; quem é controlador; direito de exclusão. (d) **WhatsApp Business:** política vigente da Meta sobre mensagens comerciais, opt-in e repasse de contato a terceiros. Cada seção termina dizendo se a pesquisa de 25/09 continua valendo ou foi corrigida. Fonte primária inacessível = "não conclusivo", nunca preenchido com fonte de segunda mão | 3–4 |
| 3 | Estudo: como se ranqueia um serviço local hoje | Três guias em `docs/estudo/`: (a) busca orgânica do Google para serviço local; (b) Google Maps e perfil de empresa, **dentro do que o item 2 permitiu**; (c) respostas de IA (o que faz um site ser citado). Cada tática com fonte e classe A–D. Cada guia termina em "o que é consenso / o que é disputado / o que não sei". Guia (c) curto é resultado aceitável **Pedido do dono em 13/11: além do Google, estudar o ranqueamento no ChatGPT.** O guia (c) passa a ter uma parte própria, `docs/estudo/03b_chatgpt.md`: como a busca do ChatGPT escolhe e cita fontes para um pedido de serviço local (de onde vem o índice, o papel do Bing e dos robôs da OpenAI como `OAI-SearchBot` e `GPTBot`, o que a documentação da OpenAI diz que um site precisa permitir, de onde vêm os dados de empresa local e de mapa, como citações em terceiros, avaliações e diretórios pesam), o que difere do Google e dos resumos de IA do Google, e como medir presença (quais perguntas testar, com que frequência, o que registrar). Fonte primária primeiro (documentação da OpenAI e do Bing), depois estudos com dado; relato de praticante e de vendedor de curso só com a classe marcada. A sessão **não** abre o ChatGPT nem digita em página: entrega `docs/estudo/03b_chatgpt_roteiro_de_teste.md` com 30 perguntas reais de um morador ou síndico de São Paulo (por praga, bairro, urgência) e a planilha de registro, para o dono rodar na conta dele; o desenho do item 6 e o protótipo do item 7 trazem o que o estudo indicar (por exemplo `robots.txt`, dados estruturados, página "quem somos" verificável). | 6–8 |
| 4 | Mapa do mercado de busca de dedetização em São Paulo | `docs/mercado/serp_sp.md` + `data/serp_sp.csv`: para as buscas principais (por praga, por bairro ou região, "24 horas", empresa × residência), quem aparece no orgânico e no mapa — tipo de página, se é empresa, diretório ou gerador de leads, e os padrões dos primeiros colocados. Cada busca registrada com termo, hora, conta logada (sim/não) e a localização que o Google mostrou. Amostra declarada, não censo. E `data/palavras_chave.csv`: mapa de termos por praga × bairro × intenção, com a coluna "volume: não medido" e o método para medir quando o owner tiver ferramenta com conta | 5–7 |
| 5 | Modelos de negócio de venda de leads | `docs/modelos_de_negocio.md`: **primeiro os modelos que não dependem de perfil próprio no mapa nem de se passar por dedetizadora** (site de conteúdo e comparação que identifica as licenciadas; pagamento por lead; exclusividade por região; gestão do perfil e do site da própria licenciada, com autorização dela); depois os que dependem, marcados com o veredito do item 2. Para cada um: como opera, as contas (com país e classe de cada número), precificação do lead (por tipo de praga, residência × empresa, exclusivo × compartilhado), e os riscos — dependência do Google, propaganda, LGPD, WhatsApp, conflito com o parceiro. O valor do lead da pesquisa antiga é confirmado ou derrubado, com fonte | 4–5 |
| 6 | Desenho do sistema, versão 0, para aprovação | `docs/desenho_v0.md`: arquitetura do site (páginas por praga × região, o que cada uma precisa ter, onde cada página exibe o que o item 2(b) exige); captação e roteamento do lead por WhatsApp, **com o texto de consentimento, para quantas empresas o contato vai e como a pessoa pede a exclusão**; como medir (posição, clique, lead, lead vendido); o que é automatizável; fases, com o que cada fase prova antes de gastar dinheiro; e a seção "o que tornaria isto inviável", respondendo as quatro restrições uma a uma. Cada escolha aponta para o trecho do estudo que a sustenta; premissa sem evidência A ou B é marcada. O desenho **não** depende de perfil de empresa fora da regra, endereço fictício, avaliação fabricada nem link comprado | 4–5 |
| 7 | Protótipo local do site | `prototipo/` em HTML e CSS puros, sem dependência e sem publicar: página inicial, uma página-modelo de praga × região, uma de empresa (restaurante ou condomínio), a página de política de privacidade com o consentimento do item 6. Todo nome de empresa, telefone, licença e depoimento leva "EXEMPLO". Um `prototipo/LEIA-ME.md` liga cada bloco da página à escolha do desenho que o justifica | 3–4 |
| 8 | Perguntas ao owner | `docs/perguntas_owner.md`: no máximo dez, em ordem de quanto mudam o desenho, cada uma com a opção adotada por padrão. Uma delas é fixa: "você conferiu a política do seu empregador sobre atividade paralela?" (só a pergunta; não pesquise) | 0,5 |

## Fila de reserva (depois dos 8 itens, na ordem)

1. Ampliar o mapa de palavras-chave e a amostra de buscas para mais bairros e pragas, dentro do limite de buscas.
2. Análise de 10 páginas que ranqueiam bem (estrutura, tamanho, dados estruturados, sinais locais), comparadas com a
   página-modelo do protótipo; ajuste o protótipo e diga o que mudou.
3. Plano de conteúdo de 90 dias: quais páginas primeiro e por quê, apontando para o mapa de palavras-chave.
4. Levantamento dos pontos de um contrato de venda de leads (região, exclusividade, preço, disputa de lead inválido),
   com fonte; levantamento, não minuta para assinar.
5. Modelo de planilha de medição em CSV (posição, clique, lead, lead vendido) com as definições de cada coluna.

## Segunda passada (depois da reserva)

Para cada item fechado, um revisor **novo**, em contexto limpo, sem ler a primeira verificação: refaz a conferência
do prompt de sistema e grava `_runs/verificacao2_item<N>.md`. Prioridade: item 2 (reabrir cada fonte primária) e as
afirmações do desenho. Achado procedente: corrija, recomite e anote na leitura. Depois reescreva a leitura.

## Quando não houver mais nada

Não invente trabalho. Escreva "RODADA CONCLUÍDA em <dia HH:MM>" no topo do painel e da leitura, confira
`git status --porcelain` vazio e zero commit sem push, feche as abas que abriu. Daí em diante, a cada turno: `date`,
a tabela item × estado e uma espera de 10 minutos (`sleep 590`). Não abra o navegador, não crie arquivo, não lance
subagente. Só volte a trabalhar se aparecer resposta nova em `RESPOSTAS_OWNER.md`.

## Fora da rodada

Comprar domínio, publicar site, criar ou reivindicar perfil de empresa, abrir conta, falar com qualquer empresa,
ferramentas que exigem conta, anúncios pagos, simulador e parecer do foco anterior.
