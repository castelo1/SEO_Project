# Verificação independente do item 7 — `prototipo/`

- **Quando:** sexta, 13/11/2026, das 22:22 às 22:35 (Brasília, lido de `TZ=America/Sao_Paulo date`: início
  "Fri Nov 13 22:22:22 -03 2026"; antes de gravar, "Fri Nov 13 22:31:47 -03 2026"; depois de gravar, "Fri Nov 13 22:34:59 -03 2026").
- **Quem:** verificador em contexto limpo, sem a conclusão de quem produziu. Só leitura de arquivo local; nenhuma
  página da web aberta, nenhum navegador, nenhum servidor local, nenhum `git` de escrita. Nada editado além deste
  arquivo.
- **Artefato** (lido inteiro, arquivo por arquivo; os números de linha abaixo são destas versões):

  | Arquivo | Alterado às | Linhas | `sha256` começa por |
  |---|---|---|---|
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` | 22:20:01 | 126 | `422cd8a6ac377b6b` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | 22:20:01 | 168 | `d11dc70143d0844a` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | 22:20:01 | 139 | `72e74af6cb1d06b5` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` | 22:20:01 | 165 | `d179a0c4ab038848` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/estilo.css` | 22:06:18 | 151 | `1810b4e818e4ef63` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | 22:20:01 | 25 | `9eee790d32503625` |
  | `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` | 22:20:01 | 116 | `e1306bccf5c24417` |

- **Arquivos abertos para conferir:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D"; inteiro, 419
  linhas, alterado às 22:19:05, `sha256` `1e1250376138bfab`);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` ("R"; inteiro, 499 linhas);
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` (linhas 467–514, para o `robots.txt`);
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md` (linha 65, o portão).
- **Abreviações:** "baratas" = `zona-oeste/baratas/index.html`; "restaurantes" = `para-empresas/restaurantes/index.html`;
  "privacidade" = `privacidade/index.html`; "início" = `index.html`; "L" = linha.

## Veredito

**APROVADO COM RESSALVAS.**

- O portão está coberto parte por parte (seção 1): quatro páginas, HTML e CSS sem programa nem dependência, nada
  publicado, todo nome de empresa, licença, órgão, endereço, preço, data, código e e-mail com "EXEMPLO", nenhum
  telefone, nenhum depoimento, LEIA-ME que liga cada bloco ao desenho.
- **Sorteio de 12 linhas do LEIA-ME: 0 falha em 12** (limite: 2); 2 das 12 batem só em parte (seção 3.2). Mesmo
  contando as duas parciais como falha, fica em 2, dentro do limite.
- Varredura das 56 linhas: 1 que não bate (E5) e 8 que batem em parte (seção 3.3).
- Nenhuma palavra vedada ou condicionada da seção 4.3 do desenho nem da seção (b) de R aparece no texto das páginas
  (seção 5). Nenhuma página oferece o serviço sem nomear empresa e licença. Nada depende de perfil de empresa,
  avaliação, link comprado ou central de WhatsApp do site.
- As ressalvas são 22 correções (seção 9): sete de conteúdo — uma promessa de privacidade que a arquitetura descrita
  não sustenta (endereço IP × toque no botão; nasce no desenho), dois desencontros entre os dados de exemplo e o que
  as páginas afirmam, uma frase de exclusão que falta na página de empresa, uma afirmação sem fonte (comprovante), o
  texto de consentimento sem a última parte do desenho, e uma frase sobre pagamento que deixa caso sem a marca
  "Publicidade" — e quinze menores.

## 1. Portão, parte por parte

| Parte do portão | Conferido como | Resultado |
|---|---|---|
| `prototipo/` com página inicial | `index.html` existe; tipo T1 (D 3.1) | sim |
| página-modelo de praga × região | `zona-oeste/baratas/index.html`; tipo T3 | sim |
| uma página de empresa (restaurante ou condomínio) | `para-empresas/restaurantes/index.html`; tipo T6 | sim |
| política de privacidade com o consentimento do item 6 | `privacidade/index.html`, bloco V4 (L80–102) | sim, com a ressalva 6 |
| HTML e CSS puros, sem dependência | busca em todos os arquivos (abaixo) | sim |
| sem publicar | sinais de hospedagem (abaixo) | sim, no que o disco mostra |
| nome de empresa, telefone, licença e depoimento levam "EXEMPLO" | inventário da seção 2 | sim |
| LEIA-ME liga cada bloco à escolha do desenho | seção 3 | sim, com as ressalvas 8 a 13 |

**O que procurei e o que achei (busca por expressão em `prototipo/`, todos os arquivos):**

| Procurado | Achado |
|---|---|
| `<script src`, `javascript:`, atributo `on…=`, `<style>`, `style=` | nenhum |
| `<script>` | 4, todos `type="application/ld+json"` (início L11; baratas L11; restaurantes L11; privacidade L10). O JSON de cada um é válido (lido por programa) |
| `@import`, `url(`, `@font-face` | nenhum; a fonte é a pilha do sistema (`estilo.css` L19) |
| `<img>`, `<svg>`, `<video>`, `<iframe>`, `<object>`, `<embed>`, `<base>`, `<meta http-equiv>` | nenhum |
| `<form>`, `action=`, `<button>` | nenhum. Os campos do formulário de exemplo (privacidade L88–96) estão soltos numa `<div>`, todos com `disabled` (4 `<input>`, 3 `<select>`); não há botão de envio |
| `<link>` | só `rel="canonical"` e `rel="stylesheet"` para `estilo.css` local |
| `http(s)://` | `https://EXEMPLO.example/…` (canônicos, itens do `BreadcrumbList`, `Sitemap:` do `robots.txt`) e `https://schema.org` (valor de `@context` nos 4 blocos JSON-LD) |
| `wa.me`, `api.whatsapp.com`, `whatsapp.com`, `tel:`, `mailto:`, `sms:` | nenhum |
| número de telefone (8 ou 9 dígitos, DDD, `0800`, `+55`) | nenhum |
| `display:none`, `visibility`, `opacity`, texto escondido | nenhum |
| `nosnippet`, `noindex` | nenhum |

