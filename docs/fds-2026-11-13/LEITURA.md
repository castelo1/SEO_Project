# Leitura — SEO para leads · 20 min · gerada em sáb 14/11 02:43

> Reescrita ao fim da **segunda passada**. Os oito itens e as cinco tarefas de reserva estão fechados, cada um com o
> arquivo do verificador. Na segunda passada, 12 revisores novos — sem ler a primeira verificação — reabriram tudo, em 14 relatórios:
> **todos devolveram "aprovado com ressalvas"; nenhum portão descumprido; nenhum veredito das restrições mudou.**
> Os 209 achados (144 nos itens, 65 nas reservas) foram aplicados, por corretores ou por mim. Essas correções não
> foram relidas por um terceiro leitor: a rodada pede uma segunda passada, não uma terceira.

## 1. Veredito em três linhas

- **O modelo é viável dentro das regras?** **Sim, numa forma mais estreita que a ideia inicial:** um site que se
  declara intermediário, nomeia em cada oferta a empresa licenciada e a licença dela, e leva a pessoa a falar direto
  com ela, no WhatsApp dela. **Não** é viável como "dedetizadora de fachada" com perfil próprio no mapa, nem como
  central de WhatsApp que repassa contatos. Se dá dinheiro, **não sei**: não há fonte brasileira de preço de lead
  exclusivo, de taxa de fechamento nem de disposição das licenciadas a pagar.
- **Fechado e verificado duas vezes:** reenquadramento; as quatro restrições lidas na fonte primária; o estudo de
  ranqueamento; o mapa do mercado de busca (129 buscas ao vivo em duas coletas); os modelos de negócio (sete ficam de
  pé); o desenho; o protótipo local de quatro páginas; as dez perguntas a você; e as cinco tarefas de reserva.
- **O que muda para você:** o mapa do Google não é ativo seu (o perfil é sempre da licenciada); o WhatsApp do botão é
  o dela, e o site só consegue provar o toque no botão; página por bairro em que só muda o nome do bairro é o exemplo
  de "página de entrada" da política de spam do Google; e tudo depende de **uma licenciada aceitar ser nomeada** —
  conversa que só você pode ter.

## 2. Decisões que só você toma (máximo 5)

As dez perguntas, com a opção adotada em cada uma e o que muda se a resposta for a outra, estão em
`/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md`. Para responder, crie
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RESPOSTAS_OWNER.md`. As cinco que mais mudam o desenho:

| Pergunta (sim/não) | Recomendo | Se não responder |
|---|---|---|
| 1. Você conferiu a política do seu empregador sobre atividade paralela? | Conferir antes de qualquer outra coisa (não pesquisei, por regra da rodada) | Tratado como não conferido: o projeto fica em estudo e protótipo local |
| 2. O site se apresenta como intermediário declarado — sem perfil próprio no Google, sem se passar por dedetizadora, nomeando a licenciada e a licença em cada oferta? | Sim — é o formato que o levantamento deixa de pé | O desenho segue assim |
| 3. O site lista só licenciadas que autorizaram, e não empresas tiradas do cadastro público? | Sim — listar sem autorização não foi levantado | Só parceiras autorizadas |
| 4. Você mesmo conversa com algumas licenciadas (3 a 5) para saber se aceitam ser nomeadas e se pagariam, antes de qualquer gasto? | Sim — a sessão não contata ninguém, e sem isso não há página de oferta | "Há licenciada disposta" segue como premissa |
| 5. Na primeira versão, o contato é só pelo botão que abre o WhatsApp da licenciada, e o formulário fica para depois? | Sim — o site não recebe nome, telefone nem conversa | O desenho segue com o botão |

Mudou na segunda passada: a opção padrão da pergunta 10 (medir o volume de busca com a sua conta) passou a "sim, no
passo (d) da fase 1", que é o que o desenho já previa. Decisões operacionais (baixar PDFs oficiais, manter o limite de
buscas ao vivo, reescrever o histórico do git) estão na "Fila do owner" de
`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`.

## 3. As restrições: o que cada fonte diz hoje e o que isso corta do plano

Detalhe, citações e endereços: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`. É levantamento com
fonte, não parecer jurídico. Na segunda passada os 34 endereços citados foram reabertos (e mais 5 achados no caminho) e as citações conferem.

