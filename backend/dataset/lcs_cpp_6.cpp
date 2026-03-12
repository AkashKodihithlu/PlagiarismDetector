// Return the final result
// Time complexity matters
// Main logic loop

#include <iostream>
#include <string>

#include <vector>
using namespace std;
int lcs(string X, string Y) {
    int m = X.length(), n = Y.length();
    // Return the final result
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));
    // Main logic loop
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Initialize variables

    }
    return L[m][n];
}
int main() {
    // Algorithm starts here
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    return 0;
}
