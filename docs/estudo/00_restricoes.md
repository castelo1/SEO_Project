# Restrições que decidem o modelo — lidas na fonte atual (item 2)

- **Leitura:** sexta, 13/11/2026, das 19:31 às 19:57 (Brasília, lido de `date`).
- **Natureza:** levantamento com fonte, **não é parecer jurídico**. Onde a norma não trata de intermediário está
  escrito "silente"; a aplicação ao caso concreto é de advogado.
- **Classe de evidência:** tudo o que está entre aspas é **classe A** (política da plataforma ou norma, lida na página
  oficial). **Quem ganha com a afirmação:** em (a) e (d), o dono da plataforma (Google, Meta), que define e aplica a
  regra e não vende método de SEO; em (b) e (c), o Estado. Nenhuma fonte de vendedor, agência ou blog foi usada.
- **Como foi conferido (duas leituras independentes):**
  1. quatro subagentes leram as fontes pela ferramenta de leitura de página (que parafraseia e corta em trechos
     curtos) e gravaram os anexos em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes_anexos/`
     (`00a_perfil_google.md`, `00b_propaganda.md`, `00c_lgpd.md`, `00d_whatsapp.md`), com cada citação marcada;
  2. a sessão principal reabriu no navegador pessoal as páginas que decidem e procurou cada trecho abaixo **no texto
     bruto da página** (busca literal). O que passou nessa segunda conferência leva **[N]**. O que só tem a leitura do
     subagente leva **[S]**.
- **Datas das fontes:** as páginas de ajuda do Google não exibem data (só "©2026"). Política de Mensagens do
  WhatsApp e Termos da Meta: atualizados em 23/09/2026. RDC 622: DOU de 16/03/2022, marcada "Vigente" na base da
  Anvisa em 13/11/2026. CDC e LGPD: texto compilado do Planalto em 13/11/2026.

## Quadro de vereditos

| Restrição | Pergunta | Veredito para um gerador de leads |
|---|---|---|
| (a) Perfil de empresa do Google | Ter perfil próprio (em qualquer formato, inclusive endereço oculto) | **Vedado** |
| (a) | Endereço de fachada: caixa postal, escritório virtual, coworking sem equipe | **Vedado** |
| (a) | Perfil da licenciada com o site ou o telefone do intermediário | **Vedado** |
| (a) | Administrar o perfil da licenciada, com autorização expressa, ela como proprietária, com o telefone e o site **dela** | **Permitido com condição** |
| (a) | Avaliação comprada, incentivada ou escrita por quem tem vínculo | **Vedado** |
| (b) Propaganda | Site de terceiro divulgar o serviço de dedetizadoras licenciadas | **Permitido com condição** (identificar a executora e a licença; sem termos vedados; site declarado intermediário) |
| (b) | Página que oferece o serviço **sem** nomear a empresa que executa | **Não conclusivo** (norma silente; é o ponto de maior risco) |
| (c) LGPD | Captar o contato e repassá-lo a **uma** empresa | **Permitido com condição** (consentimento específico e destacado para o repasse) |
| (c) | Repassar a **várias** empresas | **Permitido com condição** (as mesmas, mais: dizer a quantas e a quais; registrar quem recebeu; avisar todas na exclusão) |
| (c) | Vender o contato só com base em legítimo interesse, sem consentimento | **Não conclusivo** (guia da ANPD não lido) |
| (d) WhatsApp | Número do site na API (Plataforma) faz a triagem e **repassa** o contato | **Vedado** pela letra dos termos da Meta |
| (d) | O mesmo pelo aplicativo gratuito WhatsApp Business | **Não conclusivo** (termos silentes sobre repasse) |
| (d) | Botão do site abre direto o WhatsApp **da licenciada** (link oficial) | **Permitido com condição** |

---

## (a) Perfil de empresa do Google

**Fontes primárias (todas em `support.google.com`, lidas em 13/11/2026):**
`/business/answer/13763036` (elegibilidade e propriedade) · `/business/answer/13762416` (visão geral das políticas) ·
`/business/answer/3038177` (diretrizes para representar a empresa) · `/business/answer/9157481` (área de cobertura) ·
`/business/answer/7353941` (política para terceiros) · `/business/answer/3403100` (proprietários e administradores) ·
`/business/answer/4569145` (perfis suspensos ou desativados) · `/business/answer/14114287` (restrições por violação) ·
`/contributionpolicy/answer/7400114` (conteúdo proibido de usuários do Maps). Versão de referência: inglês
(`?hl=en`); a versão em português avisa que pode ter tradução automática.

### 1. Gerador de leads pode ter perfil? — **Vedado**

- "To qualify for a Business Profile, a business must make in-person contact with customers during its stated
  hours." — 13763036 **[N]**
- Lista "Ineligible businesses" da mesma página: "Lead generation agents or companies." e "Brands, organizations,
  artists, and other online-only businesses." **[N]** (os dois itens também constam de 13762416 **[N]**)
- "Sales associates or lead generation agents for corporations aren't individual practitioners and aren't eligible
  for a Business Profile." — 3038177 **[N]**

O site do projeto capta contatos, não atende ninguém presencialmente e só existe on-line: cai em dois itens da lista
de inelegíveis e não cumpre a condição de entrada.

### 2. O que conta como endereço e atendimento

- "P.O. boxes or mailboxes located at remote locations aren't acceptable." — 3038177 **[N]**
- Endereço alugado sem operação no local, "also known as a virtual office, that location isn't eligible for a
  Business Profile". — 3038177 **[N]**
- Coworking só se o escritório "maintains clear signage, receives customers at the location during business hours,
  and is staffed during business hours by your business staff". — 3038177 **[N]**
- Empresa que vai ao cliente (é o caso da dedetizadora): "If you're a service-area business, you should hide your
  business address from customers." — 3038177 **[N]**; um perfil para a base real, até 20 áreas de cobertura, a cerca
  de 2 horas de carro da base (9157481 **[S]**, resumido).
- Nome: "Your name should reflect your business's real-world name, as used consistently on your storefront, website,
  stationery, and as known to customers." — 3038177 **[N]** (praga, bairro ou "24 horas" que não façam parte do nome
  real são informação desnecessária).
- Telefone e site do perfil: "Do not provide phone numbers or URLs that redirect or "refer" users to landing pages or
  phone numbers other than those of the actual business, including pages created on social media sites." e "The
  phone number must be under the direct control of the business." — 3038177 **[N]**

**Vereditos:** endereço fictício, caixa postal, escritório virtual, coworking sem equipe: **vedado**. Perfil de
serviço local com endereço oculto para o gerador de leads: **vedado** (continua inelegível pelo ponto 1). Perfil de
serviço local da dedetizadora licenciada, na base real dela: **permitido com condição**. Telefone ou endereço de site
do intermediário no perfil: **vedado**.

### 3. O que acontece com perfil fora da regra

- "We may suspend or disable Business Profiles that don't follow our guidelines." — 4569145 **[N]**
- "If a merchant's account is restricted, all Business Profiles associated with that account will be suspended."
  (gatilho: "a pattern of violating Google Business Profile policies") — 13762416 **[N]**
- "Merchants that set their business address at a P.O. Box will have their profile suspended." — 13762416 **[N]**
- Recurso: "Appeals can only be submitted once." e "Do not create a new Business Profile for the same business." —
  4569145 **[N]**
- Avaliações: é engajamento falso a avaliação "paid for, directly or in kind"; é vedado oferecer incentivo "in
  exchange for posting any review or revision or removal of a negative review"; é vedado "selectively solicit
  positive reviews from customers"; conflito de interesses inclui "a contractual or consultory relationship". —
  7400114 **[N]**
- Sanção ao perfil por avaliação falsa: fica sem receber avaliações novas por um período, tem as existentes
  despublicadas por um período e exibe aviso público de que avaliações falsas foram removidas. — 14114287 **[N]**

Consequência que pesa no desenho: restrição da **conta** derruba todos os perfis ligados a ela, inclusive os de
parceiras que o projeto administrasse pela mesma conta.

### 4. Caminhos legítimos para o mapa

- "Only business owners or authorized representatives may verify and manage their business information on a Business
  Profile." e "Any individual or company that manages business information for a Business Profile that they don't
  own is considered an authorized representative." — 13763036 **[N]**
- "Never claim a Business Profile without express consent from the business owner." — 13763036 **[N]**; na política
  para terceiros, o consentimento pode ser escrito ou por ação positiva (marcar uma caixa) e "Verbal consent isn't
  sufficient." — 7353941 **[N]**
- "After a profile has been created for a client, make the business owner the owner of the profile, and make yourself
  the manager of the profile." e "all end customers must retain ownership or co-ownership of their Business Profile
  at all times." — 7353941 **[N]**
- Devolução do controle: "Within 7 business days of notice from an end customer" — 7353941 **[N]**
- "Website content must be owned and managed by the business owner." e o telefone e o site do perfil "should always
  be the single, authoritative phone number and website for the business and be verifiable by the business owner". —
  13763036 **[N]**
- Sanção ao terceiro: "We may suspend a Business Profile and/or the Google Account you use to manage the Business
  Profile if you commit a serious policy violation." — 7353941 **[N]**

**Caminhos que sobram:**
1. **Administrar o perfil da licenciada como representante autorizado** — permitido com condição: consentimento
   expresso (não verbal); ela é a proprietária e o projeto entra como administrador; telefone e site do perfil são os
   dela; devolução do acesso em até 7 dias úteis quando ela pedir; nenhuma promessa de posição.
2. **Orientar a licenciada** a enquadrar-se como empresa de serviço local (uma base, um perfil, endereço oculto, nome
   real) e a pedir avaliações verdadeiras, sem incentivo e sem selecionar só os satisfeitos.
3. **O site de leads fica fora do mapa** e compete no resultado orgânico. É o que resta por exclusão.

**Não é caminho:** perfil próprio do site; perfil em endereço de fachada; perfil da parceira com o site ou o
telefone do intermediário; perfil "alugado" cuja propriedade fica com o intermediário.

**O que isso corta do plano:** no mapa o projeto não constrói patrimônio próprio. O que ele pode vender ali é um
**serviço de gestão** do perfil da licenciada; o perfil, as avaliações e as ligações são dela e ela pode retomá-los.
A tática do artigo do owner "negócio local: ranquear o perfil, não o site"
(`/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md`, linha 2.12) só se aplica ao perfil
**da licenciada**.

**Não conclusivo em (a):** o que mudou nas regras em 2025–2026 (páginas sem data; arquivo histórico inacessível);
número de rastreamento de chamadas contratado pela própria licenciada (a palavra não aparece nas páginas); prazo do
recurso e duração das restrições.

### Pesquisa de 25/09 — continua valendo ou foi corrigida

`/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`:
- linhas 13 e 102 (gerador de leads inelegível; contato presencial; caixa postal não vale): **continuam valendo**;
  a lista de inelegíveis hoje está em 13763036 e 13762416, não em 3038177;
- linha 13 ("fica restrito a orgânico e anúncios"): **incompleta** — faltou o caminho de administrar o perfil da
  licenciada;
- linha 103 (endereço oculto para empresa de serviço local): **confirmada na fonte primária**; "principal causa de
  suspensão" é afirmação de agência, não conferível;
- linha 108 e, por extensão, linhas 42, 87 e 91 ("controlar o número de telefone"): **corrigidas** — no perfil da
  parceira, o número e o site têm de ser dela; o controle do número pelo intermediário só vale no **site**.

---

## (b) Propaganda de controle de pragas

**Fontes primárias (lidas em 13/11/2026):**
- RDC Anvisa nº 622, de 09/03/2022 (DOU 16/03/2022), base oficial da Anvisa, marcada "Vigente":
  https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&tipo=RDC&numeroAto=00000622&seqAto=000&valorAno=2022&orgao=RDC/DC/ANVISA/MS
- Código de Defesa do Consumidor, Lei 8.078/1990: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- Lei 6.437/1977 (infrações sanitárias): https://www.planalto.gov.br/ccivil_03/leis/l6437.htm
- Estado de São Paulo: Lei 10.083/1998 (Código Sanitário),
  https://www.al.sp.gov.br/repositorio/legislacao/lei/1998/lei-10083-23.09.1998.html; Portaria CVS 9/2000, lida em
  **cópia oficial hospedada pela Prefeitura de São Paulo** (arquivo .doc; o site do CVS devolveu erro 403)
- Município de São Paulo: Lei 13.725/2004 (Código Sanitário),
  https://legislacao.prefeitura.sp.gov.br/leis/lei-13725-de-09-de-janeiro-de-2004; Portaria SMS 266/2025,
  https://legislacao.prefeitura.sp.gov.br/portaria-secretaria-municipal-da-saude-sms-266-de-6-de-maio-de-2025

### O que a RDC 622 diz (texto que decide)

- A quem se dirige — art. 2º: "Esta Resolução se aplica às empresas especializadas" **[N]**. As palavras
  "intermediário", "anunciante" e "site" não aparecem na resolução **[S]**: sobre terceiro que só anuncia ou indica,
  **norma silente**.
- Art. 5º: a contratação "somente pode ser efetuada com empresa especializada" **[N]**.
- Art. 21: a nota fiscal "somente é valida se for emitida por pessoa jurídica de direito privado" **[N]**.
- **Art. 22, caput:** "toda e qualquer forma de propaganda de empresa especializada deve conter claramente a
  identificação dela nos órgãos licenciadores competentes, bem como o número de sua licença" **[N]**
- **Art. 22, I:** "não provocar temor, angústia ou utilizar expressões ou imagens sugerindo que a saúde das pessoas
  será ou poderá ser afetada por não usar produtos ou prestação de serviço" **[N]**
- **Art. 22, II:** não publicar mensagens como "Aprovado", "Recomendado por especialista", "Demonstrado em ensaios
  científicos", "Publicidade aprovada pela Vigilância Sanitária", "Ministério da Saúde" ou órgão congênere **[N]**
- **Art. 22, III:** não sugerir ausência de efeitos adversos nem usar "inócuo", "seguro", "atóxico" ou "produto
  natural" **[N]** (salvo expressão registrada na Anvisa **[S]**)
- Art. 23: o descumprimento é infração sanitária, com as penas da Lei 6.437/1977 **[S]**; essa lei imputa a infração
  "a quem lhe deu causa ou para ela concorreu" (art. 3º) **[S]**.

### Estado e município de São Paulo

- Portaria CVS 9/2000, item 10.4: as empresas mencionam em toda publicidade "o número da Licença de Funcionamento,
  concedida pelo órgão competente municipal ou estadual, sua razão social e endereço" **[S]** — pede **mais** que a
  RDC (razão social e endereço). Ressalvas: cópia oficial em terceiro; **vigência não confirmada** na fonte primária.
- Códigos sanitários do estado (art. 122, XV, e art. 111) e do município (art. 129, XV, e art. 117): propaganda
  enganosa de "produto ou serviço de saúde" é infração, e responde quem "lhe deu causa, concorreu para sua prática ou
  dela se beneficiou" **[S]**. Nenhum dos dois menciona controle de pragas; se dedetização é "serviço de saúde" para
  esse fim, **norma silente**.
- Portaria SMS 266/2025: não tem regra de propaganda **[S]**.
- Qual número a licenciada da capital recebe (cadastro estadual CEVS ou municipal CMVS): **não conclusivo** — o
  anexo vigente e a Portaria CVS 1/2024 (republicada pela última vez em 15/10/2026) só existem em PDF e não foram
  lidos. Não trava o desenho: o art. 22 pede o número da licença e a identificação no órgão, sem dizer a sigla;
  exibe-se o número **como consta na licença da parceira** e o nome do órgão emissor.

### Código de Defesa do Consumidor

- Art. 36: "A publicidade deve ser veiculada de tal forma que o consumidor, fácil e imediatamente, a identifique como
  tal." **[N]**; o parágrafo único manda guardar os dados que sustentam a mensagem **[S]**.
- Art. 37: "É proibida toda publicidade enganosa ou abusiva." **[N]**; é enganosa a informação falsa "ou, por
  qualquer outro modo, mesmo por omissão, capaz de induzir em erro o consumidor" **[N]**; é abusiva a que "explore o
  medo ou a superstição" **[N]**; "a publicidade é enganosa por omissão quando deixar de informar sobre dado
  essencial do produto ou serviço" **[N]**.
- Art. 38: "O ônus da prova da veracidade e correção da informação ou comunicação publicitária cabe a quem as
  patrocina." **[N]**
- Art. 7º, parágrafo único: "Tendo mais de um autor a ofensa, todos responderão solidariamente" **[N]**; art. 34: o
  fornecedor responde "pelos atos de seus prepostos ou representantes autônomos" **[N]**. O CDC não usa as palavras
  "intermediário" nem "cadeia de fornecimento": que o gerador de leads responda junto com a dedetizadora por um dano
  do serviço é leitura de tribunal, **não levantada aqui**.

### Conclusão para o site

**(i) Cada página que oferece o serviço exibe:** a razão social da empresa que executa; o número da licença
sanitária e o órgão que a emitiu, como constam no documento dela; o endereço dela (CVS 9/2000, por prudência); a
marca de publicidade onde a posição ou o destaque for pago (CDC, art. 36). CNPJ, validade da licença e responsável
técnico não são exigidos **na propaganda** pelas normas lidas — exibi-los é escolha de desenho.

**(ii) Não pode dizer:** texto ou imagem de medo; "aprovado", "recomendado por especialista", "aprovado pela
Vigilância Sanitária" ou órgão público como selo; "seguro", "atóxico", "inócuo", "produto natural", "sem risco para
crianças e animais"; qualquer afirmação sem prova guardada ("24 horas", "garantia", "melhor preço").

**(iii) Tem de ficar claro quem é o site:** não é dedetizadora, não tem licença e não executa; capta o pedido e o
encaminha a empresa licenciada; contrato, nota fiscal e comprovante de execução são da licenciada; nada de "nossa
equipe", "nossos técnicos", "nossa licença".

**(iv) Onde a norma é silente:** página genérica ("dedetização em Pinheiros — peça orçamento") sem empresa nomeada;
se o dono do site pode ser autuado como quem "concorreu" ou "se beneficiou"; quais são os "dados essenciais" do
art. 37, § 3º.

**Veredito: permitido com condição.** Um desenho em que **toda** página de oferta nomeia a licenciada que atende
aquela região cumpre as condições mesmo com os pontos não conclusivos em aberto.

**O que isso corta do plano:** páginas praga × bairro "anônimas", com cara de dedetizadora e botão de orçamento, são
o formato de maior risco. Ou a página nomeia a licenciada que atende, ou é página de conteúdo e comparação que
**não** oferece o serviço em nome próprio.

### Pesquisa de 25/09 — continua valendo ou foi corrigida

`/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md`:
- linha 44 (art. 22): **continua valendo**, com termos vedados a mais ("Recomendado por especialista", "Demonstrado
  em ensaios científicos", "Ministério da Saúde", "produto natural");
- linha 156: **corrigida em parte** — o art. 21 exige nota de pessoa jurídica; não diz "da pessoa jurídica que
  executa";
- linha 157 ("vale para o texto do site", confiança Alta): **texto confirmado, alcance rebaixado** — que o art. 22
  alcance o site de terceiro é interpretação (norma silente);
- linha 158 (comprovante é da licenciada): **continua valendo**;
- linha 159 (formato seguro): continua como leitura; as normas pedem licença, órgão, razão social e endereço — CNPJ
  não é exigido por elas;
- linha 163 (solidariedade "na cadeia"): **formulação corrigida** — "cadeia de fornecimento" não está no texto da lei;
- linha 188: **continua valendo**;
- linhas 14 e 82 (o estado licencia na capital) e linha 160 (terceirização entre licenciadas): **não deu para
  conferir** (PDF).

---

## (c) LGPD — captar o contato e repassá-lo

**Fontes primárias (lidas em 13/11/2026):** Lei 13.709/2018, texto compilado
(https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; última alteração exibida: Lei 15.352/2026,
que não mexe nos artigos usados aqui **[S]**); Resolução CD/ANPD nº 2/2022, texto compilado no site da ANPD
(https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022);
Agenda Regulatória da ANPD (https://www.gov.br/anpd/pt-br/assuntos/regulacao/agenda-regulatoria-1, tabela de
12/11/2026); glossário e perguntas frequentes da ANPD.

### Base legal e consentimento

- Consentimento (art. 5º, XII): "manifestação livre, informada e inequívoca pela qual o titular concorda com o
  tratamento de seus dados pessoais para uma finalidade determinada" **[N]**
- **Art. 7º, § 5º:** "O controlador que obteve o consentimento […] que necessitar comunicar ou compartilhar dados
  pessoais com outros controladores deverá obter consentimento específico do titular para esse fim" **[N]**
- Art. 8º, § 1º: por escrito, "deverá constar de cláusula destacada das demais cláusulas contratuais" **[N]**
- Art. 8º, § 2º: "Cabe ao controlador o ônus da prova de que o consentimento foi obtido em conformidade com o
  disposto nesta Lei" **[N]**
- Art. 8º, § 4º: "as autorizações genéricas para o tratamento de dados pessoais serão nulas" **[N]**
- Art. 8º, § 5º: "O consentimento pode ser revogado a qualquer momento mediante manifestação expressa do titular, por
  procedimento gratuito e facilitado" **[N]**
- Art. 9º, § 1º: consentimento nulo se a informação for enganosa ou não tiver sido apresentada antes, com clareza
  **[S]**; art. 6º, III: só o mínimo necessário **[S]**.
- ANPD: **não há** guia nem norma sobre consentimento, sobre venda de dados ou sobre "agregadores de dados"; os três
  temas estão na agenda como "em andamento", em elaboração interna **[S]**.

### Quem é controlador

- Controlador é quem toma "as decisões referentes ao tratamento" (art. 5º, VI) **[S]**: o site que capta é
  controlador; a dedetizadora que recebe também é (o próprio § 5º fala em "outros controladores").
- Art. 42, § 1º, II: os controladores diretamente envolvidos "respondem solidariamente" **[N]**, com direito de
  regresso (§ 4º) **[S]**.
- Se são controladores independentes ou conjuntos: **não conclusivo** (guia da ANPD em PDF, não lido).

### Direito de exclusão

- Art. 18, VI: "eliminação dos dados pessoais tratados com o consentimento do titular" **[N]**
- Art. 18, VII: "informação das entidades públicas e privadas com as quais o controlador realizou uso compartilhado
  de dados" **[N]**
- **Art. 18, § 6º:** o responsável informa "de maneira imediata, aos agentes de tratamento com os quais tenha
  realizado uso compartilhado de dados a correção, a eliminação, a anonimização ou o bloqueio dos dados, para que
  repitam idêntico procedimento" **[N]**
- Prazo geral de resposta ao titular: ainda **não fixado** em regulamento **[S]**; declaração completa de acesso em
  até 15 dias (art. 19, II) **[S]**.

### Agente pequeno e dado sensível

- Resolução CD/ANPD nº 2/2022: microempresa, empresa de pequeno porte e MEI não precisam indicar encarregado, mas
  têm de manter um canal de comunicação com o titular, registro simplificado das operações e segurança básica
  **[S]**; perdem o regime se o tratamento for de alto risco (larga escala somada a dado sensível, a decisão só
  automatizada ou a dado de idosos) **[S]**.
- Nome, telefone, bairro, tipo de praga e tipo de imóvel não são dado sensível. "Dado referente à saúde" é
  (art. 5º, II) **[S]**: alergia, asma, picada de escorpião. Consequência: não perguntar nada de saúde; evitar campo
  de texto livre.

### Conclusão operacional

O texto de consentimento precisa trazer: a finalidade (receber orçamento de dedetização); a autorização **separada e
destacada** para o repasse; quem é o site e como falar com ele; **para quais empresas** o contato vai (nomeadas, ou no
mínimo quantas e onde ver a lista — se "até N empresas" sem nome basta é **não conclusivo**); quais dados vão; que a
pessoa pode recusar; como revogar e pedir a exclusão, de graça. Guarda-se como prova: o texto exibido (versão), data
e hora, o que a pessoa marcou, e a que empresas o contato foi, com data. Na exclusão, avisa-se cada empresa que
recebeu. Contato futuro ou marketing é outra finalidade e pede outra autorização.

**Vereditos:** repassar a **uma** empresa — **permitido com condição**. Repassar a **várias** — **permitido com
condição**, com mais exigências (dizer a quantas e a quais; limitar ao necessário; registrar quem recebeu cada
contato; avisar todas na exclusão; sem revenda posterior). **Vedado** pela letra da lei: repassar sem informar;
repassar com autorização genérica ("aceito os termos"). **Não conclusivo:** vender só com legítimo interesse; apoiar
o repasse só no art. 7º, V; prazo de guarda da prova em anos; caixa pré-marcada (a lei não usa a expressão; por
prudência, não usar).

**O que isso corta do plano:** "lista de contatos como ativo" só existe para quem autorizou cada finalidade e
enquanto não revogar; vender o mesmo contato a muitas empresas, ou revendê-lo depois, fica fora.

### Pesquisa de 25/09 — continua valendo ou foi corrigida

`/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`, linha 167: **vale na direção, corrigida
no detalhe** — a lei pede consentimento "específico" e destacado (não "explícito"); a frase-modelo sozinha não
basta (faltam controlador, finalidade, revogação e registro de quem recebeu); faltava o dever de avisar as empresas
na exclusão. Linhas 91 e 165 ("lista com consentimento para contato futuro"): **valem com condição** — contato futuro
pede autorização própria.

---

## (d) WhatsApp Business

**Fontes primárias (lidas em 13/11/2026):**
- Política de Mensagens do WhatsApp Business, "Last updated: September 23, 2026" **[N]**:
  https://whatsappbusiness.com/policy/ (os endereços antigos `business.whatsapp.com/policy` e
  `www.whatsapp.com/legal/business-policy` redirecionam para lá)
- Termos da Meta para a Plataforma do WhatsApp Business, "Última atualização: 23 de setembro de 2026" **[N]**:
  https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform
- Termos do aplicativo WhatsApp Business, vigentes desde 23/09/2026 **[S]**:
  https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App
- Documentação de opt-in **[S]**: https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in
- Ajuda, "conversa em um clique" **[S]**: https://faq.whatsapp.com/5913398998672934

### Mensagens comerciais e opt-in

- "You may only contact people on WhatsApp if: (a) they have given you their mobile phone number or username; and
  (b) you have received opt-in permission from the recipient confirming that they wish to receive subsequent messages
  or calls from you." **[N]** A responsabilidade de obter o opt-in conforme a lei é de quem envia **[N]**.
- A documentação exige que o opt-in diga claramente o nome da empresa de quem a pessoa vai receber mensagens **[S]**.
- "You must respect all requests (either on or off WhatsApp) by a person to block, discontinue, or otherwise opt
  out" **[N]**
- "You must not impersonate another business or otherwise mislead customers as to the nature of your business."
  **[N]**
- Na API: fora da janela de 24 horas depois da última mensagem do usuário, só modelo de mensagem aprovado **[S]**;
  automação é permitida na janela, mas a empresa "must also have available prompt, clear, and direct escalation
  paths" **[N]**.
- Se a mensagem do usuário, por si, dispensa opt-in: a política é **silente**.

### Repasse do contato a terceiros

- **API (Plataforma) — cláusula 4.1 dos Termos da Meta, texto oficial em português:** a empresa não deve
  "(b) compartilhar, transferir, vender, licenciar ou distribuir Dados da Plataforma do WhatsApp Business, incluindo
  quaisquer formas ou dados anônimos, agregados ou derivados, para quaisquer terceiros, exceto para um Provedor de
  Soluções de acordo com estes Termos" **[N]**. "Dados da Plataforma" são os "dados obtidos com o uso da Plataforma
  do WhatsApp Business" **[N]**; "Provedor de Soluções" é o terceiro autorizado a usar a API em nome da empresa
  **[N]** — não é um comprador de contatos. A cláusula não traz exceção por consentimento do usuário **[N]** (se
  existe exceção em outro documento, por exemplo nos termos de tratamento de dados, não foi conferido).
- **Aplicativo e API — Política de Mensagens:** "You are responsible for and must secure all necessary notices,
  permissions, and consents to collect, use, and share people's content and information" **[N]**; "You may not
  forward or otherwise share information from a customer chat with any other customer." **[N]**; dados obtidos do
  WhatsApp sobre a pessoa não se usam "for any purpose other than as reasonably necessary to support messaging with
  that person" **[N]**.
- **Aplicativo gratuito:** os termos não têm cláusula que proíba nem que permita repassar o contato a terceiro
  **[S]**: **silente**.
- A palavra "lead" não aparece nos dois documentos **[S]**. Serviço de dedetização não está entre os conteúdos
  restritos; a venda de inseticida e pesticida químico está (política comercial da Meta) **[S]**.

### Os dois desenhos

- **Desenho A — o número do site faz a triagem no WhatsApp e repassa o contato à licenciada.** Pela API: **vedado**
  pela letra da cláusula 4.1(b). Pelo aplicativo gratuito: **não conclusivo** (silente; pesam contra a trava de
  finalidade e a exigência de consentimento). Em qualquer caso, a licenciada só pode chamar a pessoa com opt-in que a
  nomeie.
- **Desenho B — o botão do site abre direto o WhatsApp da licenciada** (link `wa.me`, recurso oficial, com mensagem
  pré-preenchida **[S]**). **Permitido com condição:** a conversa é iniciada pela pessoa, com a empresa que vai
  atender; as obrigações da política recaem sobre a conta da licenciada. Limite: o site só registra o clique, não o
  telefone nem a conversa.
- **Variante que não passa pelo WhatsApp do site (inferência, não frase da fonte):** o contato é colhido num
  **formulário do site**, com o consentimento da seção (c) nomeando a licenciada, e é ela que chama a pessoa. O dado
  não é "dado da Plataforma" (não veio do WhatsApp), e o opt-in nomeia quem vai enviar a mensagem. A política é
  silente sobre o opt-in de uma empresa ser colhido por outra; a condição que ela fixa (nomear quem envia) fica
  atendida.

**O que isso corta do plano:** o "número próprio do site que faz a triagem e encaminha o lead" — que a pesquisa
antiga recomendava — não se sustenta na API e é incerto no aplicativo. O WhatsApp do site, se existir, serve para
orientar a pessoa e entregar a ela o link da licenciada; a prova de que houve contato tem de vir de outro lugar
(clique registrado, formulário com consentimento, ou confirmação da licenciada).

**Não obtido / não conclusivo em (d):** tarifas da API para o Brasil (as duas páginas oficiais de preço se
contradizem; a documentação diz que, desde 01/10/2026, a mensagem de serviço é gratuita só até 1.000 por número por
mês **[S]**); se os termos comuns do WhatsApp (que vedam vender "dados obtidos de nós") valem para a conta do
aplicativo Business.

### Pesquisa de 25/09 — continua valendo ou foi corrigida

`/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`: linha 88 ("número próprio ou API que
faz a triagem e encaminha o lead"): **corrigida** — vedado na API, não conclusivo no aplicativo. Linha 91: **vale com
ressalva** — contato futuro pelo WhatsApp exige opt-in em nome de quem envia. A hipótese de que a maior parte do
contato vem por WhatsApp e não por ligação **não foi conferida**.

---

## O que as quatro restrições, juntas, deixam de pé

1. Um **site de conteúdo e comparação** que se declara intermediário, nomeia em cada página de oferta a licenciada
   que atende (razão social, licença, órgão, endereço) e não usa os termos vedados.
2. Captação por **botão que abre o WhatsApp da licenciada** ou por **formulário com consentimento específico** que
   nomeia quem recebe; registro de quem recebeu cada contato; canal de exclusão que avisa as empresas.
3. No mapa, só a **gestão autorizada do perfil da licenciada**, com o telefone e o site dela.
4. Fora: perfil próprio, endereço de fachada, avaliação incentivada, página "anônima" com cara de dedetizadora,
   repasse pelo WhatsApp do site via API, venda do mesmo contato a muitas empresas sem que a pessoa saiba quais.

## O que não foi lido e por quê

- **PDFs oficiais** (Portaria CVS 1/2024 e sua republicação de 15/10/2026; Anexo I da Portaria SMS 266/2025; guias
  da ANPD de legítimo interesse, de agentes de tratamento e de cookies): a ferramenta de leitura não extrai texto de
  PDF. Tudo o que dependia deles está marcado "não conclusivo".
- **Diário Oficial da União** (`in.gov.br`): não abriu em nenhuma tentativa; a RDC 622 foi lida na base de
  legislação da Anvisa e as resoluções da ANPD, no site da ANPD.
- **Site do Centro de Vigilância Sanitária** (`cvs.saude.sp.gov.br`): erro 403; a vigência da Portaria CVS 9/2000
  não foi confirmada.
- **Jurisprudência** sobre responsabilidade de site de indicação e **autorregulamentação publicitária**: fora do
  escopo deste item.
- A lista completa do que cada subagente tentou abrir está no fim de cada anexo.
