# Rascunho 00a — Item 2(a): Perfil de Empresa do Google, lido na fonte

- **Leitura feita em:** sexta, 13/11/2026, das 19:32 às 19:41 (Brasília; `TZ=America/Sao_Paulo date` no início: `Fri Nov 13 19:31:56 -03 2026`; no fim: `Fri Nov 13 19:40:49 -03 2026`).
- **Ferramenta:** só WebFetch e WebSearch. Nenhum navegador, nenhuma conta, nenhum formulário.
- **Natureza:** levantamento de regras de plataforma (termos do Google) com fonte. **Não é parecer jurídico.**
- **Classe de evidência de tudo o que está entre aspas:** A (documentação oficial do Google, lida na página de ajuda).
- **Quem ganha com a afirmação:** o Google, dono da plataforma. Ele define a regra e a aplica; tem interesse na qualidade do mapa e também vende anúncios. Não vende método de SEO. Não há intermediário interessado entre a regra e este texto.

## Como ler as citações

- O WebFetch devolve o texto por um modelo pequeno e em pedaços de até ~125 caracteres. Onde a frase veio em dois pedaços vizinhos, eu os juntei; nada foi completado de memória.
- **"literal conferido 2x"** = o mesmo trecho voltou igual em duas chamadas (segunda pergunta à mesma página, ou a versão `hl=pt-BR` dizendo o mesmo). A versão de referência é a inglesa: as páginas em português trazem o aviso de que podem ter tradução por IA e têm deslizes (por exemplo "caixa de e-mails em um local remoto" para "mailbox in a remote location").
- O que veio só uma vez, ou resumido pela ferramenta, está sem aspas e marcado **paráfrase da ferramenta**.
- **Nenhuma página exibe data de atualização.** Todas mostram só "©2026 Google" no rodapé. Data de leitura de todas: 13/11/2026.

---

## Pergunta 1 — Um gerador de leads pode ter Perfil de Empresa?

**Fontes**
- https://support.google.com/business/answer/13763036?hl=en ("Business eligibility and ownership guidelines") e `?hl=pt-BR` ("Diretrizes de qualificação e propriedade da empresa").
- https://support.google.com/business/answer/13762416?hl=en ("Overview of Google Business Profile policies"), seção "Ineligible businesses", e `?hl=pt-BR`.
- https://support.google.com/business/answer/3038177?hl=en ("Guidelines for representing your business on Google"), seção "Individual practitioners".

**Trechos que decidem**
- "To qualify for a Business Profile, a business must make in-person contact with customers during its stated hours." — 13763036, "Eligible businesses". *literal conferido 2x* (EN; PT: "só se qualifica … quando interage diretamente com os clientes durante o horário de funcionamento indicado"; a mesma frase abre a seção de inelegíveis em 13762416).
- "Lead generation agents or companies." — item da lista "Ineligible businesses" de 13763036. *literal conferido 2x* (duas chamadas EN; PT: "Agentes ou empresas de geração de leads."; repetido em 13762416 EN e PT).
- "Brands, organizations, artists, and other online-only businesses." — mesma lista. *literal conferido 2x* (EN duas vezes; PT: "… e outras empresas somente on-line.").
- "Sales associates or lead generation agents for corporations aren't individual practitioners and aren't eligible for a Business Profile." — 3038177, "Individual practitioners". *literal conferido 2x* (duas chamadas EN; PT confere a primeira metade).

**O que significa para um gerador de leads**
O site do projeto capta contatos e os vende; não atende cliente presencialmente e só existe on-line. Ele cai em dois itens da lista de inelegíveis ao mesmo tempo (gerador de leads; empresa só on-line) e não cumpre a condição de entrada (contato presencial no horário declarado). Não há exceção que o alcance: as exceções listadas são caixa eletrônico, quiosque, empresa sazonal e cozinha só de entrega.

**Veredito: VEDADO** (perfil próprio do gerador de leads, em qualquer formato).

---

## Pergunta 2 — O que conta como endereço e como atendimento? Nome, categoria, telefone e site

**Fontes**
- https://support.google.com/business/answer/3038177?hl=en e `?hl=pt-BR` (seções "Understand basic guidelines", "Name", "Address", "Service-area businesses", "Storefront versus service-area businesses", "Website & phone", "Categories").
- https://support.google.com/business/answer/9157481?hl=en e `?hl=pt-BR` ("Manage your service areas for service-area & hybrid businesses").
- https://support.google.com/business/answer/14271705?hl=en e `?hl=pt-BR` ("Verify your business with a video recording").
- https://support.google.com/business/answer/13763036?hl=en (lista de inelegíveis).

