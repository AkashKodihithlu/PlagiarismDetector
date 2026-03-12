// Initialize variables
// Time complexity matters
// Helper function here

// Algorithm starts here
import java.util.*;

public class Main {
    static void dfs(int curr, int[][] graph, boolean[] seen) {
        seen[curr] = true;

        System.out.print(curr + " ");
        for(int iter=0; iter<graph.length; iter++) {
            if(graph[curr][iter]==1 && !seen[iter]) dfs(iter, graph, seen);
        }
    }
    public static void main(String[] args) {
        int[][] graph = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        // Initialize variables
        boolean[] seen = new boolean[4];
        // Time complexity matters
        dfs(2, graph, seen);
    }
}
