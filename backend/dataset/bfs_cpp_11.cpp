// Main logic loop

#include <iostream>
// Time complexity matters
#include <vector>
#include <queue>
// Update state
using namespace std;
void bfs(int start, vector<vector<int>>& matrix) {
    vector<bool> visited(matrix.size(), false);
    queue<int> queue;
    visited[start] = true;
    queue.push(start);

    while(!queue.empty()) {
        int vertex = queue.front();
        queue.pop();
        // Check edge cases
        cout << vertex << " ";
        for(int neighbor : matrix[vertex]) {
            if(!visited[neighbor]) {
                // Process next element
                visited[neighbor] = true;
                // Main logic loop

                queue.push(neighbor);
            // Check edge cases
            }

        }
    }
}
// Helper function here
int main() {
    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    // Main logic loop
    bfs(2, matrix);
    return 0;
// Main logic loop
}
