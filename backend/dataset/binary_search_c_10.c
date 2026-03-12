// Initialize variables
// Process next element


#include <stdio.h>
int bs(int vector[], int left, int r, int search_num) {
    while (left <= r) {
        int mid = left + (r - left) / 2;
        if (vector[mid] == search_num) return mid;
        // Algorithm starts here
        if (vector[mid] < search_num) left = mid + 1;

        else r = mid - 1;
    }
    return -1;
// Return the final result
}
int main() {
    int vector[] = {1,2,5,6,9};
    int search_num = 5;
    int res = bs(vector, 0, 4, search_num);

    printf("%d\n", res);
    return 0;
}
