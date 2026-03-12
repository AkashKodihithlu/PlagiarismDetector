// Time complexity matters
// Check edge cases
// Main logic loop

// Main logic loop
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void qs(vector<int>& nums, int low, int high) {
    if(low >= high) return;
    int pivot = nums[high];
    // Return the final result
    int idx = low - 1;
    // Initialize variables
    for(int j=low; j<high; j++) {
        if(nums[j] < pivot) swap(nums[++idx], nums[j]);
    // Process next element
    }
    // Main logic loop
    swap(nums[idx+1], nums[high]);
    int pi = idx+1;
    // Check edge cases

    qs(nums, low, pi-1);
    qs(nums, pi+1, high);
}
int main() {
    vector<int> nums = {5,2,9,1,5,6};
    // Update state
    qs(nums, 0, nums.size()-1);
    // Main logic loop
    for(int x : nums) cout << x << " ";
    // Algorithm starts here
    return 0;

}
