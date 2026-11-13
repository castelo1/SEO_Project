# Verificação do item 2 — Restrições que decidem o modelo

- **Início:** `Fri Nov 13 20:02:17 -03 2026` · **fim das conferências:** `Fri Nov 13 20:13:10 -03 2026` (saídas de
  `TZ=America/Sao_Paulo date`).
- **Verificador:** subagente em contexto limpo, sem a conclusão de quem produziu. Não alterei nenhum arquivo além
  deste; não fiz commit; não usei navegador, memória corporativa, skill nem subagente.
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (449 linhas, como estava no
  commit `08e541d`).
- **Ferramentas:** só `WebFetch` (33 chamadas; 4 deram tempo esgotado e foram repetidas com êxito). A ferramenta
  limita cada citação a cerca de 125 caracteres; por isso pedi os trechos em pedaços consecutivos e com pergunta
  de sim ou não.
- **Natureza:** conferência de levantamento com fonte; **não é parecer jurídico**.
- **Limite desta verificação:** a marca **[N]** do artefato ("conferido no texto bruto, no navegador") não é
  reproduzível por mim. O que posso afirmar é que todo trecho que reabri pela ferramenta de leitura bateu.

## VEREDITO: APROVADO, com 1 ponto reprovado e 8 correções pedidas

- Sorteio: **12 OK · 0 FALHA · 0 INCONCLUSIVO** (3 das 12 com ressalva de endereço, falha F2).
- Portão: cumprido na estrutura (quatro seções, fonte, data, trecho, veredito, estado da pesquisa de 25/09).
  **Um ponto reprovado:** a Portaria CVS 9/2000 foi preenchida com cópia hospedada por terceiro (F3).
- Fora do sorteio achei **1 afirmação factual errada** (F1) e **1 endereço que não abre como está escrito** (F2).
- A decisão de fechar o item com as correções feitas, ou só depois delas, é da sessão principal. Minha
  recomendação: corrigir F1, F2 e F3 antes de fechar; as demais podem ir junto.

## 1. Portão, transcrito de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linha 60)

> `docs/estudo/00_restricoes.md` com quatro seções, cada uma com a URL da fonte primária, a data de leitura, o
> trecho curto que decide, e o veredito para um gerador de leads: **permitido / permitido com condição / vedado /
> não conclusivo**. (a) **Perfil de empresa do Google:** diretrizes e regras de elegibilidade vigentes, na página
> do Google — gerador de leads pode ter perfil? o que conta como endereço e atendimento? o que acontece com perfil
> fora da regra? quais caminhos legítimos para o mapa sobram (por exemplo, o perfil ser da empresa licenciada
> parceira)? (b) **Propaganda de controle de pragas:** texto da RDC 622/2022 na fonte oficial e a norma da
> vigilância sanitária de São Paulo (estado e município) — o que um site que anuncia o serviço tem de exibir e o
> que não pode dizer; e o que o Código de Defesa do Consumidor diz de publicidade enganosa. (c) **LGPD:** base
> legal e consentimento para captar um contato e repassá-lo a uma ou mais empresas; quem é controlador; direito de
> exclusão. (d) **WhatsApp Business:** política vigente da Meta sobre mensagens comerciais, opt-in e repasse de
> contato a terceiros. Cada seção termina dizendo se a pesquisa de 25/09 continua valendo ou foi corrigida. Fonte
> primária inacessível = "não conclusivo", nunca preenchido com fonte de segunda mão

### Conferência do portão

