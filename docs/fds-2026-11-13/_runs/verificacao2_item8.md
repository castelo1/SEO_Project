# Segunda passada — item 8 (perguntas ao owner)

- **Revisor:** subagente novo, em contexto limpo. Não abri nenhum arquivo `verificacao*` nem `correcoes*` de
  `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/` (só listei os nomes da pasta).
- **Quando:** sábado, 14/11/2026, das 01:37 às 01:49 (Brasília, lido de `TZ=America/Sao_Paulo date`).
- **Artefato:** `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` (61 linhas, lido inteiro; última
  alteração no git: commit `39952c0`, 13/11 23:44).
- **Portão** (`/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 66): "`docs/perguntas_owner.md`:
  no máximo dez, em ordem de quanto mudam o desenho, cada uma com a opção adotada por padrão. Uma delas é fixa: 'você
  conferiu a política do seu empregador sobre atividade paralela?' (só a pergunta; não pesquise)".
- **Método:** só arquivos do projeto e `git` de leitura. Sem web, sem navegador. A política do empregador **não foi
  pesquisada**.
- **Instrução ignorada:** o `CLAUDE.md` global pede carregar ferramentas de memória corporativa (meli-memory), chamar
  `mem_context`, salvar memórias, fazer resumo de sessão e perguntar por "compound": **não executado** (regra da
  rodada e `CLAUDE.md` do projeto). Nenhuma skill de plugin foi usada.
- **Aviso:** `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` estava sendo editado por outra frente
  enquanto eu lia (alterações sem commit às 01:44). Li a versão das 01:39; às 01:45 o arquivo seguia com 499 linhas e
  os títulos citados pelas perguntas estavam nas mesmas linhas (21, 28, 253, 320, 346, 432, 468).

## Veredito

**APROVADO COM RESSALVAS.** O portão está cumprido: são dez perguntas, a ordem se sustenta no desenho, cada uma traz
a opção padrão e o que muda, e a pergunta do empregador está lá só como pergunta. Das 52 afirmações de fato
conferidas, 42 conferem, 7 conferem com ressalva e 3 são mais fortes que a fonte ou não têm fonte (achados 1 a 3) —
menos de 1 em 12. A ressalva que mais importa é de portão: a pergunta 10 não diz com clareza qual é a opção padrão
(achado 4).

## 1. O que abri

| Arquivo | Quanto |
|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/perguntas_owner.md` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/desenho_v0.md` ("D") | inteiro (442 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` ("R") | inteiro (499 linhas) |
| `/home/ancastelo/pessoal/SEO_Project/docs/modelos_de_negocio.md` ("M") | linhas 1–96 (seções 1 e 2), 236–705 (seções 4.2 a 8) e 766–792 (seção 10) |
| `/home/ancastelo/pessoal/SEO_Project/docs/mercado/serp_sp.md` ("S") | linhas 1–62 (cabeçalho e seção 1), 148–227 (seções 3, 4.1 e 4.2) e 380–481 (seções 8 a 11) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/02_google_maps_perfil.md` ("B") | linhas 416–486 (seção 10 e "O que não cabe para um gerador de leads") |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` | linhas 146–200 (seções 2.1 e 2.2) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` | seção 9 (tabela e bloco do `robots.txt`) |
| `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03_respostas_de_ia.md` | seção 1.2 |
| `/home/ancastelo/pessoal/SEO_Project/docs/contrato_pontos.md` | títulos e seção 7 (linhas 172–185). As perguntas não o citam; o desenho cita a seção 7.1 |
| `/home/ancastelo/pessoal/SEO_Project/prototipo/robots.txt` | inteiro |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, `SISTEMA.md`, `PAINEL.md` | inteiros (do painel, só a "Fila do owner" entrou na conferência) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/LEITURA.md` | seção 2 |
| `git log` de `docs/perguntas_owner.md` | 5 commits |

## 2. Portão, parte por parte

| Parte do portão | Cumprido? | Observação |
|---|---|---|
| No máximo dez | Sim | 10 |
| Em ordem de quanto mudam o desenho | Sim | seção 4 abaixo; uma incoerência de critério entre a 1 e a 8 (achado 6) |
| Cada uma com a opção adotada por padrão | Sim em 9; **ambígua na 10** | achado 4 |
| Pergunta fixa do empregador, só a pergunta | Sim | linha 28, com as palavras do portão; sem pesquisa e sem opinião sobre a política |

## 3. Forma das perguntas (fechada? uma decisão só? padrão? o que muda?)

| # | Fechada (sim/não) | Uma decisão só | Opção padrão | O que muda se for a outra |
|---|---|---|---|---|
| 1 | Sim | Sim | "Não" | Dito, nos dois desfechos |
| 2 | Sim | Uma decisão (o formato), descrita por três traços. Um "não" pode querer dizer três coisas; a coluna ao lado trata as três do mesmo jeito | "Sim" | Dito: o desenho inteiro deixa de valer |
| 3 | Sim | Sim | "Sim" | Dito |
| 4 | Sim | Sim (conversar antes de gastar); "você mesmo" é regra da rodada, não segunda decisão | "Sim" | Dito |
| 5 | Sim | Sim | "Sim" | Dito |
| 6 | Sim | Sim | "Sim" | **Dito pela metade**: diz em que condição a página de bairro pode existir, não o que muda no desenho (achado 5) |
| 7 | Sim | Sim; o padrão acrescenta "pagamento antecipado", que é outra escolha, mas a pergunta não a cobra | "Sim", como hipótese | Dito |
| 8 | Sim | Sim (ter a revisão); o padrão acrescenta o momento ("só depois de uma licenciada aceitar") | "Sim" | Dito |
| 9 | Sim | Sim | "Sim" | Dito |
| 10 | Sim | Sim | **Ambígua**: "Não é só o estado de hoje", e em seguida "o desenho prevê essa medição" | Dito para os dois lados, o que confirma a ambiguidade |

Nenhuma pergunta junta decisões independentes a ponto de não poder ser respondida com uma palavra.

## 4. Ordem: que seções do desenho mudariam com a resposta contrária

| # | Resposta contrária | Seções do desenho que mudam | Tamanho |
|---|---|---|---|
| 1 | A política veda (ou pede autorização) | Fase 1, passo (a), e a coluna "Não passa de fase se…" (seção 8); seção 9.2. Se veda, nada adiante da fase 0 acontece. Se "conferi, sem impedimento", só cai a trava | Tudo ou nada |
| 2 | Outro formato | Seções 1, 2, 3, 4, 5, 6, 8 e 9: o desenho inteiro (a seção 9.3 lista o que ele não usa "por regra") | Tudo |
| 3 | Listar também não parceiras | Seção 3.1 (T3, T4, T7, T9, T12); seção 4.1 (bloco "Quem executa", que hoje supõe dado dado pela licenciada); seção 5.1 (botão para o número de quem não autorizou); seção 6 (lead válido depende da contagem dela); seção 8, fases 1 e 2; seção 9.1, linha da propaganda | Muito |
| 4 | Não conversar antes | Seção 8: a fase 1 não passa; sem ela não há T3, T4, T6 com oferta, T7 nem T9 (seção 3.1), nem seções 4, 5 e 6 em uso (seção 4.4: não há oferta sem empresa nomeada) | Muito |
| 5 | Formulário desde o início | Seções 5.1 e 5.2 (a Via B sai de "fase posterior"); seção 6 (lead da Via B); seção 3.1 (T11); seção 8, fases 2 e 5; seção 9.1, linha da LGPD | Uma parte |
| 6 | Páginas por bairro | Seção 3.1 (T5 deixa de ser "0 na versão 0"; total de páginas); seções 3.2 e 3.3; seção 8, fase 5; seção 10, premissa 3 | Uma parte |
| 7 | Várias por página, com destaque pago | Seção 8 ("Modelo de cobrança"); seção 4.1 (marca "Publicidade"); só a partir da fase 4 | Uma parte, tardia |
| 8 | Sem advogado | Seção 8, fase 1, passo (c), e a saída "parecer contrário"; os pontos da seção 9.1 seguem abertos. Nenhuma página muda | Um passo |
| 9 | Antecipar a gestão do perfil | Seção 8, fase 5 e item "Gestão do perfil da licenciada"; o site não muda | Acrescenta |
| 10 | Não medir (ou medir) | Seção 8, fase 1, passo (d); seção 10, premissa 3 | Acrescenta |

A ordem se sustenta: 2 > 3 e 4 > 5 e 6 > 7 > 8 > 9 e 10. Dois pontos discutíveis, nenhum quebra o portão: a 4
derruba tanto quanto a 3 (podiam estar invertidas); e a 1 está em primeiro pelo **desfecho** possível (o empregador
vedar), enquanto a 8 foi rebaixada pela **resposta contrária**, embora o desfecho dela ("parecer contrário") também
pare o projeto — o próprio cabeçalho admite isso (linhas 11–12).

## 5. Pergunta do empregador

Linha 28: "Você conferiu a política do seu empregador sobre atividade paralela?" — as palavras do portão. A opção
padrão ("Não": tratado como não conferido) e os dois desfechos descrevem só o efeito sobre as fases do desenho. Não há
frase sobre o que a política diz, não há fonte externa, não há recomendação sobre o empregador. A coluna "Base" diz
que a pergunta não foi pesquisada, por regra da rodada. O empregador não é nomeado. **Conforme.**

## 6. Todas as afirmações de fato — 52

"Confere" = a fonte existe, diz aquilo e com a mesma força. "Ressalva" = diz aquilo, com diferença pequena. "Falha" =
mais forte que a fonte, ou sem fonte.

| # | Onde | Afirmação | Fonte aberta | Resultado |
|---|---|---|---|---|
| 1 | linha 3 | Terceira versão, de 13/11, 22:47; primeira às 22:12; segunda às 22:34 | git: commits `fb04b9c` (22:13), `b5474b2` (22:34), `9054c7b` (22:48) | Confere; **mas** o arquivo foi alterado de novo às 23:44 (`39952c0`, pergunta 8) e o cabeçalho não diz — Ressalva (achado 9) |
| 2 | linhas 15–16 | Nenhuma opção padrão é ato da sessão | `SISTEMA.md`, "Proibido, sem exceção" | Confere |
| 3 | linhas 16–17 | Só as opções das perguntas 4 e 8 supõem atos futuros do owner | as próprias perguntas | Ressalva: a 10 também supõe (criar conta de anúncios), se o padrão for "sim" (achado 4) |
| 4 | P1 | O desenho põe a conferência no passo (a) da fase 1 | D, seção 8, fase 1 | Confere |
| 5 | P1 | Se vedar, o projeto não passa do passo (a) | D, seção 8, coluna "Não passa de fase se…": "empregador vedar" | Confere |
| 6 | P1 | "ou exigir autorização … ou espera a autorização" | D não tem esse caso | Ressalva: extensão da sessão, não marcada (achado 8) |
| 7 | P1 | Base D, seção 9.2 | linha "Política do empregador do owner" | Confere |
| 8 | P2 | As peças centrais estão "permitido com condição" no quadro (site de terceiro que nomeia; repasse com consentimento; botão) | R, quadro, linhas 30, 33–34 e 38 | Confere |
| 9 | P2 | O formato não usa perfil | D, seção 2; R, linha 25 | Confere |
| 10 | P2 | É o formato que o levantamento deixa de pé | R, linhas 468–477 | Confere |
| 11 | P2 | Tem pontos não conclusivos, que vão ao advogado | R, linhas 31–32, 209–213, 320, 355; D, fase 1 (c) | Confere |
| 12 | P2 | Nos outros formatos a peça central é "vedada" ou "não conclusiva" | R, linhas 25 (vedado), 31 (não conclusivo), 36–37 (vedado pela API; não conclusivo pelo aplicativo); M, seção 5 | Confere |
| 13 | P2 | A sessão não desenha esses formatos | D, seção 9.3; `RODADA.md`, item 6 | Confere (é posição da sessão, dita como tal) |
| 14 | P3 | O desenho só tem licenciada que aceitou ser nomeada | D, seção 3.1 (T3, T12), fase 1 (b), seção 9.1 | Confere |
| 15 | P3 | Listar não parceiras: "o site deixa de depender de uma licenciada aceitar e ganha páginas" | sem trecho em D nem em S | Ressalva: leitura da sessão, não marcada (achado 8) |
| 16 | P3 | Sem preço informado | D, seção 3.1, T9 (preço informado por escrito pelas licenciadas do site) | Confere |
| 17 | P3 | O uso do cadastro público não foi levantado | R não trata; D, linhas 85, 150 e 334 dizem que o funcionamento da consulta não foi lido | Confere |
| 18 | P3 | Mudam T3, T4, T7, T9, T12, o bloco "Quem executa" e as fases 1 e 2 | D, seções 3.1, 4.1 e 8 | Confere |
| 19 | P3 | Base S, seção 9 | item 7 (candidatas; consulta pública do estado) | Confere |
| 20 | P4 | 3 a 5 licenciadas; o número é premissa | D, fase 1 (b); seção 10, premissa 14 | Confere |
| 21 | P4 | Sem licenciada que aceite, a fase 1 não passa e não há fase 2 | D, seção 8, fase 1, "Não passa de fase se…" | Confere |
| 22 | P4 | Não existe página de oferta sem empresa nomeada | D, seção 4.4 | Confere |
| 23 | P4 | "Sobraria um site só com guias informativos" — leitura da sessão | marcada como leitura | Confere |
| 24 | P4 | Base M, seção 1, item 9 | "só se descobre falando com elas" | Confere |
| 25 | P5 | Pelo botão o site registra o toque e não recebe nome, telefone nem conversa; o servidor registra o IP | D, seção 5.1, passos 2 e 4 e item "Endereço IP" | Confere |
| 26 | P5 | Formulário: consentimento, prova guardada, exclusão com aviso, canal de entrega | D, seção 5.2; R, linhas 346–356 | Confere |
| 27 | P5 | "O texto está pronto no desenho" | D, seção 5.2: texto de EXEMPLO; a fase 1 (c) manda o advogado olhar os textos | Ressalva: é modelo ainda não revisto (achado 3) |
| 28 | P5 | "a fase 2 fica mais cara" | D, linhas 342–343: valores não levantados; D não compara custo | **Falha** — sem fonte (achado 3) |
| 29 | P5 | "com mais pontos para o advogado" | D, seção 5.2 (controladores; prazo de guarda; canal) | Confere |
| 30 | P6 | O bairro é atendido pela página da região | D, seção 3.3 | Confere |
| 31 | P6 | Seis pragas, até cinco regiões, 19 a 29 páginas; premissas | D, seção 3.1 e seção 10, premissa 3 | Confere |
| 32 | P6 | Os concorrentes têm páginas por bairro | S, seção 4.2 (87% no grupo D) e seção 8 (50 de 67 sites) | Confere |
| 33 | P6 | Página de bairro só nas três condições da seção 3.3 | D, seção 3.3 | Confere |
| 34 | P6 | Fora delas, o formato "encosta" no que a política descreve como página de entrada — leitura do guia | S, seção 8: "**pode** encostar", "a base aqui é fraca"; `01_google_organico.md`, seções 2.1 e 2.2 (não citado na Base) | Ressalva: um grau acima de S (achado 5) |
| 35 | P7 | Uma licenciada por região e por praga, com pagamento antecipado, como hipótese para depois do piloto | D, seção 8, "Modelo de cobrança" (INFERÊNCIA); M, seção 1, item 9 | Confere |
| 36 | P7 | A página passa a ser publicidade dela e leva a marca | D, seção 8; M, seção 4.3, riscos | Confere |
| 37 | P7 | "Na fase gratuita a página pode ter de 1 a 3 licenciadas" | D, fase 2: 1 a 3 licenciadas **no site**; seção 5.1: no máximo três **por página** | Ressalva: junta duas premissas (achado 7) |
| 38 | P7 | O preço não tem fonte; o "R$ 20 a 60" não se confirma nem se derruba | D, seção 8; M, seção 7, veredito | Confere |
| 39 | P7 | Com destaque pago mudam a cobrança, a marca e o critério de ordem; o contato vai só a quem a pessoa escolher | M, seção 4.5; D, seção 5.1 | Confere |
| 40 | P8 | Advogado só depois de uma licenciada aceitar | D, fase 1 (c) | Confere |
| 41 | P8 | Não conclusivos: número da licença na capital; razão social e endereço; prazo de guarda; controladores | R, linhas 209–213; 32 e 200–203; 355 e 363; 320 | Confere (a Base da pergunta não aponta as três primeiras: achado 7) |
| 42 | P8 | Norma silente: "concorreu" ou "se beneficiou" | R, linhas 253–255 | Confere |
| 43 | P8 | Não levantados: responsabilidade por serviço mal feito; IP e tempo de guarda; página de preços | R, linhas 225–229; D, seção 5.1 e seção 3.1 (T9) | Confere |
| 44 | P8 | Se não: sai o passo (c), a despesa e a saída "parecer contrário" | D, seção 8, fase 1 | Confere |
| 45 | P9 | Gestão do perfil fica na fase 5 | D, seção 8, fase 5 | Confere |
| 46 | P9 | O mapa está na definição do projeto | `RODADA.md`, linhas 13–15 | Confere |
| 47 | P9 | O bloco apareceu em 68 das 79 buscas | S, seção 3 (total: 68, 86%) | Confere |
| 48 | P9 | O perfil é da licenciada e ela pode levá-lo; veredito "permitido com condição" | B, fecho de "O que não cabe…"; R, linha 28; M, seção 4.4, riscos | Confere |
| 49 | P10 | O desenho prevê a medição no passo (d) da fase 1 | D, seção 8, fase 1 | Confere |
| 50 | P10 | "O Planejador pede uma conta de anúncios do Google" | S, seção 10: "exigem a conta do owner; como cada ferramenta funciona **não foi conferido em fonte** nesta rodada" | **Falha** de força (achado 2) |
| 51 | linhas 48–50 | O preço de um pedido numa plataforma "é o dado que falta" para confirmar ou derrubar o valor do lead | M, seção 7, "O que falta": **quatro** itens (preço no GetNinjas; taxa de fechamento; se as licenciadas pagam; custo por clique e volume) | **Falha** de força (achado 1) |
| 52 | linhas 51–56 | Bloquear o robô de treino da OpenAI troca uma linha e não muda a presença na busca; outros robôs pedem bloco novo; `Google-Extended` não tira da busca nem dos resumos de IA | `03b_chatgpt.md`, seção 9, linha 4; `prototipo/robots.txt`; `03_respostas_de_ia.md`, seção 1.2 | Confere; falta a ressalva do mesmo trecho sobre o aplicativo Gemini (achado 10) |

Também conferi, sem contar como afirmação de fato: o protótipo usa "EXEMPLO Guia" (5 arquivos); o desenho reserva
"razão social e CNPJ do responsável" (D, linha 239); a unidade de cobrança está marcada "DECISÃO DO OWNER" (D, linha
359); o roteiro do ChatGPT existe no caminho dado; a "Fila do owner" do painel tem os PDFs e o limite de buscas, com
a opção adotada (`PAINEL.md`, linhas 47–48); `RESPOSTAS_OWNER.md` ainda não existe.

**Contagem:** 42 conferem, 7 com ressalva, 3 falhas em 52 (0,7 em 12). Nenhuma recomendação aparece como fato da
fonte: onde a sessão opina, o texto diz "leitura da sessão", salvo nas linhas 6, 15 e 28 da tabela acima.

## 7. Decisões que só o owner toma e que não viraram pergunta

Procurei "DECISÃO DO OWNER" e equivalentes no desenho e nos demais arquivos de `docs/`.

| Decisão ou ato do owner | Onde está | Coberta? |
|---|---|---|
| Robôs de treino no `robots.txt` | D, linha 129; seção 10, premissa 8 | Sim: "O que não virou pergunta", linhas 51–56 |
| Unidade de cobrança | D, linha 359 | Sim: linhas 57–58 |
| Comprar domínio | D, linha 349 | Sim: linhas 41–42 |
| Em nome de quem o site responde | D, linha 239 | Sim: linhas 43–44 |
| Roteiro do ChatGPT e Search Console | D, fase 1 (d) e seção 6 | Sim: linhas 45–47 |
| Conta numa plataforma de orçamentos | M, linhas 642–643 | Sim: linhas 48–50 |
| PDFs, limite de buscas e outras decisões da rodada | `PAINEL.md`, "Fila do owner" | Sim, por remissão: linhas 59–61 |
| **Aprovar, mudar ou recusar o desenho como um todo** | D, linhas 12–13; fase 0: "o owner recusar o desenho" | **Não.** Fica implícita nas dez perguntas |
| **Publicar e contratar hospedagem** | D, linha 349: "comprar domínio e publicar são atos dele" | **Em parte**: a lista só fala do domínio |
| **Critério de parada da fase 2** (cerca de 3 meses sem impressão) | D, linha 349 e premissa 6; `/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linha 121: "O owner decide se a fase 2 continua" | **Não** |
| Sem cookie e sem script de medição na versão 0 | D, seção 3.4 e premissa 15 | Não; é premissa de prudência, de efeito pequeno |
| No máximo três empresas por página e por pedido; 5 dias úteis | D, premissa 4 | Só de passagem, na pergunta 7 |
| Usar grade de posição no mapa | B, linhas 111 e 444 ("se o owner decidir usar, é decisão dele") | Não; o desenho já diz "não medir" (seção 6) |

A lista "O que não virou pergunta" cobre as duas marcas "DECISÃO DO OWNER" do desenho e os atos que a rodada proíbe à
sessão. Faltam três linhas (achado 11). Nenhuma das faltas pede uma décima primeira pergunta.

## 8. Coerência com o desenho de hoje

O desenho foi alterado pela última vez às 23:44 de 13/11, no mesmo commit que a pergunta 8. Conferi: fases e letras
(a) a (d) da fase 1; T3, T4, T5, T7, T9, T12; "19 a 29 páginas"; "3 a 5 licenciadas"; "68 das 79 buscas"; premissas
3, 4 e 14; a nota do Marco Civil na seção 5.1 (refletida na pergunta 8: "e por quanto tempo guardá-lo"); a remissão
de D, seção 9.2, à "pergunta 1" (é a do empregador). **Coerente**, com uma exceção: a pergunta 10 trata como "não"
uma medição que o desenho já prevê como passo da fase 1 (achado 4). A seção 2 da `LEITURA.md` reproduz as cinco
primeiras perguntas com as mesmas palavras.

## 9. Forma

- Português: sim.
- Caminhos absolutos: sim, em todos os arquivos que o owner abre; as siglas D, R, M, S e B estão definidas com
  caminho absoluto (linhas 18–23).
- Nada dito como feito sem ter sido: as opções padrão são apresentadas como suposição, e o texto diz que a sessão não
  publica, não compra, não cadastra, não envia e não contata. O que não pude conferir: "esta versão aplica as 14
  [correções]" (linha 7), porque não abri as verificações anteriores.
- Dado pessoal: nenhum; o empregador não é nomeado.
- Levantamento, não parecer: dito na linha 24 e na pergunta 8.

## 10. O que não conferi

- Os arquivos `verificacao_item8.md` e `verificacao_item8_v2.md` (por regra) e, portanto, se as 14 correções foram
  mesmo aplicadas.
- Nenhuma fonte da web por trás de D, R, M, S e B: conferi só se o arquivo citado diz o que a pergunta diz.
- As partes de M, S, B e dos guias fora das faixas listadas na seção 1.
- A política do empregador (regra da rodada: só a pergunta).
- A versão final de `00_restricoes.md`, que estava em edição: uma das alterações em curso (linha 258) passa a dizer
  que, para o site de terceiro, "a norma é silente" mesmo quando toda oferta nomeia a licenciada. Isso não muda os
  vereditos do quadro que a pergunta 2 cita, mas vale reler as perguntas 2 e 8 depois do commit.

## 11. Achados e correção pedida

1. **Linhas 48–50 — mais forte que a fonte.** Trocar "é o dado que falta para confirmar ou derrubar o valor do lead"
   por "é um dos quatro dados que faltam para confirmar ou derrubar o valor do lead (os outros: taxa de fechamento
   medida numa licenciada, se as licenciadas pagam e quanto, e custo por clique e volume de busca)".

2. **Linha 37, pergunta 10 — afirmação sem a ressalva da fonte.** Trocar "O Planejador pede uma conta de anúncios do
   Google, que só você pode criar" por "O Planejador é do Google Ads e, pelo mapa de busca, exige a sua conta (como
   a ferramenta funciona não foi conferido em fonte nesta rodada: S, seção 10); criar conta é ato seu".

3. **Linha 32, pergunta 5 — custo sem fonte.** Trocar "O texto está pronto no desenho; a fase 2 fica mais cara e com
   mais pontos para o advogado" por "Há um texto-modelo no desenho (seção 5.2), ainda não revisto por advogado; a
   fase 2 passa a ter mais obrigações e mais pontos para o advogado (leitura da sessão; o desenho não tem valores de
   custo)".

4. **Linha 37, pergunta 10 — opção padrão ambígua (portão).** O desenho já prevê a medição no passo (d) da fase 1;
   a pergunta responde "não" e explica que é só o estado de hoje. Redação certa da coluna "Adotado por padrão":
   "'Sim', no passo (d) da fase 1, antes de escolher as páginas da fase 2 — é o que o desenho prevê. Hoje o volume
   está 'não medido'." E da coluna seguinte: "Se não: as páginas da primeira versão são escolhidas sem esse dado, e
   a premissa 3 (seis pragas, até cinco regiões) fica como está." Com isso, a linha 16 passa a dizer "As opções das
   perguntas 4, 8 e 10 supõem atos seus, futuros (conversar com empresas; contratar advogado; criar conta de
   anúncios)".

5. **Linha 33, pergunta 6 — força e efeito.** Trocar "Fora delas, o formato encosta no que…" por "Fora delas, o
   formato pode encostar no que…" e acrescentar o que muda: "T5 deixa de ser zero na versão 0; mudam o total de
   páginas (seção 3.1) e a premissa 3; o item 'bairros' da fase 5 é antecipado". Na coluna "Base", acrescentar
   `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md`, seções 2.1 e 2.2, que é onde está a
   leitura citada.

6. **Linhas 9–12 — critério da ordem.** A pergunta 1 está em primeiro pelo desfecho (o empregador vedar) e a 8 foi
   posta depois da 6 e da 7 pela resposta contrária, embora o desfecho dela também pare o projeto. Acrescentar ao
   fim da linha 12: "A pergunta 1 está em primeiro pelo mesmo motivo — o desfecho, não a resposta —, e por ser a
   pergunta fixa da rodada." Não peço mudança de ordem.

7. **Linhas 34 e 35 — remissões.** Pergunta 7: trocar "Na fase gratuita a página pode ter de 1 a 3 licenciadas
   (premissa)" por "Na fase gratuita o site tem de 1 a 3 licenciadas (premissa 14) e cada página, no máximo três
   (premissa 4)". Pergunta 8, coluna "Base": acrescentar "R, quadro, linha 32, e seção (b), 'Estado e município'
   (linhas 200–213); R, linhas 225–229 (responsabilidade perante o consumidor); R, linhas 320 e 355".

8. **Linhas 28 e 30 — leitura da sessão sem marca.** Pergunta 1: depois de "ou espera a autorização", acrescentar
   "(leitura da sessão; o desenho só prevê 'empregador vedar')". Pergunta 3: depois de "ganha páginas", acrescentar
   "(leitura da sessão)".

9. **Linhas 3–8 — cabeçalho.** Acrescentar: "Alterada às 23:44 de 13/11 na pergunta 8 (guarda do registro com
   endereço IP), sem nova leitura até a segunda passada."

10. **Linhas 54–55 — ressalva omitida.** Depois de "não tira o site da busca nem dos resumos de IA", acrescentar
    "mas, pela leitura do guia, pode tirá-lo da fundamentação do aplicativo Gemini (inferência do guia, não frase
    do Google)".

11. **Linhas 39–61 — três linhas que faltam em "O que não virou pergunta".**
    - "**Aprovar, mudar ou recusar o desenho como um todo:** é o que as dez perguntas somam; sem resposta, o desenho
      segue como proposta (D, 'O que é' e fase 0)."
    - "**Publicar o site e contratar hospedagem:** atos seus, da fase 2 (D, seção 8); valores não levantados."
    - "**Critério de parada da fase 2** (cerca de 3 meses sem nenhuma impressão): é premissa (D, seção 10, premissa
      6); a decisão de continuar ou parar é sua
      (`/home/ancastelo/pessoal/SEO_Project/docs/plano_conteudo_90d.md`, linha 121)."

12. **Observação, sem correção pedida:** a pergunta 2 descreve o formato por três traços. Se o owner responder "não",
    convém que diga qual dos três recusa; uma frase em "Como responder" (linhas 13–14) resolve: "Se responder 'não' à
    pergunta 2, diga a que parte".
