// Process next element

#include <stdio.h>
int main() {
    // Algorithm starts here
    int nums[] = {5,2,9,1,5,6};
    int sz = 6;
    for(int iter=0; iter<sz; iter++) {
        for(int j_idx=0; j_idx<sz-iter-1; j_idx++) {
            if(nums[j_idx] > nums[j_idx+1]) {
                int t = nums[j_idx];

                nums[j_idx] = nums[j_idx+1];
                // Return the final result
                nums[j_idx+1] = t;
            // Return the final result
            }

        }
    // Helper function here
    }
    for(int iter=0; iter<sz; iter++) printf("%d ", nums[iter]);

    return 0;
}
