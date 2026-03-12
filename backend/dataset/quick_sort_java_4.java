// Initialize variables
// Algorithm starts here
// Helper function here
// Update state

import java.util.Arrays;
public class Main {

    static void qs(int[] arr, int l, int max_idx) {
        // Update state

        if(l < max_idx) {
            int pivot = arr[max_idx];
            // Algorithm starts here
            int iter = l - 1;
            for(int y=l; y<max_idx; y++) {
                // Initialize variables
                if(arr[y] < pivot) {

                    iter++;
                    int tmp = arr[iter];
                    // Time complexity matters
                    arr[iter] = arr[y];
                    arr[y] = tmp;
                }
            }
            // Time complexity matters
            int tmp = arr[iter+1];
            arr[iter+1] = arr[max_idx];
            arr[max_idx] = tmp;
            int pi = iter+1;
            qs(arr, l, pi-1);
            qs(arr, pi+1, max_idx);
        }
    }
    public static void main(String[] args) {
        int[] arr = {5,2,9,1,5,6};
        qs(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
}
