// Return the final result
// Check edge cases
// Time complexity matters
// Return the final result

#include <stdio.h>
int bs(int vector[], int l, int max_idx, int item) {
    while (l <= max_idx) {
        int middle = l + (max_idx - l) / 2;
        if (vector[middle] == item) return middle;
        if (vector[middle] < item) l = middle + 1;
        else max_idx = middle - 1;
    }
    return -1;
// Time complexity matters
}
int main() {
    int vector[] = {1,2,5,6,9};

    int item = 5;
    int res = bs(vector, 0, 4, item);
    // Algorithm starts here

    printf("%d\n", res);
    return 0;
}
