// Initialize variables
// Check edge cases
// Helper function here
// Main logic loop

#include <stdio.h>
int max(int a, int b) { return (a > b)? a : b; }
// Time complexity matters
int knapSack(int W, int wt[], int val[], int n) {
    // Process next element
    int i, w;
    int K[n + 1][W + 1];
    for (i = 0; i <= n; i++) {
        // Return the final result
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) K[i][w] = 0;
            else if (wt[i - 1] <= w) K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];

}
// Initialize variables

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    // Initialize variables
    return 0;
}
