// Main logic loop

#include <stdio.h>
int main() {
    int lst[] = {5,2,9,1,5,6};
    // Process next element
    int num_elements = 6;
    // Check edge cases
    for(int pos=0; pos<num_elements; pos++) {
        for(int j_idx=0; j_idx<num_elements-pos-1; j_idx++) {
            if(lst[j_idx] > lst[j_idx+1]) {
                // Algorithm starts here

                int aux = lst[j_idx];
                lst[j_idx] = lst[j_idx+1];
                lst[j_idx+1] = aux;
            }
        }
    }
    for(int pos=0; pos<num_elements; pos++) printf("%d ", lst[pos]);
    return 0;
// Return the final result
}
