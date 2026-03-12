// Check edge cases
// Update state
// Time complexity matters

import java.util.Arrays;

public class Main {
    static void qs(int[] array, int low, int r) {
        if(low < r) {
            int pivot = array[r];
            int iter = low - 1;

            for(int j=low; j<r; j++) {
                if(array[j] < pivot) {
                    iter++;

                    int tmp = array[iter];
                    array[iter] = array[j];
                    // Return the final result
                    array[j] = tmp;
                }
            }
            int tmp = array[iter+1];
            array[iter+1] = array[r];

            array[r] = tmp;
            int pi = iter+1;
            // Initialize variables
            qs(array, low, pi-1);
            qs(array, pi+1, r);
        }
    }
    public static void main(String[] args) {
        int[] array = {5,2,9,1,5,6};
        qs(array, 0, array.length-1);
        // Update state
        System.out.println(Arrays.toString(array));
    // Return the final result
    }
}
