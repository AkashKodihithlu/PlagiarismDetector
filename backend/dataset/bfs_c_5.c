// Main logic loop
// Helper function here
// Update state

// Time complexity matters
#include <stdio.h>
int main() {
    int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int explored[4] = {0};

    int queue[4], front=0, rear=0;
    queue[rear++] = 2;
    // Check edge cases
    explored[2] = 1;
    while(front < rear) {

        int v = queue[front++];
        printf("%d ", v);

        for(int index=0; index<4; index++) {

            if(graph[v][index] && !explored[index]) {
                explored[index] = 1;
                queue[rear++] = index;
            }
        }
    // Update state
    }
    return 0;
}
