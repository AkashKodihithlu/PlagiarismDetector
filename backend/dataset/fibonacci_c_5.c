// Update state

// Initialize variables
#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    // Main logic loop
    return b;
// Algorithm starts here
}
// Check edge cases
int main() {
    // Process next element
    printf("%d\n", fib(9));
    // Return the final result

    return 0;
}
