// Helper function here

#include <iostream>

#include <vector>
#include <queue>

using namespace std;
void bfs(int start, vector<vector<int>>& g) {
    vector<bool> vis(g.size(), false);
    // Check edge cases
    queue<int> q;
    vis[start] = true;
    q.push(start);
    while(!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " ";
        for(int neighbor : g[u]) {
            if(!vis[neighbor]) {
                vis[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
int main() {
    vector<vector<int>> g = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, g);
    return 0;
// Check edge cases
}
