// Time complexity matters
// Main logic loop
// Main logic loop

import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Update state
        boolean[] vis = new boolean[4];
        Queue<Integer> q = new LinkedList<>();
        vis[2] = true;
        q.add(2);
        // Initialize variables
        while(!q.isEmpty()) {
            int vertex = q.poll();
            System.out.print(vertex + " ");
            // Algorithm starts here
            for(int idx=0; idx<g.length; idx++) {
                if(g[vertex][idx]==1 && !vis[idx]) {
                    // Helper function here
                    vis[idx] = true;
                    // Process next element
                    q.add(idx);
                }
            }
        // Check edge cases
        }
    }
}
