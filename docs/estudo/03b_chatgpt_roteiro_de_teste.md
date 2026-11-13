# Roteiro de teste no ChatGPT — 30 perguntas de dedetização em São Paulo (para o dono rodar na conta dele)

- **Escrito em:** sexta, 13/11/2026, 20:18 (Brasília; `TZ=America/Sao_Paulo date`). Fontes lidas em 13/11/2026, entre 19:47 e 20:16.
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
| Uma rodada é amostra, não posição; conta-se **frequência** | menos de 1 chance em 100 de duas execuções darem a mesma lista (ChatGPT e Google IA juntos; 2.961 execuções; EUA presumido) | SparkToro e Gumshoe · https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/ · 28/01/2026 | B | a Gumshoe vende monitoramento de IA |
| Idem, em busca local | 23% de coincidência entre repetições; 10% de respostas sem empresa; 4,1 empresas por resposta em média (cerca de 200 mil buscas; país não declarado) | BrightLocal · https://www.brightlocal.com/research/local-ai-visibility-study/ · 16/09/2026 | B | BrightLocal vende monitoramento local |
| Registrar a conta, o plano e o modelo | conta gratuita em modo instantâneo e conta paga em modo de raciocínio puxam resultados de origens diferentes; cerca de um terço das perguntas repetidas trocou de origem (1.249 respostas; majoritariamente em inglês) | Resoneo · https://think.resoneo.com/chatgpt-retrieval/ · jul–ago/2026 | B | consultoria de SEO |
| Registrar se buscou na web; não forçar a busca na primeira passada | em sessões gratuitas deslogadas, só 14,4% das respostas tinham buscas (66,6 milhões de respostas; todos os países) | Ahrefs · https://ahrefs.com/blog/query-fan-out-chatgpt/ · 12/10/2026 | B | Ahrefs vende ferramenta de SEO |
| Testar à mão, no aplicativo, e não por API | a API não reproduz o produto (o modelo "puro" repete buscas em 61–71% dos casos, contra 0–17% no aplicativo) | Resoneo (acima) | B | idem |
| Registrar mapa e cartões de local | no modo instantâneo a resposta sobre empresas vem com mapa; no modo de raciocínio o mapa some | Resoneo (acima) | B | idem |
| Registrar tipo de fonte (diretório, mapa, site de empresa…) | em inglês, o Yelp esteve em 80% das respostas locais (EUA, Reino Unido, Austrália; 60.970 checagens). No Brasil: sem dado | BrightLocal · https://www.brightlocal.com/resources/ai-directory-sources/ · 26/08/2026 | B | BrightLocal vende cadastro em diretórios |
| Localização do aparelho desligada | o compartilhamento é opcional e vem desligado; um teste achou resultados "perto de mim" a cerca de 45 minutos | Search Engine Roundtable, citando notas de versão da OpenAI · https://www.seroundtable.com/chatgpt-location-sharing-41128.html · 31/03/2026 | C | veículo do setor |
| Chat temporário para isolar a memória | **premissa não conferida**: a página de ajuda da OpenAI deu 403 | https://help.openai.com/en/articles/9237897-chatgpt-search (não abriu) | — | — |

## 1. Preparação (10 minutos)

| Item | Como deixar | Por quê |
|---|---|---|
| **Conta** | **Passada principal: logado na sua conta, em chat temporário.** Um chat novo para cada pergunta | Logado é como a maioria das pessoas com conta usa; o plano decide de onde vêm os resultados (Resoneo, B). O chat temporário serve para a memória e o histórico não contaminarem — **confira o aviso que o próprio aplicativo mostra ao abrir o chat temporário**; se ele não disser que a memória fica de fora, desligue a memória nas configurações e anote |
| **Subamostra deslogada** | Depois da passada principal, repetir as perguntas **1, 2, 3, 4, 5, 12, 13, 16, 25 e 29** em janela anônima do navegador, sem entrar na conta | Deslogado é outro perfil de usuário e busca menos (Ahrefs, B). Comparar os dois mostra o quanto a conta muda a resposta. Se a versão deslogada não deixar buscar, anote e pare a subamostra |
| **Plano** | Anotar o seu (gratuito, Go, Plus…) na coluna `plano` | Conta paga e gratuita se comportam de modo diferente (Resoneo, B). Se a sua for paga, a subamostra deslogada é a aproximação do que vê quem não paga |
| **Modelo** | Deixar o padrão que o aplicativo oferecer; **não** escolher modo de raciocínio nem pesquisa aprofundada. Anotar o nome exibido | Padrão é o que o morador comum usa; o modo muda a origem dos resultados (Resoneo, B) |
| **Busca na web** | Conferir que a busca está **disponível** (não desativada nas configurações). Na primeira passada, **não** clicar no botão de buscar: deixe o ChatGPT decidir | Saber se ele busca sozinho é um dos dados. Se ele responder **sem** fonte, repita a mesma pergunta num chat novo com a busca selecionada e registre numa segunda linha, com `busca_forcada = sim` |
| **Memória** | Fora de jogo pelo chat temporário, ou desligada; anotar em `observacoes` qual dos dois | Efeito da memória sobre a busca: não sei; por isso, isolar |
| **Localização** | Compartilhamento de localização do aparelho **desligado**; sem VPN; rede de São Paulo | O bairro já está escrito em cada pergunta: é ele a variável. Com a localização ligada, mistura-se o bairro da pergunta com o lugar onde você está |
| **Idioma** | Aplicativo e perguntas em português do Brasil | — |
| **Dispositivo** | O mesmo em todas as rodadas (recomendo o computador, pelo navegador: é mais fácil copiar os endereços das fontes) | Aplicativo de celular e navegador podem mostrar mapa e cartões de forma diferente |
| **Instruções personalizadas** | Se houver, desligar durante o teste ou anotar | Podem alterar o tom e o conteúdo |

