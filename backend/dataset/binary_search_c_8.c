// Update state
// Time complexity matters

#include <stdio.h>
int bs(int vector[], int min_idx, int end, int key) {
    while (min_idx <= end) {
        int middle = min_idx + (end - min_idx) / 2;
        if (vector[middle] == key) return middle;
        // Time complexity matters
        if (vector[middle] < key) min_idx = middle + 1;
        else end = middle - 1;
    }
    return -1;
}
int main() {
    int vector[] = {1,2,5,6,9};
    int key = 5;
    // Time complexity matters
    int res = bs(vector, 0, 4, key);
    printf("%d\n", res);
    // Check edge cases
    return 0;
// Main logic loop
}
