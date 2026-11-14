# Desenho do sistema, versão 0 — para aprovação do owner (item 6)

- **Estado:** primeira versão, escrita pela sessão principal em sexta, 13/11/2026, a partir das 21:54 (Brasília, lido
  de `date`). **Ainda não verificada.** Nada aqui foi publicado, comprado, cadastrado nem enviado.
- **O que é:** o desenho de um site que capta pedidos de controle de pragas na cidade de São Paulo e os leva a
  empresas licenciadas, dentro das quatro restrições lidas na fonte. É proposta para o owner aprovar, mudar ou
  recusar; **não é plano de execução**.
- **Em que se apoia** (cada escolha aponta para um destes arquivos):
  - **[R]** restrições, item 2, fechado: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`
  - **[A]** guia de busca orgânica, item 3, fechado: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`
  - **[B]** guia de Maps e perfil, item 3, fechado: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`
  - **[C]** guia de respostas de IA, item 3, fechado: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`
  - **[G]** parte do ChatGPT, item 3, fechado: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`
  - **[S]** mapa do mercado de busca, item 4, **em verificação**: `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md`
  - **[M]** modelos de negócio, item 5, **em verificação**: `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`
- **Marcas usadas:** "classe A/B" = a escolha tem fonte oficial ou estudo com dado no arquivo citado; **PREMISSA** =
  escolha sem evidência A ou B (minha, ou de fonte C ou D); **INFERÊNCIA** = decorre de fonte A, mas a aplicação ao
  caso é leitura minha; **DECISÃO DO OWNER** = não decido.
- **Natureza:** o que encosta em norma (RDC 622, CDC, LGPD, termos do WhatsApp e do Google) é **levantamento com
  fonte, não parecer jurídico**. Nome de trabalho do site neste arquivo: "EXEMPLO Guia".

## 1. O desenho em uma página

1. **O que o site é:** um guia que indica dedetizadoras licenciadas de São Paulo. Ele diz que é intermediário, nomeia
   em cada oferta a empresa que executa, com o número da licença e o órgão que a emitiu, e leva a pessoa a falar
   **direto com ela**. Não tem perfil de empresa no Google, não se apresenta como dedetizadora e não tem central de
   WhatsApp. [R, "O que as quatro restrições, juntas, deixam de pé", linhas 468–477]
2. **Onde está a diferença:** na amostra de 79 buscas, quase tudo o que aparece é site de dedetizadora com uma página
   por bairro, e só 12 dos 67 sites de serviço lidos mostram o número da licença [S, seções 4.2 e 7.3]. O site aposta
   no que falta: **licença conferida e visível, quem executa, como a pessoa confere, preço com origem declarada**.
   Se isso atrai busca e clique é **PREMISSA**: nada medido ainda.
3. **Poucas páginas, cada uma com algo que só ela diz.** Nada de centenas de páginas por bairro com o nome trocado:
   é o exemplo de página de entrada da política de spam do Google [A, seções 2.1 e 2.2]. Página de oferta só existe
   onde há licenciada nomeada.
4. **Captação:** na versão 0, só o **botão que abre o WhatsApp da licenciada** (o site registra o clique, não o
   contato). O formulário com consentimento fica desenhado, para uma fase posterior. [R, seção (d), "Os dois
   desenhos", linhas 432–446]
5. **Para quantas empresas vai o contato:** pelo botão, para **uma** — a que a pessoa escolheu. Pelo formulário, para a
   empresa da página e, se a pessoa marcar, para até mais duas, **cada uma nomeada**. [R, seção (c), "Vereditos",
   linhas 358–364]
6. **Medição:** posição e clique pelo Search Console (conta do owner); lead pelo registro de cliques no botão; lead
   vendido pela conferência mensal com a licenciada. **Sem rastreador automático de posição.** [A, seção 8]
7. **Fases:** cada fase prova uma coisa antes de gastar com a seguinte; a primeira despesa só vem depois de uma
   licenciada aceitar ser nomeada (seção 8).
8. **O que derruba tudo** está na seção 9, restrição por restrição.

## 2. O que o site é e o que não é

| Escolha | Base | Marca |
|---|---|---|
| O site se declara intermediário em todas as páginas: "indica empresas licenciadas; não é dedetizadora; não executa o serviço; contrato, nota fiscal e comprovante são da empresa" | [R], seção (b), "Conclusão para o site", item (iii), linhas 246–251 (o próprio item 2 marca como inferência do CDC, art. 37, e da RDC 622, arts. 5º e 21); [A], seção 3, "Transparência de um intermediário" | INFERÊNCIA |
| Não usa "nossa equipe", "nossos técnicos", "nossa licença" | [R], linhas 250–251 | escolha de desenho |
| Não tem perfil de empresa no Google, em formato nenhum | [R], quadro de vereditos, linha 25 (vedado) | classe A |
| Não marca a si mesmo como negócio local nos dados estruturados; usa `Organization` | [A], seção 5 (linhas de `Organization` e `LocalBusiness`) | classe A (o tipo) + INFERÊNCIA (não usar `LocalBusiness`) |
| Não tem número de WhatsApp que conversa, faz triagem e repassa | [R], quadro, linhas 36–37 (vedado pela API; não conclusivo pelo aplicativo) | classe A |
| Não pede, não compra e não exibe avaliação copiada de outro site; não mostra estrelas | [R], quadro, linha 29; [A], seção 5 (estrelas e origem das avaliações) | classe A |
| Não compra link nem menção; link para parceira que paga leva `rel="sponsored"` | [A], seção 2.1; [C], seção 7.2 | classe A |
| Página "quem somos": quem responde pelo site, o que o site é, como as licenciadas entram, como o site ganha dinheiro, como pedir a exclusão de dados | [A], seção 3 ("quem, como e por quê"); [C], seção 7.1; [G], seção 9, linha 10 | classe A para a recomendação do Google; como fator de citação por IA é PREMISSA |

## 3. Arquitetura do site

### 3.1 Tipos de página

| Tipo | Para que serve | Oferece o serviço? | Quantas na versão 0 |
|---|---|---|---|
| T1 Início | Dizer o que o site é; levar a praga, região e "como conferir a licença" | Não | 1 |
| T2 Guia de praga | Responder a dúvida (como identificar, o que o serviço envolve, o que perguntar à empresa, o que a norma exige, com fonte). Leva às páginas T3 | Não: é conteúdo | 6 (baratas, ratos, cupim, escorpião, percevejo, pombos) |
| T3 Praga × região | Página de oferta: quais licenciadas **nomeadas** atendem aquela praga naquela região, com licença, área atendida, preço informado por elas e botão | **Sim**, em nome da licenciada | só onde houver licenciada; meta inicial: 1 a 5 |
| T4 Região | Lista as licenciadas da região e leva às T3 e às páginas de bairro, se existirem | Sim, em nome das licenciadas | até 5 (as cinco regiões), só onde houver licenciada |
| T5 Bairro | **Só existe** se tiver algo próprio (ver 3.3) | Sim | 0 na versão 0 |
| T6 Público (condomínio; restaurante) | O que muda para quem contrata como empresa; licenciadas que atendem esse público | Sim, se houver licenciada | 2 |
| T7 Ficha da licenciada | Identificação, licença, órgão emissor, área atendida, serviços, como conferir; o botão | Sim | uma por licenciada |
| T8 Como conferir a licença | Passo a passo na consulta pública | Não | 1 |
| T9 Preços | Faixas **informadas pelas licenciadas do site**, com data; nada de tabela copiada | Não | 1 |
| T10 Quem somos · Como funciona | Seção 2 | Não | 2 |
| T11 Política de privacidade · Excluir meus dados | Seção 5 | Não | 2 |
| T12 Para dedetizadoras | Como uma licenciada entra, o que é exigido dela, como é cobrada | Não | 1 |

Total da versão 0: cerca de 20 a 25 páginas. **O número é PREMISSA:** não há, em fonte A ou B, quantidade de páginas
que um site novo sustenta [A, seção 2.2, "dois limites honestos"].

### 3.2 Por que essa forma, e não "uma página por bairro"

| Escolha | Base | Marca |
|---|---|---|
| Começar por praga e por região, não por bairro | A política de spam dá como exemplo de página de entrada páginas por região que afunilam o usuário [A, seção 2.1]; a tabela de sinais de página legítima [A, seção 2.2, linhas 187–194] é inferência do guia | classe A (texto da política) + INFERÊNCIA (aplicação) |
| Não copiar o formato dos concorrentes, embora ele esteja ranqueando | Na amostra, 79% a 87% dos resultados das buscas com bairro são páginas internas por local, e a leitura dos sites achou texto de molde com o nome trocado [S, seções 4.2 e 8]. O desenho não pode depender de prática que a política lista como spam (regra do item 6) | observação da amostra (não verificada) + regra da rodada |
| O conteúdo próprio de cada página de oferta é a **licença conferida** de quem atende ali | Só 12 de 67 sites lidos mostram o número [S, seção 7.3]; a RDC 622, art. 22, pede o número em toda propaganda de empresa especializada [R, linhas 186–187] | classe A (a norma) + observação da amostra; que isso renda posição é PREMISSA |
| Páginas de dúvida e de comparação valem mais para o intermediário do que "dedetizadora perto de mim" | [A], seção 7 (fecho: hipótese apoiada em duas fontes B de fora do Brasil) | PREMISSA |
| Página de público (condomínio, restaurante) em vez de bairro para quem contrata como empresa | Nas buscas de empresa × residência, 68% dos resultados são páginas de serviço ou de segmento e 1% é página por local [S, seção 4.2] | observação da amostra |
| Uma página trata de uma busca e de suas variações próximas ("dedetização" e "dedetizadora" na mesma página) | [A], seção 4 (duplicidade e página canônica); "uma palavra-chave, uma página" continua classe D | INFERÊNCIA |

### 3.3 Quando uma página de bairro pode existir (T5)

Só quando as três condições valem juntas; senão, o bairro é atendido pela página da região.

1. Há pelo menos uma licenciada nomeada que declara atender o bairro. [R, seção (b), veredito, linhas 257–258]
2. A página tem algo que só ela diz — por exemplo, preço informado pela licenciada para aquele bairro, ou dado
   público do bairro **com fonte**. [A, seção 2.2, linha 189]
3. Ela está na navegação (região → bairro) e não é só destino de busca. [A, seção 2.2, linhas 191–192]

### 3.4 O que toda página tem (técnica)

| Elemento | Como | Base | Marca |
|---|---|---|---|
| Título e título principal | Um `<title>` próprio e descritivo, coerente com o `<h1>` | [A], seção 4 (link de título) | classe A |
| Abertura da página | O `<h1>` e uma frase que diz o quê, onde e quem, no começo do corpo | [G], seção 9, linha 6 (uma fonte B; o estudo não testou efeito) | PREMISSA |
| Fatos em texto visível | Quem executa, número da licença, órgão, região atendida, preço e data: em HTML, não só em imagem nem só em dado estruturado | [C], seção 7.1; [G], seção 9, linha 7 | classe A para o Google (fontes de 2025); PREMISSA para o ChatGPT |
| Data de revisão visível | "Licença conferida em …", "Preço informado em …" | [C], seção 7.1 | classe A (orientação, sem dado) |
| Endereços | Legíveis, em minúsculas, sem acento, com hífen: `/pragas/baratas/`, `/zona-oeste/baratas/` | [A], seção 4 (endereços) | classe A |
| Navegação e links | Trilha (Início → Zona Oeste → Baratas); toda página ligada por pelo menos outra; texto do link descritivo; sem lista de bairros no rodapé | [A], seção 4 (links internos; texto âncora); seção 2.2 | classe A |
| Dados estruturados | `Organization` em Início e Quem somos; `BreadcrumbList`; só o que está visível. Sem `FAQPage` como aposta (o resultado rico acabou em 07/05/2026). `LocalBusiness` da licenciada na ficha dela: **só com autorização dela** e é ponto não conclusivo | [A], seção 5 | classe A; `LocalBusiness` de terceiro: não conclusivo |
| Sem dependência de script | Conteúdo e links no HTML que o servidor entrega; botão como `<a href>` | [A], seção 4 (links rastreáveis; JavaScript); [G], seção 9, linha 5 | classe A (Google); PREMISSA (ChatGPT) |
| Celular primeiro; sem janela que cubra a tela | Desenho responsivo; botão de WhatsApp pequeno e fixo, nunca intersticial | [A], seção 4 (indexação pelo celular; intersticiais) | classe A |
| `robots.txt` | Libera Googlebot, Bingbot e os robôs de busca e de visita da OpenAI (`OAI-SearchBot`, `ChatGPT-User`) e de outros motores; robôs de treino: liberados por padrão, **DECISÃO DO OWNER** | [G], seção 2 e seção 9, linhas 1 a 4; [C], seções 1.2 e 3 | classe A |
| Sem `nosnippet`; controle de IA do Search Console em "Incluir" | Para poder ser citado nos resumos de IA do Google | [C], seção 1.2 | classe A |
| `sitemap.xml` com data verdadeira; `rel="canonical"` para si | — | [A], seção 4 (sitemap; duplicidade) | classe A |
| Sem `llms.txt`, sem página "para IA", sem texto escondido | — | [C], seções 1.1 e 7.2 | classe A |
| Registro de acesso bruto do servidor | Para ver se os robôs de busca visitam | [G], seção 9, linha 15 | requisito de medição |

## 4. Onde cada página exibe o que a regra de propaganda exige (item 2(b))

Base de toda a seção: [R], seção (b), "Conclusão para o site", itens (i) a (iv), linhas 231–258.

### 4.1 Bloco "Quem executa" — obrigatório em toda página que oferece o serviço (T3, T4, T5, T6, T7)

Fica **acima do botão**, em texto, e traz, para cada licenciada da página:

| Campo | Exemplo no protótipo | Base | Marca |
|---|---|---|---|
| Nome da empresa como consta na licença | "EXEMPLO Controle de Pragas Ltda." | RDC 622, art. 22, caput [R, linhas 186–187] | classe A |
| Número da licença sanitária e órgão que a emitiu, como constam no documento dela | "Licença sanitária nº EXEMPLO-000000, emitida por EXEMPLO (órgão de vigilância sanitária)" | idem; qual número vale na capital (estadual ou municipal) é não conclusivo: exibe-se o que está na licença [R, linhas 209–213] | classe A |
| Razão social por extenso e endereço | "EXEMPLO — Rua EXEMPLO, 000, São Paulo" | indício da Portaria CVS 9/2000, não conferido na fonte [R, linhas 235–236] | por prudência |
| "Licença conferida pelo EXEMPLO Guia em dd/mm/aaaa" e link para a consulta pública | — | escolha de desenho; a consulta pública de licenças do estado apareceu numa busca da amostra [S, seção 4.4] — **como a consulta funciona não foi lido** | PREMISSA |
| Área atendida, como a licenciada declarou | "Atende: Pinheiros, Butantã, Lapa" | o mapa de uma parceira rende na região da base dela [B, seção 6] | INFERÊNCIA |
| Marca "Publicidade" quando a posição ou o destaque for pago | faixa "Publicidade — empresa parceira" | CDC, art. 36 [R, linhas 217–218 e 233–235] | classe A |

### 4.2 Faixa fixa em todas as páginas

"O EXEMPLO Guia indica empresas licenciadas. Não é dedetizadora e não executa o serviço: você contrata a empresa, e a
nota fiscal e o comprovante são dela." — [R, linhas 246–251] (INFERÊNCIA).

### 4.3 O que nenhuma página diz

| Não dizer | Base |
|---|---|
| Texto ou imagem de medo ("sua família em risco", foto de infestação para assustar) | RDC 622, art. 22, I; CDC, art. 37, § 2º [R, linhas 188–189 e 239] |
| "Aprovado", "recomendado por especialista", "publicidade aprovada pela Vigilância Sanitária", órgão público como selo | RDC 622, art. 22, II [R, linhas 190–192] |
| "Inócuo", "seguro", "atóxico", "produto natural", "sem risco para crianças e animais" | RDC 622, art. 22, III [R, linhas 193–194 e 241–242] |
| "24 horas", "garantia", "melhor preço" **sem prova guardada** dada pela licenciada | CDC, arts. 36, parágrafo único, e 38 [R, linhas 243–244] |
| "A melhor dedetizadora", "as melhores" sem critério exposto | [A], seção 3 (sistema de avaliações comparativas); [C], seção 7.2 |
| "Garantido pelo Google", "verificado pelo Google" | [B], seção 7 (inferência do guia) |
| Qualquer promessa de posição a uma licenciada | [B], seção 10.2 |

Páginas T2 (guia de praga) não oferecem o serviço em nome próprio; quando falam de risco à saúde, de produto ou de
segurança, cada afirmação tem fonte oficial [A, seção 3, "Dedetização é YMYL?" — inferência do guia].

### 4.4 Onde a norma é silente e o que o desenho faz

Página genérica de oferta sem empresa nomeada é **não conclusivo** e é o ponto de maior risco [R, quadro, linha 31;
linhas 253–262]. **O desenho não tem essa página:** região sem licenciada não tem página de oferta; a busca daquela
região é atendida pelo guia de praga (T2), que só informa.

## 5. Captação e roteamento do contato

### 5.1 Via A — botão que abre o WhatsApp da licenciada (versão 0)

| Passo | O que acontece | Base | Marca |
|---|---|---|---|
| 1 | A pessoa vê o bloco "Quem executa" e o botão "Falar com a EXEMPLO no WhatsApp" | seção 4.1 | — |
| 2 | Ao lado do botão: "Você vai abrir uma conversa no WhatsApp da EXEMPLO, que é quem atende. O EXEMPLO Guia não recebe o seu número nem a conversa; registra só que o botão foi tocado (data, página e empresa)." | [R], seção (d), Desenho B, linhas 438–441 | classe A (o link é recurso oficial) |
| 3 | O botão é um link para o número **da licenciada**, com mensagem pronta: "Olá! Vim pelo EXEMPLO Guia (código ZO-BAR). Quero um orçamento de dedetização de baratas em Pinheiros." | mensagem pré-preenchida do link oficial [R, linha 439, leitura só do subagente] | classe A |
| 4 | O site registra o clique: data e hora, página, empresa, código. **Nenhum dado da pessoa** | "o site só registra o clique, não o telefone nem a conversa" [R, linhas 440–441] | classe A |
| 5 | A conversa, o orçamento, o contrato e a nota são entre a pessoa e a licenciada | [R], linhas 246–251 | INFERÊNCIA |

- **Para quantas empresas vai o contato:** uma — a do botão que a pessoa tocou. Página com duas ou três licenciadas
  tem um botão por empresa.
- **Como a pessoa pede a exclusão:** o site não tem dado dela para excluir. A página diz isso e informa que o pedido
  vai à empresa com quem ela conversou, com o canal dessa empresa (o que a licenciada informar).
- **O código na mensagem** serve para a licenciada reconhecer de onde veio o contato (seção 6). A pessoa pode apagá-lo;
  por isso o clique é o que se conta, e a conferência com a licenciada é por amostra. PREMISSA: que as licenciadas
  aceitem conferir.
- **Como o clique é registrado sem script:** o botão aponta para um endereço do próprio site que anota o clique e
  redireciona para o link oficial do WhatsApp. É decisão de implementação; no protótipo o botão é um link de EXEMPLO
  que não leva a lugar nenhum. O registro de acesso do servidor guarda endereço IP, que pode ser dado pessoal: guardar
  pelo menor tempo possível e não ligar o IP ao clique. **O tratamento de IP em registro de servidor não foi levantado
  no item 2** — PREMISSA de prudência.

### 5.2 Via B — formulário com consentimento (desenhada; entra só em fase posterior)

Base: [R], seção (c), "Conclusão operacional", linhas 346–356, e seção (d), "Variante que não passa pelo WhatsApp do
site", linhas 442–446 (o item 2 marca a variante como **inferência**).

**Campos** (só o mínimo; nenhum campo de texto livre; nada de saúde — [R], linhas 342–344): como quer ser chamado;
telefone com WhatsApp; bairro (lista); praga (lista); tipo de imóvel (lista).

**Texto do formulário (EXEMPLO; os colchetes são preenchidos com dados reais):**

> **Pedir orçamento à [NOME DA LICENCIADA]**
>
> O EXEMPLO Guia é um site que indica dedetizadoras licenciadas. Não é dedetizadora, não executa o serviço e não cobra
> nada de você. Responsável pelo site: [razão social e CNPJ do responsável]. Contato sobre os seus dados: [e-mail].
>
> ☐ **Autorizo o EXEMPLO Guia a enviar meu nome, meu telefone, meu bairro, o tipo de praga e o tipo de imóvel à
> [NOME DA LICENCIADA], licença sanitária nº [NÚMERO], emitida por [ÓRGÃO], só para que ela me mande um orçamento de
> controle de pragas por WhatsApp ou por ligação.**
>
> ☐ Autorizo também o envio dos mesmos dados, para o mesmo fim, à [SEGUNDA LICENCIADA], licença nº [NÚMERO].
> *(caixa opcional; no máximo duas empresas a mais, cada uma com a sua caixa)*
>
> Você pode não autorizar: nesse caso nada é enviado, e você pode falar direto com a empresa pelo botão do WhatsApp.
> Seus dados não vão para nenhuma outra empresa, não são repassados de novo e não são usados para propaganda.
>
> Para retirar a autorização ou apagar os seus dados, a qualquer momento e de graça: página "Excluir meus dados" ou
> [e-mail]. Quando você pedir, apagamos o seu pedido e avisamos na hora cada empresa que o recebeu, para que faça o
> mesmo. Guardamos só o registro de que a autorização foi dada e de que foi retirada.
>
> Política de privacidade: [link].

**De onde vem cada parte do texto:**

| Parte | Base (LGPD, pelas linhas de [R]) |
|---|---|
| Quem é o site e como falar com ele | art. 9º, III e IV (linhas 349–350, leitura do subagente) |
| Finalidade determinada: receber orçamento | art. 5º, XII; art. 8º, § 4º (linhas 296–297 e 305) |
| Autorização do repasse **separada, destacada e não pré-marcada** | art. 7º, § 5º; art. 8º, § 1º (linhas 298–302); caixa pré-marcada: não conclusivo, por prudência não usar (linhas 363–364) |
| Empresa nomeada, com a licença | art. 9º, V (linhas 350–351); o opt-in do WhatsApp tem de nomear quem vai falar (linha 398) |
| Quais dados vão | art. 6º, III (linha 352) |
| Pode recusar, e o que acontece | art. 18, VIII (linha 352) |
| Como revogar e excluir, de graça | art. 8º, § 5º; art. 18, VI (linhas 306–307 e 324–325) |
| Aviso às empresas na exclusão | art. 18, § 6º (linhas 328–331) |
| Sem repasse posterior nem outro uso | inferência do art. 7º, § 5º, e do art. 6º, I (linhas 360–361) |

- **Para quantas empresas vai o contato:** uma por padrão (a da página); **no máximo três**, e só as que a pessoa
  marcar, cada uma nomeada. A lei não fixa número máximo [R, linha 368]; as plataformas brasileiras lidas repassam o
  mesmo pedido a até 4 ou 6 prestadores [M, seção 6]. **Três é PREMISSA de prudência**, não exigência.
- **Quem chama a pessoa:** a licenciada, do WhatsApp **dela**; o site não conversa. [R, linhas 442–446]
- **O que o site guarda como prova:** a versão do texto exibido, data e hora, o que a pessoa marcou e a que empresas o
  pedido foi, com data [R, linhas 353–355]. Por quanto tempo: **não conclusivo** [R, linha 355].
- **Como a pessoa pede a exclusão:** página "Excluir meus dados" (informa o telefone usado no pedido) ou e-mail. O
  site apaga o pedido, avisa de imediato cada empresa que o recebeu e anota a data do aviso. Prazo de resposta ao
  titular: a autoridade ainda não fixou [R, linhas 332–334]; o desenho adota **até 5 dias úteis — PREMISSA**.
- **Por que não na versão 0:** o formulário torna o site controlador de dados pessoais, com todas as obrigações da
  seção (c), antes de se saber se alguém clica. O botão prova a demanda sem tratar dado de contato.

### 5.3 O que fica fora do roteamento

| Fora | Base |
|---|---|
| Número de WhatsApp do site que conversa e repassa | [R], quadro, linhas 36–37; linhas 448–451 |
| Enviar o mesmo pedido a empresas que a pessoa não marcou, ou vender depois a outras | [R], linhas 358–368 |
| Guardar a conversa, pedir endereço completo, CPF ou qualquer dado de saúde | [R], linhas 342–344 e 352 |
| Mensagem de marketing depois do pedido | outra finalidade, outra autorização [R, linha 356] |
| Número de telefone do site que encaminha a ligação e grava a chamada | não levantado no item 2 nem no item 5 [M, seção 4.2, riscos] — fica fora até ser levantado |

## 6. Como medir

| O que | Como | Quem vê | Automatizável? | Base |
|---|---|---|---|---|
| Posição média, impressões e cliques por página e por busca | Relatório de desempenho do Search Console | só o owner (conta dele) | exportar: sim; **consultar o Google por robô: não** | [A], seção 8 |
| Presença em resumo de IA do Google | Relatório de IA generativa do Search Console (só impressões) | só o owner | exportar: sim | [C], seções 1.3 e 7.3 |
| Posição "na tela", com mapa e anúncios | Conferência manual, por amostra, anotando termo, hora e local (como no item 4) | owner ou sessão, nas regras da rodada | **não**: consulta automática contraria a política de spam do Google | [A], seção 8, linha de tráfego gerado por máquina; [S], seção 2 |
| Visitas dos robôs de busca (Google, Bing, OpenAI) | Registro de acesso bruto do servidor | owner | sim | [G], seção 9, linha 15 |
| Presença no ChatGPT | Roteiro de 30 perguntas, mensal, com repetições obrigatórias | owner (conta dele) | não (manual, por desenho) | `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`, seção 4 |
| Lead (clique no botão) | Registro do próprio site: data, página, empresa, código | owner | sim | seção 5.1; [R], linhas 440–441 |
| Lead (pedido por formulário), quando existir | Registro do pedido com a prova de consentimento | owner | sim | seção 5.2 |
| Lead válido e lead vendido | Conferência mensal com a licenciada: quantos contatos com o código chegaram, quantos viraram orçamento e serviço | owner e licenciada | não (depende dela) | [M], seções 4.0.1 e 4.2 (as plataformas tratam lead inválido por regra escrita) — PREMISSA: que ela informe |
| Receita por página | Lead vendido × preço combinado | owner | sim, depois da conferência | [M], seção 4.2 |

- **Comparar períodos iguais** (28 dias contra 28 dias) e esperar o fim de atualização central do Google antes de
  concluir [A, seção 8].
- **O modelo da planilha** (posição, clique, lead, lead vendido, com a definição de cada coluna) é a tarefa 5 da fila
  de reserva; não está neste arquivo.
- **Não medir:** "posição no mapa" de uma parceira por grade ou rastreador [B, seção 9]; nota de "autoridade" de
  ferramenta [A, seção 8].

## 7. O que é automatizável e o que não é

| Tarefa | Automatizar? | Por quê |
|---|---|---|
| Montar as páginas T3 a T7 a partir de uma planilha de licenciadas (nome, licença, órgão, área, preço informado, data da conferência) | Sim | O dado é próprio e conferido; o texto fixo é pouco. Gerar página **sem** dado próprio é o que a política chama de conteúdo em escala [A, seção 2.1] |
| `sitemap.xml`, trilha, dados estruturados, títulos e descrições a partir dos mesmos dados | Sim | [A], seção 4 (descrição gerada por programa é aceita se for específica) |
| Aviso de licença perto de vencer e de página sem conferência há mais de N dias | Sim | Mantém verdadeiro o que a página afirma (CDC, art. 38 [R, linhas 223–224]) |
| Relatório mensal: cliques por página e por empresa, a partir do registro do site | Sim | seção 6 |
| Rascunho de texto de guia de praga com IA | Só como rascunho; toda página revisada por pessoa, e nenhuma licença, preço ou norma sem fonte | [A], seção 3 (IA generativa) |
| Conferir a licença na consulta pública | **Não** nesta versão: é consulta manual (o funcionamento da consulta não foi lido) | PREMISSA |
| Consultar o Google para saber a posição | **Nunca** por robô | [A], seção 8 |
| Pedir, premiar ou escrever avaliação; responder avaliação pela licenciada sem aprovação dela | **Nunca** | [R], quadro, linha 29; [B], seção 3.1 |
| Entrar em contato com licenciadas ou com consumidores | **Não automatizar**; contato com empresa é ação do owner | regra do projeto |
| Publicar dezenas de páginas de uma vez | Não | [A], seção 2.2 (o ritmo em si não está em documento do Google: PREMISSA) |

## 8. Fases — o que cada uma prova antes de gastar dinheiro

Valores em reais de domínio, hospedagem e consulta jurídica **não foram levantados nesta rodada**; por isso as fases
dizem "despesa", sem número.

| Fase | O que se faz | Quem faz | O que prova | Despesa | Não passa de fase se… |
|---|---|---|---|---|---|
| 0 — estudo e protótipo (esta rodada) | Restrições, guias, mapa de busca, modelos, este desenho, protótipo local | sessão | Que existe um desenho dentro das regras | nenhuma | o owner recusar o desenho |
| 1 — validar sem site | (a) owner confere a política do empregador sobre atividade paralela; (b) advogado olha os pontos não conclusivos do item 2 e os textos das seções 4 e 5; (c) owner conversa com 3 a 5 licenciadas: aceitam ser nomeadas? pagariam? como? (d) owner roda o roteiro do ChatGPT e mede o volume de busca no Planejador de palavras-chave | owner | Que há ao menos **uma** licenciada disposta a ser nomeada, e que nada no jurídico nem no emprego impede | consulta jurídica | nenhuma licenciada aceitar; parecer contrário; empregador vedar |
| 2 — site mínimo no ar | Cerca de 20 páginas (seção 3.1), com 1 a 3 licenciadas nomeadas **sem cobrança**; Search Console e sitemap | owner publica (comprar domínio e publicar são atos dele) | Que as páginas são indexadas, recebem impressões e visitas dos robôs de busca | domínio e hospedagem | em cerca de 3 meses não houver impressão nenhuma (prazo PREMISSA: o Google não dá prazo [A, seção 9]) |
| 3 — piloto de contatos | Botão da Via A; registro de cliques; conferência mensal com a licenciada | owner e licenciada | Quantos cliques viram conversa, orçamento e serviço — a taxa de fechamento que hoje ninguém tem [M, seção 7] | nenhuma nova | os cliques forem poucos demais para medir, ou a licenciada não conferir |
| 4 — cobrança | Preço por contato válido ou mensalidade por região, de preferência pré-paga; regra escrita de contato inválido; contrato | owner | Que a licenciada paga pelo que recebeu | contrato (levantamento na fila de reserva 4) | ela não pagar o que o piloto mostrou valer |
| 5 — ampliar | Mais regiões e, só com as condições de 3.3, bairros; formulário da Via B; gestão do perfil da licenciada como segundo serviço | owner | Que o modelo se repete com outra licenciada | horas | a segunda licenciada não repetir o resultado da primeira |

- **Modelo de cobrança previsto para a fase 4:** uma licenciada por região e por praga, nomeada na página, com
  pagamento antecipado — é o caso mais simples perante as quatro restrições [M, seção 1, item 9; seções 4.3 e 4.6].
  O **valor** não tem fonte: o "R$ 20 a 60 por lead" da pesquisa antiga não se confirma nem se derruba [M, seção 7].
  DECISÃO DO OWNER, depois do piloto.
- **Prazo:** semanas para indexar; de 6 a 12 meses para saber se há tráfego — PREMISSA do guia [A, seção 9], sem
  garantia.
- **Gestão do perfil da licenciada** (fase 5): é o único caminho do projeto até o bloco de mapa, que apareceu em 68
  das 79 buscas da amostra [S, seção 3]; o roteiro e os limites estão em [B], seção 10. O perfil e as avaliações são
  dela e ela pode levá-los embora [B, "O que não cabe para um gerador de leads", fecho].

## 9. O que tornaria isto inviável

### 9.1 As quatro restrições, uma a uma

| Restrição | O desenho depende de quê | O que o tornaria inviável | Como se saberia |
|---|---|---|---|
| **Perfil de empresa do Google** [R, seção (a)] | De **não** ter perfil. O site vive do orgânico e de citação por IA | Se o orgânico, sem mapa, não trouxer visita: o bloco de mapa e os anúncios ocupam a página (68 e 60 das 79 buscas) e o Google não garante posição a ninguém. Ou se o Google tratar o site como página de entrada ou conteúdo em escala | Search Console na fase 2: impressões, cliques, ação manual |
| **Propaganda de controle de pragas** [R, seção (b)] | De toda oferta nomear a licenciada e a licença | Se **nenhuma licenciada aceitar ser nomeada** num site de terceiro; se a vigilância sanitária entender que o site "concorre" para infração da empresa e autuá-lo (norma silente); se a exigência estadual de razão social e endereço, ou a regra de qual número vale na capital, pedir algo que a parceira não possa exibir | Conversas da fase 1; advogado; leitura dos PDFs que faltam |
| **LGPD** [R, seção (c)] | Na Via A, de **não** tratar dado de contato; na Via B, do consentimento específico | Se a autoridade vier a regular venda de contatos de forma mais dura que a lei (o tema está na agenda dela); se a licenciada que recebe o pedido o usar para outra coisa (os controladores respondem solidariamente, art. 42); se o custo de cumprir a Via B não se pagar | Acompanhar a agenda da autoridade; contrato com a licenciada |
| **WhatsApp Business** [R, seção (d)] | Do link oficial que abre a conversa com a licenciada | Se a Meta mudar os termos e restringir o uso do link por terceiros; se a licenciada perder a conta por violar a política; e, comercialmente, porque **o site só prova o clique**: se a licenciada disser que a pessoa não escreveu, não há como provar | Reler os termos a cada mudança (a última foi em 23/09/2026); conferência do piloto |

### 9.2 Fora das quatro restrições

| Risco | Por que pode derrubar | Base |
|---|---|---|
| As licenciadas não pagam, ou pagam menos do que custa manter o site | Não há fonte brasileira de preço de lead exclusivo, de taxa de fechamento nem de disposição de pagar | [M], seções 7 e 8 ("não sei") |
| O orgânico já é dos sites das dedetizadoras | 10 domínios têm 39% dos resultados; 13 domínios aparecem em 5 ou mais das 20 buscas por bairro | [S], seções 4.1 e 4.2 |
| O resumo de IA responde antes do clique | Apareceu em 73 das 79 buscas; o efeito sobre o clique é disputado | [S], seção 3; [C], "O que é disputado" |
| Dependência de uma licenciada | Se ela sai, a página de oferta deixa de existir (seção 4.4) | [M], seção 4.3, riscos |
| Dependência de um canal | Uma atualização do Google muda a posição sem aviso; havia uma em curso na coleta | [A], seção 1.3 |
| Responsabilidade perante o consumidor por serviço mal feito | Se o intermediário responde junto com a executora é leitura de tribunal, não levantada | [R], linhas 225–229 |
| Política do empregador do owner | Só o owner confere | item 8 da rodada (pergunta fixa) |

### 9.3 O que este desenho não usa, por regra

Perfil de empresa fora da política; endereço fictício ou de fachada; avaliação fabricada, comprada ou incentivada;
link comprado; página de oferta sem empresa nomeada; central de WhatsApp que repassa; rastreador automático de
posição; contato com empresa ou pessoa feito pela sessão.

## 10. Premissas sem evidência A ou B (lista única)

1. Que mostrar a licença conferida e o preço com origem atrai busca, clique ou citação por IA.
2. Que páginas de dúvida e de comparação rendem mais ao intermediário do que as de "perto de mim".
3. Cerca de 20 páginas na versão 0; 6 pragas; até 5 regiões.
4. No máximo três empresas por pedido no formulário; resposta a pedido de exclusão em até 5 dias úteis.
5. Que a licenciada aceite conferir, todo mês, os contatos pelo código.
6. Cerca de 3 meses para ver impressões; de 6 a 12 meses para saber se há tráfego.
7. Que abrir a página com o título e uma frase de "o quê, onde, quem" ajude a ser citado pelo ChatGPT (uma fonte B,
   que não testou o efeito).
8. Liberar os robôs de treino de modelos.
9. Guardar o registro de acesso do servidor pelo menor tempo possível e não ligar endereço IP a clique.
10. Que a consulta pública de licenças permita conferir, à mão, o número de cada licenciada.

## 11. O que o item 4 e o item 5 ainda podem mudar aqui

Este desenho cita números do mapa de busca [S] e dos modelos de negócio [M], que estavam **em verificação** quando ele
foi escrito. Se a verificação mudar algum, as linhas afetadas são: seção 1, itens 2 e 5; seção 3.2; seção 5.2
(quantas empresas); seção 8 (modelo de cobrança); seção 9. As 10 buscas de confiança, preço e informação (grupo H),
que testariam a premissa 1, não tinham sido feitas.
