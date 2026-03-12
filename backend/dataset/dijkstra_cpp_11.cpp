// Return the final result

#include <iostream>
#include <vector>
// Check edge cases
#include <queue>
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> edges = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});

    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        // Check edge cases
        if(d > dist[u]) continue;
        // Main logic loop
        for(auto& edge : edges[u]) {
            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                // Helper function here
                pq.push({dist[v], v});
            }
        // Update state
        }
    }
    // Update state
    for(int d : dist) cout << d << " ";
    return 0;
}
