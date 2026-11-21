---
id: lfa-mt-mesmo-numero-de-0-e-1
titulo: Máquina de Turing no nível de implementação — decidir {w | w tem o mesmo número de 0s e 1s}, marcar pares com X, tabela de transição e simulação
assunto: lfa-06-maquinas-de-turing
tipo: lista
questao: Máquina de Turing, questão 2 (a)
resolucao: sim
fonte: Atividade teórica de Teoria da Computação 2015.1 (Prof. Thyago, UFAL), Máquina de Turing, questão 2 (a)
fontes_catalogo: ufal-thyago-atividade-2015-1
autoria: Atividade do Prof. Thyago Tenório Martins de Oliveira (UFAL); resolução da equipe TutorON
licenca: Não declarada (atividade); paráfrase
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Atividade 2015.1, MT, questão 2(a): decidir $L = \{w \in \{0,1\}^* \mid w$ tem tantos 0 quanto 1$\}$. Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Descrição de implementação** (o que a questão pede):
1. Marque o início da fita com $\triangleright$, deslocando a entrada uma célula para a direita, para a máquina saber onde voltar.
2. Procure, da esquerda para a direita, o primeiro símbolo não marcado (0 ou 1). Se só houver X até o branco, **aceite**.
3. Marque-o com X e procure à direita um símbolo **oposto** não marcado. Se achar, marque com X; se chegar ao branco, **rejeite**.
4. Volte até $\triangleright$ e repita o passo 2.

**Tabela do laço principal** (estados de deslocamento omitidos; X = marcado, ⊔ = branco):

| Estado | Lê | Escreve, move, vai para |
|---|---|---|
| $q_0$ | X | X, D, $q_0$ |
| $q_0$ | 0 | X, D, $a_1$ (procura um 1) |
| $q_0$ | 1 | X, D, $a_0$ (procura um 0) |
| $q_0$ | ⊔ | aceita |
| $a_1$ | 0 ou X | igual, D, $a_1$ |
| $a_1$ | 1 | X, E, volta |
| $a_1$ | ⊔ | rejeita |
| $a_0$ | 1 ou X | igual, D, $a_0$ |
| $a_0$ | 0 | X, E, volta |
| $a_0$ | ⊔ | rejeita |
| volta | 0, 1 ou X | igual, E, volta |
| volta | $\triangleright$ | $\triangleright$, D, $q_0$ |

Traço resumido de $0110$: os pares marcados são (0, 1), depois (1, 0). Só sobram X, então a máquina aceita. Para $001$: marca (0, 1); o segundo 0 não acha 1, então rejeita.

A máquina **decide** $L$ (sempre para): cada volta marca 2 símbolos, então são no máximo $|w|/2$ voltas, cada uma com $O(|w|)$ passos, e o total é $O(|w|^2)$.

As questões 2(b) e 2(c) usam a mesma ideia: para cada 1, marque dois 0. A (c) é o complemento da (b): basta trocar aceita e rejeita, o que só vale porque a máquina sempre para.

**Verificação:** a tabela completa (25 transições, com o deslocamento inicial) foi simulada em `tests_acervo/lfa_verif.py` para todas as cadeias até comprimento 10, sempre parando, e aceita exatamente as que têm tantos 0 quanto 1.
