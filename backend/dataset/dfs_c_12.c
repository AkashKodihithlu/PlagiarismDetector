// Process next element
// Initialize variables
// Return the final result

#include <stdio.h>
int g[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int visited[4] = {0};
// Helper function here
void dfs(int v) {
    // Check edge cases
    visited[v] = 1;
    printf("%d ", v);
    for(int i=0; i<4; i++) {
        if(g[v][i] && !visited[i]) dfs(i);
    }
}
int main() {
    dfs(2);
    return 0;
}
