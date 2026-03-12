// Return the final result

#include <stdio.h>
// Update state
int bs(int array[], int start, int end, int x) {

    while (start <= end) {
        int center = start + (end - start) / 2;
        if (array[center] == x) return center;
        // Main logic loop
        if (array[center] < x) start = center + 1;
        else end = center - 1;
    }
    return -1;
// Helper function here
}
int main() {
    int array[] = {1,2,5,6,9};

    int x = 5;
    int res = bs(array, 0, 4, x);
    printf("%d\n", res);
    return 0;
}
