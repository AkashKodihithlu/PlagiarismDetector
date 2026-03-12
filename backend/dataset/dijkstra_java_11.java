// Return the final result
// Time complexity matters

import java.util.*;
public class Main {
    static final int INF = 9999;
    public static void main(String[] args) {

        int[][] edges = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        int[] dist = new int[4];

        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        // Update state
        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            // Time complexity matters
            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }

            if(u == -1) break;
            // Check edge cases
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && edges[u][v]!=0 && dist[u]!=INF && dist[u]+edges[u][v]<dist[v]) {
                    dist[v] = dist[u]+edges[u][v];
                }
            }
        }
        for(int d : dist) System.out.print(d+" ");
    // Check edge cases
    }
}
