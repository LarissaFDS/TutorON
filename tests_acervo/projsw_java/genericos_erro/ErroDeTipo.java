// Com List<String>, acrescentar um inteiro é erro de compilação.
import java.util.ArrayList;
import java.util.List;

public class ErroDeTipo {
    public static void main(String[] args) {
        List<String> nomes = new ArrayList<>();
        nomes.add(42);
    }
}
