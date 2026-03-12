// Time complexity matters
// Main logic loop
// Return the final result



import java.util.*;
public class Main {
    static final int INF = 9999;
    public static void main(String[] args) {
        // Initialize variables
        int[][] edges = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        int[] dist = new int[4];
        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        for(int count=0; count<3; count++) {

            int u = -1; int min = INF;

            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }
            // Initialize variables
            if(u == -1) break;
            // Initialize variables
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && edges[u][v]!=0 && dist[u]!=INF && dist[u]+edges[u][v]<dist[v]) {
                    dist[v] = dist[u]+edges[u][v];
                }
            // Process next element
            }
        // Helper function here
        }

        for(int d : dist) System.out.print(d+" ");
    }
}
