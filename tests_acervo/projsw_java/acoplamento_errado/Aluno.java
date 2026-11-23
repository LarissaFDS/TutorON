// Versão das notas: não compila, porque long - long é long e o método devolve int.
public class Aluno implements Comparable<Aluno> {
    long matricula;
    public long getMatricula() { return matricula; }
    @Override public int compareTo(Aluno outro) {
        return this.getMatricula() - outro.getMatricula();
    }
}
