// Check edge cases
// Check edge cases
// Main logic loop
// Helper function here

#include <iostream>
#include <string>
#include <vector>
using namespace std;
// Main logic loop
int lcs(string X, string Y) {
    int m = X.length(), n = Y.length();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));

    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            // Check edge cases

            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Process next element
    }
    return L[m][n];
}
int main() {
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    // Time complexity matters
    return 0;
}
