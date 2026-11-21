---
id: logica-consequencia-vs-derivacao
titulo: Diferença entre ⊨ e ⊢: consequência lógica, derivação, corretude e completude
assunto: logica-08-corretude-completude
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica de predicados: Semântica, completude e corretude (Tiago Massoni, UFCG); slides Forma Normal: equivalência (UFCG)
fontes_catalogo: ufcg-massoni-slides
autoria: Prof. Tiago Massoni (UFCG; Alloy com Prof. Rohit Gheyi), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Qual a diferença entre ⊨ e ⊢** ($\models$ e $\vdash$)**:** a diferença é que consequência lógica é semântica (vale em todos os modelos); derivação é sintática (existe uma prova com regras).
- $\Gamma\models\psi$ (símbolo "turnstile duplo", **consequência lógica**, semântica): em todo modelo (valoração, na lógica proposicional) em que todas as fórmulas de $\Gamma$ são verdadeiras, $\psi$ também é. Mostra-se com tabela-verdade, tableau ou raciocínio sobre modelos.
- $\Gamma\vdash\psi$ ("turnstile", **derivação**, sintaxe): existe uma prova de $\psi$ a partir de $\Gamma$ com as regras de um sistema (dedução natural, resolução). Mostra-se exibindo a prova.

**Corretude** (soundness): se $\Gamma\vdash\psi$ então $\Gamma\models\psi$; as regras nunca provam algo falso. **Completude:** se $\Gamma\models\psi$ então $\Gamma\vdash\psi$; tudo o que é consequência tem prova. As duas valem para a lógica proposicional e para a de primeira ordem (dedução natural). Por isso $\varphi\equiv\psi$ é o mesmo que $\varphi\dashv\vdash\psi$.

**Como usar:** para mostrar que um argumento **vale**, basta uma prova ($\vdash$). Para mostrar que **não vale**, uma tentativa de prova que falha não basta: exiba um **contramodelo** (pela corretude, se houvesse prova, não haveria contramodelo).

**Exemplo:** $\{p\to q,\;\neg q\}\models\neg p$ (nenhuma das 4 valorações é contramodelo) e $p\to q,\;\neg q\vdash\neg p$ (uma linha de MT). Já $\{p\to q,\;q\}\not\models p$: $p$=F, $q$=V é contramodelo, logo não existe prova.

**Na primeira ordem:** a validade é indecidível (Church); não há tabela-verdade; verifica-se $\models$ raciocinando sobre todos os modelos, ou procurando prova ($\vdash$).

**Verificação:** as duas consequências do exemplo foram conferidas por tabela-verdade em Python, e a prova de uma linha pelo verificador de dedução natural.
