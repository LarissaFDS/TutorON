---
id: controle-anot-erro-regime-exemplo
titulo: Exemplo de erro ao degrau com realimentação não unitária: G = 2/(s+1), H = (s+2)/(s+3); Gmf = 2(s+3)/(s²+6s+7), ess = 1/7
assunto: controle-06-erro-regime
tipo: resolucao
resolucao: sim
fonte: Anotações "Resposta em Regime permanente" (20 out. 2026), p. 2
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Sistemas de Controle 2026.2; professor não identificado nas anotações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de livros e de provas parafraseados; fotos de quadro, de livro e figuras coladas não foram copiadas
fontes_catalogo: ufal-controle-anotacoes-otavio-2026-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: validada
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: validada.

**Enunciado (paráfrase):** erro de rastreamento ao degrau para ramo direto $G = \frac{2}{s + 1}$ e realimentação **negativa** com $H = \frac{s + 2}{s + 3}$.

**Malha fechada:**
$$G_{mf} = \frac{G}{1 + GH} = \frac{2(s + 3)}{(s + 1)(s + 3) + 2(s + 2)} = \frac{2(s + 3)}{s^2 + 6s + 7}.$$ Polos $-3 \pm \sqrt2$: estável, pode usar o TVF.

**Erro (com $e = r - y$, não $r - Hy$):**
$$e_{ss} = \lim_{s\to0}s\Big[1 - \frac{2(s + 3)}{s^2 + 6s + 7}\Big]\frac1s = 1 - \frac67 = \frac17.$$

Atenção: com $H \ne 1$, as fórmulas de $K_p$, $K_v$ e do tipo para realimentação unitária **não** se aplicam diretamente; use $1 - G_{mf}$.

**Verificação:** `scipy.signal.step` de $G_{mf}$ tende a $6/7 = 0{,}857$.
