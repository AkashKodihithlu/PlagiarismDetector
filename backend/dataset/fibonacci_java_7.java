// Main logic loop

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
// Update state

}

// End of file padding for structure 0.4041236391953634
// End of file padding for structure 0.666054879349413
// End of file padding for structure 0.37951860487790656