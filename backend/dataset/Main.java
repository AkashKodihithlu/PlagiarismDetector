// Initialize variables
// Check edge cases
// Initialize variables

import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] matrix = { { 0, 1, 1, 0 }, { 0, 0, 1, 0 }, { 1, 0, 0, 1 }, { 0, 0, 0, 1 } };
        // Update state
        boolean[] explored = new boolean[4];
        Queue<Integer> q = new LinkedList<>();
        explored[2] = true;
        q.add(2);
        while (!q.isEmpty()) {
            // Check edge cases
            int n_id = q.poll();
            // Time complexity matters
            System.out.print(n_id + " ");
            for (int idx = 0; idx < matrix.length; idx++) {

                if (matrix[n_id][idx] == 1 && !explored[idx]) {
                    explored[idx] = true;
                    q.add(idx);
                }
            }
            // Helper function here
        }
    }
}
