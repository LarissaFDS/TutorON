// Lê um arquivo texto linha a linha com BufferedReader; try-with-resources fecha o arquivo.
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Linhas {
    static int contar(String nome) throws IOException {
        int n = 0;
        try (BufferedReader in = new BufferedReader(new FileReader(nome))) {
            while (in.readLine() != null) n++;
        }
        return n;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(contar(args[0]));
        try {
            contar(args[0] + ".naoexiste");
        } catch (FileNotFoundException e) {        // subclasse de IOException: vem antes
            System.out.println("FileNotFoundException");
        } catch (IOException e) {
            System.out.println("IOException");
        }
    }
}
