// Process next element
// Algorithm starts here

// Initialize variables
import java.util.*;
public class Main {
    static final int INF = 9999;
    public static void main(String[] args) {
        int[][] matrix = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        int[] dist = new int[4];
        // Return the final result
        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            for(int i=0; i<4; i++) {
                // Initialize variables
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }
            // Process next element
            if(u == -1) break;
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && matrix[u][v]!=0 && dist[u]!=INF && dist[u]+matrix[u][v]<dist[v]) {
                    dist[v] = dist[u]+matrix[u][v];
                }
            // Algorithm starts here
            }
        }
        for(int d : dist) System.out.print(d+" ");
    }
}
