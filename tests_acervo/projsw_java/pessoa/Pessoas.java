// == compara referências; equals (sobrescrito) compara o conteúdo; hashCode acompanha equals.
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

class Pessoa {
    private final String nome, cpf;
    Pessoa(String nome, String cpf) { this.nome = nome; this.cpf = cpf; }
    @Override public boolean equals(Object o) {
        if (!(o instanceof Pessoa)) return false;
        Pessoa p = (Pessoa) o;
        return nome.equals(p.nome) && cpf.equals(p.cpf);
    }
    @Override public int hashCode() { return Objects.hash(nome, cpf); }
    @Override public String toString() { return "Pessoa " + nome + ", CPF " + cpf; }
}

class PessoaSemEquals {
    final String nome, cpf;
    PessoaSemEquals(String nome, String cpf) { this.nome = nome; this.cpf = cpf; }
}

public class Pessoas {
    public static void main(String[] args) {
        Pessoa a = new Pessoa("Joao", "113"), b = new Pessoa("Joao", "113");
        System.out.println((a == b) + " " + a.equals(b));
        Set<Pessoa> s = new HashSet<>();
        s.add(a);
        s.add(b);
        System.out.println(s.size());
        PessoaSemEquals c = new PessoaSemEquals("Joao", "113"), d = new PessoaSemEquals("Joao", "113");
        System.out.println(c.equals(d));
        System.out.println(a);
    }
}
