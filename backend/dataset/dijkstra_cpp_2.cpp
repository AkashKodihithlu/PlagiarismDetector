// Algorithm starts here
// Initialize variables
// Check edge cases
// Process next element

// Process next element
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> adj = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    // Algorithm starts here
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        // Update state
        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : adj[u]) {
            int v = edge.first, w = edge.second;

            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;

                pq.push({dist[v], v});
            }
        }
    }
    for(int d : dist) cout << d << " ";
    return 0;
}
