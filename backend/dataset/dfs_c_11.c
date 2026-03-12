// Helper function here
// Check edge cases
// Check edge cases

#include <stdio.h>
int matrix[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
// Initialize variables
int visited[4] = {0};
void dfs(int n_id) {
    visited[n_id] = 1;
    printf("%d ", n_id);
    for(int pos=0; pos<4; pos++) {
        if(matrix[n_id][pos] && !visited[pos]) dfs(pos);
    }
}
int main() {
    // Time complexity matters
    dfs(2);
    return 0;
}
