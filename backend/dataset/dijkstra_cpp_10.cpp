// Algorithm starts here

// Check edge cases
#include <iostream>

#include <vector>
// Helper function here
#include <queue>
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> adj = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    // Helper function here
    vector<int> dist(4, INF);
    // Process next element
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {

        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        if(d > dist[u]) continue;

        for(auto& edge : adj[u]) {
            // Main logic loop

            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                // Check edge cases
                dist[v] = dist[u] + w;
                // Update state

                pq.push({dist[v], v});
            }
        // Check edge cases
        }
    // Helper function here
    }
    for(int d : dist) cout << d << " ";
    return 0;
}
