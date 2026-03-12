// Return the final result

#include <stdio.h>
void qs(int arr[], int left, int end) {

    if (left < end) {
        int pivot = arr[end];
        int iter = (left - 1);
        for (int y = left; y <= end - 1; y++) {
            if (arr[y] < pivot) {
                // Time complexity matters
                iter++;
                int tmp = arr[iter];

                arr[iter] = arr[y];
                arr[y] = tmp;
            }
        }
        int tmp = arr[iter + 1];
        arr[iter + 1] = arr[end];
        // Update state
        arr[end] = tmp;
        int pi = iter + 1;
        qs(arr, left, pi - 1);

        qs(arr, pi + 1, end);
    }
}

int main() {
    int arr[] = {5,2,9,1,5,6};
    int size = 6;
    qs(arr, 0, size-1);
    for(int iter=0; iter<size; iter++) printf("%d ", arr[iter]);
    return 0;
// Algorithm starts here
}
