---
id: projsw-padrao-observer-biblioteca-atraso
titulo: Padrão Observer — a biblioteca avisa por e-mail e calcula multa quando um empréstimo atrasa, sem conhecer as classes que reagem
assunto: projsw-05-regras-de-projeto
tipo: notas
questao: projeto 5 (sistema de biblioteca: notificações de atraso)
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
Lista de projetos de Projeto/Engenharia de Software do 4º período de Engenharia de Computação (IC-UFAL), projeto 5 (sistema de biblioteca: notificações de atraso). Status da resolução: validada. A explicação e o código são da equipe TutorON e não é gabarito do professor; o código está em `tests_acervo/projsw_java/observer` e é compilado e executado no teste.

**Problema.** O projeto de biblioteca pede notificações automáticas de atraso. Se `Biblioteca.verificar` chamasse direto `enviarEmail(...)` e `calcularMulta(...)`, cada reação nova (SMS, relatório) obrigaria a mexer na classe central: acoplamento alto.

**Observer:** o objeto observado (sujeito) guarda uma lista de observadores que implementam uma interface e, quando o evento ocorre, chama todos. Quem reage se **inscreve**; o sujeito não sabe quais classes concretas existem.
```java
interface ObservadorDeAtraso { void atrasou(String livro, int dias); }
private final List<ObservadorDeAtraso> observadores = new ArrayList<>();
void inscrever(ObservadorDeAtraso o) { observadores.add(o); }
void verificar(String livro, int diasDeAtraso) {
    if (diasDeAtraso <= 0) return;
    for (ObservadorDeAtraso o : observadores) o.atrasou(livro, diasDeAtraso);
}
```
Com dois observadores (e-mail e multa de R$ 1,50 por dia), `verificar("Dom Casmurro", 0)` não imprime nada e `verificar("Dom Casmurro", 3)` imprime o aviso e a multa de 4.50.

**Quando usar:** várias ações independentes depois de um mesmo evento, ou quando a lista de reações muda. Cuidados: a ordem de notificação é a ordem de inscrição; um observador lento atrasa todos; lembre de permitir desinscrever. Interfaces de eventos de Java (listeners do Swing) seguem a mesma ideia.

**Verificação:** `test_observer_biblioteca` compila e roda o exemplo e confere a saída.
