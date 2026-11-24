// Command: cada ação vira um objeto com executar() e desfazer(); uma pilha guarda o histórico.
import java.util.ArrayDeque;
import java.util.Deque;

public class Editor {
    interface Comando { void executar(); void desfazer(); }

    static StringBuilder texto = new StringBuilder();
    static final Deque<Comando> historico = new ArrayDeque<>();

    static class Inserir implements Comando {
        private final String trecho;
        Inserir(String trecho) { this.trecho = trecho; }
        public void executar() { texto.append(trecho); }
        public void desfazer() { texto.setLength(texto.length() - trecho.length()); }
    }

    static void fazer(Comando c) { c.executar(); historico.push(c); }

    static void desfazer() { if (!historico.isEmpty()) historico.pop().desfazer(); }

    public static void main(String[] args) {
        fazer(new Inserir("Ola"));
        fazer(new Inserir(", mundo"));
        System.out.println(texto);
        desfazer();
        System.out.println(texto);
        desfazer();
        desfazer();
        System.out.println("[" + texto + "]");
    }
}
