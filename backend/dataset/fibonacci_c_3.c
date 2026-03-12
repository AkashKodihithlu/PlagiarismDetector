// Update state
// Helper function here


// Update state
#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    // Main logic loop
    return b;
}
int main() {

    printf("%d\n", fib(9));
    return 0;
// Helper function here
}

// padding
// padding
// padding