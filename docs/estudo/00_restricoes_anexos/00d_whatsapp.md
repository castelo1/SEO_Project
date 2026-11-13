# Rascunho 00d — WhatsApp Business: mensagens comerciais, opt-in e repasse de contato a terceiros

- **Leitura feita em:** sexta, 13/11/2026, das 19:31 às 19:45 (horário de Brasília; `TZ=America/Sao_Paulo date` no início: `Fri Nov 13 19:31:56 -03 2026`).
- **Item da rodada:** 2, seção (d). Rascunho de subagente: é hipótese até a sessão principal conferir.
- **Natureza:** levantamento de política e de termos contratuais com fonte. **Não é parecer jurídico.**
- **Classe de evidência de tudo o que segue:** A (política oficial da Meta/WhatsApp lida na fonte), salvo onde marcado.
- **Quem ganha com a afirmação:** a Meta é a dona da regra e a parte que a aplica (ganha com a própria plataforma e, na API, com a cobrança por mensagem). Nenhuma fonte de provedor, agência ou ferramenta foi usada.

## Como ler as marcas de conferência

A ferramenta de leitura (WebFetch) responde por um modelo pequeno, que se recusou a transcrever seções inteiras e limita cada citação a ~125 caracteres. Por isso as citações abaixo foram montadas com fragmentos consecutivos pedidos como "exact words".

- **[2x]** = literal conferido em duas chamadas diferentes (outra pergunta, ou a versão em outro idioma).
- **[1x]** = literal obtido uma única vez; trate como "muito provável", reconfira antes de publicar entre aspas.
- **[paráfrase]** = paráfrase da ferramenta; não usar entre aspas.

Aviso de domínio: os endereços oficiais `business.whatsapp.com/policy`, `www.whatsapp.com/legal/business-policy` e `www.whatsapp.com/legal/commerce-policy` respondem hoje com redirecionamento 301 para `whatsappbusiness.com/policy/` (o menu "For Business" de `www.whatsapp.com` também aponta para `whatsappbusiness.com`). Tratei esse domínio como oficial por ser o destino do redirecionamento do próprio servidor da Meta. A sessão principal pode querer confirmar isso no navegador.

---

## 1. Quais documentos regem cada caso, e a data de cada um

| Documento | URL aberta | Data exibida | Vale para |
|---|---|---|---|
| WhatsApp Business Messaging Policy (Política de Mensagens) | https://whatsappbusiness.com/policy/ (pt-BR: https://whatsappbusiness.com/pt-br/policy/) | "Last updated: September 23, 2026" / "Última atualização: 23 de setembro de 2026" [2x] | app WhatsApp Business **e** Plataforma (API/Cloud API); a seção 2 é só da Plataforma |
| WhatsApp Terms for WhatsApp Business App | https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App | "Effective September 23, 2026" [2x] | app WhatsApp Business (gratuito) |
| WhatsApp Terms for WhatsApp Business Platform | https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-Platform | "Effective September 23, 2026" [2x] | API/Cloud API |
| Meta Terms for WhatsApp Business Platform (antigos "Business Solution Terms") | https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform | "Last Modified: September 23, 2026" / "Última atualização: 23 de setembro de 2026" [2x] | API/Cloud API |
| Política Comercial | não há mais página própria do WhatsApp: `whatsapp.com/legal/commerce-policy` redireciona para a Política de Mensagens, que remete à Meta Commerce Policy: https://www.facebook.com/policies_center/commerce | sem data exibida | recursos de comércio (catálogo, pagamentos) |
| WhatsApp Messaging Guidelines | https://www.whatsapp.com/legal/messaging-guidelines | "Last updated: September 23, 2026" [1x] | incorporadas pelos Termos do app Business |
| Termos de Serviço comuns | https://www.whatsapp.com/legal/terms-of-service (pt: `?lang=pt_BR`) | "Effective Date: January 4, 2021" / "Data da vigência: 4 de janeiro de 2021" [2x] | conta pessoal (WhatsApp Messenger) |
| Página-índice dos termos de empresa | https://www.whatsapp.com/legal/business-terms | sem data; só lista os dois termos (App e Plataforma) | — |

