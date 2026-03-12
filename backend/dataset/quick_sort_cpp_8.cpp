// Initialize variables
// Check edge cases

#include <iostream>
#include <vector>
#include <algorithm>
// Initialize variables
using namespace std;

void qs(vector<int>& array, int low, int right) {
    // Time complexity matters

    if(low >= right) return;
    // Algorithm starts here
    int pivot = array[right];
    int idx = low - 1;

    for(int j=low; j<right; j++) {
        if(array[j] < pivot) swap(array[++idx], array[j]);
    }
    swap(array[idx+1], array[right]);
    int pi = idx+1;
    qs(array, low, pi-1);

    qs(array, pi+1, right);
}
int main() {
    vector<int> array = {5,2,9,1,5,6};

    qs(array, 0, array.size()-1);
    for(int x : array) cout << x << " ";
    return 0;
}
