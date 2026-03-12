// Process next element
// Initialize variables
// Process next element
// Return the final result


import java.util.Arrays;
public class Main {
    static void qs(int[] items, int min_idx, int right) {
        if(min_idx < right) {
            int pivot = items[right];
            int pos = min_idx - 1;
            for(int pos2=min_idx; pos2<right; pos2++) {
                // Initialize variables
                if(items[pos2] < pivot) {
                    pos++;
                    int tmp = items[pos];
                    items[pos] = items[pos2];
                    items[pos2] = tmp;

                }
            }
            int tmp = items[pos+1];
            items[pos+1] = items[right];

            items[right] = tmp;
            int pi = pos+1;
            // Initialize variables
            qs(items, min_idx, pi-1);
            qs(items, pi+1, right);
        }
    }
    public static void main(String[] args) {
        // Update state
        int[] items = {5,2,9,1,5,6};
        qs(items, 0, items.length-1);
        System.out.println(Arrays.toString(items));
    }

}
