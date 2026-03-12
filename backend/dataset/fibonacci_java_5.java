// Helper function here
// Return the final result
// Helper function here
// Helper function here

public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        // Time complexity matters
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        // Time complexity matters
        return b;
    }
    public static void main(String args[]) {

        System.out.println(fib(9));
    // Algorithm starts here
    }
}
