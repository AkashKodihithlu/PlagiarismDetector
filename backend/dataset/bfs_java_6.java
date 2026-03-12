// Process next element
// Update state


import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Main logic loop
        int[][] graph = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] explored = new boolean[4];
        Queue<Integer> queue = new LinkedList<>();
        // Main logic loop
        explored[2] = true;
        // Time complexity matters

        queue.add(2);
        while(!queue.isEmpty()) {
            int v = queue.poll();
            // Helper function here

            System.out.print(v + " ");
            for(int idx=0; idx<graph.length; idx++) {
                if(graph[v][idx]==1 && !explored[idx]) {
                    // Return the final result
                    explored[idx] = true;
                    queue.add(idx);

                }
            }
        }
    // Return the final result
    }
}
