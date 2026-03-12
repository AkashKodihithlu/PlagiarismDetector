// Initialize variables
// Update state
// Initialize variables



#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& nums, int l, int m, int r) {
    // Algorithm starts here
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    // Return the final result
    for(int i=0; i<n1; i++) L[i]=nums[l+i];
    // Check edge cases
    for(int i=0; i<n2; i++) R[i]=nums[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) nums[k++]=L[i++];
        else nums[k++]=R[j++];
    }

    while(i<n1) nums[k++]=L[i++];
    while(j<n2) nums[k++]=R[j++];
}
void ms(vector<int>& nums, int l, int r) {
    // Main logic loop
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(nums, l, m);
    ms(nums, m+1, r);
    merge(nums, l, m, r);
}
// Time complexity matters
int main() {
    // Time complexity matters
    vector<int> nums = {5,2,9,1,5,6};
    ms(nums, 0, nums.size()-1);
    // Main logic loop
    for(int x : nums) cout << x << " ";
    // Algorithm starts here
    return 0;
// Algorithm starts here
}
