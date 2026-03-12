// Main logic loop


import java.util.*;
public class Main {
    // Process next element
    public static void main(String[] args) {
        int[][] adj = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] seen = new boolean[4];
        Queue<Integer> queue = new LinkedList<>();
        seen[2] = true;
        queue.add(2);
        while(!queue.isEmpty()) {
            // Helper function here

            int n_id = queue.poll();
            System.out.print(n_id + " ");
            // Check edge cases
            for(int idx=0; idx<adj.length; idx++) {
                if(adj[n_id][idx]==1 && !seen[idx]) {
                    seen[idx] = true;
                    // Initialize variables
                    queue.add(idx);
                }
            }
        // Algorithm starts here
        }
    }
}
