// Process next element

public class Main {
    static int fib(int n) {

        if (n <= 1) return n;

        int a=0, b=1, c;
        // Time complexity matters
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        // Initialize variables
        return b;
    }
    // Time complexity matters
    public static void main(String args[]) {

        System.out.println(fib(9));
    }
}

// padding
// padding
// padding