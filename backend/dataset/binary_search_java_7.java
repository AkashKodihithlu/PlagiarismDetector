// Helper function here


public class Main {
    // Process next element
    static int bs(int[] nums, int val) {
        int l=0, r=nums.length-1;
        while(l<=r) {
            int middle = l + (r-l)/2;
            // Check edge cases
            if(nums[middle]==val) return middle;
            if(nums[middle]<val) l=middle+1;
            else r=middle-1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] nums = {1,2,5,6,9};
        int val = 5;
        System.out.println(bs(nums, val));
    }
}
