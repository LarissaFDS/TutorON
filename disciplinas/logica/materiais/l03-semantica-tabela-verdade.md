---
id: logica-semantica-tabela-verdade
titulo: Semântica proposicional: valoração, tabela-verdade dos conectivos, modelos, validade e satisfazibilidade
assunto: logica-02-proposicional-sintaxe-semantica
tipo: material_estudo
resolucao: sim
fonte: Slides de Lógica Clássica Proposicional e Linguagens Proposicionais (Baldoino Fonseca, UFAL), semântica
fontes_catalogo: ufal-baldoino-slides-proposicional
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: corrigida (resolução da equipe TutorON, não é gabarito do professor; conferida com Python; o original tem erro apontado abaixo).

Uma **valoração** (interpretação) é uma função $v$ que dá V ou F a cada símbolo proposicional. Ela se estende às fórmulas: $\neg a$ é V quando $a$ é F; $a\land b$ é V só quando ambos são V; $a\lor b$ é F só quando ambos são F; $a\to b$ é F só quando $a$ é V e $b$ é F; $a\leftrightarrow b$ é V quando $a$ e $b$ têm o mesmo valor. Uma valoração que torna $\Phi$ verdadeira é um **modelo** de $\Phi$.

| $P$ | $Q$ | $\neg P$ | $P\land Q$ | $P\lor Q$ | $P\to Q$ | $P\leftrightarrow Q$ |
|---|---|---|---|---|---|---|
| V | V | F | V | V | V | V |
| V | F | F | F | V | F | F |
| F | V | V | F | V | V | F |
| F | F | V | F | F | V | V |

**Válida** (tautologia): V em todas as valorações. **Satisfazível:** V em pelo menos uma. **Insatisfazível** (contraditória): F em todas. $\varphi$ é satisfazível se e somente se $\neg\varphi$ não é válida.

**Exemplos dos slides:** $P\to(P\lor Q)$ é válida. $(P\to\neg Q)\land(\neg P\to Q)$ é V exatamente quando $P$ e $Q$ têm valores diferentes (2ª e 3ª linhas). **Correção:** o slide lista $I_1=\{P,Q\}$, $I_2=\{P,\neg Q\}$, $I_3=\{\neg P,Q\}$ e repete $I_4=\{P,\neg Q\}$; a quarta é $\{\neg P,\neg Q\}$.

**Verificação:** as cinco colunas e os dois exemplos foram recalculados em Python nas 4 valorações.
