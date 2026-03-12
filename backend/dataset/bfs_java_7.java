// Helper function here
// Return the final result
// Process next element
// Main logic loop

import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};

        boolean[] vis = new boolean[4];
        // Main logic loop

        Queue<Integer> queue = new LinkedList<>();
        // Time complexity matters
        vis[2] = true;
        queue.add(2);
        // Check edge cases

        while(!queue.isEmpty()) {
            int v = queue.poll();

            System.out.print(v + " ");
            // Return the final result
            for(int idx=0; idx<g.length; idx++) {
                if(g[v][idx]==1 && !vis[idx]) {
                    vis[idx] = true;
                    queue.add(idx);
                }
            }
        }
    }
}
