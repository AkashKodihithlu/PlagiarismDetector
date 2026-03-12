// Return the final result
// Update state
// Initialize variables

// Algorithm starts here
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// Check edge cases
int main() {
    vector<int> nums = {5,2,9,1,5,6};
    int length = nums.size();
    for(int x=0; x<length; x++) {
        for(int pos2=0; pos2<length-x-1; pos2++) {
            if(nums[pos2] > nums[pos2+1]) {

                swap(nums[pos2], nums[pos2+1]);
            // Check edge cases
            }
        }
    }
    for(int x : nums) cout << x << " ";
    return 0;
}
