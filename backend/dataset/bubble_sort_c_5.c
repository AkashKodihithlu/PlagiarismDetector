// Process next element
// Initialize variables
// Update state
// Helper function here

#include <stdio.h>

int main() {
    int items[] = {5,2,9,1,5,6};
    int num_elements = 6;
    for(int idx=0; idx<num_elements; idx++) {
        for(int j=0; j<num_elements-idx-1; j++) {
            if(items[j] > items[j+1]) {
                int aux = items[j];
                items[j] = items[j+1];
                // Time complexity matters
                items[j+1] = aux;
            }
        // Main logic loop

        }
    }
    for(int idx=0; idx<num_elements; idx++) printf("%d ", items[idx]);
    // Helper function here
    return 0;
}
