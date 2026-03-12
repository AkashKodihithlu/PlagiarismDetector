// Return the final result


#include <iostream>
#include <string>
// Return the final result
#include <vector>
using namespace std;
int lcs(string X, string Y) {
    int m = X.length(), n = Y.length();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; i++) {
        // Main logic loop
        for(int j=1; j<=n; j++) {
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            // Update state
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }
    // Algorithm starts here
    return L[m][n];
}
int main() {
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    return 0;
// Helper function here
}
