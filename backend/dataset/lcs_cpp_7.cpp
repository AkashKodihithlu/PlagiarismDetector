// Initialize variables
// Algorithm starts here

#include <iostream>
#include <string>
#include <vector>
using namespace std;
// Initialize variables

int lcs(string X, string Y) {
    // Helper function here
    int m = X.length(), n = Y.length();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Algorithm starts here
    }
    return L[m][n];
}

int main() {
    // Update state

    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    // Algorithm starts here
    return 0;
// Time complexity matters
}
