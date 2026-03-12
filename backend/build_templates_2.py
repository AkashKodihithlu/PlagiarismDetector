import json

with open("a:/plagiarism/backend/templates.json", "r") as f:
    t = json.load(f)

t["bfs"]["py"].append('''
def solve(VAR_GRAPH, start):
    VAR_VISITED, VAR_QUEUE = set([start]), [start]
    res = []
    while VAR_QUEUE:
        VAR_NODE = VAR_QUEUE.pop(0)
        res.append(VAR_NODE)
        for neighbor in VAR_GRAPH.get(VAR_NODE, []):
            if neighbor not in VAR_VISITED:
                VAR_VISITED.add(neighbor)
                VAR_QUEUE.append(neighbor)
    return res
def main():
    VAR_GRAPH = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(VAR_GRAPH, 2))
if __name__ == "__main__":
    main()
''')
t["bfs"]["c"].append('''
#include <stdio.h>
int main() {
    int VAR_GRAPH[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
    int VAR_VISITED[4] = {0};
    int VAR_QUEUE[4], front=0, rear=0;
    VAR_QUEUE[rear++] = 2;
    VAR_VISITED[2] = 1;
    while(front < rear) {
        int VAR_NODE = VAR_QUEUE[front++];
        printf("%d ", VAR_NODE);
        for(int VAR_I=0; VAR_I<4; VAR_I++) {
            if(VAR_GRAPH[VAR_NODE][VAR_I] && !VAR_VISITED[VAR_I]) {
                VAR_VISITED[VAR_I] = 1;
                VAR_QUEUE[rear++] = VAR_I;
            }
        }
    }
    return 0;
}
''')
t["bfs"]["cpp"].append('''
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
void bfs(int start, vector<vector<int>>& VAR_GRAPH) {
    vector<bool> VAR_VISITED(VAR_GRAPH.size(), false);
    queue<int> VAR_QUEUE;
    VAR_VISITED[start] = true;
    VAR_QUEUE.push(start);
    while(!VAR_QUEUE.empty()) {
        int VAR_NODE = VAR_QUEUE.front();
        VAR_QUEUE.pop();
        cout << VAR_NODE << " ";
        for(int neighbor : VAR_GRAPH[VAR_NODE]) {
            if(!VAR_VISITED[neighbor]) {
                VAR_VISITED[neighbor] = true;
                VAR_QUEUE.push(neighbor);
            }
        }
    }
}
int main() {
    vector<vector<int>> VAR_GRAPH = {{1,2}, {2}, {0,3}, {3}};
    bfs(2, VAR_GRAPH);
    return 0;
}
''')
t["bfs"]["java"].append('''
import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[][] VAR_GRAPH = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] VAR_VISITED = new boolean[4];
        Queue<Integer> VAR_QUEUE = new LinkedList<>();
        VAR_VISITED[2] = true;
        VAR_QUEUE.add(2);
        while(!VAR_QUEUE.isEmpty()) {
            int VAR_NODE = VAR_QUEUE.poll();
            System.out.print(VAR_NODE + " ");
            for(int VAR_I=0; VAR_I<VAR_GRAPH.length; VAR_I++) {
                if(VAR_GRAPH[VAR_NODE][VAR_I]==1 && !VAR_VISITED[VAR_I]) {
                    VAR_VISITED[VAR_I] = true;
                    VAR_QUEUE.add(VAR_I);
                }
            }
        }
    }
}
''')


