---
id: ia-logica-proposicional-validade-satisfatibilidade-tautologia-contradicao-consequencia-logica-tabela-verdade
titulo: Lógica proposicional para RCR: fórmula válida (tautologia), insatisfatível (contradição), satisfatível e inválida; consequência lógica e verificação por tabela-verdade
assunto: ia-03-conhecimento-e-raciocinio
tipo: material_estudo
questao: aula 3 de Lógica Proposicional (consequência lógica, 2013)
resolucao: sim
fonte: Aulas de Representação de Conhecimento e Raciocínio e de Lógica Proposicional do Prof. Evandro Costa (IC-UFAL), 2013 e 2016
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-evandro-rcr-logica
autoria: Slides do Prof. Evandro Costa (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), aula 3 de Lógica Proposicional (consequência lógica, 2013) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Uma fórmula bem formada (fbf) é:
- **válida (tautologia):** verdadeira em **todas** as interpretações;
- **insatisfatível (contradição, inconsistente):** falsa em todas;
- **inválida:** falsa em pelo menos uma;
- **satisfatível (consistente):** verdadeira em pelo menos uma.

**Exemplo:** $a = (P \to \lnot Q) \land (\lnot P \to Q)$ (se P então não Q, e se não P então Q) só é verdadeira quando $P$ e $Q$ têm valores diferentes: é **satisfatível e inválida** (equivale a $P \oplus Q$).

**Validade por tabela-verdade:** $((P \to Q) \land (Q \to R) \land P) \to R$ tem 3 átomos e $2^3 = 8$ interpretações. Em todas vale V: é uma **tautologia** (silogismo hipotético seguido de modus ponens).

**Consequência lógica:** $\Gamma \models \alpha$ (alfa decorre de gama) se todo modelo de $\Gamma$ é modelo de $\alpha$. Equivale a:
- $(\gamma_1 \land \dots \land \gamma_n) \to \alpha$ ser válida;
- $\Gamma \cup \{\lnot\alpha\}$ ser insatisfatível (base da prova por **refutação** e da **resolução**).

**Custo:** a tabela-verdade cresce como $2^n$; com muitos átomos usam-se regras de inferência, resolução ou SAT solvers.

Tableaux, dedução natural e resolução em detalhe ficam em Lógica para Computação; aqui o foco é a lógica como linguagem da base de conhecimento.

**Verificação:** `test_validade_tabela_verdade` percorre as 8 interpretações e confere que a fórmula é tautologia e que $a$ é satisfatível e inválida.
