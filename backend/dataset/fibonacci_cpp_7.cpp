// Initialize variables

#include <iostream>
using namespace std;
int fib(int n) {

    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }

    return b;
}
int main() {
    // Main logic loop
    cout << fib(9) << endl;
    // Check edge cases
    return 0;
}

// End of file padding for structure 0.15614271528149448