---
id: clp-escopo-estatico-dinamico-ambiente-de-referencia
titulo: Escopo de uma variável e ambiente de referência de um comando; escopo estático × dinâmico com exemplo
assunto: clp-02-nomes-vinculacao-escopo
tipo: prova
questao: AB1 2013.1 Q6
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
Provas de Conceitos de Linguagens de Programação do Prof. Alcino Dall'Igna Jr. (UFAL), AB1 2013.1 Q6 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Escopo** de uma variável: o conjunto de **comandos em que ela é visível**, isto é, pode ser referenciada.

**Ambiente de referência** de um comando: o conjunto de **todas as variáveis visíveis** naquele comando. Em escopo estático, são as locais mais as de todos os escopos que o envolvem no texto, menos as ocultadas por nomes iguais.

**Escopo estático (léxico):** o nome se resolve pelo **texto do programa**, procurando no bloco atual e depois nos que o envolvem (C, Java, Python, Haskell). **Escopo dinâmico:** se resolve pela **sequência de chamadas** em execução, procurando no chamador, depois no chamador dele (Lisp antigo, Perl com `local`, shell).

```python
x = "global"

def mostra():
    return x          # qual x?

def chama():
    x = "local de chama"
    return mostra()
```
- estático: `chama()` devolve `"global"` (`mostra` foi escrita no nível global);
- dinâmico: devolveria `"local de chama"` (quem chamou `mostra` foi `chama`).

Prós e contras: o estático é legível e verificável na compilação; o dinâmico dá flexibilidade, mas os nomes dependem do caminho de execução, o que prejudica a legibilidade e a confiabilidade.

Observação: escopo e **tempo de vida** são diferentes. Uma `static` local de C tem escopo da função, mas vive o programa todo.

**Verificação:** `test_escopo_estatico_e_dinamico` roda o exemplo em Python (resultado `"global"`) e um interpretador mínimo com pilha de ambientes para o caso dinâmico (resultado `"local de chama"`).
