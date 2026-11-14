# Protótipo local do site — LEIA-ME (item 7)

- **Estado:** escrita pela sessão principal em sexta, 13/11/2026, entre 22:03 e 22:10 (Brasília, lido de `date`), e
  alinhada às 22:21 à segunda versão do desenho (faixa fixa, registro de acesso, canal do formulário, `robots.txt`).
  **Ainda não verificada.**
- **O que é:** quatro páginas em HTML e CSS puros, sem script, sem dependência, sem imagem e sem fonte externa. Abrem
  direto do disco. **Nada foi publicado, comprado, cadastrado nem enviado.** Nenhum botão leva a lugar nenhum.
- **Todo nome de empresa, licença, órgão emissor, endereço, preço, data, código e e-mail é "EXEMPLO".** Não há telefone
  nem depoimento em página nenhuma (o desenho não usa avaliação nem número de telefone do site).
- **Desenho que justifica cada bloco:** `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` (abaixo, "D" + seção).
- **Natureza:** os textos que encostam em norma (propaganda, privacidade) vêm de levantamento com fonte, não de
  parecer jurídico; a política de privacidade é texto de EXEMPLO e precisa de advogado antes de qualquer uso.

## Arquivos, na ordem de abrir

| Arquivo (caminho absoluto) | Tipo de página no desenho (D 3.1) |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` | T1 Início |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | T3 Praga × região (página-modelo) |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | T6 Público: restaurante |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/privacidade/index.html` | T11 Política de privacidade e exclusão, com o texto de consentimento |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/estilo.css` | folha de estilo única |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | exemplo de `robots.txt` (D 3.4) |

Cada bloco tem, no HTML, o atributo `data-bloco` com o código da tabela abaixo e um comentário com o mesmo código.

## Blocos comuns às quatro páginas

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| G1 | Faixa "PROTÓTIPO LOCAL" | Não é parte do site: é a marca "EXEMPLO" pedida no portão do item 7 |
| G2 | Cabeçalho com o nome do site e a navegação principal | D 3.4, linha "Navegação e links" (toda página ligada por outra; texto de link descritivo) |
| G3 | Faixa fixa, no alto de toda página, logo abaixo do cabeçalho e antes do título: "indica empresas licenciadas; não é dedetizadora, não tem licença e não executa o serviço…" | D 4.2 (texto e lugar iguais aos do desenho); D 2, primeira linha da tabela |
| G4 | Rodapé: responsável pelo site, contato, links para privacidade e exclusão; **sem lista de bairros** | D 2, linha "quem somos"; D 3.4, linha "Navegação e links" (sem lista de bairros no rodapé); D 5.2 (como pedir exclusão) |
| `<head>` | `<title>` próprio; descrição; `rel="canonical"`; `viewport`; sem `nosnippet` | D 3.4, linhas "Título e título principal", "`sitemap.xml`… `rel="canonical"`", "Celular primeiro", "Sem `nosnippet`" |
| Dados estruturados | `Organization` só no Início; `BreadcrumbList` nas outras; nenhum `LocalBusiness`, nenhuma estrela, nenhum `FAQPage` | D 3.4, linha "Dados estruturados"; D 2, linhas de `Organization` e de avaliações |
| Sem script | Todo conteúdo e todo link estão no HTML; botão é `<a href>` | D 3.4, linha "Sem dependência de script" |
| `estilo.css` | Uma coluna no celular; nada cobre a tela | D 3.4, linha "Celular primeiro; sem janela que cubra a tela" |
| `robots.txt` | Libera robôs de busca e de visita, e (por padrão) os de treino; fecha a robôs o endereço `/ir/`, que registraria o toque no botão | D 3.4, linha "`robots.txt`"; D 10, premissa 8; D 5.1, "Como o clique é registrado sem script" (PREMISSA) |

## Página inicial — `index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| I1 | Título e frase de abertura que diz o que o site é, onde e o que cada indicação mostra; data de revisão | D 1, itens 1 e 2; D 3.4, linhas "Abertura da página" (PREMISSA) e "Data de revisão visível" |
| I2 | "Como funciona", em três passos; o terceiro diz que o site não recebe o número nem a conversa | D 5.1, passos 1 a 5 |
| I3 | Lista por praga (seis guias; só a página de baratas na Zona Oeste está prototipada) | D 3.1, T2; D 3.2, linha "Começar por praga e por região" |
| I4 | Tabela por região: página de empresas só onde há licenciada; nas demais, "nenhuma por enquanto" e remissão ao guia | D 3.1, T4; D 4.4 (região sem licenciada não tem página de oferta) |
| I5 | Entrada para quem contrata como empresa | D 3.1, T6; D 3.2, linha "Página de público… em vez de bairro" |
| I6 | "Como conferir a licença": o que a norma exige da propaganda e remissão ao passo a passo | D 3.1, T8; D 4.1, linhas do número da licença e de "Licença conferida"; D 10, premissa 10 |
| I7 | "Como o site ganha dinheiro" e a marca "Publicidade" | D 2, linha "quem somos"; D 4.1, linha "Marca 'Publicidade'" |

