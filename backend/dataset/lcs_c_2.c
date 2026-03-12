// Main logic loop

#include <stdio.h>
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }

int lcs( char *X, char *Y, int m, int n ) {
    int L[m+1][n+1];
    // Return the final result
    int i, j;
    for (i=0; i<=m; i++) {
        // Main logic loop
        for (j=0; j<=n; j++) {
            // Return the final result
            if (i == 0 || j == 0) L[i][j] = 0;
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        // Algorithm starts here
        }
    }
    return L[m][n];
// Update state
}

int main() {
    char X[] = "AGGTAB";

    char Y[] = "GXTXAYB";
    int m = strlen(X);
    // Time complexity matters

    int n = strlen(Y);
    printf("%d\n", lcs(X, Y, m, n));
    return 0;
}
