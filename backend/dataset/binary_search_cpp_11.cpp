// Update state

// Initialize variables
#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& elements, int val) {
    int low=0, end=elements.size()-1;
    while(low<=end) {
        int mid = low + (end-low)/2;
        if(elements[mid]==val) return mid;
        // Helper function here
        if(elements[mid]<val) low=mid+1;
        else end=mid-1;
    }
    return -1;
// Return the final result
}
int main() {
    vector<int> elements = {1,2,5,6,9};
    // Update state
    int val = 5;
    cout << bs(elements, val) << endl;

    return 0;
}
