# Verificação independente — fila de reserva, item 4 (pontos de um contrato de venda de leads)

- **Artefato conferido:** `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` (391 linhas, lido inteiro, linha a
  linha; gravado às 22:56 de 13/11/2026).
- **Quando:** sexta, 13/11/2026. Início às 22:58 (lido de `TZ=America/Sao_Paulo date`: 22:58:47); última leitura de
  fonte às 23:09 (`date`: 23:09:47); redação deste arquivo a partir de 23:10 (`date`: 23:10:35), Brasília.
- **Quem:** verificador em contexto limpo; não recebi a conclusão de quem produziu. Não editei o artefato nem outro
  arquivo; este é o único arquivo gravado.
- **Como li a web:** só a ferramenta de leitura de página (35 leituras em 29 endereços; uma caiu e foi repetida; nenhuma busca). Ela corta a
  citação literal em cerca de 125 caracteres (confirmei: ela mesma avisa) e resume o resto; pedi os artigos em trechos
  consecutivos. Não usei navegador, não baixei arquivo, não criei conta, não preenchi formulário, não contatei ninguém.
  **Página que pediu ação: nenhuma.**
- **Natureza:** conferência de levantamento com fonte. Nada aqui é parecer jurídico.

## Veredito

**APROVADO COM RESSALVAS.**

- Portão: cumprido (os quatro pontos nomeados estão tratados, com fonte; é levantamento, não minuta; diz que não é
  parecer).
- Sorteio: **1 falha em 12** (limite: 2); nenhum inconclusivo.
- Fora do sorteio: **um erro de conteúdo** (linha 91: o art. 711 do Código Civil é lido ao contrário), ressalvas de lei
  cortadas, quatro conclusões jurídicas escritas como fato, a seção 14 anunciada como "veredito já fechado" quando parte
  das linhas não é, e um termo entre aspas que a página não traz. Nenhuma sugestão de coisa vedada pelo quadro do item 2.
- As 20 correções estão no fim; as 9 primeiras são as que pesam.

---

## 1. Portão

Texto do portão (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linhas 74–75, lido): "Levantamento
dos pontos de um contrato de venda de leads (região, exclusividade, preço, disputa de lead inválido), com fonte;
levantamento, não minuta para assinar."

| Exigência | Onde está no artefato | Confere? |
|---|---|---|
| Região, com fonte | Seção 2 (linhas 76–82): Lei 4.886, art. 27, d; CC, art. 710; RDC 622, arts. 3º e 4º; CDC, arts. 30 e 37; termos de Angi, Service Direct, Google | Sim |
| Exclusividade, com fonte | Seção 3 (linhas 86–94): CC, arts. 711, 726, 421, 421-A, 598, 412, 413; Lei 4.886, arts. 27 e 31; Lei 12.529, art. 36 | Sim (com o erro da linha 91) |
| Preço, com fonte | Seção 4 (linhas 98–105): CC, arts. 597, 394, 395, 406, 412, 476; Lei 10.192; LC 116; termos de oHub, GetNinjas, Service Direct, 99 Calls | Sim |
| Disputa de lead inválido, com fonte | Seção 5 (linhas 109–142): tabela motivo a motivo e cinco pontos, com os termos de seis plataformas | Sim |
| Levantamento, não minuta | Busquei redação de cláusula ("as partes acordam/convencionam/declaram", "fica eleito", "obriga-se", "compromete-se", "CLÁUSULA"): **nenhuma ocorrência**. As colunas descrevem pontos e perguntas | Sim |
| Diz que não é parecer | Linhas 5–9 ("Não é minuta para assinar e não é parecer jurídico"; "o arquivo não conclui") | Sim |

## 2. Sorteio de 12 afirmações com fonte externa

**Método (reproduzível).** Unidade = cada trio (linha do artefato, coluna da tabela, código de fonte) nas linhas 65 a
273, isto é, cada célula que traz um código `L…` ou `P…` entre colchetes, uma unidade por código distinto na célula
(linha de prosa conta como coluna 0). Numeração na ordem do arquivo, por um script de `python3` que percorre as linhas,
separa as células por ` | ` e colhe os códigos dentro de `[...]`. Resultado: **137 unidades — 57 de lei, norma ou órgão
(L-001 a L-057) e 80 de plataforma (P-001 a P-080)**. Sorteio estratificado (8 de lei, 4 de plataforma), semente
**20261113**:

```
seq 1 57 | shuf --random-source=<(yes 20261113) | head -8    # 51 50 53 4 6 1 10 34   (reservas: 9 29 3 44 18 54)
seq 1 80 | shuf --random-source=<(yes 20261113) | head -4    # 51 50 53 58            (reservas: 5 55 56 57 60 10)
```

(`shuf (uutils coreutils) 0.10.0`.) Para cada unidade conferi **tudo** o que a célula atribui àquela fonte. Nenhuma
reserva foi usada: todas as 12 fontes abriram.