| Restrição | O que a fonte diz (lido em 13 e 14/11/2026) | O que corta do plano |
|---|---|---|
| **Perfil de empresa do Google** | A lista de empresas inelegíveis traz "Lead generation agents or companies" e empresas só on-line; o perfil exige contato presencial com clientes. Telefone e site do perfil têm de ser os da empresa real, sob controle dela. Terceiro pode administrar o perfil com consentimento expresso, mantendo a empresa como proprietária. Conta com padrão de violação tem todos os perfis suspensos | Perfil próprio (inclusive com endereço oculto); endereço de fachada; perfil da parceira com o seu site ou o seu número; avaliação incentivada. Sobra: gestão autorizada do perfil **dela** |
| **Propaganda de controle de pragas** | RDC 622/2022, art. 22: toda propaganda de empresa especializada traz a identificação dela no órgão licenciador e o número da licença; veda texto de medo, selos como "aprovado pela Vigilância Sanitária" e as palavras "inócuo", "seguro", "atóxico", "produto natural". CDC, arts. 36 a 38: publicidade identificável, não enganosa nem por omissão, com prova guardada. A norma **não fala** de site intermediário | Página "anônima" com cara de dedetizadora e botão de orçamento é o formato de maior risco. Nomear a licenciada em cada oferta atende ao que as normas lidas pedem da propaganda dela; se isso basta para o site de terceiro, a norma é silente |
| **LGPD** | Art. 7º, § 5º: repassar o contato a outro controlador exige consentimento específico para esse fim (ressalvadas as outras bases legais); autorização genérica é nula; o ônus da prova é de quem capta; na exclusão, avisa-se de imediato cada empresa que recebeu. A autoridade nacional ainda **não tem** norma sobre consentimento; a agenda dela traz "consentimento" e "agregadores de dados" em andamento | "Lista de contatos como ativo" só vale para quem autorizou cada finalidade; repasse a várias empresas só se a pessoa souber a quantas e a quais; nada de dado de saúde |
| **WhatsApp Business** | Política de Mensagens (23/09/2026): só se contata quem deu o número e o opt-in; o opt-in nomeia a empresa que vai falar; a trava de finalidade não cobre o conteúdo da conversa. Termos da Meta para a API, cláusula 4.1(b): vedado compartilhar ou vender a terceiros os dados obtidos pela Plataforma; a cláusula 1.3 faz os Termos prevalecerem sobre as políticas (as duas conferidas por mim no texto bruto em 14/11). Termos do aplicativo gratuito: silentes sobre repasse. O link que abre conversa direta é recurso oficial | O "número próprio que faz a triagem e encaminha o lead" (recomendado pela pesquisa antiga) cai na API e fica "não conclusivo" no aplicativo |

**A pesquisa de 25/09 valia?** Na direção, sim; no detalhe, foi corrigida em vários pontos (cada correção está no fim
de cada seção do arquivo; o resumo está em `/home/ancastelo/pessoal/SEO_Project/docs/ESTADO.md`, seção 2.1).

## 4. Itens

Todos os arquivos de evidência estão em `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/`; a coluna dá
o nome do arquivo da primeira verificação e o da segunda passada (os achados aplicados estão em `correcoes2_*.md`).

