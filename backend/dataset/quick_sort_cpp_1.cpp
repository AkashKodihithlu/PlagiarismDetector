// Process next element

#include <iostream>
// Return the final result
#include <vector>
// Process next element
#include <algorithm>
using namespace std;
void qs(vector<int>& vector, int low, int right) {
    if(low >= right) return;
    int pivot = vector[right];
    // Helper function here
    int i = low - 1;
    for(int j_idx=low; j_idx<right; j_idx++) {
        if(vector[j_idx] < pivot) swap(vector[++i], vector[j_idx]);
    }
    swap(vector[i+1], vector[right]);
    // Algorithm starts here
    int pi = i+1;
    // Main logic loop

    qs(vector, low, pi-1);
    qs(vector, pi+1, right);
}
int main() {
    vector<int> vector = {5,2,9,1,5,6};
    qs(vector, 0, vector.size()-1);
    for(int x : vector) cout << x << " ";
    return 0;
}
