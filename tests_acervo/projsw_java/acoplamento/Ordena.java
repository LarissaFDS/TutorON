// Lista ordenada genérica: só conhece Comparable, não sabe nada de Aluno.
import java.util.ArrayList;
import java.util.List;

class Aluno implements Comparable<Aluno> {
    private final String nome;
    private final long matricula;
    Aluno(String nome, long matricula) { this.nome = nome; this.matricula = matricula; }
    String getNome() { return nome; }
    long getMatricula() { return matricula; }
    @Override public int compareTo(Aluno outro) { return Long.compare(matricula, outro.matricula); }
}

class ListaOrdenada<T extends Comparable<T>> {
    private final List<T> elementos = new ArrayList<>();
    void add(T x) {
        int i = 0;
        while (i < elementos.size() && x.compareTo(elementos.get(i)) >= 0) i++;
        elementos.add(i, x);
    }
    List<T> comoLista() { return elementos; }
}

public class Ordena {
    public static void main(String[] args) {
        ListaOrdenada<Aluno> l = new ListaOrdenada<>();
        l.add(new Aluno("Ana", 3_000_000_000L));
        l.add(new Aluno("Bia", 1L));
        l.add(new Aluno("Caio", 2_000_000_000L));
        StringBuilder sb = new StringBuilder();
        for (Aluno a : l.comoLista()) sb.append(a.getNome()).append(' ');
        System.out.println(sb.toString().trim());
        // a subtração convertida para int erra o sinal com matrículas grandes:
        System.out.println((int) (3_000_000_000L - 1L) < 0);
        ListaOrdenada<String> s = new ListaOrdenada<>();
        s.add("b");
        s.add("a");
        System.out.println(s.comoLista());
    }
}
