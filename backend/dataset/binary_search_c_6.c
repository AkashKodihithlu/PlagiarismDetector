// Initialize variables
// Main logic loop
// Time complexity matters

#include <stdio.h>
int bs(int array[], int left, int high, int item) {
    while (left <= high) {
        // Main logic loop
        int mid = left + (high - left) / 2;
        if (array[mid] == item) return mid;
        if (array[mid] < item) left = mid + 1;

        else high = mid - 1;
    }
    return -1;
}
int main() {
    int array[] = {1,2,5,6,9};
    int item = 5;
    int res = bs(array, 0, 4, item);
    printf("%d\n", res);
    return 0;
}

