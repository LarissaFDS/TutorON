---
id: metodologia-abnt-referencias
titulo: Como fazer referências segundo a ABNT (NBR 6023) — livro, artigo de periódico com DOI e documento on-line, ordem e alinhamento
assunto: metodologia-05-normas-abnt-citacoes-referencias
tipo: exercicio
resolucao: sim
fonte: Alves e Arruda, Como elaborar um artigo científico (BU-UFSC, 2004), lista de referências do modelo da turma; atualização pela NBR 6023:2018 segundo guias de bibliotecas
fontes_catalogo: alves-arruda-2004-artigo,ufscar-manual-nbr6023-2018,lopez-silva-2013-latex,wilkins-1995-latex,wilson-2014-best-practices
autoria: Exemplos da equipe TutorON (com apoio de IA), montados a partir dos dados das próprias obras
licenca: Texto próprio da equipe
publicacao_transcricao: não; só paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: parcial
status_resolucao: corrigida
revisao_humana: pendente
---
Exercício da equipe TutorON. A norma de referências é a **NBR 6023**; o modelo da turma segue a edição de 2002, e a vigente é a de **2018**.

**Regras gerais** (modelo da turma e guias da NBR 6023:2018): a lista se chama REFERÊNCIAS; só entra o que foi citado; ordem alfabética do sobrenome; alinhamento só à margem esquerda; espaço simples dentro de cada referência e uma linha em branco entre elas; o título principal em destaque (negrito, aqui com \*\*).

**Livro** — SOBRENOME, Nome. **Título**: subtítulo. Edição. Local: Editora, ano.
> LOPEZ, Ivo Fernandez; SILVA, Maria Darci Godinho da. **Introdução ao uso do LaTeX**. Versão 1.2a. Rio de Janeiro: Edição do autor, 2013.

**Artigo de periódico com DOI** — autor, título do artigo, **nome do periódico**, local, volume, número, páginas ou número do artigo, ano, DOI. Com quatro ou mais autores, pode-se indicar o primeiro seguido de et al.:
> WILSON, Greg *et al*. Best practices for scientific computing. **PLOS Biology**, [*S. l.*], v. 12, n. 1, e1001745, 2014. DOI: 10.1371/journal.pbio.1001745.

**Documento on-line** — os dados do documento, seguidos de "Disponível em:" e "Acesso em:":
> WILKINS, David R. **Getting started with LaTeX**. 2. ed. [*S. l.*: *s. n.*], 1995. Disponível em: https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/. Acesso em: 21 nov. 2026.

**Correção do modelo.** O modelo de 2004 escreve o endereço entre os sinais < e >, como *Disponível em: <http://…>*. A NBR 6023:2018 tirou esses sinais; o endereço vem sem eles. Status da resolução: corrigida, pela edição vigente da norma.

**Na prática:** em LaTeX, não digite a lista à mão; use BibTeX com o estilo do abntex2cite (veja os blocos de BibTeX).

**Verificação:** cada referência tem autor, título, local, editora ou periódico e ano; a lista está em ordem alfabética (LOPEZ, WILKINS, WILSON) e nenhum endereço está entre < e >.
