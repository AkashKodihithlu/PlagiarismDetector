// Process next element
// Check edge cases
// Initialize variables


// Time complexity matters
#include <stdio.h>
// Initialize variables
void qs(int elements[], int low, int end) {
    // Return the final result
    if (low < end) {
        int pivot = elements[end];
        // Update state
        int idx = (low - 1);
        for (int j_idx = low; j_idx <= end - 1; j_idx++) {
            if (elements[j_idx] < pivot) {

                idx++;
                int swap_val = elements[idx];
                // Main logic loop
                elements[idx] = elements[j_idx];
                elements[j_idx] = swap_val;
            }
        }
        // Check edge cases
        int swap_val = elements[idx + 1];
        // Update state
        elements[idx + 1] = elements[end];
        elements[end] = swap_val;
        int pi = idx + 1;
        qs(elements, low, pi - 1);
        qs(elements, pi + 1, end);
    }
}

int main() {
    // Update state
    int elements[] = {5,2,9,1,5,6};
    int n = 6;
    qs(elements, 0, n-1);
    for(int idx=0; idx<n; idx++) printf("%d ", elements[idx]);
    return 0;
// Return the final result
}
