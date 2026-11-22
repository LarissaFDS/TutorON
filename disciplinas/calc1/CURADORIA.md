# Curadoria — Cálculo 1 (`calc1`, ECOM004)

Situação: **MVP** desde 21/11/2026, sem aviso: suíte, bateria de relevância e perguntas de exemplo com a IA real passaram. Blocos com `revisao_humana: pendente`; resoluções da equipe TutorON conferidas por código (`tests_acervo/test_disciplina_calc1.py`), não gabarito do professor.

## Disciplina

- Código ECOM004, 60 h, Engenharia de Computação da UFAL (PPC versão 2014, `ufal-ecom-ppc-2014-ementa`). Ementa: funções e gráficos; limite e continuidade; a derivada e a derivação; valores extremos; técnicas de construção de gráficos; a diferencial; integração e a integral definida. O texto foi lido em dois trechos do PDF: conferir palavra a palavra com o plano de curso.
- Professor: as provas do pacote não trazem nome impresso. Não foi registrado nenhum professor.
- Os 11 assuntos seguem a ementa e os tópicos pedidos pela equipe.

## Fotos e dados pessoais

- Fotos de provas e de resoluções manuscritas foram lidas e parafraseadas; **nenhuma imagem ou PDF está no repositório**.
- Nas fotos de prova os nomes estão apagados; nas resoluções manuscritas não há nome visível. Links de redes sociais dos arquivos de dicas não foram copiados. Há teste contra e-mail, link de grupo e endereço web nos blocos.
- Publicação da transcrição não autorizada: os blocos trazem o enunciado parafraseado com os dados.

## Fontes (`fontes.json`)

| id | Uso | Licença |
|---|---|---|
| `ufal-ecom-ppc-2014-ementa` | citada | Documento institucional público; licença não declarada |
| `ufal-im-calc1-provas-fotos` | acervo | Não declarada (prova da disciplina) |
| `ufal-im-calc1-provas-pdf` | acervo | Não declarada (prova da disciplina) |
| `ufal-im-calc1-banco` | acervo | Não declarada |
| `ufal-calc1-resolucoes-manuscritas` | acervo | Não declarada |
| `ufal-calc1-aula-distancia-2017` | acervo | Não declarada |
| `ufal-calc1-listas-simulados` | acervo | Não declarada |
| `ufal-calc1-dicas-apoio` | acervo | Não declarada |
| `ufal-im-thales-slides` | citada | Não declarada |
| `lista-xu-yang-comp210` | candidato | Não declarada |
| `stewart-calculo-slides-cengage` | referencia | Protegido (direitos reservados) |
| `stewart-calculo` | referencia | Protegido (direitos reservados) |
| `stewart-solucoes` | referencia | Protegido (direitos reservados) |
| `apostol-calculus` | referencia | Protegido (direitos reservados) |
| `openstax-calculus-v1` | referencia | CC BY-NC-SA 4.0 |
| `active-calculus` | candidato | CC BY-SA (versão 2.0 segundo o link do livro; conferir) |
| `mit-ocw-1801sc` | citada | CC BY-NC-SA 4.0 |
| `geogebra` | citada | Termos de uso do GeoGebra (não é material) |
| `desmos` | citada | Termos de uso do Desmos (não é material) |

Livros protegidos (Stewart, manual de soluções, Apostol) e os slides da editora: só referência por seção; não transcritos, versionados nem ingeridos. OpenStax não é ingerido por causa da restrição a treino de modelos no prefácio.

## Blocos

| id | Assunto | Status |
|---|---|---|
| `calc1-inequacao-trig-crescimento` | calc1-01-funcoes-inequacoes-modulo | validada |
| `calc1-limite-modulo-confronto` | calc1-01-funcoes-inequacoes-modulo | validada |
| `calc1-limites-algebricos` | calc1-02-limites-continuidade | validada |
| `calc1-continuidade-por-partes` | calc1-02-limites-continuidade | validada |
| `calc1-tvi-raizes` | calc1-02-limites-continuidade | pendente_professor |
| `calc1-assintotas-limites-infinito` | calc1-03-limites-infinito-assintotas | validada |
| `calc1-derivada-pela-definicao` | calc1-04-derivada-definicao-tangente | validada |
| `calc1-retas-tangentes-problemas` | calc1-04-derivada-definicao-tangente | validada |
| `calc1-diferenciabilidade` | calc1-04-derivada-definicao-tangente | validada |
| `calc1-regra-cadeia-tangente-horizontal` | calc1-05-regras-derivacao | corrigida |
| `calc1-derivacao-implicita` | calc1-05-regras-derivacao | validada |
| `calc1-derivadas-log-inversas` | calc1-05-regras-derivacao | validada |
| `calc1-funcoes-hiperbolicas` | calc1-05-regras-derivacao | validada |
| `calc1-taxas-relacionadas` | calc1-06-taxas-aproximacao-linear | validada |
| `calc1-aproximacao-linear` | calc1-06-taxas-aproximacao-linear | validada |
| `calc1-extremos-absolutos` | calc1-07-extremos-tvm | validada |
| `calc1-tvm-rolle` | calc1-07-extremos-tvm | pendente_professor |
| `calc1-esboco-grafico` | calc1-08-esboco-graficos | validada |
| `calc1-regra-lhospital` | calc1-09-lhospital | validada |
| `calc1-otimizacao-geometrica` | calc1-10-otimizacao | corrigida |
| `calc1-otimizacao-custo` | calc1-10-otimizacao | validada |
| `calc1-primitivas-condicoes` | calc1-11-primitivas-integral | validada |
| `calc1-integral-definida` | calc1-11-primitivas-integral | validada |

