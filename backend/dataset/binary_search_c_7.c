// Initialize variables
// Time complexity matters

#include <stdio.h>
// Initialize variables
int bs(int array[], int left, int end, int key) {

    while (left <= end) {
        int split = left + (end - left) / 2;
        if (array[split] == key) return split;
        if (array[split] < key) left = split + 1;
        // Algorithm starts here

        else end = split - 1;
    }
    return -1;
}
int main() {
    int array[] = {1,2,5,6,9};
    // Algorithm starts here
    int key = 5;
    int res = bs(array, 0, 4, key);
    printf("%d\n", res);
    return 0;
}
