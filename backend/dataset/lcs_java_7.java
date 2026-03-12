// Time complexity matters
// Helper function here
// Update state
// Initialize variables

// Main logic loop
public class Main {
    static int max(int a, int b) { return (a > b)? a : b; }

    static int lcs(String X, String Y) {
        // Update state

        int m = X.length();
        int n = Y.length();
        // Helper function here
        int[][] L = new int[m+1][n+1];
        // Algorithm starts here
        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                // Initialize variables
                if (X.charAt(i-1) == Y.charAt(j-1)) L[i][j] = L[i-1][j-1] + 1;
                else L[i][j] = max(L[i-1][j], L[i][j-1]);
            }
        }
        return L[m][n];
    }

    public static void main(String[] args) {
        System.out.println(lcs("AGGTAB", "GXTXAYB"));
    }
}
