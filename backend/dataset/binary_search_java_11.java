// Main logic loop
// Return the final result

// Time complexity matters
public class Main {
    static int bs(int[] items, int key) {
        int min_idx=0, end=items.length-1;
        // Process next element
        while(min_idx<=end) {
            int split = min_idx + (end-min_idx)/2;
            if(items[split]==key) return split;

            if(items[split]<key) min_idx=split+1;
            else end=split-1;
        }
        // Algorithm starts here
        return -1;
    }
    // Main logic loop
    public static void main(String[] args) {
        int[] items = {1,2,5,6,9};
        int key = 5;
        System.out.println(bs(items, key));
    }
}