| Exigência | Resultado | Onde |
|---|---|---|
| Quatro seções (a)–(d) | sim | linhas 40, 155, 262, 346 |
| URL da fonte primária em cada seção | sim, com três defeitos | (a) dá só o caminho depois de `support.google.com`, sem o endereço inteiro; (b) o endereço da RDC 622 não abre como está (F2) e a CVS 9/2000 não tem endereço (F3) |
| Data de leitura | sim | 13/11/2026 em cada seção e no cabeçalho |
| Trecho curto que decide | sim | citações entre aspas em todas as seções |
| Veredito numa das quatro palavras | sim | quadro (linhas 22–36) e fim de cada seção |
| (a) gerador de leads pode ter perfil? | sim — vedado | linhas 50–60 |
| (a) endereço e atendimento | sim | linhas 62–82 |
| (a) perfil fora da regra | sim | linhas 84–100 |
| (a) caminhos legítimos | sim | linhas 102–129 |
| (b) RDC 622 na fonte oficial | sim (base de legislação da Anvisa) | linhas 158–159, 169–185 |
| (b) norma do estado | sim, em parte: Lei 10.083/1998 lida na Assembleia Legislativa; Portaria CVS 9/2000 em cópia de terceiro | linhas 162–164, 189–195 |
| (b) norma do município | sim | Lei 13.725/2004 e Portaria SMS 266/2025 |
| (b) CDC, publicidade enganosa | sim | linhas 202–215 |
| (c) base legal e consentimento | sim | linhas 271–286 |
| (c) quem é controlador | sim | linhas 288–294 |
| (c) direito de exclusão | sim | linhas 296–305 |
| (d) mensagens comerciais e opt-in | sim | linhas 359–372 |
| (d) repasse a terceiros | sim | linhas 374–391 |
| Cada seção termina com o estado da pesquisa de 25/09 | sim, nas quatro | linhas 141, 243, 336, 419 |
| Nenhum ponto preenchido com fonte de segunda mão | **não, em um ponto** | Portaria CVS 9/2000, item 10.4 (F3) |

## 2. Sorteio

**Método:** numerei as afirmações com citação entre aspas de cada seção, na ordem em que aparecem (21 em (a), 14
em (b), 11 em (c), 10 em (d)), e sorteei 3 por seção com `seq 1 N | shuf -n 3` (`shuf` do uutils coreutils 0.10.0,
semente do sistema), às 20:02:59. Saiu: (a) 2, 7, 19 · (b) 2, 3, 5 · (c) 2, 4, 7 · (d) 4, 7, 10.

| Nº | Afirmação do artefato | URL aberta | O que a fonte devolveu | Resultado |
|---|---|---|---|---|
| a2 | Lista "Ineligible businesses" traz "Lead generation agents or companies." | https://support.google.com/business/answer/13763036?hl=en | Título "Business eligibility and ownership guidelines". Seis itens na lista; o terceiro é "Lead generation agents or companies." Só "©2026 Google" como data, como o artefato diz. (1ª chamada: tempo esgotado; 2ª: sim) | OK |
| a7 | Coworking só se "maintains clear signage, receives customers at the location during business hours, and is staffed during business hours by your business staff" | https://support.google.com/business/answer/3038177?hl=en | Os dois pedaços estão na página, na frase sobre escritório em espaço de coworking | OK |
| a19 | "Within 7 business days of notice from an end customer" | https://support.google.com/business/answer/7353941?hl=en | "Within 7 business days of notice from an end customer, you must provide that client the ability to disassociate the…" | OK |
| b2 | RDC 622, art. 5º: "somente pode ser efetuada com empresa especializada" | endereço do artefato: erro "URL inválida"; endereço completo de `/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md` linha 25: abriu | "somente pode ser efetuada com empresa especializada." DOU 16/03/2022, Seção 1; marcada "Vigente" | OK no conteúdo; endereço com defeito (F2) |
| b3 | Art. 21: "somente é valida se for emitida por pessoa jurídica de direito privado" | idem | Texto idêntico (a página também grafa "valida"); o artigo continua vedando nota avulsa de pessoa física | OK no conteúdo; F2 |
| b5 | Art. 22, I: "não provocar temor, angústia ou utilizar expressões ou imagens sugerindo que a saúde das pessoas será ou poderá ser afetada por não usar produtos ou prestação de serviço" | idem | Texto idêntico, em dois pedaços | OK no conteúdo; F2 |
| c2 | LGPD, art. 7º, § 5º: "O controlador que obteve o consentimento […] que necessitar comunicar ou compartilhar dados pessoais com outros controladores deverá obter consentimento específico do titular para esse fim" | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | Texto idêntico. **O parágrafo continua:** "ressalvadas as hipóteses de dispensa do consentimento previstas nesta Lei." — ressalva que o artefato não transcreve (F6) | OK |
| c4 | Art. 8º, § 2º: "Cabe ao controlador o ônus da prova de que o consentimento foi obtido em conformidade com o disposto nesta Lei" | idem | Texto idêntico | OK |
| c7 | Art. 5º, VI: controlador é quem toma "as decisões referentes ao tratamento" | idem | "…a quem competem as decisões referentes ao tratamento de dados pessoais;" | OK |
| d4 | Automação permitida na janela, mas a empresa "must also have available prompt, clear, and direct escalation paths" | https://whatsappbusiness.com/policy/ | "You may use automation when responding during the 24-hour window, but must also have available prompt, clear, and direct escalation paths." | OK |
| d7 | "You are responsible for and must secure all necessary notices, permissions, and consents to collect, use, and share people's content and information" | idem | Texto idêntico (a página usa apóstrofo curvo) | OK |
| d10 | Política: "Last updated: September 23, 2026"; Termos da Meta: "Última atualização: 23 de setembro de 2026" | idem e https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform | As duas datas aparecem exatamente assim | OK |

