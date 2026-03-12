// Return the final result

public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    public static void main(String args[]) {
        // Return the final result
        System.out.println(fib(9));
    // Check edge cases
    }
// Algorithm starts here
}

// End of file padding for structure 0.5183832923859387
// End of file padding for structure 0.13144565172161982
// End of file padding for structure 0.06121157899554941