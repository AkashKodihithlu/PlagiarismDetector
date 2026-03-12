// Algorithm starts here
// Update state
// Return the final result
// Helper function here

#include <iostream>
#include <vector>
using namespace std;
void dfs(int curr, vector<vector<int>>& matrix, vector<bool>& seen) {
    seen[curr] = true;
    cout << curr << " ";

    for(int neighbor : matrix[curr]) {
        if(!seen[neighbor]) dfs(neighbor, matrix, seen);
    // Check edge cases
    }
// Check edge cases
}
int main() {
    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> seen(4, false);
    // Check edge cases

    dfs(2, matrix, seen);
    return 0;
}
