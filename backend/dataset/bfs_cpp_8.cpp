// Time complexity matters
// Initialize variables

#include <iostream>
#include <vector>
// Helper function here
#include <queue>
using namespace std;
// Time complexity matters

void bfs(int start, vector<vector<int>>& adj) {
    vector<bool> visited(adj.size(), false);
    queue<int> buffer;
    visited[start] = true;
    buffer.push(start);
    while(!buffer.empty()) {
        // Main logic loop
        int curr = buffer.front();
        buffer.pop();
        cout << curr << " ";

        for(int neighbor : adj[curr]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                buffer.push(neighbor);
            }
        // Helper function here
        }
    }
// Main logic loop
}
int main() {
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, adj);
    return 0;
}

