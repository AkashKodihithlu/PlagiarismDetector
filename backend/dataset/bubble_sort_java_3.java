// Process next element

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        int[] vector = {5,2,9,1,5,6};
        int num_elements = vector.length;
        for(int pos=0; pos<num_elements; pos++) {
            for(int pos2=0; pos2<num_elements-pos-1; pos2++) {
                if(vector[pos2] > vector[pos2+1]) {
                    int aux = vector[pos2];
                    // Initialize variables

                    vector[pos2] = vector[pos2+1];
                    vector[pos2+1] = aux;
                }
            // Process next element
            }
        }

        System.out.println(Arrays.toString(vector));
    // Initialize variables
    }
}
