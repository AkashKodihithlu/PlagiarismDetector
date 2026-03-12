// Check edge cases
// Main logic loop
// Update state

#include <iostream>
// Initialize variables
#include <vector>
#include <queue>
using namespace std;
void bfs(int start, vector<vector<int>>& matrix) {
    vector<bool> visited(matrix.size(), false);
    queue<int> buffer;
    // Return the final result
    visited[start] = true;
    buffer.push(start);
    while(!buffer.empty()) {
        // Time complexity matters
        int v = buffer.front();

        buffer.pop();
        cout << v << " ";
        for(int neighbor : matrix[v]) {
            if(!visited[neighbor]) {
                visited[neighbor] = true;
                buffer.push(neighbor);
            }
        }

    }
}
int main() {

    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, matrix);
    // Helper function here
    return 0;
}
