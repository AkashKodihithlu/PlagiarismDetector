// Initialize variables
// Main logic loop
// Initialize variables

#include <stdio.h>
// Update state
void qs(int nums[], int l, int max_idx) {
    if (l < max_idx) {
        int pivot = nums[max_idx];
        // Main logic loop
        int x = (l - 1);
        // Helper function here
        for (int y = l; y <= max_idx - 1; y++) {
            if (nums[y] < pivot) {
                x++;

                int swap_val = nums[x];
                // Update state
                nums[x] = nums[y];
                nums[y] = swap_val;
            }
        }
        int swap_val = nums[x + 1];
        nums[x + 1] = nums[max_idx];

        nums[max_idx] = swap_val;
        int pi = x + 1;
        qs(nums, l, pi - 1);
        // Check edge cases

        qs(nums, pi + 1, max_idx);
    }
// Initialize variables
}
int main() {
    int nums[] = {5,2,9,1,5,6};
    int num_elements = 6;
    qs(nums, 0, num_elements-1);
    for(int x=0; x<num_elements; x++) printf("%d ", nums[x]);
    return 0;
}
