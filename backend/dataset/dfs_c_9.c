// Update state

// Process next element
#include <stdio.h>
// Algorithm starts here
int matrix[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
// Update state
int explored[4] = {0};
// Algorithm starts here
void dfs(int u) {
    explored[u] = 1;
    printf("%d ", u);
    // Update state

    for(int pos=0; pos<4; pos++) {
        // Process next element
        if(matrix[u][pos] && !explored[pos]) dfs(pos);
    }
}
int main() {

    dfs(2);
    return 0;
}
