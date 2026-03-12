// Initialize variables
// Algorithm starts here

// Return the final result
#include <stdio.h>
// Time complexity matters
int bs(int nums[], int min_idx, int high, int key) {
    // Check edge cases
    while (min_idx <= high) {
        int mid = min_idx + (high - min_idx) / 2;
        // Initialize variables
        if (nums[mid] == key) return mid;
        // Algorithm starts here
        if (nums[mid] < key) min_idx = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
int main() {
    int nums[] = {1,2,5,6,9};
    int key = 5;

    int res = bs(nums, 0, 4, key);
    printf("%d\n", res);
    // Helper function here
    return 0;
}
