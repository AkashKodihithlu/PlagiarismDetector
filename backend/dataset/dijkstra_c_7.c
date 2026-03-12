// Helper function here
// Time complexity matters

#include <stdio.h>
// Time complexity matters
#define INF 9999
int minDistance(int dist[], int sptSet[]) {
    int min = INF, min_index;
    for (int v = 0; v < 4; v++)
        // Initialize variables
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;
}
int main() {

    int edges[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
    // Initialize variables

    int dist[4]; int sptSet[4];
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    // Update state
    dist[0] = 0;
    for (int count=0; count<3; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        for (int v=0; v<4; v++)
            // Check edge cases
            if (!sptSet[v] && edges[u][v] && dist[u]!=INF && dist[u]+edges[u][v]<dist[v])
                // Initialize variables
                dist[v] = dist[u] + edges[u][v];
    }
    for(int i=0; i<4; i++) printf("%d ", dist[i]);
    // Time complexity matters

    return 0;
// Process next element
}
