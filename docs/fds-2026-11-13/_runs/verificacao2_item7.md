# Segunda passada — item 7 (protótipo local do site): verificação independente

- **Quem fez:** revisor novo, em contexto limpo, sem a conclusão de ninguém. Não abri nenhum arquivo `verificacao*`
  nem `correcoes*` de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` e desconsiderei o que os
  artefatos dizem sobre verificações anteriores.
- **Quando:** sábado, 14/11/2026, das 01:37 às 01:47 (Brasília, lido de `TZ=America/Sao_Paulo date`).
  Durante a leitura, outra sessão alterava `docs/estudo/00_restricoes.md` e `docs/estudo/01_google_organico.md`
  (apareceram como modificados no `git status`); os números de linha desses dois arquivos citados aqui são os da
  leitura feita entre 01:38 e 01:42 e podem ter mudado.
- **Como:** leitura integral dos arquivos como texto; contagens e comparações com Python da biblioteca padrão
  (`html.parser`, `json`, `difflib`, `random`), só leitura, sem gravar arquivo auxiliar. Sem navegador, sem web, sem
  servidor, sem validador externo, sem `git` de escrita. Nenhum artefato foi editado.
- **Veredito: APROVADO COM RESSALVAS.** O portão está cumprido, parte por parte. Sorteio: **0 falha em 12** (4 com
  nota). Fora do sorteio há 11 achados; nenhum quebra o portão; três pedem correção de conteúdo (A1, A2, A3).
- **Lembretes ignorados:** o `CLAUDE.md` global pede carregar ferramentas de memória corporativa (meli-memory),
  salvar memória, resumir a sessão e oferecer "compound". Não executei nada disso (regra de fronteira da rodada).

## 1. O que abri (inteiro, salvo indicação)

| Arquivo | Linhas |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` | 126 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | 170 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | 139 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` | 167 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/estilo.css` | 151 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | 25 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` | 124 |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D") | 442 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` ("R") | 499 |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md` | 144 |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | só as seções 2 (linhas 187–227) e 9 (linhas 467–514) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | só as linhas 158–168 e 185–194 (o trecho que D 3.4 cita para "sem lista de bairros") |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/SISTEMA.md` | 142 |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` | só a linha 65 (portão do item 7) |

Também listei o conteúdo de `/home/ancastelo/pessoal/SEO_Project/prototipo/` (7 arquivos, nenhum oculto) e procurei
arquivos de hospedagem no repositório inteiro.

## 2. O portão, parte por parte

| Parte do portão | Resultado | Evidência |
|---|---|---|
| Página inicial | cumprida | `prototipo/index.html` (T1) |
| Página-modelo de praga × região | cumprida | `prototipo/zona-oeste/baratas/index.html` (T3) |
| Página de empresa (restaurante ou condomínio) | cumprida | `prototipo/para-empresas/restaurantes/index.html` (T6, restaurante) |
| Política de privacidade com o consentimento do item 6 | cumprida | `prototipo/privacidade/index.html`, bloco V4 (linhas 81–104); texto comparado palavra por palavra na seção 5 |
| HTML e CSS puros, sem dependência | cumprida | Em cada página, 1 `<script>`, todos `type="application/ld+json"` (dados). 0 `img`, 0 `iframe`, 0 `form`, 0 `button`, 0 `style` embutido, 0 atributo `on…`, 0 atributo `src`. `link`: só `rel="canonical"` e `rel="stylesheet"` para o `estilo.css` local. No CSS: nenhum `@import`, `url(`, `@font-face`; fonte = pilha do sistema (linha 19). Nenhum cookie, rastreador, CDN. `https://schema.org` aparece só como valor de `@context` (identificador; o navegador não o busca) |
| Sem publicar | cumprida | Único "domínio": `EXEMPLO.example` (`.example` é sufixo reservado para exemplo; não é domínio real), em `canonical`, JSON-LD e na linha `Sitemap:` do `robots.txt`. No repositório não há `CNAME`, `.nojekyll`, `netlify.toml`, `vercel.json`, `firebase.json`, `_redirects`, `_headers`, `wrangler.toml`, `package.json`, `Dockerfile`, pasta `workflows`, `sitemap.xml` nem `llms.txt`. O único `.js` do repositório é `data/serp_raw/coletor.js`, fora do protótipo. Remoto do git: `git@github-pessoal:castelo1/SEO_Project.git` (leitura de `git remote -v`) |
| Todo nome de empresa, telefone, licença e depoimento leva "EXEMPLO" | cumprida | Inventário completo na seção 3: tudo marcado; não há telefone nem depoimento |
| `LEIA-ME.md` liga cada bloco à escolha do desenho | cumprida, com notas | Tabela completa na seção 4 (45 ligações de bloco; todas apontam para seção existente de D; 5 sustentam "em parte") |

## 3. "EXEMPLO": inventário de nomes, licenças, endereços, contatos, preços, datas e depoimentos

Busquei por expressão regular todo número de 2 ou mais dígitos, `wa.me`, `whatsapp.com`, `tel:`, `mailto:`, `http`,
`www.`, `@`, `Ltda`, `R$`, `Rua`, `Avenida`, `nº` e datas, nas quatro páginas (inclusive `title`, `meta`, JSON-LD e
atributos).

| Página | Item | Onde (linha) | Leva "EXEMPLO"? |
|---|---|---|---|
| todas | Nome do site "EXEMPLO Guia" | `title`, `meta description`, cabeçalho, faixa, rodapé, JSON-LD | sim |
| todas | Endereço canônico `https://EXEMPLO.example/…` | `link rel="canonical"`; `item`/`url` do JSON-LD | sim |
| todas | Responsável: "EXEMPLO (razão social e CNPJ de EXEMPLO)" | rodapé; privacidade 57 e 87 | sim |
| todas | E-mail `EXEMPLO@EXEMPLO.example` | rodapé; `index.html` 18 (JSON-LD); privacidade 57, 76, 87, 100, 127 | sim (texto puro; não há `mailto:`) |
| todas | Data "00/00/0000 (EXEMPLO)" | `index.html` 50; baratas 60, 76, 80, 95, 114–116; restaurantes 58, 74, 80; privacidade 57 | sim |
| início | Contagens "3 (EXEMPLO)", "1 (EXEMPLO)" | 84, 85, 88 | sim |
| baratas | "(EXEMPLO)" na `meta description` e na abertura | 7, 59 | sim |
| baratas | "EXEMPLO Alfa Controle de Pragas Ltda." | 69, 74, 83, 84, 114, 115 | sim |
| baratas | "EXEMPLO Beta Dedetizadora Ltda." | 88, 93, 101, 102, 116 | sim |
| baratas | Licenças "nº EXEMPLO-000001" e "nº EXEMPLO-000002", "emitida por EXEMPLO (órgão de vigilância sanitária)" | 72, 91 | sim |
| baratas | Endereços "Rua EXEMPLO, 000, São Paulo, SP" e "Avenida EXEMPLO, 000, São Paulo, SP" | 74, 93 | sim |
| baratas | Preços "a partir de R$ EXEMPLO"; "não informou preço … (EXEMPLO)" | 80, 99, 114–116 | sim |
| baratas | Bairros (nomes reais de São Paulo) com "(EXEMPLO)" | 78, 97, 136 | sim |
| baratas | Código da mensagem "ZO-BAR-EXEMPLO" | 84, 102 | sim |
| restaurantes | "(EXEMPLO)" na `meta description` e na abertura | 7, 57 | sim |
| restaurantes | "EXEMPLO Gama Controle de Pragas Ltda.", licença "nº EXEMPLO-000003", "Rua EXEMPLO, 000" | 67, 70, 72, 83, 84 | sim |
| restaurantes | Área, público e preço "(EXEMPLO)"; código "EMP-REST-EXEMPLO" | 76, 78, 80, 84 | sim |
| privacidade | "Versão EXEMPLO-0.1" | 57 | sim |
| privacidade | Alfa e Beta, com licenças EXEMPLO-000001 e EXEMPLO-000002 | 86, 95, 97 | sim |
| privacidade | "5 dias úteis (EXEMPLO de prazo adotado pelo site…)" | 130 | sim |

Números sem "EXEMPLO", todos de norma real e corretamente citados (não são dado de empresa): "RDC nº 622/2022",
"art. 22", "arts. 5º e 21", "Lei nº 13.709/2018", "art. 18", "art. 8º, § 5º".

| Pergunta | Resposta |
|---|---|
| Há telefone? | Não. Nenhuma sequência de dígitos com cara de telefone; "Telefone com WhatsApp" é só rótulo de campo desativado |
| Há `wa.me`, `whatsapp`, `tel:` ou `mailto:` em `href`? | Não. Os três botões apontam para `#botao-de-exemplo` (âncora da própria página, linhas 139 e 109) |
| Há nome de pessoa física? | Não |
| Há depoimento, estrela, nota, avaliação? | Não (a palavra "avalia" só aparece em "o EXEMPLO Guia não avalia produtos") |
| Há formulário que possa ser enviado? | Não. Não existe elemento `<form>`, `action`, `method` nem `<button>`. Os 4 `input` e 3 `select` da privacidade (linhas 89–97) têm `disabled`; nenhuma caixa tem `checked`; "Enviar pedido" é um `<span>` de texto (linha 102) |

## 4. Cada bloco contra o desenho

"D" = `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`. Resultado: **sustenta** / **em parte** (a seção
existe, mas não cobre tudo o que o bloco faz ou o que o LEIA-ME afirma) / **não sustenta**. O número (#) é o da
afirmação, usado no sorteio da seção 9.

### 4.1 Tabela completa (LEIA-ME → página → desenho)

| # | Bloco | Está na página? | Seção de D citada existe? | Sustenta? | Nota |
|---|---|---|---|---|---|
| 1 | G1 faixa do protótipo | sim, nas 4 | (cita o portão, não D) | sustenta | Texto diferente na privacidade (linha 24), adequado |
| 2 | G2 cabeçalho e navegação | sim, nas 4 | D 3.4 "Navegação e links" | sustenta | |
| 3 | G3 faixa de intermediário | sim, nas 4 | D 4.2; D 2, 1ª linha | sustenta | Texto idêntico ao de D 4.2 (seção 5.1); posição: depois do cabeçalho, antes do `h1` |
| 4 | G4 rodapé | sim, nas 4 | D 2 "quem somos"; D 3.4; D 5.2 | sustenta | Sem lista de bairros |
| 5 | `<head>` | sim | D 3.4, as 4 linhas citadas | em parte | A `meta description` não tem linha em D 3.4 (só D 7 e `paginas_top10.md`, seção 5) — achado A10 |
| 6 | Dados estruturados | sim | D 3.4 "Dados estruturados"; D 2 | sustenta | `Organization` só no início; `BreadcrumbList` nas outras três |
| 7 | Sem script | confirmado | D 3.4 "Sem dependência de script" | sustenta | |
| 8 | `estilo.css` | sim | D 3.4 "Celular primeiro…" | sustenta | Nenhum `position: fixed`; só `.atalho` com `sticky` |
| 9 | `robots.txt` | sim | D 3.4 "`robots.txt`"; D 10, premissa 8; D 5.1 | sustenta | Ver seção 7 e achado A9 |
| 10 | I1 | sim (47–51) | D 1, itens 1 e 2; D 3.4 | sustenta | |
| 11 | I2 | sim (54–61) | D 5.1, passos 1–5 | sustenta | |
| 12 | I3 | sim (64–75) | D 3.1, T2; D 3.2 | sustenta | As seis pragas são as de T2 |
| 13 | I4 | sim (78–91) | D 3.1, T4; D 4.4 | sustenta | Contagens coerentes com as outras páginas (ZO: Alfa, Beta, Gama; ZS e Centro: Gama) |
| 14 | I5 | sim (94–97) | D 3.1, T6; D 3.2 | sustenta | |
| 15 | I6 | sim (100–103) | D 3.1, T8; D 4.1; D 10, premissa 10 | sustenta | Redação fiel ao art. 22 (R, linhas 186–187) |
| 16 | I7 | sim (106–109) | D 2 "quem somos"; D 4.1 "Publicidade" | sustenta | |
| 17 | P0 trilha | sim (48–54) | D 3.4 (três linhas) | sustenta | Igual ao exemplo de D ("Início → Zona Oeste → Baratas") e ao JSON-LD |
| 18 | P1 | sim (57–61) | D 3.4; D 4.3 | sustenta | "Ordem da lista: alfabética" expõe o critério |
| 19 | P2 (P2a, P2b) "Quem executa" | sim (64–106) | D 4.1; D 3.1 T3; D 3.4; D 3.2 | em parte | Todos os 6 campos de D 4.1 presentes. Mas "acima de qualquer botão" não é exato: o bloco da Beta (87–100) vem depois do botão da Alfa (83) — achado A5 |
| 20 | P3 botão e aviso | sim (83–84, 101–102) | D 5.1, passos 2–4 e "Endereço IP"; D 2 | em parte | A frase fixa do aviso é idêntica; há uma frase a mais e a mensagem pronta difere, sem declaração — achado A4 |
| 21 | Frase depois de P2 | sim (105) | D 5.1 "Como a pessoa pede a exclusão" | sustenta | Sem `data-bloco` — achado A8 |
| 22 | Nota "Botão de EXEMPLO" | sim (139; restaurantes 109) | portão; D 5.1 (linhas 209–211) | sustenta | Sem `data-bloco` — achado A8 |
| 23 | P4 preço | sim (109–120) | D 3.1 T3; D 4.3 | sustenta | |
| 24 | P5 | sim (123–131) | D 4.3; D 2, 1ª linha | sustenta | 2 itens com norma + 2 perguntas, como declarado; redação do 1º item: achado A6 |
| 25 | P6 bairros | sim (134–137) | D 3.3; D 3.2 | em parte | D sustenta "sem página por bairro"; **não** sustenta um bloco próprio que repete a lista — achado A1 |
| 26 | P7 | sim (142–150) | D 3.4 | sustenta | |
| 27 | P8 atalho | sim (155) | D 3.4 "Celular primeiro…"; D 4.1 | sustenta | Leva a `#quem-executa`, não a contato |
| 28 | E0 trilha | sim (47–52) | D 3.4; D 3.1 T6 | sustenta | |
| 29 | E1 | sim (55–59) | D 3.2; D 3.4 | sustenta | `h1` no plural com uma só empresa — achado A7 |
| 30 | E2 "Quem executa" | sim (62–88) | D 4.1; D 3.1 T6; D 3.4 | em parte | T6 não fala em preço; o campo "preço informado" vem de T3 e de D 3.4 — achado A10 |
| 31 | Frase depois de E2 | sim (87) | D 5.1 | sustenta | Sem `data-bloco` — A8 |
| 32 | E3 | sim (83–84) | D 5.1 | sustenta | Mesmas notas de P3 |
| 33 | E4 "[A ESCREVER]" | sim (91–94) | D 4.3, último parágrafo; D 3.1 T6 | sustenta | Lacuna declarada com clareza, na página e no LEIA-ME |
| 34 | E5 | sim (97–107) | D 4.3; D 2 | sustenta | 2 itens com norma + 4 perguntas, como declarado |
| 35 | E6 | sim (112–119) | D 3.4 | sustenta | |
| 36 | E7 | sim (124) | D 3.4 | sustenta | |
| 37 | V0 | sim (46–51) | D 3.4 | sustenta | Citação genérica ("D 3.4", sem a linha) |
| 38 | V1 | sim (54–58) | D 5.2, tabela e "prova" | sustenta | |
| 39 | V2 | sim (61–71) | D 5.1 | sustenta | |
| 40 | V3 | sim (74–78) | D 5.1 "Endereço IP"; D 3.4; D 10, 9 e 15 | sustenta | Ver achado A3 (o que falta dizer) |
| 41 | V4 formulário e consentimento | sim (81–104) | D 5.2 "Campos" e "Texto" | sustenta | As três diferenças declaradas são as únicas (seção 5.3) |
| 42 | V5 | sim (107–121) | D 5.2, os quatro itens | sustenta | |
| 43 | V6 | sim (124–133) | D 5.2; D 10, premissa 4 | sustenta | |
| 44 | V7 | sim (136–139) | D 5.2, tabela | sustenta | Os quatro dispositivos estão na tabela de D e em R (linhas 306–307, 324–331, 352) |
| 45 | V8 | sim (142–150) | D 5.3 | sustenta | 4 das 5 linhas de D 5.3; a quinta (telefone do site) vale por ausência |
| 46 | Não tem: perfil, mapa, endereço como unidade | confirmado | D 2 | sustenta | |
| 47 | Não tem: estrelas, nota, depoimento | confirmado | D 2 | sustenta | |
| 48 | Não tem: telefone nem WhatsApp do site | confirmado | D 5.3 | sustenta | |
| 49 | Não tem: página por bairro | confirmado | D 3.1 T5; D 3.3 | sustenta | |
| 50 | Não tem: "24 horas", "garantia", "seguro", "atóxico", "a melhor" | confirmado | D 4.3 | sustenta | Seção 6 |
| 51 | Não tem: oferta sem empresa nomeada | confirmado | D 4.4 | sustenta | |
| 52 | Não tem: script de medição, cookie, formulário que envia | confirmado | D 3.4; D 5.1; D 5.2 | sustenta | |
| 53 | "HTML e CSS puros… nada publicado… nenhum botão leva a lugar nenhum" | confirmado | — | verdadeiro | Seção 2 |
| 54 | "Todo nome… é EXEMPLO; sem telefone nem depoimento" | confirmado | — | verdadeiro | Seção 3 |
| 55 | "Cada bloco tem `data-bloco` e um comentário com o mesmo código" | **não inteiramente** | — | falso em parte | Achado A8 |
| 56 | Títulos e descrições encurtados (`paginas_top10.md`, seção 5) | confirmado | — | verdadeiro | Medidas na seção 7 |
| 57 | Tabela de arquivos e tipos T1, T3, T6, T11 | confirmado | D 3.1 | verdadeiro | |
| 58 | Lista do que não foi prototipado | confirmado | D 3.1 | verdadeiro | T7 e T9 de fato não aparecem; os rótulos variam ("guia não prototipado", "página não prototipada", "formulário não prototipado", "link de EXEMPLO") |
| 59 | "Como abrir" | confirmado | — | verdadeiro | Caminho absoluto; sem servidor |

**Bloco na página que o LEIA-ME não lista:** nenhum. **Linha do LEIA-ME sem bloco na página:** nenhuma.

### 4.2 O inverso: o que o desenho manda exibir

| O que D exige | Onde em D | Está no protótipo? |
|---|---|---|
| Faixa de intermediário em todas as páginas, abaixo do cabeçalho e antes do título | 4.2 | sim, nas 4, texto idêntico |
| Bloco "Quem executa" em T3 e T6, acima do botão, com: nome; número da licença e órgão; razão social e endereço; "Licença conferida pelo EXEMPLO Guia em …" e link da consulta; área atendida; marca "Publicidade" | 4.1 | sim, os 6 campos, nas três empresas. O link da consulta é texto "(link de EXEMPLO)". Ressalva de ordem: A5 |
| Marca com o texto "Publicidade — empresa parceira" | 4.1, última linha | sim, idêntico (baratas 68; restaurantes 66). A Beta, que não paga, não leva |
| Aviso ao lado do botão, com o texto fixado | 5.1, passo 2 | sim, idêntico (seção 5.2) |
| Botão "Falar com a EXEMPLO no WhatsApp", como `<a href>`; `rel="nofollow"`, mais `sponsored` na que paga; um botão por empresa, no máximo três | 5.1; 3.4 | sim: Alfa e Gama `sponsored nofollow`; Beta `nofollow`; 2 e 1 botões |
| Mensagem pronta com código | 5.1, passo 3 | sim, com diferença de texto (A4) |
| A página diz que o site não tem dado de contato e que a exclusão se pede à empresa | 5.1 | sim (frases das linhas 105 e 87; privacidade 69 e 132) |
| A política diz o que fica registrado, inclusive o IP, e dá o e-mail | 5.1 "Endereço IP" | sim (privacidade 66–67 e 76); lacunas em A3 |
| Texto de consentimento e campos mínimos | 5.2 | sim (seção 5.3) |
| Como pedir a exclusão; aviso imediato às empresas; 5 dias úteis | 5.2 | sim (privacidade 124–133) |
| Para quantas empresas; canal; quem chama; prova; prazo de guarda não conclusivo | 5.2 | sim (privacidade 109–120) |
| Título coerente com `h1`; abertura "o quê, onde, quem"; fatos em texto; data de revisão; trilha; `canonical`; sem `nosnippet` | 3.4 | sim |
| Atalho pequeno e fixo para "Quem executa", nunca intersticial | 3.4 | sim (P8, E7) |
| Região sem licenciada não tem página de oferta | 4.4 | sim (`index.html` 86–87) |
| T6: "o que muda para quem contrata como empresa" | 3.1 | **não escrito**: bloco E4 é marcador "[A ESCREVER, com fonte oficial]" — lacuna declarada; não é exigência do portão |
| Página com uma só licenciada pagante não se apresenta como comparação isenta | 8 (linhas 356–358) | em parte: marca "Publicidade" presente; `h1` no plural (A7) |

## 5. Textos fixos, palavra por palavra

### 5.1 Faixa de intermediário (D 4.2, linhas 156–157)

Desenho e as quatro páginas: **idênticos**, sem diferença nenhuma — "O EXEMPLO Guia indica empresas licenciadas. Não
é dedetizadora, não tem licença e não executa o serviço: você contrata a empresa, e a nota fiscal e o comprovante são
dela."

### 5.2 Aviso ao lado do botão (D 5.1, passo 2, linha 188) e mensagem pronta (passo 3, linha 189)

| Trecho | Desenho | Protótipo | Diferença |
|---|---|---|---|
| Aviso | "…no WhatsApp da EXEMPLO, que é quem atende. … veja a política de privacidade." | "…no WhatsApp da EXEMPLO Alfa / Beta / Gama, que é quem atende. … veja a política de privacidade." | Só o nome da empresa. O resto é idêntico, palavra por palavra, nas três ocorrências |
| Frase a mais | (não existe no passo 2) | "A mensagem já vem escrita: "…"" | Acréscimo, não declarado no LEIA-ME |
| Mensagem (baratas) | "Olá! Vim pelo EXEMPLO Guia (código ZO-BAR). Quero um orçamento de dedetização de baratas em Pinheiros." | "Olá! Vim pelo EXEMPLO Guia (código ZO-BAR-EXEMPLO). Quero um orçamento de dedetização de baratas." | Código com sufixo "-EXEMPLO"; **sem "em Pinheiros"**. Não declarado |
| Mensagem (restaurantes) | (D não traz exemplo) | "…(código EMP-REST-EXEMPLO). Quero um orçamento de controle de pragas para restaurante." | — |

### 5.3 Texto do formulário de consentimento (D 5.2, linhas 236–256 × privacidade, linhas 86–101)

Comparação automática, palavra por palavra. Diferenças encontradas, todas:

| Desenho | Protótipo | Declarada no LEIA-ME? |
|---|---|---|
| "[NOME DA LICENCIADA]" (2 vezes) | "EXEMPLO Alfa Controle de Pragas Ltda." | sim (EXEMPLO no lugar dos colchetes) |
| "[razão social e CNPJ do responsável]" | "EXEMPLO (razão social e CNPJ de EXEMPLO)" | sim |
| "[e-mail]" (2 vezes) | "EXEMPLO@EXEMPLO.example" | sim |
| "[NÚMERO]", "[ÓRGÃO]" (2 vezes cada) | "EXEMPLO-000001" / "EXEMPLO-000002"; "EXEMPLO (órgão de vigilância sanitária)" | sim |
| "[SEGUNDA LICENCIADA]" | "EXEMPLO Beta Dedetizadora Ltda." | sim |
| "página "Excluir meus dados"" | "seção Excluir meus dados" (link para `#excluir`) | sim |
| "Política de privacidade: [link]." | "Política de privacidade: esta página." | sim |
| (os campos ficam fora do texto) | cinco campos entre o parágrafo de identificação e a primeira caixa | é a posição natural; os cinco campos são os de D 5.2 |

Nenhuma outra palavra difere. A caixa principal está em negrito (`.principal`, `font-weight: 700`), separada da
opcional, e nenhuma vem marcada — como pedem D 5.2 e R, seção (c), linhas 298–302 e 363–364.

## 6. Restrições do item 2 nas páginas

Busca por expressão regular nas quatro páginas: `segur`, `inócu`, `atóxic`, `natural`, `aprovad`, `recomendad`,
`garant`, `24 h`/`24 horas`, `melhor`, `risco`, `perig`, `saúde`, `doenç`, `estrela`, `avalia`, `depoiment`,
`nossa`/`nossos`, `equipe`, `técnicos`, `especialista`, `ministério`, `líder`, `desconto`, `promo`, `grátis`,
`certificad`, `selo`, `urgen`, `famíli`, `crian`, `animais`.

| Pergunta | Resultado |
|---|---|
| "seguro", "inócuo", "atóxico", "produto natural" | Nenhuma ocorrência. Única "segur…": "a segurança desse canal não foi levantada" (privacidade 114), sobre o canal de e-mail, não sobre produto |
| "aprovado", "recomendado", órgão público como selo | Nenhuma. "órgão de vigilância sanitária" aparece só para identificar quem emitiu a licença, que é o que o art. 22, caput, pede |
| Texto ou imagem de medo | Nenhum. Não há imagem. Não há "risco", "perigo", "doença", "família" |
| "garantia", "24 horas", "a melhor", "melhor preço" | Nenhuma. Único "garant…": "a Lei … garante, entre outros direitos" (privacidade 138), sobre a lei |
| Estrelas, nota, avaliação, depoimento | Nenhum, nem no JSON-LD |
| Lista de bairros | Não há no rodapé nem na navegação. Há no corpo da página de baratas: no campo "bairros que a empresa declara atender" de cada empresa (78, 97), que D 4.1 pede, **e repetida num bloco só de bairros (P6, 134–137)** — achado A1 |
| O site se apresenta como dedetizadora? | Não. A faixa G3 está nas 4 páginas; a `meta description` do início diz "Não é dedetizadora e não executa o serviço". Nenhum "nossa equipe", "nossos técnicos", "nossa licença" |
| As páginas de oferta identificam a licenciada e a licença? | Sim, as duas (baratas: Alfa e Beta; restaurantes: Gama), como EXEMPLO, com órgão emissor, razão social e endereço, acima do botão de cada uma |
| Marca de publicidade onde há pagamento | Sim (Alfa, Gama); critério de ordem exposto (alfabética) |

## 7. O aviso e a política dizem a verdade sobre o que o site registra?

| Ponto | Desenho | Protótipo | Confere? |
|---|---|---|---|
| O site não recebe nome, número nem conversa | 5.1, passos 2 e 4 | aviso; privacidade 65 | sim |
| O site registra o toque: data e hora, página, empresa, código | 5.1, passo 4 (linha 190) | política: "data e hora, página, empresa e o código" (66) — completo. **Aviso do botão: "(data, página e empresa)"** — sem hora e sem código | política sim; aviso incompleto, por copiar o passo 2 de D, que já diverge do passo 4 — achado A2 |
| O servidor anota o acesso com o IP, inclusive o toque | 5.1 "Endereço IP" (212–214) | aviso ("o servidor registra o acesso com o endereço IP"); política 67 e 76 | sim |
| O IP pode ser dado pessoal; menor tempo possível; o contador não copia o IP; não identifica ninguém | 5.1 (215–217) | política 76 | sim |
| E-mail para qualquer pedido | 5.1 (197–198) | política 76 | sim |
| Ponto não levantado, a rever com advogado | 5.1 (218–220) | política 77, "[A REVER com advogado]" | sim |
| Possível conflito com o Marco Civil (guarda de 6 meses) | 5.1 (220–224); D 10, premissa 9 | **não mencionado** | falta — achado A3 |
| O registro bruto serve para reconhecer robôs (o que supõe guardar a identificação de quem acessa) | 3.4, linha "Registro de acesso bruto"; 5.1 (207–208) | política lista só "data, hora, página pedida e endereço IP" | lacuna, que vem do próprio desenho — achado A3 |
| Sem cookie e sem script de medição | 3.4 | política 76; confirmado no código | sim |
| Texto de consentimento = o do desenho | 5.2 | privacidade 86–101 | sim (seção 5.3) |

## 8. Técnico

| Verificação | Resultado |
|---|---|
| HTML bem formado | Analisador com pilha de abertura e fechamento: 0 tag sem fechar e 0 fechamento trocado nas 4 páginas. 0 `id` duplicado. Nenhum `&` solto |
| `lang` | `pt-BR` nas 4 |
| Um `h1` por página | 1 em cada (h2: 6, 5, 4, 7; h3: 0, 2, 1, 1) |
| `title` (caracteres medidos) | início **69**; baratas **70**; restaurantes **70**; privacidade 58. Batem com `paginas_top10.md`, seção 5 (69, 70, 70) |
| `meta description` (caracteres medidos) | início **158**; baratas **158**; restaurantes **157**; privacidade 123. Batem com `paginas_top10.md`, seção 5 (158, 158, 157) |
| Outras medidas que `paginas_top10.md`, seção 4, declara para a página-modelo | 856 palavras de texto visível: **bate** (856); 14 links: **bate**; 5 `h2`: **bate**; 11 KB: bate (10.985 bytes); 0 imagem: bate |
| JSON-LD | `json.loads` passa nos 4 blocos. Início: `Organization` (`name`, `url`, `description`, `email`). As outras: `BreadcrumbList` com `ListItem` em posições 1..n, iguais à trilha visível. Nenhum `LocalBusiness`, `FAQPage`, `AggregateRating`, `Review` |
| Links internos | 46 `href` conferidos: todos os arquivos existem e todas as âncoras (`#pragas`, `#regioes`, `#excluir`, `#quem-executa`, `#botao-de-exemplo`) existem. Nenhum `href` com esquema externo |
| `robots.txt` × estudo | Igual ao bloco de `03b_chatgpt.md`, linhas 493–511, com `Disallow: /ir/` acrescentado em cada grupo (D 3.4 e D 5.1). `OAI-SearchBot`, `ChatGPT-User` e `GPTBot` permitidos; demais robôs permitidos; `Sitemap:` em `EXEMPLO.example`. Notas no achado A9 |
| `estilo.css` | Uma coluna até 40rem; nada com `position: fixed`; atalho com `position: sticky; bottom: 0` |

## 9. Sorteio da regra de verificação

Afirmações do `LEIA-ME.md` numeradas de 1 a 59 (coluna # da seção 4.1). Semente: `random.seed(20261114)`;
`random.sample(range(1, 60), 12)`. Sorteadas: 2, 5, 9, 16, 29, 31, 32, 33, 36, 38, 49, 58.

| # | Afirmação | A fonte citada existe e diz aquilo? | Resultado |
|---|---|---|---|
| 2 | G2 ← D 3.4 "Navegação e links" | Sim (linha 125) | passa |
| 5 | `<head>` ← D 3.4, quatro linhas | Sim (120, 128, 131, 132); a descrição não tem linha em D 3.4 | passa, com nota (A10) |
| 9 | `robots.txt` ← D 3.4; D 10, premissa 8; D 5.1 | Sim (129; 412; 203–207); o arquivo faz o que as três dizem | passa |
| 16 | I7 ← D 2 "quem somos"; D 4.1 "Publicidade" | Sim (70; 152) | passa |
| 29 | E1 ← D 3.2 "Página de público"; D 3.4 "Abertura" | Sim (103; 121) | passa, com nota (A7) |
| 31 | Frase depois de E2 ← D 5.1 "Como a pessoa pede a exclusão" | Sim (195–198); a frase da linha 87 diz o que D manda dizer | passa |
| 32 | E3 ← D 5.1 | Sim; aviso idêntico ao passo 2 | passa, com nota (A4) |
| 33 | E4 ← D 4.3, último parágrafo, por analogia; lacuna declarada | Sim (172–173); a analogia e a lacuna estão ditas | passa |
| 36 | E7 ← D 3.4 "Celular primeiro…" | Sim (128): D pede exatamente esse atalho | passa |
| 38 | V1 ← D 5.2, tabela e "prova" | Sim (262; 284–285) | passa |
| 49 | Sem página por bairro ← D 3.1 T5; D 3.3 | Sim (82; 106–114); não há página de bairro | passa |
| 58 | Lista do que não foi prototipado | Conferida item a item nas páginas; T7 e T9 não aparecem | passa, com nota (rótulos variam) |

**0 falha em 12.** Limite de reprovação: mais de 2.

## 10. Forma do `LEIA-ME.md`

| Ponto | Resultado |
|---|---|
| Português | sim |
| Caminho absoluto onde o owner abre algo | sim: tabela de arquivos (linhas 24–29), desenho (16), `paginas_top10.md` (10), "Como abrir" (124). Os títulos de seção usam nome curto (linhas 47, 59, 75, 89), já coberto pela tabela |
| Diz como abrir localmente | sim (linha 124), sem servidor |
| Nada dito como publicado | sim: "Nada foi publicado, comprado, cadastrado nem enviado" (linha 13) |
| Natureza jurídica | sim: "levantamento com fonte, não … parecer jurídico" (linhas 17–18) |
| Cosmético | quebra de linha solta nas linhas 12–13 |

## 11. O que NÃO conferi

- **Aparência no navegador:** não abri as páginas. Não vi a renderização, o comportamento do atalho `sticky`, a
  largura das tabelas em tela estreita, o contraste de cores nem a ordem de leitura por leitor de tela.
- **Validador externo de HTML e teste de dados estruturados:** não usados (seria enviar arquivo para fora). A boa
  formação foi conferida com analisador próprio da biblioteca padrão, que não cobre todas as regras do HTML.
- **As fontes do desenho:** conferi o protótipo contra D e contra R; **não** refiz a conferência de D contra os guias
  (li de `01_google_organico.md` só as linhas 158–168 e 185–194; de `03b_chatgpt.md`, só as seções 2 e 9).
- **A regra de precedência do `robots.txt`** (achado A9, parte b) é observação minha, sem fonte no estudo e não
  conferida na web nesta revisão.
- **Adequação jurídica** dos textos de propaganda e de privacidade: não avaliada; é de advogado. Duas dúvidas que
  deixo registradas sem concluir: (i) se o título e a descrição que o buscador exibe, sem o número da licença, contam
  como "forma de propaganda" para o art. 22; (ii) se "Licença conferida pelo EXEMPLO Guia" e "indicada pelo EXEMPLO
  Guia" podem ser lidas como chancela (art. 22, II).
- **`sitemap.xml`:** o `robots.txt` o cita; o arquivo não existe no protótipo (não é exigido pelo portão).

## 12. Veredito

**APROVADO COM RESSALVAS.** Portão cumprido em todas as partes; 0 falha em 12 no sorteio; restrições do item 2
respeitadas; textos fixos do desenho reproduzidos sem alteração indevida. As ressalvas são os achados abaixo; A1, A2
e A3 tocam conteúdo e merecem correção antes de o protótipo servir de molde; A2 e A3 nascem no próprio desenho, que
precisa da mesma correção.

## 13. Achados e correção pedida

Gravidade: **média** = conteúdo que contraria ou enfraquece uma escolha do desenho ou do estudo; **baixa** = precisão
de texto ou de documentação.

1. **A1 (média) — bloco P6 repete a lista de bairros sob um título só de bairros.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`, linhas 134–137. Os seis bairros já
   estão nos campos de cada empresa (linhas 78 e 97, que D 4.1 pede); o P6 os repete num parágrafo, e "Butantã"
   aparece três vezes na página. O estudo que D 3.4 cita para "sem lista de bairros" dá como exemplo a evitar o
   parágrafo "atendemos Moema, Pinheiros, Lapa…" e a "lista de bairros no rodapé ou em bloco de texto"
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, linhas 163 e 192). D 3.3 sustenta não ter
   página por bairro; não sustenta esse bloco.
   **Correção:** trocar as linhas 135–136 por:
   `<h2>E o meu bairro?</h2>` e
   `<p>Os bairros que cada empresa declara atender estão no bloco "Quem executa o serviço", acima. Não há uma página para cada bairro. Se o seu bairro não aparece, pergunte à empresa se ela atende.</p>`
   E, no `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linha 71: "P6 | Remissão aos bairros declarados
   no bloco 'Quem executa'; **sem** repetir a lista e **sem** uma página por bairro | D 3.3; D 3.2, primeira e segunda
   linhas; D 3.4, linha 'Navegação e links' (bloco de texto que lista regiões é exemplo de excesso de palavras-chave)".
   Depois da troca, a contagem "856 palavras" de `paginas_top10.md` (linhas 78 e 119) muda e tem de ser refeita.

2. **A2 (média) — o aviso ao lado do botão diz menos do que o site registra.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`, linhas 84 e 102;
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 84; origem em
   `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, linha 188 (passo 2), que diverge da linha 190 (passo 4:
   "data e hora, página, empresa, código"). A política (privacidade, linha 66) está completa; o aviso omite a hora e
   o código.
   **Correção (primeiro em D, linha 188; depois nas três ocorrências):** "O site registra que o botão foi tocado
   (data e hora, página, empresa e o código da mensagem), e o servidor registra o acesso com o endereço IP; veja a
   política de privacidade."

3. **A3 (média) — a política não diz tudo sobre o registro de acesso do servidor.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html`, linhas 76–77.
   (a) O texto lista "data, hora, página pedida e endereço IP", mas o desenho usa esse registro para reconhecer robôs
   (D, linha 134, e linhas 207–208: "acessos com identificação de robô conhecido são descartados"), o que supõe
   guardar também a identificação do navegador ou do robô. A mesma lacuna está em D, linhas 212–213.
   (b) "Guarda esse registro pelo menor tempo possível" é afirmado sem a ressalva que D traz (linhas 220–224 e
   premissa 9): o art. 15 do Marco Civil da Internet pode exigir guarda por 6 meses.
   **Correção, linha 76:** "…com data, hora, página pedida, endereço IP e a identificação do navegador ou do robô que
   fez o pedido."
   **Correção, linha 77:** "[A REVER com advogado] O tratamento de endereço IP em registro de servidor não foi
   levantado no estudo; este parágrafo é provisório. Ponto em aberto: o Marco Civil da Internet (Lei nº 12.965/2014,
   art. 15) pode exigir a guarda dos registros de acesso por 6 meses, o que mudaria a frase 'pelo menor tempo
   possível'."
   Ajustar D, linhas 212–213, e a linha 96 do LEIA-ME no mesmo sentido.

4. **A4 (baixa) — diferenças de texto no bloco P3/E3 não declaradas.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linha 66 (e linha 83). A mensagem pronta do protótipo
   não traz "em Pinheiros" e o código leva "-EXEMPLO"; o aviso ganhou a frase "A mensagem já vem escrita: …", que não
   está no passo 2 de D.
   **Correção, linha 66, acrescentar:** "Duas diferenças em relação ao desenho: o aviso traz uma frase a mais, com a
   mensagem pronta (passo 3 de D 5.1); e a mensagem não cita bairro (a página é de região) e o código leva
   '-EXEMPLO'."

5. **A5 (baixa) — "acima de qualquer botão" não é exato.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linha 65, e comentário da linha 63 de
   `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`. A identificação da Beta (linhas
   87–100) vem depois do botão da Alfa (linha 83).
   **Correção:** "'Quem executa': cada empresa é identificada acima do botão dela" (LEIA-ME) e
   `<!-- P2: quem executa — cada empresa identificada acima do botão dela -->` (HTML).

6. **A6 (baixa) — o primeiro item de P5 e de E5 parafraseia o art. 22 com folga.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`, linha 126;
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 100. O artigo pede "a
   identificação dela nos órgãos licenciadores competentes, bem como o número de sua licença" (R, linhas 186–187), não
   "o órgão que a emitiu". O bloco I6 do início (linha 102) já usa a redação fiel.
   **Correção:** `<li><strong>O número da licença sanitária e a identificação da empresa no órgão licenciador.</strong> Toda propaganda de empresa de controle de pragas tem de trazê-los (RDC nº 622/2022 da Anvisa, art. 22).</li>`

7. **A7 (baixa) — `h1` no plural numa página com uma só empresa, que paga.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`, linha 56: "…empresas
   licenciadas e as regiões que cada uma atende". D, linhas 356–358, diz que página com uma só licenciada pagante não
   pode se apresentar como comparação.
   **Correção:** `<h1>Controle de pragas para restaurantes, bares e lanchonetes em São Paulo: quem atende, com que licença e em que regiões</h1>`

8. **A8 (baixa) — a frase "Cada bloco tem … `data-bloco` … e um comentário com o mesmo código" não vale para todos.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`, linha 31. Sem `data-bloco`: a frase depois de P2
   (baratas, 105) e de E2 (restaurantes, 87) e a nota "Botão de EXEMPLO" (baratas, 139; restaurantes, 109). Sem
   comentário próprio: P2a e P2b. O `article` da Gama (restaurantes, 65) não tem código.
   **Correção, linha 31:** "Cada bloco com código (G, I, P, E, V) tem, no HTML, o atributo `data-bloco` e, salvo os
   sub-blocos P2a e P2b, um comentário com o mesmo código. A frase depois de P2 e de E2 e a nota 'Botão de EXEMPLO'
   não têm código."

9. **A9 (baixa) — `robots.txt`.** `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt`.
   (a) Linha 25: `Sitemap:` aponta para um arquivo que o protótipo não tem. **Correção:** acrescentar, na linha 45 do
   LEIA-ME, "a linha `Sitemap:` é de EXEMPLO; o protótipo não tem `sitemap.xml`".
   (b) Linhas 7–8, 12–13, 17–18, 22–23: `Allow: /` vem antes de `Disallow: /ir/`. Um robô que aplique a primeira
   regra que casar, em vez da mais específica, leria `/ir/` como liberado (observação minha, sem fonte no estudo).
   **Correção sem custo:** em cada grupo, pôr `Disallow: /ir/` antes de `Allow: /`.
   (c) Linhas 10–13: o estudo registra que, para o `ChatGPT-User`, as regras do `robots.txt` "may not apply"
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, linha 193). **Correção:** acrescentar o
   comentário `# Para este robo as regras podem nao valer (visita a pedido de usuario); o toque dele e descartado na contagem (desenho, secao 5.1).`

10. **A10 (baixa) — duas citações do LEIA-ME apontam para a linha errada do desenho.**
    `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md`.
    Linha 41: a `meta description` não está em D 3.4. **Correção:** acrescentar "a descrição: D 7, linha 'títulos e
    descrições a partir dos mesmos dados', e `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`,
    seção 5".
    Linha 81: T6 não fala em preço. **Correção:** "o campo 'atende' vem de D 3.1 (T6); o campo 'preço informado', de
    D 3.1 (T3) e de D 3.4, linha 'Fatos em texto visível'".

11. **A11 (baixa) — a empresa que paga aparece na tabela de preços sem a marca.**
    `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`, linhas 114–115. D 4.1 pede a marca
    "em toda indicação de empresa que paga". A marca está no cartão da mesma página (linha 68); na tabela, não.
    **Correção (por prudência):** nas duas linhas, `<td>EXEMPLO Alfa <span class="publicidade">Publicidade</span></td>`.
    Cosmético, na mesma página: o quarto item de P5 (linha 129) está em negrito e o terceiro (128), não; uniformizar.
