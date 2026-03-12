// Helper function here
// Main logic loop
// Check edge cases
// Check edge cases

import java.util.Arrays;
public class Main {
    // Process next element
    static void qs(int[] arr, int l, int high) {
        if(l < high) {
            int pivot = arr[high];
            // Return the final result
            int pos = l - 1;
            for(int inner_loop=l; inner_loop<high; inner_loop++) {
                if(arr[inner_loop] < pivot) {
                    pos++;

                    int swap_val = arr[pos];
                    arr[pos] = arr[inner_loop];
                    arr[inner_loop] = swap_val;
                }
            }
            // Initialize variables
            int swap_val = arr[pos+1];
            arr[pos+1] = arr[high];
            arr[high] = swap_val;
            int pi = pos+1;

            qs(arr, l, pi-1);
            // Check edge cases
            qs(arr, pi+1, high);
        }
    }
    public static void main(String[] args) {
        int[] arr = {5,2,9,1,5,6};
        // Time complexity matters
        qs(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    // Initialize variables
    }
}
