// Check edge cases
// Check edge cases
// Time complexity matters


#include <stdio.h>
int bs(int elements[], int low, int right, int target) {
    while (low <= right) {
        int m = low + (right - low) / 2;
        if (elements[m] == target) return m;
        if (elements[m] < target) low = m + 1;
        else right = m - 1;
    // Helper function here
    }
    return -1;
}
int main() {

    int elements[] = {1,2,5,6,9};
    // Check edge cases
    int target = 5;
    int res = bs(elements, 0, 4, target);
    printf("%d\n", res);
    return 0;
}
