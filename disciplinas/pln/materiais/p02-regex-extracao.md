---
id: pln-expressoes-regulares-extrair-campos-grupos-nomeados-endereco-url-referencia-apa
titulo: Extrair campos com uma única expressão regular (grupos nomeados e opcionais): endereço com rua, número, apartamento, bairro, CEP, cidade e estado; todas as URLs de um texto; autores, ano, título e editora de uma referência APA
assunto: pln-01-regex-e-preprocessamento
tipo: lista
questao: Lista 1, questões 3 a 5
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 1, questões 3 a 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Grupos nomeados:** `(?P<nome>...)` captura um trecho e dá nome a ele; `m.groupdict()` devolve um dicionário. **Grupo opcional:** `(?:..., )?` (não capturante com `?`) para partes que podem faltar. **`re.I`** ignora maiúsculas (CEP e cep). **Preguiçoso:** `.+?` pega o mínimo possível, útil antes de um separador.

**Exemplo parecido** (agenda, não endereço): "Reunião, sala 12, bloco B, 14h30. Maceió, AL." com bloco opcional:
```python
import re

PADRAO = re.compile(
    r"(?P<evento>[^,]+), sala (?P<sala>\d+)"
    r"(?:, bloco (?P<bloco>\w+))?"
    r", (?P<hora>\d{1,2}h\d{2})\. (?P<cidade>[^,]+), (?P<uf>[A-Z]{2})\.",
    re.I)

m = PADRAO.fullmatch("Reunião, sala 12, bloco B, 14h30. Maceió, AL.")
print(m.groupdict())
```
Sem o bloco, `bloco` vem `None`. No endereço da questão, o apartamento ("apt", "ap") e o bairro são opcionais; teste os três exemplos da lista e um que **não** deve casar.

**URLs:** `re.findall` com algo como `https?://[^\s]+` pega o essencial; decida o que fazer com pontuação no fim (`.` ou `)` colados) e com endereços sem `http` (`www.`).

**Referência APA:** separe primeiro em partes grandes (autores até `(ano).`, título até o próximo `.`, editora), depois quebre os autores por `, &` e `.,`. Teste com outra referência no mesmo formato.

**Verificação:** `test_regex_extracao` roda o padrão da agenda com e sem bloco, confere que um texto fora do formato não casa e que o padrão de URL acha duas URLs num texto e ignora o ponto final.
