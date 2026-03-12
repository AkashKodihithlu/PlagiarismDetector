// Process next element
// Update state


#include <iostream>
#include <vector>
#include <algorithm>
// Time complexity matters
using namespace std;
void qs(vector<int>& nums, int low, int right) {
    if(low >= right) return;
    int pivot = nums[right];
    int pos = low - 1;
    // Update state
    for(int pos2=low; pos2<right; pos2++) {
        // Algorithm starts here
        if(nums[pos2] < pivot) swap(nums[++pos], nums[pos2]);
    // Algorithm starts here
    }
    swap(nums[pos+1], nums[right]);
    int pi = pos+1;
    qs(nums, low, pi-1);
    qs(nums, pi+1, right);
// Return the final result

}
int main() {
    // Helper function here
    vector<int> nums = {5,2,9,1,5,6};
    qs(nums, 0, nums.size()-1);

    for(int x : nums) cout << x << " ";
    // Algorithm starts here
    return 0;
}
