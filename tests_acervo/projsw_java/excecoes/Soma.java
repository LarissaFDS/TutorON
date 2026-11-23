// try-catch em volta do laço (versão 1) e dentro do laço (versão 2).
public class Soma {
    static void soma1(String[] args) {
        try {
            int sum = 0;
            for (String a : args) sum += Integer.parseInt(a);
            System.out.println("Sum = " + sum);
        } catch (NumberFormatException nfe) {
            System.err.println("One of the command-line arguments is not an integer.");
        }
    }

    static void soma2(String[] args) {
        int sum = 0;
        for (String a : args) {
            try {
                sum += Integer.parseInt(a);
            } catch (NumberFormatException nfe) {
                System.err.println("[" + a + "] is not an integer and will not be included in the sum.");
            }
        }
        System.out.println("Sum = " + sum);
    }

    public static void main(String[] args) {
        String[] resto = java.util.Arrays.copyOfRange(args, 1, args.length);
        if (args[0].equals("1")) soma1(resto); else soma2(resto);
    }
}
