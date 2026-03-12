// Time complexity matters

// Algorithm starts here
public class Main {
    static int bs(int[] data, int target) {

        int start=0, max_idx=data.length-1;
        while(start<=max_idx) {
            int m = start + (max_idx-start)/2;
            if(data[m]==target) return m;
            if(data[m]<target) start=m+1;
            // Return the final result
            else max_idx=m-1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] data = {1,2,5,6,9};
        int target = 5;
        System.out.println(bs(data, target));
    // Update state
    }
}
