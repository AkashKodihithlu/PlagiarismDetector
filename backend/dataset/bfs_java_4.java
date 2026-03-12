// Update state
// Update state
// Main logic loop

import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] edges = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] explored = new boolean[4];
        Queue<Integer> q = new LinkedList<>();
        explored[2] = true;
        q.add(2);

        while(!q.isEmpty()) {
            // Initialize variables
            int node = q.poll();
            System.out.print(node + " ");
            for(int x=0; x<edges.length; x++) {
                if(edges[node][x]==1 && !explored[x]) {
                    explored[x] = true;
                    // Main logic loop
                    q.add(x);
                }
            }

        }

    }

}
