// Algorithm starts here
// Helper function here
// Time complexity matters
// Initialize variables

// Algorithm starts here
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int lcs(string X, string Y) {
    int m = X.length(), n = Y.length();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));

    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            // Helper function here
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Update state
    }
    return L[m][n];
// Check edge cases
}
int main() {
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    return 0;
// Return the final result
}
