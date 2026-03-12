import json

t = {
    "bubble_sort": {"py": [], "c": [], "cpp": [], "java": []},
    "quick_sort": {"py": [], "c": [], "cpp": [], "java": []},
    "merge_sort": {"py": [], "c": [], "cpp": [], "java": []},
    "binary_search": {"py": [], "c": [], "cpp": [], "java": []},
    "dfs": {"py": [], "c": [], "cpp": [], "java": []},
    "bfs": {"py": [], "c": [], "cpp": [], "java": []},
    "dijkstra": {"py": [], "c": [], "cpp": [], "java": []},
    "knapsack": {"py": [], "c": [], "cpp": [], "java": []},
    "fibonacci": {"py": [], "c": [], "cpp": [], "java": []},
    "lcs": {"py": [], "c": [], "cpp": [], "java": []}
}

t["bubble_sort"]["py"].append('''
def solve(VAR_ARR):
    VAR_SIZE = len(VAR_ARR)
    for VAR_I in range(VAR_SIZE):
        for VAR_J in range(0, VAR_SIZE-VAR_I-1):
            if VAR_ARR[VAR_J] > VAR_ARR[VAR_J+1]:
                VAR_ARR[VAR_J], VAR_ARR[VAR_J+1] = VAR_ARR[VAR_J+1], VAR_ARR[VAR_J]
    return VAR_ARR
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
''')
t["bubble_sort"]["c"].append('''
#include <stdio.h>
int main() {
    int VAR_ARR[] = {5,2,9,1,5,6};
    int VAR_SIZE = 6;
    for(int VAR_I=0; VAR_I<VAR_SIZE; VAR_I++) {
        for(int VAR_J=0; VAR_J<VAR_SIZE-VAR_I-1; VAR_J++) {
            if(VAR_ARR[VAR_J] > VAR_ARR[VAR_J+1]) {
                int VAR_TEMP = VAR_ARR[VAR_J];
                VAR_ARR[VAR_J] = VAR_ARR[VAR_J+1];
                VAR_ARR[VAR_J+1] = VAR_TEMP;
            }
        }
    }
    for(int VAR_I=0; VAR_I<VAR_SIZE; VAR_I++) printf("%d ", VAR_ARR[VAR_I]);
    return 0;
}
''')
t["bubble_sort"]["cpp"].append('''
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> VAR_ARR = {5,2,9,1,5,6};
    int VAR_SIZE = VAR_ARR.size();
    for(int VAR_I=0; VAR_I<VAR_SIZE; VAR_I++) {
        for(int VAR_J=0; VAR_J<VAR_SIZE-VAR_I-1; VAR_J++) {
            if(VAR_ARR[VAR_J] > VAR_ARR[VAR_J+1]) {
                swap(VAR_ARR[VAR_J], VAR_ARR[VAR_J+1]);
            }
        }
    }
    for(int x : VAR_ARR) cout << x << " ";
    return 0;
}
''')
t["bubble_sort"]["java"].append('''
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        int[] VAR_ARR = {5,2,9,1,5,6};
        int VAR_SIZE = VAR_ARR.length;
        for(int VAR_I=0; VAR_I<VAR_SIZE; VAR_I++) {
            for(int VAR_J=0; VAR_J<VAR_SIZE-VAR_I-1; VAR_J++) {
                if(VAR_ARR[VAR_J] > VAR_ARR[VAR_J+1]) {
                    int VAR_TEMP = VAR_ARR[VAR_J];
                    VAR_ARR[VAR_J] = VAR_ARR[VAR_J+1];
                    VAR_ARR[VAR_J+1] = VAR_TEMP;
                }
            }
        }
        System.out.println(Arrays.toString(VAR_ARR));
    }
}
''')

