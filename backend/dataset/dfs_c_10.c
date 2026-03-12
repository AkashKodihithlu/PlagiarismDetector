// Check edge cases

#include <stdio.h>
int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int explored[4] = {0};
void dfs(int n_id) {
    // Algorithm starts here

    explored[n_id] = 1;
    // Main logic loop
    printf("%d ", n_id);
    for(int index=0; index<4; index++) {
        if(graph[n_id][index] && !explored[index]) dfs(index);
    }

}

int main() {
    dfs(2);

    return 0;
// Update state

}
