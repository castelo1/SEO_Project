#!/usr/bin/env python3
# Segunda passada, reserva 5 - sorteio de 12 afirmacoes de docs/medicao_modelo.md (todas as 36 foram conferidas; o sorteio e so para o placar). So leitura.
import random
SEMENTE='verificacao2-reserva5-20261114'
AF=[
'L7-8: uma linha por pagina x periodo de 28 dias x licenciada; virgula; UTF-8; AAAA-MM-DD; decimal com ponto',
'L13-14: tres colunas vem da licenciada',
'L14: nenhuma coluna e preenchida por consulta automatica ao Google',
'L18-19: A 8 recomenda comparar periodos iguais (semana ou 28 dias) e esperar ao menos uma semana depois do fim de atualizacao central',
'L26: exemplo = "sim" nas linhas de exemplo (as duas linhas do CSV)',
'L27: periodo de 28 dias (A 8)',
'L28: pagina = caminho, como no endereco (D 3.4, enderecos)',
'L29: tipo_pagina T1 a T12 (D 3.1)',
'L31: licenciada = nome da empresa nomeada na pagina; uma linha por licenciada (D 4.1)',
'L32: impressoes (A 8, classe A)',
'L33: cliques_na_busca (A 8, classe A); nao e o toque no botao',
'L34: taxa_de_clique = cliques / impressoes (A 8)',
'L35: posicao_media: resultado mais alto; bloco; resumo de IA; mapa nao descrito (A 8)',
'L36: impressoes_em_ia: so impressoes; ja dentro do total (C 1.3, classe A)',
'L37: buscas_conferidas_a_mao: pessoa digita, sem script (D 6, linha "Posicao na tela")',
'L38: posicao_na_tela_mediana (D 6; A 8: vale para uma pessoa, um lugar, um momento)',
'L39: visitas dos robos, do registro de acesso bruto (D 3.4 e D 6; G 9, linha 15)',
'L40: leads_toque_no_botao (D 5.1 e D 6)',
'L41: leads_pedido_formulario (D 5.2 e D 6)',
'L42: leads_validos = contatos que a licenciada confirma ter recebido com o codigo; contagem mensal (D 6, PREMISSA)',
'L43: orcamentos (D 6, PREMISSA)',
'L44: servicos_fechados: para a taxa de fechamento, nao para cobrar (D 6)',
'L45: leads_vendidos = leads validos pagos; por unidade ou cobertos pela mensalidade; zero antes da fase 4 (D 6 e D 8)',
'L46: forma_de_cobranca; unidade de cobranca e decisao do owner (D 8)',
'L47: preco_combinado_reais; o valor nao tem fonte de mercado (D 8)',
'L48: receita_reais = leads vendidos x preco, ou a mensalidade (D 6, linha "Receita por pagina")',
'L49: atualizacao_central_no_periodo; painel de status (A 8; A 1.3)',
'L50: observacao sem dado pessoal',
'L58: taxa de fechamento nao tem fonte brasileira',
'L60: nao somar impressoes com impressoes_em_ia (C 1.3)',
'L65-66: ChatGPT tem roteiro e planilha proprios (caminho)',
'L67: posicao no mapa: nao medir (D 6, "Nao medir")',
'L68-69: volume em data/palavras_chave.csv, coluna "volume", hoje "nao medido"',
'L3: escrito em 13/11/2026 as 22:41',
'CSV, linha de exemplo 1: coerente (taxa vazia com impressoes 0; receita = vendidos x preco)',
'CSV, linha de exemplo 2: pagina de guia, sem botao nem licenciada, colunas de lead vazias',
]
r=random.Random(SEMENTE)
idx=sorted(r.sample(range(1,len(AF)+1),12))
print('semente:',SEMENTE,'| universo:',len(AF),'| sorteadas:',idx)
for i in idx: print(i,'-',AF[i-1])
