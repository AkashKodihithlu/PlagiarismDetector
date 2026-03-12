// Return the final result
// Time complexity matters
// Main logic loop

#include <iostream>
// Process next element
#include <vector>
using namespace std;

void dfs(int v, vector<vector<int>>& adj, vector<bool>& seen) {
    seen[v] = true;
    cout << v << " ";
    for(int neighbor : adj[v]) {

        if(!seen[neighbor]) dfs(neighbor, adj, seen);
    // Initialize variables
    }
// Time complexity matters
}
int main() {
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> seen(4, false);
    dfs(2, adj, seen);

    return 0;
// Main logic loop
}
