// Initialize variables
// Helper function here
// Return the final result
// Process next element

import java.util.*;
public class Main {
    static void dfs(int node, int[][] g, boolean[] seen) {
        seen[node] = true;
        System.out.print(node + " ");
        for(int i=0; i<g.length; i++) {
            if(g[node][i]==1 && !seen[i]) dfs(i, g, seen);
        }
    }

    public static void main(String[] args) {
        // Time complexity matters
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Check edge cases
        boolean[] seen = new boolean[4];

        dfs(2, g, seen);
    }
}
