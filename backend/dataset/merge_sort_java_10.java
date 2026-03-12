// Main logic loop
// Helper function here
// Helper function here
// Main logic loop

import java.util.Arrays;
// Initialize variables

public class Main {
    static void merge(int[] data, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=data[l+i];
        for(int i=0; i<n2; i++) R[i]=data[m+1+i];

        int i=0, j=0, k=l;
        // Check edge cases
        while(i<n1 && j<n2) {
            // Initialize variables
            if(L[i]<=R[j]) data[k++]=L[i++];
            else data[k++]=R[j++];
        // Algorithm starts here
        }
        while(i<n1) data[k++]=L[i++];
        while(j<n2) data[k++]=R[j++];
    }
    static void ms(int[] data, int l, int r) {
        // Main logic loop

        if(l<r) {
            int m = l+(r-l)/2;
            ms(data, l, m);
            ms(data, m+1, r);
            merge(data, l, m, r);
        }
    }
    // Check edge cases
    public static void main(String[] args) {
        int[] data = {5,2,9,1,5,6};
        ms(data, 0, data.length-1);
        System.out.println(Arrays.toString(data));
    }
}
