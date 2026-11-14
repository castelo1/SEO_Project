# Leitura — SEO para leads · 19 min · gerada em sex 13/11 22:48

> Reescrita ao fechar o item 8. **Fechados e verificados: itens 1, 2, 3, 5, 6, 7 e 8.** O mapa do mercado de busca
> (item 4) está escrito, **ainda não verificado**, com a coleta ao vivo em pausa até 23:17. Da fila de reserva, a
> planilha de medição está escrita (não verificada) e o levantamento de pontos de contrato está em curso.

## 1. Veredito em três linhas

- **O modelo é viável dentro das regras?** **Sim, numa forma mais estreita que a ideia inicial:** um site que se
  declara intermediário, nomeia em cada oferta a empresa licenciada e a licença dela, e leva a pessoa a falar direto
  com ela, no WhatsApp dela. **Não** é viável como "dedetizadora de fachada" com perfil próprio no mapa, nem como
  central de WhatsApp que repassa contatos. Se dá dinheiro, **não sei**: não há fonte brasileira de preço de lead
  exclusivo, de taxa de fechamento nem de disposição das licenciadas a pagar.
- **Fechado e verificado:** o reenquadramento (item 1); as quatro restrições lidas na fonte primária (item 2); o
  estudo de ranqueamento em cinco arquivos (item 3, três verificações); os modelos de negócio (item 5: sete modelos
  ficam de pé; 11 de 12 afirmações sorteadas conferidas; 17 correções aplicadas e conferidas por mim no arquivo).
- **O que muda para você:** o mapa do Google não é ativo seu (o perfil é sempre da licenciada); o WhatsApp do botão é
  o dela, e o site só consegue provar o toque no botão; página por bairro em que só muda o nome do bairro é o exemplo
  de "página de entrada" da política de spam do Google; e tudo depende de **uma licenciada aceitar ser nomeada** —
  conversa que só você pode ter.

## 2. Decisões que só você toma (máximo 5)

As dez perguntas, com a opção adotada em cada uma e o que muda se a resposta for a outra, estão em
`/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`. As cinco primeiras, que são as que mais mudam o desenho:

| Pergunta (sim/não) | Recomendo | Se não responder |
|---|---|---|
| 1. Você conferiu a política do seu empregador sobre atividade paralela? | Conferir antes de qualquer outra coisa (não pesquisei, por regra da rodada) | Tratado como não conferido: o projeto fica em estudo e protótipo local |
| 2. O site se apresenta como intermediário declarado — sem perfil próprio no Google, sem se passar por dedetizadora, nomeando a licenciada e a licença em cada oferta? | Sim — é o formato que o levantamento deixa de pé | O desenho segue assim |
| 3. O site lista só licenciadas que autorizaram, e não empresas tiradas do cadastro público? | Sim — listar sem autorização não foi levantado | Só parceiras autorizadas |
| 4. Você mesmo conversa com algumas licenciadas (3 a 5) para saber se aceitam ser nomeadas e se pagariam, antes de qualquer gasto? | Sim — a sessão não contata ninguém, e sem isso não há página de oferta | "Há licenciada disposta" segue como premissa |
| 5. Na primeira versão, o contato é só pelo botão que abre o WhatsApp da licenciada, e o formulário fica para depois? | Sim — o site não recebe nome, telefone nem conversa | O desenho segue com o botão |

Decisões operacionais (baixar PDFs oficiais, manter o limite de buscas ao vivo, histórico do git) estão na "Fila do
owner" de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`.

## 3. As restrições: o que cada fonte diz hoje e o que isso corta do plano

