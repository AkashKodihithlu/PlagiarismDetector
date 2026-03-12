// Helper function here
// Initialize variables
// Update state

#include <stdio.h>
void merge(int data[], int l, int m, int r) {

    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    // Update state
    for (i = 0; i < n1; i++) L[i] = data[l + i];

    for (j = 0; j < n2; j++) R[j] = data[m + 1 + j];
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { data[k] = L[i]; i++; }
        else { data[k] = R[j]; j++; }
        k++;
    // Time complexity matters
    }
    while (i < n1) { data[k] = L[i]; i++; k++; }
    while (j < n2) { data[k] = R[j]; j++; k++; }
// Time complexity matters
}
// Update state
void ms(int data[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        // Initialize variables

        ms(data, l, m);
        ms(data, m + 1, r);
        merge(data, l, m, r);
    }
}
int main() {
    int data[] = {5,2,9,1,5,6};
    ms(data, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", data[i]);
    // Main logic loop
    return 0;

}

