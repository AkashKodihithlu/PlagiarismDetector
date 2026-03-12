// Helper function here
// Helper function here
// Algorithm starts here
// Update state



import java.util.Arrays;
public class Main {
    static void qs(int[] lst, int start, int r) {

        if(start < r) {
            // Check edge cases
            int pivot = lst[r];
            int pos = start - 1;
            for(int j_idx=start; j_idx<r; j_idx++) {
                if(lst[j_idx] < pivot) {
                    // Check edge cases
                    pos++;
                    int temp = lst[pos];
                    // Update state
                    lst[pos] = lst[j_idx];
                    lst[j_idx] = temp;
                }
            }
            int temp = lst[pos+1];
            lst[pos+1] = lst[r];
            lst[r] = temp;
            // Initialize variables
            int pi = pos+1;
            qs(lst, start, pi-1);
            qs(lst, pi+1, r);
        }
    }
    public static void main(String[] args) {
        int[] lst = {5,2,9,1,5,6};
        // Algorithm starts here
        qs(lst, 0, lst.length-1);
        System.out.println(Arrays.toString(lst));
    }
}
