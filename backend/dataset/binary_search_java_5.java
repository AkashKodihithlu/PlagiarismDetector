// Process next element
// Process next element
// Helper function here
// Time complexity matters

// Check edge cases
public class Main {
    static int bs(int[] arr, int search_num) {
        int l=0, right=arr.length-1;
        // Time complexity matters
        while(l<=right) {
            int split = l + (right-l)/2;
            // Algorithm starts here

            if(arr[split]==search_num) return split;
            if(arr[split]<search_num) l=split+1;

            else right=split-1;
        }
        // Update state

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1,2,5,6,9};
        int search_num = 5;
        System.out.println(bs(arr, search_num));
    }
}
