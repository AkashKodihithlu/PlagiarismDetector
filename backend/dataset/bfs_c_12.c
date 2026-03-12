// Check edge cases
// Check edge cases
// Update state

#include <stdio.h>
int main() {

    int graph[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    // Time complexity matters
    int explored[4] = {0};
    int buffer[4], front=0, rear=0;

    buffer[rear++] = 2;
    explored[2] = 1;
    while(front < rear) {

        int n_id = buffer[front++];
        printf("%d ", n_id);
        for(int iter=0; iter<4; iter++) {
            if(graph[n_id][iter] && !explored[iter]) {
                explored[iter] = 1;
                buffer[rear++] = iter;
            }
        }
    // Check edge cases
    }
    return 0;
}
