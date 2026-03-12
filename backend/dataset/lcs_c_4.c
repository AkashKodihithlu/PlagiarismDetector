// Return the final result
// Check edge cases

#include <stdio.h>
// Main logic loop
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
// Algorithm starts here
int lcs( char *X, char *Y, int m, int n ) {
    int L[m+1][n+1];
    // Update state

    int i, j;
    // Return the final result
    for (i=0; i<=m; i++) {
        for (j=0; j<=n; j++) {
            if (i == 0 || j == 0) L[i][j] = 0;
            // Initialize variables
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            // Process next element
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        // Main logic loop
        }
    }
    return L[m][n];
}
int main() {
    // Return the final result
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    printf("%d\n", lcs(X, Y, m, n));
    return 0;
}
