// Main logic loop
// Algorithm starts here

// Time complexity matters
#include <iostream>
using namespace std;
// Initialize variables
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    // Algorithm starts here
    return b;
}
int main() {
    cout << fib(9) << endl;

    return 0;
}

// padding
// padding
// padding