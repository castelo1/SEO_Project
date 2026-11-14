# Roteiro de teste no ChatGPT — 30 perguntas de dedetização em São Paulo (para o dono rodar na conta dele)

- **Escrito em:** sexta, 13/11/2026, 20:18 (Brasília; `TZ=America/Sao_Paulo date`). Fontes lidas em 13/11/2026, entre 19:47 e 20:16.
- **Corrigido em:** sexta, 13/11/2026, concluída às 21:23 (Brasília; `TZ=America/Sao_Paulo date`), depois da verificação independente
  (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_ia_chatgpt.md`, 12 falhas
  numeradas). A correção não foi verificada de novo. Mudou: 5 perguntas de comerciante trocadas por perguntas de
  morador e de síndico (as originais foram para o apêndice), urgência redistribuída, coluna `rede`, repetições
  obrigatórias.
- **Por que existe:** a sessão não abre o ChatGPT nem digita em página. Não há estudo com dado sobre quais fontes o
  ChatGPT cita para serviço local **no Brasil** (seção 5.4 de
  `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md`). Este roteiro produz esse dado.
- **O que ele mede:** quem o ChatGPT cita (empresas e fontes) quando um morador ou síndico de São Paulo pede
  dedetização. **Não mede posição.**

## Legenda das classes de evidência

| Classe | O que é | Vira regra? |
|---|---|---|
| A | documentação oficial lida na página | sim |
| B | estudo com amostra, método e dado expostos (o conflito de quem publica vai anotado) | sim, com o limite da amostra e o país |
| C | reportagem, depoimento relatado, pesquisa de opinião | só hipótese |
| D | vendedor sem método exposto | não |

## Em que o desenho do roteiro se apoia

| Escolha do roteiro | Evidência | Fonte · data da fonte · lida em 13/11/2026 | Classe | Quem ganha |
|---|---|---|---|---|
| Uma rodada é amostra agregada, não posição; conta-se **frequência**; repetir um subconjunto é obrigatório | menos de 1 chance em 100 de duas execuções darem a mesma lista (ChatGPT e Google IA juntos; 2.961 execuções; EUA presumido). Os autores listam "quantas execuções bastam" como questão em aberto e dão, como orientação prática (opinião, não resultado medido), "usually at least 60-100X" — número que este roteiro **não atinge** (seção 4) | SparkToro e Gumshoe · https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/ · 28/01/2026 | B | a Gumshoe vende monitoramento de IA |
| Idem, em busca local | 23% de coincidência entre repetições; 10% de respostas sem empresa; 4,1 empresas por resposta em média (cerca de 200 mil buscas; país não declarado) | BrightLocal · https://www.brightlocal.com/research/local-ai-visibility-study/ · 16/09/2026 | B | BrightLocal vende monitoramento local |
| Registrar a conta, o plano e o modelo | conta gratuita em modo instantâneo e conta paga em modo de raciocínio puxam resultados de origens diferentes; cerca de um terço das perguntas repetidas trocou de origem (1.249 respostas; corpus em inglês, sem recorte por país) | Resoneo · https://think.resoneo.com/chatgpt-retrieval/ · jul–ago/2026 | B | consultoria de SEO |
| Registrar se buscou na web; não forçar a busca na primeira passada | 14,4% das respostas **continham buscas derivadas** (66,6 milhões de respostas; todos os países). O estudo **só tem sessões gratuitas deslogadas**: não compara com sessão logada e, pela correção que a própria Ahrefs fez (releitura do verificador independente), o número não é "14,4% buscaram na web" | Ahrefs · https://ahrefs.com/blog/query-fan-out-chatgpt/ · 12/10/2026 | B | Ahrefs vende ferramenta de SEO |
| Testar à mão, no aplicativo, e não por API | **"API ≠ aplicativo":** uma B (Resoneo) apoia; os autores da SparkToro tratam como questão em aberto; não é consenso. Dado da Resoneo: o modelo "puro" repete buscas em 61–71% dos casos, contra 0–17% no aplicativo | Resoneo (acima); SparkToro e Gumshoe (acima) | B | idem |
| Registrar mapa e cartões de local | no modo instantâneo a resposta sobre empresas vem com mapa; no modo de raciocínio o mapa some | Resoneo (acima) | B | idem |
| Registrar tipo de fonte (diretório, mapa, site de empresa…) | em inglês, o Yelp esteve em 80% das respostas locais (EUA, Reino Unido, Austrália; 60.970 checagens). No Brasil: sem dado | BrightLocal · https://www.brightlocal.com/resources/ai-directory-sources/ · 26/08/2026 | B | BrightLocal vende cadastro em diretórios |
| Localização do aparelho desligada | o compartilhamento é opcional e vem desligado; um teste achou resultados "perto de mim" a cerca de 45 minutos | Search Engine Roundtable, citando notas de versão da OpenAI · https://www.seroundtable.com/chatgpt-location-sharing-41128.html · 31/03/2026 | C | veículo do setor |
| Chat temporário (ou memória desligada) para isolar a memória | "If memory is enabled, ChatGPT may use relevant saved memories when rewriting a search query." Que a memória muda a busca **deixou de ser premissa**: conferido na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). **Continua não conferido** que o chat temporário deixa a memória de fora: por isso a instrução de ler o aviso do próprio aplicativo (seção 1) | OpenAI, "Searching the web with ChatGPT" · https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt · a página diz "atualizada há 25 dias" (por volta de 19/10/2026) | A (com a ressalva do 403) | OpenAI |
| Bairro escrito na pergunta; anotar a rede (coluna `rede`); sem VPN | a busca usa a localização geral inferida do endereço IP e pode repassá-la a provedores terceiros: "collects general location information based on your IP address and may share that general location with third-party search providers". Sem bairro na pergunta, a cidade vem do IP (perguntas 12 e 25) — conferido na ajuda oficial da OpenAI (mesma página, mesma ressalva) | OpenAI (acima) | A (com a ressalva do 403) | OpenAI |
| Coluna de mapa mesmo rodando no computador | "On iOS and Android, relevant results may also include a map." A página só menciona mapa no celular; **não diz "só"**. Se o navegador de computador mostra mapa: não conferido — a coluna registra o que aparecer | OpenAI (acima) | A para a frase; o resto é observação a fazer | OpenAI |

## 1. Preparação (10 minutos)

| Item | Como deixar | Por quê |
|---|---|---|
| **Conta** | **Passada principal: logado na sua conta, em chat temporário.** Um chat novo para cada pergunta | **Premissa, sem fonte:** logado é como a maioria das pessoas com conta usa. O plano decide de onde vêm os resultados (Resoneo, B). O chat temporário serve para a memória e o histórico não contaminarem — **confira o aviso que o próprio aplicativo mostra ao abrir o chat temporário**; se ele não disser que a memória fica de fora, desligue a memória nas configurações e anote |
| **Subamostra deslogada (obrigatória)** | Depois da rodada, repetir **uma vez** as 6 perguntas do subconjunto fixo — **1, 2, 12, 13, 16 e 29** — em janela anônima do navegador, sem entrar na conta | Deslogado é outro perfil de usuário (a ajuda da OpenAI diz que quem não está logado também pode buscar). Se ele busca menos que o logado: **não sei** — o estudo da Ahrefs só tem sessões deslogadas e não compara. Comparar os dois mostra o quanto a conta muda a resposta. Se a versão deslogada não deixar buscar, anote e pare a subamostra |
| **Repetições (obrigatórias)** | As mesmas 6 perguntas — **1, 2, 12, 13, 16 e 29** — repetidas **5 vezes, em dias diferentes**, logado, em chat temporário, com a mesma preparação da rodada | Uma execução não mede uma pergunta isolada; as repetições mostram o tamanho do ruído (regra de medição, seção 4) |
| **Plano** | Anotar o seu (gratuito, Go, Plus…) na coluna `plano` | Conta paga e gratuita se comportam de modo diferente (Resoneo, B). Se a sua for paga, a subamostra deslogada é a aproximação do que vê quem não paga |
| **Modelo** | Deixar o padrão que o aplicativo oferecer; **não** escolher modo de raciocínio nem pesquisa aprofundada. Anotar o nome exibido | **Premissa, sem fonte:** o padrão é o que o morador comum usa. O modo muda a origem dos resultados (Resoneo, B) |
| **Busca na web** | Conferir que a busca está **disponível** (não desativada nas configurações). Na primeira passada, **não** clicar no botão de buscar: deixe o ChatGPT decidir | Saber se ele busca sozinho é um dos dados. Se ele responder **sem** fonte, repita a mesma pergunta num chat novo com a busca selecionada e registre numa segunda linha, com `busca_forcada = sim` |
| **Memória** | Fora de jogo pelo chat temporário, ou desligada; anotar em `observacoes` qual dos dois | Com a memória ligada, o ChatGPT pode usar memórias salvas ao reescrever a busca — conferido na ajuda oficial da OpenAI (https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt, lida em 13/11/2026 pela sessão principal no navegador; o verificador independente recebeu erro 403 e não pôde reconferir). O **tamanho** do efeito: não sei. Por isso, isolar |
| **Localização e rede** | Compartilhamento de localização do aparelho **desligado**; **sem VPN**; rede de São Paulo, a mesma em todas as execuções se possível; anotar na coluna `rede` se foi rede de casa, rede móvel ou VPN | O bairro está escrito em 28 das 30 perguntas: é ele a variável. **Sem bairro na pergunta, a cidade vem do endereço IP** (ajuda oficial da OpenAI, mesma ressalva): é o caso das perguntas **12 e 25**, que ficam sem bairro de propósito — nelas o texto só diz "São Paulo", e a localização que o ChatGPT acrescenta à busca (a cidade, pelo que a ajuda descreve) vem do endereço IP. Com VPN ou rede de outra cidade, essas duas (e talvez as outras) mudam. Com a localização do aparelho ligada, mistura-se o bairro da pergunta com o lugar onde você está |
| **Idioma** | Aplicativo e perguntas em português do Brasil | — |
| **Dispositivo** | O mesmo em todas as rodadas (recomendo o computador, pelo navegador: é mais fácil copiar os endereços das fontes) | Aplicativo de celular e navegador podem mostrar mapa e cartões de forma diferente: a ajuda da OpenAI só menciona mapa no iOS e no Android, sem dizer que é só lá. No computador o mapa pode não aparecer; a coluna `mostrou_mapa_ou_cartoes` registra o que vier |
| **Instruções personalizadas** | Se houver, desligar durante o teste ou anotar | Podem alterar o tom e o conteúdo |

**Quanto tempo leva:** cerca de 2 a 3 minutos por execução (perguntar, esperar, abrir a lista de fontes, anotar).
Rodada das 30, no mesmo dia e na mesma faixa de horário: 60 a 90 minutos. Subamostra deslogada (6 execuções): 12 a 18
minutos. Repetições (6 perguntas em 5 dias diferentes, 30 execuções): 12 a 18 minutos por dia. Total do mês: 66
execuções, **cerca de 2h15 a 3h20**.

**Como perguntar:** copie a pergunta exatamente como está, sem acrescentar nada. Não continue a conversa: vale só a
primeira resposta. Depois de anotar, feche o chat e abra outro.

## 2. As 30 perguntas

Copie uma por vez. As 30 são de **morador (de casa ou de apartamento) ou de síndico**, como pede o portão da rodada.
As perguntas **12 e 25 não têm bairro, de propósito**: testam o pedido sem localização fina, e nelas a cidade que o
ChatGPT usa na busca vem do endereço IP (seção 1, linha "Localização e rede"). As cinco perguntas de dono de bar,
restaurante e lanchonete que estavam na primeira versão saíram das 30 e estão no apêndice, como extras opcionais.

1. Apareceu barata na cozinha do meu apartamento na Vila Mariana. Preciso de uma dedetizadora confiável aqui no bairro. Quem você indica?
2. Tem um rato andando no quintal da minha casa na Penha agora à noite. Qual empresa de desratização atende hoje na zona leste?
3. Sou síndico de um prédio de 80 apartamentos em Santana e preciso contratar dedetização e desratização das áreas comuns para o mês que vem. Quais empresas devo cotar?
4. Apareceu barata na cozinha e no banheiro do meu apartamento em Pinheiros. Quero fazer uma dedetização na semana que vem. Qual empresa do bairro você indica?
5. Achei cupim no batente da porta e no guarda-roupa do meu apartamento em Perdizes. Qual é a melhor empresa de descupinização de São Paulo para esse caso?
6. Encontrei um escorpião no banheiro de casa, no Butantã, e tenho criança pequena. O que eu faço agora e quem eu chamo hoje?
7. Acordei cheio de picadas e acho que é percevejo de cama. Moro num apartamento na Bela Vista. Que empresa resolve isso e quanto custa mais ou menos?
8. Meu cachorro pegou pulga e agora a casa inteira, no Tatuapé, está infestada. Quero contratar uma dedetização para esta semana. Qual empresa você indica?
9. De ontem para hoje começou a sair muita formiga das tomadas e do armário da cozinha do meu apartamento em Moema. Tem dedetizadora que venha ainda hoje? Qual você recomenda?
10. Os pombos tomaram conta do telhado e das sacadas do nosso condomínio na Mooca. Sou o síndico. Que empresa faz o controle de pombos ou instala tela?
11. Está tendo muito mosquito da dengue na minha rua, no Jabaquara. Existe empresa que faz controle de mosquito em casa? Qual é confiável?
12. Como eu sei se uma dedetizadora de São Paulo é licenciada pela vigilância sanitária? Onde eu consulto antes de contratar?
13. Quanto custa dedetizar um apartamento de dois quartos contra baratas na Lapa? Quero uma faixa de preço e empresas para pedir orçamento.
14. Sou síndico de um prédio residencial na Liberdade e a administradora pediu o certificado de dedetização em dia. Quais empresas emitem o comprovante e atendem a região central?
15. Qual é a melhor dedetizadora da zona norte de São Paulo? Moro numa casa no Tucuruvi e quero fazer uma dedetização geral preventiva.
16. Apareceram ratos na casa de máquinas e na garagem do nosso prédio, na Santa Cecília. Sou a síndica e os moradores estão cobrando. Quem faz desratização urgente em condomínio, ainda hoje?
17. Tem cupim subindo pela parede da minha casa no Ipiranga. Quanto custa uma descupinização e quais empresas dão garantia?
18. Achamos dois escorpiões na área de lazer do condomínio, em Itaquera, e tem criança brincando lá. Sou o síndico: o que eu faço agora e que empresa eu chamo hoje?
19. Comprei um sofá usado e acho que veio com percevejo. Moro numa casa em Santo Amaro e quero resolver hoje, antes que espalhe. Quem atende?
20. Moro num apartamento na República e todo dia tem formiga na pia e no armário da cozinha. Trabalho fora e preciso de uma empresa que faça o controle à noite ou no fim de semana. Quem você indica?
21. Os pombos fizeram ninho no telhado e na calha da minha casa na Vila Leopoldina. Tem empresa especializada em afastar pombos sem machucar os animais?
22. Com o calor, aumentou muito o pernilongo no nosso condomínio no Campo Limpo. Sou síndico. Vale contratar controle de mosquitos para as áreas comuns? Quem faz?
23. Meu gato está com pulga e o apartamento, na Casa Verde, também: não dá para esperar. A dedetização é segura para animais? Qual empresa trabalha com isso e atende ainda hoje?
24. Apareceu um ninho de baratas atrás da geladeira aqui em casa, em São Mateus, e não consigo dormir. Tem dedetizadora 24 horas que venha agora?
25. Vi um anúncio de dedetização por 99 reais em São Paulo. Isso é golpe? Como eu comparo empresas sem cair em cilada?
26. Acabei de ver um rato na cozinha do meu sobrado na Freguesia do Ó. O que é melhor: chamar uma dedetizadora ainda hoje ou resolver sozinho com ratoeira? Se for empresa, qual atende hoje?
27. Vou comprar um apartamento antigo na Consolação e a vistoria achou sinais de cupim. Que empresa faz a avaliação e o tratamento, e quanto tempo demora?
28. Vi sinais de rato na área de serviço do meu apartamento, no térreo de um prédio na Vila Prudente. Quero contratar uma desratização esta semana. Quem atende a zona leste?
29. Compare para mim três dedetizadoras bem avaliadas que atendem Pirituba: preço, garantia e se têm licença. É para uma casa com baratas e formigas.
30. Nosso condomínio no Bom Retiro quer fechar um contrato anual de controle de pragas. O que o contrato precisa ter e quais empresas de São Paulo atendem condomínios?

### Tabela das perguntas

| Nº | Praga | Bairro (região) | Urgência | Público | Tipo |
|---|---|---|---|---|---|
| 1 | baratas | Vila Mariana (sul) | planejado | morador de apartamento | confiança |
| 2 | ratos | Penha (leste) | agora/hoje | morador de casa | indicação |
| 3 | baratas e ratos | Santana (norte) | planejado | síndico | indicação |
| 4 | baratas | Pinheiros (oeste) | planejado | morador de apartamento | indicação |
| 5 | cupim | Perdizes (oeste) | planejado | morador de apartamento | comparação ("a melhor") |
| 6 | escorpião | Butantã (oeste) | agora/hoje | morador de casa | indicação |
| 7 | percevejo | Bela Vista (centro) | planejado | morador de apartamento | preço |
| 8 | pulgas | Tatuapé (leste) | planejado | morador de casa | indicação |
| 9 | formigas | Moema (sul) | agora/hoje | morador de apartamento | indicação |
| 10 | pombos | Mooca (leste) | planejado | síndico | indicação |
| 11 | mosquito | Jabaquara (sul) | planejado | morador de casa | confiança |
| 12 | geral | São Paulo (cidade) | planejado | morador (não especificado) | confiança (licença) |
| 13 | baratas | Lapa (oeste) | planejado | morador de apartamento | preço |
| 14 | geral | Liberdade (centro) | planejado | síndico | confiança (comprovante) |
| 15 | geral | Tucuruvi (norte) | planejado | morador de casa | comparação ("a melhor") |
| 16 | ratos | Santa Cecília (centro) | agora/hoje | síndica | indicação |
| 17 | cupim | Ipiranga (sul) | planejado | morador de casa | preço |
| 18 | escorpião | Itaquera (leste) | agora/hoje | síndico | indicação |
| 19 | percevejo | Santo Amaro (sul) | agora/hoje | morador de casa | indicação |
| 20 | formigas | República (centro) | planejado | morador de apartamento | indicação |
| 21 | pombos | Vila Leopoldina (oeste) | planejado | morador de casa | indicação |
| 22 | mosquito | Campo Limpo (sul) | planejado | síndico | indicação |
| 23 | pulgas | Casa Verde (norte) | agora/hoje | morador de apartamento | confiança (segurança) |
| 24 | baratas | São Mateus (leste) | agora/hoje | morador de casa | indicação |
| 25 | geral | São Paulo (cidade) | planejado | morador (não especificado) | confiança e preço |
| 26 | ratos | Freguesia do Ó (norte) | agora/hoje | morador de casa | comparação |
| 27 | cupim | Consolação (centro) | planejado | morador de apartamento | indicação |
| 28 | ratos | Vila Prudente (leste) | planejado | morador de apartamento | indicação |
| 29 | baratas e formigas | Pirituba (norte) | planejado | morador de casa | comparação |
| 30 | geral | Bom Retiro (centro) | planejado | síndico | indicação (contrato) |

**Conferência da distribuição** (contagem refeita por script sobre a tabela acima, em 13/11/2026; **cada recorte soma
30**):

- Praga: baratas 4 (1, 4, 13, 24) · baratas e formigas 1 (29) · baratas e ratos 1 (3) · ratos 4 (2, 16, 26, 28) ·
  cupim 3 (5, 17, 27) · escorpião 2 (6, 18) · percevejo 2 (7, 19) · pulgas 2 (8, 23) · formigas 2 (9, 20) · pombos 2
  (10, 21) · mosquito 2 (11, 22) · geral 5 (12, 14, 15, 25, 30). Soma: 30.
- Região: sul 6 (1, 9, 11, 17, 19, 22) · leste 6 (2, 8, 10, 18, 24, 28) · centro 6 (7, 14, 16, 20, 27, 30) · norte 5
  (3, 15, 23, 26, 29) · oeste 5 (4, 5, 6, 13, 21) · cidade inteira, sem bairro 2 (12, 25). Soma: 30.
- Urgência: agora/hoje 9 (2, 6, 9, 16, 18, 19, 23, 24, 26) · planejado 21. Soma: 30.
- Público: morador de apartamento 10 (1, 4, 5, 7, 9, 13, 20, 23, 27, 28) · morador de casa 11 (2, 6, 8, 11, 15, 17,
  19, 21, 24, 26, 29) · síndico ou síndica 7 (3, 10, 14, 16, 18, 22, 30) · morador, sem dizer casa ou apartamento 2
  (12, 25). Soma: 30. Nenhuma pergunta de comerciante.
- Tipo: indicação 17 (2, 3, 4, 6, 8, 9, 10, 16, 18, 19, 20, 21, 22, 24, 27, 28, 30) · confiança 6 (1, 11, 12, 14, 23,
  25; a 25 também fala de preço) · comparação 4 (5, 15, 26, 29) · preço 3 (7, 13, 17). Soma: 30.

**As 9 urgentes, cruzadas** (para a urgência não se confundir com a zona): por região — leste 3 (2, 18, 24) · sul 2
(9, 19) · norte 2 (23, 26) · oeste 1 (6) · centro 1 (16); por público — casa 5 (2, 6, 19, 24, 26) · apartamento 2
(9, 23) · síndico ou síndica 2 (16, 18).

**Limite dos recortes.** Com 30 perguntas, cada recorte tem pouca coisa dentro: 2 perguntas na maioria das pragas, 5
ou 6 por região, 9 urgentes. **Duas perguntas por praga não sustentam conclusão por praga**; o recorte por região e o
por urgência indicam, no máximo, uma direção a conferir; e a urgência ainda pesa mais na leste (3 das 9) do que na
oeste e no centro (1 cada). Use os recortes para levantar hipótese, não para concluir.

As perguntas 6 e 18 (escorpião) pedem orientação de emergência: o registro é só do que o ChatGPT **cita**; não é
orientação de saúde para seguir.

## 3. O que registrar por pergunta

Uma linha por execução. Se a pergunta foi repetida (repetições obrigatórias, busca forçada ou deslogado), é outra
linha. São **22 colunas** (a coluna `rede` entrou depois da primeira versão, que tinha 21).

| Coluna | O que escrever |
|---|---|
| `rodada` | ano e mês, por exemplo `2026-11` |
| `data` · `hora` | dia e hora de Brasília em que a resposta saiu (são duas colunas) |
| `n_pergunta` | 1 a 30 (ou C1 a C5, se rodar as extras do apêndice) |
| `execucao` | 1 na rodada mensal; 2 a 6 nas cinco repetições obrigatórias do subconjunto (1, 2, 12, 13, 16 e 29) |
| `conta` | `logada-temporario`, `logada-normal` ou `deslogada` |
| `plano` | gratuito, Go, Plus… ou `nenhum` (deslogado) |
| `modelo_exibido` | o nome que o aplicativo mostra |
| `rede` | `casa`, `movel` ou `vpn` — só o tipo de rede. **Não** escreva endereço IP, nome da rede, operadora nem endereço |
| `localizacao_compartilhada` | sim ou não |
| `busca_forcada` | sim se você selecionou a busca; não se o ChatGPT decidiu sozinho |
| `buscou_na_web` | sim se a resposta trouxe fontes ou o aviso de busca; senão, não |
| `qtd_empresas_citadas` | número |
| `empresas_citadas` | nomes das **empresas**, na ordem, separados por ponto e vírgula. Se o nome for de pessoa física, escreva `[pessoa física — omitido]` |
| `fontes_citadas_dominios` | só os domínios, separados por ponto e vírgula, na ordem da lista de fontes |
| `tipos_de_fonte` | para cada domínio, na mesma ordem: `site de empresa`, `diretório`, `mapa`, `imprensa`, `fórum`, `governo`, `intermediário` ou `outro` |
| `mostrou_mapa_ou_cartoes` | não, mapa, cartões ou mapa e cartões |
| `citou_licenca_ou_vigilancia` | sim se a resposta falou em licença, alvará, vigilância sanitária ou responsável técnico; senão, não |
| `apareceu_intermediario` | sim se entre as fontes ou indicações houver site de comparação, de orçamentos ou de leads; senão, não |
| `intermediarios_dominios` | quais |
| `site_do_projeto_citado` | sim, não ou `n.a.` (enquanto o site não existir) |
| `observacoes` | o que chamou atenção: respondeu sem indicar empresa, indicou empresa de outra cidade, mostrou anúncio patrocinado, pediu a localização, memória desligada ou chat temporário etc. |

Cabeçalho da planilha e duas linhas de **EXEMPLO fictício** (nomes e domínios inventados):

```csv
rodada,data,hora,n_pergunta,execucao,conta,plano,modelo_exibido,rede,localizacao_compartilhada,busca_forcada,buscou_na_web,qtd_empresas_citadas,empresas_citadas,fontes_citadas_dominios,tipos_de_fonte,mostrou_mapa_ou_cartoes,citou_licenca_ou_vigilancia,apareceu_intermediario,intermediarios_dominios,site_do_projeto_citado,observacoes
EXEMPLO-2026-11,2026-11-14,10:05,1,1,logada-temporario,gratuito,EXEMPLO modelo padrao,casa,nao,nao,sim,3,EXEMPLO Dedetizadora Alfa; EXEMPLO Controle de Pragas Beta; EXEMPLO Gama Saude Ambiental,exemplo-alfa.example; exemplo-guia-de-empresas.example; exemplo-mapa.example,site de empresa; diretorio; mapa,mapa e cartoes,nao,nao,,n.a.,EXEMPLO ficticio: indicou duas empresas de bairro vizinho
EXEMPLO-2026-11,2026-11-14,10:09,12,1,logada-temporario,gratuito,EXEMPLO modelo padrao,casa,nao,nao,nao,0,,,,nao,sim,nao,,n.a.,EXEMPLO ficticio: respondeu sem buscar e sem fonte; repetir com busca forcada em outra linha
```

Onde guardar: sugiro um arquivo por rodada em
`/home/ancastelo/pessoal/SEO_Project/data/chatgpt_rodadas/AAAA-MM.csv` (a pasta ainda não existe; criar na primeira
rodada).

## 4. Frequência e como comparar rodadas

**Regra de medição (texto igual em `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md`,
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` e
`/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt_roteiro_de_teste.md`):**