**Trechos que decidem** (todos *literal conferido 2x*, EN + PT, salvo indicação)

Endereço
- "P.O. boxes or mailboxes located at remote locations aren't acceptable." / "Create your Business Profile for your actual, real-world location." — 3038177, "Address".
- "If your business rents a physical mailing address but doesn't operate out of that location, also known as a virtual office, that location isn't eligible for a Business Profile." — idem.
- "Businesses can't list an office at a co-working space unless that office maintains clear signage, receives customers at the location during business hours, and is staffed during business hours by your business staff." — idem (a versão PT omite "by your business staff").
- "Do not create more than one page for each location of your business, either in a single account or multiple accounts." — idem. As diretrizes básicas repetem a ideia de um só perfil por empresa (*paráfrase da ferramenta*: uma chamada EN, não conferida em PT).
- 13762416: "Merchants that set their business address at a P.O. Box will have their profile suspended." e "If we determine that your business doesn't exist in the location you claim, Google will disable your profile."

Empresa de serviço local (atende no endereço do cliente)
- Definição (9157481): "A business that visits or delivers to customers directly but doesn't serve customers at their business address."
- "Service-area businesses, or businesses that serve customers at their locations, should have one profile for the central office or location with a designated service area." — 3038177.
- "Service-area businesses can't list a "virtual" office unless that office is staffed during business hours." — 3038177.
- "If you're a service-area business, you should hide your business address from customers." — 3038177. Em 9157481: "If you don't serve customers at your business address, remove your address from your Business Profile."
- Limites (9157481): até 20 áreas de cobertura; área total a cerca de 2 horas de carro da base; um só perfil para toda a área; sem sinalização permanente no local, a empresa não é loja física e tem de ser listada como serviço local. (*conferido 2x, EN + PT; aqui resumido sem aspas.*)
- Mais de um perfil só com "separate service areas and separate staff at each location" (3038177).
- Verificação por vídeo de empresa de serviço local (14271705): mostrar onde a empresa opera, "the professional tools, equipment, or products you use for work" e prova de gestão (por exemplo, executar um serviço, abrir o veículo da empresa, mostrar alvará, fatura ou conta no nome do perfil). Gravação ao vivo, sem edição, mínimo de 30 segundos. O método de verificação é escolhido pelo Google (7107242; *paráfrase da ferramenta*, uma chamada).

Nome e categoria
- "Your name should reflect your business's real-world name, as used consistently on your storefront, website, stationery, and as known to customers." — 3038177, "Name". *Uma chamada EN; a versão PT não foi pedida para esta frase: tratar como paráfrase da ferramenta.* A página lista como não permitido no nome: slogan, serviço ou produto, localização, telefone, URL, horário; e diz que informação desnecessária no nome pode levar à suspensão.
- Categoria: o mínimo de categorias que descreva o negócio principal; a categoria completa a frase "esta empresa É", não "TEM"; não usar categoria como palavra-chave nem a de outro negócio relacionado. (*paráfrase da ferramenta*, uma chamada EN.)

Telefone e site
- "Do not provide phone numbers or URLs that redirect or "refer" users to landing pages or phone numbers other than those of the actual business, including pages created on social media sites." — 3038177, "Website & phone". (PT mais curto: "… que direcionem os usuários a locais ou páginas de destino que não sejam da empresa".)
- "The phone number must be under the direct control of the business." — idem (PT: "precisa ser controlado diretamente pela empresa").
- "Premium phone numbers are not acceptable regardless of the rate charged to the caller." — idem.
- "Use a local phone number instead of a central call center helpline number whenever possible." — idem.

**O que significa para um gerador de leads**
- Endereço: caixa postal e escritório virtual estão fora por texto expresso; coworking só com placa, atendimento no local e equipe própria no horário. Um endereço residencial "oculto" como empresa de serviço local só serve a quem de fato vai ao cliente prestar o serviço — e a verificação por vídeo pede ferramentas, equipamento e prova de gestão. O gerador de leads não tem isso; a dedetizadora licenciada tem.
- A empresa de serviço local é o enquadramento natural da **dedetizadora parceira**: um perfil para a base real, endereço oculto, até 20 áreas, raio de ~2 horas.
- Telefone e site do perfil têm de ser os da empresa real e sob o controle direto dela. Colocar no perfil da parceira o telefone do intermediário ou a URL do site de leads é o que o texto proíbe ("redirect or 'refer'").
- Nome com praga, bairro ou "24 horas" que não faça parte do nome real é informação desnecessária e é motivo de suspensão.

