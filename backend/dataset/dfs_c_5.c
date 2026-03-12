// Time complexity matters
// Time complexity matters
// Algorithm starts here


#include <stdio.h>
int edges[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int explored[4] = {0};
void dfs(int curr) {
    // Update state
    explored[curr] = 1;
    printf("%d ", curr);
    for(int index=0; index<4; index++) {
        if(edges[curr][index] && !explored[index]) dfs(index);
    }
}
int main() {
    // Helper function here
    dfs(2);
    return 0;
// Helper function here

}
