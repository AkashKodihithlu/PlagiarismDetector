// Initialize variables
// Process next element
// Return the final result

#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    // Process next element
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\n", fib(9));

    return 0;
// Process next element
}


// padding
// padding
// padding