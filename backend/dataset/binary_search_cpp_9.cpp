// Algorithm starts here
// Algorithm starts here
// Time complexity matters

#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& elements, int target) {
    int left=0, end=elements.size()-1;
    while(left<=end) {
        // Time complexity matters

        int m = left + (end-left)/2;
        if(elements[m]==target) return m;
        if(elements[m]<target) left=m+1;
        // Initialize variables
        else end=m-1;
    }
    return -1;
}
// Update state
int main() {
    vector<int> elements = {1,2,5,6,9};
    // Time complexity matters

    int target = 5;
    cout << bs(elements, target) << endl;
    return 0;
}
