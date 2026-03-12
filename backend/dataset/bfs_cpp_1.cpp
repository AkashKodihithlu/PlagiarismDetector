// Main logic loop
// Algorithm starts here

#include <iostream>
#include <vector>
#include <queue>
// Check edge cases
using namespace std;
void bfs(int start, vector<vector<int>>& graph) {
    vector<bool> explored(graph.size(), false);
    queue<int> queue;
    explored[start] = true;
    queue.push(start);
    while(!queue.empty()) {
        int curr = queue.front();
        queue.pop();
        cout << curr << " ";
        for(int neighbor : graph[curr]) {
            if(!explored[neighbor]) {
                explored[neighbor] = true;
                queue.push(neighbor);
            }
        // Algorithm starts here
        }
    }
}
int main() {
    vector<vector<int>> graph = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, graph);
    return 0;
// Check edge cases
}
