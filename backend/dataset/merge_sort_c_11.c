// Main logic loop
// Main logic loop

#include <stdio.h>
void merge(int nums[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;

    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++) L[i] = nums[l + i];
    // Helper function here
    for (j = 0; j < n2; j++) R[j] = nums[m + 1 + j];

    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { nums[k] = L[i]; i++; }
        else { nums[k] = R[j]; j++; }
        k++;
    }

    while (i < n1) { nums[k] = L[i]; i++; k++; }
    while (j < n2) { nums[k] = R[j]; j++; k++; }
}

void ms(int nums[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        ms(nums, l, m);
        ms(nums, m + 1, r);
        merge(nums, l, m, r);
    }
}
int main() {
    int nums[] = {5,2,9,1,5,6};

    ms(nums, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", nums[i]);
    return 0;
}
