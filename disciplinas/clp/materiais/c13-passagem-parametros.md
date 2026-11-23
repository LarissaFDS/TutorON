---
id: clp-passagem-de-parametros-modelos-semanticos-valor-resultado-referencia
titulo: Modelos semânticos de passagem de parâmetros (entrada, saída, entrada e saída), implementações (valor, resultado, valor-resultado, referência, nome) e diferença entre valor-resultado e referência
assunto: clp-06-subprogramas
tipo: prova
questao: AB2 2011.2 Q9-Q10
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB2 2011.2 Q9-Q10 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Modelos semânticos (Q9a):**
- **modo entrada** (*in*): o parâmetro formal **recebe** dados do real;
- **modo saída** (*out*): o formal **transmite** dados para o real;
- **modo entrada e saída** (*inout*): faz os dois.

**Implementações:** **por valor** (entrada; cópia do valor); **por resultado** (saída; o valor do formal é copiado para o real no retorno); **por valor-resultado** (entrada e saída por **cópia**: copia na chamada e copia de volta no retorno); **por referência** (entrada e saída por **caminho de acesso**: o formal é um apelido do real); **por nome** (substituição textual, ALGOL 60).

**Exemplo de linguagem (Q9b):** **Ada** declara os três modos com `in`, `out` e `in out`. C só tem passagem por valor e simula a saída com ponteiros; C++ tem valor e referência (`int&`); Java passa tudo por valor (o valor de uma referência a objeto).

**Valor-resultado × referência (Q10):** os dois são de entrada e saída. A diferença: o valor-resultado trabalha numa **cópia local** e só atualiza o real **no retorno**; a referência altera o real **na hora**. O resultado só difere quando há **apelidos**:
```text
global = 1
sub f(x): x = x + 10; global = global * 2
f(global)
```
- por referência: `x` é `global`: 1 + 10 = 11, depois 11 × 2 = **22**;
- por valor-resultado: `x` local = 11, `global` vira 2 durante a execução, e no retorno a cópia sobrescreve: **11**.
A referência é mais eficiente (não copia), mas cria apelidos e acesso indireto; a cópia isola, mas custa memória e tempo com objetos grandes.

**Verificação:** `test_passagem_de_parametros` simula os dois modos em Python com o exemplo (22 e 11), e compila em C a versão por ponteiro (referência), que imprime 22.
