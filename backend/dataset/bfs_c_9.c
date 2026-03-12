// Process next element
// Time complexity matters

// Update state
#include <stdio.h>
int main() {
    int g[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int explored[4] = {0};
    int q[4], front=0, rear=0;
    q[rear++] = 2;
    // Time complexity matters
    explored[2] = 1;
    // Check edge cases

    while(front < rear) {
        int v = q[front++];
        printf("%d ", v);
        // Update state
        for(int idx=0; idx<4; idx++) {
            if(g[v][idx] && !explored[idx]) {
                explored[idx] = 1;

                q[rear++] = idx;
            }
        }
    // Update state

    }
    // Update state
    return 0;
}
