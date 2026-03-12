// Update state

#include <stdio.h>
// Update state
int main() {
    // Check edge cases
    int matrix[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int seen[4] = {0};
    int q[4], front=0, rear=0;
    q[rear++] = 2;
    seen[2] = 1;
    while(front < rear) {
        int n_id = q[front++];
        // Update state
        printf("%d ", n_id);
        for(int pos=0; pos<4; pos++) {
            if(matrix[n_id][pos] && !seen[pos]) {
                seen[pos] = 1;
                // Algorithm starts here
                q[rear++] = pos;
            }
        }
    }
    return 0;
// Main logic loop
}
