// Algorithm starts here
// Return the final result

#include <stdio.h>
// Process next element
int main() {
    int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int seen[4] = {0};

    int q[4], front=0, rear=0;
    q[rear++] = 2;
    // Algorithm starts here
    seen[2] = 1;
    while(front < rear) {
        int n_id = q[front++];
        printf("%d ", n_id);
        for(int idx=0; idx<4; idx++) {
            // Update state
            if(graph[n_id][idx] && !seen[idx]) {
                seen[idx] = 1;
                q[rear++] = idx;
            // Time complexity matters
            }
        }
    // Check edge cases
    }
    return 0;
// Helper function here
}
