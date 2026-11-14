# Mapa do mercado de busca — dedetização em São Paulo (item 4)

- **O que é:** quem aparece no Google quando alguém busca dedetização em São Paulo — no resultado orgânico, no bloco de
  mapa e nos anúncios — numa **amostra declarada** de 79 buscas feitas ao vivo em sexta, 13/11/2026, das 20:26 às
  21:16 (Brasília). **Não é censo, não é posição média, não é volume de busca.**
- **Arquivos:**
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_sp.csv` — 1.060 linhas, uma por resultado visto (anúncio, perfil no
    bloco de mapa, resultado orgânico), com termo, hora, logado, local exibido.
  - `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp_registro.md` — o registro de cada busca (termo, hora,
    conta logada, localização que o Google mostrou).
  - `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv` — os 157 domínios do orgânico, por frequência, com a
    classe (empresa, diretório, gerador de leads) dos mais frequentes.
  - `/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv` — 1.260 termos por praga × local × intenção, com
    "volume: não medido" (seção 10).
  - Brutos e scripts: `/home/ancastelo/pessoal/SEO_Project/data/serp_raw/` (lotes `lote_01.jsonl` a `lote_07.jsonl`,
    `coletor.js`, `monta_csv.py`, `monta_registro.py`) e `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`.
- **Fonte de todo número deste arquivo**, salvo indicação: os arquivos acima (Brasil, cidade de São Paulo, 13/11/2026).
  Para refazer as contas: `python3 /home/ancastelo/pessoal/SEO_Project/data/serp_raw/monta_csv.py`.

## 1. Em uma página

1. **A página de resultado de uma busca comercial de dedetização em São Paulo tem quatro camadas.** Em 79 buscas:
   "Visão geral criada por IA" em 73; bloco de mapa "Empresas" em 68; anúncio de texto em 60; perfil patrocinado dentro
   do bloco de mapa em 47. Só 12 buscas não tinham nenhum anúncio. A ordem vertical das camadas **não foi registrada**.
2. **O orgânico é de sites de dedetizadoras, com uma página por bairro.** 709 resultados, 157 domínios; os 10 domínios
   mais frequentes somam 39% dos resultados e os 20 mais frequentes, 57%. Nas buscas por bairro, 87% dos resultados
   são páginas internas com o nome do local no endereço (`/dedetizadora-em-pinheiros/`); em 21 das 32 buscas com bairro,
   os três primeiros são todos desse tipo.
3. **Diretório e marketplace aparecem pouco.** Um diretório (ohub.com.br) está em 21 das 79 buscas, quase sempre do
   meio da página para baixo (posição mediana 5); os demais (triider, reclameaqui, coteibem, pedegas, pestwase,
   listazn) aparecem uma ou duas vezes. Rede social e fórum: 6 resultados em 709.
4. **Quem é empresa, quem é diretório e quem é gerador de leads** entre os domínios mais frequentes: seção 7 (lido nas
   páginas de cada site por dois subagentes; classificação por leitura de 1 a 3 páginas por domínio).
5. **O bloco de mapa muda com o bairro e com o lugar de quem busca.** 64 perfis distintos em 202 linhas; três perfis
   ocupam 43% das linhas, e um deles é de Osasco — a cidade que o Google exibiu como localização do navegador em parte
   das buscas. Nas 20 buscas por bairro apareceram 37 perfis distintos. Nota mediana 5,0; 96% das linhas com nota 4,8
   ou mais; mediana de 146 avaliações por perfil.
6. **Um único anunciante domina a amostra:** aparece nos anúncios de texto de 58 das 79 buscas e como perfil
   patrocinado em 47. Nenhum anúncio foi clicado.
7. **Busca informativa de risco à saúde é do governo:** em "controle de escorpião" (cidade e Butantã), 12 dos 16
   resultados são de órgãos públicos e do Instituto Butantan; não há bloco de mapa.
8. **Não sei:** volume de busca de qualquer termo; o que a "Visão geral criada por IA" citou em cada busca (só a
   presença foi registrada); o resultado para quem busca de outro ponto da cidade, deslogado ou pelo celular; as 10
   buscas de confiança, preço e informação (grupo H), que não foram feitas (seção 2.4).

## 2. Método e amostra

### 2.1 O que foi buscado

89 consultas planejadas em oito grupos (`/home/ancastelo/pessoal/SEO_Project/data/serp_consultas.csv`), escolhidas por
mim para cobrir o que o portão pede (por praga, por bairro ou região, "24 horas", empresa × residência). **São termos
plausíveis, não os termos mais buscados:** não há volume medido (seção 10).

| Grupo | O que é | Planejadas | Feitas |
|---|---|---|---|
| A | genérica + cidade ("dedetização são paulo") | 10 | 10 |
| B | praga + cidade ("desratização são paulo") | 13 | 13 |
| C | região ("dedetizadora zona leste sp") | 5 | 5 |
| D | bairro ("dedetizadora moema"), 20 bairros das cinco regiões | 20 | 20 |
| E | praga × bairro ("descupinização pinheiros") | 12 | 12 |
| F | empresa × residência (restaurante, condomínio, apartamento, escola, indústria) | 13 | 13 |
| G | urgência ("24 horas", "urgente", "hoje", "aberta agora") | 6 | 6 |
| H | confiança, preço e informação ("dedetizadora com licença…", "quanto tempo dura…") | 10 | **0** |
| | **Total** | **89** | **79** |

### 2.2 Como foi buscado

- **Onde:** busca web do Google (`https://www.google.com/search?q=<termo>&hl=pt-BR&gl=br&pws=0`), pelo endereço, no
  navegador pessoal do owner (Chrome, computador), numa aba aberta pela sessão. **Não é o aplicativo nem o site do
  Google Maps:** o "mapa" deste arquivo é o bloco "Empresas" que a busca web mostra (em geral 3 perfis, às vezes mais
  um patrocinado).
