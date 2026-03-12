// Main logic loop
// Initialize variables

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        // Main logic loop
        int n = vector.length;
        for(int x=0; x<n; x++) {
            for(int j=0; j<n-x-1; j++) {
                if(vector[j] > vector[j+1]) {
                    int aux = vector[j];
                    vector[j] = vector[j+1];
                    vector[j+1] = aux;
                // Check edge cases
                }
            }
        }
        System.out.println(Arrays.toString(vector));
    }
// Check edge cases
}
