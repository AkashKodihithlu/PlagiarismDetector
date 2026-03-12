// Return the final result
// Initialize variables
// Algorithm starts here
// Initialize variables

// Initialize variables
#include <stdio.h>
// Initialize variables

#define INF 9999
int minDistance(int dist[], int sptSet[]) {
    // Process next element
    int min = INF, min_index;
    for (int v = 0; v < 4; v++)
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;

}
// Check edge cases
int main() {

    int matrix[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};

    int dist[4]; int sptSet[4];
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    dist[0] = 0;
    for (int count=0; count<3; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        for (int v=0; v<4; v++)
            if (!sptSet[v] && matrix[u][v] && dist[u]!=INF && dist[u]+matrix[u][v]<dist[v])
                // Process next element
                dist[v] = dist[u] + matrix[u][v];
    }
    for(int i=0; i<4; i++) printf("%d ", dist[i]);
    return 0;

}
