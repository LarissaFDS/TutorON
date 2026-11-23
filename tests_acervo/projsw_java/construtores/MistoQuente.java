// Ordem de construção e método polimórfico chamado no construtor (exemplo das notas de Programação II, UFCG).
class Refeicao {
    Refeicao() { System.out.println("Refeicao()"); }
}

class Almoco extends Refeicao {
    Almoco() {
        System.out.println("Almoco() antes do preparo");
        prepara();
        System.out.println("Almoco() depois do preparo");
    }
    void prepara() { System.out.println("Prepara Almoco"); }
}

class AlmocoPortatil extends Almoco {
    AlmocoPortatil() {
        System.out.println("AlmocoPortatil() antes do preparo");
        prepara();
        System.out.println("AlmocoPortatil() depois do preparo");
    }
    @Override void prepara() { System.out.println("Prepara AlmocoPortatil"); }
}

class Pao { Pao() { System.out.println("Pao()"); } }
class Queijo { Queijo() { System.out.println("Queijo()"); } }
class Presunto { Presunto() { System.out.println("Presunto()"); } }

public class MistoQuente extends AlmocoPortatil {
    private Pao pao = new Pao();
    private Queijo queijo = new Queijo();
    private Presunto presunto = new Presunto();

    MistoQuente() {
        System.out.println("MistoQuente() antes do preparo");
        prepara();
        System.out.println("MistoQuente() depois do preparo");
    }

    @Override void prepara() {
        System.out.println("Prepara MistoQuente" + (pao == null ? " (pao ainda null)" : ""));
    }

    public static void main(String[] args) { new MistoQuente(); }
}
