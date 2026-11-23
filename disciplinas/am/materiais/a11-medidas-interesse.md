---
id: am-medidas-de-interesse-lift-dependencia-entre-itens-regras-ilusorias
titulo: Medidas de interesse de regras de associação: limitações do modelo suporte/confiança, dependência entre itens, lift (interesse) e regras ilusórias
assunto: am-03-agrupamento-e-associacao
tipo: prova
questao: slides 07b (medidas de interesse)
resolucao: sim
fonte: Provas de Aprendizagem de Máquina do Prof. Aydano Machado (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Aprendizagem de Máquina (COMP390); provas AB1 e AB2 (uma delas de 2021.1)
fontes_catalogo: ufal-aydano-slides-am
autoria: Questões do Prof. Aydano Machado (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Aprendizagem de Máquina, Prof. Aydano Machado (UFAL), slides 07b (medidas de interesse) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Problema do modelo suporte/confiança:** gera **regras demais** (nos slides, uma base de compras de 422 famílias com SupMin 3% e ConfMin 60% gerou 8 469 regras de 2 itens), muitas **redundantes** ou **ilusórias**. Confiança alta não basta quando o consequente já é muito frequente.

**Comparar a confiança com o suporte do consequente:**
- $\text{conf}(A \Rightarrow B) = \text{sup}(B)$: $A$ e $B$ são **independentes**; a regra não informa nada;
- $\text{conf}(A \Rightarrow B) < \text{sup}(B)$: **dependência negativa**: quem compra $A$ tem **menos** chance de comprar $B$;
- $\text{conf}(A \Rightarrow B) > \text{sup}(B)$: **dependência positiva**: a regra é interessante.

**Lift** (interesse):
$$\text{lift}(A \Rightarrow B) = \frac{\text{conf}(A \Rightarrow B)}{\text{sup}(B)} = \frac{\text{sup}(A \cup B)}{\text{sup}(A)\,\text{sup}(B)}$$
Em palavras: quantas vezes a chance de $B$ aumenta quando $A$ está presente. Lift 1, independência; menor que 1, dependência negativa; maior que 1, positiva.

**Exemplos dos slides** (suporte de $A$, de $B$, da regra e confiança):
- filé ⇒ açúcar: 8,77%, 86,49%, 7,58%, 86,49%: lift $\approx 1{,}00$, **independentes**, apesar da confiança alta;
- banana nanica ⇒ banana prata: 12,09%, 76,07%, 7,35%, 60,78%: lift $\approx 0{,}80$, **negativa**;
- milho em conserva ⇒ ervilha em conserva: 32,94%, 37,91%, 27,01%, 82,01%: lift $\approx 2{,}16$, **positiva**.

Outras medidas: convicção, alavancagem (*leverage*) $= \text{sup}(A \cup B) - \text{sup}(A)\text{sup}(B)$.

**Verificação:** `test_lift_dos_exemplos` recalcula os três lifts com os números dos slides, confere que a confiança é a razão dos suportes (com tolerância de arredondamento) e classifica cada regra como independente, negativa ou positiva.
