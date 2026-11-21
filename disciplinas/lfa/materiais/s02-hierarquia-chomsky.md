---
id: lfa-hierarquia-de-chomsky
titulo: Hierarquia de Chomsky — tipos 0 a 3, gramática e reconhecedor de cada classe (regulares, livres de contexto, sensíveis ao contexto, recursivamente enumeráveis)
assunto: lfa-01-linguagens-chomsky
tipo: material_estudo
resolucao: nao
fonte: Apostila 01 (Profa. Simone Prado, UNESP), tabela linguagem × gramática × reconhecedor; ementa de ECOM014 no PPC de 2014
fontes_catalogo: unesp-prado-apostilas-tc
autoria: Profa. Simone das Graças Domingues Prado (UNESP), apostila usada pela turma; paráfrase e conferência da equipe TutorON
licenca: Não declarada; paráfrase, sem transcrição
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
A ementa de ECOM014 cita "tipos de linguagens e a hierarquia de Chomsky". Cada classe contém a de baixo e tem um gerador (gramática) e um reconhecedor (autômato):

| Tipo | Linguagens | Gramática (forma das produções) | Reconhecedor |
|---|---|---|---|
| 3 | regulares | regular: $A \to aB$ ou $A \to a$ (ou $A \to \varepsilon$) | autômato finito (AFD, AFN) |
| 2 | livres de contexto | $A \to \alpha$, um só não terminal à esquerda | autômato com pilha não determinístico |
| 1 | sensíveis ao contexto | $\alpha \to \beta$ com $|\alpha| \le |\beta|$ | autômato linearmente limitado |
| 0 | recursivamente enumeráveis | irrestrita | máquina de Turing |

As inclusões são próprias, e cada uma tem um exemplo que separa as classes:
- $a^n b^n$ é livre de contexto e não é regular (lema do bombeamento);
- $a^n b^n c^n$ é sensível ao contexto e não é livre de contexto;
- $A_{TM}$ (aceitação por máquina de Turing) é recursivamente enumerável e não é decidível.

As linguagens **decidíveis** (recursivas) ficam entre o tipo 1 e o tipo 0.

Como usar: para mostrar que uma linguagem está numa classe, basta exibir um gerador ou reconhecedor daquela classe. Para mostrar que **não** está, é preciso uma prova de impossibilidade: bombeamento para as regulares e as livres de contexto, diagonalização ou redução para a decidibilidade.

**Verificação:** a classe de cada exemplo é conferida nos blocos de bombeamento, de autômato com pilha e do problema da parada; nenhuma afirmação deste bloco depende de conta.
