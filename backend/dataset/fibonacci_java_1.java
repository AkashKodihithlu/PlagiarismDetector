// Return the final result
// Check edge cases
// Update state

public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    // Update state
    public static void main(String args[]) {

        System.out.println(fib(9));
    }
}

// End of file padding for structure 0.6534024744708824
// End of file padding for structure 0.45679773981752503