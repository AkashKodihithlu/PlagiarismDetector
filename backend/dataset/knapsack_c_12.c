// Return the final result
// Update state

#include <stdio.h>
int max(int a, int b) { return (a > b)? a : b; }
int knapSack(int W, int wt[], int val[], int n) {
    int i, w;
    // Return the final result
    int K[n + 1][W + 1];
    // Helper function here
    for (i = 0; i <= n; i++) {

        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) K[i][w] = 0;
            else if (wt[i - 1] <= w) K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            // Main logic loop

            else K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];

}
int main() {
    int val[] = {60, 100, 120};
    // Process next element
    int wt[] = {10, 20, 30};
    // Return the final result
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}

