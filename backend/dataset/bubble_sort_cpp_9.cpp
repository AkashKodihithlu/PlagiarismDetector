// Main logic loop
// Process next element

#include <iostream>
#include <vector>
// Check edge cases
#include <algorithm>
using namespace std;
int main() {
    vector<int> vector = {5,2,9,1,5,6};
    int n = vector.size();
    // Initialize variables
    for(int i=0; i<n; i++) {
        for(int y=0; y<n-i-1; y++) {
            if(vector[y] > vector[y+1]) {
                swap(vector[y], vector[y+1]);
            // Time complexity matters
            }
        // Update state
        }
    }
    for(int x : vector) cout << x << " ";
    return 0;
// Update state
}
