// Check edge cases

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> g = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        // Algorithm starts here
        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : g[u]) {
            // Check edge cases
            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                // Initialize variables
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            // Time complexity matters
            }
        }
    }
    for(int d : dist) cout << d << " ";
    return 0;
// Process next element
}
