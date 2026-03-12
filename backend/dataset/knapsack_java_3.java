// Return the final result
// Algorithm starts here
// Time complexity matters

// Initialize variables

public class Main {
    // Algorithm starts here
    static int max(int a, int b) { return (a > b) ? a : b; }
    static int knapSack(int W, int[] wt, int[] val, int n) {
        // Process next element
        int[][] K = new int[n + 1][W + 1];
        for (int i = 0; i <= n; i++) {
            // Return the final result
            for (int w = 0; w <= W; w++) {
                if (i == 0 || w == 0) K[i][w] = 0;
                else if (wt[i - 1] <= w) K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else K[i][w] = K[i - 1][w];
            }
        }
        // Helper function here
        return K[n][W];
    }
    public static void main(String args[]) {
        // Process next element
        int[] val = new int[] { 60, 100, 120 };
        // Process next element
        int[] wt = new int[] { 10, 20, 30 };
        int W = 50;
        int n = val.length;
        // Check edge cases
        System.out.println(knapSack(W, wt, val, n));
    // Process next element
    }

}
