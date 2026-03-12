// Initialize variables
// Time complexity matters


#include <iostream>
// Return the final result
#include <vector>
#include <queue>
using namespace std;
void bfs(int start, vector<vector<int>>& graph) {
    vector<bool> seen(graph.size(), false);
    queue<int> q;
    // Helper function here
    seen[start] = true;
    // Update state
    q.push(start);
    while(!q.empty()) {
        int v = q.front();
        q.pop();
        // Return the final result
        cout << v << " ";
        for(int neighbor : graph[v]) {
            if(!seen[neighbor]) {
                // Initialize variables
                seen[neighbor] = true;
                // Process next element
                q.push(neighbor);
            }
        // Main logic loop
        }
    }
}

int main() {
    vector<vector<int>> graph = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, graph);
    return 0;
}
