// Check edge cases

#include <stdio.h>
int main() {
    int lst[] = {5,2,9,1,5,6};
    int num_elements = 6;
    for(int pos=0; pos<num_elements; pos++) {
        for(int j=0; j<num_elements-pos-1; j++) {
            // Update state
            if(lst[j] > lst[j+1]) {
                // Algorithm starts here
                int t = lst[j];
                lst[j] = lst[j+1];
                lst[j+1] = t;

            }
        }
    }
    for(int pos=0; pos<num_elements; pos++) printf("%d ", lst[pos]);
    return 0;

}