- **JSON-LD e "HTML e CSS puros":** considero compatível. O bloco `application/ld+json` é dado embutido no HTML; o
  navegador não o executa nem busca nada por causa dele (`https://schema.org` ali é identificador de vocabulário, não
  recurso carregado). Fica o registro: `https://schema.org` é o único endereço de domínio real em todo o protótipo, e
  não é link. O LEIA-ME (L6) e o `estilo.css` (L1) dizem "sem script" sem essa ressalva — correção 19.
- **`EXEMPLO.example`:** `.example` é domínio reservado para documentação; não resolve.
- **Nada publicado:** em `/home/ancastelo/pessoal/SEO_Project` não há `CNAME`, `.nojekyll`, `netlify.toml`,
  `vercel.json`, `firebase.json`, `wrangler.toml`, `_config.yml`, `Dockerfile` nem `.github/workflows/`. O único
  remoto é `git@github-pessoal:castelo1/SEO_Project.git` (repositório do projeto; lido com `git remote -v`). **Não
  conferi** a configuração do repositório no GitHub (se há página publicada a partir dele): isso só se vê na conta, e
  não usei `gh` nem navegador.
- **Botões:** os três botões (baratas L83 e L101; restaurantes L85) apontam para `#botao-de-exemplo`, âncora que não
  existe em página nenhuma: tocar não leva a lugar nenhum. É o que o LEIA-ME declara (L7 e L60).

## 2. "EXEMPLO": inventário

Todo valor abaixo foi procurado no texto visível, em `<title>`, em `<meta name="description">` e no JSON-LD.

| O quê | Valor como aparece | Onde | Leva "EXEMPLO"? |
|---|---|---|---|
| Nome do site | "EXEMPLO Guia" | 4 páginas: `<title>`, descrição, cabeçalho, faixa, rodapé; JSON-LD do início (L15) | sim |
| Empresa | "EXEMPLO Alfa Controle de Pragas Ltda." / "EXEMPLO Alfa" | baratas L69, L74, L83, L84, L114, L115; privacidade L85, L94 | sim |
| Empresa | "EXEMPLO Beta Dedetizadora Ltda." / "EXEMPLO Beta" | baratas L88, L93, L101, L102, L116; privacidade L96 | sim |
| Empresa | "EXEMPLO Gama Controle de Pragas Ltda." / "EXEMPLO Gama" | restaurantes L69, L74, L85, L86 | sim |
| Licença | "nº EXEMPLO-000001", "nº EXEMPLO-000002", "nº EXEMPLO-000003" | baratas L72, L91; restaurantes L72; privacidade L94, L96 | sim |
| Órgão emissor | "emitida por EXEMPLO (órgão de vigilância sanitária)" | baratas L72, L91; restaurantes L72; privacidade L94 | sim |
| Endereço | "Rua EXEMPLO, 000, São Paulo, SP"; "Avenida EXEMPLO, 000, São Paulo, SP" | baratas L74, L93; restaurantes L74 | sim |
| Preço | "a partir de R$ EXEMPLO"; "contrato mensal a partir de R$ EXEMPLO"; "não informou preço … (EXEMPLO)" | baratas L80, L99, L114–116; restaurantes L82 | sim (na L116 o "EXEMPLO" está no nome e na data da mesma linha da tabela) |
| Data | "00/00/0000 (EXEMPLO)" — 15 ocorrências | início L50; baratas L60, L76, L80, L95, L114–116; restaurantes L60, L76, L82; privacidade L57 | sim, todas (busca por `00/00/0000` sem "(EXEMPLO)" logo depois: nenhuma) |
| E-mail | "EXEMPLO@EXEMPLO.example" | início L18 (JSON-LD), L115; rodapé das outras três; privacidade L57, L75, L86, L99, L125 | sim |
| Código da mensagem | "ZO-BAR-EXEMPLO"; "EMP-REST-EXEMPLO" | baratas L84; restaurantes L86 | sim |
| Versão do texto | "EXEMPLO-0.1" | privacidade L57 | sim |
| Responsável pelo site | "EXEMPLO (razão social e CNPJ de EXEMPLO)" | rodapé das 4; privacidade L57, L86 | sim |
| Quantidade de empresas | "2 (EXEMPLO)"; "Duas empresas licenciadas (EXEMPLO)"; "Uma empresa licenciada (EXEMPLO)" | início L84; baratas L59; restaurantes L59 | sim |
| Bairros e zonas atendidos | listas seguidas de "(EXEMPLO)" | baratas L78, L97, L136; restaurantes L78, L80 | sim (os nomes de bairro são reais, o que o pedido admite) |
| Prazo | "até 5 dias úteis (EXEMPLO de prazo adotado pelo site…)" | privacidade L128 | sim |
| Endereços absolutos | `https://EXEMPLO.example/…` | canônicos, JSON-LD, `robots.txt` L25 | sim |
| Telefone | — | — | não há nenhum |
| Depoimento, avaliação, estrela, nota | — | — | não há nenhum ("estrela" só em comentário de HTML, baratas L10 e restaurantes L10; "avalia" só em "não avalia produtos", baratas L129) |

- **Nome de pessoa física:** nenhum. **Nome de empresa real do setor:** nenhum.
- **Nomes reais que aparecem e não são empresa de exemplo:** "WhatsApp" (canal do botão, em três páginas); "Anvisa"
  (na citação da RDC 622); no `robots.txt`, "ChatGPT", "Googlebot", "Bingbot" e os nomes dos robôs `OAI-SearchBot`,
  `ChatGPT-User`, `GPTBot`. São nome de norma, de canal e de identificador técnico; não pedem "EXEMPLO".
- A faixa G1 de início, baratas e restaurantes diz "Todo nome de empresa, licença, endereço, preço e data nesta página
  é EXEMPLO"; a da privacidade (L24) troca por "Texto de EXEMPLO… não é parecer jurídico".