t["quick_sort"]["py"].append('''
def solve(VAR_ARR):
    if len(VAR_ARR) <= 1: return VAR_ARR
    pivot = VAR_ARR[len(VAR_ARR) // 2]
    left = [x for x in VAR_ARR if x < pivot]
    mid = [x for x in VAR_ARR if x == pivot]
    right = [x for x in VAR_ARR if x > pivot]
    return solve(left) + mid + solve(right)
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
''')
t["quick_sort"]["c"].append('''
#include <stdio.h>
void qs(int VAR_ARR[], int VAR_LOW, int VAR_HIGH) {
    if (VAR_LOW < VAR_HIGH) {
        int pivot = VAR_ARR[VAR_HIGH];
        int VAR_I = (VAR_LOW - 1);
        for (int VAR_J = VAR_LOW; VAR_J <= VAR_HIGH - 1; VAR_J++) {
            if (VAR_ARR[VAR_J] < pivot) {
                VAR_I++;
                int VAR_TEMP = VAR_ARR[VAR_I];
                VAR_ARR[VAR_I] = VAR_ARR[VAR_J];
                VAR_ARR[VAR_J] = VAR_TEMP;
            }
        }
        int VAR_TEMP = VAR_ARR[VAR_I + 1];
        VAR_ARR[VAR_I + 1] = VAR_ARR[VAR_HIGH];
        VAR_ARR[VAR_HIGH] = VAR_TEMP;
        int pi = VAR_I + 1;
        qs(VAR_ARR, VAR_LOW, pi - 1);
        qs(VAR_ARR, pi + 1, VAR_HIGH);
    }
}
int main() {
    int VAR_ARR[] = {5,2,9,1,5,6};
    int VAR_SIZE = 6;
    qs(VAR_ARR, 0, VAR_SIZE-1);
    for(int VAR_I=0; VAR_I<VAR_SIZE; VAR_I++) printf("%d ", VAR_ARR[VAR_I]);
    return 0;
}
''')
t["quick_sort"]["cpp"].append('''
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void qs(vector<int>& VAR_ARR, int VAR_LOW, int VAR_HIGH) {
    if(VAR_LOW >= VAR_HIGH) return;
    int pivot = VAR_ARR[VAR_HIGH];
    int VAR_I = VAR_LOW - 1;
    for(int VAR_J=VAR_LOW; VAR_J<VAR_HIGH; VAR_J++) {
        if(VAR_ARR[VAR_J] < pivot) swap(VAR_ARR[++VAR_I], VAR_ARR[VAR_J]);
    }
    swap(VAR_ARR[VAR_I+1], VAR_ARR[VAR_HIGH]);
    int pi = VAR_I+1;
    qs(VAR_ARR, VAR_LOW, pi-1);
    qs(VAR_ARR, pi+1, VAR_HIGH);
}
int main() {
    vector<int> VAR_ARR = {5,2,9,1,5,6};
    qs(VAR_ARR, 0, VAR_ARR.size()-1);
    for(int x : VAR_ARR) cout << x << " ";
    return 0;
}
''')
t["quick_sort"]["java"].append('''
import java.util.Arrays;
public class Main {
    static void qs(int[] VAR_ARR, int VAR_LOW, int VAR_HIGH) {
        if(VAR_LOW < VAR_HIGH) {
            int pivot = VAR_ARR[VAR_HIGH];
            int VAR_I = VAR_LOW - 1;
            for(int VAR_J=VAR_LOW; VAR_J<VAR_HIGH; VAR_J++) {
                if(VAR_ARR[VAR_J] < pivot) {
                    VAR_I++;
                    int VAR_TEMP = VAR_ARR[VAR_I];
                    VAR_ARR[VAR_I] = VAR_ARR[VAR_J];
                    VAR_ARR[VAR_J] = VAR_TEMP;
                }
            }
            int VAR_TEMP = VAR_ARR[VAR_I+1];
            VAR_ARR[VAR_I+1] = VAR_ARR[VAR_HIGH];
            VAR_ARR[VAR_HIGH] = VAR_TEMP;
            int pi = VAR_I+1;
            qs(VAR_ARR, VAR_LOW, pi-1);
            qs(VAR_ARR, pi+1, VAR_HIGH);
        }
    }
    public static void main(String[] args) {
        int[] VAR_ARR = {5,2,9,1,5,6};
        qs(VAR_ARR, 0, VAR_ARR.length-1);
        System.out.println(Arrays.toString(VAR_ARR));
    }
}
''')

