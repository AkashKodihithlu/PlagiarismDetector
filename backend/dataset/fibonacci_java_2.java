// Helper function here
// Initialize variables
// Check edge cases
// Time complexity matters

// Initialize variables
public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    public static void main(String args[]) {
        System.out.println(fib(9));
    }
}

// End of file padding for structure 0.017378299273822617
// End of file padding for structure 0.3090092714777559