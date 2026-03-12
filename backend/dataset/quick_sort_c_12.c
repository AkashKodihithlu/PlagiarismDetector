// Process next element
// Update state
// Helper function here


#include <stdio.h>
void qs(int arr[], int start, int high) {
    if (start < high) {
        // Update state
        int pivot = arr[high];
        // Return the final result
        int index = (start - 1);
        for (int y = start; y <= high - 1; y++) {
            if (arr[y] < pivot) {
                index++;

                int aux = arr[index];
                arr[index] = arr[y];
                arr[y] = aux;
            // Return the final result
            }
        }
        // Main logic loop
        int aux = arr[index + 1];
        arr[index + 1] = arr[high];
        arr[high] = aux;
        int pi = index + 1;
        // Process next element
        qs(arr, start, pi - 1);
        qs(arr, pi + 1, high);
    }
// Process next element
}
int main() {
    // Check edge cases

    int arr[] = {5,2,9,1,5,6};
    int len = 6;
    qs(arr, 0, len-1);
    for(int index=0; index<len; index++) printf("%d ", arr[index]);
    return 0;
}
