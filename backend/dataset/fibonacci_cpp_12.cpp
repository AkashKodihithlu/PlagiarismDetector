// Time complexity matters

// Process next element
#include <iostream>
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
// Update state
}
int main() {
    cout << fib(9) << endl;
    return 0;
}

// End of file padding for structure 0.13103496451440544
// End of file padding for structure 0.42223844520922715
// End of file padding for structure 0.25014719026831633