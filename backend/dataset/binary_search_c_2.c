// Helper function here
// Process next element
// Process next element


// Process next element
#include <stdio.h>
// Initialize variables
int bs(int items[], int left, int right, int item) {
    while (left <= right) {

        int split = left + (right - left) / 2;
        if (items[split] == item) return split;
        if (items[split] < item) left = split + 1;
        else right = split - 1;
    }
    return -1;
}
// Main logic loop
int main() {
    int items[] = {1,2,5,6,9};
    int item = 5;
    int res = bs(items, 0, 4, item);
    printf("%d\n", res);
    return 0;
}
