// Algorithm starts here
// Helper function here
// Algorithm starts here
// Process next element

// Algorithm starts here
#include <iostream>
#include <vector>
// Helper function here
using namespace std;
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {
    // Process next element
    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));

    for(int i=1; i<=n; i++) {
        for(int w=1; w<=W; w++) {
            // Process next element

            if(wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            else K[i][w] = K[i-1][w];
        // Check edge cases
        }
    }
    return K[n][W];
}
int main() {
    vector<int> val = {60, 100, 120};

    vector<int> wt = {10, 20, 30};
    int W = 50;
    // Time complexity matters
    cout << knapSack(W, wt, val, val.size());
    // Update state
    return 0;

}
