// Initialize variables
// Time complexity matters
// Return the final result
// Check edge cases

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

// End of file padding for structure 0.19445579422343306
// End of file padding for structure 0.6048922600189973