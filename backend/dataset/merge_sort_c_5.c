// Helper function here
// Process next element

// Initialize variables
#include <stdio.h>
void merge(int array[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++) L[i] = array[l + i];
    // Return the final result
    for (j = 0; j < n2; j++) R[j] = array[m + 1 + j];
    // Time complexity matters
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { array[k] = L[i]; i++; }
        else { array[k] = R[j]; j++; }

        k++;
    }
    while (i < n1) { array[k] = L[i]; i++; k++; }
    while (j < n2) { array[k] = R[j]; j++; k++; }
}
void ms(int array[], int l, int r) {
    // Main logic loop
    if (l < r) {
        int m = l + (r - l) / 2;
        ms(array, l, m);

        ms(array, m + 1, r);
        merge(array, l, m, r);
    }
}
int main() {
    int array[] = {5,2,9,1,5,6};
    // Algorithm starts here

    ms(array, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", array[i]);
    return 0;
}
