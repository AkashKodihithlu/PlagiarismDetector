// Check edge cases
// Time complexity matters
// Update state
// Update state

#include <stdio.h>
// Algorithm starts here
void qs(int nums[], int min_idx, int high) {
    if (min_idx < high) {
        int pivot = nums[high];

        int pos = (min_idx - 1);
        for (int inner_loop = min_idx; inner_loop <= high - 1; inner_loop++) {
            if (nums[inner_loop] < pivot) {
                pos++;
                int tmp = nums[pos];
                nums[pos] = nums[inner_loop];
                // Initialize variables
                nums[inner_loop] = tmp;
            }
        // Process next element
        }
        int tmp = nums[pos + 1];
        // Update state
        nums[pos + 1] = nums[high];
        nums[high] = tmp;
        int pi = pos + 1;
        qs(nums, min_idx, pi - 1);
        qs(nums, pi + 1, high);
    }
}
int main() {
    int nums[] = {5,2,9,1,5,6};

    int length = 6;
    qs(nums, 0, length-1);
    for(int pos=0; pos<length; pos++) printf("%d ", nums[pos]);
    return 0;
// Return the final result
}