Detalhe, citações e endereços: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`. É levantamento com
fonte, não parecer jurídico.

| Restrição | O que a fonte diz (lido em 13/11/2026) | O que corta do plano |
|---|---|---|
| **Perfil de empresa do Google** | A lista de empresas inelegíveis traz "Lead generation agents or companies" e empresas só on-line; o perfil exige contato presencial com clientes. Telefone e site do perfil têm de ser os da empresa real, sob controle dela. Terceiro pode administrar o perfil com consentimento expresso, mantendo a empresa como proprietária. Conta com padrão de violação tem todos os perfis suspensos; o recurso só pode ser enviado uma vez | Perfil próprio (inclusive com endereço oculto); endereço de fachada; perfil da parceira com o seu site ou o seu número; avaliação incentivada. Sobra: gestão autorizada do perfil **dela** |
| **Propaganda de controle de pragas** | RDC 622/2022, art. 22: toda propaganda de empresa especializada traz a identificação dela no órgão licenciador e o número da licença; veda texto de medo, selos como "aprovado pela Vigilância Sanitária" e as palavras "inócuo", "seguro", "atóxico", "produto natural". CDC, arts. 36 a 38: publicidade identificável, não enganosa nem por omissão, com prova guardada. A norma **não fala** de site intermediário | Página "anônima" com cara de dedetizadora e botão de orçamento é o formato de maior risco (norma silente). Cada página de oferta nomeia a licenciada e a licença, ou é conteúdo que não oferece o serviço em nome próprio |
| **LGPD** | Art. 7º, § 5º: repassar o contato a outro controlador exige consentimento específico para esse fim (ressalvadas as outras bases legais); autorização genérica é nula; o ônus da prova é de quem capta; na exclusão, avisa-se de imediato cada empresa que recebeu. A autoridade nacional ainda **não tem** norma sobre consentimento nem sobre venda de dados | "Lista de contatos como ativo" só vale para quem autorizou cada finalidade; repasse a várias empresas só se a pessoa souber a quantas e a quais; nada de dado de saúde |
| **WhatsApp Business** | Política de Mensagens (23/09/2026): só se contata quem deu o número e o opt-in; o opt-in nomeia a empresa que vai falar. Termos da Meta para a API, cláusula 4.1(b): vedado compartilhar ou vender a terceiros os dados obtidos pela Plataforma (leitura literal). Termos do aplicativo gratuito: silentes sobre repasse. O link que abre conversa direta é recurso oficial | O "número próprio que faz a triagem e encaminha o lead" (recomendado pela pesquisa antiga) cai na API e fica incerto no aplicativo |

**A pesquisa de 25/09 valia?** Na direção, sim; no detalhe, foi corrigida em vários pontos (cada correção está no fim
de cada seção do arquivo).

## 4. Itens

| Item | Estado | Portão | Evidência do verificador |
|---|---|---|---|
| 1 Reenquadramento | **fechado** | `docs/ESTADO.md` novo; prompt antigo movido com `git mv`; nada apagado | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item1.md` |
| 2 Restrições na fonte primária | **fechado** | quatro seções com fonte, data, trecho e veredito | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item2.md` |
| 3 Estudo de ranqueamento | **fechado**, com três ressalvas (seção 6) | três guias, a parte do ChatGPT e o roteiro de teste, cada tática com fonte e classe | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3.md` (índice de três verificações) |
| 4 Mapa do mercado de busca | em curso — texto e planilhas escritos (79 de 89 buscas), **não verificado**; coleta em pausa até 23:17 | `docs/mercado/serp_sp.md`, `data/serp_sp.csv`, `data/palavras_chave.csv` | — |
| 5 Modelos de negócio | **fechado**, com uma ressalva (seção 6) | modelos que não dependem de perfil nem de se passar por dedetizadora, depois os que dependem; contas, preço do lead, riscos; R$ 20–60 confirmado ou derrubado | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item5.md` (aprovado com ressalvas); correções em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/correcoes_item5.md` |
| 6 Desenho, versão 0 | **fechado**, com uma ressalva (seção 6) | arquitetura, o que cada página exibe, captação com texto de consentimento, medição, automação, fases, "o que tornaria isto inviável" | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item6.md` e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item6_correcoes.md` (dois leitores independentes, ambos "aprovado com ressalvas") |
| 7 Protótipo local | **fechado**, com uma ressalva (seção 6) | quatro páginas em HTML e CSS puros, tudo marcado "EXEMPLO", e um LEIA-ME que liga cada bloco ao desenho | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item7.md` (aprovado com ressalvas; 0 falha em 12) |
| 8 Perguntas ao owner | **fechado** na segunda tentativa, com uma ressalva (seção 6) | no máximo dez, na ordem de quanto mudam o desenho, cada uma com a opção padrão; a do empregador é fixa | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item8.md` (1ª versão reprovada) e `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item8_v2.md` (2ª versão aprovada com ressalvas) |

## 5. O que é consenso · o que é disputado · o que não sei

- **Consenso (fonte oficial lida e verificada):**
  - as quatro restrições da seção 3;
  - o Google não vende nem garante posição, no orgânico nem no mapa, e nenhum terceiro pode prometê-la;
  - a política de spam do Google dá como exemplo de "página de entrada" páginas por região que afunilam o usuário;
    comprar link viola a política; enviar consultas automáticas para checar posição também;
  - no mapa, o Google declara três fatores (relevância, distância e destaque), **sem dizer qual pesa mais**; empresa
    que vai ao cliente tem um perfil por base real, com endereço oculto;
  - para aparecer nos resumos de IA do Google não há requisito extra; o Google não usa `llms.txt`; o resultado rico
    de perguntas frequentes deixou de existir em maio de 2026;
  - para poder ser citado pelo ChatGPT, o site tem de permitir o robô de busca da OpenAI (`OAI-SearchBot`); bloquear
    o robô de treino não tira o site da busca;
  - as três plataformas brasileiras de pedido de orçamento lidas (GetNinjas, Cronoshare, oHub) cobram do prestador,
    adiantado, por contato dividido entre vários prestadores; lead inválido se devolve em crédito, não em dinheiro.
- **Disputado:** qual fator pesa mais no mapa e quanto a posição cai com a distância (estudos dos Estados Unidos);
  quanto pesam os links; se o resumo de IA reduz o clique e quanto; de onde vem o índice da busca do ChatGPT; se o
  repasse pelo aplicativo gratuito do WhatsApp é permitido; se "o cliente não respondeu" conta como lead inválido.
