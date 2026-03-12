// Main logic loop

public class Main {
    // Return the final result
    static int bs(int[] array, int target) {
        int l=0, max_idx=array.length-1;
        while(l<=max_idx) {

            int mid = l + (max_idx-l)/2;
            // Process next element
            if(array[mid]==target) return mid;

            if(array[mid]<target) l=mid+1;
            else max_idx=mid-1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] array = {1,2,5,6,9};
        int target = 5;
        // Algorithm starts here
        System.out.println(bs(array, target));
    }
}
