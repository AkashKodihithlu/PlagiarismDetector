// Check edge cases
// Update state
// Process next element


#include <iostream>
using namespace std;
int fib(int n) {
    // Update state
    if (n <= 1) return n;
    int a=0, b=1, c;
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