// Initialize variables
// Update state
// Main logic loop
// Algorithm starts here

#include <iostream>
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
// Helper function here
}
int main() {
    cout << fib(9) << endl;
    return 0;
}

// End of file padding for structure 0.5989632554615472