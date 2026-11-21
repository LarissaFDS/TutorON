---
id: logica-model-checking-ltl
titulo: Verificação de sistemas: provas versus model checking, sistemas de transição e lógica temporal LTL
assunto: logica-13-model-checking-alloy
tipo: material_estudo
resolucao: sim
fonte: Slides Model Checking (Tiago Massoni, UFCG), parte própria dos slides; as páginas copiadas do livro de Huth e Ryan não foram usadas
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

**Por que verificar:** sistemas de missão crítica, economicamente críticos ou de segurança; falhas de concorrência são difíceis de achar com testes.

Uma técnica de verificação tem três partes: **como modelar** o sistema, **uma linguagem para especificar** propriedades e **um método** de verificação.
- **Baseada em provas:** o sistema é um conjunto de fórmulas $\Gamma$, a especificação é $\varphi$; verificar é provar $\Gamma\vdash\varphi$.
- **Baseada em modelos (model checking):** o sistema é um modelo $M$, a especificação é $\varphi$; verificar é **calcular** se $M\models\varphi$, de forma automática.

**Sistema de transição** $M=\langle S,\to,L\rangle$: estados $S$, transições ($\to$, todo estado tem ao menos um sucessor) e rótulos $L(s)$ com os átomos verdadeiros em $s$. Um **caminho** é uma sequência infinita $s_1\to s_2\to\cdots$.

**LTL** (lógica temporal linear): fórmulas valem num caminho. $X\varphi$: no próximo estado; $G\varphi$: sempre (globalmente); $F\varphi$: em algum momento futuro; $\varphi\,U\,\psi$: $\varphi$ vale até $\psi$ valer (e $\psi$ vale um dia). $M,s\models\varphi$ se **todo** caminho a partir de $s$ satisfaz $\varphi$.

**Exemplo próprio:** semáforo com estados $s_0$ {verde}, $s_1$ {amarelo}, $s_2$ {vermelho}, transições $s_0\to s_1\to s_2\to s_0$. Vale $G(\mathit{amarelo}\to X\,\mathit{vermelho})$ e $G\,F\,\mathit{verde}$; não vale $G\,\mathit{verde}$.

Propriedade típica de máquina de bebidas: "sempre que o botão é apertado, em algum momento sai café ou chá": $G(\mathit{botao}\to F(\mathit{cafe}\lor\mathit{cha}))$.

**Verificação:** as três fórmulas do semáforo foram avaliadas em Python no único caminho (periódico) a partir de $s_0$.