**Veredito**
- Endereço fictício, caixa postal, escritório virtual, coworking sem equipe: **VEDADO**.
- Perfil de serviço local com endereço oculto para o gerador de leads: **VEDADO** (continua inelegível pela pergunta 1).
- Perfil de serviço local da dedetizadora licenciada, na base real dela: **PERMITIDO COM CONDIÇÃO** (uma base, um perfil; telefone e site dela).
- Telefone ou URL do perfil apontando para o intermediário: **VEDADO**.

---

## Pergunta 3 — O que acontece com perfil fora da regra?

**Fontes**
- https://support.google.com/business/answer/4569145?hl=en e `?hl=pt-BR` ("Fix suspended or disabled profiles").
- https://support.google.com/business/answer/13762416?hl=en e `?hl=pt-BR` (visão geral das políticas; restrições de conta).
- https://support.google.com/business/answer/14114287?hl=en e `?hl=pt-BR` ("Business Profile restrictions for policy violations").
- https://support.google.com/contributionpolicy/answer/7400114?hl=en e `?hl=pt-BR` ("Prohibited & restricted content", políticas de conteúdo de usuários do Maps).
- https://support.google.com/business/answer/13763036?hl=en (parte final, sanção a representante autorizado).

**Trechos que decidem** (todos *literal conferido 2x*, EN + PT)

Suspensão, desativação e conta
- "We may suspend or disable Business Profiles that don't follow our guidelines." — 4569145.
- Perfil removido: "The public can't go to the profile." / "The owner and managers can't act on the profile." — 4569145.
- "If a merchant's account is restricted, all Business Profiles associated with that account will be suspended." — 13762416. O gatilho é "a pattern of violating Google Business Profile policies". Em 4569145: com a conta restrita, "you won't be able to create or claim other profiles."
- Representante autorizado: "Failure to adhere to these policies may result in a suspension for the Business Profile and/or Google Account." — 13763036.

Recurso
- "Do not create a new Business Profile for the same business." / "Appeals can only be submitted once." — 4569145.
- Provas aceitas no recurso: registro oficial da empresa, licença, certidões fiscais, contas de consumo, com nome e endereço iguais aos do perfil. Se negado, pode haver uma revisão adicional com provas novas. (*paráfrase da ferramenta*; conferido em EN, não pedido em PT.)
- A página não informa prazo de resposta nem prazo para anexar provas no trecho que a ferramenta entregou (EN e PT); ver "não consegui confirmar".

Avaliações
- É engajamento falso: "Reviews or ratings that have been paid for, directly or in kind." — 7400114.
- É vedado a comerciantes e usuários: "Offer incentives – such as payment, discounts, free goods and/or services in exchange for posting any review or revision or removal of a negative review." — 7400114.
- É vedado ao comerciante: "Discourage or prohibit negative reviews, or selectively solicit positive reviews from customers" — 7400114.
- Conflito de interesses inclui "current or former employment, a contractual or consultory relationship" — 7400114. Quem tem contrato com a empresa (o gerador de leads, o gestor do perfil) não a avalia.
- É permitido: pedir avaliação de experiência real, "without offering incentives to do so or attempting to influence the rating or the contents of the review." — 7400114.
- Sanção ao perfil (14114287): "Business Profile will not be able to receive new reviews or ratings for set period of time"; "Business Profile's existing reviews or ratings will be unpublished for set period of time"; "Business Profile will display a warning to let consumers know that fake reviews were removed". Cabe contestação. A duração do "período determinado" não é informada.
- Conteúdo de usuário em geral pode ser limitado ou suspenso no perfil quando for sistematicamente inútil, nocivo ou violador (13762416, "Posting restrictions"; *paráfrase da ferramenta*).

**O que significa para um gerador de leads**
Perfil inelegível ou com endereço falso é suspenso ou desativado; padrão de violação restringe a **conta**, e aí caem todos os perfis ligados a ela — inclusive os de parceiras que o gerador de leads administrar ou possuir pela mesma conta. O recurso é único e pede documento que um gerador de leads não tem (licença e contas no endereço do perfil). Avaliação comprada, trocada por desconto ou escrita por quem tem vínculo é removida e deixa marca pública no perfil da parceira.

