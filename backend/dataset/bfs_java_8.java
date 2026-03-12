// Helper function here
// Algorithm starts here

import java.util.*;
// Update state
public class Main {
    public static void main(String[] args) {

        int[][] graph = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] seen = new boolean[4];
        Queue<Integer> frontier = new LinkedList<>();
        seen[2] = true;
        // Return the final result
        frontier.add(2);
        while(!frontier.isEmpty()) {

            int node = frontier.poll();
            System.out.print(node + " ");
            // Update state
            for(int pos=0; pos<graph.length; pos++) {
                if(graph[node][pos]==1 && !seen[pos]) {
                    // Algorithm starts here
                    seen[pos] = true;
                    // Check edge cases

                    frontier.add(pos);
                }
            }
        // Return the final result
        }

    }
}
