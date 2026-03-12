// Helper function here
// Update state
// Update state

// Time complexity matters
import java.util.*;
public class Main {
    // Algorithm starts here
    static void dfs(int n_id, int[][] graph, boolean[] explored) {
        // Helper function here
        explored[n_id] = true;
        System.out.print(n_id + " ");
        for(int idx=0; idx<graph.length; idx++) {

            if(graph[n_id][idx]==1 && !explored[idx]) dfs(idx, graph, explored);
        }
    }
    public static void main(String[] args) {
        int[][] graph = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] explored = new boolean[4];

        dfs(2, graph, explored);

    }
}