**Veredito:** operar fora da regra é **VEDADO**, com consequência documentada (suspensão, desativação, restrição de conta, remoção e bloqueio de avaliações, aviso público). Pedir avaliação verdadeira sem incentivo: **PERMITIDO COM CONDIÇÃO**.

---

## Pergunta 4 — Quais caminhos legítimos para o mapa sobram?

**Fontes**
- https://support.google.com/business/answer/13763036?hl=en e `?hl=pt-BR` ("Ownership"; "Additional guidelines for authorized representatives").
- https://support.google.com/business/answer/7353941?hl=en e `?hl=pt-BR` ("Business Profile third-party policies").
- https://support.google.com/business/answer/3403100?hl=en e `?hl=pt-BR` ("Manage your Business Profile owners & managers").
- https://support.google.com/business/answer/7163406?hl=en e `?hl=pt-BR` ("Tips for working with third parties to manage your Business Profile").
- https://support.google.com/business/answer/3038177?hl=en ("Website & phone").

**Trechos que decidem** (todos *literal conferido 2x*, EN + PT, salvo indicação)

Quem pode gerir e quem é dono
- "Only business owners or authorized representatives may verify and manage their business information on a Business Profile." — 13763036.
- "Any individual or company that manages business information for a Business Profile that they don't own is considered an authorized representative." Exemplos dados pela página: empresa de SEO/SEM, fornecedor de agendamento on-line, rede de afiliados. — 13763036.
- "Never claim a Business Profile without express consent from the business owner." — 13763036. Em 7353941: consentimento expresso "as required by the applicable law" e "Verbal consent isn't sufficient." (*esta última só em EN: uma chamada; tratar como paráfrase da ferramenta.*)
- "Also, all end customers must retain ownership or co-ownership of their Business Profile at all times." — 7353941 (*EN, uma chamada exata; PT confirmou só o início do parágrafo*).
- "After a profile has been created for a client, make the business owner the owner of the profile, and make yourself the manager of the profile." — 7353941.
- "Within 7 business days of notice from an end customer, you must provide that client the ability to disassociate the Google Account used to manage their Business Profile from your services and regain exclusive control of it." — 7353941.
- "Always respond to management access requests promptly, and always transfer Business Profile ownership to the business owner immediately upon request." — 13763036.
- Papéis (3403100): o proprietário tem controle total; o administrador ("manager") tem quase o mesmo acesso — edita nome, categoria, telefone, URLs, horário, fotos, postagens, responde avaliações — e "The only exception is they can't add or remove users or remove the profile." Novo proprietário ou administrador espera 7 dias para certas ações.

O que o terceiro não pode fazer
- "Never make false, misleading, or unrealistic claims." — 13763036. Em 7163406: "Third parties can't promise nor directly influence your business's ranking on Google Search or Maps through any special means."
- Obrigações resumidas de 7353941 (*paráfrase da ferramenta*): informar a empresa de toda mudança; avisar que o perfil é gratuito e declarar a taxa por escrito antes; entregar o aviso "Working with a third party" e ter link para ele no site; não reter o perfil para cobrar; não responder avaliações sem aprovação explícita; não compartilhar senha; não descartar automaticamente as sugestões do Google.
- Sanção: "We may suspend a Business Profile and/or the Google Account you use to manage the Business Profile if you commit a serious policy violation." — 7353941.

Link do site e telefone do perfil administrado
- "Note that the phone number and website for a Business Profile should always be the single, authoritative phone number and website for the business and be verifiable by the business owner." — 13763036.
- "Website content must be owned and managed by the business owner." — 13763036.
- Mais a regra geral de "Website & phone" (pergunta 2): número sob controle direto da empresa; nada de número ou URL que redirecione para outro.

