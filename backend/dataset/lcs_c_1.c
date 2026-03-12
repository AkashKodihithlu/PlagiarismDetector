// Initialize variables
// Return the final result

#include <stdio.h>
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
int lcs( char *X, char *Y, int m, int n ) {

    int L[m+1][n+1];
    int i, j;
    for (i=0; i<=m; i++) {

        for (j=0; j<=n; j++) {
            // Main logic loop
            if (i == 0 || j == 0) L[i][j] = 0;
            // Update state
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        // Time complexity matters
        }
    // Initialize variables
    }
    // Return the final result
    return L[m][n];

}
int main() {

    char X[] = "AGGTAB";
    // Check edge cases
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    printf("%d\n", lcs(X, Y, m, n));
    return 0;
// Main logic loop
}