## 3. LEIA-ME × páginas × desenho

### 3.1 Blocos `data-bloco` × LEIA-ME

| Página | `data-bloco` no HTML | No LEIA-ME? |
|---|---|---|
| início | G1, G2, G3, G4, I1, I2, I3, I4, I5, I6, I7 | todos (L31–34, L45–51) |
| baratas | G1–G4, P0, P1, P2, P2a, P2b, P3 (4 vezes: botão e aviso de cada empresa), P4, P5, P6, P7, P8 | todos (L57–66; P2a e P2b na linha de P2) |
| restaurantes | G1–G4, E0, E1, E2, E3 (2 vezes), E4, E5, E6, E7 | todos (L72–79) |
| privacidade | G1–G4, V0, V1, V2, V3, V4, V5, V6, V7, V8 | todos (L85–93) |

- **Inverso:** todo código das tabelas do LEIA-ME (G1–G4, I1–I7, P0–P8, E0–E7, V0–V8) existe na página
  correspondente. As linhas sem código (`<head>`, "Dados estruturados", "Sem script", `estilo.css`, `robots.txt`,
  "Frase depois de P2") também existem (a frase: baratas L105).
- **Sem linha no LEIA-ME:** a frase equivalente da página de empresa (restaurantes L89) — entra na correção 4.
- O LEIA-ME (L25) diz que cada bloco tem um comentário com o mesmo código: P2a, P2b e o segundo P3 (baratas L87–102)
  não têm comentário próprio. Sem efeito; não peço correção.

### 3.2 Sorteio declarado — 0 falha em 12 (2 parciais)

- **Lista sorteada:** as 56 linhas de dados das sete tabelas do LEIA-ME (L18–23, L31–39, L45–51, L57–66, L72–79,
  L85–93, L99–105), numeradas de 1 a 56 na ordem do arquivo, sem as linhas de cabeçalho.
- **Comando** (semente `item7-2026-11-13`; rodado duas vezes, mesmo resultado; `shuf` do uutils coreutils 0.10.0,
  OpenSSL 3.5.5):
  `seq 1 56 | shuf -n 12 --random-source=<(openssl enc -aes-256-ctr -pbkdf2 -pass pass:"item7-2026-11-13" -nosalt </dev/zero 2>/dev/null)`
- **Saída:** `10 40 12 18 33 16 51 41 31 43 35 7`
- **Critério, fixado antes do sorteio** (classifiquei as 56 linhas antes de sortear): **falha** = a seção citada não
  existe, não diz o que a linha lhe atribui, não justifica o bloco, ou a linha descreve o bloco de um jeito que a
  página desmente; **parcial** = a seção existe e justifica o bloco no essencial, mas a citação é imprecisa ou
  incompleta.

| # | Linha do LEIA-ME | Seção citada | Existe? | Diz aquilo? | Justifica o bloco como está na página? | Resultado |
|---|---|---|---|---|---|---|
| 10 | L34, G4 (rodapé) | D 2, linha "quem somos"; D 3.4, "Navegação e links"; D 5.2 | sim (D L68, L123, L274–276) | sim: "sem lista de bairros no rodapé" é literal; a exclusão por página ou e-mail está em 5.2 | sim: rodapé das 4 páginas traz responsável, contato, links para privacidade e `#excluir`, e nenhuma lista de bairros | **bate** |
| 40 | L79, E7 (atalho fixo) | D 3.4, "Celular primeiro…" | sim (D L126) | **em parte:** o desenho diz "botão de WhatsApp pequeno e fixo, nunca intersticial" | em parte: a página (restaurantes L124; `estilo.css` L127–135) tem um atalho fixo para o bloco "Quem executa", não um botão de WhatsApp. É mais prudente e combina com D 4.1, mas a linha não diz que se afasta da letra de 3.4 | **parcial** (correção 9) |
| 12 | L36, dados estruturados | D 3.4, "Dados estruturados"; D 2, linhas de `Organization` e de avaliações | sim (D L124, L64, L66) | sim | sim: `Organization` só no início; `BreadcrumbList` nas outras três; nenhum `LocalBusiness`, estrela ou `FAQPage`; nomes da trilha iguais aos visíveis. Observações na seção 4(f) | **bate** |
| 18 | L47, I3 (por praga) | D 3.1, T2; D 3.2, "Começar por praga e por região" | sim (D L77, L97) | sim: seis guias, as mesmas seis pragas | sim (início L64–75) | **bate** |
| 33 | L72, E0 (trilha) | D 3.4, "Navegação e links" | sim (D L123) | sim (trilha) | sim (restaurantes L48–54). Observação: o nível "Para empresas" não é tipo de página em D 3.1 — correção 8 | **bate** |
| 16 | L45, I1 (título e abertura) | D 1, itens 1 e 2; D 3.4, "Abertura da página" e "Data de revisão visível" | sim (D L31–41, L119, L121) | sim; a abertura é marcada PREMISSA, como a linha diz | sim (início L48–50) | **bate** |
| 51 | L100, sem estrelas, nota, depoimento, avaliação | D 2, linha das avaliações | sim (D L66) | sim | sim: nenhuma das quatro páginas tem (seção 2) | **bate** |
| 41 | L85, V0 (trilha) | D 3.4 | sim (D L123–124) | sim (a linha não diz qual linha da tabela; é a de navegação) | sim (privacidade L46–51; igual ao JSON-LD L14–17) | **bate** |
| 31 | L65, P7 ("Veja também") | D 3.4, "Navegação e links" | sim | sim | sim: os quatro itens que a linha lista são os da página (baratas L142–147) | **bate** |
| 43 | L87, V2 (botão do WhatsApp) | D 5.1, tabela de passos; itens "Para quantas empresas" e "Como a pessoa pede a exclusão" | sim (D L183–196) | sim | sim: os cinco itens de privacidade L64–68 repetem os passos 2 a 5 e os dois itens; "pode apagar o código" está em D L198–199 | **bate** |
| 35 | L74, E2 ("Quem executa") | D 4.1 | sim (D L139–150) | sim para os seis campos | em parte: os seis campos de 4.1 estão na página e acima do botão (restaurantes L69–83, botão na L85); mas o bloco tem mais dois campos, "Atende" (público) e "Preço informado", que não são de 4.1 e vêm de D 3.1 (T6, T3) e D 3.4 | **parcial** (correção 10) |
| 7 | L31, G1 (faixa do protótipo) | nenhuma seção do desenho: a linha diz que vem do portão | — | — | sim: a faixa está nas quatro páginas e o portão pede a marca "EXEMPLO" | **bate** |

