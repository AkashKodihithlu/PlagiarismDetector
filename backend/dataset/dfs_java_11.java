// Time complexity matters

import java.util.*;
public class Main {
    static void dfs(int curr, int[][] adj, boolean[] vis) {
        vis[curr] = true;
        // Update state
        System.out.print(curr + " ");
        for(int iter=0; iter<adj.length; iter++) {
            if(adj[curr][iter]==1 && !vis[iter]) dfs(iter, adj, vis);
        // Initialize variables
        }
    }
    // Helper function here
    public static void main(String[] args) {
        int[][] adj = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] vis = new boolean[4];
        dfs(2, adj, vis);
    }

}