t["merge_sort"]["py"].append('''
def solve(VAR_ARR):
    if len(VAR_ARR) > 1:
        VAR_MID = len(VAR_ARR)//2
        L = VAR_ARR[:VAR_MID]
        R = VAR_ARR[VAR_MID:]
        solve(L)
        solve(R)
        VAR_I = VAR_J = k = 0
        while VAR_I < len(L) and VAR_J < len(R):
            if L[VAR_I] < R[VAR_J]:
                VAR_ARR[k] = L[VAR_I]
                VAR_I += 1
            else:
                VAR_ARR[k] = R[VAR_J]
                VAR_J += 1
            k += 1
        while VAR_I < len(L):
            VAR_ARR[k] = L[VAR_I]
            VAR_I += 1; k += 1
        while VAR_J < len(R):
            VAR_ARR[k] = R[VAR_J]
            VAR_J += 1; k += 1
    return VAR_ARR
def main():
    print(solve([5,2,9,1,5,6]))
if __name__ == "__main__":
    main()
''')
t["merge_sort"]["c"].append('''
#include <stdio.h>
void merge(int VAR_ARR[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++) L[i] = VAR_ARR[l + i];
    for (j = 0; j < n2; j++) R[j] = VAR_ARR[m + 1 + j];
    i = 0; j = 0; k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) { VAR_ARR[k] = L[i]; i++; }
        else { VAR_ARR[k] = R[j]; j++; }
        k++;
    }
    while (i < n1) { VAR_ARR[k] = L[i]; i++; k++; }
    while (j < n2) { VAR_ARR[k] = R[j]; j++; k++; }
}
void ms(int VAR_ARR[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        ms(VAR_ARR, l, m);
        ms(VAR_ARR, m + 1, r);
        merge(VAR_ARR, l, m, r);
    }
}
int main() {
    int VAR_ARR[] = {5,2,9,1,5,6};
    ms(VAR_ARR, 0, 5);
    for(int i=0; i<6; i++) printf("%d ", VAR_ARR[i]);
    return 0;
}
''')
t["merge_sort"]["cpp"].append('''
#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& VAR_ARR, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=VAR_ARR[l+i];
    for(int i=0; i<n2; i++) R[i]=VAR_ARR[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) VAR_ARR[k++]=L[i++];
        else VAR_ARR[k++]=R[j++];
    }
    while(i<n1) VAR_ARR[k++]=L[i++];
    while(j<n2) VAR_ARR[k++]=R[j++];
}
void ms(vector<int>& VAR_ARR, int l, int r) {
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(VAR_ARR, l, m);
    ms(VAR_ARR, m+1, r);
    merge(VAR_ARR, l, m, r);
}
int main() {
    vector<int> VAR_ARR = {5,2,9,1,5,6};
    ms(VAR_ARR, 0, VAR_ARR.size()-1);
    for(int x : VAR_ARR) cout << x << " ";
    return 0;
}
''')
t["merge_sort"]["java"].append('''
import java.util.Arrays;
public class Main {
    static void merge(int[] VAR_ARR, int l, int m, int r) {
        int n1=m-l+1, n2=r-m;
        int[] L = new int[n1]; int[] R = new int[n2];
        for(int i=0; i<n1; i++) L[i]=VAR_ARR[l+i];
        for(int i=0; i<n2; i++) R[i]=VAR_ARR[m+1+i];
        int i=0, j=0, k=l;
        while(i<n1 && j<n2) {
            if(L[i]<=R[j]) VAR_ARR[k++]=L[i++];
            else VAR_ARR[k++]=R[j++];
        }
        while(i<n1) VAR_ARR[k++]=L[i++];
        while(j<n2) VAR_ARR[k++]=R[j++];
    }
    static void ms(int[] VAR_ARR, int l, int r) {
        if(l<r) {
            int m = l+(r-l)/2;
            ms(VAR_ARR, l, m);
            ms(VAR_ARR, m+1, r);
            merge(VAR_ARR, l, m, r);
        }
    }
    public static void main(String[] args) {
        int[] VAR_ARR = {5,2,9,1,5,6};
        ms(VAR_ARR, 0, VAR_ARR.length-1);
        System.out.println(Arrays.toString(VAR_ARR));
    }
}
''')


t["binary_search"]["py"].append('''
def solve(VAR_ARR, VAR_TARGET):
    VAR_LOW, VAR_HIGH = 0, len(VAR_ARR) - 1
    while VAR_LOW <= VAR_HIGH:
        VAR_MID = (VAR_LOW + VAR_HIGH) // 2
        if VAR_ARR[VAR_MID] == VAR_TARGET: return VAR_MID
        elif VAR_ARR[VAR_MID] < VAR_TARGET: VAR_LOW = VAR_MID + 1
        else: VAR_HIGH = VAR_MID - 1
    return -1
def main():
    VAR_TARGET = 5
    print(solve([1,2,5,6,9], VAR_TARGET))
if __name__ == "__main__":
    main()
''')
t["binary_search"]["c"].append('''
#include <stdio.h>
int bs(int VAR_ARR[], int VAR_LOW, int VAR_HIGH, int VAR_TARGET) {
    while (VAR_LOW <= VAR_HIGH) {
        int VAR_MID = VAR_LOW + (VAR_HIGH - VAR_LOW) / 2;
        if (VAR_ARR[VAR_MID] == VAR_TARGET) return VAR_MID;
        if (VAR_ARR[VAR_MID] < VAR_TARGET) VAR_LOW = VAR_MID + 1;
        else VAR_HIGH = VAR_MID - 1;
    }
    return -1;
}
int main() {
    int VAR_ARR[] = {1,2,5,6,9};
    int VAR_TARGET = 5;
    int res = bs(VAR_ARR, 0, 4, VAR_TARGET);
    printf("%d\\n", res);
    return 0;
}
''')
t["binary_search"]["cpp"].append('''
#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& VAR_ARR, int VAR_TARGET) {
    int VAR_LOW=0, VAR_HIGH=VAR_ARR.size()-1;
    while(VAR_LOW<=VAR_HIGH) {
        int VAR_MID = VAR_LOW + (VAR_HIGH-VAR_LOW)/2;
        if(VAR_ARR[VAR_MID]==VAR_TARGET) return VAR_MID;
        if(VAR_ARR[VAR_MID]<VAR_TARGET) VAR_LOW=VAR_MID+1;
        else VAR_HIGH=VAR_MID-1;
    }
    return -1;
}
int main() {
    vector<int> VAR_ARR = {1,2,5,6,9};
    int VAR_TARGET = 5;
    cout << bs(VAR_ARR, VAR_TARGET) << endl;
    return 0;
}
''')
t["binary_search"]["java"].append('''
public class Main {
    static int bs(int[] VAR_ARR, int VAR_TARGET) {
        int VAR_LOW=0, VAR_HIGH=VAR_ARR.length-1;
        while(VAR_LOW<=VAR_HIGH) {
            int VAR_MID = VAR_LOW + (VAR_HIGH-VAR_LOW)/2;
            if(VAR_ARR[VAR_MID]==VAR_TARGET) return VAR_MID;
            if(VAR_ARR[VAR_MID]<VAR_TARGET) VAR_LOW=VAR_MID+1;
            else VAR_HIGH=VAR_MID-1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] VAR_ARR = {1,2,5,6,9};
        int VAR_TARGET = 5;
        System.out.println(bs(VAR_ARR, VAR_TARGET));
    }
}
''')


