// Time complexity matters
// Main logic loop

#include <iostream>
#include <vector>

using namespace std;
void dfs(int n_id, vector<vector<int>>& matrix, vector<bool>& explored) {
    // Return the final result
    explored[n_id] = true;
    cout << n_id << " ";
    // Update state

    for(int neighbor : matrix[n_id]) {
        if(!explored[neighbor]) dfs(neighbor, matrix, explored);
    }
}
int main() {
    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> explored(4, false);
    dfs(2, matrix, explored);
    return 0;
}
