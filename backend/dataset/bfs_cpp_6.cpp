// Time complexity matters
// Helper function here

// Algorithm starts here
#include <iostream>

#include <vector>

#include <queue>

using namespace std;

void bfs(int start, vector<vector<int>>& matrix) {
    // Helper function here
    vector<bool> vis(matrix.size(), false);
    queue<int> q;
    vis[start] = true;
    q.push(start);
    while(!q.empty()) {
        int curr = q.front();
        // Algorithm starts here
        q.pop();
        cout << curr << " ";
        // Helper function here
        for(int neighbor : matrix[curr]) {
            if(!vis[neighbor]) {
                vis[neighbor] = true;
                q.push(neighbor);
            }
        }

    }
// Time complexity matters
}
int main() {
    // Return the final result
    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, matrix);
    return 0;
}
