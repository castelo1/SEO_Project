# Sessão de revisão de uma frente da rodada de 13–14/11/2026

Você vai conduzir, com o dono presente, a revisão do que uma sessão autônoma produziu nesta frente. O objetivo é
ele sair com cada pendência decidida e com um plano de integração ao trabalho que já vinha sendo feito.

## Contexto que você precisa

- A rodada rodou de sex 13/11 19:18 a sáb 14/11 08:23 e foi **interrompida por gasto**: US$ 8.800 em 13 horas,
  94% em subagentes. O que estava em subagente no instante do corte pode ter ficado pela metade.
- **Orçamento agora: cerca de US$ 80 por dia para tudo.** Esta sessão roda em Opus 5.5 e deve custar de US$ 20
  a 40. Por isso: **não lance subagentes** (se um for indispensável, diga por quê e o custo estimado, e espere o
  "sim"); não releia arquivo grande por inteiro (as revisões passam de 200 KB: busque o trecho); não rode
  consulta pesada no BigQuery nem refaça trabalho da rodada.
- O que as raias escreveram é **relato, não fato**: antes de apresentar ao dono um número ou um "fechado" que
  pese na decisão, abra o artefato e confira aquele ponto. Diga o que conferiu e o que não conferiu.
- Visão geral da rodada e minha avaliação de valor (a confirmar):
  não se aplica a este projeto pessoal; use o painel e a leitura.

## Passo 1 — Mapa da frente, em uma tela (antes de qualquer pergunta)

Leia `docs/fds-2026-11-13/PAINEL.md` e `docs/fds-2026-11-13/LEITURA.md` e o `docs/ESTADO.md` do projeto.
Entregue, em até 40 linhas:
1. **O que foi feito e conferido** (por nome, com o caminho absoluto do entregável principal).
2. **O que ficou pela metade** e o que falta para fechar (horas, consultas, custo estimado).
3. **Pendências, dúvidas e bloqueios**, numa lista única **em ordem de prioridade**, com esta régua:
   erro ou risco em produção → o que destrava entrega que o dono pediu ou assinatura de KPI → número já
   mostrado a terceiros → o resto. Junte decisões que são a mesma decisão; descarte as que a interrupção
   tornou sem objeto e diga quais.
4. **O que eu recomendo ignorar ou arquivar** (rastro, versões intermediárias, itens de baixo valor).
Pare e pergunte se a ordem serve.

## Passo 2 — Uma pendência por vez, na ordem

Para cada uma, nesta forma, e então **espere a resposta**:
- **Contexto** (3 a 5 linhas: o que é, por que apareceu, o que a rodada mediu, o que eu conferi agora).
- **Opções**, cada uma com o que ganha, o que custa (tempo do dono, dólares, risco) e se é reversível.
- **Recomendo** (uma opção, com o motivo em uma frase) e **o que acontece se ficar sem decisão**.
Se o dono tiver uma dúvida, responda com o artefato aberto, não de memória. Registre cada resposta, na hora,
em `REVISAO_RESPOSTAS.md` na pasta da leitura da raia (data, pendência, decisão, quem executa).

## Passo 3 — Integração

Com as decisões tomadas, proponha em uma tabela: o que muda nos arquivos do projeto, o texto novo do
`docs/ESTADO.md` e o que é arquivado. **Execute só o que o dono aprovar, item a item.**

## Fronteira

Projeto pessoal: sem memória corporativa e sem material da empresa. Sem mensagem ou candidatura enviada, sem
criar conta, sem preencher formulário, sem comprar ou publicar nada, sem abrir o LinkedIn a não ser a pedido do
dono, presente. Commit e push no repositório pessoal ao fim de cada etapa. Forma de todo texto: português,
caminho absoluto no que ele precisa abrir, cada número com unidade, período e fonte.

## Encerramento

Quando a lista acabar ou o dono parar: grave `REVISAO_RESUMO.md` ao lado das respostas (decidido, executado,
pendente com dono e prazo, próximo passo), diga o gasto aproximado da sessão e encerre. Não emende outro assunto.
