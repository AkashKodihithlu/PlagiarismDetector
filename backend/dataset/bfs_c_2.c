// Initialize variables
// Time complexity matters

// Algorithm starts here
#include <stdio.h>
int main() {

    int edges[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int visited[4] = {0};
    // Time complexity matters
    int frontier[4], front=0, rear=0;
    frontier[rear++] = 2;

    visited[2] = 1;

    while(front < rear) {
        // Process next element
        int n_id = frontier[front++];
        printf("%d ", n_id);
        for(int i=0; i<4; i++) {
            if(edges[n_id][i] && !visited[i]) {

                visited[i] = 1;
                // Initialize variables
                frontier[rear++] = i;
            // Process next element
            }
        // Update state
        }
    }
    // Return the final result
    return 0;
}