| # | Unidade | Afirmação do artefato | Fonte aberta | O que a fonte diz | Resultado | Classe correta? |
|---|---|---|---|---|---|---|
| 1 | L-051 · linha 220 · L3 | CC, art. 473 e parágrafo único (denúncia; investimentos consideráveis); art. 599 (aviso de oito dias, serviço pago por mês); art. 720 (agência por tempo indeterminado: noventa dias) | planalto.gov.br, Código Civil compilado (caracteres 100.000–200.000) | Art. 473, p. único: "a denúncia unilateral só produzirá efeito depois de transcorrido prazo compatível com a natureza e o vulto dos investimentos". Art. 599, p. único, I: "com antecedência de oito dias, se o salário se houver fixado por tempo de um mês, ou mais". Art. 720: "mediante aviso prévio de noventa dias, desde que transcorrido prazo compatível com a natureza e o vulto do investimento exigido do agente" | **Confere** (a condição final do art. 720 ficou de fora: correção 18) | A, sim |
| 2 | L-050 · linha 219 · L3 | CC, art. 598: prestação de serviço por no máximo quatro anos | idem | "A prestação de serviço não se poderá convencionar por mais de quatro anos" | **Confere** | A, sim |
| 3 | L-053 · linha 221 · L1 | "Mantê-la com o nome dela depois da saída: propaganda de empresa que não autorizou e informação que deixou de ser verdadeira (CDC, arts. 30 e 37, § 1º — resumo)" | planalto.gov.br, CDC compilado | Art. 30: informação ou publicidade suficientemente precisa "obriga o fornecedor que a fizer veicular ou dela se utilizar e integra o contrato". Art. 37, § 1º: é enganosa a informação falsa ou capaz de induzir em erro, "mesmo por omissão". Nenhum dos dois fala de página mantida depois do fim de um contrato nem de "propaganda de empresa que não autorizou" | **Falha**: os artigos existem e têm esse número, mas a frase é aplicação ao caso (inferência de quem escreveu) marcada como "resumo" do artigo | A, sim |
| 4 | L-004 · linha 71 · L3 | CC, art. 422: boa-fé na formação e na execução (resumo) | planalto.gov.br, Código Civil | "Os contratantes são obrigados a guardar, assim na conclusão do contrato, como em sua execução" (probidade e boa-fé) | **Confere** | A, sim |
| 5 | L-006 · linha 80 · L10 | Lei 4.886, art. 27, d: "indicação da zona ou zonas em que será exercida a representação" | planalto.gov.br, Lei 4.886 | Texto idêntico; alínea com redação da Lei 8.420/1992 | **Confere** | A, sim |
| 6 | L-001 · linha 69 · L3 | CC, art. 425 (contrato atípico, citação); art. 594 (citação); art. 710 (agência, resumo); art. 722 (corretagem, resumo) | planalto.gov.br, Código Civil | Art. 425: "É lícito às partes estipular contratos atípicos, observadas as normas gerais fixadas neste Código." Art. 594: "Toda a espécie de serviço ou trabalho lícito, material ou imaterial, pode ser contratada mediante retribuição." Art. 710: agência, "em caráter não eventual e sem vínculos de dependência" (início literal; o resto resumido pela ferramenta). Art. 722: corretagem, "não ligada a outra em virtude de mandato, de prestação de serviços" | **Confere** | A, sim |
| 7 | L-010 · linha 90 · L3 | CC, art. 711 (citação e resumo); art. 726 (resumo); art. 421 (citação); art. 421-A (citação) | planalto.gov.br, Código Civil | Art. 711: "Salvo ajuste, o proponente não pode constituir, ao mesmo tempo, mais de um agente, na mesma zona, com idêntica incumbência; nem pode o agente assumir o encargo de nela tratar de negócios do mesmo gênero, à conta de outros proponentes." Art. 421 e art. 421-A: texto idêntico ao citado, redação da Lei 13.874/2019. Art. 726: se a corretagem com exclusividade for ajustada por escrito, o corretor tem direito à remuneração integral mesmo sem mediar | **Confere** (o resumo do art. 726 é frouxo: correção 13) | A, sim |
| 8 | L-034 · linha 168 · L14 | Página da ANPD: "a comunicação à ANPD e ao(s) titular(es) deverá ser realizada pelo controlador no prazo de três (3) dias úteis" e "o operador deverá informar o fato, sem demora injustificada, ao controlador dos dados" | gov.br/anpd, comunicado de incidente de segurança | As duas frases aparecem, literais; a página cita os arts. 6º e 9º da Resolução CD/ANPD 15/2024; publicada em 23/12/2022, modificada em 26/08/2026 (datas iguais às do artefato) | **Confere** | A, sim |
| 9 | P-051 · linha 178 · P2 | Termos do aplicativo WhatsApp Business: "Company is responsible for all activities occurring under its account." e "Company may only allow authorized individuals acting on behalf of Company" | whatsapp.com/legal/WhatsApp-Terms-for-WhatsApp-Business-App | As duas frases aparecem; "Effective September 23, 2026" | **Confere** | A, sim |
| 10 | P-050 · linha 165 · P5 | oHub, cl. 3.7: sigilo sobre dados de outros usuários; não "divulgar ou vender para qualquer terceiro" | ohub.com.br/termos (abriu na segunda tentativa; a primeira caiu) | Cl. 3.7: "Comprometer-se a não divulgar ou vender para qualquer terceiro" informação obtida no site sobre outro usuário, tratada como sigilosa. Sem data; rodapé "2026" | **Confere** | A (sobre si), sim |
| 11 | P-053 · linha 179 · P2 | Termos do aplicativo: "we have the right to limit, throttle, suspend, or terminate Company’s account."; "at any time and for any reason, permissible by applicable law."; "Company will not create another WhatsApp business account without our express written permission." | idem 9 | As três aparecem (as duas primeiras são trechos de frases mais longas) | **Confere** | A, sim |
| 12 | P-058 · linha 194 · P4 | oHub devolve crédito ao prestador e não trata do consumidor | ohub.com.br/politica-contato-garantido-termos | Fala em "devolução de créditos" ao fornecedor; pedido só pela plataforma; não define garantia alguma ao comprador | **Confere** | A (sobre si), sim |

