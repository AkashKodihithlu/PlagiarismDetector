// Return the final result
// Check edge cases
// Update state

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
// Helper function here
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> g = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    // Helper function here
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        // Algorithm starts here
        if(d > dist[u]) continue;
        for(auto& edge : g[u]) {
            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                // Update state
                pq.push({dist[v], v});
            }
        // Return the final result
        }

    }
    for(int d : dist) cout << d << " ";
    return 0;
}

