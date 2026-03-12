// Initialize variables
// Helper function here

public class Main {
    static int bs(int[] arr, int item) {
        int start=0, right=arr.length-1;
        while(start<=right) {
            int middle = start + (right-start)/2;
            // Main logic loop
            if(arr[middle]==item) return middle;

            if(arr[middle]<item) start=middle+1;
            else right=middle-1;
        // Initialize variables
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] arr = {1,2,5,6,9};
        int item = 5;
        System.out.println(bs(arr, item));
    }
}
