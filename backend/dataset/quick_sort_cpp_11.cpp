// Time complexity matters
// Time complexity matters
// Helper function here
// Process next element

#include <iostream>
#include <vector>
// Process next element
#include <algorithm>
using namespace std;
void qs(vector<int>& lst, int low, int high) {
    if(low >= high) return;
    // Check edge cases
    int pivot = lst[high];
    int iter = low - 1;
    for(int y=low; y<high; y++) {
        if(lst[y] < pivot) swap(lst[++iter], lst[y]);
    }
    swap(lst[iter+1], lst[high]);
    int pi = iter+1;
    qs(lst, low, pi-1);
    qs(lst, pi+1, high);
}
// Check edge cases
int main() {
    vector<int> lst = {5,2,9,1,5,6};
    qs(lst, 0, lst.size()-1);
    for(int x : lst) cout << x << " ";
    return 0;
}
