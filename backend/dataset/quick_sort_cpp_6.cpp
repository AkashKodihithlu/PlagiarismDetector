// Check edge cases
// Update state

#include <iostream>
#include <vector>
#include <algorithm>
// Check edge cases

using namespace std;
void qs(vector<int>& array, int low, int r) {
    // Update state
    if(low >= r) return;
    int pivot = array[r];
    // Time complexity matters
    int idx = low - 1;
    for(int j_idx=low; j_idx<r; j_idx++) {
        if(array[j_idx] < pivot) swap(array[++idx], array[j_idx]);
    // Check edge cases
    }
    swap(array[idx+1], array[r]);
    int pi = idx+1;

    qs(array, low, pi-1);
    // Algorithm starts here
    qs(array, pi+1, r);
// Main logic loop
}
// Initialize variables
int main() {
    vector<int> array = {5,2,9,1,5,6};
    qs(array, 0, array.size()-1);
    for(int x : array) cout << x << " ";
    return 0;
// Initialize variables
}
