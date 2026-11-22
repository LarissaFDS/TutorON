---
id: clp-vinculacao-memoria-tempo-de-vida-estaticas-pilha-heap
titulo: Quando ocorre a vinculação à memória e qual o tempo de vida de variáveis estáticas, dinâmicas de pilha e dinâmicas em memória livre (heap)
assunto: clp-02-nomes-vinculacao-escopo
tipo: prova
questao: AB1 2013.1 Q5
resolucao: sim
fonte: Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (IC-UFAL)
curso: Ciência da Computação (UFAL), Conceitos de Linguagens de Programação (CCOM027); provas de 2011.2 a 2013.1
fontes_catalogo: ufal-alcino-provas-clp
autoria: Questões do Prof. Alcino Dall'Igna Jr. (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Vinculação à memória** (alocação) liga a variável a uma célula; o **tempo de vida** vai da alocação à liberação.

| categoria | quando é vinculada | tempo de vida | exemplo |
|---|---|---|---|
| **estática** | **antes da execução** (carga do programa) | a **execução inteira** | `static int n;` em C, globais |
| **dinâmica de pilha** | quando a **declaração é elaborada**: na **chamada** do subprograma | da **chamada ao retorno** | variáveis locais de C e Java |
| **dinâmica em memória livre, explícita** | em **execução**, por comando explícito (`malloc`, `new`) | até a liberação explícita (`free`, `delete`) ou o coletor de lixo | objetos de Java, `malloc` em C |
| **dinâmica implícita** | em execução, **a cada atribuição** | enquanto o valor estiver em uso | variáveis de Python e JavaScript |

Vantagens e custos: estáticas são eficientes (endereço direto), mas não permitem recursão e não compartilham memória; as de pilha permitem recursão, mas custam a alocação a cada chamada e não guardam histórico; as de heap dão estruturas dinâmicas, mas são mais lentas e trazem ponteiros pendentes e vazamentos.

Exemplo em C:
```c
int conta(void) {
    static int n = 0;   /* estática: guarda o valor entre chamadas */
    int k = 0;          /* de pilha: nasce em cada chamada */
    n++; k++;
    return n * 10 + k;
}
```
Três chamadas devolvem 11, 21 e 31: `n` sobrevive entre as chamadas, `k` não.

**Verificação:** `test_tempo_de_vida_em_c` compila esse código com gcc e confere 11, 21, 31, e que um `malloc` feito numa função continua válido depois do retorno dela, até o `free`.
