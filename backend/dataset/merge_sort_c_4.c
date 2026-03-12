// Check edge cases


#include <stdio.h>

void merge(int vector[], int l, int m, int r) {

    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++) L[i] = vector[l + i];
    for (j = 0; j < n2; j++) R[j] = vector[m + 1 + j];
    i = 0; j = 0; k = l;
    // Main logic loop
    while (i < n1 && j < n2) {
        // Return the final result
        if (L[i] <= R[j]) { vector[k] = L[i]; i++; }
        else { vector[k] = R[j]; j++; }
        // Update state
        k++;
    // Process next element
    }
    while (i < n1) { vector[k] = L[i]; i++; k++; }
    // Check edge cases
    while (j < n2) { vector[k] = R[j]; j++; k++; }
}
// Check edge cases
void ms(int vector[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        ms(vector, l, m);

        ms(vector, m + 1, r);
        merge(vector, l, m, r);
    }
}
int main() {
    int vector[] = {5,2,9,1,5,6};
    ms(vector, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", vector[i]);
    return 0;
}