1. **Rodada mensal das 30 perguntas:** uma execução de cada pergunta, logado, em chat temporário, todas no mesmo dia.
   É uma **amostra agregada**: responde "em quantas das 30 o site ou a empresa aparece". **Ela não mede uma pergunta
   isolada.**
2. **Obrigatório, todo mês:** um subconjunto fixo de **6 perguntas** (1, 2, 12, 13, 16 e 29) repetido **5 vezes, em
   dias diferentes**, no mesmo perfil da rodada (30 execuções a mais por mês); e uma **subamostra deslogada** (janela
   anônima) das mesmas 6, **uma vez**.
3. **Limite declarado:** a SparkToro/Gumshoe dá como orientação prática repetir cada pergunta "usually at least
   60-100X" e tirar a média
   (https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/,
   28/01/2026, lida em 13/11/2026). É opinião prática dos autores, não resultado medido — a mesma página lista "quantas
   execuções bastam" como questão em aberto; a fonte é classe B de vendedor (a Gumshoe vende monitoramento de IA).
   **Este roteiro não atinge esse número:** as 6 execuções logadas por pergunta do subconjunto (1 da rodada mais 5
   repetições) mostram o tamanho do ruído; não estimam com precisão a frequência de uma pergunta.
4. **"API ≠ aplicativo":** uma B (Resoneo) apoia; os autores da SparkToro tratam como questão em aberto; não é
   consenso.

