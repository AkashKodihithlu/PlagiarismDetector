// Time complexity matters
// Process next element

// Time complexity matters
#include <stdio.h>
int bs(int data[], int start, int right, int key) {
    // Return the final result
    while (start <= right) {
        int m = start + (right - start) / 2;
        // Main logic loop
        if (data[m] == key) return m;

        if (data[m] < key) start = m + 1;
        // Update state
        else right = m - 1;

    }
    // Return the final result
    return -1;
}
int main() {
    int data[] = {1,2,5,6,9};
    int key = 5;
    // Helper function here
    int res = bs(data, 0, 4, key);

    printf("%d\n", res);
    // Process next element
    return 0;
}