**Quanto tempo leva:** cerca de 2 a 3 minutos por pergunta (perguntar, esperar, abrir a lista de fontes, anotar).
Passada principal: 60 a 90 minutos. Subamostra deslogada: 20 a 30 minutos. Total: **cerca de 1h30 a 2h**, de preferência
no mesmo dia e na mesma faixa de horário.

**Como perguntar:** copie a pergunta exatamente como está, sem acrescentar nada. Não continue a conversa: vale só a
primeira resposta. Depois de anotar, feche o chat e abra outro.

## 2. As 30 perguntas

Copie uma por vez.

1. Apareceu barata na cozinha do meu apartamento na Vila Mariana. Preciso de uma dedetizadora confiável aqui no bairro. Quem você indica?
2. Tem um rato andando no quintal da minha casa na Penha agora à noite. Qual empresa de desratização atende hoje na zona leste?
3. Sou síndico de um prédio de 80 apartamentos em Santana e preciso contratar dedetização e desratização das áreas comuns para o mês que vem. Quais empresas devo cotar?
4. Tenho um bar em Pinheiros e apareceu barata no salão bem na véspera do fim de semana. Quem faz dedetização de madrugada, ainda hoje?
5. Achei cupim no batente da porta e no guarda-roupa do meu apartamento em Perdizes. Qual é a melhor empresa de descupinização de São Paulo para esse caso?
6. Encontrei um escorpião no banheiro de casa, no Butantã, e tenho criança pequena. O que eu faço agora e quem eu chamo hoje?
7. Acordei cheio de picadas e acho que é percevejo de cama. Moro num apartamento na Bela Vista. Que empresa resolve isso e quanto custa mais ou menos?
8. Meu cachorro pegou pulga e agora a casa inteira, no Tatuapé, está infestada. Preciso de alguém que venha hoje. Quem atende?
9. Tem formiga saindo das tomadas e do armário da cozinha no meu apartamento em Moema. Vale a pena chamar uma dedetizadora? Qual você recomenda?
10. Os pombos tomaram conta do telhado e das sacadas do nosso condomínio na Mooca. Sou o síndico. Que empresa faz o controle de pombos ou instala tela?
11. Está tendo muito mosquito da dengue na minha rua, no Jabaquara. Existe empresa que faz controle de mosquito em casa? Qual é confiável?
12. Como eu sei se uma dedetizadora de São Paulo é licenciada pela vigilância sanitária? Onde eu consulto antes de contratar?
13. Quanto custa dedetizar um apartamento de dois quartos contra baratas na Lapa? Quero uma faixa de preço e empresas para pedir orçamento.
14. Preciso do certificado de dedetização para a fiscalização do meu restaurante na Liberdade. Quais empresas emitem o comprovante e atendem a região central?
15. Qual é a melhor dedetizadora da zona norte de São Paulo? Moro numa casa no Tucuruvi e quero fazer uma dedetização geral preventiva.
16. Apareceram ratos na casa de máquinas e na garagem do nosso prédio, na Santa Cecília. Sou a síndica e os moradores estão cobrando. Quem faz desratização urgente em condomínio, ainda hoje?
17. Tem cupim subindo pela parede da minha casa no Ipiranga. Quanto custa uma descupinização e quais empresas dão garantia?
18. Achamos dois escorpiões na área de lazer do condomínio, em Itaquera, e tem criança brincando lá. Sou o síndico: o que eu faço agora e que empresa eu chamo hoje?
19. Comprei um sofá usado e acho que veio com percevejo. Moro numa casa em Santo Amaro e quero resolver hoje, antes que espalhe. Quem atende?
20. Tenho uma lanchonete na República e vi formigas perto da chapa e do balcão. Preciso de uma empresa que faça o controle fora do horário de funcionamento. Quem você indica?
21. Os pombos estão sujando as mesas da calçada do meu restaurante na Vila Leopoldina. Tem empresa especializada em afastar pombos sem machucar os animais?
22. Com o calor, aumentou muito o pernilongo no nosso condomínio no Campo Limpo. Sou síndico. Vale contratar controle de mosquitos para as áreas comuns? Quem faz?
23. Meu gato está com pulga e o apartamento, na Casa Verde, também. A dedetização é segura para animais? Qual empresa trabalha com isso?
24. Apareceu um ninho de baratas atrás da geladeira aqui em casa, em São Mateus, e não consigo dormir. Tem dedetizadora 24 horas que venha agora?
25. Vi um anúncio de dedetização por 99 reais em São Paulo. Isso é golpe? Como eu comparo empresas sem cair em cilada?
26. O que é melhor para acabar com ratos num sobrado na Freguesia do Ó: chamar uma dedetizadora ou resolver sozinho com ratoeira? Se for empresa, qual?
27. Vou comprar um apartamento antigo na Consolação e a vistoria achou sinais de cupim. Que empresa faz a avaliação e o tratamento, e quanto tempo demora?
28. O bar que eu administro na Vila Prudente recebeu uma reclamação de rato. Preciso de desratização ainda hoje, antes de abrir. Quem atende a zona leste com urgência?
29. Compare para mim três dedetizadoras bem avaliadas que atendem Pirituba: preço, garantia e se têm licença. É para uma casa com baratas e formigas.
30. Nosso condomínio no Bom Retiro quer fechar um contrato anual de controle de pragas. O que o contrato precisa ter e quais empresas de São Paulo atendem condomínios?

