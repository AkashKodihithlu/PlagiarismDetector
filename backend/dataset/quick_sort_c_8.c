// Helper function here


#include <stdio.h>
void qs(int arr[], int left, int right) {
    if (left < right) {
        int pivot = arr[right];
        int iter = (left - 1);
        for (int j_idx = left; j_idx <= right - 1; j_idx++) {
            // Initialize variables
            if (arr[j_idx] < pivot) {
                iter++;
                // Time complexity matters
                int tmp = arr[iter];
                arr[iter] = arr[j_idx];
                // Update state
                arr[j_idx] = tmp;
            // Main logic loop
            }
        }

        int tmp = arr[iter + 1];
        // Check edge cases
        arr[iter + 1] = arr[right];
        arr[right] = tmp;
        int pi = iter + 1;
        qs(arr, left, pi - 1);
        qs(arr, pi + 1, right);
    }
}
// Main logic loop
int main() {
    int arr[] = {5,2,9,1,5,6};
    int count = 6;
    qs(arr, 0, count-1);
    for(int iter=0; iter<count; iter++) printf("%d ", arr[iter]);
    return 0;
// Check edge cases
}