| Item | Estado | Portão | Evidência do verificador (em `_runs/`) |
|---|---|---|---|
| 1 Reenquadramento | **fechado** | `docs/ESTADO.md` novo; prompt antigo movido com `git mv`; nada apagado | `verificacao_item1.md`; `verificacao2_item1.md` (50 de 51 remissões conferem) |
| 2 Restrições na fonte primária | **fechado** | quatro seções com fonte, data, trecho e veredito | `verificacao_item2.md`; `verificacao2_item2.md` (34 fontes reabertas; 1 falha em 12) |
| 3 Estudo de ranqueamento | **fechado** | três guias, a parte do ChatGPT e o roteiro de teste, cada tática com fonte e classe | `verificacao_item3.md` (índice de três); `verificacao2_item3_guias_a_b.md` e `verificacao2_item3_ia_chatgpt.md` (48 afirmações reabertas, sem falha) |
| 4 Mapa do mercado de busca | **fechado** | quem aparece no orgânico e no mapa, tipo de página, empresa × diretório × gerador de leads, padrões dos primeiros; cada busca com termo, hora, conta e local; mapa de termos com "volume: não medido" | `verificacao_item4.md`; `verificacao2_item4.md` (0 falha em 12; registro das 89 buscas sem divergência) |
| 5 Modelos de negócio | **fechado** | modelos que não dependem de perfil nem de se passar por dedetizadora, depois os que dependem; contas, preço do lead, riscos; R$ 20–60 confirmado ou derrubado | `verificacao_item5.md`; `verificacao2_item5.md` (39 de 40 fontes reabertas; 0 falha em 12) |
| 6 Desenho, versão 0 | **fechado** | arquitetura, o que cada página exibe, captação com texto de consentimento, medição, automação, fases, "o que tornaria isto inviável" | `verificacao_item6.md` e `verificacao_item6_correcoes.md`; `verificacao2_item6.md` (140 remissões conferidas; 0 falha em 12) |
| 7 Protótipo local | **fechado** | quatro páginas em HTML e CSS puros, tudo marcado "EXEMPLO", e um LEIA-ME que liga cada bloco ao desenho | `verificacao_item7.md`; `verificacao2_item7.md` (0 falha em 12) |
| 8 Perguntas ao owner | **fechado** (na segunda tentativa) | no máximo dez, na ordem de quanto mudam o desenho, cada uma com a opção padrão; a do empregador é fixa | `verificacao_item8.md` (1ª versão reprovada) e `verificacao_item8_v2.md`; `verificacao2_item8.md` (3 falhas em 52) |
| Reservas 1 a 5 | **fechadas** | ampliar amostra e mapa de termos; dez páginas × página-modelo; plano de 90 dias; pontos de contrato; planilha de medição | `verificacao_reserva<N>.md` (a 3 foi reprovada na 1ª versão); `verificacao2_reserva<N>.md` (falhas em 12: 0, 2, 1, 0, 0) |

## 5. O que é consenso · o que é disputado · o que não sei

- **Consenso (fonte oficial lida e verificada):**
  - as quatro restrições da seção 3;
  - o Google não vende nem garante posição, no orgânico nem no mapa, e nenhum terceiro pode prometê-la;
  - a política de spam do Google dá como exemplo de "página de entrada" páginas por região que afunilam o usuário;
    comprar link viola a política; enviar consultas automáticas à Busca para checar posição também (estender isso à
    "grade de posição" no Maps é leitura do guia — o projeto não usa grade);
  - no mapa, o Google declara três fatores (relevância, distância e destaque), **sem dizer qual pesa mais**; empresa
    que vai ao cliente tem um perfil por base real, com endereço oculto;
  - para aparecer nos resumos de IA do Google não há requisito extra; o Google ignora `llms.txt`; o resultado rico de
    perguntas frequentes deixou de existir em maio de 2026;
  - para poder ser citado pelo ChatGPT, o site tem de permitir o robô de busca da OpenAI (`OAI-SearchBot`); bloquear
    o robô de treino não tira o site da busca.
- **Padrão nos termos das plataformas lidas (cada uma sobre si; não conta como consenso pela regra da rodada):** as
  três plataformas brasileiras de pedido de orçamento lidas (GetNinjas, Cronoshare, oHub) cobram do prestador,
  adiantado, por contato dividido entre vários prestadores; lead inválido se devolve em crédito ou saldo (só a
  Cronoshare diz com todas as letras que não devolve em dinheiro).