t["dijkstra"]["py"].append('''
import heapq
def solve(VAR_GRAPH, start):
    distances = {node: float('infinity') for node in VAR_GRAPH}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, VAR_NODE = heapq.heappop(pq)
        if curr_dist > distances[VAR_NODE]: continue
        for neighbor, weight in VAR_GRAPH[VAR_NODE].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances
def main():
    VAR_GRAPH = {0: {1:4, 2:1}, 1: {3:1}, 2: {1:2, 3:5}, 3: {}}
    print(solve(VAR_GRAPH, 0))
if __name__ == "__main__":
    main()
''')
t["dijkstra"]["c"].append('''
#include <stdio.h>
#define INF 9999
int minDistance(int dist[], int sptSet[]) {
    int min = INF, min_index;
    for (int v = 0; v < 4; v++)
        if (sptSet[v] == 0 && dist[v] <= min) { min = dist[v]; min_index = v; }
    return min_index;
}
int main() {
    int VAR_GRAPH[4][4] = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
    int dist[4]; int sptSet[4];
    for(int i=0; i<4; i++) { dist[i]=INF; sptSet[i]=0; }
    dist[0] = 0;
    for (int count=0; count<3; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = 1;
        for (int v=0; v<4; v++)
            if (!sptSet[v] && VAR_GRAPH[u][v] && dist[u]!=INF && dist[u]+VAR_GRAPH[u][v]<dist[v])
                dist[v] = dist[u] + VAR_GRAPH[u][v];
    }
    for(int i=0; i<4; i++) printf("%d ", dist[i]);
    return 0;
}
''')
t["dijkstra"]["cpp"].append('''
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 1e9;
int main() {
    vector<vector<pair<int,int>>> VAR_GRAPH = {{{1,4},{2,1}}, {{3,1}}, {{1,2},{3,5}}, {}};
    vector<int> dist(4, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});
    while(!pq.empty()) {
        int d = pq.top().first, u = pq.top().second;
        pq.pop();
        if(d > dist[u]) continue;
        for(auto& edge : VAR_GRAPH[u]) {
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
''')
t["dijkstra"]["java"].append('''
import java.util.*;
public class Main {
    static final int INF = 9999;
    public static void main(String[] args) {
        int[][] VAR_GRAPH = {{0,4,1,0}, {0,0,0,1}, {0,2,0,5}, {0,0,0,0}};
        int[] dist = new int[4];
        boolean[] sptSet = new boolean[4];
        Arrays.fill(dist, INF);
        dist[0] = 0;
        for(int count=0; count<3; count++) {
            int u = -1; int min = INF;
            for(int i=0; i<4; i++) {
                if(!sptSet[i] && dist[i]<min) { min = dist[i]; u = i; }
            }
            if(u == -1) break;
            sptSet[u] = true;
            for(int v=0; v<4; v++) {
                if(!sptSet[v] && VAR_GRAPH[u][v]!=0 && dist[u]!=INF && dist[u]+VAR_GRAPH[u][v]<dist[v]) {
                    dist[v] = dist[u]+VAR_GRAPH[u][v];
                }
            }
        }
        for(int d : dist) System.out.print(d+" ");
    }
}
''')


t["knapsack"]["py"].append('''
def solve(W, wt, val, VAR_SIZE):
    K = [[0 for x in range(W + 1)] for x in range(VAR_SIZE + 1)]
    for VAR_I in range(VAR_SIZE + 1):
        for w in range(W + 1):
            if VAR_I == 0 or w == 0:
                K[VAR_I][w] = 0
            elif wt[VAR_I-1] <= w:
                K[VAR_I][w] = max(val[VAR_I-1] + K[VAR_I-1][w-wt[VAR_I-1]], K[VAR_I-1][w])
            else:
                K[VAR_I][w] = K[VAR_I-1][w]
    return K[VAR_SIZE][W]
def main():
    print(solve(50, [10, 20, 30], [60, 100, 120], 3))
if __name__ == "__main__":
    main()
''')
t["knapsack"]["c"].append('''
#include <stdio.h>
int max(int a, int b) { return (a > b)? a : b; }
int knapSack(int W, int wt[], int val[], int n) {
    int i, w;
    int K[n + 1][W + 1];
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) K[i][w] = 0;
            else if (wt[i - 1] <= w) K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}
int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}
''')
t["knapsack"]["cpp"].append('''
#include <iostream>
#include <vector>
using namespace std;
int knapSack(int W, vector<int>& wt, vector<int>& val, int n) {
    vector<vector<int>> K(n + 1, vector<int>(W + 1, 0));
    for(int i=1; i<=n; i++) {
        for(int w=1; w<=W; w++) {
            if(wt[i-1] <= w) K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]);
            else K[i][w] = K[i-1][w];
        }
    }
    return K[n][W];
}
int main() {
    vector<int> val = {60, 100, 120};
    vector<int> wt = {10, 20, 30};
    int W = 50;
    cout << knapSack(W, wt, val, val.size());
    return 0;
}
''')
t["knapsack"]["java"].append('''
public class Main {
    static int max(int a, int b) { return (a > b) ? a : b; }
    static int knapSack(int W, int[] wt, int[] val, int n) {
        int[][] K = new int[n + 1][W + 1];
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (i == 0 || w == 0) K[i][w] = 0;
                else if (wt[i - 1] <= w) K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else K[i][w] = K[i - 1][w];
            }
        }
        return K[n][W];
    }
    public static void main(String args[]) {
        int[] val = new int[] { 60, 100, 120 };
        int[] wt = new int[] { 10, 20, 30 };
        int W = 50;
        int n = val.length;
        System.out.println(knapSack(W, wt, val, n));
    }
}
''')


