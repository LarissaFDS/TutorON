// Observer: a biblioteca avisa quem se inscreveu quando um empréstimo atrasa, sem conhecer as classes concretas.
import java.util.ArrayList;
import java.util.List;

public class Biblioteca {
    interface ObservadorDeAtraso { void atrasou(String livro, int dias); }

    private final List<ObservadorDeAtraso> observadores = new ArrayList<>();

    void inscrever(ObservadorDeAtraso o) { observadores.add(o); }

    void verificar(String livro, int diasDeAtraso) {
        if (diasDeAtraso <= 0) return;
        for (ObservadorDeAtraso o : observadores) o.atrasou(livro, diasDeAtraso);
    }

    public static void main(String[] args) {
        Biblioteca b = new Biblioteca();
        b.inscrever((livro, dias) -> System.out.println("e-mail: " + livro + " atrasado " + dias + " dia(s)"));
        b.inscrever((livro, dias) -> System.out.println("multa: R$ " + String.format(java.util.Locale.ROOT, "%.2f", dias * 1.5)));
        b.verificar("Dom Casmurro", 0);
        b.verificar("Dom Casmurro", 3);
    }
}
