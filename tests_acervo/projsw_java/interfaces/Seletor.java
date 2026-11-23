// Um só cliente para coleções de alunos e de disciplinas, por meio de interfaces.
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

interface Nomeavel { String getNome(); }

interface SelecionavelPorNome { Iterator<Nomeavel> getIteradorPorNome(String nome); }

class Aluno implements Nomeavel {
    private final String nome;
    Aluno(String nome) { this.nome = nome; }
    public String getNome() { return nome; }
}

class Disciplina implements Nomeavel {
    private final String nome;
    Disciplina(String nome) { this.nome = nome; }
    public String getNome() { return nome; }
    @Override public String toString() { return "Disciplina " + nome; }
}

class Colecao<T extends Nomeavel> implements SelecionavelPorNome {
    private final List<T> itens = new ArrayList<>();
    void add(T x) { itens.add(x); }
    public Iterator<Nomeavel> getIteradorPorNome(String nome) {
        List<Nomeavel> achados = new ArrayList<>();
        for (T x : itens) if (x.getNome().equals(nome)) achados.add(x);
        return achados.iterator();
    }
}

public class Seletor {
    static int conta(SelecionavelPorNome c, String nome) {   // o cliente só conhece a interface
        int k = 0;
        for (Iterator<Nomeavel> it = c.getIteradorPorNome(nome); it.hasNext(); it.next()) k++;
        return k;
    }

    public static void main(String[] args) {
        Colecao<Aluno> alunos = new Colecao<>();
        alunos.add(new Aluno("Joao"));
        alunos.add(new Aluno("Ana"));
        alunos.add(new Aluno("Joao"));
        Colecao<Disciplina> disc = new Colecao<>();
        disc.add(new Disciplina("Programacao"));
        disc.add(new Disciplina("Calculo"));
        System.out.println(conta(alunos, "Joao") + " " + conta(disc, "Programacao") + " " + conta(disc, "Joao"));
        Nomeavel n = new Disciplina("Grafos");
        System.out.println(n);                          // ligação dinâmica: toString de Disciplina
    }
}