**Contagem: 12 OK, 0 FALHA, 0 INCONCLUSIVO.**

### Trechos que decidem, conferidos além do sorteio (todos bateram)

| Trecho | Fonte | Resultado |
|---|---|---|
| "To qualify for a Business Profile, a business must make in-person contact…"; "Brands, organizations, artists, and other online-only businesses."; "Never claim a Business Profile without express consent…"; "Website content must be owned and managed by the business owner." | 13763036 | sim, os quatro |
| Telefone e site: "Do not provide phone numbers or URLs that redirect or "refer" users to landing pages or phone numbers other than those of the actual business" e "The phone number must be under the direct control of the business." | 3038177 | sim, os dois |
| "Sales associates or lead generation agents for corporations aren't individual practitioners" | 3038177 | sim |
| "Verbal consent isn't sufficient."; "all end customers must retain ownership or co-ownership…"; "After a profile has been created for a client, make the business owner the owner…"; "We may suspend a Business Profile and/or the Google Account you use to manage…" | 7353941 | sim, os quatro |
| "If a merchant's account is restricted, all Business Profiles associated with that account will be suspended."; "a pattern of violating…"; "Merchants that set their business address at a P.O. Box…"; a lista com "Lead generation agents or companies." | https://support.google.com/business/answer/13762416?hl=en | sim, os quatro |
| "paid for, directly or in kind"; "in exchange for posting any review or revision or removal of a negative review"; "selectively solicit positive reviews from customers"; "a contractual or consultory relationship" | https://support.google.com/contributionpolicy/answer/7400114?hl=en | sim, os quatro |
| "We may suspend or disable Business Profiles…"; "Appeals can only be submitted once."; "Do not create a new Business Profile for the same business." | https://support.google.com/business/answer/4569145?hl=en | sim, os três |
| Três restrições por avaliação falsa | https://support.google.com/business/answer/14114287?hl=en | sim; a página diz "for set period of time", sem prazo, como o artefato registra |
| "You can have up to 20 service areas."; cerca de 2 horas de carro | https://support.google.com/business/answer/9157481?hl=en | sim |
| RDC 622, art. 2º, art. 22 caput, II e III, art. 23 | base da Anvisa (endereço completo) | sim. O inciso II termina com "exceto nos casos especificamente determinados pela Anvisa", que o artefato não cita |
| As palavras "intermediário", "anunciante" e "site" não aparecem na RDC 622 | idem | confirmado (uma chamada) |
| Lei 6.437/1977, art. 3º: "a quem lhe deu causa ou para ela concorreu" | https://www.planalto.gov.br/ccivil_03/leis/l6437.htm | sim |
| Lei estadual 10.083/1998, art. 122, XV, e art. 111; Lei municipal 13.725/2004, art. 129, XV, e art. 117 | endereços do artefato | sim nos quatro; nenhuma das duas menciona controle de pragas |
| CDC, arts. 36, 37 (caput, §§ 1º, 2º, 3º), 38, 7º parágrafo único, 34 | https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | sim, os oito trechos |
| LGPD, art. 5º, XII; art. 8º, §§ 1º, 4º, 5º; art. 18, VI, VII e § 6º; art. 42, § 1º, II | Planalto | sim. O art. 18, § 6º, termina com "exceto nos casos em que esta comunicação seja comprovadamente impossível ou implique esforço desproporcional" (F6) |
| Lei 15.352/2026 como última alteração da LGPD | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm | existe (25/02/2026); altera o art. 5º, VIII e XIX, e os arts. 55-A e 55-C. Os incisos usados no artefato (II, VI, XII) não foram alterados. O texto do Planalto grafa "15.452" no art. 55-A com link para a 15.352 (erro da página) |
| Cláusula 4.1(b) dos Termos da Meta, em português | https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform | texto idêntico ao do artefato; a definição entre parênteses de "Dados da Plataforma" está na alínea (a); a seção 4 não traz exceção por consentimento |
| Regra de opt-in: "You may only contact people on WhatsApp if: (a)… and (b)…" | https://whatsappbusiness.com/policy/ | frase inteira idêntica |
| "You must not impersonate another business…"; "You may not forward or otherwise share information from a customer chat with any other customer."; "…reasonably necessary to support messaging with that person"; opt-out | idem | sim |
| Opt-in tem de dizer o nome da empresa | https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in | "Businesses must clearly state the business's name that a person is opting in to receive messages from." A página nada diz sobre opt-in colhido por terceiro |
| Link `wa.me` e mensagem pré-preenchida | https://faq.whatsapp.com/5913398998672934 | sim |
| Termos do aplicativo: vigentes desde 23/09/2026; sem cláusula sobre repasse; sem a palavra "lead" | https://www.whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App | "Effective September 23, 2026."; nenhuma cláusula sobre venda ou repasse de contato a terceiro; incorpora a Política de Mensagens |
| Portaria CVS 9/2000, item 10.4 | cópia `.doc` em `drive.prefeitura.sp.gov.br` (endereço só no anexo `00b_propaganda.md`, linha 96) | o texto do item 10.4 bate com o artefato; o arquivo não diz quem o publicou nem traz indicação de vigência |

