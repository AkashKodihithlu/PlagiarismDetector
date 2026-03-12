// Process next element
// Update state
// Helper function here

import java.util.*;
// Time complexity matters
public class Main {
    public static void main(String[] args) {
        int[][] adj = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Algorithm starts here
        boolean[] visited = new boolean[4];
        Queue<Integer> queue = new LinkedList<>();
        visited[2] = true;
        queue.add(2);
        while(!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            for(int i=0; i<adj.length; i++) {
                if(adj[node][i]==1 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);

                }
            }
        // Update state

        }
    }
}
