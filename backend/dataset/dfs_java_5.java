// Check edge cases

import java.util.*;
// Process next element
public class Main {
    static void dfs(int v, int[][] g, boolean[] visited) {
        // Time complexity matters
        visited[v] = true;

        System.out.print(v + " ");
        for(int index=0; index<g.length; index++) {
            if(g[v][index]==1 && !visited[index]) dfs(index, g, visited);

        }
    }
    public static void main(String[] args) {
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] visited = new boolean[4];
        dfs(2, g, visited);
    // Helper function here
    }
}
