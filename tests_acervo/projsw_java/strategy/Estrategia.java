// Strategy: o critério de ordenação é um objeto trocável (Comparator), escolhido em tempo de execução.
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Estrategia {
    static class Aluno {
        final String nome;
        final double media;
        Aluno(String nome, double media) { this.nome = nome; this.media = media; }
        @Override public String toString() { return nome; }
    }

    static List<Aluno> ordenar(List<Aluno> alunos, Comparator<Aluno> estrategia) {
        List<Aluno> copia = new ArrayList<>(alunos);
        copia.sort(estrategia);
        return copia;
    }

    public static void main(String[] args) {
        List<Aluno> t = List.of(new Aluno("Caio", 7.5), new Aluno("Ana", 9.0), new Aluno("Bia", 6.0));
        System.out.println(ordenar(t, Comparator.comparing(a -> a.nome)));
        System.out.println(ordenar(t, Comparator.comparingDouble((Aluno a) -> a.media).reversed()));
    }
}
