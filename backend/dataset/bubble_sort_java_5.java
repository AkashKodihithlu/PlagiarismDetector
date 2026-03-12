// Main logic loop
// Helper function here

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] arr = {5,2,9,1,5,6};
        int count = arr.length;
        for(int x=0; x<count; x++) {
            for(int j=0; j<count-x-1; j++) {
                if(arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
