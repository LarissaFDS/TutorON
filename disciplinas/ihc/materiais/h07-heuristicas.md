---
id: ihc-dez-heuristicas-de-nielsen-avaliacao-heuristica-severidade
titulo: As 10 heurísticas de usabilidade de Nielsen (visibilidade do estado, correspondência com o mundo real, controle e liberdade, consistência, prevenção de erros, reconhecer em vez de lembrar, flexibilidade, design minimalista, recuperação de erros, ajuda) e a avaliação heurística
assunto: ihc-02-avaliacao-de-usabilidade
tipo: exercicio
questao: slides (Nielsen, 1993) e sugestões de melhoria do projeto
resolucao: sim
fonte: Slides da disciplina (cita Nielsen, 1993) e as 10 heurísticas publicadas pelo Nielsen Norman Group
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-slides-dcu,nngroup-10-heuristicas
autoria: Heurísticas de Jakob Nielsen; explicação da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), slides (Nielsen, 1993) e sugestões de melhoria do projeto (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**As 10 heurísticas de Jakob Nielsen** (1994, revistas pelo Nielsen Norman Group):
1. **Visibilidade do estado do sistema:** mostrar o que está acontecendo, com *feedback* em tempo razoável.
2. **Correspondência entre o sistema e o mundo real:** linguagem e conceitos do usuário, não do programador.
3. **Controle e liberdade do usuário:** saídas claras, desfazer e refazer.
4. **Consistência e padrões:** a mesma coisa com o mesmo nome e lugar, seguindo as convenções da plataforma.
5. **Prevenção de erros:** evitar o erro antes de precisar de mensagem (confirmação, limites, bons padrões).
6. **Reconhecer em vez de lembrar:** opções visíveis, sem exigir memória.
7. **Flexibilidade e eficiência de uso:** atalhos para avançados sem atrapalhar iniciantes.
8. **Design estético e minimalista:** sem informação irrelevante competindo com a relevante.
9. **Ajudar a reconhecer, diagnosticar e recuperar erros:** mensagens em linguagem simples, com o problema e a solução.
10. **Ajuda e documentação:** fácil de buscar e focada na tarefa.

**Avaliação heurística:** de 3 a 5 avaliadores percorrem a interface **separadamente**, anotam cada problema com a heurística violada e uma **severidade** (0 a 4: de "não é problema" a "catástrofe") e depois juntam as listas. É barata e rápida, mas **não substitui o teste com usuários**: acha problemas que especialistas veem, não necessariamente os que usuários reais encontram.

**Ligações com o material:**
- "Malfunction 54" (Therac-25) viola a 9 e a 1;
- a barra de busca difícil de achar por um iniciante pede mais destaque, ligado à 6 e à 8;
- atalhos de teclado para avançados são a 7.

Na sugestão de melhoria do trabalho, diga **qual heurística** foi violada e **o que foi observado**.

**Verificação:** `test_heuristicas_de_nielsen` confere que a lista tem as 10 heurísticas na ordem da fonte e classifica três problemas de exemplo pela heurística violada.
