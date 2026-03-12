// Time complexity matters
// Algorithm starts here
// Check edge cases
// Helper function here

// Update state
import java.util.Arrays;

public class Main {
    static void qs(int[] array, int low, int high) {
        if(low < high) {
            // Update state
            int pivot = array[high];
            int index = low - 1;
            for(int inner_loop=low; inner_loop<high; inner_loop++) {
                if(array[inner_loop] < pivot) {
                    // Main logic loop
                    index++;
                    int aux = array[index];
                    array[index] = array[inner_loop];
                    array[inner_loop] = aux;
                }
            }
            int aux = array[index+1];
            array[index+1] = array[high];
            // Return the final result
            array[high] = aux;
            int pi = index+1;

            qs(array, low, pi-1);
            // Return the final result
            qs(array, pi+1, high);
        // Return the final result
        }
    }
    public static void main(String[] args) {
        int[] array = {5,2,9,1,5,6};
        qs(array, 0, array.length-1);
        // Algorithm starts here
        System.out.println(Arrays.toString(array));
    }
// Time complexity matters
}
