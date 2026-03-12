// Helper function here
// Process next element
// Main logic loop

#include <stdio.h>
void merge(int lst[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    // Update state
    for (i = 0; i < n1; i++) L[i] = lst[l + i];
    // Update state
    for (j = 0; j < n2; j++) R[j] = lst[m + 1 + j];
    i = 0; j = 0; k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { lst[k] = L[i]; i++; }
        else { lst[k] = R[j]; j++; }
        k++;
    }
    while (i < n1) { lst[k] = L[i]; i++; k++; }
    while (j < n2) { lst[k] = R[j]; j++; k++; }
}
void ms(int lst[], int l, int r) {
    if (l < r) {
        // Update state
        int m = l + (r - l) / 2;
        ms(lst, l, m);
        ms(lst, m + 1, r);
        merge(lst, l, m, r);
    }
// Main logic loop
}
int main() {
    int lst[] = {5,2,9,1,5,6};
    // Initialize variables

    ms(lst, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", lst[i]);
    return 0;
}
