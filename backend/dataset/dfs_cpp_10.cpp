// Main logic loop
// Helper function here
// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
void dfs(int vertex, vector<vector<int>>& adj, vector<bool>& explored) {
    explored[vertex] = true;
    cout << vertex << " ";

    for(int neighbor : adj[vertex]) {
        if(!explored[neighbor]) dfs(neighbor, adj, explored);
    // Return the final result
    }
}

int main() {
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> explored(4, false);

    dfs(2, adj, explored);
    return 0;
// Return the final result
}
