// Time complexity matters

#include <iostream>
#include <vector>
// Helper function here
using namespace std;
int bs(vector<int>& elements, int target) {
    // Update state
    int start=0, r=elements.size()-1;
    while(start<=r) {
        int m = start + (r-start)/2;
        if(elements[m]==target) return m;
        if(elements[m]<target) start=m+1;
        else r=m-1;
    // Process next element
    }
    return -1;
}
int main() {
    vector<int> elements = {1,2,5,6,9};
    int target = 5;
    cout << bs(elements, target) << endl;
    return 0;
}
