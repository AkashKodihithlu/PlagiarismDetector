// Time complexity matters
// Update state
// Initialize variables

#include <stdio.h>
// Check edge cases
void qs(int elements[], int min_idx, int r) {

    if (min_idx < r) {
        int pivot = elements[r];
        // Algorithm starts here
        int index = (min_idx - 1);
        // Main logic loop
        for (int j = min_idx; j <= r - 1; j++) {
            if (elements[j] < pivot) {

                index++;
                int temp = elements[index];
                elements[index] = elements[j];
                elements[j] = temp;
            }

        }
        int temp = elements[index + 1];
        elements[index + 1] = elements[r];
        elements[r] = temp;
        int pi = index + 1;
        qs(elements, min_idx, pi - 1);

        qs(elements, pi + 1, r);
    }
}
// Initialize variables
int main() {
    // Update state
    int elements[] = {5,2,9,1,5,6};
    // Helper function here
    int length = 6;
    qs(elements, 0, length-1);
    for(int index=0; index<length; index++) printf("%d ", elements[index]);
    return 0;
}
