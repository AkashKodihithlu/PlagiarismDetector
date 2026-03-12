// Initialize variables
// Update state

#include <stdio.h>
int fib(int n) {
    // Time complexity matters

    if (n <= 1) return n;
    // Check edge cases
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }

    return b;
// Algorithm starts here
}
int main() {
    printf("%d\n", fib(9));
    return 0;
}

