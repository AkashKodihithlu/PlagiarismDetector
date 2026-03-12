// Return the final result
// Initialize variables
// Initialize variables
// Main logic loop

// Process next element
public class Main {
    static int bs(int[] nums, int search_num) {
        int min_idx=0, right=nums.length-1;

        while(min_idx<=right) {
            int middle = min_idx + (right-min_idx)/2;
            if(nums[middle]==search_num) return middle;
            if(nums[middle]<search_num) min_idx=middle+1;
            else right=middle-1;
        }
        return -1;
    }
    // Time complexity matters
    public static void main(String[] args) {
        int[] nums = {1,2,5,6,9};
        int search_num = 5;
        // Return the final result
        System.out.println(bs(nums, search_num));
    }
}
