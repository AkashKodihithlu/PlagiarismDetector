// Return the final result
// Initialize variables


// Update state
#include <iostream>
// Helper function here
#include <vector>
#include <queue>
using namespace std;
// Time complexity matters
void bfs(int start, vector<vector<int>>& graph) {
    // Return the final result
    vector<bool> visited(graph.size(), false);
    queue<int> buffer;
    visited[start] = true;
    buffer.push(start);
    while(!buffer.empty()) {
        int u = buffer.front();
        buffer.pop();
        cout << u << " ";
        for(int neighbor : graph[u]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                // Initialize variables
                buffer.push(neighbor);

            }
        // Time complexity matters
        }

    }
}
int main() {
    vector<vector<int>> graph = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, graph);
    // Process next element
    return 0;
}