## Correções e pendências

- `calc1-regra-cadeia-tangente-horizontal` (corrigida): a resolução manuscrita diz y = 5 em todos os pontos de tangente horizontal de 5^(sen²(2x+3)); para n par o valor é 1.
- `calc1-otimizacao-geometrica` (corrigida): anotação "π/4" na foto da questão da calha; o ângulo ótimo é π/3.
- `calc1-tvi-raizes` (pendente do professor): o sinal de y = −15x na prova de 30.08.2014 torna o enunciado falso (uma interseção só); com 15x há três.
- `calc1-tvm-rolle` (pendente do professor): f′ ≤ 5 com intervalo aberto (2, 4); a resposta depende da continuidade nas pontas.
- "Três exercícios com soluções" (2017): erro de passagem, lim_{x→1⁻} √(1−x²) vale 0, não 1; a conclusão não muda.
- Simulado 2016.1, RESOL. AB1, "Exercícios resolvidos" e "Três exercícios" foram conferidos onde usados.
- Não há problema da escada no pacote; o bloco de taxas relacionadas traz o roteiro que serve para ele.

## Fronteiras

- Cálculo 2: técnicas de integração, integrais impróprias, aplicações da integral, séries.
- Cálculo 3: várias variáveis, derivadas parciais, integrais múltiplas.
- Física 1: cinemática e dinâmica; aqui só a derivada como taxa. Isolamento testado nos dois sentidos.

## Pendências

- Revisão humana dos 23 blocos e confirmação das duas pendências com o professor.
- Conferir a ementa com o plano de curso; confirmar a autoria do banco de questões e da lista COMP210.
- Conferir a versão e a licença do Active Calculus antes de usá-lo.

## Complemento de Ciência da Computação (22/11/2026)

O TutorON organiza o acervo por disciplina, não por curso: o material de Cálculo Diferencial e Integral de Ciência da Computação (COMP363; no PPC de 2011, CCOM011 Cálculo 1) entrou na disciplina `calc1` já existente, sem cópia e sem mudar a situação.

**Ementas.** A ementa de CCOM011 no PPC de CC (`ufal-ppc-cc-2011`) é igual, palavra por palavra, à de ECOM004. As duas turmas fazem as provas do Instituto de Matemática.

**Fontes novas:** `ufal-ppc-cc-2011` (citada), `ufal-cc-calc1-banco-provas` (acervo) e `ufal-cc-calc1-bancos-solucionados` (referência; bancos solucionados, Stewart, Guidorizzi e Apostol ficaram fora do pacote e não foram abertos).

**O que entrou.** O banco da turma de CC tem as provas avulsas do IM-UFAL de 2003 a 2013. As de 2012.2 e 2013 já estavam no acervo pelas fotos de ECOM; viraram blocos novos só as 4ª provas de 2006 e 2007, que cobrem limites com potência, primitivas, TVM, otimização e esboço:

| Bloco | Tema | Status da resolução |
|---|---|---|
| `calc1-cc-limites-potencias-log` | $1^\infty$, $0\cdot\infty$ e 0/0 com logaritmo | validada |
| `calc1-cc-primitivas-tvm-estimativa` | f a partir de f'' e derivada terceira com condições; estimativa pelo TVM | corrigida |
| `calc1-cc-otimizacao-cercas` | cerca de menor custo e maior área com dois arames | validada |
| `calc1-cc-esboco-x3-sobre-x2-menos-1` | esboço completo de x³/(x² − 1) | validada |

**Correção.** Na 4ª prova de 2007 (Q5a), a derivada terceira é $2-6x$, com "(0, 2) ponto de máximo local" e "(1, 31/12) ponto de inflexão": as condições determinam $y=-x^4/4+x^3/3+x^2/2+2$, mas $y''(0)=1>0$, então (0, 2) é mínimo local. O bloco é `corrigida` e explica a divergência.

**Dados pessoais.** As provas escaneadas trazem nomes de alunos e de professores escritos à mão; nada disso foi copiado. Nenhum PDF ou imagem foi versionado. As demais provas (2003 a 2011, Prova 1 a 3) foram lidas como evidência dos tópicos, que já têm bloco.
