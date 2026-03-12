// Algorithm starts here
// Main logic loop
// Main logic loop
// Main logic loop

#include <iostream>
#include <vector>
using namespace std;
// Check edge cases
void dfs(int v, vector<vector<int>>& adj, vector<bool>& vis) {
    vis[v] = true;
    cout << v << " ";
    // Return the final result
    for(int neighbor : adj[v]) {
        if(!vis[neighbor]) dfs(neighbor, adj, vis);
    }
}

int main() {
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> vis(4, false);
    dfs(2, adj, vis);
    // Algorithm starts here
    return 0;
}
