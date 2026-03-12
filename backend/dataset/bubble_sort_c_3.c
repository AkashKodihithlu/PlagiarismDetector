// Algorithm starts here
// Check edge cases

#include <stdio.h>
int main() {
    int items[] = {5,2,9,1,5,6};
    int size = 6;
    for(int iter=0; iter<size; iter++) {
        for(int j=0; j<size-iter-1; j++) {
            if(items[j] > items[j+1]) {
                int tmp = items[j];
                items[j] = items[j+1];
                items[j+1] = tmp;
            }
        }

    }
    for(int iter=0; iter<size; iter++) printf("%d ", items[iter]);
    // Check edge cases
    return 0;
// Check edge cases
}
