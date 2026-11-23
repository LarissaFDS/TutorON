---
id: ihc-metodos-centrados-no-usuario-regra-de-ouro-entrevista-etnografia-teste-de-utilizacao-feedback-do-cliente
titulo: Métodos centrados no usuário: regra de ouro (conheça seus usuários), avaliação das necessidades (entrevista, métodos etnográficos), teste de utilização com protótipos, feedback do cliente após a distribuição; o antigo método guru
assunto: ihc-01-design-centrado-no-usuario
tipo: exercicio
questao: slides 12 a 18
resolucao: sim
fonte: Slides "A Nova Informática: Design centrado no Usuário" da disciplina (base: Shneiderman, 2006; Nielsen, 1993)
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-slides-dcu,shneiderman-laptop-leonardo
autoria: Slides da disciplina (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), slides 12 a 18 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Antes: o método guru.** Interfaces obscuras feitas pelo programador para uso próprio, e usuários iniciantes dependentes de especialistas. O exemplo dos slides é `grep -v ^$`: poderoso, mas ninguém adivinha que isso apaga linhas em branco.

**Para que serve o computador depende de quem usa:** analista, dona de casa, aposentado, estudante de direito, médico, criança. A dificuldade do projetista é se adaptar ao **baixo entusiasmo tecnológico** e à **baixa tolerância à frustração** desses usuários.

**Regra de ouro** (Nielsen, 1993; Shneiderman, 1998): *conheça seus usuários e o que eles estão fazendo*. Fácil de dizer, difícil de fazer.

**Método 1 — avaliar as necessidades** (antes de projetar):
- **entrevistas**: o que o usuário tenta fazer, com que frequência, onde trava;
- **métodos etnográficos**: observar o uso real, com gravação e anotações, no ambiente do usuário;
- **teorias antropológicas** orientam a observação e a interpretação. Exemplo citado: Laurel (2001), sobre como adolescentes usam o computador.

**Método 2 — teste de utilização** (durante o projeto): os usuários fazem **tarefas reais** com **protótipos** enquanto o analista observa onde têm problemas. Deixe claro ao participante que **quem está sendo avaliado é o software, não ele**.

**Método 3 — feedback do cliente** (depois da distribuição): dados automáticos de uso enviados pela internet, com consentimento do usuário:
- quantos usam;
- com que frequência;
- que recursos usam e quais não usam;
- relatórios de problemas.

**Como escolher:** necessidades no início, teste com protótipo a cada versão, *feedback* depois do lançamento. Os três se completam, e o ciclo se repete.

**Verificação:** `test_metodos_por_fase` confere a tabela método × fase do projeto (antes, durante, depois) usada acima.
