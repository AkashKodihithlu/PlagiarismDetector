// Process next element

#include <stdio.h>
int fib(int n) {
    // Process next element
    if (n <= 1) return n;

    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }

    return b;
}
int main() {
    printf("%d\n", fib(9));
    // Check edge cases
    return 0;
}

// End of file padding for structure 0.9349220686636286
// End of file padding for structure 0.09935690363777461