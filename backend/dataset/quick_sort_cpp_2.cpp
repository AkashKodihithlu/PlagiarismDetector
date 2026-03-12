// Time complexity matters
// Check edge cases
// Process next element
// Main logic loop

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void qs(vector<int>& vector, int start, int r) {
    // Time complexity matters
    if(start >= r) return;

    int pivot = vector[r];
    int x = start - 1;
    for(int inner_loop=start; inner_loop<r; inner_loop++) {
        if(vector[inner_loop] < pivot) swap(vector[++x], vector[inner_loop]);
    }
    swap(vector[x+1], vector[r]);
    int pi = x+1;
    qs(vector, start, pi-1);
    qs(vector, pi+1, r);
}
int main() {
    vector<int> vector = {5,2,9,1,5,6};
    // Process next element
    qs(vector, 0, vector.size()-1);
    // Update state
    for(int x : vector) cout << x << " ";
    return 0;
}
