# Protótipo local do site — LEIA-ME (item 7)

- **Estado:** escrita pela sessão principal em sexta, 13/11/2026, entre 22:03 e 22:10 (Brasília, lido de `date`), e
  alinhada às 22:21 à segunda versão do desenho. Conferida por verificador independente
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item7.md`: aprovado com ressalvas; 0
  falha em 12 no sorteio; 22 correções pedidas). As 22 correções foram aplicadas às 22:38 pela sessão principal e
  ainda não foram relidas por terceiro.
- **Segunda passada (14/11/2026):** um revisor novo, sem acesso à primeira verificação, releu o protótipo
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao2_item7.md`: aprovado com ressalvas; 0
  falha em 12; 11 achados, 3 de conteúdo). Os 11 foram aplicados às 01:54 pela sessão principal, junto com dois
  acertos que vêm da correção do desenho feita na mesma passada (campo "Dados pessoais" em cada empresa; última
  frase do texto de consentimento). Essas correções não foram relidas por terceiro. **Ponto em aberto** (segunda
  passada da reserva 2): os três títulos têm 70, 69 e 70 caracteres, acima do máximo de 67 visto nas dez páginas
  comparadas; não há regra do Google sobre tamanho de título no estudo, e os títulos não foram mexidos.
- **Ajuste das 22:55 (fila de reserva, tarefa 2):** títulos e meta descrições das páginas foram encurtados depois da
  comparação com dez páginas bem colocadas; o que mudou e por quê está em
  `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`, seção 5.
- **O que é:** quatro páginas em HTML e CSS puros, sem programa (só blocos JSON-LD, que são dados), sem dependência,
  sem imagem e sem fonte externa. Abrem
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

Cada bloco com código (G, I, P, E, V) tem, no HTML, o atributo `data-bloco` e, salvo os sub-blocos P2a e P2b, um
comentário com o mesmo código. A frase depois de P2 e de E2, a nota "Botão de EXEMPLO" e o cartão da empresa na
página de restaurantes não têm código.

