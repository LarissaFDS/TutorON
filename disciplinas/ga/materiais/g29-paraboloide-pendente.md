---
id: ga-paraboloide-secao
titulo: Paraboloide de vértice (3, −1, 0) cuja seção perpendicular ao eixo, a duas unidades do vértice, é uma elipse de eixos 5 e 8
assunto: ga-12-quadricas-superficies
tipo: prova
questao: 3a
semestre: 2017.1
resolucao: sim
fonte: Fotos de provas de Geometria Analítica (ECOM005), UFAL | 4ª Avaliação (12.05.2017), Q3a
fontes_catalogo: ufal-ga-provas-2017
autoria: Enunciado: Instituto de Matemática da UFAL (professor não impresso na prova), parafraseado pela equipe TutorON; resolução da equipe TutorON, redigida com auxílio de IA e conferida por código
licenca: Não declarada (prova da disciplina); as fotos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco traz o enunciado parafraseado e os dados, não a transcrição literal
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: pendente_professor
revisao_humana: pendente
---
Questão de prova (enunciado parafraseado). Status da resolução: pendente de confirmação do professor (o enunciado não diz a direção do eixo nem se "eixos" são os eixos inteiros ou os semieixos; a resolução da equipe TutorON, conferida com SymPy, vale para a leitura abaixo).

Dados: vértice V(3, −1, 0); a seção por um plano perpendicular ao eixo, a 2 unidades de V, é uma elipse de eixos 5 e 8.

**Leitura adotada.** Eixo do paraboloide paralelo a Oz, abrindo para z > 0; 5 e 8 são os comprimentos dos eixos inteiros (semieixos 5/2 e 4).

**Resolução.** Paraboloide elíptico de vértice V: $\dfrac{(x-3)^2}{\alpha} + \dfrac{(y+1)^2}{\beta} = z$. Em z = 2, o traço é $\dfrac{(x-3)^2}{2\alpha} + \dfrac{(y+1)^2}{2\beta} = 1$, de semieixos $\sqrt{2\alpha}$ e $\sqrt{2\beta}$.
- $2\alpha = \tfrac{25}{4}$, então $\alpha = \tfrac{25}{8}$;
- $2\beta = 16$, então $\beta = 8$.
Equação: $\dfrac{(x-3)^2}{25/8} + \dfrac{(y+1)^2}{8} = z$.

Outras leituras mudam a resposta: se 5 e 8 forem semieixos, $\alpha = \tfrac{25}{2}$ e $\beta = 32$; se o paraboloide abrir para z < 0, troque z por −z; se o eixo for paralelo a Ox ou a Oy, troque os papéis das variáveis. Diga ao aluno qual leitura está usando.

**Verificação:** em z = 2, o ponto $(3 + \tfrac52, -1, 2)$ dá $\tfrac{25/4}{25/8} = 2$, e $(3, 3, 2)$ dá $\tfrac{16}{8} = 2$; em z = 0, só o vértice satisfaz a equação.
