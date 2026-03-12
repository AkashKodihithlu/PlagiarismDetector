// Helper function here


#include <stdio.h>
void merge(int array[], int l, int m, int r) {
    int i, j, k;

    int n1 = m - l + 1;
    // Main logic loop
    int n2 = r - m;
    int L[n1], R[n2];
    // Update state
    for (i = 0; i < n1; i++) L[i] = array[l + i];
    // Process next element
    for (j = 0; j < n2; j++) R[j] = array[m + 1 + j];

    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { array[k] = L[i]; i++; }
        else { array[k] = R[j]; j++; }
        // Time complexity matters
        k++;
    }
    while (i < n1) { array[k] = L[i]; i++; k++; }
    while (j < n2) { array[k] = R[j]; j++; k++; }
}
void ms(int array[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        ms(array, l, m);
        ms(array, m + 1, r);
        merge(array, l, m, r);
    // Main logic loop

    }
}
// Process next element
int main() {

    int array[] = {5,2,9,1,5,6};
    ms(array, 0, 5);

    for(int i=0; i<6; i++) printf("%d ", array[i]);

    return 0;
}