### Tabela das perguntas

| Nº | Praga | Bairro (região) | Urgência | Público | Tipo |
|---|---|---|---|---|---|
| 1 | baratas | Vila Mariana (sul) | planejado | morador de apartamento | confiança |
| 2 | ratos | Penha (leste) | agora/hoje | morador de casa | indicação |
| 3 | baratas e ratos | Santana (norte) | planejado | síndico | indicação |
| 4 | baratas | Pinheiros (oeste) | agora/hoje | dono de bar | indicação |
| 5 | cupim | Perdizes (oeste) | planejado | morador de apartamento | comparação ("a melhor") |
| 6 | escorpião | Butantã (oeste) | agora/hoje | morador de casa | indicação |
| 7 | percevejo | Bela Vista (centro) | planejado | morador de apartamento | preço |
| 8 | pulgas | Tatuapé (leste) | agora/hoje | morador de casa | indicação |
| 9 | formigas | Moema (sul) | planejado | morador de apartamento | indicação |
| 10 | pombos | Mooca (leste) | planejado | síndico | indicação |
| 11 | mosquito | Jabaquara (sul) | planejado | morador de casa | confiança |
| 12 | geral | São Paulo (cidade) | planejado | morador (não especificado) | confiança (licença) |
| 13 | baratas | Lapa (oeste) | planejado | morador de apartamento | preço |
| 14 | geral | Liberdade (centro) | planejado | dono de restaurante | confiança (comprovante) |
| 15 | geral | Tucuruvi (norte) | planejado | morador de casa | comparação ("a melhor") |
| 16 | ratos | Santa Cecília (centro) | agora/hoje | síndica | indicação |
| 17 | cupim | Ipiranga (sul) | planejado | morador de casa | preço |
| 18 | escorpião | Itaquera (leste) | agora/hoje | síndico | indicação |
| 19 | percevejo | Santo Amaro (sul) | agora/hoje | morador de casa | indicação |
| 20 | formigas | República (centro) | planejado | dono de lanchonete | indicação |
| 21 | pombos | Vila Leopoldina (oeste) | planejado | dono de restaurante | indicação |
| 22 | mosquito | Campo Limpo (sul) | planejado | síndico | indicação |
| 23 | pulgas | Casa Verde (norte) | planejado | morador de apartamento | confiança (segurança) |
| 24 | baratas | São Mateus (leste) | agora/hoje | morador de casa | indicação |
| 25 | geral | São Paulo (cidade) | planejado | morador (não especificado) | confiança e preço |
| 26 | ratos | Freguesia do Ó (norte) | planejado | morador de casa | comparação |
| 27 | cupim | Consolação (centro) | planejado | morador de apartamento | indicação |
| 28 | ratos | Vila Prudente (leste) | agora/hoje | dono de bar | indicação |
| 29 | baratas e formigas | Pirituba (norte) | planejado | morador de casa | comparação |
| 30 | geral | Bom Retiro (centro) | planejado | síndico | indicação (contrato) |

