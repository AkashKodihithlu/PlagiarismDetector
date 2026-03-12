// Time complexity matters
// Update state

// Initialize variables
#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& vector, int key) {
    int min_idx=0, high=vector.size()-1;
    while(min_idx<=high) {
        int center = min_idx + (high-min_idx)/2;
        if(vector[center]==key) return center;
        if(vector[center]<key) min_idx=center+1;
        else high=center-1;
    // Helper function here
    }
    return -1;
}
int main() {
    // Time complexity matters
    vector<int> vector = {1,2,5,6,9};
    int key = 5;
    cout << bs(vector, key) << endl;
    return 0;
}

