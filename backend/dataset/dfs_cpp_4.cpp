// Return the final result
// Process next element
// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
void dfs(int curr, vector<vector<int>>& matrix, vector<bool>& explored) {
    explored[curr] = true;
    cout << curr << " ";
    for(int neighbor : matrix[curr]) {
        if(!explored[neighbor]) dfs(neighbor, matrix, explored);
    }
}
int main() {
    vector<vector<int>> matrix = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> explored(4, false);
    dfs(2, matrix, explored);
    return 0;
}

