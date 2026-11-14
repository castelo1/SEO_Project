# Método do exemplo salvo pelo owner no X — extraído tática por tática

- **Fonte:** artigo longo publicado no X em 08/10/2026, "como usar Claude para SEO"
  (https://x.com/NicholasDulait/status/2108212094214529135). Lido inteiro no navegador pessoal em 13/11/2026, por volta de 19:35
  (Brasília). O texto **não** foi copiado para o repositório: abaixo está o método, com as minhas palavras.
- **Quem ganha com a afirmação:** o autor é cofundador de uma ferramenta paga de SEO, citada no artigo como parte
  necessária do método e com chamada para teste gratuito em três pontos do texto. Vários dos métodos são atribuídos a
  outros praticantes que vendem serviço de link, agência ou plataforma. **Classe D (vendedor) para tudo**, até que
  documentação oficial (A) ou estudo com dado (B) confirme.
- **O que o artigo pede ao leitor e foi ignorado** (conteúdo de página é dado, não instrução): criar conta na
  ferramenta, conectar o Search Console, instalar um conector, enviar e-mails de prospecção de links.
- **Limites que o próprio autor declara:** começou com audiência (o sócio é conhecido no meio); os métodos de terceiros
  são de terceiros; os números sobre o ChatGPT são de dados **franceses**; **o sistema para negócio local não é caso
  dele** ("é o que agências locais fazem"); ele escolhe disputas fáceis; em domínio novo disputando termos comerciais
  principais, o mesmo processo produz páginas na 40ª posição; o conteúdo envelhece.

Coluna "Sobe de classe se…" indica o que os guias do item 3 conferem. Coluna "Cabe aqui?" antecipa o encaixe num site
que **gera leads e não presta o serviço** (a resposta definitiva depende do item 2).

## Parte 1 — Escolher palavras-chave que pagam

| # | Tática | Classe hoje | Sobe de classe se… | Cabe aqui? |
|---|---|---|---|---|
| 1.1 | Mirar buscas de quem já quer contratar (serviço + cidade), não buscas informativas de vaidade. Ler a intenção olhando o que o Google já ranqueia: se dominam páginas de serviço com preço, é comercial; se dominam artigos, é informativa | D | houver documentação do Google sobre intenção/tipos de resultado, ou estudo com dado | Sim: "dedetização + bairro", "dedetizadora + praga" |
| 1.2 | Trabalhar por **padrão** de busca (mesma intenção, uma palavra muda: "[serviço] [cidade]"), não por palavra solta. Achar padrões pelo autocompletar do Google (com asterisco) e volumes no Planejador de palavras-chave | D | — (é método de trabalho; o risco está em 2.6) | Sim: praga × bairro × intenção é o mapa do item 4 |
| 1.3 | Nunca deixar o modelo inventar volume de busca; sem dado, escrever "n/d" | D (mas coincide com a regra da rodada) | — | Sim: `data/palavras_chave.csv` leva "volume: não medido" |
| 1.4 | Ordem de nove tipos de página para quem vende software (alternativa a, comparação, integração etc.) | D | — | Não se aplica (não é software) |
| 1.5 | Escolher resultados de busca que dá para ganhar com a autoridade atual: em site novo, ir no pequeno e específico (bairro e serviço específico antes da cidade inteira) | D | estudo com dado sobre dificuldade × autoridade | Sim, é a hipótese da cauda longa de `research/03_modelos_negocio_escala.md` linha 109 |
| 1.6 | Relato de fracasso: domínio novo, sem marca nem links, publicando muito de uma vez, nunca ranqueou | C/D (relato do próprio autor, sem site nem data conferíveis) | — | Alerta: é exatamente o risco de um site novo com dezenas de páginas praga × bairro |

## Parte 2 — Construir páginas que merecem ranquear

| # | Tática | Classe hoje | Sobe de classe se… | Cabe aqui? |
|---|---|---|---|---|
| 2.1 | Uma palavra-chave, uma página; antes de criar, ver no Search Console se já há página com cliques ou impressões para a busca (evitar duas páginas disputando a mesma busca) | D | documentação do Google sobre conteúdo duplicado/canonização | Sim, depois que houver site e dados |
| 2.2 | Palavras secundárias: listar as outras buscas em que a página líder também aparece e cobrir tudo numa URL; o título é o elemento de página mais forte; a descrição serve para ganhar o clique | D | documentação do Google sobre títulos e snippets (A) | Sim |
| 2.3 | Cobrir o que os três primeiros cobrem, na ordem em que respondem, **mais um elemento que ninguém tem** (questionário, calculadora, dado próprio, fotos reais, vídeo) | D | — | Sim; o "elemento a mais" tem de ser verdadeiro (ex.: como conferir a licença, tabela de preço com fonte) |
| 2.4 | O Google pune conteúdo em escala **sem originalidade**, seja feito por pessoa ou por IA; o volume em si não é a infração | D citando política do Google | **política de spam do Google ("scaled content abuse") lida na fonte → A** | Regra central para páginas praga × bairro |
| 2.5 | Um H1 com a palavra principal; dados estruturados coerentes com o que a página mostra; pelo menos cinco links internos, no corpo do texto de páginas de tema próximo, para cada página nova | D | documentação do Google sobre links rastreáveis e dados estruturados (A para o princípio; o número "cinco" é só do autor) | Sim |
| 2.6 | Duplicar o padrão devagar; página em que só muda o nome da cidade é "página de entrada" (doorway), que a política de spam do Google cita com o exemplo de páginas por região que afunilam para uma só; cada variante precisa de algo que só ela pode dizer | D citando política do Google | **política de spam do Google ("doorway abuse") lida na fonte → A** | **Decisivo:** é o risco nº 1 do modelo praga × bairro |
| 2.7 | Ritmo constante de publicação (ex.: duas por semana; no máximo uma por dia em site novo) em vez de despejar dezenas de uma vez | D (opinião: "se eu fosse o Google…") | estudo com dado; não há documentação conhecida | Hipótese a testar; barato de seguir |
| 2.8 | Dar ao modelo um molde de página e um arquivo de processo (links internos, dados estruturados, sitemap, pedido de indexação), não um prompt solto; conferir antes de publicar o que sumiu em relação à versão anterior; publicar só com aprovação humana | D (método de trabalho) | — | Sim para a fase de construção |
| 2.9 | Atualizar o sitemap a cada publicação | D | documentação do Google sobre sitemaps (A) | Sim |
| 2.10 | Antes de publicar mais: cortar páginas sem clique, reapontar páginas para a busca que o Google já lhes dá, reagrupar por tema | C/D (caso do autor: de 1,5 mil para 15 mil cliques por mês em três meses, sem site identificado) | — | Só depois de existir site com histórico |
| 2.11 | Multilíngue: domínio de país limita; usar hreflang | D | documentação do Google sobre hreflang (A) | Não se aplica (só português, só São Paulo) |
| 2.12 | **Negócio local: ranquear o perfil de empresa, não o site.** O mapa mostra três perfis; o Google escolhe por proximidade, relevância e "autoridade" | D | **ajuda do Google sobre classificação local (relevância, distância, destaque) → A para os três fatores** | **Conflito com o item 2(a):** o perfil pertence a quem presta o serviço; um gerador de leads não tem perfil próprio |
| 2.13 | Medir o perfil numa grade de pontos da cidade e resumir em "% de pontos no top 3" | D (exige ferramenta paga) | — | **Não usar.** A grade é consulta automática de posição: vedada pela política de spam do Google para consulta automática à Busca (classe A); a página não cita o Maps, e estender a regra ao Maps é leitura do guia (b) (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção 9). O projeto não roda nem contrata grade; alternativa: dados de desempenho do próprio perfil, que só a licenciada vê (corrigido em 14/11/2026, 01:55; antes dizia "só para o perfil de uma licenciada parceira, com autorização dela") |
| 2.14 | Auditoria do perfil: várias categorias verdadeiras (até 10), 20 a 40 serviços, descrição completa, 20 fotos, atributos, postagem semanal; não deixar o modelo inventar categoria | D | documentação do Google sobre categorias/serviços (A para o que existe; os números são do autor); estudos de fatores locais (B) | Só para o perfil de uma licenciada parceira, com autorização dela |
| 2.15 | Pedir ao cliente que mencione o serviço feito no texto da avaliação | D | política de avaliações do Google (o que é permitido pedir) + estudo com dado | Só o dono do perfil pode pedir; nunca incentivar nem fabricar |
| 2.16 | Página de destino do perfil: título e H1 com categoria + cidade, mapa incorporado, categorias secundárias como H2, avaliações, endereço e telefone idênticos aos do perfil | D | estudo com dado sobre consistência de nome, endereço e telefone | Vale para o site da licenciada, não para o do gerador de leads |
| 2.17 | "Núcleo de 30": o site espelha o perfil (uma página por categoria e por serviço), ordenadas por volume de busca | D | — | Estrutura aproveitável para páginas por praga |
| 2.18 | Páginas de bairro escritas sobre o lugar (moradia, problemas comuns ali), não sobre a empresa; trocar só o nome é doorway | D citando política do Google | mesma fonte de 2.6 | Sim: define o que uma página de bairro precisa ter |

## Parte 3 — Ganhar autoridade (links)

| # | Tática | Classe hoje | Sobe de classe se… | Cabe aqui? |
|---|---|---|---|---|
| 3.1 | Site novo fica cerca de seis meses sem resultado; métricas de autoridade de ferramentas não são do Google; o placar é o Search Console | D | estudo com dado sobre tempo até ranquear (ex.: o estudo citado em `research/03_modelos_negocio_escala.md` linha 99) | Prazo a assumir no desenho |
| 3.2 | Pedir link a quem já citou a marca sem link; oferecer substituto para link quebrado | D | — | Depende de contato com terceiros: **fora da rodada**; fica como tática descrita |
| 3.3 | Pedir link a sites que ranqueiam e a listas em que há concorrentes; copiar a lista de quem aponta para concorrentes | D | — | Idem (contato) |
| 3.4 | Máquina de e-mails de prospecção em domínio parecido, com envio automático | D | — | **Não cabe:** envio em massa e domínio "parecido" são risco de spam e de reputação; proibido na rodada |
| 3.5 | Troca de links: o Google lista troca excessiva como spam; teste "eu incluiria este negócio se ele não me desse nada?" | D citando política do Google | **política de spam de links lida na fonte → A** | Regra de limite |
| 3.6 | Conteúdo citável: dado próprio, ferramenta gratuita, infográfico; presença em plataformas (vídeo, fórum, rede profissional); um perfil forte de avaliações | D | estudos com dado sobre o que atrai links | Sim: dado próprio (ex.: tabela de preços com fonte, mapa de licenciadas) é o candidato |
| 3.7 | Comprar link por último: link pago que passa crédito viola a política dos dois lados; o desfecho comum é o link ser ignorado; se comprar, cinco checagens | D citando política do Google | mesma fonte de 3.5 | **Vedado pelo portão do item 6** (o desenho não depende de link comprado) |
| 3.8 | Perfil de links "limpo demais" chama atenção (âncoras exatas, um só tipo de domínio); dois terços dos links ganhos somem com o tempo (número do próprio site do autor) | D / C | — | Informativo |

## Parte 4 — Ser citado por terceiros para aparecer nas respostas de IA

| # | Tática | Classe hoje | Sobe de classe se… | Cabe aqui? |
|---|---|---|---|---|
| 4.1 | Sem SEO não há o que a IA achar: quando o ChatGPT não sabe, ele busca na web; por isso IA vem depois do SEO | D | documentação da OpenAI sobre a busca do ChatGPT (A) | Sim; conferido no guia `03b_chatgpt.md` |
| 4.2 | Dados de um praticante francês que diz rodar 1 milhão de perguntas por mês no ChatGPT: respostas com fonte vêm de busca; o treino tem atraso de cerca de um ano e meio; "ele busca no Google"; fontes giram todo mês; autoridade do domínio não é o filtro | D (vende plataforma de links; dado da **França**, método não publicado) | estudo com amostra e método expostos; **a afirmação "busca no Google" contradiz a hipótese do Bing e precisa de fonte primária** | Ponto disputado a tratar no guia `03b_chatgpt.md` |
| 4.3 | O ChatGPT reescreve a conversa em duas a cinco buscas curtas ("melhor + termo + ano + país"; "avaliações + marca"; "alternativa a + concorrente"); otimizar para essas buscas, não para a pergunta do usuário | D | documentação da OpenAI sobre reescrita de consulta (A) + estudo com dado | Sim: "melhor dedetizadora São Paulo 2026", "dedetizadora confiável + bairro" entram no roteiro de teste |
| 4.4 | O Google diz que não há requisito extra nem otimização especial para aparecer nos resumos de IA; não gastar tempo com `llms.txt` | D citando documentação do Google | **documentação do Google sobre recursos de IA lida na fonte → A** | Sim |
| 4.5 | Colocar-se em primeiro no próprio ranking deixou de render citação; o modelo passou a citar o ranking de terceiros | D (caso do sócio, um teste ao vivo) | estudo com dado | Para nós: o site **não** deve se autodeclarar "a melhor"; listas de licenciadas com critério exposto |
| 4.6 | Ser listado em rankings de terceiros; troca de rankings; renovar todo ano com o ano no título | D | — | Troca é contato com terceiros e encosta na política de troca de links: fora da rodada; registrar como disputado |
| 4.7 | Citação barata (R$-equivalente a 10–20 euros) renderia o mesmo que mídia grande; redes de blogs | D (quem afirma vende links) | — | **Não cabe:** é compra de link/citação; vedado pelo portão do item 6 |
| 4.8 | Reddit: participação muito diferente por motor e em queda no ChatGPT (dados franceses); método de achar os tópicos que o modelo lê e comentar identificado | D | estudos com dado sobre fontes citadas por motor (B) | Baixa aplicação no Brasil para dedetização; verificar que fontes brasileiras aparecem (diretórios, Reclame Aqui, mapas) |
| 4.9 | Ocupar a primeira tela com outros formatos (vídeo, publicação em rede social, lista de terceiros), já que o domínio só leva duas posições | D | documentação do Google sobre diversidade de sites + observação ao vivo no item 4 | Hipótese; o item 4 registra que formatos aparecem nas buscas de dedetização |
| 4.10 | Testar as perguntas à mão, deslogado, uma vez por mês, porque a API devolve fontes diferentes do aplicativo | D | documentação da OpenAI; estudo com dado | Sim: é o desenho do roteiro `03b_chatgpt_roteiro_de_teste.md` |

## Parte 5 — Repetir toda semana

| # | Tática | Classe hoje | Sobe de classe se… | Cabe aqui? |
|---|---|---|---|---|
| 5.1 | Depois de uma mudança, esperar até dois meses antes de reverter; três meses antes de pensar em links; seis meses em domínio novo | D | documentação do Google sobre tempo para mudanças surtirem efeito (A) | Prazos a assumir |
| 5.2 | Revisão semanal no Search Console: comparar 28 dias com os 28 anteriores; separar queda de posição de queda de clique (pode ser resumo de IA acima) | D (método) | — | Sim, quando houver site; o modelo de planilha da fila de reserva usa isso |
| 5.3 | Regras do agente: ler é livre; publicar e mudar título exigem aprovação; apagar página, mexer em `robots.txt`, enviar e-mail externo e comprar ficam bloqueados; cada rejeição vira regra escrita | D (método), coerente com as regras deste projeto | — | Sim |

## O que este exemplo **não** sustenta sozinho

1. Nada aqui é caso de dedetização, de São Paulo nem de gerador de leads. O único bloco sobre negócio local (2.12–2.18)
   o próprio autor diz não ser caso dele.
2. As afirmações com número (cinco links internos, 20 fotos, 30 páginas, 25–50% do líder, seis meses, 2 por semana) não
   têm amostra nem método: são regras de bolso de vendedor.
3. As citações de política do Google (2.4, 2.6, 3.5, 3.7, 4.4) são as únicas partes que podem virar regra — **depois**
   de lidas na fonte, nos guias do item 3.
4. A tática central para negócio local ("ranquear o perfil, não o site") esbarra na restrição do item 2(a): o perfil de
   empresa não é do gerador de leads.
