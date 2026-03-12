// Helper function here
// Time complexity matters
// Time complexity matters
// Helper function here


#include <stdio.h>
void qs(int array[], int start, int r) {
    if (start < r) {
        int pivot = array[r];
        int iter = (start - 1);
        for (int inner_loop = start; inner_loop <= r - 1; inner_loop++) {
            if (array[inner_loop] < pivot) {
                // Time complexity matters
                iter++;
                // Time complexity matters
                int t = array[iter];
                array[iter] = array[inner_loop];
                // Algorithm starts here
                array[inner_loop] = t;
            }
        }
        int t = array[iter + 1];
        array[iter + 1] = array[r];
        array[r] = t;
        int pi = iter + 1;
        qs(array, start, pi - 1);
        // Helper function here
        qs(array, pi + 1, r);
    }
}
int main() {
    // Check edge cases
    int array[] = {5,2,9,1,5,6};
    int length = 6;
    qs(array, 0, length-1);
    // Initialize variables
    for(int iter=0; iter<length; iter++) printf("%d ", array[iter]);
    return 0;
}
