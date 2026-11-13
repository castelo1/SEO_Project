# Leitura — SEO para leads · 14 min · gerada em sex 13/11 20:26

> Reescrita ao fechar o item 2. Fechados e verificados: itens 1 e 2. O estudo de ranqueamento (item 3) tem quatro
> guias escritos, **ainda não verificados**. Itens 4 a 8 não estão prontos.

## 1. Veredito em três linhas

- **O modelo é viável dentro das regras?** **Sim, numa forma mais estreita que a ideia inicial:** um site de conteúdo
  e comparação que se declara intermediário, nomeia a empresa licenciada em cada oferta e leva a pessoa a falar direto
  com ela. **Não** é viável como "dedetizadora de fachada" com perfil próprio no mapa nem como central de WhatsApp que
  repassa contatos pela API.
- **Fechado e verificado:** o reenquadramento do projeto (item 1) e as quatro restrições lidas na fonte primária
  (item 2), com 12 de 12 citações sorteadas conferidas por um verificador independente.
- **O que muda para você:** o mapa do Google não é um ativo seu (o perfil é sempre da licenciada); a captação por
  WhatsApp tem de abrir a conversa com a licenciada, ou passar por formulário com consentimento que a nomeie; cada
  página que oferece o serviço mostra quem executa e a licença.

## 2. Decisões que só você toma (máximo 5)

| Pergunta (sim/não) | Recomendo | Se não responder |
|---|---|---|
| Aceita que o site **não** terá perfil próprio no Google Maps, e que no mapa o projeto só pode vender gestão do perfil da licenciada (com o telefone e o site dela)? | Sim — é a regra do Google; não há alternativa dentro da regra | O desenho segue assim |
| A captação começa pelo botão que abre o WhatsApp **da licenciada** (o site só registra o clique), em vez de um número próprio que faz a triagem? | Sim — é o único desenho de WhatsApp sem ponto vedado nem incerto | O desenho adota o botão direto, com formulário de consentimento como alternativa |
| Autoriza baixar para o projeto os PDFs oficiais que a ferramenta não leu (Portaria CVS 1/2024, anexo municipal, guias da ANPD)? | Sim — fecha os pontos "não conclusivo" do item 2 | Ficam não conclusivos |
| Mantém a coleta de até 600 buscas ao vivo, sabendo que o Google lista consultas automáticas entre as práticas que ele veda? | Sim, com o limite de 20 s e parada ao primeiro aviso de robô | Mantido |
| Quer tirar do repositório o `PROMPT_PLANO.md` antigo, que cita o seu empregador e a sua formação (reescrever o histórico do git)? | Não — repositório privado; reescrever histórico é destrutivo | Fica como está |

## 3. As restrições: o que cada fonte diz hoje e o que isso corta do plano

Detalhe, citações e endereços: `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md`. É levantamento com
fonte, não parecer jurídico.

| Restrição | O que a fonte diz (lido em 13/11/2026) | O que corta do plano |
|---|---|---|
| **Perfil de empresa do Google** | A lista de empresas inelegíveis traz "Lead generation agents or companies" e empresas só on-line; o perfil exige contato presencial com clientes. Telefone e site do perfil têm de ser os da empresa real, sob controle dela. Terceiro pode administrar o perfil com consentimento expresso, mantendo a empresa como proprietária. Conta com padrão de violação tem todos os perfis suspensos; o recurso só pode ser enviado uma vez | Perfil próprio (inclusive com endereço oculto); endereço de fachada; perfil da parceira com o seu site ou o seu número; avaliação incentivada. Sobra: gestão autorizada do perfil **dela** |
| **Propaganda de controle de pragas** | RDC 622/2022, art. 22: toda propaganda de empresa especializada traz a identificação dela no órgão licenciador e o número da licença; veda texto de medo, selos como "aprovado pela Vigilância Sanitária" e as palavras "inócuo", "seguro", "atóxico", "produto natural". CDC, arts. 36 a 38: publicidade identificável, não enganosa nem por omissão, com prova guardada. A norma **não fala** de site intermediário | Página "anônima" com cara de dedetizadora e botão de orçamento é o formato de maior risco (norma silente). Cada página de oferta nomeia a licenciada e a licença, ou é conteúdo que não oferece o serviço em nome próprio |
| **LGPD** | Art. 7º, § 5º: repassar o contato a outro controlador exige consentimento específico para esse fim (ressalvadas as outras bases legais); autorização genérica é nula; o ônus da prova é de quem capta; na exclusão, avisa-se de imediato cada empresa que recebeu. A autoridade nacional ainda **não tem** norma sobre consentimento nem sobre venda de dados | "Lista de contatos como ativo" só vale para quem autorizou cada finalidade; repasse a várias empresas só se a pessoa souber a quantas e a quais (ou onde ver a lista); nada de dado de saúde |
| **WhatsApp Business** | Política de Mensagens (23/09/2026): só se contata quem deu o número e o opt-in; o opt-in nomeia a empresa que vai falar. Termos da Meta para a API, cláusula 4.1(b): vedado compartilhar ou vender a terceiros os dados obtidos pela Plataforma (leitura literal). Termos do aplicativo gratuito: silentes sobre repasse. O link que abre conversa direta é recurso oficial | O "número próprio que faz a triagem e encaminha o lead" (recomendado pela pesquisa antiga) cai na API e fica incerto no aplicativo |

