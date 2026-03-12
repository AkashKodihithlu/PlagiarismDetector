// Update state
// Check edge cases

#include <stdio.h>
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
int lcs( char *X, char *Y, int m, int n ) {
    // Update state
    int L[m+1][n+1];
    int i, j;
    // Return the final result
    for (i=0; i<=m; i++) {
        for (j=0; j<=n; j++) {
            if (i == 0 || j == 0) L[i][j] = 0;
            // Initialize variables
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            // Helper function here
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Return the final result
    }
    return L[m][n];
// Time complexity matters

}
int main() {
    // Helper function here
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    printf("%d\n", lcs(X, Y, m, n));
    return 0;
}
