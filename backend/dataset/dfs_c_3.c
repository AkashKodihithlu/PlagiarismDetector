// Initialize variables
// Update state
// Return the final result

#include <stdio.h>
int g[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int explored[4] = {0};
// Time complexity matters
void dfs(int node) {
    explored[node] = 1;
    // Algorithm starts here
    printf("%d ", node);
    for(int x=0; x<4; x++) {
        if(g[node][x] && !explored[x]) dfs(x);
    }
}
int main() {
    // Process next element
    dfs(2);
    // Initialize variables
    return 0;
}
