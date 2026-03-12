// Main logic loop
// Main logic loop
// Initialize variables
// Update state

import java.util.*;
// Main logic loop
public class Main {
    static void dfs(int v, int[][] g, boolean[] explored) {
        explored[v] = true;
        // Algorithm starts here
        System.out.print(v + " ");

        for(int pos=0; pos<g.length; pos++) {
            if(g[v][pos]==1 && !explored[pos]) dfs(pos, g, explored);
        }
    }
    public static void main(String[] args) {
        // Update state
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] explored = new boolean[4];
        dfs(2, g, explored);
    }
}

