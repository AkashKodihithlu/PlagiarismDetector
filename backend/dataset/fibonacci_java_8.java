// Main logic loop

public class Main {
    static int fib(int n) {
        if (n <= 1) return n;

        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        // Main logic loop
        return b;
    // Helper function here
    }

    public static void main(String args[]) {
        System.out.println(fib(9));

    }
}

// End of file padding for structure 0.6566515181470277