**Placar: 11 conferem, 1 falha, 0 inconclusivo.** As datas que a tabela de fontes dá para L1, L3, L10, L14, P2, P4 e P5
bateram com o que a ferramenta devolveu.

## 3. Conferências obrigatórias (fora do sorteio)

### (a) CDC — planalto.gov.br, texto compilado

| Artigo | O que o artefato atribui (linha) | O que o texto diz | Confere? |
|---|---|---|---|
| 7º, p. único | "Tendo mais de um autor a ofensa, todos responderão solidariamente pela reparação" (195) | Idêntico; continua "dos danos previstos nas normas de consumo" | Sim |
| 14 | Responsabilidade do fornecedor de serviços sem culpa; § 3º: só se exime provando que o defeito inexiste ou culpa exclusiva do consumidor ou de terceiro (193) | Caput e § 3º, I e II, dizem isso | Sim |
| 18 | Trata de **produto**; citação "Os fornecedores de produtos de consumo duráveis ou não duráveis respondem solidariamente" (194) | Idêntico. A observação de que o equivalente para serviço é o art. 20 está certa | Sim |
| 20 | Vício de qualidade do serviço; disparidade com oferta ou publicidade; reexecução, devolução ou abatimento (194) | Caput e incisos I a III dizem isso | Sim |
| 25 | Caput: vedada a cláusula que "impossibilite, exonere ou atenue a obrigação de indenizar"; § 1º: "Havendo mais de um responsável pela causação do dano, todos responderão solidariamente" (195, 196) | Idêntico | Sim no texto; a aplicação nas linhas 57 e 196 vai além (seção 4) |
| 34 | "O fornecedor do produto ou serviço é solidariamente responsável pelos atos de seus prepostos ou representantes autônomos." (197) | Idêntico | Sim |
| 36 | Caput (identificação da publicidade) e p. único ("manterá, em seu poder," os dados) (152, 154) | Idênticos | Sim |
| 37 | § 1º: enganosa a que induz em erro, mesmo por omissão (81, 221) | Diz isso | Sim no texto; na linha 221 a frase é inferência (sorteio, nº 3) |
| 38 | "O ônus da prova da veracidade e correção da informação ou comunicação publicitária cabe a quem as patrocina." (152) | Idêntico | Sim |
| Também lidos | Art. 2º ("destinatário final", 141); art. 3º e § 2º ("mediante remuneração", 192); art. 30 (81, 155) | Batem | Sim |

A nota de data de L1 (alteração mais recente vista: MP 1.393/2026, no art. 57) confere.

### (b) LGPD — planalto.gov.br (primeiros 100.000 caracteres)

| Dispositivo | O que o artefato atribui | O que o texto diz | Confere? |
|---|---|---|---|
| Art. 7º, § 5º | "Compartilhar com outro controlador pede consentimento específico" (165) | "O controlador que obteve o consentimento referido no inciso I do caput" e precisa comunicar ou compartilhar com outros controladores obtém consentimento específico, **ressalvadas as hipóteses de dispensa do consentimento previstas na lei** | **Em parte**: número certo; o resumo corta a quem a regra se dirige e a ressalva (correção 5) |
| Art. 18, § 6º | O responsável informa "de maneira imediata" os agentes com quem compartilhou, "para que repitam idêntico procedimento" (167) | Diz isso, e termina com a exceção: comunicação comprovadamente impossível ou de esforço desproporcional | **Em parte**: a exceção foi cortada; [R], linhas 330–331, a traz (correção 6) |
| Art. 42 | § 1º, II: controladores diretamente envolvidos "respondem solidariamente"; § 1º, I: operador; § 4º: regresso; art. 43: exclusões (169, 290) | Bate, inciso por inciso | Sim |
| Art. 48 | "O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança" que possa acarretar risco ou dano relevante (168) | Idêntico; o § 1º fala em prazo razoável definido pela autoridade | Sim |
| Também lidos | Art. 5º, VI e VII; art. 6º, I; arts. 15, 16 e 37; Resolução CD/ANPD 2/2022, arts. 9º, 11, § 1º, e 14, II (com a redação que remete à Resolução 15/2024); glossário da ANPD, verbete de controladoria conjunta | Batem; as datas de L13 e L15 conferem | Sim |

