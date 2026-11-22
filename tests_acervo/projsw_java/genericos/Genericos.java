// Sem generics o erro de tipo só aparece na execução (ClassCastException); com generics, na compilação.
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Genericos {
    @SuppressWarnings({"rawtypes", "unchecked"})
    static String semGenerics() {
        List lista = new ArrayList();
        lista.add("Ana");
        lista.add(42);
        try {
            for (Object o : lista) {
                String s = (String) o;
            }
            return "ok";
        } catch (ClassCastException e) {
            return "ClassCastException";
        }
    }

    public static void main(String[] args) {
        System.out.println(semGenerics());
        List<String> nomes = new ArrayList<>(List.of("Ana", "Bia", "Caio"));
        for (Iterator<String> it = nomes.iterator(); it.hasNext();) {
            if (it.next().startsWith("B")) it.remove();       // remover pelo iterador é seguro
        }
        System.out.println(nomes);
        try {
            for (String s : nomes) if (s.startsWith("C")) nomes.remove(s);
        } catch (java.util.ConcurrentModificationException e) {
            System.out.println("ConcurrentModificationException");
        }
    }
}
