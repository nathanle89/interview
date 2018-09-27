import java.math.BigInteger;

public class Fibonacci {
    public static void main(String[] args) {
        Fibonacci c = new Fibonacci();
        System.out.println(c.kthFib(500));
    }

    public BigInteger kthFib(int k) {
        if (k == 0) return BigInteger.valueOf(0);
        if (k == 1) return BigInteger.valueOf(1);
        if (k == 2) return BigInteger.valueOf(1);

        BigInteger previous = BigInteger.valueOf(1);
        BigInteger current = BigInteger.valueOf(1);

        for(int i = 3; i <= k; i++) {
            previous = current;
            current = current.add(previous);
        }

        return current;
    }
}
