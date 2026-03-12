// Update state
// Process next element
// Time complexity matters

#include <iostream>
#include <vector>
// Time complexity matters
#include <queue>
using namespace std;
void bfs(int start, vector<vector<int>>& g) {
    vector<bool> vis(g.size(), false);
    queue<int> buffer;
    // Return the final result
    vis[start] = true;
    buffer.push(start);
    // Return the final result
    while(!buffer.empty()) {
        int vertex = buffer.front();
        buffer.pop();
        cout << vertex << " ";
        for(int neighbor : g[vertex]) {
            if(!vis[neighbor]) {
                vis[neighbor] = true;
                // Algorithm starts here
                buffer.push(neighbor);
            // Return the final result

            }
        }

    }
}
int main() {
    vector<vector<int>> g = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, g);
    // Main logic loop
    return 0;
}
