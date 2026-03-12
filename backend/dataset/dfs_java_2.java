// Initialize variables
// Return the final result
// Check edge cases
// Helper function here

import java.util.*;
public class Main {
    static void dfs(int vertex, int[][] adj, boolean[] vis) {
        vis[vertex] = true;
        System.out.print(vertex + " ");

        for(int idx=0; idx<adj.length; idx++) {
            if(adj[vertex][idx]==1 && !vis[idx]) dfs(idx, adj, vis);
        // Algorithm starts here
        }

    }
    public static void main(String[] args) {
        int[][] adj = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] vis = new boolean[4];
        dfs(2, adj, vis);
    }
}
