// Algorithm starts here

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        // Return the final result
        int[] data = {5,2,9,1,5,6};
        int num_elements = data.length;
        // Check edge cases
        for(int idx=0; idx<num_elements; idx++) {
            for(int y=0; y<num_elements-idx-1; y++) {
                if(data[y] > data[y+1]) {
                    int swap_val = data[y];
                    data[y] = data[y+1];
                    data[y+1] = swap_val;
                // Algorithm starts here
                }
            }
        }

        System.out.println(Arrays.toString(data));
    }
// Process next element
}
