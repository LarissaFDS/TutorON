---
id: clp-compatibilidade-de-tipos-por-nome-por-estrutura-em-c
titulo: Compatibilidade de tipos por nome × por estrutura e como C implementa compatibilidade de tipos (struct por nome, typedef, arrays e ponteiros por estrutura)
assunto: clp-03-tipos
tipo: prova
questao: AB1 2013.1 Q8; final 2012.2 Q1
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q8; final 2012.2 Q1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por nome:** duas variáveis têm tipos compatíveis só se foram declaradas **na mesma declaração** ou com o **mesmo nome de tipo**. Fácil de implementar e seguro, mas restritivo: um subintervalo de inteiros declarado com outro nome não é compatível com `Integer`, e um parâmetro precisa usar exatamente o nome de tipo da declaração.

**Por estrutura:** os tipos são compatíveis se têm **estruturas idênticas** (mesmos componentes, na mesma ordem e com os mesmos tipos). É mais flexível, mas difícil de implementar (comparar estruturas recursivas) e **não distingue** tipos de mesma forma e significado diferente: `celsius` e `fahrenheit`, ambos `float`, viram compatíveis.

**Como C faz (Q8c):** usa **estrutura** para quase tudo e **nome** para `struct`, `union` e `enum`:
- `struct` e `union`: cada declaração cria um **tipo novo**. Duas `struct` com os mesmos campos e nomes diferentes **não** são compatíveis (atribuir uma à outra é erro de compilação);
- `typedef` **não cria tipo novo**, só um apelido: `typedef float celsius;` é compatível com `float`;
- arrays e ponteiros: compatibilidade por estrutura do tipo dos elementos.

(Exceção técnica: em C, estruturas declaradas em **arquivos diferentes** com a mesma marca e os mesmos campos são compatíveis; dentro de um arquivo, vale a regra por nome.)

**Verificação:** `test_compatibilidade_em_c` compila com gcc: atribuir uma `struct a` a uma `struct b` de campos iguais dá erro (*incompatible types*); `typedef float celsius` aceita receber `float` sem aviso.
