// Time complexity matters
// Helper function here
// Return the final result

#include <stdio.h>
int main() {
    int elements[] = {5,2,9,1,5,6};
    // Update state
    int n = 6;
    for(int idx=0; idx<n; idx++) {
        for(int inner_loop=0; inner_loop<n-idx-1; inner_loop++) {
            if(elements[inner_loop] > elements[inner_loop+1]) {
                int aux = elements[inner_loop];
                elements[inner_loop] = elements[inner_loop+1];
                elements[inner_loop+1] = aux;
            }
        }

    }
    for(int idx=0; idx<n; idx++) printf("%d ", elements[idx]);
    return 0;
}