- **Conta:** **logado** na conta Google do owner em todas as 79 (só leitura; nenhum painel aberto). O parâmetro
  `pws=0` pede resultado sem personalização; **não garante** que ela esteja ausente.
- **Localização que o Google mostrou:** "São Paulo, SP" em 33 buscas, "Osasco, SP" em 10, nenhuma em 36 (a página não
  exibiu local). O Google atribuiu ao navegador uma posição na zona oeste da Grande São Paulo; o bloco de mapa reflete
  isso (seção 5).
- **Quando:** sexta-feira à noite, 20:26 a 21:16. Hora de cada busca: lida do relógio da própria página (momento da
  navegação). Uma atualização central do Google estava em curso desde 10/11/2026
  (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`): os resultados podem estar em movimento.
- **O que se leu de cada página**, por um script que só lê o que está na tela
  (`/home/ancastelo/pessoal/SEO_Project/data/serp_raw/coletor.js`): se há "Visão geral criada por IA"; domínio dos
  anúncios de texto; nome, nota e número de avaliações dos perfis do bloco "Empresas" e do perfil patrocinado; domínio,
  caminho e título dos resultados orgânicos da primeira página (9, em geral). Telefones foram mascarados como `[tel]`
  antes de sair da página. **Nada foi clicado:** nem anúncio, nem "ligar", nem "WhatsApp", nem "rota", nem site.
- **Intervalo entre buscas:** mediana de 28 segundos (mínimo 17, máximo 224). **Três intervalos ficaram abaixo dos 20 segundos da regra da
  rodada, por erro meu na montagem do lote:** B11→B12 (18 s), D02→D03 (19 s) e E02→E03 (17 s).

### 2.3 Limites da amostra (ler antes de usar qualquer número)

1. **Um ponto, uma hora, uma conta.** Tudo foi visto de um único lugar (zona oeste da Grande São Paulo), numa sexta à
   noite, logado. O bloco de mapa depende de onde está quem busca e de quem está aberto na hora
   (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seções 4.3 e 6). O orgânico também pode
   variar.
2. **Uma busca por termo.** Sem repetição: não dá para separar o que é estável do que é ruído.
3. **Só a primeira página, só a busca web.** A lista completa do Maps não foi coletada (fica na fila de reserva 1).
4. **Ordem vertical não registrada.** O script não guardou se o bloco de mapa e os anúncios vinham acima do orgânico;
   a premissa do guia (a) de que vêm acima **continua não conferida**.
5. **"Visão geral criada por IA": só a presença.** O script detectou o rótulo na página; não registrou se o resumo
   estava aberto, o que dizia nem que fontes citava.
6. **Títulos e caminhos cortados.** Título em até 60 caracteres nos lotes 1 e 2 e em 34 nos lotes 3 a 7; caminho em 50.
   Contagens de palavras no título ("24 horas", "preço") são piso, não valor exato.
7. **Anunciante não identificado em 31 dos 102 anúncios de texto** (a leitura do domínio falhou; saiu "google.com").
8. **Tipo de página pelo endereço, não pelo conteúdo.** "Página interna por local" = o caminho contém o nome de um
   bairro ou região da lista do script. Não li as páginas: **não afirmo que sejam "páginas de entrada"** no sentido da
   política de spam do Google; isso exige ler o texto (fila de reserva 2).
9. **Consulta automática.** A política de spam do Google lista o envio de consultas automáticas entre as práticas que
   veda (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seção 8). A rodada autorizou até 600
   buscas com 20 segundos de intervalo; a decisão de manter isso está na fila do owner
   (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md`).

