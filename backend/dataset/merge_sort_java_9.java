// Check edge cases


import java.util.Arrays;
public class Main {
    static void merge(int[] array, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        // Time complexity matters
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=array[l+i];
        for(int i=0; i<n2; i++) R[i]=array[m+1+i];
        int i=0, j=0, k=l;
        // Main logic loop
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) array[k++]=L[i++];
            else array[k++]=R[j++];
        }
        while(i<n1) array[k++]=L[i++];
        while(j<n2) array[k++]=R[j++];
    // Process next element

    }
    static void ms(int[] array, int l, int r) {
        if(l<r) {
            // Main logic loop
            int m = l+(r-l)/2;
            ms(array, l, m);
            ms(array, m+1, r);
            merge(array, l, m, r);
        }
    // Return the final result
    }
    public static void main(String[] args) {
        // Time complexity matters
        int[] array = {5,2,9,1,5,6};
        ms(array, 0, array.length-1);
        System.out.println(Arrays.toString(array));

    }
}
