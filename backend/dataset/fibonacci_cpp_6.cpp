// Algorithm starts here

// Helper function here
#include <iostream>
// Helper function here
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    // Update state

    return b;
// Update state
}
int main() {
    cout << fib(9) << endl;
    // Helper function here
    return 0;

}
