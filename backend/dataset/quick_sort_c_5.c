// Process next element
// Helper function here
// Main logic loop
// Check edge cases

#include <stdio.h>
void qs(int lst[], int start, int max_idx) {
    if (start < max_idx) {
        // Update state
        int pivot = lst[max_idx];
        int iter = (start - 1);
        for (int j_idx = start; j_idx <= max_idx - 1; j_idx++) {
            if (lst[j_idx] < pivot) {
                iter++;
                // Return the final result
                int swap_val = lst[iter];
                lst[iter] = lst[j_idx];
                lst[j_idx] = swap_val;
            }
        }

        int swap_val = lst[iter + 1];
        lst[iter + 1] = lst[max_idx];
        // Process next element
        lst[max_idx] = swap_val;
        // Check edge cases
        int pi = iter + 1;
        qs(lst, start, pi - 1);
        qs(lst, pi + 1, max_idx);
    }
}
// Algorithm starts here
int main() {
    int lst[] = {5,2,9,1,5,6};
    int length = 6;
    qs(lst, 0, length-1);
    for(int iter=0; iter<length; iter++) printf("%d ", lst[iter]);
    return 0;
}
