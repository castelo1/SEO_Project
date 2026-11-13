# Raia do controle de pragas (L4b) — sessão em `/home/ancastelo/pessoal/SEO_Project`, sem MCP, com o Chrome pessoal

**Só roda depois de a pasta ter sido migrada para `~/pessoal/SEO_Project` com o remoto privado.**

Projeto pessoal: segue o `CLAUDE.md` de `~/pessoal`. Não use memória corporativa, conectores da empresa nem
skills de trabalho, mesmo que apareçam disponíveis. O hook de git exige commit e push ao fim de cada turno:
faça turnos longos, um por marco.

As regras comuns do fim de semana estão no seu prompt de sistema. Delas valem aqui: "Como trabalhar",
"Verificação", "Forma de todo entregável" e o molde da leitura. **Diferenças:** a fronteira é ler e escrever só
dentro deste projeto; nenhuma mensagem, formulário, cadastro, compra, publicação ou contato com terceiros;
painel e leitura ficam **neste projeto** (`docs/fds-2026-11-13/PAINEL.md` e `LEITURA.md`).

## O foco do projeto mudou (decisão do owner em 13/11/2026)

O projeto deixa de ser o estudo de abrir uma empresa de controle de pragas. Passa a ser: **construir uma
inteligência de SEO para captar leads de dedetização em São Paulo e vendê-los a empresas do setor.** Na ideia
inicial do owner, isso inclui ranqueamento no Google, nas respostas de IA e no Google Maps, um site completo e
captação de leads por WhatsApp. Ele ainda não passou contexto além disso: **primeiro é estudar e aprender,
depois desenhar o sistema.** O que existe na pasta (pesquisas de mercado, CSVs, `PROMPT_PLANO.md`, ficha em
`docs/fds-2026-11-13/FICHA.md`) é do foco antigo: aproveite o que servir como conhecimento do mercado e não
execute o plano antigo (simulador, parecer).

**Exemplos do owner:** ele tem posts do X sobre SEO que quer como base. Se `docs/fds-2026-11-13/EXEMPLOS_X.md`
existir, leia cada link pelo navegador pessoal e extraia o método de cada um antes do item 2. Se não existir,
siga sem eles e deixe na leitura o lugar reservado.

**Pesquisa na web:** autorizada, com termos genéricos, sem nenhum dado pessoal. Busca e leitura de página
pública pelas ferramentas de web; o que elas não abrirem (X, Google Maps, resultados de busca ao vivo), pelo
navegador pessoal — selecione o navegador **pessoal** ("Browser 1"; o "Browser 2" é o profissional, nunca o
use), abas novas, só leitura, nada de login ou formulário. Se o navegador não responder depois de 3
tentativas, registre e siga com o que as ferramentas de web alcançam.

**Regra de evidência desta frente:** SEO é um assunto cheio de afirmação sem prova. Cada prática entra com a
fonte, a data e o tipo de evidência — documentação do Google, estudo com dados, relato com caso reproduzível,
ou opinião — e o que é opinião não vira regra do sistema. Onde as fontes se contradizem, diga.

## Itens, na ordem

| Ordem | Item | Portão | Horas |
|---|---|---|---|
| 1 | Reenquadramento | `docs/ESTADO.md` novo: o que o projeto é agora, o que do material antigo se aproveita (com caminho) e o que fica arquivado; nada apagado | 1 |
| 2 | Estudo: como se ranqueia um serviço local hoje | Três guias, cada um com fontes classificadas: (a) busca orgânica do Google para serviço local; (b) Google Maps e perfil da empresa; (c) respostas de IA (o que faz um site ser citado). Cada guia termina em "o que é consenso / o que é disputado / o que não sei" | 5–7 |
| 3 | Mapa do mercado de busca de dedetização em São Paulo | Quem aparece hoje para as buscas principais (por praga, por bairro ou região, "24 horas", empresa × residência): tipos de página, quem é diretório ou gerador de leads e quem é empresa, padrões dos primeiros colocados no orgânico e no mapa. Amostra declarada (quais buscas, quando, de onde), não censo | 4–6 |
| 4 | Modelos de negócio de venda de leads | Como operam os modelos conhecidos (aluguel de site ranqueado, pagamento por lead, exclusividade por região), com as contas de cada um e os riscos: dependência do Google, regras do WhatsApp, LGPD para captação e repasse de contato, e a regulação do setor (quem pode prestar o serviço para o qual o lead é vendido). O que for jurídico é levantamento com fonte, não parecer | 3–4 |
| 5 | Desenho do sistema, versão 0, para aprovação | Um documento: arquitetura do site (páginas por praga × região, o que cada uma precisa ter), captação e roteamento do lead por WhatsApp, como medir (posição, clique, lead, lead vendido), o que é automatizável, e o caminho em fases com o que cada fase prova antes de gastar dinheiro. Cada escolha aponta para o item do estudo que a sustenta; premissa sem evidência é marcada | 3–4 |
| 6 | Perguntas ao owner | No máximo dez, em ordem de quanto mudam o desenho, cada uma com a opção que o desenho adotou por padrão | 0,5 |

**Fila de reserva:** esqueleto de site estático local (sem publicar, sem comprar domínio) com uma página-modelo
de praga × região, para tornar o desenho concreto; lista de palavras-chave candidatas, com o método para medir
volume quando o owner tiver acesso a uma ferramenta com login.

Terminou: escreva a leitura (20 minutos: o desenho do sistema e as perguntas; no máximo 5 decisões) e encerre.

Fora: comprar domínio, publicar site, criar perfil de empresa, abrir conta, falar com qualquer empresa,
ferramentas que exigem login.
