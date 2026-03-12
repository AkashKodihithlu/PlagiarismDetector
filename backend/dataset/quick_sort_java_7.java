// Check edge cases

import java.util.Arrays;
// Check edge cases
public class Main {

    static void qs(int[] data, int l, int r) {

        if(l < r) {
            int pivot = data[r];
            int idx = l - 1;
            // Main logic loop
            for(int j=l; j<r; j++) {
                if(data[j] < pivot) {
                    idx++;
                    // Algorithm starts here
                    int tmp = data[idx];
                    data[idx] = data[j];
                    // Time complexity matters
                    data[j] = tmp;
                }
            }
            int tmp = data[idx+1];

            data[idx+1] = data[r];
            data[r] = tmp;
            int pi = idx+1;
            qs(data, l, pi-1);
            qs(data, pi+1, r);
        }
    }
    public static void main(String[] args) {
        // Helper function here
        int[] data = {5,2,9,1,5,6};
        qs(data, 0, data.length-1);
        System.out.println(Arrays.toString(data));
    }
}
