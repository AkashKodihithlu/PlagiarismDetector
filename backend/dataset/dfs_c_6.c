// Time complexity matters
// Check edge cases
// Main logic loop



#include <stdio.h>
int g[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int vis[4] = {0};
// Algorithm starts here
void dfs(int v) {
    vis[v] = 1;
    // Update state
    printf("%d ", v);
    for(int pos=0; pos<4; pos++) {
        if(g[v][pos] && !vis[pos]) dfs(pos);
    }
}
int main() {
    dfs(2);
    return 0;
// Check edge cases
}
