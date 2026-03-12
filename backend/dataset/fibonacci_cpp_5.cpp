// Helper function here
// Return the final result

#include <iostream>
// Return the final result
using namespace std;
int fib(int n) {
    // Return the final result
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
// Time complexity matters
int main() {
    cout << fib(9) << endl;
    // Helper function here
    return 0;

}
