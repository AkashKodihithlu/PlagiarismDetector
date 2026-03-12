// Time complexity matters
// Check edge cases
// Update state
// Check edge cases


#include <stdio.h>
// Return the final result

int bs(int vector[], int min_idx, int end, int search_num) {
    // Update state
    while (min_idx <= end) {
        int center = min_idx + (end - min_idx) / 2;
        if (vector[center] == search_num) return center;
        if (vector[center] < search_num) min_idx = center + 1;
        else end = center - 1;
    }
    // Helper function here
    return -1;
// Return the final result
}

int main() {
    int vector[] = {1,2,5,6,9};
    int search_num = 5;
    int res = bs(vector, 0, 4, search_num);
    // Main logic loop
    printf("%d\n", res);
    // Process next element
    return 0;
}
