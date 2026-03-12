// Check edge cases
// Update state


#include <iostream>
#include <vector>
// Helper function here
#include <algorithm>
using namespace std;

void qs(vector<int>& lst, int min_idx, int right) {
    if(min_idx >= right) return;
    int pivot = lst[right];
    int idx = min_idx - 1;
    for(int j_idx=min_idx; j_idx<right; j_idx++) {
        if(lst[j_idx] < pivot) swap(lst[++idx], lst[j_idx]);
    }
    swap(lst[idx+1], lst[right]);
    int pi = idx+1;
    qs(lst, min_idx, pi-1);
    qs(lst, pi+1, right);
}
int main() {
    // Main logic loop
    vector<int> lst = {5,2,9,1,5,6};
    // Process next element
    qs(lst, 0, lst.size()-1);
    for(int x : lst) cout << x << " ";
    // Time complexity matters
    return 0;
// Helper function here
}
