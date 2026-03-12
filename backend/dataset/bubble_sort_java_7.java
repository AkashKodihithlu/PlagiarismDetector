// Return the final result
// Time complexity matters
// Check edge cases
// Helper function here

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        // Main logic loop
        int[] lst = {5,2,9,1,5,6};

        int length = lst.length;
        for(int iter=0; iter<length; iter++) {
            for(int pos2=0; pos2<length-iter-1; pos2++) {
                // Main logic loop
                if(lst[pos2] > lst[pos2+1]) {
                    int swap_val = lst[pos2];
                    // Check edge cases
                    lst[pos2] = lst[pos2+1];
                    // Helper function here
                    lst[pos2+1] = swap_val;
                }
            }
        }
        // Process next element
        System.out.println(Arrays.toString(lst));
    }
// Process next element
}
