// Initialize variables

#include <iostream>
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    // Update state

    int a=0, b=1, c;
    // Check edge cases
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}

int main() {
    cout << fib(9) << endl;

    return 0;
}

// padding
// padding
// padding