## Blocos comuns às quatro páginas

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| G1 | Faixa "PROTÓTIPO LOCAL" | Não é parte do site: é a marca "EXEMPLO" pedida no portão do item 7 |
| G2 | Cabeçalho com o nome do site e a navegação principal | D 3.4, linha "Navegação e links" (toda página ligada por outra; texto de link descritivo) |
| G3 | Faixa fixa, no alto de toda página, logo abaixo do cabeçalho e antes do título: "indica empresas licenciadas; não é dedetizadora, não tem licença e não executa o serviço…" | D 4.2 (texto e lugar iguais aos do desenho); D 2, primeira linha da tabela |
| G4 | Rodapé: responsável pelo site, contato, links para privacidade e exclusão; **sem lista de bairros** | D 2, linha "quem somos"; D 3.4, linha "Navegação e links" (sem lista de bairros no rodapé); D 5.2 (como pedir exclusão) |
| `<head>` | `<title>` próprio; descrição; `rel="canonical"`; `viewport`; sem `nosnippet` | D 3.4, linhas "Título e título principal", "`sitemap.xml`… `rel="canonical"`", "Celular primeiro", "Sem `nosnippet`"; a descrição: D 7, linha "títulos e descrições a partir dos mesmos dados", e `/home/ancastelo/pessoal/SEO_Project/docs/mercado/paginas_top10.md`, seção 5 |
| Dados estruturados | `Organization` só no Início; `BreadcrumbList` nas outras; nenhum `LocalBusiness`, nenhuma estrela, nenhum `FAQPage` | D 3.4, linha "Dados estruturados"; D 2, linhas de `Organization` e de avaliações |
| Sem script | Todo conteúdo e todo link estão no HTML; botão é `<a href>` | D 3.4, linha "Sem dependência de script" |
| `estilo.css` | Uma coluna no celular; nada cobre a tela | D 3.4, linha "Celular primeiro; sem janela que cubra a tela" |
| `robots.txt` | Libera robôs de busca e de visita, e (por padrão) os de treino; fecha a robôs o endereço `/ir/`, que registraria o toque no botão. A linha `Sitemap:` é de EXEMPLO; o protótipo não tem `sitemap.xml`. Em cada grupo, `Disallow: /ir/` vem antes de `Allow: /` (por prudência, para robô que aplique a primeira regra que casar; observação do revisor, sem fonte no estudo). No grupo do `ChatGPT-User`, um comentário lembra que as regras podem não valer para ele (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`, seção 2) | D 3.4, linha "`robots.txt`"; D 10, premissa 8; D 5.1, "Como o clique é registrado sem script" (PREMISSA) |

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
| P2 (P2a, P2b) | **"Quem executa"**: cada empresa é identificada acima do botão dela, com nome, número da licença e órgão emissor, razão social e endereço, data em que o site conferiu a licença, bairros que a empresa declara atender, preço informado e contato da empresa para pedidos sobre dados pessoais; marca "Publicidade" na parceira que paga para aparecer | D 4.1, campo a campo (RDC 622, art. 22; CDC, art. 36; razão social e endereço por prudência); o campo "preço informado" vem de D 3.1 (T3) e de D 3.4, linha "Fatos em texto visível"; D 3.2, linha "O conteúdo próprio de cada página de oferta é a licença conferida" |
| P3 | Botão "Falar com a EXEMPLO … no WhatsApp" e o aviso ao lado (o que o site registra e o que o servidor registra); mensagem pronta com código; `rel="sponsored"` na parceira que paga | D 5.1, passos 2, 3 e 4 e item "Endereço IP" (texto do aviso igual ao do desenho); D 2, linha de `rel="sponsored"`. No protótipo o link é `#botao-de-exemplo`. Duas diferenças em relação ao desenho: o aviso traz uma frase a mais, com a mensagem pronta (passo 3 de D 5.1); e a mensagem não cita bairro (a página é de região) e o código leva "-EXEMPLO" |
| Frase depois de P2 | "O EXEMPLO Guia não recebe o seu nome, o seu telefone nem a conversa… Para pedir a exclusão… fale com a empresa" | D 5.1, "Como a pessoa pede a exclusão" (o site não tem dado de contato; o que registra está na política) |
| Nota "Botão de EXEMPLO" (antes de P7 e de E6) | Destino do link de exemplo: diz que o botão não abre o WhatsApp de ninguém | Marca "EXEMPLO" do portão do item 7; D 5.1 (no protótipo o botão não leva a lugar nenhum) |
| P4 | Tabela de preço com empresa, imóvel, valor e data em que foi informado; a empresa que paga leva a marca "Publicidade" também aqui (D 4.1: em toda indicação de empresa que paga) | D 3.1, T3 ("preço informado por elas"); D 4.3, linha "sem prova guardada" (CDC, arts. 36 e 38) |
| P5 | "O que pedir à empresa antes de contratar": dois itens com norma citada — licença (art. 22) e nota de pessoa jurídica (arts. 5º e 21) — e duas perguntas sem afirmação do site (comprovante; produtos e cuidados) | D 4.3 (nada de "seguro", "atóxico", medo); D 2, primeira linha (contrato, nota e comprovante são da empresa) |
| P6 | Remissão aos bairros declarados no bloco "Quem executa"; **sem** repetir a lista e **sem** uma página por bairro | D 3.3 (as três condições); D 3.2, primeira e segunda linhas; D 3.4, linha "Navegação e links" (bloco de texto que lista regiões é exemplo de excesso de palavras-chave) |
| P7 | "Veja também": guia da praga, região, conferir licença, página de restaurantes | D 3.4, linha "Navegação e links" |
| P8 | Atalho pequeno e fixo no pé da tela, que leva ao bloco "Quem executa" (não a um contato) | D 3.4, linha "Celular primeiro; sem janela que cubra a tela" (o desenho pede esse atalho, não um botão de contato fixo); D 4.1 ("acima do botão") |

## Página de empresa — `para-empresas/restaurantes/index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| E0 | Trilha de dois níveis: Início › Restaurantes, bares e lanchonetes. O trecho `/para-empresas/` do endereço não é página no desenho | D 3.4, "Navegação e links"; D 3.1, T6 |
| E1 | Título e abertura (o quê, onde, quem); data de revisão | D 3.2, linha "Página de público… em vez de bairro"; D 3.4, "Abertura da página" (PREMISSA) |
| E2 | "Quem executa", com os mesmos campos de P2, as regiões e o público que a empresa declara atender | D 4.1; o campo "atende" vem de D 3.1 (T6); o campo "preço informado", de D 3.1 (T3) e de D 3.4, linha "Fatos em texto visível" |
| Frase depois de E2 | "O EXEMPLO Guia não recebe o seu nome, o seu telefone nem a conversa… Para pedir a exclusão… fale com a empresa" | D 5.1, "Como a pessoa pede a exclusão" |
| E3 | Botão e aviso da via A | D 5.1 |
| E4 | Bloco **"[A ESCREVER, com fonte oficial]"**: o que a norma de serviços de alimentação pede | D 4.3, último parágrafo, por analogia: ele trata dos guias de praga (T2) e pede fonte oficial para afirmação sobre saúde, produto ou segurança; o protótipo aplica a mesma regra à página de público (D 3.1, T6). **Lacuna declarada:** essa norma não foi levantada no estudo |
| E5 | "O que perguntar no orçamento": dois itens com norma citada e quatro perguntas sem afirmação do site | D 4.3; D 2, primeira linha |
| E6 | "Veja também" | D 3.4, "Navegação e links" |
| E7 | Atalho pequeno e fixo para "Quem executa" (não a um contato) | D 3.4, "Celular primeiro…" (o desenho pede esse atalho, não um botão de contato fixo) |

## Política de privacidade — `privacidade/index.html`

| Bloco | O que é | Escolha do desenho que o justifica |
|---|---|---|
| V0 | Trilha | D 3.4 |
| V1 | Título; versão do texto; responsável pelo site e contato sobre dados | D 5.2, tabela "De onde vem cada parte", linha "Quem é o site e como falar com ele"; a versão serve à prova (D 5.2, "O que o site guarda como prova") |
| V2 | O que acontece no botão do WhatsApp: abre a conversa com a licenciada; o site não recebe nome, número nem conversa; registra o toque, e o servidor anota o acesso com o endereço IP; o contato vai a **uma** empresa; exclusão se pede à empresa | D 5.1, tabela de passos e os itens "Para quantas empresas" e "Como a pessoa pede a exclusão" |
| V3 | Registro de acesso do servidor (anota cada acesso, inclusive o toque no botão, com endereço IP, que pode ser dado pessoal, e com a identificação do navegador ou do robô): menor tempo possível, com a ressalva de que o art. 15 do Marco Civil da Internet pode exigir guarda por 6 meses e de que o regulamento (Decreto nº 8.771/2016, art. 13, § 2º, e art. 15-A) trata do mínimo a reter e da porta lógica de origem; o IP não vai para a contagem de toques nem é usado para identificar ninguém; sem cookie nem script de medição; aviso "[A REVER com advogado]" | D 5.1, item "Endereço IP" (PREMISSA de prudência; ponto não levantado); D 3.4, linha "Sem cookie e sem script de medição"; D 10, premissas 9 e 15 |
| V4 | **Formulário de exemplo, desativado, com o texto de consentimento**: campos mínimos; caixa principal não marcada que nomeia a licenciada e a licença; caixa opcional para outra empresa nomeada; recusa; não repasse; como retirar e excluir | D 5.2, "Campos" e "Texto do formulário". Texto igual ao do desenho (inclusive a última frase, corrigida na segunda passada), com três diferenças declaradas: EXEMPLO no lugar dos colchetes; "seção" em vez de "página" (no protótipo, "Excluir meus dados" é uma seção desta página); e "Política de privacidade: esta página" em vez do link |
| V5 | Para quantas empresas vai; que dados; por que canal o pedido chega à empresa (PREMISSA); quem fala depois; o que fica guardado como prova; prazo de guarda "[A DEFINIR com advogado]" | D 5.2, itens "Para quantas empresas", "Por que canal o pedido chega à licenciada", "Quem chama a pessoa", "O que o site guarda como prova" (prazo: não conclusivo) |
| V6 | "Excluir meus dados": pedido, exclusão, aviso imediato às empresas, confirmação em até 5 dias úteis | D 5.2, item "Como a pessoa pede a exclusão" (5 dias úteis: PREMISSA; D 10, premissa 4) |
| V7 | Direitos, com os artigos da LGPD | D 5.2, tabela "De onde vem cada parte" (art. 8º, § 5º; art. 18, VI, VIII e § 6º) |
| V8 | O que o site não faz | D 5.3 |

## O que o protótipo não tem, de propósito

| Não tem | Por quê |
|---|---|
| Perfil de empresa, mapa, endereço do site como "unidade" | D 2 (vedado pelo item 2) |
| Estrelas, nota, depoimento, avaliação | D 2, linha das avaliações (o desenho fala em avaliação e estrelas; estender a "depoimento" é leitura do protótipo) |
| Telefone ou número de WhatsApp do site | D 5.3 |
| Página por bairro | D 3.1, T5 (0 na versão 0); condições em D 3.3 |
| "24 horas", "garantia", "seguro", "atóxico", "a melhor" | D 4.3 |
| Página de oferta sem empresa nomeada | D 4.4 |
| Script de medição, cookie, formulário que envia | D 3.4, linha "Sem cookie e sem script de medição" (PREMISSA); D 5.1 (clique registrado no servidor, sem script); o formulário da via B é de fase posterior (D 5.2, "Por que não na versão 0") |

## Páginas do desenho que não foram prototipadas

Aparecem como texto cinza com "(não prototipada)", sem link: guia de praga (T2), região (T4), a página de
condomínios (a outra T6), como conferir a licença (T8), quem somos e como funciona (T10), "Excluir meus dados" como
página própria (T11) e para dedetizadoras (T12). **Não aparecem no protótipo:** ficha da licenciada (T7) e preços
(T9). O portão do item 7 pede quatro páginas; as demais ficam para depois da aprovação do desenho.

## Como abrir

Abra `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` no navegador, direto do disco. Não é preciso servidor.
