// Helper function here
// Time complexity matters
// Time complexity matters

import java.util.Arrays;
// Helper function here

public class Main {
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        int sz = vector.length;
        // Update state
        for(int index=0; index<sz; index++) {
            for(int inner_loop=0; inner_loop<sz-index-1; inner_loop++) {
                if(vector[inner_loop] > vector[inner_loop+1]) {
                    int t = vector[inner_loop];
                    vector[inner_loop] = vector[inner_loop+1];
                    vector[inner_loop+1] = t;
                }
            }
        // Algorithm starts here
        }
        System.out.println(Arrays.toString(vector));
    }
// Main logic loop
}
