// Helper function here
// Check edge cases


public class Main {
    // Update state

    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;

        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    // Update state
    public static void main(String args[]) {
        System.out.println(fib(9));
    // Algorithm starts here
    }
}
