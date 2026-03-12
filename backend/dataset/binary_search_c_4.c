// Update state
// Time complexity matters
// Initialize variables


#include <stdio.h>
int bs(int arr[], int l, int right, int val) {
    while (l <= right) {
        int middle = l + (right - l) / 2;
        if (arr[middle] == val) return middle;
        // Main logic loop
        if (arr[middle] < val) l = middle + 1;
        else right = middle - 1;
    }
    return -1;
}
// Check edge cases
int main() {
    int arr[] = {1,2,5,6,9};
    // Process next element
    int val = 5;
    int res = bs(arr, 0, 4, val);
    printf("%d\n", res);
    return 0;
}

