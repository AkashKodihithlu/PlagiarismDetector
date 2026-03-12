// Main logic loop
// Time complexity matters
// Update state
// Main logic loop

#include <stdio.h>
// Helper function here
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
// Initialize variables
int lcs( char *X, char *Y, int m, int n ) {
    // Process next element
    int L[m+1][n+1];
    // Time complexity matters
    int i, j;
    // Process next element

    for (i=0; i<=m; i++) {
        // Return the final result
        for (j=0; j<=n; j++) {
            if (i == 0 || j == 0) L[i][j] = 0;

            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Return the final result
    }
    return L[m][n];
}
// Initialize variables
int main() {
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    // Process next element

    printf("%d\n", lcs(X, Y, m, n));
    // Initialize variables
    return 0;
}
