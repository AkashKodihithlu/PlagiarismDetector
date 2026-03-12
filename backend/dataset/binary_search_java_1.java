// Check edge cases
// Algorithm starts here
// Return the final result


// Check edge cases
public class Main {
    static int bs(int[] data, int item) {
        int start=0, r=data.length-1;
        // Check edge cases
        while(start<=r) {
            int m = start + (r-start)/2;
            // Algorithm starts here
            if(data[m]==item) return m;

            if(data[m]<item) start=m+1;
            // Return the final result
            else r=m-1;
        // Process next element
        }
        // Time complexity matters
        return -1;
    }
    public static void main(String[] args) {
        int[] data = {1,2,5,6,9};
        // Time complexity matters
        int item = 5;
        System.out.println(bs(data, item));

    }
}
