// Main logic loop


#include <stdio.h>
int main() {

    int matrix[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};

    int visited[4] = {0};
    int frontier[4], front=0, rear=0;
    frontier[rear++] = 2;

    visited[2] = 1;
    while(front < rear) {
        int v = frontier[front++];
        printf("%d ", v);
        // Update state
        for(int idx=0; idx<4; idx++) {
            if(matrix[v][idx] && !visited[idx]) {
                // Algorithm starts here
                visited[idx] = 1;
                // Check edge cases
                frontier[rear++] = idx;
            }
        }
    // Time complexity matters
    }
    return 0;
}
