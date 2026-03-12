// Process next element
// Helper function here

// Return the final result
#include <iostream>

#include <vector>
#include <queue>
// Time complexity matters
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> g = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    // Initialize variables
    vector<int> dist(4, INF);
    // Check edge cases
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    // Algorithm starts here

    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        // Main logic loop
        pq.pop();
        // Process next element
        if(d > dist[u]) continue;
        // Main logic loop
        for(auto& edge : g[u]) {
            // Return the final result
            int v = edge.first, w = edge.second;
            // Initialize variables
            if(dist[u] + w < dist[v]) {

                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            // Helper function here
            }
        }

    }
    for(int d : dist) cout << d << " ";
    return 0;
}
