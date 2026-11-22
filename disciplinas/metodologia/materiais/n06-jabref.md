---
id: metodologia-nota-jabref
titulo: Nota da equipe — JabRef: gerenciador de referências que edita o arquivo .bib usado pelo BibTeX
assunto: metodologia-08-referencias-bibtex-jabref
tipo: nota
resolucao: nao
fonte: Nota da equipe TutorON escrita com apoio de IA, a partir de ideias gerais das fontes do catálogo, sem transcrição
fontes_catalogo: jabref
autoria: Equipe TutorON com apoio de IA; sem revisão humana
licenca: Texto próprio
publicacao_transcricao: não se aplica
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
O **JabRef** é um programa livre (licença MIT, em Java) que abre e edita arquivos .bib. A turma recebeu a versão 2.10; as versões atuais têm recursos parecidos, com interface diferente.

Uso típico:
1. Crie ou abra o `refs.bib` do trabalho.
2. Nova entrada: escolha o tipo (Article, Book, Misc) e preencha os campos; ou cole um DOI ou ISBN para buscar os dados.
3. Gere a chave de citação automaticamente (padrão autor e ano, como `lopez2013`).
4. No .tex, cite com `\cite{lopez2013}` e compile com BibTeX.

Vantagens: evita erro de sintaxe no .bib, aponta campos faltando e duplicatas, e importa referências de bases de dados.

**Verificação:** nota sem revisão humana; fica fora da busca até ser revisada.
