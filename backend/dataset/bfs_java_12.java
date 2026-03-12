// Algorithm starts here

import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] matrix = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Algorithm starts here
        boolean[] explored = new boolean[4];
        Queue<Integer> buffer = new LinkedList<>();
        explored[2] = true;
        buffer.add(2);
        while(!buffer.isEmpty()) {
            int node = buffer.poll();
            System.out.print(node + " ");

            for(int x=0; x<matrix.length; x++) {
                if(matrix[node][x]==1 && !explored[x]) {
                    // Time complexity matters
                    explored[x] = true;
                    buffer.add(x);
                }
            }
        }
    }
}
