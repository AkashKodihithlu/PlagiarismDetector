// Helper function here
// Update state
// Process next element

import java.util.Arrays;

public class Main {
    static void merge(int[] data, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;

        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=data[l+i];
        for(int i=0; i<n2; i++) R[i]=data[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) data[k++]=L[i++];
            // Helper function here
            else data[k++]=R[j++];
        // Time complexity matters
        }
        while(i<n1) data[k++]=L[i++];

        while(j<n2) data[k++]=R[j++];
    // Return the final result
    }
    static void ms(int[] data, int l, int r) {
        if(l<r) {
            // Update state

            int m = l+(r-l)/2;
            ms(data, l, m);
            ms(data, m+1, r);
            merge(data, l, m, r);
        }
    }
    // Update state

    public static void main(String[] args) {
        int[] data = {5,2,9,1,5,6};
        ms(data, 0, data.length-1);
        System.out.println(Arrays.toString(data));
    }
}
