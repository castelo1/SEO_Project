# Notas da classificação de domínios — parte 1 (35 domínios)

Arquivo de dados: `/home/ancastelo/pessoal/SEO_Project/data/serp_dominios_classe_parte1.csv`. Leituras feitas em 13/11/2026, das 21:21 às 21:36 (horário de São Paulo).

## Limite desta classificação

- Cada domínio foi lido em 1 a 3 páginas (inicial, uma página que apareceu no resultado, e "quem somos"/"empresa"/"contato" quando havia), por uma ferramenta que baixa a página e devolve um resumo feito por um modelo pequeno. Eu não vi o HTML nem as imagens.
- "não visto" quer dizer que o resumo não mostrou. Não prova ausência. Número de licença em imagem, em PDF ou em página não aberta fica de fora.
- Nenhum número de licença foi conferido em base oficial. Nenhum CNPJ foi consultado.
- As contagens de links ("cerca de 270") são estimativas do resumo, não contagem minha.
- Em alguns domínios consultei a inicial uma segunda vez (mesma URL, resposta em cache) só para achar o endereço da página "quem somos". Nenhum domínio teve mais de 3 URLs abertas.

Horas de leitura por lote (as colunas `urls_abertas` e `hora_leitura` do CSV seguem a mesma ordem):
21:21 e 21:23 a 21:25, páginas iniciais; 21:27 a 21:29, páginas que apareceram no resultado; 21:31 a 21:36, páginas institucionais e as restantes.

## (a) Contagem por classe

| classe | domínios |
|---|---|
| `empresa_sem_licenca_vista` | 19 |
| `empresa_licenca_exibida` | 7 |
| `gerador_de_leads_ou_rede` | 7 |
| `diretorio_marketplace` | 1 |
| `nao_abriu` | 1 |
| `governo_universidade`, `rede_social_forum`, `outro` | 0 |

Como li a regra das classes:

- Número de licença no texto: `empresa_licenca_exibida`, mesmo com sinais de rede (o sinal vai na coluna própria).
- Sem número, mas com CNPJ, razão social ou endereço: `empresa_sem_licenca_vista`.
- Nenhum dos três identificadores nas páginas abertas: `gerador_de_leads_ou_rede`. Em cinco dos sete casos (protecpragas, exterminex, gallidedetizadora, primosdedetizadora, santanadedetizadora) a classe vem só dessa ausência. Nenhum deles declara repassar pedidos; todos falam em equipe própria. São os casos mais frágeis da tabela.
- Duas classes são disputáveis e estão marcadas na coluna `observacao`: universoambiental.eco.br (mostra CEVS, mas tem sinais de rede) e biosolucoes.app.br (mostra CNPJ, mas o próprio site traz os sinais de rede).

Os 7 com número de licença no texto (rótulo como aparece na página):

| domínio | rótulo e número | URL | hora |
|---|---|---|---|
| dedetizadora.srv.br | "Licença Sanitária: 351500404-812-00058-1-9" e "Alvará de Funcionamento: 84/2026" | https://dedetizadora.srv.br/ | 21:21 |
| eccocleandedetizacao.com.br | "CEVS: 355030890-812-000266-1-1" | https://eccocleandedetizacao.com.br/ | 21:21 |
| lunardedetizadora.com.br | "CEVS: 351060902-812-000006-1-2" | https://lunardedetizadora.com.br/ | 21:23 |
| biosp.com.br | "Sistema de Informação de Vigilância Sanitária de estado de São Paulo sob o número 351630901-812-000034-1-7" | https://biosp.com.br/ | 21:23 |
| universoambiental.eco.br | "CEVS: 353780001- 812000004 -1- 8" | http://www.universoambiental.eco.br/preco-de-dedetizacao--osasco-sp | 21:29 |
| desentupidoraimperio.com.br | "CEVS: 355030890-812-000209-1-5" | https://desentupidoraimperio.com.br/ | 21:25 |
| alvodedetizadora.com.br | "Licença Anvisa 355030890-812-000271-1-1" | https://alvodedetizadora.com.br/ | 21:25 |

