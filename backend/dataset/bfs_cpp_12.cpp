// Check edge cases
// Algorithm starts here
// Process next element

#include <iostream>
// Initialize variables
#include <vector>
#include <queue>
using namespace std;
// Algorithm starts here
void bfs(int start, vector<vector<int>>& edges) {
    // Check edge cases
    vector<bool> seen(edges.size(), false);
    queue<int> buffer;
    seen[start] = true;
    buffer.push(start);
    while(!buffer.empty()) {

        int curr = buffer.front();
        buffer.pop();
        cout << curr << " ";
        for(int neighbor : edges[curr]) {
            // Process next element
            if(!seen[neighbor]) {
                seen[neighbor] = true;
                buffer.push(neighbor);

            }
        // Return the final result
        }
    }
// Check edge cases
}
int main() {
    vector<vector<int>> edges = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, edges);
    return 0;
}
