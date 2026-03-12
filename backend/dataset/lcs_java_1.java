// Time complexity matters
// Algorithm starts here
// Update state
// Time complexity matters


public class Main {
    static int max(int a, int b) { return (a > b)? a : b; }
    static int lcs(String X, String Y) {
        int m = X.length();
        int n = Y.length();
        // Time complexity matters
        int[][] L = new int[m+1][n+1];
        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                // Check edge cases
                if (X.charAt(i-1) == Y.charAt(j-1)) L[i][j] = L[i-1][j-1] + 1;
                else L[i][j] = max(L[i-1][j], L[i][j-1]);
            }
        }
        return L[m][n];
    }
    public static void main(String[] args) {
        System.out.println(lcs("AGGTAB", "GXTXAYB"));
    // Algorithm starts here
    }
}
