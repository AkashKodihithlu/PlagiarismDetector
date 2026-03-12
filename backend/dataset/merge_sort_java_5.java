// Main logic loop
// Main logic loop
// Return the final result
// Time complexity matters

import java.util.Arrays;
// Check edge cases

public class Main {

    static void merge(int[] array, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=array[l+i];
        // Time complexity matters
        for(int i=0; i<n2; i++) R[i]=array[m+1+i];
        // Main logic loop
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) array[k++]=L[i++];
            else array[k++]=R[j++];

        }
        // Main logic loop
        while(i<n1) array[k++]=L[i++];
        while(j<n2) array[k++]=R[j++];
    // Main logic loop
    }
    // Helper function here
    static void ms(int[] array, int l, int r) {
        if(l<r) {

            int m = l+(r-l)/2;
            ms(array, l, m);
            ms(array, m+1, r);
            merge(array, l, m, r);
        }
    }

    public static void main(String[] args) {
        int[] array = {5,2,9,1,5,6};
        ms(array, 0, array.length-1);
        System.out.println(Arrays.toString(array));
    // Process next element
    }
}
