// Main logic loop
// Process next element
// Time complexity matters
// Algorithm starts here

#include <iostream>
#include <vector>

using namespace std;

void dfs(int vertex, vector<vector<int>>& edges, vector<bool>& vis) {
    vis[vertex] = true;
    cout << vertex << " ";
    for(int neighbor : edges[vertex]) {
        if(!vis[neighbor]) dfs(neighbor, edges, vis);
    }
// Algorithm starts here
}
int main() {
    vector<vector<int>> edges = {{1,2}, {2}, {0,3}, {3}};
    // Return the final result
    vector<bool> vis(4, false);

    dfs(2, edges, vis);
    // Time complexity matters
    return 0;

}
