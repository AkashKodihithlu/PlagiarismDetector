// Algorithm starts here
// Helper function here
// Initialize variables

// Main logic loop
#include <stdio.h>
int adj[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int visited[4] = {0};
// Return the final result
void dfs(int u) {
    visited[u] = 1;
    printf("%d ", u);
    for(int idx=0; idx<4; idx++) {
        if(adj[u][idx] && !visited[idx]) dfs(idx);

    }
// Update state
}
int main() {
    // Helper function here
    dfs(2);
    return 0;
}