Como aplicar:

- **Sempre as mesmas 30 perguntas, no mesmo dispositivo, na mesma rede e com a mesma preparação.** Por que mensal: o
  sistema muda em escala de semanas (em 2026, o campo que mostrava a origem dos resultados sumiu em 21/07 e as
  proporções entre as origens mudaram em agosto — Resoneo, B). Rodar as 30 mais vezes no mês, com uma execução por
  pergunta, não melhora a medida de nenhuma pergunta; o esforço extra vai para as repetições do item 2.
- **As respostas variam a cada execução. Uma rodada é uma amostra agregada, não uma posição.** Não escreva "estamos em
  2º lugar". Escreva "aparecemos em 4 das 30 perguntas". Não escreva "aparecemos na pergunta 7": uma execução não
  mede uma pergunta.
- **Repetições (item 2):** chat novo a cada vez; `execucao` de 2 a 6; dias diferentes entre si. O subconjunto (1, 2,
  12, 13, 16 e 29) cobre as cinco regiões e a pergunta sem bairro, as duas urgências e os quatro tipos de pergunta.
  Se a lista de empresas mudar muito entre repetições, diferença pequena entre meses não quer dizer nada.
- **Subamostra deslogada (item 2):** as mesmas 6, uma vez, em janela anônima; `conta` = `deslogada`.

