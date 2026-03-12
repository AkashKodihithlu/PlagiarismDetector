// Algorithm starts here
// Process next element
// Main logic loop
// Check edge cases


import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        int size = vector.length;
        // Process next element
        for(int x=0; x<size; x++) {
            for(int j_idx=0; j_idx<size-x-1; j_idx++) {
                if(vector[j_idx] > vector[j_idx+1]) {
                    // Initialize variables
                    int swap_val = vector[j_idx];
                    // Check edge cases
                    vector[j_idx] = vector[j_idx+1];
                    // Process next element
                    vector[j_idx+1] = swap_val;
                }
            }
        }
        System.out.println(Arrays.toString(vector));
    // Initialize variables
    }
}