- **Não sei:** qualquer número **do Brasil** de clique, de prazo ou de posição; quanto vale um lead exclusivo de
  dedetização em São Paulo, que fração dos contatos vira serviço e se as licenciadas pagam; volume de busca; que
  fontes o ChatGPT e o resumo de IA do Google citam para dedetização em São Paulo; se uma página genérica, sem empresa
  nomeada, conta como "propaganda de empresa especializada".

## 6. Afirmado e NÃO conferido · o que não foi feito e por quê

- **Item 3, três ressalvas:** (1) o que a ajuda oficial da OpenAI diz sobre a busca do ChatGPT foi lido só por mim, no
  navegador; os verificadores receberam erro 403; (2) 12 defeitos menores foram corrigidos depois da última
  verificação e ainda não passaram por novo verificador; (3) duas das 30 perguntas do roteiro do ChatGPT ficaram sem
  bairro, de propósito.
- **Item 5, uma ressalva:** as 17 correções pedidas pelo verificador foram aplicadas por um corretor e conferidas por
  mim no arquivo, **não** por um novo verificador (fica para a segunda passada). O que o item diz: o "R$ 20 a 60 por
  lead" da pesquisa antiga **não se confirma nem se derruba** — era resultado de uma fórmula; o único preço público
  brasileiro achado é de outro produto (oHub: R$ 19 a R$ 41 por resposta, pedido de empresa, dividido entre
  fornecedores). Toda conta de receita do arquivo é ilustração, com premissas arbitrárias marcadas.
- **Item 2:** os trechos marcados **[S]** foram lidos só pelo subagente (30 pontos); os **[N]** foram reconferidos por
  mim no texto bruto da página.
- **Item 4 (não verificado):** tudo vem de **uma** amostra — 79 buscas, numa sexta à noite, logado na sua conta, de um
  só ponto da Grande São Paulo, **coletadas por script** (o próprio arquivo diz que isso é a "consulta automática" que
  a política do Google veda; a decisão de manter está na fila do owner). Números preliminares: resumo de IA em 73 das
  79 buscas; bloco de mapa em 68; anúncio em 60; 10 domínios com 39% dos resultados; 50 dos 67 sites de serviço lidos
  têm páginas por bairro, região ou cidade; só 12 dos 67 mostram o número da licença — mas os 11 domínios que o
  mostram ocupam 37 das 79 primeiras posições. A classificação dos sites foi feita por ferramenta que resume a página:
  "não visto" não prova ausência.
- **Item 6, uma ressalva:** o desenho passou por dois leitores independentes; os 10 ajustes pedidos pelo segundo
  foram aplicados por mim e ainda não foram relidos por terceiro. No desenho, 17 escolhas são premissas sem evidência
  (lista na seção 10 dele). **Não levantados:** o tratamento do endereço IP que o servidor registra junto do toque no
  botão; se a página de preços conta como propaganda; a norma sanitária de restaurantes.
- **Item 7, uma ressalva:** as 22 correções pedidas pelo verificador foram aplicadas por mim e ainda não foram
  relidas por terceiro. O verificador conferiu o código das páginas, não as abriu em navegador. A página de
  restaurantes tem um bloco "[A ESCREVER]" (a norma sanitária de serviços de alimentação não foi levantada).
- **Item 8, uma ressalva:** a primeira versão das perguntas foi reprovada (afirmações mais fortes que a fonte e
  perguntas com várias decisões coladas); a segunda foi aprovada com ressalvas; as 14 correções da terceira versão
  foram aplicadas por mim e ainda não foram relidas por terceiro.
- **Fila de reserva:** o modelo de planilha de medição
  (`/home/ancastelo/pessoal/SEO_Project/docs/medicao_modelo.md`) está escrito e **não verificado**.
- **Não feito:** as 10 buscas de confiança, preço e informação e 5 repetições (só depois das 23:17); a lista completa
  do Google Maps; normas e guias que só existem em PDF; o Diário Oficial; o site do Centro de Vigilância Sanitária
  (erro 403); valores de domínio, hospedagem e advogado.
- **Erros meus, já registrados:** três intervalos de busca abaixo dos 20 segundos da regra (17, 18 e 19 segundos);
  lotes de teste descartados (cerca de 15 buscas perdidas); verificação de robô do Google às 21:16, não resolvida.

## 7. Arquivos para abrir, na ordem (soma = 19 min)

1. `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` — 1 min
2. `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` — 3 min
3. `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos e "O que as quatro
   restrições, juntas, deixam de pé") — 4 min
4. `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (seções 1, 8 e 9) — 5 min
5. `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html`, aberto no navegador, e as três páginas ligadas a ele —
   2 min
6. `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (só "Em uma página") — 2 min
7. `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (só "Em uma página"; não verificado) — 2 min