**Falhas: 0 em 12. Parciais: 2 em 12** (linhas 40 e 35).

### 3.3 Varredura das 56 linhas — o que não bate

**Não bate (1):**

- **L77, E5.** O LEIA-ME diz "três itens com norma citada e três perguntas sem afirmação". Na página (restaurantes
  L102–107) só **dois** itens citam norma (art. 22; arts. 5º e 21); o terceiro, o comprovante (L104), não cita
  nenhuma. Correção 5.

**Batem em parte (8):**

| Linha | Bloco | O que não fecha | Correção |
|---|---|---|---|
| L59 | P2 | "D 4.1, campo a campo" — o campo "Preço informado pela empresa" (baratas L79–80, L98–99) não está em D 4.1; vem de D 3.1 (T3) e D 3.4 ("Data de revisão visível") | 10 |
| L74 | E2 | o mesmo, mais o campo "Atende" (público), que vem de D 3.1 (T6) | 10 |
| L62 | P4 | cita D 3.1, T9, que pede em cada linha "o nome e o número da licença de quem informou" e o caminho para a ficha (D L84); a tabela (baratas L111–118) só tem o nome. A base certa é T3 ("preço informado por elas", D L78) | 11 |
| L66 | P8 | D 3.4 (L126) diz "botão de WhatsApp pequeno e fixo"; o protótipo põe um atalho para o bloco. A linha explica a escolha ("não a um contato"; D 4.1), mas não a registra como diferença em relação ao desenho | 9 |
| L79 | E7 | o mesmo, sem a explicação | 9 |
| L76 | E4 | "D 4.3, último parágrafo (afirmação sobre norma, saúde ou produto só com fonte oficial)" — o parágrafo (D L170–171) fala das páginas T2 e de "risco à saúde, de produto ou de segurança"; não diz "norma" e não trata de T6. Vale por analogia, e a linha não diz isso | 12 |
| L89 | V4 | "texto igual ao do desenho" — não é igual: falta a última parte e há três diferenças pequenas (seção 4(b)) | 6 |
| L102 | sem página por bairro | "D 3.3 (0 na versão 0)" — o "0 na versão 0" está em D 3.1, linha T5 (D L80); D 3.3 só dá as condições | 13 |

**Batem (47):** L18–23 (os quatro tipos T1, T3, T6, T11 existem em D 3.1 e correspondem às páginas; `robots.txt` em
D 3.4); L31–39 (G1 a `robots.txt`: D 4.2 confere palavra por palavra; D 10, premissas 8 e 15 existem e dizem aquilo);
L45–51 (I1 a I7: D 1, itens 1 e 2; D 5.1, passos 1 a 5; T2 com as mesmas seis pragas; T4 e D 4.4; T6; T8 e premissa
10; D 2 "quem somos" e D 4.1 "Publicidade"); L57, L58, L60, L61, L63, L64, L65 (P0, P1, P3, frase, P5, P6, P7); L72,
L73, L75, L78 (E0, E1, E3, E6); L85–88, L90–93 (V0 a V3, V5 a V8: D 5.1 "Endereço IP" e premissas 9 e 15; os quatro
itens de D 5.2; premissa 4; os artigos da tabela "De onde vem cada parte"; os quatro primeiros itens de D 5.3); L99,
L100, L101, L103, L104, L105.

### 3.4 Outras afirmações do LEIA-ME conferidas

- L107–112, "Páginas do desenho que não foram prototipadas… aparecem como texto cinza com '(não prototipada)'": a
  lista não inclui a página de condomínios (T6), que aparece em cinza no início (L96) e em restaurantes (L115), nem o
  nível "Para empresas" da trilha (restaurantes L51); e inclui T7 (ficha) e T9 (preços), que **não aparecem** em
  página nenhuma. Correção 8.
- L3–5, horários: os arquivos alterados por último têm hora 22:20:01; o LEIA-ME diz "alinhada às 22:21". Diferença de
  um minuto; sem pedido de correção.

## 4. Fidelidade ao desenho

### (a) Aviso ao lado do botão × D 5.1, passo 2 (D L186)

| Página | Texto | Confere? |
|---|---|---|
| baratas L84 (Alfa) | igual ao do desenho, com "EXEMPLO Alfa" no lugar de "EXEMPLO"; acrescenta a mensagem pronta do passo 3, com o código "ZO-BAR-EXEMPLO" e sem "em Pinheiros" | sim |
| baratas L102 (Beta) | igual ao do desenho | sim; **não menciona a mensagem pronta nem o código**, que o passo 3 dá a todo botão e que a privacidade (L66) diz existir — correção 14 |
| restaurantes L86 (Gama) | igual ao do desenho, mais a mensagem pronta com "EMP-REST-EXEMPLO" | sim |

O botão é `<a href>` com `rel="nofollow"` e, nas duas parceiras com a marca "Publicidade", `rel="sponsored nofollow"`
(baratas L83, L101; restaurantes L85): confere com D L204–205 e D L67.

### (b) Texto de consentimento × D 5.2, "Texto do formulário" (D L225–244)

