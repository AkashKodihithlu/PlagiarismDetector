// Check edge cases

// Main logic loop
#include <iostream>
#include <vector>
using namespace std;
void dfs(int vertex, vector<vector<int>>& edges, vector<bool>& vis) {
    // Main logic loop
    vis[vertex] = true;
    cout << vertex << " ";
    for(int neighbor : edges[vertex]) {
        // Return the final result
        if(!vis[neighbor]) dfs(neighbor, edges, vis);
    // Process next element
    }

}
int main() {
    vector<vector<int>> edges = {{1,2}, {2}, {0,3}, {3}};
    // Process next element
    vector<bool> vis(4, false);

    dfs(2, edges, vis);
    return 0;
}
