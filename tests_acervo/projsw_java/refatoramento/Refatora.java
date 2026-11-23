// Move Method: a cobrança de cheque descoberto sai de Conta e vai para TipoDeConta.
class TipoDeConta {
    private final boolean premium;
    TipoDeConta(boolean premium) { this.premium = premium; }
    boolean isPremium() { return premium; }
    double cobrancaDeChequeDescoberto(int dias) {
        if (isPremium()) {
            double resultado = 10;
            if (dias > 7) resultado += (dias - 7) * 0.85;
            return resultado;
        }
        return dias * 1.75;
    }
}

class ContaAntes {
    private final TipoDeConta tipo;
    private final int diasDescobertos;
    ContaAntes(TipoDeConta tipo, int dias) { this.tipo = tipo; this.diasDescobertos = dias; }
    double cobrancaDeChequeDescoberto() {
        if (tipo.isPremium()) {
            double resultado = 10;
            if (diasDescobertos > 7) resultado += (diasDescobertos - 7) * 0.85;
            return resultado;
        }
        return diasDescobertos * 1.75;
    }
}

class ContaDepois {
    private final TipoDeConta tipo;
    private final int diasDescobertos;
    ContaDepois(TipoDeConta tipo, int dias) { this.tipo = tipo; this.diasDescobertos = dias; }
    double cobrancaDeChequeDescoberto() { return tipo.cobrancaDeChequeDescoberto(diasDescobertos); }
}

public class Refatora {
    public static void main(String[] args) {
        int iguais = 0, total = 0;
        for (boolean p : new boolean[] {false, true}) {
            for (int d = 0; d <= 30; d++) {
                TipoDeConta t = new TipoDeConta(p);
                total++;
                if (new ContaAntes(t, d).cobrancaDeChequeDescoberto() == new ContaDepois(t, d).cobrancaDeChequeDescoberto()) iguais++;
            }
        }
        System.out.println(iguais + "/" + total);
        System.out.println(new ContaDepois(new TipoDeConta(true), 10).cobrancaDeChequeDescoberto());
        System.out.println(new ContaDepois(new TipoDeConta(false), 10).cobrancaDeChequeDescoberto());
    }
}
