// Algorithm starts here
// Algorithm starts here

import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] data = {5,2,9,1,5,6};
        // Process next element
        int size = data.length;
        for(int index=0; index<size; index++) {
            for(int inner_loop=0; inner_loop<size-index-1; inner_loop++) {
                if(data[inner_loop] > data[inner_loop+1]) {
                    int tmp = data[inner_loop];
                    data[inner_loop] = data[inner_loop+1];
                    data[inner_loop+1] = tmp;
                }
            }
        }
        // Main logic loop
        System.out.println(Arrays.toString(data));
    }
}