**Não conferido:** `support.google.com/business/answer/3403100` (listada como fonte, sem citação no artefato);
Resolução CD/ANPD nº 2/2022; Agenda Regulatória da ANPD; Portaria SMS 266/2025; política comercial da Meta; página
de preços da API; redirecionamento dos endereços antigos da política do WhatsApp.

## 3. Vereditos — decorrem do trecho?

| Linha do quadro | Decorre? | Observação |
|---|---|---|
| (a) perfil próprio — vedado | sim | dois itens da lista de inelegíveis e a condição de contato presencial |
| (a) endereço de fachada — vedado | sim | caixa postal, escritório virtual e coworking têm frase própria |
| (a) perfil da licenciada com telefone ou site do intermediário — vedado | sim | regra de telefone e site (3038177) e "Website content must be owned…" (13763036) |
| (a) administrar o perfil da licenciada — permitido com condição | sim | cada condição tem trecho, **menos "nenhuma promessa de posição"**, que entra sem citação nem página (F8) |
| (a) avaliação comprada ou de quem tem vínculo — vedado | sim | 7400114 |
| (b) site de terceiro divulga licenciadas — permitido com condição | **por inferência** | a RDC se dirige às "empresas especializadas" e é silente sobre terceiro, como o próprio artefato diz. "Permitido" é ausência de vedação; as condições vêm de aplicar o art. 22 por prudência e do CDC. O artefato reconhece isso na linha 250, mas o quadro não marca |
| (b) página sem nomear a executora — não conclusivo | sim | coerente com "norma silente" |
| (c) repasse a uma empresa — permitido com condição | sim | art. 7º, § 5º, e art. 8º, §§ 1º e 4º |
| (c) repasse a várias — permitido com condição | **em parte** | ver item (iv) abaixo (F5) |
| (c) só legítimo interesse — não conclusivo | sim | guia não lido; mas a ressalva final do § 5º, que é o que abre essa hipótese, não foi transcrita (F6) |
| (d) triagem e repasse pela API — vedado pela letra | sim, com ressalva incompleta | ver item (i) abaixo (F4) |
| (d) o mesmo pelo aplicativo — não conclusivo | sim | termos do aplicativo sem cláusula sobre repasse (conferido) |
| (d) botão abre o WhatsApp da licenciada — permitido com condição | sim, apoiado só em leitura [S] | o recurso é oficial (conferido); a "condição" não está enunciada de forma precisa no quadro |

