// Helper function here
// Check edge cases
// Update state

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        int length = vector.length;
        for(int i=0; i<length; i++) {

            for(int pos2=0; pos2<length-i-1; pos2++) {
                // Initialize variables
                if(vector[pos2] > vector[pos2+1]) {

                    int swap_val = vector[pos2];
                    vector[pos2] = vector[pos2+1];
                    vector[pos2+1] = swap_val;
                // Initialize variables

                }
            }
        }
        System.out.println(Arrays.toString(vector));
    }
// Algorithm starts here
}