### 2.4 O que deu errado na coleta

- **Verificação de robô às 21:16.** Na 80ª busca válida (H01, "dedetizadora confiável são paulo"), depois de cerca de
  28 minutos de coleta contínua, o Google mostrou a página de "tráfego incomum". **Não foi resolvida.** As buscas ao
  vivo pararam por 2 horas, como manda a regra da rodada; a aba foi fechada. O grupo H ficou sem coleta.
- **Lotes de teste descartados (20:10–20:22).** Um lote de 5 buscas estourou o tempo da ferramenta, continuou rodando e
  se sobrepôs ao seguinte, com buscas a menos de 20 segundos e rótulos trocados. Descartei tudo e recomecei; desde
  então cada registro guarda o termo lido do título da própria página.
- **Queda de conexão às 20:55.** Um lote seguiu rodando sem resposta; um registro saiu duplicado (D17), removido ao
  gravar; uma busca (D18) pode ter sido enviada duas vezes.
- **Total gasto do limite de 600:** cerca de 95 buscas — 79 válidas, 1 barrada e cerca de 15 perdidas em testes e
  lotes descartados.

## 3. O que a página mostra, por grupo de busca

Número de buscas em que cada camada apareceu.

| Grupo | Buscas | Visão geral criada por IA | Bloco "Empresas" | Anúncio de texto | Perfil patrocinado no bloco |
|---|---|---|---|---|---|
| A genérica + cidade | 10 | 10 | 10 | 8 | 8 |
| B praga + cidade | 13 | 13 | 11 | 11 | 6 |
| C região | 5 | 4 | 5 | 5 | 5 |
| D bairro | 20 | 16 | 17 | 9 | 14 |
| E praga × bairro | 12 | 11 | 8 | 10 | 6 |
| F empresa × residência | 13 | 13 | 12 | 11 | 6 |
| G urgência | 6 | 6 | 5 | 6 | 2 |
| **Total** | **79** | **73 (92%)** | **68 (86%)** | **60 (76%)** | **47 (59%)** |

- **Sem resumo de IA (6):** "dedetizadora zona oeste sp", "dedetizadora mooca", "dedetização perdizes", "dedetização
  ipiranga", "dedetização campo limpo", "cupim vila mariana dedetizadora".
- **Sem bloco "Empresas" (11):** as duas de escorpião; mosquito da dengue; "dedetizadora santana" (os resultados são
  de uma empresa que se chama Santana); "dedetizadora santa cecília"; "dedetização campo limpo"; "cupim vila mariana
  dedetizadora"; percevejo na Bela Vista; pulgas no Ipiranga; "comprovante vigilância sanitária"; "dedetizadora 24h
  zona leste".
