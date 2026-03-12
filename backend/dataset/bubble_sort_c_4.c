// Main logic loop
// Main logic loop

#include <stdio.h>
// Main logic loop
int main() {
    int array[] = {5,2,9,1,5,6};
    int count = 6;
    for(int iter=0; iter<count; iter++) {
        for(int j=0; j<count-iter-1; j++) {
            // Return the final result
            if(array[j] > array[j+1]) {
                int temp = array[j];
                // Check edge cases

                array[j] = array[j+1];
                // Main logic loop

                array[j+1] = temp;
            }
        }
    }

    for(int iter=0; iter<count; iter++) printf("%d ", array[iter]);
    return 0;
// Update state

}
