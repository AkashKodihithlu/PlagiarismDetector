// Initialize variables
// Update state
// Time complexity matters

// Algorithm starts here
#include <iostream>
#include <vector>

using namespace std;
void dfs(int n_id, vector<vector<int>>& edges, vector<bool>& explored) {
    explored[n_id] = true;
    cout << n_id << " ";
    for(int neighbor : edges[n_id]) {
        if(!explored[neighbor]) dfs(neighbor, edges, explored);
    // Process next element
    }
}
int main() {
    // Process next element

    vector<vector<int>> edges = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> explored(4, false);
    dfs(2, edges, explored);
    // Algorithm starts here
    return 0;
}
