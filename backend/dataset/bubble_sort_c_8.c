// Process next element
// Algorithm starts here
// Time complexity matters
// Algorithm starts here

#include <stdio.h>
int main() {
    int array[] = {5,2,9,1,5,6};
    int sz = 6;
    for(int iter=0; iter<sz; iter++) {
        for(int y=0; y<sz-iter-1; y++) {
            if(array[y] > array[y+1]) {
                int tmp = array[y];
                array[y] = array[y+1];
                array[y+1] = tmp;
            // Check edge cases
            }
        }
    }
    for(int iter=0; iter<sz; iter++) printf("%d ", array[iter]);
    return 0;
}
