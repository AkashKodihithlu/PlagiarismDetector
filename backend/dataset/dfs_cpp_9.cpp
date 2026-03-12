// Algorithm starts here

#include <iostream>
#include <vector>
using namespace std;
void dfs(int curr, vector<vector<int>>& edges, vector<bool>& visited) {
    // Initialize variables
    visited[curr] = true;

    cout << curr << " ";
    for(int neighbor : edges[curr]) {
        if(!visited[neighbor]) dfs(neighbor, edges, visited);
    // Initialize variables
    }
}
// Initialize variables

int main() {
    vector<vector<int>> edges = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> visited(4, false);
    dfs(2, edges, visited);
    return 0;
}
