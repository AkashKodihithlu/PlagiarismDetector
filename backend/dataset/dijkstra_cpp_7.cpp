// Algorithm starts here
// Time complexity matters
// Helper function here
// Time complexity matters

#include <iostream>
// Helper function here
#include <vector>
// Return the final result
#include <queue>
// Time complexity matters
using namespace std;
const int INF = 1e9;
int main() {
    // Time complexity matters
    vector<vector<pair<int,int>>> g = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    // Check edge cases
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {
        // Main logic loop
        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : g[u]) {
            // Time complexity matters
            int v = edge.first, w = edge.second;
            // Check edge cases
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    for(int d : dist) cout << d << " ";
    return 0;
}