Pista não verificada: três números começam por 355030 e os outros quatro por prefixos diferentes. Se o prefixo for código de município, parte dessas licenças seria de fora da capital. Não conferi isso em fonte nenhuma; fica para a sessão principal checar no SIVISA.

## (b) Padrões que se repetem

1. **Uma página por bairro, zona ou cidade, com texto genérico e o nome do lugar inserido.** Vista em 30 dos 34 domínios abertos (coluna `paginas_por_bairro`). Onde o molde ficou à mostra:
   - depoimentos da página do Ipiranga citam Osasco, Pirituba, Barueri e Guarulhos — https://protecpragas.com.br/dedetizadora-ipiranga/ (21:27);
   - a página de Pinheiros fala em "todo o bairro do Morumbi" e em orçamento "em Atibaia" — https://heloindedetizadora.com.br/empresa-de-dedetizacao-em-pinheiros/ (21:29);
   - a FAQ da página de Perdizes pergunta quanto custa "na Zona Sul" — https://primordialdedetizacao.com.br/dedetizadora-em-perdizes/ (21:28);
   - "São Paulo é uma cidade média de São Paulo" — https://grupoexpansao.com/sao-paulo/dedetizacao/lapa/ (21:29);
   - a imagem da página de Pinheiros tem nome de arquivo de Alphaville — https://etoprag.com.br/empresa-de-dedetizacao-em-pinheiros/ (21:31);
   - texto sobre Osasco com trechos sobre os Estados Unidos e "Estado de Osasco" — http://www.universoambiental.eco.br/preco-de-dedetizacao--osasco-sp (21:29).
   Exceções parciais, com algum dado local: https://ecoservicos.com.br/dedetizadora-moema/ (21:27), https://doctorinsect.com/dedetizadora-em-osasco/ (21:28), https://zet-tecdedetizadora.com.br/dedetizadora-em-santo-amaro/ (21:29).

2. **Listas longas de links internos para bairros e palavras-chave na mesma página.** Estimativas do resumo: cerca de 270 em protecpragas (URL acima); cerca de 180 em zet-tec (URL acima); cerca de 150 em https://keikodedetizadora.com.br/servicos/dedetizadora-no-tatuape (21:27); 100 a 150 em https://eccocleandedetizacao.com.br/dedetizadora-sp.php (21:27); cerca de 120 em primordial (URL acima); cerca de 108 em https://deltadedetizacao.com.br/dedetizacao-em-sao-paulo/ (21:27); cerca de 110 em https://biosolucoes.app.br/sao-paulo-sp/dedetizacao-de-aranhas (21:31); cerca de 88 em http://www.exterminex.com.br/servico-de-dedetizacao-em-perdizes.php (21:28); cerca de 80 em https://interprag.com.br/dedetizacao-santo-amaro (21:28).

3. **"24 horas" (ou "24h").** Visto em 20 dos 34 domínios abertos. Não visto como oferta em 14: eccoclean, uniprag, dedetizabem, termitek, ohub, exterminex, biodesin (horário comercial), interprag, doctorinsect, grupoexpansao, ambientalepragas, império (08:00 às 22:00), etoprag (horário comercial), alvo. Contradição na mesma página: "Atendimento 24 horas" e "Segunda a sexta – 10h às 18h" — https://primosdedetizadora.com.br/ (21:25).

4. **Licença afirmada sem número.** Em 14 domínios a página diz ser legalizada ou licenciada e não mostra número. Exemplos: "dedetizadora 100% legalizada e certificada" — https://protecpragas.com.br/ (21:21); "100% legalizada na prefeitura e vigilância sanitária de SP" — https://deltadedetizacao.com.br/ (21:21); selo "Empresa Licenciada pela Vigilância Sanitária" — https://doctorinsect.com/ (21:23); logotipos de órgãos sob "Nossas licenças" — https://ecoservicos.com.br/ (21:23); "Registro nos órgãos competentes" — https://etoprag.com.br/ (21:25); licença e alvará só como links para PDF — https://www.biodesin.com.br/quem-somos/ (21:34). Quando há número, o rótulo varia (ver tabela acima): "Licença Sanitária", "CEVS", "SIVISA", "Licença Anvisa".

