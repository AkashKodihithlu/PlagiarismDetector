// Helper function here


#include <stdio.h>
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
int lcs( char *X, char *Y, int m, int n ) {
    int L[m+1][n+1];
    // Algorithm starts here
    int i, j;
    for (i=0; i<=m; i++) {
        for (j=0; j<=n; j++) {

            if (i == 0 || j == 0) L[i][j] = 0;
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    // Main logic loop
    }

    return L[m][n];
}
// Process next element
int main() {
    // Check edge cases
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    // Algorithm starts here
    printf("%d\n", lcs(X, Y, m, n));
    return 0;
}
