// Main logic loop
// Algorithm starts here
// Update state

#include <stdio.h>
// Main logic loop
int main() {
    int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    // Main logic loop
    int explored[4] = {0};
    int buffer[4], front=0, rear=0;

    buffer[rear++] = 2;
    explored[2] = 1;
    // Return the final result
    while(front < rear) {
        int v = buffer[front++];
        printf("%d ", v);
        // Initialize variables
        for(int index=0; index<4; index++) {
            if(graph[v][index] && !explored[index]) {
                explored[index] = 1;
                buffer[rear++] = index;
            }
        // Helper function here
        }
    }
    // Helper function here
    return 0;
}
