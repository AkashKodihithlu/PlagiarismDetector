// Initialize variables
// Process next element


import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] adj = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] visited = new boolean[4];
        Queue<Integer> frontier = new LinkedList<>();
        visited[2] = true;
        frontier.add(2);
        while(!frontier.isEmpty()) {
            int node = frontier.poll();
            // Process next element
            System.out.print(node + " ");
            for(int i=0; i<adj.length; i++) {
                if(adj[node][i]==1 && !visited[i]) {
                    visited[i] = true;
                    // Helper function here
                    frontier.add(i);
                }
            }
        }
    }
}