| Parte do desenho | Na página (privacidade) | Confere? |
|---|---|---|
| Título "Pedir orçamento à [NOME]" | L85 | sim |
| Parágrafo "O EXEMPLO Guia é um site que indica… Responsável… Contato…" | L86 | sim, palavra por palavra |
| Campos: como quer ser chamado; telefone com WhatsApp; bairro, praga e tipo de imóvel em lista; nenhum texto livre além do nome | L88–92 | sim |
| Caixa principal, em destaque | L94 (classe `principal`, negrito em `estilo.css` L124) | sim, palavra por palavra |
| Caixa opcional da segunda empresa | L96 | sim no essencial; a página diz "licença sanitária nº" (o desenho, "licença nº") e reduz "(caixa opcional; no máximo duas empresas a mais, cada uma com a sua caixa)" a "(opcional)" |
| "Você pode não autorizar… não são usados para propaganda." | L98 | sim, palavra por palavra |
| "Para retirar a autorização ou apagar… página 'Excluir meus dados' ou [e-mail]…" | L99 | sim; "página" virou "seção", com link para `#excluir` |
| "Política de privacidade: [link]." | — | **falta** (correção 6) |

- **Nenhuma caixa vem marcada:** as duas `<input type="checkbox">` (L94, L96) não têm `checked` (busca: 0
  ocorrência); a página o diz na L82.
- **O que a "Conclusão operacional" de R (L348–356) pede:**

| Exigência | Onde está | Confere? |
|---|---|---|
| Finalidade | L94: "só para que ela me mande um orçamento de controle de pragas" | sim |
| Autorização separada e destacada para o repasse | L94: caixa própria, em negrito, não marcada | sim |
| Quem é o site e como falar com ele | L86 | sim |
| Para quais empresas, nomeadas | L94 e L96: nome e número da licença | sim |
| Quais dados vão | L94; L111 | sim |
| Pode recusar e o que acontece | L98 | sim |
| Como revogar e excluir, de graça | L99; L122–131 | sim |
| Prova guardada (versão, data e hora, o que marcou, a que empresas foi, **com data**) | L99; L114 | sim, menos a data do envio a cada empresa (correção 16) |
| Aviso a cada empresa na exclusão | L99; L127 | sim |
| Contato futuro ou propaganda é outra autorização | L98; L116; L146 | sim (o site diz que não faz) |

### (c) Bloco "Quem executa" × D 4.1 (D L139–150)

| Campo de D 4.1 | Alfa (baratas) | Beta (baratas) | Gama (restaurantes) |
|---|---|---|---|
| Nome como consta na licença | L69 | L88 | L69 |
| Número da licença e órgão emissor | L72 | L91 | L72 |
| Razão social por extenso e endereço | L74 | L93 | L74 |
| "Licença conferida pelo EXEMPLO Guia em…" e link para a consulta pública | L76 (o link é texto cinza, "link de EXEMPLO") | L95 | L76 |
| Área atendida, como declarada | L78 | L97 | L78 |
| Marca "Publicidade" quando pago | L68 | não tem (não paga destaque) | L68 |

Todos os campos estão presentes. **Posição:** em cada cartão a lista de dados vem antes do botão (baratas L70–81
antes de L83; L89–100 antes de L101; restaurantes L70–83 antes de L85). Não há botão de contato acima do bloco em
nenhuma das duas páginas; o cabeçalho não tem contato; o atalho fixo (baratas L153; restaurantes L124) leva a
`#quem-executa`, não a um contato.

### (d) Faixa fixa × D 4.2 (D L154–156)

O texto de G3 é igual, palavra por palavra, nas quatro páginas (início L42; baratas L43; restaurantes L43; privacidade
L41). Lugar: logo depois do `<header>` e antes do `<main>` e do `<h1>`, como o desenho pede. Li "fixa" como "presente
em toda página": no CSS (`estilo.css` L47–52) a faixa não fica presa à tela.

### (e) `robots.txt` × D 3.4 (D L127) e D 5.1 (D L201–205)

- Libera `OAI-SearchBot`, `ChatGPT-User`, `GPTBot` (treino: liberado por padrão, decisão do owner) e todos os demais
  (`User-agent: *`, que cobre Googlebot e Bingbot): confere com D 3.4.
- `Disallow: /ir/` está repetido nos quatro grupos (L8, L13, L18, L23), o que é necessário: um robô que tem grupo
  próprio ignora o grupo `*`. Confere com D 5.1.
- O bloco é o de `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, L493–511, mais as linhas `/ir/`,
  como o comentário da L2 diz. "Treino de modelos: não afeta a busca" tem base nesse arquivo (L474, classe A).
- `Sitemap:` aponta para `https://EXEMPLO.example/sitemap.xml`; não há `sitemap.xml` no protótipo (é exemplo).

### (f) Dados estruturados × D 3.4 (D L124)

- Tipos: `Organization` (início), `BreadcrumbList` (as outras três). Nenhum `LocalBusiness`, `AggregateRating`,
  `Review` ou `FAQPage`. Confere.
- **Só o que está visível:** os nomes dos itens das três trilhas são iguais aos da trilha visível. No `Organization`,
  nome e e-mail estão visíveis (rodapé, L115). Duas observações:
  1. a descrição (início L17) é paráfrase: a palavra "intermediário" não está no texto visível do início (está na
     descrição `<meta>`, L7; a ideia está na faixa, L42) — correção 22;
  2. os itens intermediários das trilhas têm endereço (`/zona-oeste/`, `/para-empresas/`) de página que o protótipo
     não tem e que na tela aparece sem link; `/para-empresas/` nem é tipo de página em D 3.1 — correção 8.

## 5. Restrições do item 2 nas páginas

Busca, sem distinção de maiúsculas, nos quatro HTML, no CSS e no `robots.txt`:

