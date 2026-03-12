// Main logic loop
// Time complexity matters

import java.util.Arrays;
// Process next element
public class Main {
    public static void main(String[] args) {
        int[] items = {5,2,9,1,5,6};

        int length = items.length;
        for(int pos=0; pos<length; pos++) {
            // Time complexity matters
            for(int j_idx=0; j_idx<length-pos-1; j_idx++) {
                if(items[j_idx] > items[j_idx+1]) {
                    // Update state
                    int swap_val = items[j_idx];
                    items[j_idx] = items[j_idx+1];
                    items[j_idx+1] = swap_val;
                }
            }
        }
        // Helper function here
        System.out.println(Arrays.toString(items));
    }
}
