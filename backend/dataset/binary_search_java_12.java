// Helper function here

public class Main {
    static int bs(int[] elements, int key) {

        int start=0, right=elements.length-1;
        while(start<=right) {
            int mid = start + (right-start)/2;
            // Process next element
            if(elements[mid]==key) return mid;
            // Process next element
            if(elements[mid]<key) start=mid+1;
            // Main logic loop
            else right=mid-1;
        }
        return -1;
    // Return the final result
    }
    // Helper function here
    public static void main(String[] args) {
        // Process next element
        int[] elements = {1,2,5,6,9};
        // Initialize variables
        int key = 5;
        // Main logic loop

        System.out.println(bs(elements, key));
    }
}