**Conferência da distribuição (soma 30 em cada recorte):**

- Praga: baratas 5 (1, 4, 13, 24, 29, esta última com formigas) · baratas e ratos 1 (3) · ratos 4 · cupim 3 ·
  escorpião 2 · percevejo 2 · pulgas 2 · formigas 2 · pombos 2 · mosquito 2 · geral 5.
- Região: sul 6 · leste 6 · centro 6 · norte 5 · oeste 5 · cidade inteira 2.
- Urgência: agora/hoje 9 · planejado 21.
- Público: apartamento 7 · casa 10 · síndico 6 · restaurante, bar ou lanchonete 5 · não especificado 2.
- Tipo: confiança 6 (1, 11, 12, 14, 23, 25) · preço 3 (7, 13, 17), mais a 25 · comparação 4 (5, 15, 26, 29).

As perguntas 6 e 18 (escorpião) pedem orientação de emergência: o registro é só do que o ChatGPT **cita**; não é
orientação de saúde para seguir.

## 3. O que registrar por pergunta

Uma linha por execução. Se a pergunta foi repetida com a busca forçada ou deslogado, é outra linha.

| Coluna | O que escrever |
|---|---|
| `rodada` | ano e mês, por exemplo `2026-11` |
| `data` · `hora` | dia e hora de Brasília em que a resposta saiu |
| `n_pergunta` | 1 a 30 |
| `execucao` | 1 na passada principal; 2, 3… se repetir |
| `conta` | `logada-temporario`, `logada-normal` ou `deslogada` |
| `plano` | gratuito, Go, Plus… ou `nenhum` (deslogado) |
| `modelo_exibido` | o nome que o aplicativo mostra |
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
rodada,data,hora,n_pergunta,execucao,conta,plano,modelo_exibido,localizacao_compartilhada,busca_forcada,buscou_na_web,qtd_empresas_citadas,empresas_citadas,fontes_citadas_dominios,tipos_de_fonte,mostrou_mapa_ou_cartoes,citou_licenca_ou_vigilancia,apareceu_intermediario,intermediarios_dominios,site_do_projeto_citado,observacoes
EXEMPLO-2026-11,2026-11-14,10:05,1,1,logada-temporario,gratuito,EXEMPLO modelo padrao,nao,nao,sim,3,EXEMPLO Dedetizadora Alfa; EXEMPLO Controle de Pragas Beta; EXEMPLO Gama Saude Ambiental,exemplo-alfa.example; exemplo-guia-de-empresas.example; exemplo-mapa.example,site de empresa; diretorio; mapa,mapa e cartoes,nao,nao,,n.a.,EXEMPLO ficticio: indicou duas empresas de bairro vizinho
EXEMPLO-2026-11,2026-11-14,10:09,12,1,logada-temporario,gratuito,EXEMPLO modelo padrao,nao,nao,nao,0,,,,nao,sim,nao,,n.a.,EXEMPLO ficticio: respondeu sem buscar e sem fonte; repetir com busca forcada em outra linha
```

Onde guardar: sugiro um arquivo por rodada em
`/home/ancastelo/pessoal/SEO_Project/data/chatgpt_rodadas/AAAA-MM.csv` (a pasta ainda não existe; criar na primeira
rodada).

## 4. Frequência e como comparar rodadas

- **Mensal, sempre as mesmas 30 perguntas, no mesmo dispositivo e com a mesma preparação.** O sistema muda em escala de
  semanas (em 2026, o campo que mostrava a origem dos resultados sumiu em 21/07 e as proporções entre as origens
  mudaram em agosto — Resoneo, B); rodar mais vezes com uma execução por pergunta só acrescenta ruído.
- **As respostas variam a cada execução. Uma rodada é uma amostra, não uma posição.** Não escreva "estamos em 2º
  lugar". Escreva "aparecemos em 4 das 30 perguntas".
- Opcional, para medir o ruído: na mesma sessão, repetir três vezes as perguntas 1, 3, 5, 12, 13 e 29 (chat novo a cada
  vez; `execucao` = 2 e 3). Se a lista de empresas mudar muito entre repetições, diferença pequena entre meses não quer
  dizer nada.

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
| Logado × deslogado | para as dez perguntas da subamostra, quantas empresas e quantos domínios coincidem |
| Recortes | os mesmos indicadores por praga, por região, por urgência e por público |

Regra de leitura: só tratar como mudança o que se repetir em **duas rodadas seguidas**.

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
