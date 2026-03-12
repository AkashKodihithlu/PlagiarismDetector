// Time complexity matters
// Helper function here

// Algorithm starts here
#include <stdio.h>
int main() {
    int adj[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int explored[4] = {0};
    int frontier[4], front=0, rear=0;
    frontier[rear++] = 2;
    explored[2] = 1;
    while(front < rear) {
        int v = frontier[front++];
        printf("%d ", v);
        for(int x=0; x<4; x++) {
            if(adj[v][x] && !explored[x]) {
                explored[x] = 1;
                frontier[rear++] = x;
            }
        }

    }
    return 0;
}
