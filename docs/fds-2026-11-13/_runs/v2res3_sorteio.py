#!/usr/bin/env python3
"""Segunda passada da reserva 3: sorteio de 12 afirmações de docs/plano_conteudo_90d.md.
A lista abaixo é a enumeração, feita pelo revisor, das afirmações com fonte citada (linha do plano lida em
14/11/2026, arquivo com mtime 01:11:34). Semente declarada. Só leitura; não grava nada."""
import random
AFIRMACOES = [
 (1, 'L15-23', 'K tem 2.721 termos e "volume: não medido" em todas as linhas'),
 (2, 'L30-33', 'As cinco primeiras páginas da base são o que as demais precisam para cumprir o desenho (D, seções 2, 4.2 e 5.1)'),
 (3, 'L34-37', 'Em três das quatro buscas informativas coletadas, o primeiro resultado não é de dedetizadora (S, seção 12.1)'),
 (4, 'L38-41', 'Pelo desenho, a fase 2 só começa com uma licenciada que aceitou ser nomeada (D, seção 8)'),
 (5, 'L44-46', 'Ritmo: de 1,5 a 1,8 página por semana (19 a 23 páginas em 12,9 semanas); 5 na primeira semana, 2 na segunda'),
 (6, 'L54', 'Antes do dia 1: política do empregador, licenciada que aceita, advogado (D, seção 8, fase 1)'),
 (7, 'L55', 'Volume no Planejador, "se o owner quiser" (D, seção 8, fase 1, letra d; S, seção 10)'),
 (8, 'L56', 'Dados da licenciada por escrito (D, seções 3.1 T7 e T9, 4.1 e 7); o desenho exige antes do site só que ela aceite ser nomeada (D, seção 8)'),
 (9, 'L57', 'Fontes oficiais para os guias de praga (D, seção 4.3, último parágrafo)'),
 (10, 'L65', 'Início: 6 termos; lá estão as dedetizadoras, o mapa e os anúncios (S, seções 1 item 2, 3 e 7.3 item 1); D, seção 2; A, seção 3'),
 (11, 'L66', 'T11: o aviso ao lado do botão remete à política e o servidor anota o IP (D, seção 5.1); "Excluir meus dados" em D, seções 5.1 e 5.2'),
 (12, 'L67', 'T8 é um dos quatro elementos em que o desenho aposta (D, seção 1, item 2: PREMISSA; D, seção 11: não confirmada no grupo H)'),
 (13, 'L67', 'Em "como saber se dedetizadora é licenciada", o segundo resultado é a consulta pública do estado e o primeiro é um site não lido (S, seção 12.1)'),
 (14, 'L67', 'intencao = confiança: 140 termos (47 + 46 + 46 + 1; 120 de bairro e 15 de região); coletados A10, H01, H02, H03'),
 (15, 'L67', 'Em H01 e H02 o resultado é de dedetizadoras e de anúncios; 11 anúncios nas três de confiança (S, seção 12.3, item 4)'),
 (16, 'L67', 'D, seção 4.3, não deixa dizer "a melhor" sem critério exposto'),
 (17, 'L68', 'T12 diz o que é exigido da licenciada e como ela entra (D, seção 3.1); conversas com licenciadas são da fase 1 (D, seção 8)'),
 (18, 'L69', 'Baratas: praga da página-modelo do protótipo e da única busca informativa de praga coletada; 1º resultado de fabricante (não lido); nenhum anúncio (S, seção 12.1)'),
 (19, 'L72', 'Cupim: em "dedetização de cupim sp", dois dos três perfis do bloco de mapa têm "cupim(s)" no nome, nas duas vezes (lote_02 B04; repeticao_01 B04r)'),
 (20, 'L73', 'T7/T4: toda oferta nomeia quem executa (D, seções 4.1 e 4.4); 24 termos por região, 23 no centro; 2 de público'),
 (21, 'L75', 'T3: formato da página-modelo, com título e descrição curtos (P, seção 5); 2 termos por praga e região'),
 (22, 'L77', 'Escorpião: 12 de 16 resultados são de órgãos públicos e do Butantan (S, seção 1, item 7); saúde pede fonte oficial (D, seção 4.3, último parágrafo)'),
 (23, 'L78', 'Preço: em H04, H05 e H10 a mesma página de "tabela de preço" está em primeiro e um marketplace aparece nas três (S, 12.1 e 12.2); hipótese mais fraca (S, 12.3, item 3)'),
 (24, 'L78', 'intencao = preço e tipo_local = cidade: 22 termos; 6 gerais, 16 de praga, 10 sem guia; coletados A05, A09, H04, H10; H05 "sem local"'),
 (25, 'L80', 'Grupo F: 68% dos 117 resultados das 13 buscas são páginas internas de serviço ou outra e 1% é página por local (S, seção 4.2); publico = condomínio: 9 termos'),
 (26, 'L81', 'Restaurante: o bloco da norma sanitária está "[A ESCREVER]" no protótipo; publico = restaurante: 9 termos'),
 (27, 'L82', 'Revisão: "licença conferida em" e "preço informado em" têm de continuar verdadeiros (D, seção 7)'),
 (28, 'L85-86', 'Contagem: de 19 a 23 páginas, dentro das 19 a 29 do desenho (D, seção 3.1)'),
 (29, 'L88-91', 'Cobertura: até 168 termos (13%) dos 1.260 de antes; urgência 835 e bairro 2.289 no mapa ampliado'),
 (30, 'L95-99', 'O desenho fixa seis guias (D, 3.1, T2) e pede poucas páginas (D, 1, item 3; total PREMISSA); 21 informativos, 4 coletados; D, 3.2, marcada INFERÊNCIA'),
 (31, 'L104', 'O site não promete prazo: D, seção 4.3, cita o CDC, art. 38, para afirmação sem prova guardada'),
 (32, 'L105', 'A norma veda "seguro" e sugestão de ausência de efeito adverso (D, seção 4.3)'),
 (33, 'L106', 'Sem texto de medo (D, seção 4.3)'),
 (34, 'L108', 'Termos informativos de formigas, pulgas, mosquito, carrapatos, aranhas e traças: 6, sem página'),
 (35, 'L111-113', 'Sete das dez páginas lidas têm ao menos um subtítulo em forma de pergunta (P, seção 4); não há fonte, nos guias, de que ajude'),
 (36, 'L119', 'Dia 28: colunas `impressoes` e `visitas_*` da planilha de medição'),
 (37, 'L121', 'Dia 84: a contagem da licenciada é da fase 3 (D, seção 10, premissa 5); critério de parada "em cerca de 3 meses não houver impressão nenhuma" (D, seção 8, fase 2; PREMISSA)'),
 (38, 'L123-124', 'Search Console é do owner (D, seção 6); comparar períodos iguais de 28 dias e marcar atualização central (A, seção 8)'),
 (39, 'L130', 'Página por bairro: D, seção 3.3 (três condições juntas); D, seção 3.1, fixa T5 = 0 na versão 0'),
 (40, 'L131', 'Sem blog de um artigo por dúvida: D, seção 3.1 e seção 1, item 3'),
 (41, 'L132', 'Não publicar tudo de uma vez: D, seção 7 e seção 10, premissa 13 (ritmo: PREMISSA)'),
 (42, 'L133', 'Texto de IA sem revisão; página sem dado próprio: D, seção 7; A, seções 2.1 e 3'),
 (43, 'L134', 'Página de oferta antes de haver licenciada: D, seção 4.4'),
 (44, 'L135', '"24 horas", "garantia", "seguro", "a melhor", estrelas, lista de bairros: D, seções 2, 3.4 e 4.3; P, seção 6'),
 (45, 'L136', 'O Google não dá prazo; o guia trabalha com 6 a 12 meses como premissa (A, seção 9)'),
 (46, 'L142-146', 'Premissa 3: resumo de IA nas 10 buscas do grupo H, 4 informativas (S, 12.1); Pew, 2025, Estados Unidos, classe B: menos clique com resumo de IA (A, seção 7)'),
]
SEMENTE = 'v2-reserva3-20261114'
random.seed(SEMENTE)
sorteadas = sorted(random.sample(AFIRMACOES, 12))
print('semente:', SEMENTE, '| universo:', len(AFIRMACOES), '| sorteadas:', [a[0] for a in sorteadas])
for n, l, t in sorteadas: print(f'{n:>2} | {l:<9} | {t}')
