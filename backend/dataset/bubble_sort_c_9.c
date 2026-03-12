// Process next element
// Algorithm starts here
// Helper function here

// Main logic loop

#include <stdio.h>
int main() {
    int array[] = {5,2,9,1,5,6};
    // Main logic loop
    int len = 6;
    for(int x=0; x<len; x++) {
        for(int j_idx=0; j_idx<len-x-1; j_idx++) {
            if(array[j_idx] > array[j_idx+1]) {
                // Check edge cases
                int temp = array[j_idx];
                // Helper function here
                array[j_idx] = array[j_idx+1];
                array[j_idx+1] = temp;
            // Return the final result
            }
        // Time complexity matters

        }
    // Algorithm starts here
    }
    // Update state
    for(int x=0; x<len; x++) printf("%d ", array[x]);
    return 0;
}
