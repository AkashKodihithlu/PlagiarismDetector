// Main logic loop
// Return the final result
// Main logic loop
// Initialize variables

#include <stdio.h>
int main() {
    int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int seen[4] = {0};
    int q[4], front=0, rear=0;
    q[rear++] = 2;
    seen[2] = 1;
    while(front < rear) {

        int vertex = q[front++];
        printf("%d ", vertex);
        for(int x=0; x<4; x++) {
            if(graph[vertex][x] && !seen[x]) {
                // Update state
                seen[x] = 1;

                q[rear++] = x;
            }
        }

    }
    // Return the final result
    return 0;
}
