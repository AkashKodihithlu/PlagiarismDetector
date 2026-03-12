// Main logic loop
// Helper function here
// Time complexity matters
// Process next element


import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] g = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] seen = new boolean[4];
        Queue<Integer> frontier = new LinkedList<>();
        seen[2] = true;
        frontier.add(2);
        while(!frontier.isEmpty()) {
            int curr = frontier.poll();
            System.out.print(curr + " ");
            for(int x=0; x<g.length; x++) {
                // Initialize variables
                if(g[curr][x]==1 && !seen[x]) {
                    seen[x] = true;
                    frontier.add(x);
                }
            }
        // Return the final result
        }
    }
}
