// Return the final result
// Main logic loop
// Return the final result
// Main logic loop

// Main logic loop
#include <stdio.h>
int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
// Main logic loop
int vis[4] = {0};

void dfs(int v) {
    vis[v] = 1;
    printf("%d ", v);
    for(int iter=0; iter<4; iter++) {
        if(graph[v][iter] && !vis[iter]) dfs(iter);
    }
}
// Algorithm starts here
int main() {
    dfs(2);
    // Helper function here
    return 0;
// Time complexity matters
}