**A pesquisa de 25/09 valia?** Na direção, sim; no detalhe, foi corrigida em vários pontos (por exemplo: "controlar o
número de telefone" não vale dentro do perfil da parceira; o consentimento é "específico", não "explícito"; o art. 21
da RDC não diz "da empresa que executa"). Cada correção está no fim de cada seção do arquivo.

## 4. Itens

| Item | Estado | Portão | Evidência do verificador |
|---|---|---|---|
| 1 Reenquadramento | **fechado** | `docs/ESTADO.md` novo; prompt antigo movido com `git mv`; nada apagado | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item1.md` |
| 2 Restrições na fonte primária | **fechado** | quatro seções com fonte, data, trecho e veredito | `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/_runs/verificacao_item2.md` (12 de 12 no sorteio; 8 defeitos fora do sorteio, corrigidos) |
| 3 Estudo de ranqueamento | em curso — guias de busca orgânica, respostas de IA e ChatGPT escritos, **não verificados**; guia do Maps em pesquisa | três guias + parte do ChatGPT + roteiro de teste | — |
| 4 Mapa do mercado de busca | adiantado — 89 consultas definidas; coleta ao vivo interrompida por falha do navegador | `docs/mercado/serp_sp.md`, `data/serp_sp.csv`, `data/palavras_chave.csv` | — |
| 5 Modelos de negócio | não iniciado | `docs/modelos_de_negocio.md` | — |
| 6 Desenho, versão 0 | não iniciado | `docs/desenho_v0.md` | — |
| 7 Protótipo local | não iniciado | `prototipo/` | — |
| 8 Perguntas ao owner | não iniciado | `docs/perguntas_owner.md` | — |

## 5. O que é consenso · o que é disputado · o que não sei

- **Consenso (fonte oficial lida e verificada):** as quatro restrições da seção 3.
- **Consenso provisório (guias do item 3, ainda sem verificador):** página por bairro em que só muda o nome do bairro
  é "página de entrada" na política de spam do Google; comprar link viola a política; o Google não dá prazo nem
  garante posição; o resultado rico de perguntas frequentes deixou de existir em maio de 2026; para aparecer nos
  resumos de IA do Google não há requisito extra.
- **Disputado:** quanto pesam os links (estudos de vendedores de ferramenta, Estados Unidos); se o ChatGPT busca no
  Bing, no Google ou em índice próprio (a OpenAI não declara; um estudo de 2026 aponta resultados do Google obtidos por
  terceiros); se o repasse pelo aplicativo gratuito do WhatsApp é permitido.
- **Não sei:** se uma página genérica, sem empresa nomeada, conta como "propaganda de empresa especializada"; quanto
  vale um lead de dedetização em São Paulo; volume de busca; qualquer número de clique ou de prazo **no Brasil**.

## 6. Afirmado e NÃO conferido · o que não foi feito e por quê

- No item 2, os trechos marcados **[S]** foram lidos só pelo subagente (30 pontos); os marcados **[N]** foram
  reconferidos por mim no texto bruto da página; o verificador sorteou 12 e todos bateram.
- **Não lido:** normas e guias que só existem em PDF; o Diário Oficial; o site do Centro de Vigilância Sanitária
  (erro 403). Por isso ficaram "não conclusivo": qual número de licença vale na capital (estadual ou municipal); a
  exigência estadual de razão social e endereço na publicidade; legítimo interesse como base para vender contato.
- Os guias do item 3 ainda são **relato de subagente**: fiz conferência pontual de duas afirmações do guia de busca
  orgânica (fim do resultado de perguntas frequentes e atualização central de 10/11/2026 — ambas confirmadas na página
  do Google), mas a verificação independente ainda não rodou.
- Coleta de buscas ao vivo: 13 buscas gastas em testes e em lotes descartados (um lote sobrepôs buscas por erro meu);
  nenhum dado aproveitado ainda.

## 7. Arquivos para abrir, na ordem (soma = 14 min)

1. `/home/ancastelo/pessoal/SEO_Project/docs/fds-2026-11-13/PAINEL.md` — 1 min
2. `/home/ancastelo/pessoal/SEO_Project/docs/estudo/00_restricoes.md` (quadro de vereditos e a seção "O que as quatro
   restrições, juntas, deixam de pé") — 6 min
3. `/home/ancastelo/pessoal/SEO_Project/docs/ESTADO.md` — 3 min
4. `/home/ancastelo/pessoal/SEO_Project/docs/estudo/01_google_organico.md` (só "Em uma página", ainda não verificado)
   — 4 min
