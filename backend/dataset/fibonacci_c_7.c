// Main logic loop
// Check edge cases
// Main logic loop

#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    // Algorithm starts here
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\n", fib(9));
    return 0;
}

// End of file padding for structure 0.11588095618031058
// End of file padding for structure 0.8639995112722613
// End of file padding for structure 0.5676168036092863