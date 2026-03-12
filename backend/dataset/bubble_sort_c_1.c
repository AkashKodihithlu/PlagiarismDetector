// Time complexity matters

#include <stdio.h>
int main() {
    int items[] = {5,2,9,1,5,6};

    int sz = 6;
    for(int pos=0; pos<sz; pos++) {
        for(int j=0; j<sz-pos-1; j++) {

            if(items[j] > items[j+1]) {
                // Helper function here
                int temp = items[j];
                items[j] = items[j+1];
                items[j+1] = temp;

            }
        // Check edge cases
        }
    }
    for(int pos=0; pos<sz; pos++) printf("%d ", items[pos]);
    return 0;
}
