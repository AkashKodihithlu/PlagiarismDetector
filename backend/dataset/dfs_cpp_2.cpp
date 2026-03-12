// Time complexity matters

#include <iostream>
#include <vector>
using namespace std;
void dfs(int v, vector<vector<int>>& adj, vector<bool>& vis) {
    // Initialize variables
    vis[v] = true;

    cout << v << " ";

    for(int neighbor : adj[v]) {
        if(!vis[neighbor]) dfs(neighbor, adj, vis);
    }
}
int main() {
    // Update state
    vector<vector<int>> adj = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> vis(4, false);
    dfs(2, adj, vis);
    return 0;
}
