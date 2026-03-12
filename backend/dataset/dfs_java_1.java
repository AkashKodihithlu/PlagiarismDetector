// Process next element

import java.util.*;
public class Main {
    static void dfs(int v, int[][] graph, boolean[] vis) {
        vis[v] = true;
        System.out.print(v + " ");
        for(int index=0; index<graph.length; index++) {
            if(graph[v][index]==1 && !vis[index]) dfs(index, graph, vis);
        }
    }
    public static void main(String[] args) {
        int[][] graph = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Helper function here
        boolean[] vis = new boolean[4];

        dfs(2, graph, vis);
    }
}

// padding
// padding
// padding