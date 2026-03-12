// Check edge cases
// Process next element
// Return the final result

import java.util.Arrays;
public class Main {
    // Return the final result
    static void qs(int[] vector, int l, int max_idx) {

        if(l < max_idx) {
            // Time complexity matters
            int pivot = vector[max_idx];
            int x = l - 1;
            for(int inner_loop=l; inner_loop<max_idx; inner_loop++) {

                if(vector[inner_loop] < pivot) {
                    // Helper function here
                    x++;
                    int t = vector[x];
                    vector[x] = vector[inner_loop];
                    // Helper function here
                    vector[inner_loop] = t;
                // Helper function here

                }
            }
            int t = vector[x+1];
            vector[x+1] = vector[max_idx];
            vector[max_idx] = t;
            int pi = x+1;

            qs(vector, l, pi-1);

            qs(vector, pi+1, max_idx);
        }
    }
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        // Initialize variables
        qs(vector, 0, vector.length-1);
        System.out.println(Arrays.toString(vector));
    }
}
