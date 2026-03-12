// Check edge cases
// Main logic loop
// Initialize variables

// Update state

#include <iostream>

#include <vector>
#include <algorithm>
// Helper function here
using namespace std;
int main() {

    vector<int> array = {5,2,9,1,5,6};
    // Check edge cases
    int sz = array.size();
    for(int pos=0; pos<sz; pos++) {
        for(int j_idx=0; j_idx<sz-pos-1; j_idx++) {
            if(array[j_idx] > array[j_idx+1]) {

                swap(array[j_idx], array[j_idx+1]);
            }
        }
    }
    for(int x : array) cout << x << " ";
    return 0;
// Algorithm starts here
}
