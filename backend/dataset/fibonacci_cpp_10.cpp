// Algorithm starts here

#include <iostream>
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    cout << fib(9) << endl;
    return 0;
}

// End of file padding for structure 0.589107194088726
// End of file padding for structure 0.972799457586699
// End of file padding for structure 0.9738229753004946
// End of file padding for structure 0.46002132868091195
// End of file padding for structure 0.9465826798574355