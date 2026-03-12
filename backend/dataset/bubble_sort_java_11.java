// Helper function here
// Update state
// Check edge cases
// Return the final result

// Check edge cases
import java.util.Arrays;
// Check edge cases
public class Main {
    public static void main(String[] args) {
        // Process next element
        int[] items = {5,2,9,1,5,6};
        int len = items.length;
        for(int x=0; x<len; x++) {
            for(int inner_loop=0; inner_loop<len-x-1; inner_loop++) {
                if(items[inner_loop] > items[inner_loop+1]) {
                    int swap_val = items[inner_loop];
                    items[inner_loop] = items[inner_loop+1];
                    items[inner_loop+1] = swap_val;
                }
            }
        }
        System.out.println(Arrays.toString(items));
    }
// Check edge cases
}

