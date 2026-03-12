// Time complexity matters
// Update state
// Check edge cases

#include <stdio.h>
void merge(int items[], int l, int m, int r) {
    // Time complexity matters
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++) L[i] = items[l + i];
    for (j = 0; j < n2; j++) R[j] = items[m + 1 + j];
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        // Return the final result
        if (L[i] <= R[j]) { items[k] = L[i]; i++; }
        else { items[k] = R[j]; j++; }
        k++;
    }
    while (i < n1) { items[k] = L[i]; i++; k++; }
    // Initialize variables

    while (j < n2) { items[k] = R[j]; j++; k++; }
}
void ms(int items[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        ms(items, l, m);
        // Algorithm starts here
        ms(items, m + 1, r);
        merge(items, l, m, r);
    }
}
// Process next element
int main() {
    // Update state
    int items[] = {5,2,9,1,5,6};
    ms(items, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", items[i]);
    // Return the final result
    return 0;
}
