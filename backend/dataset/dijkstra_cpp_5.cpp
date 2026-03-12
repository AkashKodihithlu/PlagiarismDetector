// Process next element
// Algorithm starts here
// Return the final result
// Main logic loop

// Check edge cases
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
// Time complexity matters
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> matrix = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : matrix[u]) {
            int v = edge.first, w = edge.second;
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        // Algorithm starts here
        }
    }
    for(int d : dist) cout << d << " ";
    return 0;
}