Sobre **"controladores conjuntos"**: o artefato não conclui (linhas 164 e 313: "não conclusivo"; guia em PDF, não
lido). A citação do glossário confere ("Determinação conjunta, comum ou convergente, por dois ou mais controladores,
das finalidades e dos elementos essenciais"); o verbete remete ao guia de agentes de tratamento, versão 2.0, de 2022.

### (c) Marco Civil, art. 15 — planalto.gov.br

- **O que o artigo diz:** "O provedor de aplicações de internet constituído na forma de pessoa jurídica e que exerça
  essa atividade" de forma organizada, profissionalmente e com fins econômicos mantém os registros de acesso a
  aplicações, sob sigilo, em ambiente controlado e de segurança, por seis meses, **nos termos do regulamento** (o fim é
  resumo da ferramenta). O § 1º permite que ordem judicial obrigue, por tempo certo, os provedores **não** sujeitos ao
  caput; o art. 17 diz que "a opção por não guardar os registros de acesso a aplicações de internet não implica
  responsabilidade" por dano de terceiros.
- **A quem se aplica:** só ao provedor de aplicações que é pessoa jurídica e exerce a atividade de forma organizada,
  profissional e com fins econômicos.
- **O artefato afirma mais do que leu? Não.** Linha 163 reproduz os três requisitos; linhas 53–54 dizem "certo tipo de
  provedor" e "**pode** conflitar"; linha 306 diz "só é conflito se o site for esse provedor". Não afirma que o site é
  esse provedor.
- **O que falta:** (i) "nos termos do regulamento" foi omitido, e o regulamento não foi lido nem aparece em "Não sei";
  (ii) o § 1º e o art. 17, que tratam justamente de quem não está no caput, não são citados; (iii) o ponto está em
  "Disputado (as fontes divergem)", mas não há duas fontes divergindo: há uma lei e uma premissa do desenho — é "não
  sei". Correção 8.
- A nota de L7 (redações da medida provisória de 2021 marcadas como rejeitadas) confere.

### (d) Código Civil — planalto.gov.br (caracteres 0 a 300.000, em três leituras)

| Tema | Artigos | Números e conteúdo batem? |
|---|---|---|
| Contrato atípico | 425 | Sim |
| Prestação de serviço | 594, 597, 598, 599 | Sim. Na linha 102, "o pré-pago tem de estar escrito" vai além do art. 597, que admite adiantamento "por convenção, ou costume" (correção 11) |
| Agência | 710, 711, 720 | Números e texto, sim. **Erro na linha 91** (abaixo) |
| Corretagem | 722, 726 | Sim; resumo do 726 frouxo (correção 13) |
| Outros citados | 265, 283, 285, 394, 395, 406 (redação da Lei 14.905/2024), 412, 413, 421, 421-A (Lei 13.874/2019), 422, 473, 476, 934 | Todos batem, com as redações que a tabela de fontes declara |

**Erro da linha 91.** O artefato diz: "Sem ajuste: na agência, quem fica preso é o agente, não o proponente (art. 711 —
resumo)". O art. 711 prende **os dois**: o proponente "não pode constituir, ao mesmo tempo, mais de um agente, na mesma
zona, com idêntica incumbência", e o agente não pode tratar ali de negócios do mesmo gênero para outros proponentes. A
linha 91 contradiz o texto da lei e contradiz o próprio artefato (linhas 38 e 90: "recíproca salvo ajuste"). Na
pergunta da linha ("a licenciada pode anunciar em outros sites?"), a licenciada estaria no lugar do proponente — o lado
que a linha diz estar livre.

Representação comercial (Lei 4.886, arts. 1º, 2º, 27, d, e, j, 31, p. único, e 34): tudo bate. A linha 35 diz que o
Código Civil "tem quatro tipos vizinhos", mas a representação comercial está em lei própria (correção 10).

### (e) RDC 622/2022, art. 22, e Lei 6.437/1977, art. 3º