Não achei "silente" usado onde a fonte fala, salvo o caso do CDC (F1).

**(i) "Vedado pela letra" no repasse pela API.** A cláusula diz o que o artefato transcreve, e não há exceção por
consentimento na seção 4. O alcance, porém, depende de ler "dados obtidos com o uso da Plataforma" como abrangendo
o nome, o telefone e o pedido que a própria pessoa informa na conversa; os termos não dizem isso expressamente, e
a definição é só um parêntese na alínea (a). A Política de Mensagens, que vale também para a API, fala em obter
consentimentos para "collect, use, and share" informações das pessoas, o que não combina com proibição absoluta.
O artefato registra uma ressalva (linhas 381–382: exceção em outro documento não conferida), mas **não** registra
essas duas, e o quadro traz "Vedado" sem ressalva alguma. O veredito se sustenta como leitura literal; falta
dizer que é leitura literal de alcance não definido.

**(ii) Variante por formulário, seção (d).** Está marcada como "inferência, não frase da fonte" (linha 403).
Confirmei que a documentação de opt-in nada diz sobre opt-in colhido por terceiro. **Porém** o resumo final
(linha 432) lista o formulário entre o que fica de pé sem repetir a marca de inferência, e a variante não aparece
no quadro de vereditos.

**(iii) Conclusões para o site, seção (b).**
- (i) número da licença e órgão: art. 22, caput — sim. Razão social: só a CVS 9/2000 a pede com essa palavra (o
  art. 22 fala em "identificação dela nos órgãos licenciadores"); o artefato não diz de onde vem. Endereço: CVS
  9/2000, marcado "por prudência" — mas depende do ponto reprovado (F3). Marca de publicidade: art. 36, por
  aplicação.
- (ii) medo, selos e "seguro/atóxico": art. 22, I a III — sim. **"Sem risco para crianças e animais"** e os
  exemplos **"24 horas", "garantia", "melhor preço"** não estão em nenhuma fonte; o CDC não proíbe dizê-los, exige
  guardar a prova (art. 36, parágrafo único) e põe o ônus em quem patrocina (art. 38). Está sob o título "Não pode
  dizer", o que diz mais do que a fonte (F7).
- (iii) "tem de ficar claro quem é o site": **nenhum artigo citado**. É inferência do art. 37 (omissão) e dos
  arts. 5º e 21 da RDC; "nada de 'nossa equipe'" é escolha de desenho (F7).
- (iv) pontos silentes: coerente.

**(iv) "Várias empresas", seção (c).** Três problemas: o quadro põe como condição "dizer a quantas e **a quais**",
e o corpo (linha 321) diz que não é conclusivo se "até N empresas" sem nome basta — contradição interna; "sem
revenda posterior" (linha 328) não aponta artigo; e "vender o mesmo contato a muitas empresas […] fica fora"
(linha 334) vai além da lei, que não fixa número, e contradiz o veredito "permitido com condição". O resumo final
(linha 436) usa a formulação correta: "sem que a pessoa saiba quais".

