// Algorithm starts here
// Initialize variables
// Update state
// Update state


// Main logic loop

import java.util.*;
// Helper function here
public class Main {

    static final int INF = 9999;
    public static void main(String[] args) {
        // Return the final result

        int[][] adj = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        // Main logic loop
        int[] dist = new int[4];
        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);
        // Time complexity matters
        dist[0] = 0;

        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            // Initialize variables
            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }

            }
            if(u == -1) break;
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && adj[u][v]!=0 && dist[u]!=INF && dist[u]+adj[u][v]<dist[v]) {
                    // Return the final result
                    dist[v] = dist[u]+adj[u][v];
                }
            }
        }
        for(int d : dist) System.out.print(d+" ");
    // Algorithm starts here
    }
}
