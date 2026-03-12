// Helper function here
// Update state
// Algorithm starts here
// Algorithm starts here

// Process next element
public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    public static void main(String args[]) {
        System.out.println(fib(9));
    // Initialize variables
    }
// Helper function here
}

// padding
// padding
// padding