5. **Telefone no título da página.** Visto em 5 domínios: https://protecpragas.com.br/ (21:21), https://biodesin.com.br/ (21:23), http://www.universoambiental.eco.br/ (21:25), https://dedetizadora.srv.br/atendimento/dedetizacao-zona-leste/ (21:27), https://dedetizadoraddpilar.com.br/dedetizadora-na-mooca/ (21:29). O `serp_sp.csv` mostra "[tel]" também em títulos de deltadedetizacao e dedetizadoranovatec, em páginas que não abri.

6. **Vocabulário de segurança e de aprovação.**
   - "Anvisa" quase sempre se refere a produto, não à empresa: "aprovados e regulamentados pela ANVISA" — https://dedetizadora.srv.br/ (21:21); "produtos seguros e aprovados pela ANVISA" — https://santanadedetizadora.com.br/ (21:25); "Produtos registrados na Anvisa" — https://hidrosampa.com.br/ (21:24). Como atributo da empresa: "Legalizada na Anvisa" — https://alvodedetizadora.com.br/ (21:25); "Certificação ANVISA e Vigilância Sanitária" — heloin, página de Pinheiros (21:29).
   - "sem cheiro": keiko (21:21), delta (21:27), ecoservicos/Moema (21:27), lunar/Bela Vista (21:28), agro (21:24), primos (21:25), heloin/Pinheiros (21:29).
   - "atóxico" apareceu em duas páginas só. Uma para armadilhas ("armadilhas adesivas atóxicas", etoprag/Pinheiros, 21:31). A outra para negar a promessa: "Nenhum inseticida é atóxico" e "desconfie de empresas que vendem que os produtos usados na desinsetização são 100% seguros" — https://biodesin.com.br/dedetizadora-em-perdizes/ (21:28).
   - Garantia com prazos muito diferentes: "até 1 ano" (dedetizadora.srv.br, 21:21; zet-tec, 21:24); "até 3 anos" e "até 3 meses" na mesma página (delta, 21:21); 3 meses (primordial, 21:23; primos, 21:25; ecoservicos/Moema, 21:27); "Garantia Anual" (hidrosampa, 21:24).

7. **Preço à vista é raro.** Visto em 3 domínios: "a partir de R$79" no título — https://deltadedetizacao.com.br/dedetizacao-em-sao-paulo/ (21:27); "planos a partir de R$150,00" — heloin/Pinheiros (21:29); tabela com valores que não batem entre si — universoambiental/Osasco (21:29). Os demais dizem "orçamento grátis" ou "preço justo".

8. **Selos.** Selos técnicos de site (W3C, PageSpeed, SSL) usados como "Selo da empresa" — https://eccocleandedetizacao.com.br/ (21:21), http://www.exterminex.com.br/ (21:24), https://interprag.com.br/ (21:23). Logotipos de órgãos e entidades (Anvisa, CRQ-IV, APRAG, SindPrag, SGS) — https://desentupidoraimperio.com.br/ (21:25), https://alvodedetizadora.com.br/ (21:25). ISO 9001 — https://uniprag.com.br/ (21:21). Avaliações do Google via Trustindex — https://dedetizabem.com.br/ (21:21), https://termitek.com.br/ (21:21).

9. **Dedetizadora e desentupidora na mesma marca.** Protec, Osaka, Interprag, Hidrosampa, Zet-Tec, DDPilar, Império, Bio Soluções, EcoServiços e Delta oferecem os dois serviços (páginas iniciais, 21:21 a 21:25).

## (c) Indícios de rede de sites

