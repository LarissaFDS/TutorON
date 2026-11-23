---
id: pln-expressoes-regulares-padroes-cpf-letras-minusculas-underscore-validacao
titulo: Expressões regulares em Python: testar se um texto tem letras minúsculas seguidas de underscore, validar o formato de um CPF (com âncoras, classes, quantificadores)
assunto: pln-01-regex-e-preprocessamento
tipo: lista
questao: Lista 1, questões 1 e 2
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
Processamento de Linguagem Natural, Prof. Thales Vieira (UFAL, 2021.1), Lista 1, questões 1 e 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

As listas são **avaliativas** (entregues em grupo, com a base de textos de cada um): aqui vão o método e um exemplo parecido, não a resposta da lista.

**Peças de uma expressão regular** (módulo `re`):
- **classes:** `[a-z]` (uma letra minúscula), `\d` (dígito), `\w` (letra, dígito ou `_`), `.` (qualquer caractere);
- **quantificadores:** `+` (1 ou mais), `*` (0 ou mais), `?` (0 ou 1), `{n}` (exatamente $n$), `{m,n}`;
- **âncoras:** `^` início e `$` fim (com `re.fullmatch`, o texto inteiro precisa casar); `\b` fronteira de palavra;
- **escape:** `\.` e `\-` casam o ponto e o hífen literais;
- **`re.search`** procura em qualquer posição; **`re.fullmatch`**, no texto todo.

**Exemplo parecido** (não é a questão): texto com **letras maiúsculas seguidas de hífen**:
```python
import re

def maiusculas_hifen(s):
    return re.search(r"[A-Z]+-", s) is not None

print(maiusculas_hifen("ABC-def"), maiusculas_hifen("abc-"))   # True False
```
Para a questão 1, troque a classe e o separador; decida se a sequência pode estar no meio do texto (`search`) ou se deve ser o texto todo (`fullmatch`).

**Formato com pontuação opcional** (exemplo com CEP `57002-220` ou `57002220`):
```python
def cep_valido(s):
    return re.fullmatch(r"\d{5}-?\d{3}", s) is not None
```
O CPF segue a mesma ideia: grupos de dígitos de tamanho fixo separados por `.` e `-`. Decida se aceita só com pontuação, só sem, ou os dois. **Formato correto não é CPF válido:** os dois últimos dígitos são verificadores (soma ponderada módulo 11), e regex não faz conta.

Mostre exemplos que casam **e** que não casam (dígito a mais, letra, separador errado).

**Verificação:** `test_regex_padroes` roda os exemplos acima e confere casos que devem e que não devem casar.