O que comparar de um mês para o outro:

| Indicador | Conta |
|---|---|
| Buscou na web | em quantas das 30 a resposta veio com fonte, sem forçar |
| Mostrou mapa ou cartões | em quantas das 30 |
| Falou de licença ou vigilância | em quantas das 30 |
| Tipos de fonte | soma de cada tipo sobre o total de fontes citadas (site de empresa × diretório × mapa × imprensa × governo × intermediário) |
| Domínios recorrentes | para cada domínio, em quantas das 30 perguntas apareceu; listar os dez primeiros |
| Empresas recorrentes | para cada empresa, em quantas das 30 apareceu |
| Intermediários | em quantas das 30 apareceu um site de comparação ou de leads, e quais |
| Site do projeto | em quantas das 30 foi citado (quando existir) |
| Logado × deslogado | para as seis perguntas do subconjunto, quantas empresas e quantos domínios coincidem |
| Ruído das repetições | para cada uma das seis perguntas do subconjunto, em quantas das 6 execuções logadas cada empresa e cada domínio apareceu |
| Recortes | os mesmos indicadores por região, por urgência e por público, **só como hipótese**; por praga não (2 perguntas por praga não sustentam conclusão — ver "Limite dos recortes", seção 2) |

Regra de leitura — **premissa minha, sem fonte** (cautela diante da variação entre execuções): só tratar como mudança o
que se repetir em **duas rodadas seguidas**.

