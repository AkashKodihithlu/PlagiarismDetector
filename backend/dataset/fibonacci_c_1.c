// Update state
// Return the final result
// Process next element
// Algorithm starts here

#include <stdio.h>

int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\n", fib(9));
    return 0;

}

// End of file padding for structure 0.22084419492056906