t["fibonacci"]["py"].append('''
def solve(VAR_SIZE):
    if VAR_SIZE <= 0: return 0
    elif VAR_SIZE == 1: return 1
    VAR_ARR = [0] * (VAR_SIZE + 1)
    VAR_ARR[1] = 1
    for i in range(2, VAR_SIZE + 1):
        VAR_ARR[i] = VAR_ARR[i-1] + VAR_ARR[i-2]
    return VAR_ARR[VAR_SIZE]
def main():
    print(solve(9))
if __name__ == "__main__":
    main()
''')
t["fibonacci"]["c"].append('''
#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    printf("%d\\n", fib(9));
    return 0;
}
''')
t["fibonacci"]["cpp"].append('''
#include <iostream>
using namespace std;
int fib(int n) {
    if (n <= 1) return n;
    int a=0, b=1, c;
    for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
    return b;
}
int main() {
    cout << fib(9) << endl;
    return 0;
}
''')
t["fibonacci"]["java"].append('''
public class Main {
    static int fib(int n) {
        if (n <= 1) return n;
        int a=0, b=1, c;
        for(int i=2; i<=n; i++) { c = a+b; a = b; b = c; }
        return b;
    }
    public static void main(String args[]) {
        System.out.println(fib(9));
    }
}
''')


t["lcs"]["py"].append('''
def solve(X, Y):
    m, n = len(X), len(Y)
    L = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: L[i][j] = L[i-1][j-1]+1
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
def main():
    print(solve("AGGTAB", "GXTXAYB"))
if __name__ == "__main__":
    main()
''')
t["lcs"]["c"].append('''
#include <stdio.h>
#include <string.h>
int max(int a, int b) { return (a > b)? a : b; }
int lcs( char *X, char *Y, int m, int n ) {
    int L[m+1][n+1];
    int i, j;
    for (i=0; i<=m; i++) {
        for (j=0; j<=n; j++) {
            if (i == 0 || j == 0) L[i][j] = 0;
            else if (X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }
    return L[m][n];
}
int main() {
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    printf("%d\\n", lcs(X, Y, m, n));
    return 0;
}
''')
t["lcs"]["cpp"].append('''
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int lcs(string X, string Y) {
    int m = X.length(), n = Y.length();
    vector<vector<int>> L(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; i++) {
        for(int j=1; j<=n; j++) {
            if(X[i-1] == Y[j-1]) L[i][j] = L[i-1][j-1] + 1;
            else L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }
    return L[m][n];
}
int main() {
    cout << lcs("AGGTAB", "GXTXAYB") << endl;
    return 0;
}
''')
t["lcs"]["java"].append('''
public class Main {
    static int max(int a, int b) { return (a > b)? a : b; }
    static int lcs(String X, String Y) {
        int m = X.length();
        int n = Y.length();
        int[][] L = new int[m+1][n+1];
        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                if (X.charAt(i-1) == Y.charAt(j-1)) L[i][j] = L[i-1][j-1] + 1;
                else L[i][j] = max(L[i-1][j], L[i][j-1]);
            }
        }
        return L[m][n];
    }
    public static void main(String[] args) {
        System.out.println(lcs("AGGTAB", "GXTXAYB"));
    }
}
''')

with open("a:/plagiarism/backend/templates.json", "w") as f:
    json.dump(t, f)
print("Updated templates.json with all algorithms")