- **RDC 622** (base da Anvisa, endereço completo de L12; "Vigente"; resolução de 09/03/2022, DOU de 16/03/2022): art.
  22, caput, "toda e qualquer forma de propaganda de empresa especializada deve conter claramente a identificação dela"
  e o número da licença; incisos I a III como o artefato descreve. Também conferidos: art. 3º, III e VI; art. 4º
  ("junto à autoridade sanitária e ambiental competente") e parágrafo único; art. 5º ("somente pode ser efetuada com
  empresa especializada"); art. 19, XI ("números das licenças sanitária e ambiental com seus respectivos prazos de
  validade"); art. 21; art. 23. **Tudo confere.**
- **Lei 6.437**, art. 3º: "O resultado da infração sanitária é imputável a quem lhe deu causa ou para ela concorreu.";
  § 1º: "Considera-se causa a ação ou omissão sem a qual a infração não teria ocorrido." **Confere**; a nota sobre o
  art. 10, V (MP 2.190-34/2001) também.

### Outras fontes abertas fora do sorteio (todas bateram, salvo o anotado)

Lei 12.529, art. 36 (caput, I, IV, § 2º, § 3º, I, c, e VI); Lei 10.192, arts. 1º e 2º; LC 116, art. 1º e subitens
1.09, 10.02, 10.08, 17.06, 17.25; Lei 9.610, arts. 4º, 7º, I e VII, 22, 29, 50, 79, § 1º; Lei 9.279, arts. 129, 130,
139, 140, 195, XI; P1 (três frases; "Last updated: September 23, 2026"); P3 (cláusulas 4a, 5c, 7d, 9a, 13c, 15b, 16b,
17b, 21a; rodapé "©2011-2024"); P6; P7; P8; P9; P10; P11; P12; P13; P14.

- **P6, linha 69:** o termo entre aspas "Billable Lead" **não aparece** na página; ela usa "Billable Call" e "Billable
  Call Leads" (correção 9).
- **P6, linha 70:** a frase citada não termina em "provides."; continua "or any call that results in a Booked
  Appointment" (correção 9).
- **P7, linha 140:** a página da Service Direct não diz que a decisão é "pela gravação"; exige gravação ativada e diz
  que a equipe de qualidade analisa (correção 17).
- **P12, linha 129:** a página dá um critério (não conseguir o cliente ou o trabalho); o que falta é prazo e percentual
  (correção 17).
- **P13:** a página traz duas datas ("Last updated June 2026" numa seção e "Last updated October 2026" no fim); o
  artefato registra a segunda. Sem efeito.

## 4. Varredura do arquivo inteiro

| O que procurei | O que achei |
|---|---|
| Afirmação sem fonte | Nenhuma que decida algo. Duas observações de quem escreveu sem marca: linha 222 ("cópias em cache e em respostas de IA estão fora do controle do site") e linha 51 ("na via A o contrato quase não tem o que dizer") |
| Conclusão jurídica como fato — responsabilidade perante o consumidor | Linhas 56–57 ("O que a lei diz **com certeza** é que cláusula **entre as partes** não afasta…") e linha 196, última coluna ("O contrato entre site e licenciada não muda o que o consumidor pode cobrar; só pode tratar de regresso"): o art. 25 diz o que está na citação; aplicá-lo ao contrato entre duas empresas é leitura. Linha 72: "CDC, art. 30, vale para a oferta ao consumidor, **não entre as empresas**" — o próprio artefato diz o contrário nas linhas 141 e 321 (se o CDC alcança a licenciada: "não levantado"). Linha 192: "O site não cobra do consumidor" está na coluna "O que a lei diz", colado em "mediante remuneração", e sugere uma conclusão que o arquivo diz não tirar. No mais, a seção 9 não conclui (linhas 187–188, 311) |
| Idem — "controladores conjuntos" | Não conclui (linhas 164, 313). Linha 169, última coluna, traz uma conclusão entre parênteses ("o regresso não muda o que o titular pode cobrar de qualquer um") |
| Idem — exclusividade e concorrência | Linha 91 (erro, seção 3(d)). Linha 94: sem conclusão; o resumo do § 2º dá só os 20% e omite a outra hipótese e o poder do Cade de mudar o percentual (correção 12). Linha 102: "o pré-pago tem de estar escrito" |
| Regra apoiada só em fonte D, C ou plataforma estrangeira | Nenhuma. A 99 Calls (D) entra como exemplo e, na linha 71, como "o que não copiar". As linhas 19–20 e 192 dizem que prática de plataforma não é lei. O "Consenso 9" (linhas 292–294) é descrição das plataformas, não regra |
| Número de outro país usado como do Brasil | Nenhum. Falta o país **ao lado** em algumas células: linhas 81, 82, 139 (45, 7 e 4 dias; 2 a 3 dias úteis), 140, 141, 142, 233 e 292–294 citam Angi, Service Direct e eLocal sem "(EUA)" (correção 14) |
| Citação mais longa do que a ferramenta devolve | Medi todo trecho entre aspas: o maior vindo da web tem 121 caracteres (linha 197). Só um passa de 125: a frase do Google na linha 71 (126), que vem de [R], linhas 126–128, e lá tem a marca [S] (só leitura de subagente) |
| Redação de cláusula | Nenhuma |
| "Fonte anterior a 2025" | P3 leva a marca. Linha 90: o "até 6" do oHub vem de artigo de 2021, marcado em [M] (linhas 108 e 595), e aqui ficou sem a marca (correção 13). L15: página modificada em 2025, mas o verbete reproduz guia de 2022 (correção 20) |
| Seção 14 | A linha 256 diz "Cada linha repete um veredito já fechado". Não é verdade para: linha 267 (página sem empresa nomeada é **não conclusivo** no quadro de [R], linha 31, e virou "não pode"); linha 266 (revenda e reuso são **inferência** em [R], linhas 360–361); linha 270 (o próprio texto diz "sem veredito próprio"); linhas 271–272 (remetem a seções deste arquivo, não a veredito do item 2); linha 273 (em [B], linha 444, o alcance no Maps é leitura do guia) |

## 5. Remissões internas

**Por linha: conferi todas** (cerca de 110, nos cinco arquivos e em `RODADA.md`), contra o estado atual dos arquivos
(`desenho_v0.md` de 22:38; `modelos_de_negocio.md` de 22:17). Li `desenho_v0.md` e `00_restricoes.md` inteiros e, de
`modelos_de_negocio.md`, `01_google_organico.md` e `02_google_maps_perfil.md`, todas as faixas citadas.

- [D] `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`: linhas 86, 89, 145–152, 151, 152, 167, 193–194, 195–198,
  199–211, 212–220, 227–228, 234, 235, 245–246, 249–250, 278–279, 280–281, 282–284, 302, 304, 307, 307–312, 309, 309–311,
  327, 328, 330, 332, 345–347, 347, 350–354, 352–354, 355–359, 358–359, 360–361, 362–364, 374, 375, 384, 386 — **batem**.
- [M] `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md`: linhas 106, 113, 119, 129, 140, 173–188, 177, 178,
  186, 229, 330–331, 346–347, 380–381, 403, 405, 472, 486–487, 574–575, 577–586, 583–586, 590–601, 594, 595, 599,
  707–754, 729, 774; e as fontes F1, F3, F6, F8, F15, F22, F25, F29, F37 com os números R2, R9, R15, R20, R26, R28 —
  **batem**.
- [R] `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`: quadro (linhas 27–31, 36–37) e linhas 73–74,
  78–80, 95–100, 110–116, 126–128, 133–134, 165, 170–174, 186–194, 200–203, 217–218, 223–229, 253–258, 286, 298–304,
  317, 320, 328–331, 353–356, 358–368, 395–397, 411–427, 438–441 — **batem**.
- [A] `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`: linhas 152–173, 164–167, 166, 167 —
  **batem**.
- [B] `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`: linhas 416–461, 418–424, 445, 451, 453,
  458, 461 — **batem**.
- `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 65 — **bate**.

**Por seção: conferi 17** — [D] seções 2, 3.1, 4.1, 4.2, 4.3 (última linha), 4.4, 5.1 (passos 2, 3 e 5), 5.2, 5.3
(primeira linha), 7, 8 (fase 3), 9.1, 9.2 e 10 (premissa 5); [M] seções 5.7 e 6; [B] seção 10. Todas existem e dizem o
que o artefato lhes atribui.

**Remissões que não batem (uma, pequena):**

1. Linha 167, quarta coluna: "avisa cada empresa 'na hora'" com remissão a [D], linhas 282–284. Nessas linhas o desenho
   diz "avisa **de imediato**"; "na hora" está na linha 249 de [D] (texto do formulário). Correção 6.

Observação sem efeito: a lista de fontes de [M] "citadas sem releitura" (linhas 364–365) omite F26, que sustenta parte
da linha 599 de [M].

## 6. Coerência com o quadro de vereditos (`00_restricoes.md`, linhas 21–38)

| Vedado ou restrito no quadro | O levantamento sugere? |
|---|---|
| Controle do perfil da licenciada pelo site; telefone ou site do intermediário no perfil (linhas 25–28) | **Não.** Seção 13 só trata da gestão autorizada, com ela como proprietária; linhas 260–261 excluem o resto |
| Controle do número dela; central de WhatsApp que tria e repassa (linhas 36–37) | **Não.** Linha 180 pede que o contrato diga que o site não opera, não acessa e não recebe cópia da conta; linha 262 exclui |
| Garantia de posição | **Não.** Linhas 71, 247, 263. A linha 231 só pergunta se posição entra no **relatório** |
| Avaliação comprada ou incentivada (linha 29) | **Não.** Linhas 248 e 264 |
| Repasse a empresa que a pessoa não escolheu; revenda (linhas 33–35) | **Não.** Linhas 165 e 266. A linha 140 aponta a captura de tela da conversa como problema, não como solução |
| Página de oferta sem empresa nomeada (linha 31: não conclusivo) | Não sugere; a linha 267 é **mais dura** que o quadro (correção 7) |

Nenhuma incoerência no sentido de afrouxar uma restrição.

## 7. Forma

| Item | Resultado |
|---|---|
| Português | Sim; citações de plataformas estrangeiras no original, como nos demais arquivos |
| Caminhos absolutos | Sim (procurei caminho relativo de arquivo: nenhum) |
| Dado pessoal | Nenhum nome de pessoa física, telefone ou avaliação copiada (só nomes de empresas e de órgãos) |
| Tabela de fontes com classe e quem ganha | Sim (linhas 331–361). A contagem (29 páginas; 28 A e 1 D) confere |
| Fontes que não abriram | Sim (linhas 375–391), com "Página que pediu ação: nenhuma" |
| Consenso / disputado / não sei | Sim (linhas 277–321). Os dez itens de consenso são classe A; ressalvas de texto faltando nos itens 1 e 7 (correção 19); o item 6 de "Disputado" não é divergência de fontes (correção 8) |
| País ao lado de regra ou número estrangeiro | Sim na primeira menção, nos cabeçalhos e na tabela de fontes; falta em algumas células (correção 14) |

## 8. O que não conferi

- Os resumos da ferramenta sobre o oHub nas linhas 121, 124 e 125 (pedido falso; "fechou com outro" no primeiro
  contato; o que não se devolve), 192 (fornecedores respondem pelas próprias contratações) e 207 (ausência de licença
  de uso de logotipo): confirmei só o sentido geral da política, não cada detalhe.
- A nota de data de L2 ("Lei nº 15.452" no texto × link para a Lei 15.352/2026).
- Os trechos que a ferramenta não alcança: últimos 25.310 caracteres da LGPD, 17.708 da Lei 9.279, 5.119 da Lei 12.529
  e o Código Civil depois do caractere 300.000. Nenhum artigo citado está neles (os citados apareceram antes).
- O texto da Resolução CD/ANPD 15/2024, os guias da ANPD em PDF e o estudo do Cade: não abri (PDF não se baixa; o
  artefato também não os leu e diz isso).
- Jurisprudência: fora do escopo; o artefato não a usa.
- Não julguei se a lista de pontos está **completa** do ponto de vista de um advogado (por exemplo, o artefato não
  trata de foro ou arbitragem além da linha 142, nem de cessão do contrato). O portão não pede isso.

---

## Correções pedidas

As nove primeiras pesam no conteúdo; as demais são de precisão e de forma.

1. **Linha 91, coluna "O que a lei diz" (erro de conteúdo).** Trocar por: "Sem ajuste: na agência, a trava é dos dois
   lados — o proponente não pode constituir outro agente na mesma zona com idêntica incumbência, e o agente não pode
   tratar ali de negócios do mesmo gênero para outros proponentes (CC, art. 711 — resumo) [L3]. Quem seria 'proponente'
   e quem seria 'agente' neste contrato, e se anunciar em outro site equivale a 'constituir outro agente': pergunta
   para o advogado. Nos demais tipos, **silente**."
2. **Linha 221, coluna "O que a lei diz" (falha do sorteio).** Trocar o começo por: "CDC, art. 30: informação ou
   publicidade suficientemente precisa obriga o fornecedor que a veicula ou dela se utiliza; art. 37, § 1º: é enganosa
   a informação falsa ou capaz de induzir em erro (resumo) [L1]. **Leitura minha, não frase da lei:** manter a página
   com o nome dela depois da saída pode cair nos dois (oferta que ela já não faz; informação que deixou de ser
   verdadeira); uso do nome sem autorização, ver 10.2."
3. **Linhas 56–57 e linha 196, última coluna.** Linha 56–57: "O que o texto diz é que é vedada a cláusula contratual
   que impossibilite, exonere ou atenue a obrigação de indenizar prevista no CDC (art. 25); como isso alcança uma
   cláusula entre o site e a licenciada é pergunta para o advogado." Linha 196: "Se o contrato entre site e licenciada
   pode ir além de tratar do **regresso** entre os dois, diante do art. 25." Na linha 169, última coluna, trocar o
   parêntese por "(se o regresso muda o que o titular pode cobrar de cada um: pergunta para o advogado)".
4. **Linha 72, coluna "O que a lei diz".** Trocar por: "CDC, art. 30, trata da oferta ao consumidor (seção 6); se o CDC
   alcança a relação entre o site e a licenciada: **não levantado** (seção 5.2, linha da devolução; 'Não sei', 12). No
   Código Civil: **silente**, salvo a boa-fé do art. 422."
5. **Linha 165, coluna "O que a lei diz".** Trocar a frase do art. 7º, § 5º, por: "O controlador que obteve o
   consentimento e precisa comunicar ou compartilhar os dados com outros controladores obtém consentimento específico
   para isso, 'ressalvadas as hipóteses de dispensa do consentimento previstas nesta Lei' (art. 7º, § 5º) [R, linhas
   298–300]."
6. **Linha 167.** Segunda coluna: acrescentar depois de "idêntico procedimento": ", 'exceto nos casos em que esta
   comunicação seja comprovadamente impossível ou implique esforço desproporcional' (art. 18, § 6º) [R, linhas
   328–331]". Quarta coluna: trocar a remissão por "[D, seção 5.2, linhas 249 e 282–284]" (ou trocar "na hora" por "de
   imediato").
7. **Seção 14, linhas 256, 266, 267 e 270–273.** Linha 256: "Cada linha aponta para onde o ponto está. Nem todas são
   veredito do item 2: a coluna do meio diz se é **vedado** (veredito), **não conclusivo e fora por escolha do
   desenho**, **inferência**, ou **texto de lei citado neste arquivo, cuja aplicação é do advogado**." Linha 267:
   "Página de oferta sem empresa nomeada (**não conclusivo** no item 2; fora por escolha do desenho); licenciada sem
   licença e órgão emissor (RDC 622, art. 22)". Linha 266: acrescentar "revenda e reuso: **inferência** de [R], linhas
   360–361". Linhas 271 e 272: acrescentar "texto de lei; não é veredito do item 2". Linha 273: acrescentar "para a
   consulta no Maps, leitura de [B], linha 444".
8. **Marco Civil: linhas 163, 305–306 e lista "Não sei".** Linha 163: "…guarda esses registros, sob sigilo, em ambiente
   controlado e de segurança, por 6 meses, 'nos termos do regulamento' (art. 15 — resumo) [L7]. O § 1º admite ordem
   judicial contra provedor não sujeito ao caput, e o art. 17 diz que não guardar os registros não implica
   responsabilidade por dano de terceiros (resumo). **Não lido:** o regulamento a que o artigo remete." Tirar o item 6
   de "Disputado" (linhas 305–306) e pô-lo em "Não sei": "Se o site é o provedor de aplicações do art. 15 do Marco
   Civil (guarda de seis meses) e o que o regulamento, não lido, exige; só então há ou não conflito com o 'menor tempo
   possível' do desenho." (Indicação do verificador, **não aberta** nesta conferência: o regulamento seria o Decreto
   8.771/2016 — conferir antes de escrever.)
9. **Linhas 69 e 70 (Service Direct).** Linha 69: trocar 'vende o "Billable Lead"' por 'cobra a "Billable Call"
   (ligação cobrável)'. Linha 70: fechar a citação sem o ponto e completar: '"Any call that occurs when a New Potential
   Customer is seeking a service that your Service Category typically provides" ou que resulte em agendamento (o fim é
   resumo) [P6]'.
10. **Linhas 35–36.** "O Código Civil admite contrato atípico (art. 425). Há quatro tipos vizinhos — prestação de
    serviço, agência e corretagem, no Código Civil, e representação comercial, na Lei 4.886/1965 — com regras
    **diferentes**…"
11. **Linha 102, coluna "O que a lei diz".** Trocar "o pré-pago tem de estar escrito" por "o adiantamento depende de
    convenção ou costume; pôr por escrito é prudência (leitura minha)".
12. **Linha 94.** Trocar o resumo do § 2º por: "Posição dominante presume-se quando a empresa é capaz de alterar
    unilateral ou coordenadamente as condições de mercado **ou** controla 20% ou mais do mercado relevante, percentual
    que o Cade pode alterar por setor (§ 2º — resumo)"; e dizer que o § 3º lista condutas que caracterizam infração "na
    medida em que configurem hipótese prevista no caput".
13. **Linha 90.** Corretagem: "se a exclusividade for ajustada por escrito, o corretor tem direito à remuneração
    integral mesmo sem mediar o negócio, salvo inércia ou ociosidade (CC, art. 726 — resumo)". Terceira coluna:
    acrescentar depois de "4 ou 6 prestadores": "(o '6' vem de artigo do oHub de 2021: **pode estar desatualizado**
    [M, linhas 108 e 595])".
14. **País ao lado: linhas 81, 82, 139, 140, 141, 142, 233 e 292–294.** Pôr "(EUA)" depois de Angi, Service Direct e
    eLocal em cada célula, e "(BR)" depois de oHub e Cronoshare nas linhas 292–294.
15. **Linha 192, coluna "O que a lei diz".** Mover "O site não cobra do consumidor [D, seção 5.2, linha 234]" para a
    coluna do desenho, ou completar: "se remuneração indireta basta para o § 2º: **não levantado: jurisprudência**".
16. **Linha 180, coluna 2.** Marcar o fecho como leitura: "…[P2]: leitura minha — isso é gerir a conta dela em nome
    dela, não um número do site".
17. **Linhas 129 e 140.** Linha 129: trocar "sem critério nem prazo na página" por "sem prazo nem percentual na página
    (o critério é só não conseguir o cliente ou o trabalho)". Linha 140: "a Service Direct exige gravação ativada e a
    análise é da equipe de qualidade dela; a eLocal confere o motivo com a gravação (resumo) [P7, P9]".
18. **Linha 220.** Completar a agência: "noventa dias, desde que transcorrido prazo compatível com a natureza e o vulto
    do investimento exigido do agente (art. 720 — resumo)".
19. **Linhas 281 e 290 (Consenso 1 e 7).** Linha 281: "…e presume paritários e simétricos os contratos civis e
    empresariais, até elementos concretos que afastem a presunção (art. 421-A)". Linha 290: acrescentar "salvo as
    exclusões do art. 43".
20. **Linhas 71, 222 e 347 (marcas).** Linha 71: anotar que a frase do Google tem em [R] a marca [S] (só leitura de
    subagente). Linha 222: marcar "cópias em cache e em respostas de IA estão fora do controle do site" como observação
    de quem escreveu. Linha 347 (L15): acrescentar "o verbete reproduz guia de 2022: **pode estar desatualizada**".