## 4. Classe de evidência e "quem ganha"

- Declaradas no cabeçalho (linhas 6–8): classe A para tudo entre aspas; quem ganha = plataforma em (a) e (d),
  Estado em (b) e (c). Não achei blog, agência nem vendedor entre as fontes.
- **A frase geral é falsa para um item:** a citação do item 10.4 da CVS 9/2000 está entre aspas e **não** foi lida
  na página oficial do órgão emissor.
- **CVS 9/2000 descrita honestamente? Em parte.** O artefato diz "cópia oficial hospedada pela Prefeitura",
  "cópia oficial em terceiro" e "vigência não confirmada". Faltam: o endereço (só está no anexo); que o arquivo
  não identifica quem o publicou (é um `.doc` numa pasta de arquivos da secretaria de abastecimento) — "oficial"
  diz mais do que se sabe; e que o anexo registra acentos corrompidos e trecho truncado no meio.
- A marca [S] cobre 30 pontos lidos só pelo subagente; os que reabri bateram.

## 5. Afirmações factuais sem URL ou sem artigo

1. Portaria CVS 9/2000: sem URL (linhas 163–164).
2. "Portaria CVS 1/2024 (republicada pela última vez em 15/10/2026)" (linha 198): sem URL.
3. "glossário e perguntas frequentes da ANPD" (linha 269): sem URL; sustenta "prazo geral ainda não fixado".
4. "política comercial da Meta" (linha 391): sem URL.
5. Mensagem de serviço gratuita só até 1.000 por número por mês desde 01/10/2026 (linhas 414–416): sem URL.
6. Termos comuns do WhatsApp que vedam vender "dados obtidos de nós" (linha 416): sem URL.
7. "nenhuma promessa de posição" (linha 123): sem página nem trecho.
8. Regra da janela de 24 horas e do modelo aprovado (linha 369): sem URL própria.
9. Resolução CD/ANPD nº 2/2022 (linhas 309–312): sem número de artigo.
10. Elementos do texto de consentimento sem artigo (linhas 319–324): identificação e contato do controlador,
    possibilidade de recusar, prazo de guarda.
11. "a versão em português avisa que pode ter tradução automática" (linha 48) e o redirecionamento dos endereços
    antigos (linhas 350–351): sem evidência registrada.
12. Conclusão (iii) da seção (b), inteira: sem artigo.

Os endereços de 2 a 6 existem nos anexos; falta trazê-los para o artefato.

## 6. Pesquisa antiga — remissões conferidas

| Remissão | A linha diz isso? |
|---|---|
| `research/03`, linha 13 (inelegível; "restrito a orgânico + Ads") | sim |
| `research/03`, linha 102 (fontes 13763036 e 3038177) | sim |
| `research/03`, linha 103 (endereço oculto; "principal causa de suspensão" vinda de agência) | sim |
| `research/03`, linha 167 ("consentimento explícito… até N empresas") | sim |
| `research/03`, linha 88 (número próprio ou API que faz a triagem e encaminha) | sim |
| `research/03`, linha 108 ("controlar o número de telefone") | **impreciso**: a expressão está na linha 42 (e nas 87 e 91); a 108 diz que o ativo fica "no site e no telefone" e não manda pôr o número do intermediário no perfil da parceira |
| `research/01`, linha 44 (art. 22) | sim |
| `research/01`, linha 156 (art. 21, "PJ que executa") | sim |
| `research/01`, linha 157 ("vale para o texto do site", Alta) | sim |
| `research/01`, linha 163 ("cadeia de fornecimento") | sim |

Caminhos completos: `/home/ancastelo/pessoal/SEO_Project/research/03_modelos_negocio_escala.md` e
`/home/ancastelo/pessoal/SEO_Project/research/01_regulacao_licencas.md`.

