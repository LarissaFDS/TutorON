---
id: pcom-lista4-exposicao-60hz
titulo: Lista 4: exposição a campo elétrico de linha de 69 kV, 60 Hz e 6ª harmônica (360 Hz); limites 500/f (ocupacional) e 250/f (público) em kV/m; conformidade e soma das frequências
assunto: pcom-08-exposicao-campos
tipo: lista
resolucao: sim
fonte: Anotações "Lista 4" (22 out. 2026), p. 1–2 (questão 1, enunciado parafraseado)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2, icnirp-1998-diretrizes, aneel-ren-398-2010
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: pendente_professor
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: pendente de confirmação do professor.

**Enunciado (parafraseado):** a 1 m sob uma linha de 69 kV mediu-se $E_1 = 5{,}5$ kV/m em 60 Hz e $E_6 = 0{,}7$ kV/m na 6ª harmônica ($6\cdot 60 = 360$ Hz). Verificar a conformidade com a tabela de limites.

**Limites usados** ($f$ em Hz, resultado em kV/m; os mesmos números da ICNIRP 1998 e, para 60 Hz, da ANEEL): ocupacional $E_L = 500/f$; público em geral $E_L = 250/f$.

| | 60 Hz | 360 Hz |
|---|---|---|
| limite ocupacional | 8,33 kV/m | 1,39 kV/m |
| limite público | 4,17 kV/m | 0,694 kV/m |

- Ocupacional: $5{,}5 < 8{,}33$ e $0{,}7 < 1{,}39$: cada frequência, sozinha, está abaixo do limite.
- Público: $5{,}5 > 4{,}17$ e $0{,}7 > 0{,}694$: **não há conformidade** nas duas.

Correções: $250/60 = 4{,}17$ (a anotação escreve 4,16). E a nota "valor muito próximo do limite, por segurança colocar conformidade" está invertida: acima do limite, mesmo por pouco, é **não conforme**; a margem de segurança iria no sentido contrário.

**Soma das frequências (ICNIRP 1998):** com várias frequências exige-se $\sum_i E_i/E_{L,i} \le 1$. Ocupacional: $5{,}5/8{,}33 + 0{,}7/1{,}39 = 0{,}66 + 0{,}50 = 1{,}16 > 1$; com a soma, nem a exposição ocupacional fica conforme. Público: 2,33.

Pendente: confirmar com o professor a tabela da lista e se a soma é exigida. A Lista 4 foi classificada nesta disciplina pela sequência das listas (Listas 1 a 3 são de Comunicação), sem confirmação.

**Verificação:** as razões foram recalculadas com `fractions`: $250/60 = 4{,}1\overline{6}$, $250/360 = 0{,}69\overline{4}$ e as somas 1,164 e 2,328.
