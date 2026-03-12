// Return the final result

public class Main {

    static int fib(int n) {
        if (n <= 1) return n;

        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        // Update state
        return b;

    }

    public static void main(String args[]) {
        // Main logic loop
        System.out.println(fib(9));
    // Main logic loop
    }

}
