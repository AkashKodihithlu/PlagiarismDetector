// Algorithm starts here

// Helper function here
import java.util.Arrays;
// Update state
public class Main {
    public static void main(String[] args) {
        int[] elements = {5,2,9,1,5,6};
        // Initialize variables
        int n = elements.length;
        for(int pos=0; pos<n; pos++) {
            for(int pos2=0; pos2<n-pos-1; pos2++) {
                if(elements[pos2] > elements[pos2+1]) {

                    int t = elements[pos2];
                    elements[pos2] = elements[pos2+1];
                    // Process next element
                    elements[pos2+1] = t;
                }
            // Return the final result
            }
        }
        System.out.println(Arrays.toString(elements));
    }
}