- **Disputado:** qual fator pesa mais no mapa e quanto a posição cai com a distância (estudos dos Estados Unidos);
  quanto pesam os links; se o resumo de IA reduz o clique e quanto; de onde vem o índice da busca do ChatGPT; se o
  repasse pelo aplicativo gratuito do WhatsApp é permitido; se "o cliente não respondeu" conta como lead inválido.
- **Não sei:** qualquer número **do Brasil** de clique, de prazo ou de posição; quanto vale um lead exclusivo de
  dedetização em São Paulo, que fração dos contatos vira serviço e se as licenciadas pagam; volume de busca; que
  fontes o ChatGPT e o resumo de IA do Google citam para dedetização em São Paulo; se uma página genérica, sem empresa
  nomeada, conta como "propaganda de empresa especializada"; se o site é o tipo de provedor que o Marco Civil obriga a
  guardar registros de acesso.

## 6. Afirmado e NÃO conferido · o que não foi feito e por quê

**O que a segunda passada mudou de conteúdo (nenhum veredito mudou):**
- *Desenho e protótipo:* o aviso ao lado do botão e a política de privacidade agora dizem tudo o que o servidor
  registra (endereço IP e identificação do navegador); a licenciada informa ao site **só números**, nunca nome,
  telefone ou conversa; entrou o campo "contato da empresa para dados pessoais"; o bloco que repetia a lista de
  bairros virou remissão; a lista de premissas sem evidência foi de 17 para 22.
- *Guarda de registros:* o Marco Civil (art. 15) manda certo tipo de provedor guardar registros de acesso por 6
  meses; o regulamento (Decreto nº 8.771/2016, art. 13, § 2º, lido por mim no texto bruto) manda reter o mínimo e
  excluir atingida a finalidade ou o prazo legal; um artigo incluído em 2026 estende a guarda do IP à porta de
  origem. Como isso se combina com "guardar pelo menor tempo possível" é **pergunta para o advogado** (pergunta 8).
- *Mapa do mercado:* nos sites lidos, ter páginas por localidade, WhatsApp ou número de licença **não separa os
  primeiros colocados dos demais** (por exemplo, licença visível em 5 de 19 dos que ficaram em primeiro, contra 12 de
  67 no total); a posição do navegador ("São Paulo" ou "Osasco") é inferência; "diretório, 4%" é piso.
- *Modelos:* o "R$ 20 a 60 por lead" da pesquisa antiga fica **"não confirmado"** — não se sustenta como número de
  trabalho e não foi derrubado por preço observado; o único preço público brasileiro achado é de outro produto (oHub:
  R$ 19 a R$ 41 por resposta, pedido de empresa, dividido entre fornecedores). Toda conta de receita é ilustração.
- *Estudo:* a "grade de posição" no mapa fica "não usar" em todos os arquivos; uma pergunta do roteiro do ChatGPT foi
  reescrita para ser de morador; uma fonte sobre respostas de IA foi rebaixada a "B fraca" (número sem amostra exposta).
- *Plano de 90 dias (4ª versão):* as páginas previstas cobrem de 235 a 239 dos 2.721 termos do mapa (8,6% a 8,8%); o
  mapa é uma grade de combinações geradas, com 129 termos de fato buscados e nenhum volume medido.

**Afirmado e não conferido:**
- **As correções da segunda passada** (209 achados) não foram relidas por terceiro; conferi por amostra no artefato
  e reproduzi os números novos do item 4 com o script do corretor.