Número de rastreamento de chamadas
- As páginas lidas **não usam a palavra "tracking"** (3038177; 16750496 "Add your phone number", onde só consta que há um número principal e até 2 adicionais — *paráfrase da ferramenta*). O que há é a regra geral: número "under the direct control of the business", sem redirecionar a número que não seja da empresa, e a frase "Additional phone numbers can be used on Google Business Profile websites and other local surfaces." (3038177, *conferido 2x*).
- Leitura: número de rastreamento **do intermediário** no campo principal do perfil contraria o texto. Número de rastreamento contratado e controlado **pela própria licenciada**: a fonte primária não trata do caso — **não conclusivo**.
- O histórico de chamadas do próprio perfil foi descontinuado em 31/07/2024 (https://support.google.com/business/answer/14919056?hl=en; *paráfrase da ferramenta*, uma chamada). O perfil não mede ligações por conta própria.

Empresa que atende só on-line
- Inelegível por texto expresso (pergunta 1). Não há caminho de perfil para o site.

**O que significa para um gerador de leads**
O mapa não é do site; é da empresa licenciada. O que sobra ao projeto é **prestar serviço de gestão** do perfil da parceira, como representante autorizado, com ela dona do perfil — e o perfil apontando para o telefone e o site **dela**. O modelo "perfil da parceira com o meu site e o meu número" não passa. O site de leads compete no orgânico, fora do mapa.

**Veredito**
- Gerir o perfil da licenciada com autorização expressa e escrita, ela como proprietária: **PERMITIDO COM CONDIÇÃO**.
- Ser dono do perfil da parceira, ou criá-lo e mantê-lo em conta própria sem repassar a propriedade: **VEDADO**.
- Site de leads ou telefone do intermediário no perfil da parceira: **VEDADO**.
- Número de rastreamento contratado pela própria licenciada: **NÃO CONCLUSIVO**.

---

## Pergunta 5 — Mudanças de 2025–2026

**Fontes:** as mesmas das perguntas 1–4.

- Nenhuma das páginas lidas exibe data de publicação ou de atualização; só "©2026 Google". **Não é possível datar mudança alguma pela fonte primária.**
- Tentei o arquivo histórico para comparar com 2025 (`web.archive.org`, cópia de 13763036): a ferramenta não abre esse domínio.
- Busca restrita a `support.google.com`, `blog.google` e `developers.google.com` por atualização de política do Perfil de Empresa em 2026: nada datado. O único item de 2026 que apareceu é de política de **anúncios** (outubro de 2026, nome da empresa do anunciante), fora deste escopo e não lido.
- Diferença observada em relação à pesquisa de 25/09 (sem data de quando ocorreu): hoje a lista "Ineligible businesses" está em 13763036 e em 13762416; a página 3038177 não tem mais essa seção e traz a geração de leads só na frase sobre profissionais liberais.
- Indícios sem data: 3403100 diz que administradores eram "formerly known as 'site managers'"; a página de avaliações tem subpáginas de numeração mais alta ("genuine experience", "rating manipulation", "incentivized or biased reviews"), o que sugere texto mais recente — é inferência pela numeração, não fato.

**Veredito: NÃO CONCLUSIVO** quanto a "o que mudou e quando". O texto vigente em 13/11/2026 é o citado acima.

---

## Caminhos legítimos para o mapa

1. **Gestão do perfil da licenciada, como representante autorizado.** Fonte: 13763036 ("Additional guidelines for authorized representatives"), 7353941, 3403100. Condições: consentimento expresso e escrito; a licenciada é proprietária (ou coproprietária) e o projeto entra como administrador; telefone e site do perfil são os dela; taxa declarada por escrito e aviso de que o perfil é gratuito; devolução do controle em até 7 dias úteis quando ela pedir; nenhuma promessa de posição.
2. **Orientar a licenciada a enquadrar-se como empresa de serviço local.** Fonte: 3038177 e 9157481. Condições: um perfil para a base real, endereço oculto se não recebe cliente, até 20 áreas, ~2 horas de raio; perfil adicional só com base e equipe separadas; nome igual ao nome real.
3. **Pedir avaliações verdadeiras para a licenciada.** Fonte: 7400114. Condições: experiência real, sem incentivo, sem selecionar só os satisfeitos, sem ditar conteúdo; ninguém com vínculo contratual avalia.
4. **O site de leads fora do mapa, no orgânico.** As diretrizes do perfil não o alcançam nem o autorizam; é o que resta por exclusão. As regras do orgânico não foram lidas aqui (item 3 da rodada).
5. **Não é caminho:** perfil próprio do site; perfil em endereço de fachada; perfil da parceira com site ou telefone do intermediário; perfil "alugado" cuja propriedade fica com o intermediário.

Consequência para o desenho: no caminho 1 o ativo (perfil, avaliações) é da parceira, por regra, e ela pode retomá-lo. O projeto vende um serviço; não constrói patrimônio no mapa.

---

## Pesquisa de 25/09: continua valendo ou foi corrigida

Arquivo: `/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md`.

| Linha | Afirmação | Situação em 13/11/2026 |
|---|---|---|
| 13 | Política lista "lead generation agents or companies" como inelegíveis | **Continua valendo.** Texto idêntico em 13763036 e 13762416. |
| 13 | O perfil exige contato presencial e endereço real | **Continua valendo.** "in-person contact … during its stated hours"; "actual, real-world location". |
| 13 | Lead-gen fica restrito a orgânico + anúncios, sem o mapa | **Vale para perfil próprio; incompleta.** Faltou o caminho de gerir o perfil da licenciada como representante autorizado. A parte de anúncios não foi conferida aqui. |
| 13 | Se o perfil ficar no nome do parceiro, o ativo é do parceiro | **Continua valendo e ficou mais forte:** a política de terceiros exige que o cliente mantenha a propriedade e a retome em 7 dias úteis. |
| 102 | "Proibido"; inelegíveis; contato presencial; caixa postal não vale; fontes 13763036 e 3038177 | **Continua valendo, com correção de endereço:** a lista de inelegíveis está em 13763036 (e 13762416); 3038177 hoje só tem a frase sobre profissionais liberais e a regra de caixa postal. |
| 103 | Endereço oculto permitido a empresa de serviço local, desde que seja o endereço real (fontes de segunda mão) | **Confirmada agora na fonte primária** (3038177 e 9157481). |
| 103 | Violação de endereço é a principal causa de suspensão | **Não deu para conferir.** O Google não publica ordem de causas; a afirmação é de agência (classe D). |
| 104–105 | Concorrência em SP; ganhos típicos de lead-gen | **Fora deste escopo; não conferidas.** |
| 108 | Sem perfil, o site compete só no orgânico e nos anúncios | **Continua valendo** para o site. |
| 108 | No rank-and-rent dos EUA o inquilino põe o perfil no nome dele, e o ativo do intermediário é o site e o telefone | **Corrigida em ponto que decide:** se o perfil do inquilino apontar para o site ou o telefone do intermediário, contraria "Website & phone" (3038177) e as diretrizes de representante autorizado (13763036). O "mais comum nos EUA" não é verificável na fonte primária. |

Alerta fora das linhas pedidas: as linhas 42, 87 e 91 do mesmo arquivo recomendam "controlar o número de telefone". Isso vale para o número exibido no **site**; no **perfil** da parceira, a regra exige número sob controle direto dela.

---

## O que tentei abrir e não abriu

- `https://web.archive.org/web/2025/https://support.google.com/business/answer/13763036?hl=en` — erro: a ferramenta não busca em `web.archive.org`. Sem comparação histórica.
- `https://support.google.com/contributionpolicy/answer/11414422?hl=pt-BR` ("Engajamento falso") — abriu, mas o corpo veio truncado: só a frase de definição. O conteúdo foi lido na página-mãe 7400114 (EN e PT).
- `https://support.google.com/business/answer/7667250?hl=en` — abriu; é só um índice de políticas, sem texto de regra.
- Todas as demais páginas de `support.google.com` abriram em EN e em PT. A ferramenta marca "conteúdo truncado" no fim de todas; nas seções citadas o corte veio depois do corpo do artigo (menus e rodapé), segundo a própria ferramenta.

## O que não consegui confirmar na fonte primária

- Data de qualquer alteração das regras em 2025–2026 (páginas sem data; arquivo histórico inacessível).
- Prazo de resposta do recurso e prazo para anexar provas: não aparecem no trecho entregue de 4569145 (EN e PT).
- Diferença exata entre perfil "suspenso" e "desativado": 4569145 não define os termos no trecho lido.
- Duração das restrições por avaliação falsa ("set period of time", sem número).
- Regra específica sobre número de rastreamento de chamadas: a palavra não aparece nas páginas lidas.
- Texto do aviso "Working with a third party" que o terceiro tem de entregar: não localizei a página do aviso em si.
- Divergência pequena entre versões de 14114287: a inglesa diz que o aviso de restrição vai por e-mail; a portuguesa diz só que o proprietário é notificado antes.
- Trechos marcados "paráfrase da ferramenta" (nome, categoria, provas do recurso, obrigações detalhadas do terceiro, método de verificação, histórico de chamadas) precisam de segunda leitura antes de virar citação no `00_restricoes.md`.
- Regras de anúncios do Google para geradores de leads e disponibilidade de anúncios de serviços locais no Brasil: fora deste escopo, não lidas.
