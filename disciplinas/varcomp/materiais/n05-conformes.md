---
id: varcomp-nota-ia-conformes
titulo: Nota — representação conforme: preservação de ângulos onde f′ ≠ 0, transformações de Möbius, w = (z − i)/(z + i)
assunto: varcomp-09-representacao-conforme
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON escrita com IA (não é material do professor)
autoria: Equipe TutorON (rascunho gerado por IA); revisão humana pendente
licenca: Texto próprio da equipe
publicacao_transcricao: não se aplica
fontes_catalogo: mit-ocw-1804-2018,beck-first-course-complex-analysis
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: conferida_por_codigo
revisao_humana: pendente
---
Rascunho escrito por IA, aguardando revisão humana; fora da busca. Contas conferidas com SymPy em `tests_acervo/test_disciplina_varcomp.py`.

Uma função analítica com $f'(z_0) \neq 0$ é **conforme** em $z_0$: preserva os ângulos entre curvas (valor e sentido). Localmente ela gira de $\arg f'(z_0)$ e escala por $|f'(z_0)|$. Onde $f' = 0$ os ângulos não se preservam: $w = z^2$ dobra os ângulos em $z = 0$.

**Transformações de Möbius:** $w = \frac{az + b}{cz + d}$ com $ad - bc \neq 0$. Levam retas e circunferências em retas e circunferências e ficam determinadas por três pontos.

Exemplo: $w = \frac{z - i}{z + i}$ leva o semiplano superior ($\operatorname{Im} z > 0$) no disco unitário $|w| < 1$: para z no semiplano superior, z está mais perto de i que de −i, então $|z - i| < |z + i|$. O eixo real vai na circunferência $|w| = 1$, e $z = i$ vai no centro $w = 0$.

**Verificação:** $z = 0 \mapsto -1$, $z = 1 \mapsto -i$, $z = i \mapsto 0$; $|w(x)| = 1$ para x real (SymPy).
