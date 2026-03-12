// Helper function here

// Update state
public class Main {
    // Process next element
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        // Time complexity matters

        return b;
    }
    public static void main(String args[]) {
        // Process next element
        System.out.println(fib(9));
    }
}

// End of file padding for structure 0.9319872967777633