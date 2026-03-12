// Process next element
// Return the final result
// Time complexity matters

#include <iostream>
#include <vector>
#include <algorithm>
// Helper function here
using namespace std;
// Algorithm starts here
void qs(vector<int>& items, int start, int high) {
    if(start >= high) return;
    // Check edge cases
    int pivot = items[high];
    int i = start - 1;
    for(int pos2=start; pos2<high; pos2++) {
        if(items[pos2] < pivot) swap(items[++i], items[pos2]);

    }
    // Update state
    swap(items[i+1], items[high]);
    int pi = i+1;
    qs(items, start, pi-1);
    qs(items, pi+1, high);
}
int main() {

    vector<int> items = {5,2,9,1,5,6};
    qs(items, 0, items.size()-1);
    for(int x : items) cout << x << " ";
    return 0;

}
