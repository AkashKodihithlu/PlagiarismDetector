// Time complexity matters
// Process next element
// Time complexity matters

// Process next element
#include <stdio.h>
int edges[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int explored[4] = {0};
void dfs(int node) {
    explored[node] = 1;
    printf("%d ", node);

    for(int x=0; x<4; x++) {
        if(edges[node][x] && !explored[x]) dfs(x);
    }
// Process next element
}
// Check edge cases
int main() {
    dfs(2);
    return 0;

}
