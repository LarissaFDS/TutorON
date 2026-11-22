---
id: projsw-arquivos-bufferedreader-try-with-resources
titulo: Arquivos em Java — FileReader embrulhado em BufferedReader, ler linha a linha até null, fechar o arquivo com try-with-resources, FileNotFoundException antes de IOException
assunto: projsw-07-excecoes-arquivos
tipo: notas
questao: exemplos de leitura de arquivo texto
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Estrutura de dados — Arquivos"
curso: Ciência da Computação (UFAL), pasta da turma de Programação 2 / Projeto de Software (COMP372); notas de aula da UFCG usadas pela turma
fontes_catalogo: ufcg-notas-programacao2
autoria: Notas de aula dos Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey (DSC-UFCG); resolução e código da equipe TutorON
licenca: Copyright da UFCG nos exemplos; paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Notas de aula de Programação II da UFCG, seção "Estrutura de dados — Arquivos" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Fluxos (streams):** o pacote `java.io` tem fluxos de bytes (`FileInputStream`, para qualquer arquivo) e de caracteres (`FileReader`, só texto). Usá-los é embrulhar um fluxo no outro: `new BufferedReader(new FileReader("dados.txt"))` acrescenta um **buffer** (lê blocos grandes de uma vez, menos acessos ao disco) e o método `readLine()`.

**Ler linha a linha:** `readLine()` devolve `null` no fim do arquivo.
```java
static int contar(String nome) throws IOException {
    int n = 0;
    try (BufferedReader in = new BufferedReader(new FileReader(nome))) {
        while (in.readLine() != null) n++;
    }
    return n;
}
```
**Fechar:** abrir um arquivo reserva um recurso do sistema operacional. As notas fecham no `finally`; desde o Java 7, o `try (...)` (try-with-resources) fecha sozinho, mesmo com exceção.

**Erros:** arquivo inexistente lança `FileNotFoundException`, subclasse de `IOException`; no `catch`, trate-a antes. `IOException` é *checked*: o método trata ou declara `throws IOException`.

**Escrever:** `PrintWriter out = new PrintWriter(new FileWriter("saida.txt"))` com `out.println(...)`; sem fechar, o buffer pode não ser gravado.

**Verificação:** `test_arquivos` grava um arquivo de 3 linhas, roda `tests_acervo/projsw_java/arquivos` (conta 3) e confere que o arquivo inexistente cai no `catch` de `FileNotFoundException`.