## Página-modelo de praga × região — `zona-oeste/baratas/index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| P0 | Trilha: Início › Zona Oeste › Baratas (igual à dos dados estruturados) | D 3.4, linhas "Navegação e links" e "Dados estruturados"; endereço `/zona-oeste/baratas/`: D 3.4, linha "Endereços" |
| P1 | Título e abertura (o quê, onde, quem); data de revisão; critério de ordem da lista declarado | D 3.4, "Abertura da página" (PREMISSA) e "Data de revisão visível"; D 4.3, linha "as melhores sem critério exposto" |
| P2 (P2a, P2b) | **"Quem executa"**, acima de qualquer botão: nome, número da licença e órgão emissor, razão social e endereço, data em que o site conferiu a licença, bairros que a empresa declara atender, preço informado; marca "Publicidade" na parceira que paga destaque | D 4.1, campo a campo (RDC 622, art. 22; CDC, art. 36; razão social e endereço por prudência); D 3.2, linha "O conteúdo próprio de cada página de oferta é a licença conferida" |
| P3 | Botão "Falar com a EXEMPLO … no WhatsApp" e o aviso ao lado; mensagem pronta com código; `rel="sponsored"` na parceira que paga | D 5.1, passos 2, 3 e 4 (texto do aviso igual ao do desenho); D 2, linha de `rel="sponsored"`. No protótipo o link é `#botao-de-exemplo` |
| Frase depois de P2 | "O EXEMPLO Guia não recebe o seu nome, o seu telefone nem a conversa…" | D 5.1, "Como a pessoa pede a exclusão" (o site não tem dado de contato; o que registra está na política) |
| P4 | Tabela de preço com empresa, imóvel, valor e data em que foi informado | D 3.1, T9; D 4.3, linha "sem prova guardada" (CDC, arts. 36 e 38) |
| P5 | "O que pedir à empresa antes de contratar": licença (art. 22), nota de pessoa jurídica (arts. 5º e 21), comprovante, produtos e cuidados (pergunta, sem afirmação do site) | D 4.3 (nada de "seguro", "atóxico", medo); D 2, primeira linha (contrato, nota e comprovante são da empresa) |
| P6 | Bairros atendidos, em texto; **sem** uma página por bairro | D 3.3 (as três condições); D 3.2, primeira e segunda linhas |
| P7 | "Veja também": guia da praga, região, conferir licença, página de restaurantes | D 3.4, linha "Navegação e links" |
| P8 | Atalho pequeno e fixo no pé da tela, que leva ao bloco "Quem executa" (não a um contato) | D 3.4, linha "Celular primeiro; sem janela que cubra a tela"; D 4.1 ("acima do botão") |

## Página de empresa — `para-empresas/restaurantes/index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| E0 | Trilha: Início › Para empresas › Restaurantes, bares e lanchonetes | D 3.4, "Navegação e links" |
| E1 | Título e abertura (o quê, onde, quem); data de revisão | D 3.2, linha "Página de público… em vez de bairro"; D 3.4, "Abertura da página" (PREMISSA) |
| E2 | "Quem executa", com os mesmos campos de P2 e o público que a empresa declara atender | D 4.1 |
| E3 | Botão e aviso da via A | D 5.1 |
| E4 | Bloco **"[A ESCREVER, com fonte oficial]"**: o que a norma de serviços de alimentação pede | D 4.3, último parágrafo (afirmação sobre norma, saúde ou produto só com fonte oficial). **Lacuna declarada:** essa norma não foi levantada no estudo |
| E5 | "O que perguntar no orçamento": três itens com norma citada e três perguntas sem afirmação | D 4.3; D 2, primeira linha |
| E6 | "Veja também" | D 3.4, "Navegação e links" |
| E7 | Atalho pequeno e fixo para "Quem executa" | D 3.4, "Celular primeiro…" |

