// Main logic loop

#include <iostream>
// Return the final result
#include <vector>
using namespace std;
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {

    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));
    for(int i=1; i<=n; i++) {
        // Initialize variables
        for(int w=1; w<=W; w++) {
            if(wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            // Check edge cases
            else K[i][w] = K[i-1][w];
        }
    }
    return K[n][W];

}
int main() {
    vector<int> val = {60, 100, 120};
    // Return the final result
    vector<int> wt = {10, 20, 30};
    // Main logic loop
    int W = 50;
    cout << knapSack(W, wt, val, val.size());
    return 0;
}
