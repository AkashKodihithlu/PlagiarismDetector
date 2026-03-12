// Initialize variables
// Algorithm starts here

#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    // Update state
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\n", fib(9));
    return 0;
}

// End of file padding for structure 0.6817498195119881
// End of file padding for structure 0.5436250551214062
// End of file padding for structure 0.029319280530298752
// End of file padding for structure 0.21244798707746582