| Ideia vedada ou condicionada (D 4.3; R, seção (b), L239–251) | Palavras procuradas | Achado |
|---|---|---|
| Medo, risco à saúde | medo, risco, perig-, doenç-, contamin-, infest-, saúde, criança, animais, pet | só "informação de saúde" em privacidade L111 ("Não pedimos…"); não é texto de medo |
| "Aprovado", "recomendado", órgão público como selo | aprovad-, recomend-, especialista, ensaio, ministério, vigilância, anvisa, selo, certificad-, verificad- | "órgão de vigilância sanitária" só como descrição de quem emitiu a licença (baratas L72, L91; restaurantes L72; privacidade L94), que é o que o art. 22, caput, pede; "Anvisa" só na citação da RDC 622 (início L102; baratas L126; restaurantes L102). Nenhum uso como chancela |
| "Inócuo", "seguro", "atóxico", "natural", ausência de efeito adverso | inócu-, segur-, atóxic-, natural, cheiro | só "a segurança desse canal" (privacidade L112), sobre o canal de entrega do pedido |
| "24 horas", "garantia", "melhor preço", "a melhor" | 24 h, garant-, melhor, líder, qualidade, confiá-, rápid-, urgen-, emergência, grátis | só "A Lei… garante" (privacidade L136). "De graça" (privacidade L99) e "não custa nada" (L130) referem-se à exclusão de dados, que a lei manda ser gratuita (R L306–307) |
| "Nossa equipe", "nossos técnicos", "nossa licença" | noss- | nenhuma. A primeira pessoa aparece só em "conferimos" (início L49), "nos informou" (início L58; baratas L59), "apagamos", "avisamos", "guardamos", "não pedimos" (privacidade) — sempre atos do site, nunca do serviço |
| Promessa de posição | posição, primeiro lugar | só "Onde a posição ou o destaque de uma empresa for pago" (início L108): explica a marca "Publicidade" |
| "Garantido/verificado pelo Google" | google | só "Googlebot" em comentário do `robots.txt` (L20) |
| Estrelas, avaliação, depoimento | estrela, avalia-, depoimento, satisf- | nenhum no texto visível (seção 2) |

- **Página que oferece o serviço sem nomear empresa e licença:** nenhuma. Início (T1) não tem botão nem pedido de
  orçamento; baratas nomeia duas empresas e restaurantes uma, com licença e órgão; a privacidade nomeia as empresas no
  formulário de exemplo. Região sem licenciada aparece como "Nenhuma por enquanto. Veja os guias por praga" (início
  L85–88), como pede D 4.4.
- **Dependências vedadas:** nenhum perfil de empresa, mapa, endereço do site como unidade (o rodapé não tem endereço
  do site), avaliação, link comprado ou número de WhatsApp do site. A privacidade diz o contrário, expressamente (L112,
  L113, L143).
- **O que achei fora da lista de palavras e que encosta na regra de propaganda:**
  1. **Página de empresa oferece o serviço "em São Paulo" inteira** (restaurantes L6, L7, L58, L59), mas a única
     empresa nomeada declara atender "Zona Oeste, Zona Sul e Centro" (L78). D 4.1 (L149) diz que a página só oferece o
     serviço onde a licenciada nomeada declara atender. Correção 3.
  2. **"As empresas indicadas podem pagar ao site para aparecer. Onde a posição ou o destaque… for pago, a indicação
     leva a marca Publicidade"** (início L108). Lida ao pé da letra, a frase admite empresa que paga para aparecer e
     não leva a marca. R (L217–218, L233–235) e D 4.1 (L150) ligam a marca a "posição ou destaque pago"; se pagar para
     constar da lista é ou não "destaque" é ponto para o advogado. Correção 7. (Levantamento, não parecer.)
  3. "Indicada pelo EXEMPLO Guia" e "Licença conferida pelo EXEMPLO Guia em…" são afirmações do site sobre terceiros;
     vêm do desenho (D 4.1, 4.2) e pedem prova guardada (CDC, art. 38; R L223–224). Não é falha do protótipo; fica
     para a lista do advogado da fase 1.

## 6. Afirmações de fato nas páginas (fora dos valores EXEMPLO)

| # | Afirmação | Onde | Fonte citada na página? | A fonte, como descrita em R, diz aquilo? |
|---|---|---|---|---|
| 1 | Toda propaganda de empresa de controle de pragas tem de trazer a identificação da empresa no órgão licenciador e o número da licença | início L102 | sim: RDC 622/2022, art. 22 | sim (R L186–187, [N]) |
| 2 | Toda propaganda… tem de trazer "o número da licença sanitária e o órgão que a emitiu" | baratas L126; restaurantes L102 | sim: art. 22 | sim, como paráfrase: a norma fala em "identificação dela nos órgãos licenciadores competentes, bem como o número de sua licença"; R lê assim na conclusão (i) (L233–234) |
| 3 | O serviço só pode ser contratado com empresa especializada; a nota tem de ser de pessoa jurídica | baratas L127; restaurantes L103 | sim: arts. 5º e 21 | sim (R L184–185, [N]). O título do item, "Nota fiscal em nome da empresa", é ambíguo — correção 15 |
| 4 | O comprovante do serviço é entregue pela própria empresa | baratas L128; restaurantes L104; e, na faixa G3 das 4 páginas, "a nota fiscal e o comprovante são dela" | **não** | R só traz o comprovante dentro da inferência (iii) (L246–251), sem artigo. **Sem fonte** — correção 5 |
| 5 | O servidor "como todo site" anota cada acesso (data, página, endereço IP) | privacidade L75 | não | "como todo site" é generalização sem fonte — correção 17 |
| 6 | O endereço IP pode ser dado pessoal | privacidade L75 | não | R não levantou o ponto (D L209–213 o diz). A própria página avisa, na L76: "[A REVER com advogado]… não foi levantado no estudo". **Lacuna declarada** |
| 7 | O site "não liga o endereço IP ao toque no botão"; "registra só que o botão foi tocado (data, página e empresa)" | privacidade L75, L66; baratas L84, L102; restaurantes L86 | é afirmação do site sobre si mesmo | **Não se sustenta com o que o desenho descreve** — ver abaixo, correção 1 |
| 8 | A lei não fixa o prazo de resposta ao pedido de exclusão | privacidade L128 | não | R diz que o prazo "ainda não [foi] fixado em regulamento" (L332–334, [S], perguntas frequentes da autoridade). Bate; falta citar — correção 17 |
| 9 | A LGPD garante: retirar a autorização (art. 8º, § 5º); eliminação (art. 18, VI); saber que pode não autorizar e a consequência (art. 18, VIII); comunicação do pedido de exclusão a quem recebeu os dados (art. 18, § 6º) | privacidade L136 | sim: Lei 13.709/2018 e os artigos | sim (R L306–307 [N]; L324–325 [N]; L352 [S]; L328–331 [N]). O § 6º tem exceção ("comprovadamente impossível ou esforço desproporcional") que a página não repete; a promessa do site (L127) é mais larga que a lei, o que não é erro |
| 10 | Retirar a autorização e pedir exclusão não custa nada | privacidade L99, L130 | pelo art. 8º, § 5º, citado na L136 | sim ("procedimento gratuito e facilitado", R L306–307) |
| 11 | Treino de modelos não afeta a busca do ChatGPT | `robots.txt` L15 | sim: comentário da L2 remete a `docs/estudo/03b_chatgpt.md`, seção 9 | sim (L474 desse arquivo) |
| 12 | O que a norma de serviços de alimentação pede | restaurantes L95 | — | **não há afirmação:** o bloco é "[A ESCREVER, com fonte oficial]" e diz que o ponto não foi levantado. Correto |

