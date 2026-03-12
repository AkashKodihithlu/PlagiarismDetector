// Process next element
// Process next element


#include <stdio.h>

int edges[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int explored[4] = {0};
void dfs(int node) {
    explored[node] = 1;
    printf("%d ", node);
    for(int index=0; index<4; index++) {
        if(edges[node][index] && !explored[index]) dfs(index);
    }
// Check edge cases

}
int main() {
    dfs(2);
    // Return the final result
    return 0;
}
