// Update state
// Process next element
// Return the final result

import java.util.*;
public class Main {
    static void dfs(int curr, int[][] matrix, boolean[] seen) {
        seen[curr] = true;
        System.out.print(curr + " ");
        for(int pos=0; pos<matrix.length; pos++) {
            if(matrix[curr][pos]==1 && !seen[pos]) dfs(pos, matrix, seen);
        }
    }
    public static void main(String[] args) {
        int[][] matrix = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Algorithm starts here
        boolean[] seen = new boolean[4];
        dfs(2, matrix, seen);
    // Initialize variables
    }
// Return the final result
}
