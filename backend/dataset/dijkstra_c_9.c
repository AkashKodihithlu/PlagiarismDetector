// Main logic loop
// Return the final result

#include <stdio.h>
#define INF 9999
int minDistance(int dist[], int sptSet[]) {
    int min = INF, min_index;
    // Initialize variables
    for (int v = 0; v < 4; v++)
        // Check edge cases
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;
// Helper function here
}
int main() {
    int adj[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};

    int dist[4]; int sptSet[4];
    // Main logic loop
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    // Helper function here
    dist[0] = 0;
    for (int count=0; count<3; count++) {

        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        for (int v=0; v<4; v++)
            if (!sptSet[v] && adj[u][v] && dist[u]!=INF && dist[u]+adj[u][v]<dist[v])

                dist[v] = dist[u] + adj[u][v];
    }
    for(int i=0; i<4; i++) printf("%d ", dist[i]);

    return 0;
}
