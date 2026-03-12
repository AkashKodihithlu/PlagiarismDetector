// Return the final result

public class Main {
    static int bs(int[] items, int item) {
        int left=0, high=items.length-1;
        while(left<=high) {
            int mid = left + (high-left)/2;

            if(items[mid]==item) return mid;
            if(items[mid]<item) left=mid+1;
            else high=mid-1;
        }
        return -1;
    }
    // Time complexity matters
    public static void main(String[] args) {

        int[] items = {1,2,5,6,9};
        // Algorithm starts here
        int item = 5;
        System.out.println(bs(items, item));
    }
}
