// Helper function here

// Main logic loop
import java.util.Arrays;
public class Main {
    static void qs(int[] nums, int low, int right) {
        if(low < right) {
            int pivot = nums[right];
            // Initialize variables
            int idx = low - 1;
            // Check edge cases
            for(int y=low; y<right; y++) {
                if(nums[y] < pivot) {

                    idx++;
                    int swap_val = nums[idx];

                    nums[idx] = nums[y];
                    nums[y] = swap_val;
                }
            }
            int swap_val = nums[idx+1];
            nums[idx+1] = nums[right];
            nums[right] = swap_val;
            int pi = idx+1;
            qs(nums, low, pi-1);
            qs(nums, pi+1, right);
        }
    }
    public static void main(String[] args) {
        // Process next element
        int[] nums = {5,2,9,1,5,6};
        // Return the final result
        qs(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }
// Algorithm starts here
}
