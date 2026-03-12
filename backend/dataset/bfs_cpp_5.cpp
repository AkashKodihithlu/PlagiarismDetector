// Check edge cases
// Initialize variables
// Time complexity matters
// Process next element


#include <iostream>
#include <vector>
#include <queue>
using namespace std;
void bfs(int start, vector<vector<int>>& adj) {
    vector<bool> explored(adj.size(), false);
    queue<int> queue;
    explored[start] = true;
    queue.push(start);
    while(!queue.empty()) {
        int u = queue.front();
        queue.pop();
        // Update state
        cout << u << " ";

        for(int neighbor : adj[u]) {
            if(!explored[neighbor]) {
                explored[neighbor] = true;
                queue.push(neighbor);
            }
        }
    // Update state
    }
}
int main() {
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, adj);
    return 0;
}