## 7. Forma

- Português: sim. Aviso "levantamento, não parecer": sim (linha 4).
- Caminhos absolutos: sim nos arquivos do projeto.
- Nome de pessoa física: nenhum.
- Número com unidade e data: sim (20 áreas, 2 horas, 7 dias úteis, 15 dias, 1.000 mensagens por mês).
- "linha 2.12" de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00x_metodo_do_exemplo_x.md` é o número da
  tática na tabela; a linha do arquivo é a 46.

## 8. Falhas e correção sugerida

| Nº | Falha | Correção |
|---|---|---|
| F1 | **Afirmação errada (linhas 213–214):** "O CDC não usa as palavras 'intermediário' nem 'cadeia de fornecimento'". A palavra "intermediário" está no caput dos arts. 54-B e 54-D (duas chamadas concordam); "cadeia de fornecimento" de fato não aparece | Trocar por: o CDC só usa "intermediário" nos arts. 54-B e 54-D, sobre oferta de crédito, fora do tema; "cadeia de fornecimento" não aparece. Conferir a mesma frase no anexo `00b_propaganda.md` |
| F2 | **Endereço da RDC 622 não abre como está (linha 159):** três tentativas devolveram "URL inválida. Acesse o sistema novamente" | Usar o endereço completo de `research/01_regulacao_licencas.md` linha 25 (termina em `&cod_menu=9434&cod_modulo=310&pesquisa=true`), que abriu duas vezes |
| F3 | **Ponto reprovado — Portaria CVS 9/2000 (linhas 163–164, 189–191, 220, 431):** fonte primária inacessível preenchida com cópia de terceiro, entre aspas, sem URL, chamada "oficial", e levada à conclusão e ao resumo final ("endereço") | Marcar a norma estadual específica de propaganda como **não conclusivo**; citar a cópia como indício, com o endereço e sem "oficial"; excluir essa citação da frase geral de classe A; no resumo final, pôr o endereço da empresa como prudência, não como exigência |
| F4 | Quadro traz "Vedado" na API sem ressalva; faltam duas ressalvas de alcance | Acrescentar ao quadro "leitura literal; alcance sobre o que a pessoa informa na conversa não definido" e registrar a tensão com a frase "collect, use, and share" da Política de Mensagens |
| F5 | Seção (c), "várias empresas": contradição entre quadro e corpo; "sem revenda posterior" sem artigo; "muitas empresas fica fora" além da lei | Alinhar o quadro ao corpo ("a quantas; se nomear é obrigatório, não conclusivo"); marcar "sem revenda" como inferência do § 5º; reescrever a linha 334 como na linha 436 |
| F6 | Citações cortadas antes da ressalva: art. 7º, § 5º; art. 18, VI e § 6º; art. 42, § 1º, II (LGPD); art. 22, II (RDC) | Transcrever ou mencionar cada ressalva; a do § 5º e a do § 6º mudam condição do desenho |
| F7 | Conclusões (ii) e (iii) da seção (b) com exemplos e exigências sem trecho | Citar o artigo de cada exigência; mover os exemplos sem fonte para "escolha de desenho"; trocar "não pode dizer" por "só com prova guardada" onde a base é o CDC |
| F8 | Afirmações sem URL ou artigo (lista da seção 5) | Trazer os endereços dos anexos; citar página e trecho de "nenhuma promessa de posição" ou retirar |
| F9 | Menores: endereços de (a) sem domínio; remissão à linha 108; marca de inferência ausente na linha 432 e no veredito (b) do quadro | Ajustar |

## 9. Registro de conteúdo de página tratado como dado

A ferramenta de leitura informou que a página dos Termos da Meta para a Plataforma do WhatsApp Business contém,
perto da cláusula 4.7, uma frase em inglês pedindo para repetir um texto e não traduzir um "segmento". Não faz
parte dos termos nem do pedido desta verificação; foi ignorada e fica aqui registrada.