Itens 4 a 6 de restaurantes L105–107 e o item 4 de baratas L129 são perguntas, não afirmações sobre norma, saúde ou
produto. Não há afirmação sobre saúde nem sobre produto em página nenhuma.

**Sobre a afirmação 7 (a de maior peso).** D 5.1 (L201–205) faz o botão apontar para um endereço do próprio site
(`/ir/…`) que anota o toque e redireciona. D 3.4 (L132) pede o registro de acesso bruto do servidor, e a privacidade
(L75) diz que o servidor "anota cada acesso (data, página pedida e endereço IP)". O pedido a `/ir/…` **é** um acesso:
no registro bruto ele fica com data, endereço e IP — ou seja, o IP fica ligado ao toque, a menos que o desenho mande
excluir esse endereço do registro ou cortar o IP nele. Como está, a página promete "não liga" (L75) e "registra só"
(L66 e os três avisos) algo que a arquitetura descrita não garante. A origem é o desenho (L209–211); o protótipo
repete. Não digo o que a lei exige aqui (ponto não levantado); digo que o texto e o mecanismo não fecham.

## 7. Qualidade mínima de marcação

| Item | Conferido | Resultado |
|---|---|---|
| `lang` | `<html lang="pt-BR">` nas 4 | sim |
| `<title>` único | 4 títulos diferentes, cada um coerente com o `<h1>` | sim |
| Um só `<h1>` | 1 por página; ordem de títulos sem salto (h1 › h2 › h3) | sim |
| `viewport` | nas 4 | sim |
| `rel="canonical"` | nas 4, para `https://EXEMPLO.example/…` da própria página | sim |
| `charset` | `utf-8` nas 4 | sim |
| Links relativos existem no disco | todos os `href` relativos das 4 páginas resolvidos por programa: todos existem | sim |
| Âncoras existem | `#pragas`, `#regioes`, `#quem-executa`, `#excluir` (inclusive vindas de outra página): existem. `#botao-de-exemplo` (3 botões): **não existe**, de propósito | sim, com a observação da correção 20 |
| Texto alternativo | não há imagem; os campos desativados têm `aria-label`; as navegações têm `aria-label`; a trilha usa `aria-current` | sim |
| Contraste (calculado pela fórmula de luminância relativa) | texto 16,0:1; link 9,1:1 (8,3:1 sobre o cinza do rodapé); texto cinza `.np`/`.revisao` 8,4:1; botão branco sobre verde 7,1:1; faixa do protótipo 8,8:1 | sim. Contorno de foco `#f59e0b` sobre branco: 2,15:1, abaixo de 3:1 — correção 21 |
| Nada cobre a tela | um só elemento preso à tela: `.atalho` (`position: sticky; bottom: 0`, `estilo.css` L127–135), uma linha de texto. Nenhum `position: fixed`, nenhuma janela | sim |
| Celular primeiro | uma coluna; uma só regra `@media (min-width: 40rem)` | sim |

**Não abri as páginas em navegador** (regra desta verificação): a conferência é do código, não da tela renderizada.

## 8. Forma do LEIA-ME

| Item | Resultado |
|---|---|
| Em português | sim |
| Caminhos absolutos | sim: tabela de arquivos (L18–23), desenho (L10), "Como abrir" (L116). Os títulos de seção (L41, L53, L68, L81) usam o caminho relativo da página, já dado por extenso na tabela |
| Diz que nada foi publicado | sim (L7: "Nada foi publicado, comprado, cadastrado nem enviado") |
| Jurídico como levantamento, não parecer | sim (L11–12); a faixa da privacidade repete (privacidade L24) e marca três pontos "[A REVER/DEFINIR com advogado]" (L76, L112, L115) |
| Estado declarado | sim (L3–5: "Ainda não verificada") |

## 9. Correções pedidas

### De conteúdo

