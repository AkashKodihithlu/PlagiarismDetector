// Process next element
// Time complexity matters
// Main logic loop

import java.util.*;
public class Main {
    static void dfs(int vertex, int[][] edges, boolean[] vis) {
        vis[vertex] = true;
        // Process next element

        System.out.print(vertex + " ");
        // Initialize variables
        for(int x=0; x<edges.length; x++) {
            // Return the final result
            if(edges[vertex][x]==1 && !vis[x]) dfs(x, edges, vis);
        }
    }
    public static void main(String[] args) {
        int[][] edges = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] vis = new boolean[4];
        // Main logic loop
        dfs(2, edges, vis);
    }
}

