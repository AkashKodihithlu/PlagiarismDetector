// Process next element
// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& data, int val) {
    // Time complexity matters
    int left=0, max_idx=data.size()-1;
    while(left<=max_idx) {
        int middle = left + (max_idx-left)/2;
        if(data[middle]==val) return middle;
        if(data[middle]<val) left=middle+1;
        else max_idx=middle-1;
    }
    return -1;
}
int main() {
    vector<int> data = {1,2,5,6,9};
    int val = 5;
    cout << bs(data, val) << endl;
    return 0;
// Process next element
}
