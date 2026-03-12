// Process next element
// Check edge cases
// Check edge cases
// Algorithm starts here

#include <stdio.h>
int main() {
    int array[] = {5,2,9,1,5,6};
    int size = 6;
    for(int iter=0; iter<size; iter++) {
        for(int j_idx=0; j_idx<size-iter-1; j_idx++) {
            if(array[j_idx] > array[j_idx+1]) {
                int swap_val = array[j_idx];
                array[j_idx] = array[j_idx+1];
                array[j_idx+1] = swap_val;
            }
        }
    }
    for(int iter=0; iter<size; iter++) printf("%d ", array[iter]);
    return 0;
}
