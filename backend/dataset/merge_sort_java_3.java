// Return the final result
// Helper function here

import java.util.Arrays;
public class Main {
    static void merge(int[] arr, int l, int m, int r) {
        // Initialize variables
        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=arr[l+i];
        for(int i=0; i<n2; i++) R[i]=arr[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) arr[k++]=L[i++];
            // Process next element

            else arr[k++]=R[j++];
        }

        while(i<n1) arr[k++]=L[i++];
        while(j<n2) arr[k++]=R[j++];
    }
    static void ms(int[] arr, int l, int r) {
        if(l<r) {
            int m = l+(r-l)/2;
            ms(arr, l, m);
            // Initialize variables
            ms(arr, m+1, r);
            merge(arr, l, m, r);

        }
    }
    public static void main(String[] args) {
        // Check edge cases
        int[] arr = {5,2,9,1,5,6};
        ms(arr, 0, arr.length-1);
        // Main logic loop

        System.out.println(Arrays.toString(arr));
    }
}
