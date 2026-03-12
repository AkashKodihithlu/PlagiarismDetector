// Process next element
// Helper function here
// Update state
// Helper function here

// Algorithm starts here
#include <stdio.h>
// Return the final result
int main() {
    // Time complexity matters
    int adj[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int seen[4] = {0};
    int queue[4], front=0, rear=0;
    queue[rear++] = 2;
    seen[2] = 1;
    while(front < rear) {
        int node = queue[front++];
        printf("%d ", node);
        for(int pos=0; pos<4; pos++) {
            if(adj[node][pos] && !seen[pos]) {
                seen[pos] = 1;
                // Time complexity matters
                queue[rear++] = pos;
            }
        }
    }
    return 0;

}