- **Item 2:** 53 trechos seguem marcados [S] (lidos só por subagente); 68 estão [N] (conferidos por mim no texto
  bruto). Normas que só existem em PDF não foram lidas (por isso "qual número de licença vale na capital" e "razão
  social e endereço na propaganda" seguem não conclusivos).
- **Item 3:** a ajuda oficial da OpenAI sobre a busca do ChatGPT dá erro 403 às ferramentas dos revisores; só eu a li,
  no navegador, e em 14/11 testei por comparação de texto os dez trechos citados (os dez conferem). A página que
  falaria de `utm_source=chatgpt.com` e de `noindex` redireciona para outro assunto: **sem fonte primária lida**.
- **Item 4 e reserva 1:** tudo vem de **uma** amostra — 89 buscas numa sexta à noite e 40 na madrugada seguinte,
  logado na sua conta, de um só ponto de acesso, **coletadas por script** (o próprio arquivo diz que isso é a
  "consulta automática" que a política do Google veda; a decisão de manter está na fila do owner). Nas 79 buscas
  principais: resumo de IA em 73; bloco de mapa em 68; anúncio em 60; 10 domínios com 39% dos resultados; nas buscas
  por bairro, 87% dos resultados são páginas com o nome do local no endereço; só 12 dos 67 sites de serviço lidos
  mostram o número da licença. Na ampliação: o resumo de IA foi o primeiro marcador da página em 38 das 39 buscas em
  que apareceu, e o primeiro orgânico ficou abaixo da primeira tela em 23 de 40. A classificação dos sites foi feita
  por ferramenta que resume a página; nenhum número de licença foi conferido em base oficial; o coletor cortou os
  endereços em 50 caracteres, o que deixa em dúvida a classe de alguns resultados.
- **Item 5:** os detalhes de operação e contas dos modelos vedados entraram na segunda passada e não foram relidos.
- **Item 6:** 22 escolhas do desenho são premissas sem evidência (seção 10 dele). **Não levantados:** o tratamento do
  endereço IP no registro do servidor; se a página de preços conta como propaganda; a norma sanitária de restaurantes.
- **Item 7:** nenhum verificador abriu as páginas em navegador (conferiram o código). A página de restaurantes tem um
  bloco "[A ESCREVER]". Três dos quatro títulos têm 69 ou 70 caracteres, acima do máximo (67) visto nas dez páginas comparadas.
- **Reservas 2, 4 e 5:** as dez páginas foram escolhidas antes das 10 buscas de confiança e preço, e o script que as
  leu não foi guardado; no levantamento de contrato, o decreto de 2026 que altera o regulamento do Marco Civil não foi
  lido; a planilha de medição tem duas premissas próprias (como ratear a mensalidade em períodos de 28 dias; em que
  linha ela entra).

**Não feito:** a lista completa do Google Maps e os dados de cada perfil; o que o resumo de IA cita em cada busca;
buscas em outro dia, outro lugar, deslogado ou no celular; normas e guias que só existem em PDF; o Diário Oficial; o
site do Centro de Vigilância Sanitária (erro 403); valores de domínio, hospedagem e advogado. Nada foi publicado,
comprado, cadastrado nem enviado; nenhuma empresa ou pessoa foi contatada; nenhum anúncio foi clicado.

**Erros meus, já registrados:** três intervalos de busca abaixo dos 20 segundos da regra (17, 18 e 19 segundos) e
lotes de teste com buscas sobrepostas (cerca de 15 buscas perdidas) — a regra do intervalo **foi descumprida** nesses
casos; verificação de robô do Google às 21:16 de 13/11, não resolvida, com pausa de duas horas e retomada sem nova
ocorrência (total da rodada: cerca de 155 das 600 buscas permitidas); o título de uma reclamação de consumidor entrou
no repositório e foi omitido depois — segue no histórico do git (fila do owner).

## 7. Arquivos para abrir, na ordem (soma = 20 min)

1. `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` — 1 min
2. `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` — 3 min
3. `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos e "O que as quatro
   restrições, juntas, deixam de pé") — 4 min
4. `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (seções 1, 8 e 9) — 5 min
5. `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html`, aberto no navegador, e as três páginas ligadas a ele —
   2 min
6. `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` (só "Em uma página") — 2 min
7. `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` (só "Em uma página") e
   `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_ampliacao.md` (só "Em uma página") — 3 min
