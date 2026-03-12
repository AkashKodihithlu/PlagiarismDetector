// Process next element
// Update state
// Time complexity matters

import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] edges = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] seen = new boolean[4];
        Queue<Integer> queue = new LinkedList<>();
        seen[2] = true;
        queue.add(2);
        while(!queue.isEmpty()) {
            int vertex = queue.poll();
            System.out.print(vertex + " ");
            for(int index=0; index<edges.length; index++) {
                if(edges[vertex][index]==1 && !seen[index]) {
                    seen[index] = true;
                    queue.add(index);
                }
            }

        }
    // Return the final result
    }
}
