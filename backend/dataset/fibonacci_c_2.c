// Update state
// Return the final result


#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    // Time complexity matters
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\n", fib(9));
    return 0;
}

// End of file padding for structure 0.4340631260157207
// End of file padding for structure 0.19148190747159244
// End of file padding for structure 0.8098738034234538