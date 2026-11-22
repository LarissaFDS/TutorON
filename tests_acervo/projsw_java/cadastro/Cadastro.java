// As quatro operações de uma coleção feita com array de tamanho fixo.
public class Cadastro {
    static final int MAX = 10;
    private final String[] nomes = new String[MAX];
    private int n = 0;

    boolean adicionar(String nome) {
        if (n == MAX) return false;            // sem este teste: ArrayIndexOutOfBoundsException
        nomes[n++] = nome;
        return true;
    }

    int pesquisar(String nome) {
        for (int i = 0; i < n; i++) if (nomes[i].equals(nome)) return i;
        return -1;
    }

    boolean remover(String nome) {
        int i = pesquisar(nome);
        if (i < 0) return false;
        nomes[i] = nomes[n - 1];               // a ordem não importa: traz o último para o buraco
        nomes[--n] = null;
        return true;
    }

    String iterar() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) sb.append(nomes[i]).append(i < n - 1 ? "," : "");
        return sb.toString();
    }

    public static void main(String[] args) {
        Cadastro c = new Cadastro();
        for (int i = 1; i <= 11; i++) System.out.println("add p" + i + " " + c.adicionar("p" + i));
        System.out.println(c.pesquisar("p3") + " " + c.pesquisar("x"));
        System.out.println(c.remover("p3") + " " + c.remover("x"));
        System.out.println(c.iterar());
        try {
            String[] cheio = new String[MAX];
            cheio[MAX] = "p11";
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("sem teste: ArrayIndexOutOfBoundsException");
        }
    }
}
