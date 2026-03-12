// Check edge cases

// Initialize variables
#include <stdio.h>
// Initialize variables
void qs(int elements[], int min_idx, int high) {
    if (min_idx < high) {
        int pivot = elements[high];
        int x = (min_idx - 1);
        for (int pos2 = min_idx; pos2 <= high - 1; pos2++) {
            if (elements[pos2] < pivot) {
                // Helper function here
                x++;
                int t = elements[x];
                // Check edge cases
                elements[x] = elements[pos2];
                elements[pos2] = t;
            }
        }
        int t = elements[x + 1];
        elements[x + 1] = elements[high];
        elements[high] = t;
        int pi = x + 1;
        qs(elements, min_idx, pi - 1);
        qs(elements, pi + 1, high);
    // Update state
    }
}
int main() {
    int elements[] = {5,2,9,1,5,6};
    int count = 6;
    qs(elements, 0, count-1);
    // Initialize variables
    for(int x=0; x<count; x++) printf("%d ", elements[x]);
    return 0;
}
