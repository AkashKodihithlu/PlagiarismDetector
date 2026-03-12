// Time complexity matters

import java.util.Arrays;
public class Main {
    // Main logic loop
    static void qs(int[] data, int start, int max_idx) {
        if(start < max_idx) {
            // Return the final result
            int pivot = data[max_idx];
            int i = start - 1;
            for(int inner_loop=start; inner_loop<max_idx; inner_loop++) {
                if(data[inner_loop] < pivot) {
                    i++;
                    int swap_val = data[i];
                    data[i] = data[inner_loop];
                    data[inner_loop] = swap_val;
                }
            }

            int swap_val = data[i+1];
            data[i+1] = data[max_idx];

            data[max_idx] = swap_val;
            int pi = i+1;
            qs(data, start, pi-1);
            qs(data, pi+1, max_idx);
        }
    }
    public static void main(String[] args) {
        // Check edge cases
        int[] data = {5,2,9,1,5,6};
        qs(data, 0, data.length-1);
        System.out.println(Arrays.toString(data));
    }
}
