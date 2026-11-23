---
id: ia-encadeamento-para-frente-e-para-tras-sistemas-de-producao-regras-se-entao-base-de-fatos
titulo: Encadeamento para frente (guiado por dados) e para trás (guiado por objetivos) em sistemas de regras se-então; exemplo da Lista 1 com as regras R1 a R5 e o fato S
assunto: ia-03-conhecimento-e-raciocinio
tipo: lista
questao: Lista 1 (2020.2), questões de encadeamento para frente e para trás
resolucao: sim
fonte: Listas 1 e 2 de Inteligência Artificial (IC-UFAL), 2020.2, Prof. Evandro de Barros Costa
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-ia-listas-2020-2
autoria: Questões do Prof. Evandro de Barros Costa (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), Lista 1 (2020.2), questões de encadeamento para frente e para trás (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Base de regras:** R1: $P \land Q \to R$; R2: $S \to T$; R3: $T \to P$; R4: $S \to V$; R5: $V \to Q$. Fato inicial: $S$. Objetivo: provar $R$.

**Encadeamento para frente** (guiado por dados): dispara toda regra cujas premissas estão na base de fatos, acrescenta a conclusão e repete até achar o objetivo ou não haver fato novo.
1. fatos {S}: disparam R2 e R4, e ficam {S, T, V};
2. disparam R3 e R5: {S, T, V, P, Q};
3. dispara R1: **R** encontrado.

**Encadeamento para trás** (guiado por objetivos): parte de $R$, procura regras que o concluam e transforma as premissas em subobjetivos.
- $R$? por R1, provar $P$ e $Q$;
- $P$? por R3, provar $T$; $T$? por R2, provar $S$: é fato;
- $Q$? por R5, provar $V$; $V$? por R4, provar $S$: é fato;
- logo $P$, $Q$ e $R$ são verdadeiros.

**Quando usar:** para frente com poucos fatos e muitos objetivos possíveis (monitoramento, configuração); para trás com um objetivo definido (diagnóstico, como no MYCIN). Com cláusulas de Horn os dois são corretos e completos.

Na implementação, guarde os fatos num conjunto e repita sobre as regras **até nada mudar**, em vez de um número fixo de iterações com uma variável para cada símbolo.

```python
REGRAS = [({"P", "Q"}, "R"), ({"S"}, "T"), ({"T"}, "P"), ({"S"}, "V"), ({"V"}, "Q")]
def para_frente(fatos):
    fatos = set(fatos)
    while True:
        novos = {c for prem, c in REGRAS if prem <= fatos} - fatos
        if not novos:
            return fatos
        fatos |= novos
```

**Verificação:** `test_encadeamento_frente_e_tras` roda os dois encadeamentos e confere que $R$ é provado a partir de $S$ e não é provado sem $S$.
