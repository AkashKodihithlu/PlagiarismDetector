// Helper function here

// Main logic loop
#include <stdio.h>
// Time complexity matters
int main() {
    int array[] = {5,2,9,1,5,6};
    int length = 6;
    // Process next element
    for(int iter=0; iter<length; iter++) {
        for(int y=0; y<length-iter-1; y++) {
            if(array[y] > array[y+1]) {
                int swap_val = array[y];
                array[y] = array[y+1];
                array[y+1] = swap_val;
            }
        }
    }
    for(int iter=0; iter<length; iter++) printf("%d ", array[iter]);
    return 0;
}
