---
id: pln-pre-processamento-minusculas-pontuacao-numeros-tokenizacao-bag-of-words-frequentes
titulo: Pré-processamento de textos: distribuição de comprimentos, remover palavras com números, minúsculas, remover pontuação, tokenizar, vocabulário de n tokens e vetor de contagens (bag-of-words), palavras mais frequentes
assunto: pln-01-regex-e-preprocessamento
tipo: lista
questao: Lista 2, questões 1 e 2
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 2, questões 1 e 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Comprimento dos textos:** `len(texto)` em caracteres para cada documento; um **histograma** mostra a distribuição (textos muito curtos ou muito longos podem ser ruído ou precisar de tratamento).

**Passos, na ordem pedida:**
1. remover **palavras com números** (`\w*\d\w*`);
2. **minúsculas** (`str.lower`), para "Casa" e "casa" serem o mesmo token;
3. remover **pontuação** (`re.sub(r"[^\w\s]", " ", t)` ou `str.translate`);
4. **tokenizar** (`split` ou um tokenizador) e montar o **vocabulário**: os $n$ tokens distintos da base, cada um com um índice;
5. cada texto vira um **vetor de dimensão $n$** com a contagem de cada token (**bag-of-words**: perde a ordem das palavras).

Exemplo com três textos: "O gato subiu.", "O cão e o gato!", "Em 2021 o cão dormiu."
- depois dos passos: `o gato subiu` / `o cão e o gato` / `em o cão dormiu`;
- vocabulário (ordem alfabética): cão, dormiu, e, em, gato, o, subiu ($n = 7$);
- vetor do 2º texto: $(1, 0, 1, 0, 1, 2, 0)$;
- mais frequentes na base: **o** (4), depois **gato** e **cão** (2 cada).

As mais frequentes costumam ser **palavras vazias** (artigos, preposições): por isso o próximo passo remove *stopwords*.

```python
import re
from sklearn.feature_extraction.text import CountVectorizer

def limpa(t):
    t = re.sub(r"\w*\d\w*", " ", t).lower()
    return re.sub(r"[^\w\s]", " ", t)

cv = CountVectorizer(preprocessor=limpa, token_pattern=r"(?u)\b\w+\b")
x = cv.fit_transform(textos)          # matriz documentos × vocabulário
freq = x.sum(axis=0).A1
```

**Verificação:** `test_preprocessamento_bow` roda o exemplo à mão e com `CountVectorizer`: mesmo vocabulário de 7 tokens, o vetor do 2º texto e "o" como palavra mais frequente.