## Política de privacidade — `privacidade/index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| V0 | Trilha | D 3.4 |
| V1 | Título; versão do texto; responsável pelo site e contato sobre dados | D 5.2, tabela "De onde vem cada parte", linha "Quem é o site e como falar com ele"; a versão serve à prova (D 5.2, "O que o site guarda como prova") |
| V2 | O que acontece no botão do WhatsApp: abre a conversa com a licenciada; o site não recebe número nem conversa; registra só o clique; o contato vai a **uma** empresa; exclusão se pede à empresa | D 5.1, tabela de passos e os itens "Para quantas empresas" e "Como a pessoa pede a exclusão" |
| V3 | Registro de acesso do servidor (endereço IP, que pode ser dado pessoal): menor tempo possível, sem ligar ao toque; sem cookie nem script de medição; aviso "[A REVER com advogado]" | D 5.1, item "Endereço IP" (PREMISSA de prudência; ponto não levantado); D 3.4, linha "Sem cookie e sem script de medição"; D 10, premissas 9 e 15 |
| V4 | **Formulário de exemplo, desativado, com o texto de consentimento**: campos mínimos; caixa principal não marcada que nomeia a licenciada e a licença; caixa opcional para outra empresa nomeada; recusa; não repasse; como retirar e excluir | D 5.2, "Campos" e "Texto do formulário" (texto igual ao do desenho, com EXEMPLO no lugar dos colchetes) |
| V5 | Para quantas empresas vai; que dados; por que canal o pedido chega à empresa (PREMISSA); quem fala depois; o que fica guardado como prova; prazo de guarda "[A DEFINIR com advogado]" | D 5.2, itens "Para quantas empresas", "Por que canal o pedido chega à licenciada", "Quem chama a pessoa", "O que o site guarda como prova" (prazo: não conclusivo) |
| V6 | "Excluir meus dados": pedido, exclusão, aviso imediato às empresas, confirmação em até 5 dias úteis | D 5.2, item "Como a pessoa pede a exclusão" (5 dias úteis: PREMISSA; D 10, premissa 4) |
| V7 | Direitos, com os artigos da LGPD | D 5.2, tabela "De onde vem cada parte" (art. 8º, § 5º; art. 18, VI, VIII e § 6º) |
| V8 | O que o site não faz | D 5.3 |

## O que o protótipo não tem, de propósito

| Não tem | Por quê |
|---|---|
| Perfil de empresa, mapa, endereço do site como "unidade" | D 2 (vedado pelo item 2) |
| Estrelas, nota, depoimento, avaliação | D 2, linha das avaliações |
| Telefone ou número de WhatsApp do site | D 5.3 |
| Página por bairro | D 3.3 (0 na versão 0) |
| "24 horas", "garantia", "seguro", "atóxico", "a melhor" | D 4.3 |
| Página de oferta sem empresa nomeada | D 4.4 |
| Script de medição, cookie, formulário que envia | D 3.4, linha "Sem cookie e sem script de medição" (PREMISSA); D 5.1 (clique registrado no servidor, sem script); o formulário da via B é de fase posterior (D 5.2, "Por que não na versão 0") |

## Páginas do desenho que não foram prototipadas

Guia de praga (T2), região (T4), ficha da licenciada (T7), como conferir a licença (T8), preços (T9), quem somos e
como funciona (T10), "Excluir meus dados" como página própria (T11), para dedetizadoras (T12). No protótipo elas
aparecem como texto cinza com "(não prototipada)", sem link. O portão do item 7 pede quatro páginas; estas ficam
para depois da aprovação do desenho.

## Como abrir

Abra `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` no navegador, direto do disco. Não é preciso servidor.
