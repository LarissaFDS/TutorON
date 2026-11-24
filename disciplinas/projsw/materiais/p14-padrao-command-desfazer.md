---
id: projsw-padrao-command-desfazer
titulo: Padrão Command — cada ação vira objeto com executar() e desfazer(); pilha de histórico para o "desfazer" (Ctrl+Z)
assunto: projsw-05-regras-de-projeto
tipo: notas
questao: projetos com edição e histórico (gerenciador de conteúdo, tarefas)
resolucao: sim
fonte: Lista de projetos de software orientado a objetos usada no 4º período de Engenharia de Computação (Software_Projects.pdf, IC-UFAL), com o tópico de padrões de projeto da disciplina
curso: Engenharia de Computação (UFAL), Engenharia de Software (ECOM021) / Projeto de Software, 4º período
fontes_catalogo: ufal-ecom-lista-projetos-oo
autoria: Lista de projetos da disciplina (autor não identificado no arquivo), citada em paráfrase; explicação e código Java da equipe TutorON
licenca: Não declarada (lista da disciplina); paráfrase, PDF não versionado; código próprio
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista de projetos de Projeto/Engenharia de Software do 4º período de Engenharia de Computação (IC-UFAL), projetos com edição e histórico (gerenciador de conteúdo, tarefas). Status da resolução: validada. A explicação e o código são da equipe TutorON e não é gabarito do professor; o código está em `tests_acervo/projsw_java/comando` e é compilado e executado no teste.

**Problema.** Sistemas da lista (gerenciador de conteúdo, de tarefas) precisam de desfazer. Guardar só o estado "antes" de tudo é caro; espalhar `if` para cada tipo de ação é frágil.

**Command:** encapsule cada ação num objeto com a mesma interface. Quem dispara não sabe o que a ação faz; o histórico é só uma pilha de comandos.
```java
interface Comando { void executar(); void desfazer(); }
static class Inserir implements Comando {
    private final String trecho;
    Inserir(String trecho) { this.trecho = trecho; }
    public void executar() { texto.append(trecho); }
    public void desfazer() { texto.setLength(texto.length() - trecho.length()); }
}
static void fazer(Comando c) { c.executar(); historico.push(c); }
static void desfazer() { if (!historico.isEmpty()) historico.pop().desfazer(); }
```
Com `fazer(new Inserir("Ola"))` e `fazer(new Inserir(", mundo"))`, o texto é `Ola, mundo`; um `desfazer()` volta a `Ola`; mais dois deixam o texto vazio, e o segundo não falha porque a pilha vazia é testada.

**Por que pilha (LIFO):** desfaz-se primeiro a última ação. Para "refazer", use uma segunda pilha que recebe o que foi desfeito. Cada comando precisa guardar o que precisa para se desfazer (aqui, o trecho inserido).

**Verificação:** `test_command_desfazer` compila e roda o exemplo e confere a saída.
