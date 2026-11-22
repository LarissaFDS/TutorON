---
id: clp-ponteiros-pendentes-vazamento-de-memoria-dangling-pointer
titulo: Os dois problemas de ponteiros: ponteiros pendentes (dangling pointers) e vazamento de memória (memory leak), como ocorrem e como as linguagens os evitam
assunto: clp-03-tipos
tipo: prova
questao: final 2012.2 Q2
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), final 2012.2 Q2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Ponteiro pendente (*dangling pointer*):** ponteiro que guarda o endereço de uma variável de heap **que já foi liberada** (ou de uma local cujo subprograma já retornou). Usá-lo lê lixo ou corrompe a memória, que pode já pertencer a outra variável. Como ocorre:
```c
int *p = malloc(sizeof *p), *q = p;
free(p);        /* q continua com o endereço liberado */
*q = 7;         /* comportamento indefinido */

int *f(void) { int local = 1; return &local; }  /* aponta para pilha morta */
```

**Vazamento de memória (*memory leak*, variável de heap perdida):** uma variável de heap **alocada que ficou sem nenhum ponteiro** para ela: não pode mais ser usada nem liberada. Como ocorre:
```c
int *p = malloc(100 * sizeof *p);
p = malloc(100 * sizeof *p);   /* o primeiro bloco ficou inacessível */
```
Repetido num laço, consome a memória até o programa falhar.

**Como as linguagens tratam:**
- pendentes: **lápides** (*tombstones*: o ponteiro aponta para uma célula intermediária, marcada nula ao liberar) e **fechaduras e chaves** (*locks-and-keys*); ou simplesmente **não ter desalocação explícita** (Java, Python);
- vazamentos: **coleta de lixo**, por **contagem de referências** (Python; não recolhe ciclos sozinha) ou **marcar e varrer** (*mark-and-sweep*).

Erro comum: trocar as definições. No pendente, o ponteiro **existe** e a memória não; no vazamento, a memória **existe** e o ponteiro não.

**Verificação:** `test_ponteiros_pendentes_e_vazamento` compila com gcc os dois exemplos (o compilador avisa sobre devolver o endereço de local) e simula em Python a contagem de referências: um ciclo de dois objetos só é recolhido pelo coletor de ciclos (`gc.collect`).
