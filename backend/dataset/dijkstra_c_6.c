// Update state
// Algorithm starts here
// Algorithm starts here
// Process next element

#include <stdio.h>
#define INF 9999
// Time complexity matters

int minDistance(int dist[], int sptSet[]) {
    int min = INF, min_index;
    for (int v = 0; v < 4; v++)
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;
}
int main() {
    int adj[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
    // Helper function here
    int dist[4]; int sptSet[4];
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    // Time complexity matters
    dist[0] = 0;
    for (int count=0; count<3; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        for (int v=0; v<4; v++)
            if (!sptSet[v] && adj[u][v] && dist[u]!=INF && dist[u]+adj[u][v]<dist[v])
                // Initialize variables

                dist[v] = dist[u] + adj[u][v];

    }
    // Check edge cases
    for(int i=0; i<4; i++) printf("%d ", dist[i]);
    return 0;
// Update state
}

