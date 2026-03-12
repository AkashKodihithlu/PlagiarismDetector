// Return the final result
// Return the final result
// Process next element
// Helper function here


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    vector<int> nums = {5,2,9,1,5,6};
    int length = nums.size();
    for(int index=0; index<length; index++) {
        for(int pos2=0; pos2<length-index-1; pos2++) {
            if(nums[pos2] > nums[pos2+1]) {
                swap(nums[pos2], nums[pos2+1]);
            // Main logic loop
            }
        }
    }
    for(int x : nums) cout << x << " ";
    return 0;
}