## 5. Avisos

1. **Não cole dado pessoal nas perguntas**: nem nome, nem endereço, nem telefone, nem número do apartamento. As 30 já
   estão prontas; use-as como estão.
2. **Não clique em "ligar", "WhatsApp", "pedir orçamento", "rota" nem em qualquer botão de contato**, e não clique em
   anúncio patrocinado (cobra o anunciante). Para registrar a fonte, basta o domínio que aparece na lista.
3. **Não contate nenhuma empresa** por causa do teste.
4. **O resultado volta para o repositório sem nomes de pessoas físicas, sem telefones e sem texto de avaliação
   copiado.** Nome de empresa e domínio podem. Não cole a resposta inteira do ChatGPT: preencha só as colunas.
5. Se o ChatGPT pedir a sua localização ou sugerir lembrar algo, recuse e anote em `observacoes`.
6. Se aparecer anúncio, anote "anúncio patrocinado" em `observacoes`; ele **não** conta como empresa citada.
7. Na coluna `rede`, só o tipo (`casa`, `movel` ou `vpn`). Endereço IP, nome da rede e operadora ficam fora.

## Apêndice — Perguntas extras de comerciante (fora das 30, opcionais)

O portão da rodada pede 30 perguntas de **morador ou síndico**. As cinco abaixo são de dono de bar, restaurante ou
lanchonete; estavam na primeira versão nos números 4, 14, 20, 21 e 28 e foram trocadas por perguntas de morador e de
síndico, com a mesma praga e o mesmo bairro. **Não contam nas 30, não entram em nenhuma contagem da seção 2 nem nos
indicadores "em quantas das 30".** Se quiser rodá-las, use a mesma preparação, registre `n_pergunta` como C1 a C5 e
leia o resultado à parte. Valem os mesmos avisos: sem dado pessoal, sem clicar em botão de contato, sem contatar
empresa.

- **C1** (baratas · Pinheiros, oeste · agora/hoje · dono de bar · indicação): Tenho um bar em Pinheiros e apareceu barata no salão bem na véspera do fim de semana. Quem faz dedetização de madrugada, ainda hoje?
- **C2** (geral · Liberdade, centro · planejado · dono de restaurante · confiança, comprovante): Preciso do certificado de dedetização para a fiscalização do meu restaurante na Liberdade. Quais empresas emitem o comprovante e atendem a região central?
- **C3** (formigas · República, centro · planejado · dono de lanchonete · indicação): Tenho uma lanchonete na República e vi formigas perto da chapa e do balcão. Preciso de uma empresa que faça o controle fora do horário de funcionamento. Quem você indica?
- **C4** (pombos · Vila Leopoldina, oeste · planejado · dono de restaurante · indicação): Os pombos estão sujando as mesas da calçada do meu restaurante na Vila Leopoldina. Tem empresa especializada em afastar pombos sem machucar os animais?
- **C5** (ratos · Vila Prudente, leste · agora/hoje · dono de bar · indicação): O bar que eu administro na Vila Prudente recebeu uma reclamação de rato. Preciso de desratização ainda hoje, antes de abrir. Quem atende a zona leste com urgência?
