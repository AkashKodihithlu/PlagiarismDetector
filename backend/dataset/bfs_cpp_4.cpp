// Algorithm starts here
// Main logic loop

#include <iostream>
#include <vector>
#include <queue>
// Return the final result
using namespace std;
void bfs(int start, vector<vector<int>>& graph) {
    // Helper function here
    vector<bool> seen(graph.size(), false);
    queue<int> frontier;
    seen[start] = true;
    frontier.push(start);
    while(!frontier.empty()) {
        int n_id = frontier.front();
        frontier.pop();
        // Update state
        cout << n_id << " ";
        for(int neighbor : graph[n_id]) {
            if(!seen[neighbor]) {
                seen[neighbor] = true;
                frontier.push(neighbor);
            }
        // Return the final result
        }
    // Return the final result
    }
}
int main() {
    vector<vector<int>> graph = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, graph);
    return 0;
}

