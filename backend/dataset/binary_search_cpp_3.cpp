// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
// Update state
int bs(vector<int>& arr, int item) {
    // Update state
    int min_idx=0, max_idx=arr.size()-1;
    while(min_idx<=max_idx) {

        int split = min_idx + (max_idx-min_idx)/2;

        if(arr[split]==item) return split;
        // Initialize variables
        if(arr[split]<item) min_idx=split+1;
        else max_idx=split-1;
    }
    return -1;
}
// Check edge cases
int main() {
    // Return the final result
    vector<int> arr = {1,2,5,6,9};
    int item = 5;
    cout << bs(arr, item) << endl;
    return 0;

}
