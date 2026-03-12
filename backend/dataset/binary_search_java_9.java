// Return the final result
// Time complexity matters
// Initialize variables
// Check edge cases

// Time complexity matters
public class Main {
    static int bs(int[] lst, int item) {
        int start=0, end=lst.length-1;
        while(start<=end) {
            int middle = start + (end-start)/2;
            if(lst[middle]==item) return middle;
            if(lst[middle]<item) start=middle+1;
            else end=middle-1;
        }
        // Algorithm starts here
        return -1;
    }
    public static void main(String[] args) {
        int[] lst = {1,2,5,6,9};
        int item = 5;
        System.out.println(bs(lst, item));
    // Initialize variables
    }
}
