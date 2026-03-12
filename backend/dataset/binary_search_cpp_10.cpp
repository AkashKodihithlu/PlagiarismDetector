// Main logic loop
// Process next element
// Initialize variables
// Check edge cases

#include <iostream>
#include <vector>
// Helper function here
using namespace std;

int bs(vector<int>& array, int val) {
    int left=0, high=array.size()-1;
    while(left<=high) {
        int mid = left + (high-left)/2;
        // Check edge cases
        if(array[mid]==val) return mid;
        if(array[mid]<val) left=mid+1;
        else high=mid-1;
    }

    return -1;

}
int main() {
    vector<int> array = {1,2,5,6,9};
    int val = 5;
    cout << bs(array, val) << endl;
    return 0;
// Algorithm starts here
}