1. **Endereço IP × toque no botão.** `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` L75 ("não
   liga o endereço IP ao toque no botão") e L66 ("registra só…"); avisos em
   `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L84 e L102 e em
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L86. O toque passa por um
   endereço do site (`/ir/…`), e o registro de acesso guarda o IP de cada pedido, inclusive desse. Corrigir primeiro
   em `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (L132, L186, L201–213): ou o desenho manda não gravar
   IP (ou gravá-lo cortado) nos pedidos a `/ir/`, ou o texto passa a dizer o que de fato fica registrado. Depois,
   alinhar as cinco linhas das páginas.
2. **Regiões do início × área da empresa de exemplo.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` L84–88 diz "2" na Zona Oeste e "Nenhuma por enquanto" na
   Zona Sul e no Centro; `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L78 diz
   que a EXEMPLO Gama atende "Zona Oeste, Zona Sul e Centro". Ou a área da Gama vira só "Zona Oeste" (e a conta do
   início, 3), ou a tabela do início diz o que conta (por exemplo, "empresas com página de praga na região").
3. **Página de empresa oferece o serviço na cidade inteira.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L6, L7, L58 e L59 ("em São
   Paulo", "na cidade de São Paulo") × L78 (três zonas). Dizer na abertura as zonas que a empresa declara atender (D
   4.1, D L149).
4. **Falta a frase da exclusão na página de empresa.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L89 não traz "Para pedir a
   exclusão do que você enviou, fale com a empresa com quem conversou", que está em baratas L105 e que D 5.1 (D
   L193–194) pede. Acrescentar a frase e uma linha "Frase depois de E2" em
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` (depois da L75).
5. **Comprovante sem fonte.** `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L128 e
   `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L104. Ou citar o artigo da
   norma, depois de lido na fonte e registrado em R, ou escrever como pergunta sem afirmação ("Peça o comprovante do
   serviço executado"). Acertar junto: o comentário de baratas L122 ("só o que tem norma citada") e
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L77 ("três itens com norma citada": são dois).
6. **Texto de consentimento não é igual ao do desenho.**
   `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` L84–101: falta a última parte, "Política de
   privacidade: [link]" (D L244) — pode ser "Política de privacidade: esta página"; L96 diz "licença sanitária nº" e
   "(opcional)" onde o desenho diz "licença nº" e "(caixa opcional; no máximo duas empresas a mais…)"; L99 diz "seção"
   onde o desenho diz "página". Ou igualar, ou registrar as diferenças em
   `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L89, que hoje diz "texto igual ao do desenho".
7. **Pagamento sem a marca "Publicidade".** `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` L108: "podem
   pagar ao site para aparecer" seguido de marca só "onde a posição ou o destaque… for pago". Redigir de modo que não
   sobre empresa pagante sem marca (por exemplo: "Quando uma empresa paga para aparecer ou para ter destaque, a
   indicação dela leva a marca Publicidade"), e levar o ponto ao advogado da fase 1.

### Menores

8. **Nível "Para empresas".** `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html`
   L17 (JSON-LD, `/para-empresas/`) e L51 (trilha): D 3.1 não tem essa página (T6 são 2 páginas; D L81 e L89). Tirar
   o nível ou incluir a página no desenho. Em `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L109–112:
   incluir condomínios (T6) e esse nível na lista do que não foi prototipado, e tirar a afirmação de que T7 e T9
   "aparecem como texto cinza" (não aparecem).
9. **Atalho fixo × desenho.** `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L66 e L79: dizer que o
   atalho para "Quem executa" **substitui** o "botão de WhatsApp pequeno e fixo" de D 3.4 (D L126), e por quê; ou
   acertar D L126.
10. `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L59 e L74: "D 4.1" não cobre os campos "Preço
    informado" e "Atende"; acrescentar D 3.1 (T3, T6) e D 3.4 ("Data de revisão visível").
11. `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L62: trocar "D 3.1, T9" por "D 3.1, T3", ou pôr o
    número da licença em cada linha da tabela
    (`/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L111–118), como T9 pede.
12. `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L76: dizer "por analogia com D 4.3, último parágrafo
    (que trata de T2)" e citar D 3.1, T6; o parágrafo não fala em "norma".
13. `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L102: "0 na versão 0" está em D 3.1 (T5), não em
    D 3.3.
14. `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L102: o aviso da EXEMPLO Beta não
    fala da mensagem pronta com código, que todo botão tem (D L187). Acrescentar, como na L84.
15. `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L127 e
    `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L103: "Nota fiscal em nome
    da empresa" pode ser lido como nota emitida **para** a empresa (na página de restaurante, o restaurante). R
    (L269–270) registra que o art. 21 pede nota de pessoa jurídica, sem dizer "da que executa". Sugestão: "Nota fiscal
    emitida por pessoa jurídica".
16. `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` L114: acrescentar a data do envio a cada
    empresa ("…e a que empresas o pedido foi enviado, com a data"), como em R L353–355 e D L272–273.
17. `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` L75: tirar "Como todo site" (generalização
    sem fonte); L128: trocar "a lei não fixa esse número" por formulação com a base de R L332–334 (o prazo de resposta
    ainda não foi fixado em regulamento).
18. `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L7 e L59: "preço informado por cada
    uma" e "o preço que ela nos informou", quando a EXEMPLO Beta não informou preço (L99). Dizer "o preço, quando a
    empresa informou".
19. `/home/ancastelo/pessoal/SEO_Project/prototipo/LEIA-ME.md` L6 e
    `/home/ancastelo/pessoal/SEO_Project/prototipo/estilo.css` L1: "sem script" → "sem programa (há um bloco de dados
    JSON-LD por página, que o navegador não executa)".
20. `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` L83 e L101 e
    `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` L85: `#botao-de-exemplo`
    não existe. Está declarado no LEIA-ME (L60); opcional: dizer no próprio aviso do protótipo que o botão não leva a
    lugar nenhum.
21. `/home/ancastelo/pessoal/SEO_Project/prototipo/estilo.css` L27: contorno de foco `#f59e0b` tem 2,15:1 sobre
    branco; usar cor com pelo menos 3:1 (opcional).
22. `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` L17: a descrição do `Organization` usa "intermediário",
    que não está no texto visível da página; usar as palavras da faixa (L42) (opcional).

## 10. O que não conferi

- A tela renderizada (não abri navegador nem servidor): quebra de linha em celular, comportamento real do atalho
  preso ao pé da tela, tamanho de toque.
- A configuração do repositório remoto (se há página publicada a partir dele).
- O texto das normas na fonte oficial: usei R como descrição da fonte, como o pedido manda.
- Os guias [A], [B], [C] e os arquivos [S] e [M] que o desenho cita: a conferência foi LEIA-ME × desenho, não desenho
  × guias (isso é do item 6).
- Validador automático de HTML: não rodei nenhum (não há dependência instalada); a leitura foi manual, com busca por
  expressão e leitura do JSON por programa.
