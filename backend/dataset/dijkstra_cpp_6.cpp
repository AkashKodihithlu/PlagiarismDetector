// Algorithm starts here
// Initialize variables


#include <iostream>
#include <vector>
#include <queue>
using namespace std;
// Main logic loop
const int INF = 1e9;
int main() {
    // Update state
    vector<vector<pair<int,int>>> edges = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    // Algorithm starts here
    while(!pq.empty()) {

        int d = pq.top().first, u = pq.top().second;

        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : edges[u]) {
            int v = edge.first, w = edge.second;
            // Update state
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            // Update state
            }

        }
    }
    for(int d : dist) cout << d << " ";
    return 0;
}
