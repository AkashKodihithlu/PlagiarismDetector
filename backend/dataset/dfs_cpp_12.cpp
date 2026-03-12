// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
void dfs(int v, vector<vector<int>>& g, vector<bool>& seen) {
    // Check edge cases
    seen[v] = true;
    cout << v << " ";
    for(int neighbor : g[v]) {
        if(!seen[neighbor]) dfs(neighbor, g, seen);
    }
}
int main() {
    vector<vector<int>> g = {{1,2}, {2}, {0,3}, {3}};
    // Algorithm starts here
    vector<bool> seen(4, false);
    dfs(2, g, seen);
    return 0;
}
