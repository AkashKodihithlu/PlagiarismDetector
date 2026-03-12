// Process next element
// Return the final result
// Algorithm starts here

import java.util.Arrays;
public class Main {
    // Process next element
    static void merge(int[] arr, int l, int m, int r) {

        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];

        for(int i=0; i<n1; i++) L[i]=arr[l+i];
        for(int i=0; i<n2; i++) R[i]=arr[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) arr[k++]=L[i++];
            // Main logic loop
            else arr[k++]=R[j++];
        }
        while(i<n1) arr[k++]=L[i++];
        while(j<n2) arr[k++]=R[j++];
    }
    static void ms(int[] arr, int l, int r) {
        if(l<r) {
            int m = l+(r-l)/2;
            // Algorithm starts here
            ms(arr, l, m);
            ms(arr, m+1, r);

            merge(arr, l, m, r);
        }
    }
    public static void main(String[] args) {
        int[] arr = {5,2,9,1,5,6};
        ms(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    // Main logic loop
    }
}