- **Rede Uniprag (declarada).** https://uniprag.com.br/quem-somos/ (21:31) lista contatos por estado que apontam para 10 domínios de outras marcas; para São Paulo, termitek.com.br. https://www.termitek.com.br/quem-somos/ (21:31) diz ser "unidade da rede Uniprag". Uniprag e Termitek somam 49 resultados orgânicos na coleta (26 e 23, segundo `serp_dominios.csv`).
- **Dedetiza Bem.** Mesma agência no rodapé ("Agência Digital Space") e mesmo padrão de título com "//" que Uniprag e Termitek — https://dedetizabem.com.br/ (21:21). Nenhuma página aberta declara vínculo. Pode ser só o mesmo fornecedor de site.
- **Par MarketingWeb.** O rodapé de https://biosolucoes.app.br/ (21:25) tem "Sites Parceiros" com cinco domínios: dedetizadorasorocaba.com.br, cupim.eco.br, universoambiental.eco.br, desentupidora.emp.br e osascenter.com.br. Os dois sites da minha lista creditam o mesmo desenvolvedor e usam páginas por cidade geradas em série. O texto de https://biosolucoes.app.br/sao-paulo-sp/dedetizacao-de-aranhas (21:31) cita "Combate Ambiental" como nome da empresa. É o indício mais forte de rede de mesmo molde nesta parte.
- **Molde comum em três marcas.** eccoclean, exterminex e interprag têm os mesmos selos de site, páginas `.php` (ou sem extensão, em interprag), lista "Informações" com dezenas de links e aviso de direitos autorais. Só interprag credita o fornecedor ("MPI Technology", 21:23). Indica mesmo fornecedor de site e de SEO, não mesmo dono: eccoclean mostra CEVS e endereço próprios.
- **Agência especializada.** primordial e lunar creditam "Prismus Digital"; em primordial o rodapé diz "Performance Para Dedetizadoras" (21:23). Cada uma mostra CNPJ; não comparei os números.
- **Sinais soltos.** Protec cita "Protec Desentupidora" em outro domínio (21:21). O logotipo de ambientalepragas tem nome de arquivo "logo-hidrotex" (21:24). santanadedetizadora tem links para um domínio de teste e comentários automáticos de sites sem relação (21:25 e 21:31). Quatro domínios mostram endereço na Bela Vista (primordial, doctorinsect, novatec e uma unidade da hidrosampa); não comparei logradouros.
- **Diretório.** https://ohub.com.br/empresas/dedetizacao/sp/sao-paulo (21:21): "O oHub reúne empresas de Dedetização em São Paulo/SP", "Receba até 4 propostas qualificadas em 24 horas", 30 empresas na página, ordem que "considera fatores como volume de respostas na plataforma".

## (d) O que não abriu ou abriu pela metade

- **rentokil.com** — `nao_abriu`. Três tentativas, três respostas 403: https://www.rentokil.com/br/ (21:25), https://www.rentokil.com/br/sobre-a-rentokil/unidade-local/ (21:31), https://rentokil.com/br/ (21:36).
- **dedetizadoranovatec.com.br** — só a inicial (21:25). `/tabela-de-preco-de-dedetizacao/` (21:31 e 21:36) e `/dedetizadora/` (21:36) deram tempo esgotado.
- **exterminex.com.br e universoambiental.eco.br** — o endereço `https://` sem `www` redireciona para `http://www.`; li por esse segundo endereço.
- **hidrosampa e zet-tec** — as páginas de bairro passam de 100 mil caracteres; o resumo cobriu só os primeiros 100 mil (o rodapé de zet-tec ficou de fora).
- **uniprag, termitek, primos, império, biosolucoes, ambientalepragas** — parte dos caminhos está cortada em 50 caracteres no CSV; abri um caminho inteiro do mesmo domínio.
- **ohub.com.br** — uma leitura só (a página do resultado).

## Pedidos de ação nas páginas

Todas as páginas de empresa pedem contato ("Ligue agora", "Solicitar orçamento", "Chama no ZAP", formulário). Nada foi clicado, preenchido ou enviado. Nenhum telefone, e-mail, nome de pessoa, número de CNPJ ou texto de avaliação foi gravado.
