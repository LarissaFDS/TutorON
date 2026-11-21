---
id: logica-conectivos-exercicios-concurso
titulo: Exercícios de conectivos: condição necessária e suficiente, contrapositiva e negação de conjunção
assunto: logica-03-consequencia-equivalencia
tipo: exercicio
resolucao: sim
questao: 1-5
fonte: Slides de Lógica Clássica Proposicional (Baldoino Fonseca, UFAL), exercícios de conectivos lógicos (questões de concurso)
fontes_catalogo: ufal-baldoino-slides-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Exercício da turma (paráfrase do enunciado) com resolução. Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

1. "Se você se esforçar, então vai vencer" ($E\to V$). Equivale a "o esforço é **condição suficiente** para vencer" (alternativa e). "Só vence se se esforçar" seria $V\to E$ (condição necessária), outra fórmula.
2. "Se Fulano mentiu, então é culpado" ($M\to C$). Segue a **contrapositiva** $\neg C\to\neg M$: "se não é culpado, não mentiu" (alternativa d). A recíproca $C\to M$ e a inversa $\neg M\to\neg C$ não seguem.
3. Negar "o pai de Marcos é pernambucano **e** a mãe é gaúcha": por De Morgan, $\neg(A\land B)\equiv\neg A\lor\neg B$: "o pai **não** é pernambucano **ou** a mãe **não** é gaúcha" (alternativa b).
4. "Se não leio, não compreendo; se jogo, não leio; se não desisto, compreendo; se é feriado, não desisto": $\neg L\to\neg C$, $J\to\neg L$, $\neg D\to C$, $F\to\neg D$. Encadeando $J\to\neg L\to\neg C\to D$ e $D\to\neg F$ (contrapositiva da última): "se jogo, não é feriado" (alternativa a).
5. Artur: $F\lor\neg G$ (lógica é fácil ou Artur não gosta de lógica), $\neg D\to\neg F$ (se geografia não é difícil, lógica é difícil). Com $G$ verdadeiro, $F$ é V; pela contrapositiva, $D$ é V: "lógica é fácil e geografia é difícil" (alternativa b).

**Verificação:** cada alternativa foi testada por tabela-verdade completa: em cada item, só a indicada é consequência lógica das premissas.
