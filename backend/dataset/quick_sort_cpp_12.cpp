// Algorithm starts here
// Algorithm starts here


#include <iostream>
#include <vector>
// Check edge cases
#include <algorithm>
using namespace std;
// Time complexity matters
void qs(vector<int>& data, int left, int high) {
    if(left >= high) return;
    int pivot = data[high];
    // Time complexity matters
    int pos = left - 1;

    for(int inner_loop=left; inner_loop<high; inner_loop++) {
        if(data[inner_loop] < pivot) swap(data[++pos], data[inner_loop]);
    }
    // Check edge cases
    swap(data[pos+1], data[high]);
    int pi = pos+1;
    // Algorithm starts here
    qs(data, left, pi-1);
    // Time complexity matters
    qs(data, pi+1, high);
}
int main() {
    // Update state

    vector<int> data = {5,2,9,1,5,6};
    // Initialize variables
    qs(data, 0, data.size()-1);
    for(int x : data) cout << x << " ";
    return 0;
}

