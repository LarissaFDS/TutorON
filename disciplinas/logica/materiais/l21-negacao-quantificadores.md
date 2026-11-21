---
id: logica-negacao-quantificadores
titulo: Como negar frases com quantificador: "todo aluno estuda", "algum", "nenhum"
assunto: logica-09-primeira-ordem-formalizacao
tipo: material_estudo
resolucao: sim
fonte: Slides Lógica de predicados: Semântica (Tiago Massoni, UFCG), validade de ∀x¬P(x) → ¬∃xP(x); slides Linguagens de Primeira Ordem (Baldoino Fonseca, UFAL)
fontes_catalogo: ufcg-massoni-slides, ufal-baldoino-slides-primeira-ordem
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL) e Prof. Tiago Massoni (UFCG), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

**Leis de De Morgan para quantificadores:** $\neg\forall x\,\varphi\equiv\exists x\,\neg\varphi$ e $\neg\exists x\,\varphi\equiv\forall x\,\neg\varphi$. A negação "atravessa" o quantificador e troca **para todo** por **existe** (e vice-versa). Os slides da UFCG mostram que $\forall x\neg P(x)\to\neg\exists x P(x)$ é válida.

**Como negar "todo aluno estuda":** formalize primeiro: $\forall x(A(x)\to E(x))$ ($A$: é aluno; $E$: estuda). Negue:
$\neg\forall x(A(x)\to E(x))\equiv\exists x\,\neg(A(x)\to E(x))\equiv\exists x(A(x)\land\neg E(x))$.
Em português: "**existe (pelo menos) um aluno que não estuda**". Erro comum: "nenhum aluno estuda" ($\forall x(A(x)\to\neg E(x))$) é mais forte que a negação e não é equivalente a ela.

**Outros casos:**
- Negar "algum aluno estuda", $\exists x(A(x)\land E(x))$: $\forall x(A(x)\to\neg E(x))$, "nenhum aluno estuda".
- Negar "nenhum cachorro é vampiro", $\neg\exists x(C(x)\land V(x))$: $\exists x(C(x)\land V(x))$, "existe um cachorro vampiro".
- Negar "todo programa tem um bug", $\forall x(P(x)\to\exists y\,B(y,x))$: $\exists x(P(x)\land\forall y\,\neg B(y,x))$, "algum programa não tem bug nenhum".

Também na lógica proposicional: negar uma conjunção dá disjunção das negações (De Morgan).

**Verificação:** em Python, a negação de "todo aluno estuda" e $\exists x(A(x)\land\neg E(x))$ coincidem em todos os modelos com universo de até 3 elementos, e "nenhum aluno estuda" difere delas em algum modelo.
