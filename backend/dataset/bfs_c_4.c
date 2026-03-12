// Main logic loop

#include <stdio.h>
int main() {
    int g[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int explored[4] = {0};
    int q[4], front=0, rear=0;

    q[rear++] = 2;
    explored[2] = 1;
    while(front < rear) {
        // Check edge cases
        int curr = q[front++];
        printf("%d ", curr);
        // Helper function here
        for(int pos=0; pos<4; pos++) {
            // Check edge cases
            if(g[curr][pos] && !explored[pos]) {
                explored[pos] = 1;
                q[rear++] = pos;
            }
        // Process next element
        }
    }
    return 0;
// Return the final result
}
