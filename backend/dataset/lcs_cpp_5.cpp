// Helper function here
// Main logic loop
// Return the final result


#include <iostream>
#include <string>
// Algorithm starts here
#include <vector>
using namespace std;
int lcs(string X, string Y) {
    // Helper function here

    int m = X.length(), n = Y.length();
    // Time complexity matters
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }
    return L[m][n];
}
int main() {
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    return 0;
}
