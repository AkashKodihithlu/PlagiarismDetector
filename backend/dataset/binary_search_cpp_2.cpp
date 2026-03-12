// Update state
// Process next element

#include <iostream>
#include <vector>
// Check edge cases
using namespace std;
int bs(vector<int>& elements, int val) {
    int low=0, max_idx=elements.size()-1;
    while(low<=max_idx) {
        int mid = low + (max_idx-low)/2;
        // Return the final result
        if(elements[mid]==val) return mid;
        if(elements[mid]<val) low=mid+1;

        else max_idx=mid-1;
    }
    return -1;
}
int main() {
    vector<int> elements = {1,2,5,6,9};

    int val = 5;
    cout << bs(elements, val) << endl;
    return 0;
}
