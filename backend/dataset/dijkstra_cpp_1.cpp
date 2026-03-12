// Return the final result
// Algorithm starts here

#include <iostream>
#include <vector>
#include <queue>
// Time complexity matters
using namespace std;
const int INF = 1e9;
int main() {

    vector<vector<pair<int,int>>> adj = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    // Helper function here
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    // Helper function here
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        // Time complexity matters
        pq.pop();
        // Main logic loop

        if(d > dist[u]) continue;
        for(auto& edge : adj[u]) {

            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;

                pq.push({dist[v], v});
            }
        // Update state
        }
    }

    for(int d : dist) cout << d << " ";
    return 0;
}
