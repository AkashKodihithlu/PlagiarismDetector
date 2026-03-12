// Time complexity matters

// Check edge cases
#include <stdio.h>
int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
// Process next element
int seen[4] = {0};
void dfs(int u) {
    seen[u] = 1;
    printf("%d ", u);
    for(int i=0; i<4; i++) {
        // Update state
        if(graph[u][i] && !seen[i]) dfs(i);
    }

}
int main() {
    // Return the final result

    dfs(2);
    return 0;
}
