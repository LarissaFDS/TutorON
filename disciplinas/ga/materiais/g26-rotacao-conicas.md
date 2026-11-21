---
id: ga-rotacao-conicas
titulo: Rotação de eixos (mudança de coordenadas): esboçar y²/4 − x²/9 = 1 rotacionada de 30° e a parábola 2y − x² = 2 rotacionada de 45°, rotacionando focos, vértices e assíntotas
assunto: ga-11-rotacao-coordenadas
tipo: prova
questao: 4b; 4b
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 2ª Avaliação (11.03.2017), Q4b; Reavaliação AB1 (24.05.2017), Q4b
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questões de prova (enunciados parafraseados). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com SymPy).

**Rotação de um ponto** pelo ângulo θ (anti-horário) em torno da origem: $(x, y) \mapsto (x\cos\theta - y\operatorname{sen}\theta,\ x\operatorname{sen}\theta + y\cos\theta)$. Para a equação da curva girada, substitua (x, y) pela rotação de $-\theta$ do ponto novo. Rotações preservam distâncias: a, b, c e p não mudam.

**Hipérbole $\tfrac{y^2}{4} - \tfrac{x^2}{9} = 1$ girada de 30°.** Antes: vértices $(0, \pm2)$, focos $(0, \pm\sqrt{13})$, assíntotas $y = \pm\tfrac23x$. Depois de girar:
- vértices $\pm(-1, \sqrt3)$;
- focos $\pm\left(-\tfrac{\sqrt{13}}{2}, \tfrac{\sqrt{39}}{2}\right)$;
- assíntotas: retas pela origem e pelos pontos girados de (3, 2) e (3, −2); (3, 2) vai para $\left(\tfrac{3\sqrt3}{2} - 1,\ \tfrac32 + \sqrt3\right)$.

**Parábola $2y - x^2 = 2$ girada de 45°.** Forma reduzida $x^2 = 2(y - 1)$: vértice (0, 1), $p = \tfrac12$, foco $(0, \tfrac32)$, diretriz $y = \tfrac12$, eixo $x = 0$. Depois de girar:
- vértice $\left(-\tfrac{\sqrt2}{2}, \tfrac{\sqrt2}{2}\right)$, foco $\left(-\tfrac{3\sqrt2}{4}, \tfrac{3\sqrt2}{4}\right)$;
- eixo: a reta $y = -x$; diretriz: $-x + y = \tfrac{\sqrt2}{2}$;
- equação: $x^2 + 2xy + y^2 + 2\sqrt2\,x - 2\sqrt2\,y + 4 = 0$. O termo $xy$ aparece, e $B^2 - 4AC = 4 - 4 = 0$ confirma que é parábola.

**Verificação:** o vértice girado satisfaz a equação nova ($0 - 2 - 2 + 4 = 0$); a distância do foco girado ao vértice girado continua $\tfrac12$; $\|(-1, \sqrt3)\| = 2$.
