---
id: bd-aula-conceitos-sgbd
titulo: Aula de BD — banco de dados, SGBD, vantagens e breve histórico
assunto: bd-01-conceitos-sgbd
tipo: material_estudo
fonte: Slides de Banco de Dados (UFAL, Profª Maria Cristina Tenório), aula 1 "Introdução a Banco de Dados", parte 1
fontes_catalogo: ufal-bd-slides
autoria: Profª Maria Cristina Tenório (slides, com créditos a material dos professores Tarsis Marinho e Patrick Brito), reescrito pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides de aula)
publicacao_transcricao: não se aplica: o bloco reescreve com texto próprio; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
revisao_humana: pendente
---
Banco de dados é uma coleção de dados inter-relacionados sobre um domínio específico (o minimundo), com significado próprio. Exemplo da aula: nome, endereço e nota dos alunos de uma escola são dados; "Marina tem a maior nota da turma" é uma informação tirada deles. As operações básicas são inserção, recuperação (consulta), atualização e exclusão.

Características da abordagem de banco de dados: natureza autodescritiva (o catálogo guarda a descrição do esquema), isolamento entre programas e dados (abstração de dados), suporte a múltiplas visões e compartilhamento com processamento de transações multiusuário. Atores: administrador do banco (DBA), projetista, analista de sistemas, programador e usuário final.

SGBD (sistema de gerenciamento de banco de dados) é a coleção de programas que permite criar e manter um banco de dados. Vantagens:
- controle de redundância (o mesmo dado guardado várias vezes desperdiça espaço e fica inconsistente);
- restrições de integridade, por exemplo nota entre 0 e 10 e matrícula única e não nula;
- backup e recuperação após falhas, mantendo o banco num estado consistente;
- restrição de acesso não autorizado (cada usuário só faz as operações permitidas);
- controle de concorrência (vários usuários ao mesmo tempo, de forma coerente).

Quando não usar um SGBD: investimento inicial alto, requisitos de tempo real que nenhum SGBD atende, ou operações muito específicas.

Histórico: nos anos 60, modelos hierárquico (IMS, árvore de registros pai e filho) e em rede (CODASYL, grafo com associações 1:N entre proprietário e membro), com acesso por ponteiros e dependência da estrutura física. Em 1970, Codd propõe o modelo relacional, que separa a estrutura lógica do armazenamento físico; Ingres e System R são os primeiros protótipos, e Peter Chen propõe o modelo entidade-relacionamento. Nos anos 80, SQL vira padrão.

Correções da equipe
- A restrição de nota do slide liga as duas comparações com "ou"; o certo é "e": `CHECK (nota >= 0 AND nota <= 10)`. Com "ou", qualquer nota passaria.
