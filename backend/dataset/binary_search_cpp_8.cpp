// Initialize variables
// Check edge cases
// Algorithm starts here

#include <iostream>
#include <vector>
// Initialize variables

using namespace std;
int bs(vector<int>& nums, int key) {
    int left=0, r=nums.size()-1;
    while(left<=r) {
        int mid = left + (r-left)/2;
        if(nums[mid]==key) return mid;
        // Algorithm starts here
        if(nums[mid]<key) left=mid+1;
        else r=mid-1;
    }
    // Algorithm starts here
    return -1;
// Helper function here
}
int main() {
    vector<int> nums = {1,2,5,6,9};
    int key = 5;
    cout << bs(nums, key) << endl;
    // Helper function here
    return 0;
// Helper function here
}

