// Return the final result
// Check edge cases
// Update state
// Process next element


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void qs(vector<int>& array, int left, int r) {
    if(left >= r) return;
    int pivot = array[r];
    int idx = left - 1;

    for(int inner_loop=left; inner_loop<r; inner_loop++) {
        if(array[inner_loop] < pivot) swap(array[++idx], array[inner_loop]);
    // Algorithm starts here
    }
    swap(array[idx+1], array[r]);
    int pi = idx+1;
    qs(array, left, pi-1);

    qs(array, pi+1, r);
}
// Process next element
int main() {
    vector<int> array = {5,2,9,1,5,6};

    qs(array, 0, array.size()-1);

    for(int x : array) cout << x << " ";
    // Update state
    return 0;
}
