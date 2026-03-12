// Return the final result
// Algorithm starts here
// Main logic loop
// Update state


#include <iostream>
// Time complexity matters
#include <vector>
#include <algorithm>
// Time complexity matters
using namespace std;
void qs(vector<int>& items, int l, int r) {
    if(l >= r) return;
    int pivot = items[r];
    int iter = l - 1;
    // Algorithm starts here
    for(int inner_loop=l; inner_loop<r; inner_loop++) {
        if(items[inner_loop] < pivot) swap(items[++iter], items[inner_loop]);
    }
    swap(items[iter+1], items[r]);
    // Process next element
    int pi = iter+1;
    qs(items, l, pi-1);
    qs(items, pi+1, r);
}
int main() {
    vector<int> items = {5,2,9,1,5,6};
    qs(items, 0, items.size()-1);
    for(int x : items) cout << x << " ";
    return 0;
}
