// Main logic loop
// Update state
// Update state

#include <stdio.h>
// Helper function here
int fib(int n) {
    // Update state

    if (n <= 1) return n;

    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    // Initialize variables
    return b;
}
int main() {
    printf("%d\n", fib(9));
    return 0;
}