Encadeamento conferido na fonte:
- Os Termos do app Business incorporam por referência: Messaging Policy, Messaging Guidelines, Business Data Processing Terms, Intellectual Property Policy, Brand Guidelines e a política de privacidade do app [1x, lista]. Em conflito, os documentos adicionais prevalecem [1x].
- Os Termos da Plataforma: "These Terms incorporate by reference the WhatsApp Business Messaging Policy and the Meta Terms for WhatsApp Business Platform" [2x].
- Os Termos do app Business **não dizem** se os Termos de Serviço comuns também se aplicam à empresa ("not stated", segundo a leitura) — ver "não confirmado".

**Para o gerador de leads:** desenho A no app = Termos do app + Messaging Policy + Guidelines. Desenho A na API = Termos da Plataforma + Meta Terms + Messaging Policy. Desenho B = os mesmos documentos, mas quem está vinculado é a **dedetizadora** dona do número; o site não é parte de contrato algum com o WhatsApp (só publica um link).

---

## 2. Opt-in

**Fontes:** Messaging Policy, seção "1. Create a Quality Experience" e seção 2 (https://whatsappbusiness.com/policy/, atualizada em 23/09/2026); documentação "Get opt-in for WhatsApp" (https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in — hoje em `developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in`; sem data de página); "About the WhatsApp Business Platform" (https://developers.facebook.com/documentation/business-messaging/whatsapp/about-the-platform; sem data). Leitura em 13/11/2026.

Trechos que decidem:
- Regra geral: "You may only contact people on WhatsApp if: (a) they have given you their mobile phone number or username" e "(b) you have received opt-in permission from the recipient confirming that they wish to receive subsequent messages or calls from you." [2x]
- Quem responde: "You are solely responsible for determining the method of opt-in, that you have obtained opt-in in a manner" [2x] que cumpra a lei aplicável [resto da frase: 1x].
- O que o opt-in tem de dizer (documentação): "Businesses must clearly state the business's name that a person is opting in to receive messages from." [2x] e "Businesses must clearly state that a person is opting in to receive communication from the business." [1x]. Na visão geral da Plataforma: "Opt-in must clarify your business name and intent." [1x]
- Desde a atualização de novembro de 2024 o opt-in "can be general and not specifically for WhatsApp" [1x], desde que cumpra a lei local.
- Saída: "You must respect all requests (either on or off WhatsApp) by a person to block, discontinue, or otherwise opt out" [2x]; e "Do not confuse, deceive, defraud, mislead, spam, or surprise people with your communications." [1x]
- Janela e modelos (seção 2, só Plataforma): "You may only initiate conversations using an approved Message Template (as defined in our documentation)." [2x]; "You may reply to a user message without use of a Message Template as long as it's within the 24-hour customer service window" [2x], que abre e reinicia a cada mensagem do usuário [1x]; "Outside the 24-hour customer service window, you may only send messages via approved Message Templates." [2x]
- Documentação: "You must obtain user opt-in before sending message templates." [1x]
- Categorias (página de preços): marketing, utilidade e autenticação são modelos; "service" é "Any non-template message not powered by the Meta Business Agent Platform." [1x]; há uma quinta categoria, Meta Business Agent, desde 01/07/2026 [paráfrase].

**A conversa iniciada pelo usuário dispensa opt-in?** A política é **silente**: não há frase dizendo que a mensagem do usuário vale como opt-in (perguntei isso expressamente à página; resposta: "no such sentence"). O que ela diz é mecânico: dentro de 24 horas da última mensagem do usuário a empresa pode responder sem modelo; fora disso, só com modelo aprovado — e a documentação exige opt-in antes de enviar modelo. A ajuda geral ("How to use WhatsApp responsibly", https://faq.whatsapp.com/361005896189245) recomenda: "Only send messages to those who have contacted you first or have requested you contact them on WhatsApp." [2x, inglês e português]

**Para o gerador de leads:** quem vai enviar a mensagem é quem precisa do opt-in, e o texto do opt-in tem de trazer o **nome da empresa que vai falar**. O meio (site, papel, telefone) é livre. Responder a quem escreveu primeiro, dentro de 24 horas, é o caso que a política trata como normal.

---

## 3. Repasse do contato a terceiros

**Fontes:** Meta Terms for WhatsApp Business Platform, cláusulas 1.1, 4.1 e 4.7 (https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform, modificados em 23/09/2026); Messaging Policy, seções 1 e 3; Termos do app Business, seções 4 e 6; Termos de Serviço comuns. Leitura em 13/11/2026.

Trechos que decidem:
- **API/Cloud API — proibição expressa de repasse.** Cláusula 4.1: a empresa não pode "(b) share, transfer, sell, license, or distribute WhatsApp Business Platform Data, including any anonymous, aggregate, or derived forms or data, to any third parties, except to a Solution Provider in accordance with these Terms" [2x em inglês + 2x em português: "compartilhar, transferir, vender, licenciar ou distribuir Dados da Plataforma do WhatsApp Business"].
  - Definição: "WhatsApp Business Platform Data (data you obtain from using the WhatsApp Business Platform)" [2x].
  - "Solution Provider" é o terceiro "authorized to use these APIs on such business' behalf" [2x] — isto é, o provedor técnico da API, não um comprador de leads.
  - Perguntei se há exceção por consentimento do usuário: resposta "No such exception appears in clause 4.1" [paráfrase da ferramenta sobre ausência; conferir no navegador].
  - A alínea (a) da mesma cláusula ressalva "the content of your message threads" só para a proibição de montar perfis [1x]; a alínea (b) não traz essa ressalva. Leitura literal: o conteúdo da conversa também é "dado da Plataforma" para fins de repasse.
  - Também vedado: "(c) distribute, sell, resell, or rent the WhatsApp Business Platform to third parties" [1x em inglês + português] e "(g) impersonate or register on behalf of any person or entity or otherwise misrepresent your affiliation" [1x em inglês + português].
- **App e API — finalidade dos dados (Messaging Policy, seção 3):** "Don't use any data obtained from us about a person you message within WhatsApp, other than the content of message threads, for any purpose other than as reasonably necessary to support messaging with that person." [1x em inglês + versão pt-BR conferida]
- **App e API — consentimento para compartilhar:** "You are responsible for and must secure all necessary notices, permissions, and consents to collect, use, and share people's content and information" [2x], incluindo manter política de privacidade publicada [1x].
- **App e API — entre clientes:** "You may not forward or otherwise share information from a customer chat with any other customer." [2x]
- **App e API — identidade:** "You must not impersonate another business or otherwise mislead customers as to the nature of your business." [2x]
- **App Business (Termos, seção 4):** "Company must also secure all necessary rights, consents, and permissions (for example, opt-in) to share its customers' contact and other personal data with WhatsApp, and to communicate with its customers via the WhatsApp service using this information." [2x]. Os Termos do app **não têm** item que proíba ou permita expressamente repassar ou vender dados de usuários a terceiros (a leitura devolveu "no such item"); vedam "(e) collect information of or about other users in any impermissible or unauthorized manner" [2x] e "(d) impersonate or register on behalf of any person or entity" [2x].
- **Termos de Serviço comuns (conta pessoal):** vedado "(g) sell, resell, rent, or charge for our Services or data obtained from us or our Services in an unauthorized manner" [inglês 1x + português]. Se isso alcança a conta do app Business, não está declarado.
- **Ajuda:** "Don't share phone numbers without consent or use data obtained from illicit sources to message users on WhatsApp" [inglês 1x + português].
- A palavra "lead" não aparece na Messaging Policy nem nos Meta Terms (busca literal pedida nas duas páginas: ausente).

**Respostas às perguntas da tarefa:**
- *A empresa A coleta e a empresa B inicia a conversa?* Para B iniciar, a regra de opt-in recai sobre B ("you have received opt-in"), e a documentação exige que o opt-in nomeie a empresa de quem a pessoa vai receber mensagens. A política é **silente** sobre o opt-in ser colhido por outra empresa em nome de B; ela só fixa o conteúdo mínimo (nome de quem envia) e a responsabilidade (de quem envia).
- *O opt-in dado a A vale para B?* Não há frase dizendo "não vale" nem "vale". Pela exigência de nomear a empresa, um opt-in que só nomeia A não atende ao requisito para B (inferência direta do texto, não frase da fonte).
- *Vender/compartilhar dados obtidos pelo WhatsApp?* Na **API**: vedado na letra da cláusula 4.1(b), sem exceção por consentimento. No **app**: silente quanto a terceiros; valem a trava de finalidade da seção 3 (dados "obtained from us", exceto o conteúdo da conversa) e a exigência de consentimento para compartilhar.
- *Agir em nome de terceiros?* Só há a figura do "Solution Provider" (opera a API em nome da empresa) e a proibição de se registrar ou se passar por outra pessoa ou entidade.

**Para o gerador de leads:** o número do site ligado à API não pode, pela letra dos Meta Terms, repassar nem vender à dedetizadora o que obteve pela API (telefone, conteúdo da triagem). No app gratuito não há a mesma cláusula, mas há trava de finalidade e exigência de consentimento, e a venda de "dados obtidos de nós" aparece proibida nos termos comuns.

---

## 4. Setores e conteúdos restritos

**Fontes:** Messaging Policy, seções 4 e 5 e "Policy for WhatsApp Commerce Features" (https://whatsappbusiness.com/policy/); Meta Commerce Policy (https://www.facebook.com/policies_center/commerce) e páginas de detalhe `/hazardous_goods_and_materials` e `/services` (sem data exibida). Leitura em 13/11/2026.

- A lista de bens e serviços cuja compra, venda ou promoção é proibida no WhatsApp for Business inclui "Hazardous goods and materials" [2x] e "Business models, goods, items, or services that we determine may be or are fraudulent, misleading, offensive, or deceptive" [2x]. Controle de pragas, pesticida e "lead generation" **não aparecem** na Messaging Policy (busca literal: ausentes).
- Meta Commerce Policy, materiais perigosos: "Commerce content may not promote the buying, selling, or trading of hazardous materials and substances." [inglês 1x + português]; exemplo não permitido: "Chemical Pesticides and Insecticides" / "Inseticidas e pesticidas químicos" [2x]. Trata de **produto**; serviço de dedetização não é mencionado.
- Meta Commerce Policy, serviços: "Approved services may only be offered through catalogs on the WhatsApp Business app or through Appointments in Facebook or Instagram." e "Services may not be offered through other commerce surfaces." [inglês 1x + português]. Entre os exemplos não permitidos nas demais superfícies: "Home maintenance services including cleaning, construction, painting, plumbing, electricians, and lawn care" [1x]. Dedetização não é citada; o que é "approved service" não está definido na página. Observação: a página-índice lista "Serviços" entre os conteúdos restritos e a página de detalhe traz o cabeçalho de conteúdo proibido.
- A Política Comercial rege se a empresa pode vender "using WhatsApp for Business, such as WhatsApp commerce product features like catalog and payments" [1x]: é sobre catálogo e pagamentos, não sobre a conversa de atendimento.
- Verticais reguladas da seção 5 (jogos, medicamentos sem receita, álcool) não incluem pragas [paráfrase].

**Para o gerador de leads:** o **serviço** de dedetização não está listado como proibido nem restrito; a **venda de inseticida/pesticida químico** está. Intermediário/gerador de leads: **silente**. O risco textual que sobra é a cláusula aberta de "modelos de negócio" que a Meta considere enganosos, e a regra de não enganar sobre a natureza do negócio.

---

## 5. Automação, volume e banimento

**Fontes:** Messaging Policy, seções 2 e 7; Meta Terms, cláusula 4.7; política de preços para "AI Providers" (https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers); Messaging Limits (https://developers.facebook.com/docs/whatsapp/messaging-limits); Central de Ajuda (URLs abaixo). Leitura em 13/11/2026.

- **Bot com saída para humano (API):** "You may use automation when responding during the 24-hour window, but must also have available prompt, clear, and direct escalation paths." [2x]. Caminhos listados: transferência para agente humano na conversa, telefone, e-mail, suporte na web, visita à loja, formulário de suporte [1x, lista].
- **Chatbots de IA de uso geral (API):** cláusula 4.7 dos Meta Terms — provedores de IA "are strictly prohibited from accessing or using the WhatsApp Business Platform" para oferecer essas tecnologias "when such technologies are the primary (rather than incidental or ancillary) functionality being made available for use" [inglês 1x + português]. Data: a página de preços para AI Providers fala em "our Terms of Service updated on January 15, 2026" [2x] e diz que, desde 11/03/2026, no Brasil ("Brazil (+55)") AI Providers podem enviar mensagens de serviço, cobradas por mensagem [2x] — nos países em que a Meta é "legally required" a permitir. Os Meta Terms em si não trazem a data da regra. Uma empresa que usa IA só para o próprio atendimento não é tratada nessa página [silente]; o texto da cláusula mira quem tem a IA como funcionalidade principal.
- **Limite de volume (API):** portfólio novo começa com limite de 250 destinatários únicos em 24 horas móveis, para mensagens **fora** da janela de atendimento; degraus de 2.000, 10.000, 100.000 e ilimitado [1x, "Newly created business portfolios have a messaging limit of 250."].
- **Automação no app gratuito:** mensagem de saudação automática (na primeira interação e após 14 dias sem conversa), mensagem de ausência e respostas rápidas (https://faq.whatsapp.com/501866148528310; ausência e respostas rápidas vistas só no resultado de busca) [1x]. O Meta Business Agent (IA da Meta) pode ser ativado no app, mas está "disponível somente para empresas selecionadas em alguns países" [1x]; Brasil não é citado (https://faq.whatsapp.com/291930066973116).
- **O que leva a restrição ou banimento:**
  - Messaging Policy, seção 7: "We may limit or remove your access to or use of WhatsApp for Business, or limit your ability to send messages, if you receive significant amounts of negative feedback" [2x no primeiro fragmento]; "Users can block or report businesses." [2x]; "Our systems may limit the amount of messages a business can send or calls a business can initiate, based on this user feedback." [2x]
  - Termos do app Business, uso aceitável: vedado "(h) send, distribute, or post spam, unsolicited electronic communications" [2x] e usar o serviço "without applicable business licenses" [2x]; a Meta pode "limit, throttle, suspend, or terminate Company's account" [1x].
  - Termos comuns: vedadas comunicações "such as bulk messaging, auto-messaging, auto-dialing, and the like" e "any non-personal use of our Services unless otherwise authorized by us" [inglês 1x + português].
  - Ajuda (https://faq.whatsapp.com/361005896189245): "Don't bulk message, auto-message, or auto-dial using WhatsApp." [inglês 1x + português]; "we ban accounts that are reported multiple times" [inglês 1x + português].
  - Ajuda (https://faq.whatsapp.com/5957850900902049, em português): os produtos "não foram projetados para o envio de mensagens automáticas ou em massa" [1x]; medidas legais desde 7 de dezembro de 2019 [1x].
  - Ajuda (https://faq.whatsapp.com/723378546580115): conta do app Business pode ser banida por violar a Política de Mensagens ou a Política Comercial da Meta, por exemplo "com o envio de spam" [1x]; "A maioria das análises é concluída em até 24 horas." [1x]
  - Ajuda (https://faq.whatsapp.com/1655751878365653): muitos bloqueios ou denúncias geram aviso e, persistindo, suspensão das listas de transmissão comerciais "por três dias" [1x]; orientação: "Envie mensagens somente para pessoas que aceitaram receber mensagens de marketing." [1x]
- "Lista comprada" não aparece com essas palavras; o que há é "data obtained from illicit sources" e "share phone numbers without consent".

**Para o gerador de leads:** triagem automática é permitida na API dentro da janela de 24 horas, com saída clara para humano. O que derruba conta, pelo texto, é mensagem não solicitada, em massa, e volume de bloqueios e denúncias — exatamente o que acontece quando uma empresa que a pessoa não conhece (a dedetizadora B) chama sem a pessoa esperar.

---

## 6. Preço da API para o Brasil

**Fonte:** "Pricing on the WhatsApp Business Platform" (https://developers.facebook.com/docs/whatsapp/pricing; sem data de página; diz refletir as mudanças vigentes desde 01/10/2026). Leitura em 13/11/2026, três chamadas.

- Modelo: "Effective July 1, 2025 – Meta charges on a per-message basis" [1x + paráfrase coerente em outras duas chamadas].
- **Mudança de 01/10/2026 (corrige o que se sabia antes):** as mensagens de serviço (sem modelo, na janela), gratuitas desde 01/11/2024, voltaram a ser cobradas acima de uma franquia: "Meta provides 1,000 free service messages per month" por número [2x]; "Meta charges as of the 1,001st service message per month, after the free tier has been used." [2x]. Modelos de utilidade enviados dentro da janela, gratuitos desde 01/07/2025, passaram a cobrança regular em 01/10/2026 [2x, paráfrase com trecho]. Sem meio de pagamento cadastrado, a Meta deixa de entregar as mensagens de serviço cobradas [1x].
- Janela: "When a WhatsApp user messages you or calls you, a 24-hour timer called a customer service window starts." [1x]
- Brasil: faturamento em reais em implantação desde 01/07/2026; "Per-message rates in BRL are published in our rate cards and volume tiers." [2x]; cobrança em BRL pela entidade local [1x].
- **Valores por mensagem para o Brasil: não obtido.** As tabelas (CSV/PDF) são links cujo endereço a ferramenta não enxergou, e a página interativa (https://whatsappbusiness.com/products/platform-pricing) veio com os campos de tarifa vazios. O único número visto é um exemplo de comparação, "0.68 ¢ per message", descrito como a tarifa de utilidade e autenticação para usuários no Brasil, **sem moeda declarada e sem data** — não usar como preço.
- **Contradição entre páginas oficiais:** a página comercial `whatsappbusiness.com/products/platform-pricing` ainda diz "we do not charge for service messages" e janela gratuita de 72 horas para anúncios [1x]; a documentação de desenvolvedor diz o contrário desde 01/10/2026 (e fala em janela de ponto de entrada gratuito de até 7 dias [1x]). Fico com a documentação, que é a mais específica e datada, mas registro o conflito.

**Para o gerador de leads:** um número do site na API paga pela triagem acima de 1.000 mensagens de serviço por mês; a dedetizadora que chamar a pessoa fora da janela paga modelo. Valores em reais: abrir a tabela oficial no navegador.

---

## 7. Links "clique para conversar" (wa.me)

**Fonte:** Central de Ajuda, "How to use click to chat" / "Como usar o recurso de conversa em um clique" (https://faq.whatsapp.com/5913398998672934; sem data de artigo). Leitura em 13/11/2026.

- É recurso oficial: permite iniciar conversa "without having their phone number saved in your phone's address book" [inglês 1x + português].
- Formato: "Use https://wa.me/<number> where the <number> is a full phone number in international format." [inglês 1x + português]
- Mensagem pré-preenchida: `https://wa.me/<número>?text=<texto codificado em URL>`; "The pre-filled message will automatically appear in the text field of a chat." [1x]. A pessoa ainda precisa tocar em enviar.
- "Click to chat works on both your phone and WhatsApp Web." [inglês 1x + português]
- Restrição ao conteúdo da mensagem pré-preenchida ou ao uso por empresas: **nenhuma declarada** no artigo. Há só orientação sobre o botão oficial "Chat on WhatsApp": "Use the button as is. Don't change the button." [1x]

**Para o gerador de leads:** o desenho B usa um recurso documentado; a conversa nasce como iniciada pelo usuário com a dedetizadora.

---

## Vereditos

### Desenho A — o número do site faz a triagem e repassa o contato à dedetizadora

- **A pela API/Cloud API: vedado na forma descrita.** A cláusula 4.1(b) dos Meta Terms proíbe compartilhar, transferir ou vender a terceiros os dados obtidos pelo uso da Plataforma, com exceção só do "Solution Provider"; não há exceção por consentimento no texto lido. Vender o lead (telefone e triagem colhidos pela API) cai na letra da cláusula.
- **A pelo app WhatsApp Business: não conclusivo.** Os Termos do app não têm cláusula sobre repasse a terceiros (silente). Pesam contra: a trava de finalidade da Messaging Policy para dados "obtained from us" (o conteúdo da conversa fica fora da trava), a exigência de consentimento para compartilhar, e a proibição de vender "data obtained from us or our Services" nos Termos comuns, cuja aplicação à conta Business não está declarada.
- **Condições que valem para A em qualquer caso (o que a fonte diz):**
  1. A dedetizadora só pode chamar a pessoa se tiver opt-in dela, e o opt-in tem de nomear a empresa que vai enviar a mensagem; a responsabilidade é de quem envia.
  2. Se a dedetizadora usar a API, a primeira mensagem dela é modelo aprovado (pago); se usar o app, fica exposta a bloqueio e denúncia de quem não a esperava.
  3. O perfil do número do site não pode enganar sobre a natureza do negócio (é intermediário, não dedetizadora).
  4. Política de privacidade publicada e consentimento para coletar, usar e compartilhar.
  5. Bot só com saída clara para humano; pedido de parar tem de ser atendido.
- **Onde a política é silente:** se o opt-in para B pode ser colhido por A; se há algum caminho consentido de repasse no app.
- **Variante que não esbarra na cláusula (inferência minha, não frase da fonte):** o número do site faz a triagem e entrega **à própria pessoa** o link wa.me da dedetizadora; quem inicia a conversa com B é a pessoa, e nenhum dado sai do WhatsApp do site para B. Na prática, isso converte A em B.

### Desenho B — o link wa.me abre direto o WhatsApp da dedetizadora; o site só registra o clique

- **Permitido com condição.** O link é recurso oficial, sem restrição declarada à mensagem pré-preenchida; a conversa é iniciada pelo usuário, e a empresa pode responder (na API, sem modelo dentro de 24 horas). O site não obtém dado algum do WhatsApp e não é parte dos termos.
- **Condições (o que a fonte diz, e recai sobre a dedetizadora):**
  1. A conta dela segue a Messaging Policy: não enganar sobre a natureza do negócio; respeitar pedido de parar.
  2. Para voltar a falar depois de 24 horas (API) ou mandar oferta, precisa de opt-in em nome dela e, na API, de modelo aprovado.
  3. A conta dela não pode vender produto proibido (inseticida/pesticida químico) pelos recursos de comércio.
- **Onde a política é silente:** sobre terceiro (o site) que publica o link e cobra pelo clique; sobre "lead generation". A regra de não enganar sugere que a mensagem pré-preenchida e a página deixem claro com quem a pessoa vai falar (inferência; o artigo do link não traz regra).
- Limite do desenho: o site não recebe o telefone nem a prova de que a conversa aconteceu — só o clique.

---

## Pesquisa de 25/09: continua valendo ou foi corrigida

Arquivo: `/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`, linhas 85–91.

- **Linha 88** ("Use um número WhatsApp Business próprio (ou API) que faz a triagem e **encaminha** o lead. Assim você guarda o registro."): **corrigida.** Pela API, encaminhar ou vender a terceiro o dado obtido na Plataforma é vedado na letra da cláusula 4.1(b) dos Meta Terms (23/09/2026). Pelo app, o repasse não tem cláusula própria e fica não conclusivo, com trava de finalidade e exigência de consentimento. Em qualquer caso, a dedetizadora que chamar a pessoa precisa de opt-in que a nomeie. A parte "no Brasil a maior parte do contato vai ser por WhatsApp" é hipótese de mercado e **não foi conferida** aqui.
- **Linha 91** ("número e lista de clientes ... ficam com você", com consentimento para contato futuro): **continua valendo com ressalva** — contato futuro pelo WhatsApp exige opt-in em nome de quem envia e, na API, modelo pago; e a lista obtida pela API não pode ser repassada a terceiro.
- **Linha 87** (rastreamento de chamadas, preços de números virtuais): fora do escopo desta seção; **não conferida**.
- **Linhas 89 e 90** (pagamento por lead, exclusividade): não tratam de WhatsApp; **não conferidas**. Observação: o modelo de pagamento por lead com repasse do contato depende do veredito acima.

---

## O que tentei abrir e não abriu (ou mudou de endereço)

- `https://business.whatsapp.com/policy` → 301 para `https://whatsappbusiness.com/pt-br/policy/` (aberta).
- `https://www.whatsapp.com/legal/business-policy` → 301 para `https://whatsappbusiness.com/policy/` (aberta).
- `https://www.whatsapp.com/legal/commerce-policy` → 301 para `https://whatsappbusiness.com/policy/`: não existe mais página própria da Política Comercial do WhatsApp.
- `https://www.whatsapp.com/legal/meta-terms-whatsapp-business` → 301 para `https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform` (aberta).
- `https://www.whatsapp.com/legal/business-terms` → abre, mas só lista os dois termos (App e Plataforma), sem texto.
- `https://www.whatsapp.com/legal/business-terms-for-whatsapp-business` (endereço que tentei por dedução) → HTTP 404.
- Tabelas de tarifas (CSV/PDF) ligadas na página de preços: endereço não visível para a ferramenta; `https://whatsappbusiness.com/products/platform-pricing` abriu com os campos de tarifa vazios.
- `facebook.com/business/help`: uma busca restrita ao domínio não trouxe artigo sobre opt-in; nenhuma página dessa central foi aberta.
- A versão pt-BR da Política de Mensagens abriu, mas a ferramenta devolveu a frase do opt-in em inglês; a tradução oficial dessa frase não foi obtida.

## O que não consegui confirmar na fonte primária

1. Texto integral, palavra por palavra, de cada seção: a ferramenta só devolve fragmentos curtos. Antes de citar entre aspas em documento final, reabrir as páginas no navegador (principalmente a cláusula 4.1 dos Meta Terms e as seções 1 e 3 da Messaging Policy).
2. Se existe exceção por consentimento ao 4.1(b) em outro documento (por exemplo, nos Business Data Processing Terms, que não abri).
3. Se o telefone de quem escreve conta como "data obtained from us" para a trava de finalidade da seção 3 no app.
4. Se os Termos de Serviço comuns (proibição de vender dados obtidos do serviço) se aplicam à conta do app Business.
5. Se o opt-in para a empresa B pode ser colhido pela empresa A: silente.
6. Tarifas por mensagem para o Brasil, em reais ou dólares, e a tarifa da mensagem de serviço acima da franquia: não obtido.
7. O que são "approved services" na política de serviços da Meta e se dedetização entra em catálogo do app.
8. Disponibilidade do Meta Business Agent no Brasil.
9. A data exata em que a cláusula de AI Providers entrou nos Meta Terms consta só da página de preços (15/01/2026), não dos próprios termos.
10. Ruído da ferramenta: em duas leituras dos Meta Terms ela relatou uma linha solta em inglês dentro da cláusula 4.7, sem relação com o texto jurídico; foi ignorada e não é instrução.
