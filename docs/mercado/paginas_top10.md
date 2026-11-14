# Dez páginas que ranqueiam bem × a página-modelo do protótipo (fila de reserva, tarefa 2)

- **Estado:** escrito pela sessão principal em sexta, 13/11/2026, às 22:57 (Brasília, lido de `date`). Conferido por
  verificador independente (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_reserva2.md`:
  aprovado com ressalvas; os 100 valores da tabela batem com o arquivo de dados; 12 correções pedidas, aplicadas às
  23:10 e não relidas por terceiro).
- **O que é:** leitura da estrutura de dez páginas que apareceram entre os três primeiros resultados orgânicos na
  amostra do item 4, comparada com a página-modelo do protótipo
  (`/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html`), e o registro do que mudou no
  protótipo por causa disso.
- **Dados:** `/home/ancastelo/pessoal/SEO_Project/data/paginas_top10.jsonl` (uma linha por página, com todas as medidas).
- **O que não é:** não é prova de por que essas páginas ranqueiam. São dez páginas, de oito sites, lidas uma vez.
  Correlação numa amostra assim não sustenta regra (classe de evidência: observação própria, não estudo).

## 1. Como as páginas foram escolhidas

Regra, aplicada a `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` (709 resultados orgânicos de 79 buscas feitas
em 13/11/2026; amostra, não censo):

1. Contar, para cada página (domínio + caminho), em quantas buscas ela ficou entre os três primeiros orgânicos.
2. Tirar páginas de governo e a página da multinacional cujo caminho ficou cortado na planilha (rentokil.com, 4
   aparições; **não lida**).
3. Ficar com as quatro de mais aparições (16, 6, 6 e 4) e, entre as empatadas com 2, escolher de modo a cobrir os
   tipos de página: três de bairro, uma de cidade vizinha, uma de praga × cidade e uma de segmento. No máximo duas
   páginas por site.

As empatadas com 2 aparições eram 17; a escolha de seis entre elas é minha, e outra pessoa poderia escolher outras.
Ficaram de fora, entre as empatadas: páginas de tabela de preço, de certificado, de restaurantes e de zona da cidade.

## 2. Como foram lidas

- No navegador pessoal (um só navegador conectado; não é o profissional), numa aba aberta por esta sessão, entre
  22:50 e 22:53 de 13/11/2026. Só leitura: cada endereço foi aberto direto e, quatro segundos depois, um trecho de
  script **leu** a estrutura da página (contagens). Nenhum clique, nenhum formulário, nenhum aviso de cookies aceito,
  nenhum botão de WhatsApp ou de telefone tocado.
- O que o script conta: palavras do texto visível; tamanho do HTML; links (total, internos, de WhatsApp, de telefone);
  títulos e subtítulos; imagens; formulários; tipos de dados estruturados (JSON-LD); e a presença de algumas palavras.
  Números de telefone foram mascarados antes de sair do navegador; nenhum foi gravado.
- **Limites:**
  - uma leitura por página, quatro segundos depois de abrir: texto carregado mais tarde não entra (a página inicial
    de um dos sites deu só 218 palavras, provavelmente por isso);
  - "palavra de licença" quer dizer que o texto contém "CEVS", "SIVISA", "licença sanitária", "licença de
    funcionamento" ou "alvará" — **não** que haja um número, nem que ele confira;
  - "bairros citados" conta quantos de 25 nomes de bairros de uma lista minha aparecem no texto;
  - a palavra "seguro" foi achada em 3 das 10 páginas, mas o contexto não foi lido: não afirmo que seja promessa de
    ausência de risco;
  - "24 h" e "garantia" foram procuradas só no corpo do texto visível, na leitura dos quatro segundos. A página 9 traz
    as duas palavras no `<title>` e saiu "não" nas duas colunas; na página 1, o verificador independente achou
    "garantia" no conteúdo (perguntas frequentes, rodapé) e a minha leitura saiu "não". Por isso as contagens dessas
    duas palavras são **"ao menos"**;
  - um dos blocos de dados estruturados da página 3 não pôde ser lido (ficou "erro" no arquivo de dados);
  - na coluna de dados estruturados, "organização" inclui `Organization` e `Corporation`; "negócio local" inclui
    `LocalBusiness`, `ProfessionalService` e `PestControl`;
  - posição no Google é a da amostra do item 4 (uma noite, uma conta, um ponto de acesso).

## 3. As dez páginas

Aparições entre os três primeiros (e na primeira posição), na amostra: 1 — 16 (11); 2 — 2 (1); 3 — 6 (0); 4 — 6 (0);
5 — 4 (0); 6 — 2 (2); 7 — 2 (1); 8 — 2 (1); 9 — 2 (1); 10 — 2 (1).

| # | Página | Tipo | Palavras | HTML (KB) | Links internos | Subtítulos (h2+h3) | Links de WhatsApp | Bairros citados (de 25) | Dados estruturados | Palavra de licença | "24 h" | "garantia" |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `dedetizadora.srv.br/` | página inicial | 466 | 105 | 69 | 8 | 3 | 0 | trilha, organização | não | sim | não |
| 2 | `dedetizadora.srv.br/lapa/` | bairro | 771 | 90 | 44 | 7 | 3 | 3 | trilha, organização | sim | sim | sim |
| 3 | `eccocleandedetizacao.com.br/dedetizadora-sp.php` | cidade | 3227 | 447 | 462 | 7 | 3 | 5 | trilha, organização, negócio local, nota agregada, artigo | sim | não | não |
| 4 | `deltadedetizacao.com.br/dedetizacao-em-sao-paulo/` | cidade | 4017 | 384 | 227 | 78 | 8 | 10 | trilha, organização, negócio local, artigo | não | sim | sim |
| 5 | `keikodedetizadora.com.br/` | página inicial | 218 | 59 | 37 | 22 | 4 | 1 | trilha, organização, perguntas, serviço | não | sim | sim |
| 6 | `protecpragas.com.br/dedetizadora-osasco/` | cidade vizinha | 2287 | 235 | 249 | 52 | 14 | 25 | trilha, organização, nota agregada, perguntas, produto | não | sim | sim |
| 7 | `biosp.com.br/dedetizacao-de-carrapatos-e-pulgas-sao-paulo/` | praga × cidade | 1051 | 224 | 126 | 13 | 4 | 1 | trilha | sim | sim | não |
| 8 | `ecoservicos.com.br/dedetizadora-moema/` | bairro | 1326 | 97 | 47 | 12 | 5 | 2 | trilha, organização | não | sim | sim |
| 9 | `keikodedetizadora.com.br/servicos/dedetizadora-na-mooca` | bairro | 999 | 993 | 524 | 10 | 1 | 19 | trilha, organização, nota agregada, perguntas, serviço | não | não | não |
| 10 | `termitek.com.br/dedetizacao-de-condominios-sao-paulo/` | segmento (condomínio) | 1202 | 256 | 203 | 12 | 15 | 1 | trilha, organização, negócio local, nota agregada, perguntas | não | não | não |

## 4. O que as dez têm em comum, e onde variam

| Medida | Mínimo | Mediana | Máximo | Página-modelo do protótipo |
|---|---|---|---|---|
| Palavras no texto visível | 218 | 1.126,5 | 4.017 | 856 |
| Tamanho do HTML (KB) | 59 | 229,5 | 993 | 11 |
| Links internos | 37 | 164,5 | 524 | 14 links ao todo |
| Subtítulos de segundo nível (h2) | 1 | 8 | 41 | 5 |
| Tamanho do `<title>` (caracteres) | 27 | 57,5 | 67 | era 98; agora 70 |
| Tamanho da meta descrição (caracteres) | 121 | 150 | 163 | era 195; agora 158 |
| Links de WhatsApp | 1 | 4 | 15 | 2 (um por empresa) |
| Imagens | 7 | 17,5 | 168 | 0 |

- **Dez de dez** têm: trilha de navegação em dados estruturados; endereço canônico apontando para si; `viewport`;
  `lang="pt-BR"`; ao menos um link de WhatsApp.
- **Nove de dez** marcam organização em dados estruturados; **três** se marcam como negócio local; **quatro** trazem
  nota agregada de avaliações; **quatro** trazem marcação de perguntas e respostas.
- **Ao menos sete de dez** escrevem "24 h"; **ao menos cinco**, "garantia" (ver os limites da seção 2); **três** trazem alguma palavra de licença no texto; **uma**
  traz "CNPJ".
- **Cinco de dez** têm formulário na página; **nenhuma** tem mapa embutido.
- **Sete de dez** têm ao menos um subtítulo em forma de pergunta.
- Variam muito: tamanho do texto (de 218 a 4.017 palavras) e quantidade de links internos (de 37 a 524). Uma página
  de bairro tem 524 links internos e a de cidade vizinha cita os 25 nomes da minha lista de bairros. O destino desses
  links não foi medido, e **se isso se enquadra** no que a política de spam do Google chama de excesso de
  palavras-chave **não foi avaliado**. As duas páginas estão entre os três primeiros — nesta amostra, nesta noite.

## 5. O que mudou no protótipo, e por quê

| Mudança | Onde | Por quê | Base |
|---|---|---|---|
| `<title>` encurtado de 98 para 70 caracteres | `/home/ancastelo/pessoal/SEO_Project/prototipo/zona-oeste/baratas/index.html` | As dez páginas ficam entre 27 e 67 caracteres; o Google pede título "descritivo e conciso", com a marca de forma breve | guia de busca orgânica, seção 4 (classe A); esta amostra |
| Meta descrição encurtada de 195 para 158 caracteres | a mesma página | As dez ficam entre 121 e 163; o Google não fixa limite, mas corta | guia de busca orgânica, seção 4 (classe A); esta amostra |
| O mesmo corte nos títulos e descrições das outras páginas (início: 69 e 158; restaurantes: 70 e 157) | `/home/ancastelo/pessoal/SEO_Project/prototipo/index.html` e `/home/ancastelo/pessoal/SEO_Project/prototipo/para-empresas/restaurantes/index.html` | Coerência | idem |

Nada mais mudou. O número de caracteres não é regra do Google: é o que se viu em dez páginas.

## 6. O que as dez fazem e o protótipo **não** copia, e por quê

| O que fazem | Quantas | O protótipo | Base da recusa |
|---|---|---|---|
| Nota agregada de avaliações em dados estruturados | 4 | Não tem estrela nem avaliação | `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md`, seção 2 (linha das avaliações), e guia de busca orgânica, seção 5 (estrelas e origem das avaliações) |
| Marcação de perguntas e respostas | 4 | Não usa | o resultado rico de perguntas frequentes deixou de existir em 07/05/2026 (desenho, seção 3.4) |
| Marcar-se como negócio local | 3 | O site não é negócio local; usa `Organization` | desenho, seção 2 |
| "24 h" e "garantia" | ao menos 7 e ao menos 5 | Não escreve, sem prova dada pela licenciada | desenho, seção 4.3 (CDC, arts. 36 e 38) |
| Dezenas ou centenas de links internos (destino não medido) | mediana de 164,5 links internos | 14 links; sem lista de bairros | desenho, seções 3.2, 3.3 e 3.4 |
| Texto longo (mediana de 1.126,5 palavras) | — | 856 palavras, sem enchimento | o guia de busca orgânica registra que não há contagem de palavras que o Google prefira (seção 1.1) e que escrever até atingir uma contagem de palavras é sinal de conteúdo feito para o buscador (seção 3) |
| Formulário de orçamento na página | 5 | Só o botão (via A) | desenho, seção 5.2 ("Por que não na versão 0") |
| Imagens (mediana de 17,5) | — | Nenhuma | o protótipo é só HTML e CSS; foto real da licenciada pode entrar depois, com descrição verdadeira (guia de busca orgânica, seção 4, linha de imagens) |

## 7. O que isto diz ao projeto (leitura minha, marcada)

1. **Parte das páginas que estão no topo faz o que o desenho recusa:** "24 h" em ao menos 7 das 10, "garantia" em
   ao menos 5, nota agregada em 4, lista extensa de bairros ou de links em 2. O desenho supõe que dá para aparecer sem
   isso; esta amostra **não confirma** a suposição, e ela não está na lista de premissas do desenho com essas
   palavras (a premissa 1 de lá trata de a licença e o preço atraírem busca). Fica registrada aqui como premissa.
2. **A licença quase não aparece no texto dessas páginas** (3 de 10 trazem alguma palavra de licença). Isso é coerente
   com o que o mapa de busca mostrou sobre os sites inteiros (12 de 67), com a mesma ressalva: palavra achada não é
   número conferido.
3. **O único ajuste que a comparação sustenta é de forma** (título e descrição mais curtos). Do resto que as dez
   têm a mais que o protótipo, parte é recusada por regra (nota agregada, marcar-se como negócio local, "24 h" e
   "garantia" sem prova, lista de bairros) e parte é escolha de fase ou não tem base para copiar (imagens,
   formulário, marcação de perguntas, texto mais longo).
4. **Subtítulos em forma de pergunta** aparecem em 7 das 10. Não há, nos guias, fonte A ou B de que isso ajude; não
   mexi no protótipo por isso. Fica como hipótese para o plano de conteúdo.

## 8. O que não foi feito

- A página da multinacional (rentokil.com) não foi lida: o caminho ficou cortado na planilha.
- O texto das páginas não foi lido por pessoa: não digo se o conteúdo é bom, original ou de molde.
- Velocidade de carregamento, tamanho total com imagens e versão de celular não foram medidos.
- Não repeti a leitura em outro dia.
