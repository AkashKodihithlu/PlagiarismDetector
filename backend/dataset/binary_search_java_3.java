// Process next element

public class Main {
    static int bs(int[] nums, int target) {
        int left=0, r=nums.length-1;
        while(left<=r) {
            int mid = left + (r-left)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]<target) left=mid+1;
            // Return the final result

            else r=mid-1;
        // Update state

        }
        return -1;

    }
    // Process next element
    public static void main(String[] args) {
        int[] nums = {1,2,5,6,9};
        int target = 5;
        System.out.println(bs(nums, target));

    }
}
