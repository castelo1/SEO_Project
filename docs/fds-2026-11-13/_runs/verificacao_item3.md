# Verificação do item 3 — índice (escrito pela sessão principal em sex 13/11/2026, 21:50, Brasília)

Este arquivo **não é uma verificação**: é o índice das três verificações independentes do item 3 e o registro do que a
sessão principal fez com cada achado. Quem aprova são os verificadores, não quem produziu.

## Portão (de `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/RODADA.md`, linha 61)

Três guias em `docs/estudo/` (orgânico; Maps e perfil dentro do item 2; respostas de IA), cada tática com fonte e
classe A–D, cada guia terminando em consenso / disputado / não sei; a parte do ChatGPT (`03b_chatgpt.md`) e o roteiro
de teste com 30 perguntas de morador ou síndico e a planilha de registro.

## As três verificações

| Arquivo | O que cobriu | Veredito | Sorteio | Falhas fora do sorteio |
|---|---|---|---|---|
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_a_b.md` (13/11, 21:00) | guias (a) orgânico e (b) Maps | APROVADO, com correções pendentes | 11 OK, 1 falha em 12 | 14 (F1–F14) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_guias_ia_chatgpt.md` (13/11, 20:59) | guia (c), `03b_chatgpt.md`, roteiro | APROVADO, com correções a fazer | 12 OK em 12 | 12 (1–12) |
| `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item3_correcoes.md` (13/11, 21:43) | as correções das 26 falhas, nos cinco arquivos, por outro verificador em contexto limpo | APROVADO COM RESSALVAS | 12 OK em 12 (linhas alteradas) | 25 resolvidas, 1 em parte; 5 defeitos novos menores e 7 antigos menores |

## O que foi feito com os achados

1. **26 falhas das duas primeiras verificações:** corrigidas por dois subagentes corretores (commits `025768c` a
   `86af317`), conferidas por amostra pela sessão principal no artefato e, depois, uma a uma pelo terceiro verificador.
2. **Falha 11 (roteiro), resolvida em parte:** as perguntas 12 e 25 continuam sem bairro, de propósito (testam o pedido
   sem localização fina; o roteiro diz isso). Se o portão ("por praga, bairro, urgência") admite duas perguntas no
   nível da cidade é **decisão do owner**; padrão adotado: manter.
3. **12 defeitos menores da terceira verificação (N1–N5, O1–O7):** corrigidos pela sessão principal entre 21:48 e 21:50 de
   13/11/2026 — prêmio a funcionário por avaliação marcado como inferência (N1); ressalva de que a política de spam é
   da Busca e que estendê-la ao Maps é leitura dos guias, em todas as ocorrências (N2); frase sobre clique em busca
   local reescrita (N3); rótulo único para uma fonte (N4); valor de `execucao` na subamostra deslogada (N5); "grid
   size" e país não declarado (O1); marca de data (O2, O6); "a distância decide" (O3); tabela com coluna faltando (O4);
   classes compostas (O5); rótulos e exemplos do roteiro (O7). **Estas 12 correções não passaram por novo
   verificador**; entram na segunda passada (`verificacao2_item3.md`).
4. **O que nenhum verificador conseguiu reconferir:** a seção "Complemento da sessão principal" de
   `/home/ancastelo/pessoal/SEO_Project/docs/estudo/03b_chatgpt.md` (ajuda oficial da OpenAI, lida só pela sessão
   principal no navegador; os verificadores receberam erro 403).

## Estado

**Item 3: fechado** em 13/11/2026, 21:50, com as ressalvas dos pontos 2, 3 e 4.
