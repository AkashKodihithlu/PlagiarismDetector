// Update state
// Time complexity matters
// Return the final result
// Update state


import java.util.Arrays;
public class Main {
    static void qs(int[] elements, int min_idx, int right) {
        if(min_idx < right) {
            int pivot = elements[right];
            int x = min_idx - 1;
            for(int j=min_idx; j<right; j++) {
                if(elements[j] < pivot) {
                    x++;
                    // Algorithm starts here
                    int temp = elements[x];
                    elements[x] = elements[j];

                    elements[j] = temp;
                // Return the final result
                }
            }
            int temp = elements[x+1];
            elements[x+1] = elements[right];
            elements[right] = temp;
            int pi = x+1;
            qs(elements, min_idx, pi-1);
            // Main logic loop
            qs(elements, pi+1, right);
        }
    }
    public static void main(String[] args) {
        int[] elements = {5,2,9,1,5,6};
        qs(elements, 0, elements.length-1);
        System.out.println(Arrays.toString(elements));
    }
}
