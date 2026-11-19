# Curadoria e integração dos PRs 31 e 34

Conferência de 03/11/2026, com metadados atuais do GitHub, `git fetch origin`,
comparação de histórico, simulação de merge e execução local da suíte combinada.
Nenhum PR foi alterado ou integrado no GitHub.

## Conclusão

A curadoria mencionada aparece em nome de **LarissaFDS**. Não encontrei autoria
com o nome Alice no histórico Git consultado. O trabalho de novos acervos partiu
da base comum em `dev`, sem incorporar os novos commits dos PRs 31 e 34.

O Git combina os arquivos sem conflitos, mas **a integração ainda não está
pronta para ser considerada validada**: a combinação de `dev` com os PRs 31 e 34
teve **500 testes aprovados e 9 falhas**. O novo prompt socrático não recebe as
regras específicas das disciplinas novas. Parte dos testes também precisa ser
adaptada à mudança do fluxo para o prompt socrático.

## O que a curadoria fez

| PR | Disciplina | Situação consultada | Conteúdo |
|---|---|---|---|
| [30](https://github.com/LarissaFDS/TutorON/pull/30) | OAC | Integrado em `dev` | 28 blocos, catálogo de fontes, correções das anotações e exercícios, regras de rigor e testes. |
| [32](https://github.com/LarissaFDS/TutorON/pull/32) | Cálculo 3 | Integrado em `dev` | 21 blocos, 16 na busca, curadoria e verificações matemáticas. |
| [33](https://github.com/LarissaFDS/TutorON/pull/33) | Física 2 | Integrado em `dev` | 34 blocos, 30 na busca, correções das notas e exercícios, verificações e rastreabilidade. |
| [35](https://github.com/LarissaFDS/TutorON/pull/35) | Estrutura de Dados | Aberto, base `dev` | 20 blocos, 18 na busca, correções de código C, catálogo, testes e regras de rigor. |

Curadoria aqui significa organizar e conferir materiais para a busca: cadastrar
fontes, reescrever/parafrasear o conteúdo, corrigir erros, distinguir material da
turma de notas da equipe, registrar pendências e gerar índices por disciplina.
**Não é um novo treinamento de pesos nem outro modelo de IA.**

As disciplinas novas estão **em validação**, com barreira 403 no atendimento
normal. Revisão humana e confirmação docente continuam pendentes; o status
"validada" de uma resolução não equivale a aprovação do professor.

Além dos dados e testes, a curadoria integrada mudou dois pontos do código:

- `acervo/disciplinas.py`: aceita e preserva o campo opcional `status_resolucao`
  (`validada`, `corrigida`, `pendente_professor`).
- `acervo/retrieval.py`: normaliza potências e alguns comandos LaTeX para a busca.

Os novos acervos não mudaram o modelo, os pesos ou a interface do tutor. O ajuste
de tokenização é compartilhado e foi incluído na verificação da combinação.

## Relação entre branches

- `dev`: `4eb75373330c003bce4cef356882f4f8498c8199`.
- [PR 31](https://github.com/LarissaFDS/TutorON/pull/31):
  `codex/tutor-socratico-treino`, `b853c9291573be04451ad8d8a51e6a722131c1b8`,
  base `dev`, **ainda como rascunho**.
- [PR 34](https://github.com/LarissaFDS/TutorON/pull/34):
  `codex/fotos-fallback-local`, `1f19744b0ce5f03744146c6906f8be4439f4dead`,
  base **`codex/tutor-socratico-treino`**. Contém um commit adicional ao PR 31.
- Ancestral comum de `dev` e PR 31: `1a2df17` (merge do PR 29).
- Ancestral comum de OAC e PR 31: `ac44410`, anterior ao trabalho novo do PR 31.

Os acervos foram desenvolvidos em paralelo. Cálculo 3 e Física 2 reaproveitaram
OAC, e a integração entre eles já está no `dev` atual. O PR 34, por outro lado,
**é empilhado sobre o PR 31**.

## Merge e testes

`git merge-tree --write-tree` terminou com sucesso para:

- `dev` + PR 31: árvore `9bc919291e0fd0ce0c845a36dbd4475ba0bf50d7`;
- `dev` + PR 34 (inclui 31): árvore `7de453416f1f3c9bdcc2022456a05a8dad67e096`;
- branch do PR 35 + PR 34: sem conflitos de arquivos; essa combinação com ED
  **não teve a suíte executada**.

Os arquivos modificados pelos dois conjuntos, em relação à base comum de 31 e
`dev`, foram `README.md` e `backend/tests/test_disciplinas.py`. O merge automático
não perdeu as adições da curadoria nesses arquivos.

Uma cópia isolada recebeu `dev` + PR 34 por merge sem commit. Com SymPy instalado
(dependência declarada em `requirements-acervo.txt`), foi executado:

```text
python -m pytest backend/tests tests_acervo eval/test_eval.py -q
9 failed, 500 passed in 55.33s

node --test backend/tests/test_foto_frontend.cjs
5 passed

git diff --check
sem erros
```

As nove falhas estão em `backend/tests/test_disciplinas.py`:

- Quatro casos de perguntas de OAC: ausência das regras RISC-V RV32 no sistema.
- Dois testes de equivalência do texto comum entre disciplinas: foram escritos
  para retirar o rigor do prompt antigo, mas o tutor agora usa outro rigor.
- Um caso de resolução corrigida de OAC: ausência da orientação específica de
  não tratar a resolução da equipe como gabarito oficial.
- Um caso de Cálculo 3: ausência das regras de notação do Stewart.
- Um caso de Física 2: ausência da convenção de sinais da primeira lei.

### Causa concreta e ajuste recomendado

Em `backend/prompts.py:160`, `sistema_socratico` substitui `d.rigor` por um texto
de `_RIGOR_SOCRATICO`, que só tem PAA e SD. Para OAC, Cálculo 3, Física 2 e ED,
usa apenas uma instrução genérica. Portanto, os novos arquivos `rigor.md` não
chegam ao sistema do tutor no caminho socrático. O material recuperado e os
status das resoluções chegam ao prompt da pergunta; as regras específicas de
orientação ficam de fora.

Antes do merge, adaptar o rigor das disciplinas novas para o atendimento
socrático, preservando notação, unidades, hipóteses e procedência. **Não basta
anexar cegamente os textos antigos**: alguns mandam preencher todos os sinais
de um datapath ou fazer uma resolução completa, contrariando a política nova.
Depois, atualizar os testes do fluxo multidisciplina para conferir o prompt
socrático e executar novamente a suíte combinada.

Não houve chamada à IA real nesta auditoria; os testes de API usam modelo
simulado e acervos reais. As consultas de workflows associados aos heads de 31
e 34 não retornaram execuções; isso não substitui as verificações locais.

## Ordem de integração recomendada

1. Levar o `dev` atual ao branch do PR 31 e corrigir a compatibilidade descrita.
2. Validar a combinação, retirar o estado de rascunho e integrar 31 em `dev`.
3. Atualizar o branch 34 com o resultado, mudar sua base para `dev`, conferir
   que o diff contém só a correção de fotos e integrar 34.
4. Se houver squash/rebase no 31, rebasear/ajustar o 34 antes de mudar sua base,
   evitando reapresentar o histórico inteiro do 31.

Esta auditoria não altera branches remotos, não faz merge e não libera as
disciplinas que estão em validação.
