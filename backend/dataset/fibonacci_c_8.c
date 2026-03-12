// Check edge cases
// Update state

#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
// Initialize variables
}
// Main logic loop
int main() {
    printf("%d\n", fib(9));
    return 0;
}

// End of file padding for structure 0.7541030423322833
// End of file padding for structure 0.9255550718422487
// End of file padding for structure 0.5986675154586686