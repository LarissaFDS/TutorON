// Esboço do projeto do robô: Robo tem uma Sala, é Comparable pela energia; dois tipos herdam de Robo.
class Sala {
    private final boolean[][] ocupada;
    Sala(int linhas, int colunas) { ocupada = new boolean[linhas][colunas]; }
    boolean livre(int l, int c) {
        return l >= 0 && c >= 0 && l < ocupada.length && c < ocupada[0].length && !ocupada[l][c];
    }
    void ocupar(int l, int c, boolean sim) { ocupada[l][c] = sim; }
}

abstract class Robo implements Comparable<Robo> {
    private Sala sala;
    private int linha, coluna, passos, energia;
    Robo(Sala sala, int energia) { this.energia = energia; mudarDeSala(sala); }

    final void mudarDeSala(Sala nova) {
        if (sala != null) sala.ocupar(linha, coluna, false);
        sala = nova;
        linha = 0;
        coluna = 0;
        sala.ocupar(0, 0, true);
    }

    boolean mover(char direcao) {                 // 'S' sobe, 'D' desce, 'E' esquerda, 'R' direita
        int l = linha + (direcao == 'D' ? 1 : direcao == 'S' ? -1 : 0);
        int c = coluna + (direcao == 'R' ? 1 : direcao == 'E' ? -1 : 0);
        if (energia == 0 || !sala.livre(l, c)) return false;
        sala.ocupar(linha, coluna, false);
        linha = l;
        coluna = c;
        sala.ocupar(l, c, true);
        passos++;
        energia--;
        return true;
    }

    int getPassos() { return passos; }
    int getEnergia() { return energia; }
    @Override public int compareTo(Robo outro) { return Integer.compare(energia, outro.energia); }
    abstract String acaoEspecial();
}

class RoboSeguranca extends Robo {
    RoboSeguranca(Sala s, int e) { super(s, e); }
    String acaoEspecial() { return "alarme"; }
}

class RoboDiversao extends Robo {
    RoboDiversao(Sala s, int e) { super(s, e); }
    String acaoEspecial() { return "responde a voz"; }
}

public class Robos {
    public static void main(String[] args) {
        Sala sala = new Sala(3, 3);
        Robo a = new RoboSeguranca(sala, 5);
        System.out.println(a.mover('S') + " " + a.mover('R') + " " + a.mover('D'));
        Robo b = new RoboDiversao(new Sala(2, 2), 1);
        System.out.println(b.mover('R') + " " + b.mover('D'));
        System.out.println(a.getPassos() + " " + a.getEnergia() + " " + b.getEnergia());
        System.out.println(a.compareTo(b) > 0);
        Robo[] r = {a, b};
        for (Robo x : r) System.out.println(x.acaoEspecial());
    }
}
