---
id: pln-spacy-etiquetas-pos-entidades-nomeadas-pessoa-lugar-contar-uma-vez-por-documento
titulo: spaCy: etiquetas gramaticais (POS) de cada token e gráfico de frequências, entidades nomeadas de pessoa e lugar, pessoas mais frequentes contando cada entidade uma vez por documento
assunto: pln-04-redes-neurais-e-spacy
tipo: lista
questao: Lista 6, questão 3
resolucao: sim
fonte: Listas de exercícios 1 a 6 de Processamento de Linguagem Natural, Prof. Thales Vieira (IC-UFAL), 2021.1
curso: Ciência da Computação (UFAL), eletiva Processamento de Linguagem Natural; turma 2021.1 (listas de out/2021 a fev/2022)
fontes_catalogo: ufal-vieira-listas-pln,scikit-learn-pln
autoria: Questões do Prof. Thales Vieira (IC-UFAL); explicação e exemplo parecido da equipe TutorON
licenca: Não declarada (listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 6, questão 3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**spaCy:** carregue o modelo do idioma (`pt_core_news_sm` para português, `en_core_web_sm` para inglês) e processe: `doc = nlp(texto)`.
- **POS:** `token.pos_` dá a etiqueta universal (NOUN, VERB, ADJ, PROPN, ADP...). Conte com `collections.Counter` e plote barras ordenadas.
- **Entidades:** `doc.ents`; cada entidade tem `ent.text` e `ent.label_`. No modelo em português, pessoa é **PER** e lugar **LOC**; no inglês, **PERSON** e **GPE**/**LOC**. Confira os rótulos do seu modelo com `nlp.get_pipe("ner").labels`.

**Contar uma vez por documento:** para cada documento, monte o **conjunto** de pessoas (`set`) e só então some ao contador global: uma pessoa citada 5 vezes num texto conta 1. Isso mede **em quantos documentos** ela aparece.

Normalize antes de contar ("Lula" e "Luiz Inácio Lula da Silva" são a mesma pessoa? decida e explique); entidades erradas do modelo (um lugar marcado como pessoa) devem ser comentadas, não escondidas.

```python
from collections import Counter

pessoas = Counter()
for doc in nlp.pipe(textos):
    pessoas.update({e.text for e in doc.ents if e.label_ in ("PER", "PERSON")})
print(pessoas.most_common(10))
```

**Verificação:** `test_contagem_uma_vez_por_documento` usa entidades já anotadas (sem o modelo do spaCy, que não está instalado nos testes) e confere que uma pessoa repetida no mesmo documento conta uma vez, e que a ordem das mais frequentes muda em relação à contagem simples.
