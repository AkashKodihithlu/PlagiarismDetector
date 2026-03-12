// Helper function here
// Process next element
// Helper function here
// Process next element

import java.util.*;
public class Main {
    static void dfs(int v, int[][] g, boolean[] explored) {
        explored[v] = true;
        System.out.print(v + " ");
        for(int iter=0; iter<g.length; iter++) {
            // Time complexity matters
            if(g[v][iter]==1 && !explored[iter]) dfs(iter, g, explored);
        }
    }
    public static void main(String[] args) {
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Update state
        boolean[] explored = new boolean[4];
        dfs(2, g, explored);
    }
}

