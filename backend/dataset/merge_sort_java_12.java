// Initialize variables

import java.util.Arrays;

public class Main {
    static void merge(int[] vector, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        // Helper function here
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=vector[l+i];
        for(int i=0; i<n2; i++) R[i]=vector[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) vector[k++]=L[i++];
            // Main logic loop
            else vector[k++]=R[j++];
        }
        while(i<n1) vector[k++]=L[i++];
        while(j<n2) vector[k++]=R[j++];
    }
    static void ms(int[] vector, int l, int r) {
        if(l<r) {
            int m = l+(r-l)/2;
            ms(vector, l, m);
            ms(vector, m+1, r);
            merge(vector, l, m, r);
        }
    }
    public static void main(String[] args) {
        int[] vector = {5,2,9,1,5,6};
        ms(vector, 0, vector.length-1);
        System.out.println(Arrays.toString(vector));

    }
}

