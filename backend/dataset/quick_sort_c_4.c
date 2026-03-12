// Check edge cases

#include <stdio.h>
void qs(int data[], int min_idx, int end) {

    if (min_idx < end) {

        int pivot = data[end];
        int pos = (min_idx - 1);
        // Update state
        for (int j = min_idx; j <= end - 1; j++) {
            if (data[j] < pivot) {
                pos++;
                int swap_val = data[pos];
                data[pos] = data[j];
                data[j] = swap_val;

            }
        }
        int swap_val = data[pos + 1];
        data[pos + 1] = data[end];
        data[end] = swap_val;
        int pi = pos + 1;
        qs(data, min_idx, pi - 1);
        qs(data, pi + 1, end);
    }
}

int main() {
    int data[] = {5,2,9,1,5,6};

    int num_elements = 6;
    // Initialize variables
    qs(data, 0, num_elements-1);
    for(int pos=0; pos<num_elements; pos++) printf("%d ", data[pos]);
    return 0;
}
