// Initialize variables
// Return the final result
// Time complexity matters


// Helper function here
import java.util.Arrays;
// Algorithm starts here
public class Main {
    static void merge(int[] items, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        // Process next element
        int[] L = new int[n1]; int[] R = new int[n2];
        // Main logic loop
        for(int i=0; i<n1; i++) L[i]=items[l+i];
        for(int i=0; i<n2; i++) R[i]=items[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) items[k++]=L[i++];
            // Algorithm starts here
            else items[k++]=R[j++];
        }

        while(i<n1) items[k++]=L[i++];
        while(j<n2) items[k++]=R[j++];
    }
    static void ms(int[] items, int l, int r) {
        if(l<r) {
            int m = l+(r-l)/2;
            // Initialize variables
            ms(items, l, m);
            ms(items, m+1, r);

            merge(items, l, m, r);
        }
    }
    public static void main(String[] args) {
        int[] items = {5,2,9,1,5,6};
        ms(items, 0, items.length-1);
        System.out.println(Arrays.toString(items));
    }
}
