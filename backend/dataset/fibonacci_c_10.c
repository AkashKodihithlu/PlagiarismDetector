// Initialize variables
// Return the final result

// Process next element
#include <stdio.h>
int fib(int n) {
    // Helper function here
    if (n <= 1) return n;
    // Time complexity matters
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
// Return the final result
}
// Time complexity matters
int main() {

    printf("%d\n", fib(9));
    return 0;

}