t["dfs"]["py"].append('''
def solve(VAR_GRAPH, start):
    VAR_VISITED = set()
    def dfs(VAR_NODE):
        if VAR_NODE not in VAR_VISITED:
            VAR_VISITED.add(VAR_NODE)
            for neighbor in VAR_GRAPH.get(VAR_NODE, []):
                dfs(neighbor)
    dfs(start)
    return VAR_VISITED
def main():
    VAR_GRAPH = {0: [1,2], 1: [2], 2: [0,3], 3: [3]}
    print(solve(VAR_GRAPH, 2))
if __name__ == "__main__":
    main()
''')
t["dfs"]["c"].append('''
#include <stdio.h>
int VAR_GRAPH[4][4] = {{0,1,1,0}, {0,0,1,0}, {1,0,0,1}, {0,0,0,1}};
int VAR_VISITED[4] = {0};
void dfs(int VAR_NODE) {
    VAR_VISITED[VAR_NODE] = 1;
    printf("%d ", VAR_NODE);
    for(int VAR_I=0; VAR_I<4; VAR_I++) {
        if(VAR_GRAPH[VAR_NODE][VAR_I] && !VAR_VISITED[VAR_I]) dfs(VAR_I);
    }
}
int main() {
    dfs(2);
    return 0;
}
''')
t["dfs"]["cpp"].append('''
#include <iostream>
#include <vector>
using namespace std;
void dfs(int VAR_NODE, vector<vector<int>>& VAR_GRAPH, vector<bool>& VAR_VISITED) {
    VAR_VISITED[VAR_NODE] = true;
    cout << VAR_NODE << " ";
    for(int neighbor : VAR_GRAPH[VAR_NODE]) {
        if(!VAR_VISITED[neighbor]) dfs(neighbor, VAR_GRAPH, VAR_VISITED);
    }
}
int main() {
    vector<vector<int>> VAR_GRAPH = {{1,2}, {2}, {0,3}, {3}};
    vector<bool> VAR_VISITED(4, false);
    dfs(2, VAR_GRAPH, VAR_VISITED);
    return 0;
}
''')
t["dfs"]["java"].append('''
import java.util.*;
public class Main {
    static void dfs(int VAR_NODE, int[][] VAR_GRAPH, boolean[] VAR_VISITED) {
        VAR_VISITED[VAR_NODE] = true;
        System.out.print(VAR_NODE + " ");
        for(int VAR_I=0; VAR_I<VAR_GRAPH.length; VAR_I++) {
            if(VAR_GRAPH[VAR_NODE][VAR_I]==1 && !VAR_VISITED[VAR_I]) dfs(VAR_I, VAR_GRAPH, VAR_VISITED);
        }
    }
    public static void main(String[] args) {
        int[][] VAR_GRAPH = {{0,1,1,0},{0,0,1,0},{1,0,0,1},{0,0,0,1}};
        boolean[] VAR_VISITED = new boolean[4];
        dfs(2, VAR_GRAPH, VAR_VISITED);
    }
}
''')


with open("a:/plagiarism/backend/templates.json", "w") as f:
    json.dump(t, f)

print("Created first part of templates.json")
