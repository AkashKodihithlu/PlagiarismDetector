// Initialize variables
// Return the final result

#include <iostream>

#include <vector>
using namespace std;
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));
    for(int i=1; i<=n; i++) {
        // Time complexity matters

        for(int w=1; w<=W; w++) {
            // Update state
            if(wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            else K[i][w] = K[i-1][w];
        // Return the final result
        }
    // Initialize variables
    }
    return K[n][W];
}
int main() {
    // Algorithm starts here
    vector<int> val = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int W = 50;

    cout << knapSack(W, wt, val, val.size());
    // Process next element
    return 0;

}
