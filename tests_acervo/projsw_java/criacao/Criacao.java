// Padrões de criação: Factory Method (escolhe a classe concreta), Builder (monta passo a passo e valida)
// e Singleton (uma só instância).
public class Criacao {
    interface Conta { String tipo(); }
    static class Corrente implements Conta { public String tipo() { return "corrente"; } }
    static class Poupanca implements Conta { public String tipo() { return "poupanca"; } }

    static Conta criarConta(String tipo) {
        switch (tipo) {
            case "corrente": return new Corrente();
            case "poupanca": return new Poupanca();
            default: throw new IllegalArgumentException("tipo desconhecido: " + tipo);
        }
    }

    static class Pedido {
        final String cliente; final int itens; final boolean presente;
        private Pedido(Builder b) { cliente = b.cliente; itens = b.itens; presente = b.presente; }
        public String toString() { return cliente + ", " + itens + " item(ns), presente=" + presente; }

        static class Builder {
            private String cliente; private int itens = 1; private boolean presente;
            Builder cliente(String c) { cliente = c; return this; }
            Builder itens(int n) { itens = n; return this; }
            Builder presente() { presente = true; return this; }
            Pedido build() {
                if (cliente == null || itens < 1) throw new IllegalStateException("pedido invalido");
                return new Pedido(this);
            }
        }
    }

    static final class Configuracao {
        private static final Configuracao UNICA = new Configuracao();
        private Configuracao() { }
        static Configuracao instancia() { return UNICA; }
    }

    public static void main(String[] args) {
        System.out.println(criarConta("poupanca").tipo());
        System.out.println(new Pedido.Builder().cliente("Ana").itens(3).presente().build());
        System.out.println(new Pedido.Builder().cliente("Bia").build());
        try { new Pedido.Builder().itens(2).build(); } catch (IllegalStateException e) { System.out.println(e.getMessage()); }
        System.out.println(Configuracao.instancia() == Configuracao.instancia());
    }
}
