// Conta tem uma Pessoa (composição): delegação em vez de herança.
class Pessoa {
    private final String nome, cpf;
    Pessoa(String nome, String cpf) { this.nome = nome; this.cpf = cpf; }
    String getNome() { return nome; }
    String getCpf() { return cpf; }
}

class Conta {
    private Pessoa titular;
    private double saldo;
    Conta(Pessoa titular) { this.titular = titular; }
    String getNomeTitular() { return titular.getNome(); }   // delega
    void trocarTitular(Pessoa nova) { titular = nova; }     // composição muda em tempo de execução
    void depositar(double v) { saldo += v; }
    double getSaldo() { return saldo; }
}

public class Composicao {
    public static void main(String[] args) {
        Conta c = new Conta(new Pessoa("Joao", "111"));
        c.depositar(50);
        System.out.println(c.getNomeTitular() + " " + c.getSaldo());
        c.trocarTitular(new Pessoa("Maria", "222"));
        System.out.println(c.getNomeTitular() + " " + c.getSaldo());
    }
}
