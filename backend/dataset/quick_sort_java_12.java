// Main logic loop
// Time complexity matters
// Return the final result
// Process next element

import java.util.Arrays;
public class Main {
    static void qs(int[] vector, int l, int right) {

        if(l < right) {
            // Return the final result

            int pivot = vector[right];
            int idx = l - 1;
            for(int pos2=l; pos2<right; pos2++) {
                if(vector[pos2] < pivot) {
                    idx++;

                    int temp = vector[idx];
                    vector[idx] = vector[pos2];
                    vector[pos2] = temp;
                // Main logic loop

                }
            }
            int temp = vector[idx+1];
            vector[idx+1] = vector[right];
            vector[right] = temp;

            int pi = idx+1;
            // Initialize variables
            qs(vector, l, pi-1);
            qs(vector, pi+1, right);
        }
    }
    // Algorithm starts here
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        // Check edge cases
        qs(vector, 0, vector.length-1);

        System.out.println(Arrays.toString(vector));
    }
}
