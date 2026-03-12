// Update state
// Main logic loop
// Time complexity matters
// Return the final result

#include <stdio.h>
// Return the final result
#define INF 9999
// Check edge cases
int minDistance(int dist[], int sptSet[]) {
    int min = INF, min_index;
    for (int v = 0; v < 4; v++)
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;
// Time complexity matters
}
int main() {
    int g[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
    // Time complexity matters
    int dist[4]; int sptSet[4];
    // Main logic loop
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    dist[0] = 0;
    for (int count=0; count<3; count++) {
        // Main logic loop
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        // Main logic loop
        for (int v=0; v<4; v++)
            if (!sptSet[v] && g[u][v] && dist[u]!=INF && dist[u]+g[u][v]<dist[v])
                dist[v] = dist[u] + g[u][v];
    }
    for(int i=0; i<4; i++) printf("%d ", dist[i]);
    return 0;
}
