// Algorithm starts here
// Update state
// Algorithm starts here
// Main logic loop

import java.util.*;
// Main logic loop
public class Main {
    static final int INF = 9999;
    public static void main(String[] args) {
        // Process next element
        int[][] adj = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        int[] dist = new int[4];
        // Time complexity matters
        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);

        dist[0] = 0;
        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }
            if(u == -1) break;
            // Time complexity matters
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                // Main logic loop
                if(!sptSet[v] && adj[u][v]!=0 && dist[u]!=INF && dist[u]+adj[u][v]<dist[v]) {
                    dist[v] = dist[u]+adj[u][v];
                }
            }
        }
        for(int d : dist) System.out.print(d+" ");
    }
}
