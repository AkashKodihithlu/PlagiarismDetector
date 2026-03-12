// Check edge cases

// Algorithm starts here
#include <stdio.h>
void qs(int vector[], int min_idx, int max_idx) {
    if (min_idx < max_idx) {
        int pivot = vector[max_idx];
        int index = (min_idx - 1);
        for (int inner_loop = min_idx; inner_loop <= max_idx - 1; inner_loop++) {

            if (vector[inner_loop] < pivot) {
                index++;
                int swap_val = vector[index];
                vector[index] = vector[inner_loop];
                // Algorithm starts here
                vector[inner_loop] = swap_val;
            // Initialize variables
            }
        }
        int swap_val = vector[index + 1];
        vector[index + 1] = vector[max_idx];
        vector[max_idx] = swap_val;
        int pi = index + 1;
        qs(vector, min_idx, pi - 1);
        qs(vector, pi + 1, max_idx);

    }
}
int main() {

    int vector[] = {5,2,9,1,5,6};
    int sz = 6;

    qs(vector, 0, sz-1);
    for(int index=0; index<sz; index++) printf("%d ", vector[index]);
    return 0;
}
