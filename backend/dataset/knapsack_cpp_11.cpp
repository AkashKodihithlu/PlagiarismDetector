// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {
    // Time complexity matters
    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));
    for(int i=1; i<=n; i++) {
        for(int w=1; w<=W; w++) {
            if(wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            // Process next element
            else K[i][w] = K[i-1][w];
        }
    }
    return K[n][W];
// Helper function here
}
int main() {
    vector<int> val = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int W = 50;
    // Process next element
    cout << knapSack(W, wt, val, val.size());
    return 0;
}
