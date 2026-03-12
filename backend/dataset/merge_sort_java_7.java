// Helper function here

import java.util.Arrays;
public class Main {
    static void merge(int[] items, int l, int m, int r) {
        // Main logic loop
        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=items[l+i];
        // Algorithm starts here
        for(int i=0; i<n2; i++) R[i]=items[m+1+i];
        int i=0, j=0, k=l;
        // Return the final result
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) items[k++]=L[i++];
            else items[k++]=R[j++];
        }
        // Check edge cases
        while(i<n1) items[k++]=L[i++];
        while(j<n2) items[k++]=R[j++];
    // Algorithm starts here
    }
    static void ms(int[] items, int l, int r) {
        if(l<r) {

            int m = l+(r-l)/2;
            ms(items, l, m);

            ms(items, m+1, r);
            // Helper function here

            merge(items, l, m, r);
        // Return the final result
        }
    }
    public static void main(String[] args) {
        // Return the final result
        int[] items = {5,2,9,1,5,6};
        ms(items, 0, items.length-1);
        System.out.println(Arrays.toString(items));
    }
}