- **Contraste com o estudo citado no guia (c):** nos Estados Unidos, em 2025, a Whitespark achou resumo de IA em 15%
  das buscas de "serviço + cidade" (540 buscas, 3 cidades; classe B, amostra pequena;
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`, seção 2). Aqui, em novembro de 2026, logado,
  foi 92%. As duas medidas não são comparáveis (país, data, método), mas a premissa "busca local quase não dispara
  resumo de IA" **não vale para esta amostra**.

## 4. Resultado orgânico

### 4.1 Concentração

- 709 resultados orgânicos, 157 domínios. Os 5 mais frequentes somam 23% dos resultados; os 10 mais frequentes, 39%; os
  20 mais frequentes, 57%. 83 domínios apareceram uma única vez.
- **Primeira posição:** dedetizadora.srv.br em 16 das 79 buscas; eccocleandedetizacao.com.br em 12;
  protecpragas.com.br e keikodedetizadora.com.br em 6 cada; biosp.com.br em 5; prefeitura.sp.gov.br e
  ecoservicos.com.br em 4 cada.
- **Os dez domínios mais frequentes** (resultados · buscas em que aparece · vezes entre os três primeiros):
  dedetizadora.srv.br (45 · 45 · 30); eccocleandedetizacao.com.br (36 · 34 · 21); keikodedetizadora.com.br (29 · 29 ·
  20); uniprag.com.br (26 · 26 · 4); protecpragas.com.br (26 · 26 · 10); dedetizabem.com.br (25 · 25 · 6);
  deltadedetizacao.com.br (23 · 23 · 6); termitek.com.br (23 · 22 · 6); ohub.com.br (22 · 21 · 5); ecoservicos.com.br
  (20 · 20 · 12). A lista inteira está em `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios.csv`.
- **Por grupo, quantos domínios respondem por metade dos resultados:** A, 10 de 37; B, 9 de 45; C, 6 de 22; D, 12 de
  66; E, 17 de 62; F, 7 de 47; G, 8 de 31. A busca por praga × bairro é a mais espalhada; a de empresa × residência, a
  mais concentrada.

### 4.2 Tipo de página (pelo endereço)

Percentual dos resultados orgânicos de cada grupo.

| Grupo | Página interna por local | Página interna de serviço ou outra | Página inicial | Blog ou artigo | Governo ou universidade | Rede social ou fórum |
|---|---|---|---|---|---|---|
| A genérica + cidade (90) | 13 | 52 | 29 | 3 | 2 | 0 |
| B praga + cidade (116) | 4 | 69 | 8 | 9 | 9 | 1 |
| C região (45) | 84 | 7 | 2 | 7 | 0 | 0 |
| D bairro (181) | 87 | 2 | 7 | 2 | 0 | 2 |
| E praga × bairro (107) | 79 | 10 | 1 | 2 | 7 | 1 |
| F empresa × residência (117) | 1 | 68 | 15 | 13 | 3 | 1 |
| G urgência (53) | 32 | 34 | 26 | 8 | 0 | 0 |

- Entre os três primeiros de todas as buscas (237 resultados): 104 páginas internas por local, 85 páginas internas de
  serviço, 34 páginas iniciais, 10 de governo, 3 de blog, 1 de rede social.
- **Busca com bairro pede página do bairro.** Em 21 das 32 buscas dos grupos D e E, os três primeiros são todos páginas
  internas por local. 249 das 316 páginas por local têm o endereço em um nível só (`dominio/bairro/`).
- **Treze domínios aparecem em 5 ou mais das 20 buscas por bairro**, cada vez com a página daquele bairro:
  protecpragas.com.br (11), lunardedetizadora.com.br, keikodedetizadora.com.br e dedetizadora.srv.br (10 cada),
  primordialdedetizacao.com.br (8), dedetizadoraddpilar.com.br e biodesin.com.br (7 cada), zet-tecdedetizadora.com.br,
  ohub.com.br, hidrosampa.com.br e ambientalepragas.com.br (6 cada), grupoexpansao.com e etoprag.com.br (5 cada).
- **Domínio com o nome exato do bairro** aparece, mas pouco: dedetizadoraemmoema.com.br,
  dedetizadoranamooca.com.br, dedetizadoraemhigienopolis.com.br, dedetizadoranobutanta.com.br,
  dedetizadoranavilamadalena.com.br, dedetizadoranavilamariana.com.br e dedetizadorazonaleste.net, uma vez cada.
- **Busca de empresa (grupo F) pede página de segmento** ("dedetização para restaurantes", "condomínios", "escolas"),
  não página de bairro; aparecem ali sites de multinacionais (rentokil.com, 5 resultados; orkinbrasil.com.br e orkinsp.com.br, 1 cada) que não
  aparecem nas buscas por bairro.

### 4.3 O que os títulos dizem (piso; títulos cortados)

| No título | Todos os orgânicos (709) | Três primeiros (237) |
|---|---|---|
| telefone (mascarado) | 54 (8%) | 20 (8%) |
| "24 horas" ou "24h" | 71 (10%) | 28 (12%) |
| "preço" ou "a partir de" | 30 (4%) | 13 (5%) |
| "melhor" | 27 (4%) | 6 (3%) |
| "orçamento" | 9 (1%) | 2 (1%) |

Nenhum desses termos é mais frequente entre os três primeiros do que no conjunto: nesta amostra, **não há sinal de que
pôr telefone, "24 horas" ou "melhor preço" no título acompanhe posição melhor**. É contagem, não teste.

### 4.4 Diretórios, marketplaces, redes sociais e governo

- **ohub.com.br:** 22 resultados em 21 buscas; posições 1 a 8, mediana 5; páginas de lista por cidade, região ou
  bairro (`/empresas/dedetizacao/sp/sao-paulo/<local>`).
- **Outros sites de lista, orçamento ou reputação:** triider.com.br (2), reclameaqui.com.br (2), coteibem.com.br (1),
  pedegas.com (1), pestwase.com (1), listazn.com.br (1). GetNinjas e Habitissimo, citados na pesquisa de 25/09, **não
  apareceram** na primeira página de nenhuma das 79 buscas.
- **Rede social e fórum:** instagram.com (4), facebook.com (1), reddit.com (1, numa busca de apartamento).
- **Governo e universidade:** 23 resultados, 12 deles nas duas buscas de escorpião; os demais em pombos, morcegos,
  mosquito da dengue, "controle de pragas", "comprovante vigilância sanitária", escola e certificado. A consulta
  pública de licenças do estado (sivisa.saude.sp.gov.br) apareceu uma vez, na busca do comprovante.

## 5. Bloco de mapa ("Empresas")

- **202 linhas, 64 perfis distintos** nas 68 buscas com bloco. Três perfis respondem por 43% das linhas: ARMOR
  Dedetizadora e Desentupidora (30 buscas; cidade exibida: Osasco), SJG Controle de Pragas Urbanas (29) e Sanitech
  (27). Depois: Primordial Dedetização (10), Lunar Dedetização (8), Heloin Dedetizadora (6).
- **O bloco acompanha o lugar.** Nas buscas sem bairro (grupos A, B, F, G) os mesmos três perfis se repetem — coerente
  com a posição que o Google atribuiu ao navegador (zona oeste, perto de Osasco). Nas 17 buscas por bairro com bloco
  (grupo D) apareceram 37 perfis distintos, e os líderes mudam (Primordial em 5, Heloin e SJG em 3). **Leitura
  (inferência a partir de uma só localização):** quem busca de outro ponto da cidade vê outros perfis nas buscas sem
  bairro; o nome do bairro na busca desloca o bloco para perto do bairro.
- **Cidade exibida na linha do perfil:** São Paulo em 114 linhas, Osasco em 32, Embu das Artes em 1; 55 linhas sem
  cidade visível (endereço oculto ou texto cortado — não distingo).
- **Nota e avaliações:** das 199 linhas com nota, mediana 5,0, mínima 4,3; 96% com 4,8 ou mais. Por perfil (61 com
  número lido): mediana de 146 avaliações; um quarto tem até 42 e um quarto tem mais de 313; máximo lido, 867 (um
  perfil exibia "1,1 mil", que o script não converteu).
- **"N anos no mercado"** aparece em 98 das 202 linhas (de 3 a 35 anos).
- **Nome do perfil:** 51 dos 64 nomes trazem palavra de serviço ("dedetizadora", "controle de pragas", "cupim"); 12
  trazem local ou "24h" (por exemplo "… zona norte", "… na Vila Mariana", "… 24h SP"). **Não dá para dizer se o nome é
  o nome real da empresa:** sem o nome registrado de cada uma não se distingue nome legítimo de nome inflado
  (`/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md`, seção 8).
- **O que não foi observado:** endereço visível ou oculto, categoria, horário, data das últimas avaliações, respostas
  do dono, site e telefone de cada perfil (exigiria abrir cada perfil; fila de reserva 1).

## 6. Anúncios

- **Anúncio de texto:** 102 anúncios em 60 buscas. Domínios lidos: brasiltechs.com em 58 buscas;
  dedetizacaoexpress24horas.com em 8 anúncios; dedetizamos.com.br em 2; ddteasy.com.br, saonadedetizacao.com.br e
  mgkdedetiza.com.br em 1 cada; 31 anúncios sem domínio identificado.
- **Perfil patrocinado no bloco de mapa:** em 47 buscas, sempre o mesmo ("BRASILTECHS DEDETIZADORA", nota 4,3, 166
  avaliações).
- **Sem anúncio nenhum:** 12 das 79 buscas.
- **Não medido:** custo por clique, posição do anúncio na página, anúncios de outros horários e de outras localizações.
  Nenhum anúncio foi clicado (cobra o anunciante).

## 7. Empresa, diretório ou gerador de leads

_Seção em preenchimento: aguarda a leitura dos sites pelos dois subagentes de classificação
(`/home/ancastelo/pessoal/SEO_Project/data/serp_dominios_classe_parte1.csv` e `…parte2.csv`)._

## 8. Padrões dos primeiros colocados

_Seção em preenchimento: junta a seção 4 com a classificação da seção 7._

## 9. O que isto diz ao projeto

_Seção em preenchimento._

## 10. Mapa de palavras-chave (`/home/ancastelo/pessoal/SEO_Project/data/palavras_chave.csv`)

- **O que tem:** 1.260 termos. As 89 consultas da coleta (79 feitas, 10 planejadas) e 1.171 **combinações geradas**
  por `/home/ancastelo/pessoal/SEO_Project/data/gera_palavras_chave.py`: 14 serviços (dedetização, dedetizadora e 12
  pragas) × 26 locais (cidade, 5 regiões, 20 bairros) × 3 intenções com local (contratar, urgência "24 horas", preço),
  mais termos de confiança por local, de público (restaurante, condomínio, apartamento, empresa, escola) por cidade e
  região, e 21 termos informativos sem local.
- **Colunas:** `termo`, `praga`, `tipo_local`, `local`, `intencao`, `publico`, `volume` (sempre "não medido"),
  `origem_do_termo` (consulta da coleta ou combinação gerada), `id_na_coleta`, `situacao_na_coleta` (coletado,
  planejado ou não buscado).
- **Por intenção:** contratar 421; urgência 371; preço 368; confiança 79; informativa 21.
- **O que o arquivo não é:** lista de termos que as pessoas buscam. É uma grade de hipóteses. Uma combinação gerada
  pode não ter busca nenhuma; termos reais podem faltar (os bairros são só 20 dos distritos da cidade).
- **Como medir o volume depois (nenhum destes foi usado; os dois primeiros exigem a conta do owner; como cada
  ferramenta funciona não foi conferido em fonte nesta rodada):**
  1. **Planejador de palavras-chave do Google Ads** — colar a coluna `termo`, com local "São Paulo" e idioma
     português; registrar a faixa de buscas mensais e a data. Fica pronto para o owner: o arquivo já está no formato
     de uma coluna por termo.
  2. **Search Console**, quando houver site no ar: impressões por consulta são a medida real da demanda que o site já
     alcança (não da demanda total).
  3. **Google Trends** (página pública): só compara termos entre si, em índice de 0 a 100, e não mostra termo de
     pouco volume. Serve para sazonalidade (por exemplo escorpião e mosquito no verão), não para volume.
  4. **Sugestões do próprio Google** (autocompletar, "As pessoas também perguntam", buscas relacionadas): mostram como
     as pessoas escrevem; entram na fila de reserva 1, dentro do limite de buscas ao vivo.
- **Coluna a acrescentar quando houver medição:** `volume_faixa`, `fonte_do_volume`, `data_da_medicao`.

## 11. O que não foi feito e o que não sei

- **Grupo H (10 buscas de confiança, preço e informação):** não coletado, por causa da verificação de robô.
- **Lista completa do Google Maps** e dados de cada perfil (endereço, categoria, horário, recência das avaliações).
- **Conteúdo das páginas que ranqueiam:** tamanho, estrutura, dados estruturados, se exibem licença (a classificação
  da seção 7 leu de 1 a 3 páginas por domínio, por ferramenta que resume). A análise de 10 páginas está na fila de
  reserva 2.
- **O que a "Visão geral criada por IA" diz e cita** nessas buscas.
- **Volume de busca, custo por clique, taxa de clique.**
- **Estabilidade:** nenhuma busca foi repetida em outro dia, outra hora, outro lugar, deslogado ou no celular.
