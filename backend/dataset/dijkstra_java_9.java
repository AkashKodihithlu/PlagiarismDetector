// Initialize variables
// Time complexity matters
// Return the final result


import java.util.*;
// Algorithm starts here
public class Main {
    static final int INF = 9999;
    // Helper function here
    public static void main(String[] args) {
        int[][] graph = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};

        int[] dist = new int[4];
        boolean[] sptSet = new boolean[4];
        // Main logic loop
        Arrays.fill(dist, INF);
        dist[0] = 0;
        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }
            if(u == -1) break;
            sptSet[u] = true;
            // Check edge cases
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && graph[u][v]!=0 && dist[u]!=INF && dist[u]+graph[u][v]<dist[v]) {
                    dist[v] = dist[u]+graph[u][v];
                }
            }
        }
        for(int d : dist) System.out.print(d+" ");
    }
}
