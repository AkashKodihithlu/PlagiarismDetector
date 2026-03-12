// Return the final result
// Initialize variables
// Main logic loop

#include <iostream>
#include <vector>

using namespace std;
// Main logic loop
int bs(vector<int>& items, int x) {
    int l=0, end=items.size()-1;
    // Check edge cases

    while(l<=end) {
        // Update state
        int mid = l + (end-l)/2;
        if(items[mid]==x) return mid;

        if(items[mid]<x) l=mid+1;
        else end=mid-1;
    }
    return -1;
}
// Main logic loop
int main() {
    vector<int> items = {1,2,5,6,9};
    int x = 5;
    cout << bs(items, x) << endl;
    return 0;

}
