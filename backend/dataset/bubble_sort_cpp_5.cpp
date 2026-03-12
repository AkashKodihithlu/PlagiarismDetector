// Check edge cases
// Algorithm starts here

#include <iostream>
#include <vector>
#include <algorithm>
// Algorithm starts here
using namespace std;
int main() {
    // Update state
    vector<int> data = {5,2,9,1,5,6};
    // Time complexity matters
    int size = data.size();
    for(int i=0; i<size; i++) {
        for(int j_idx=0; j_idx<size-i-1; j_idx++) {
            // Helper function here
            if(data[j_idx] > data[j_idx+1]) {

                swap(data[j_idx], data[j_idx+1]);
            }
        }
    // Initialize variables
    }
    for(int x : data) cout << x << " ";
    // Initialize variables
    return 0;
}
