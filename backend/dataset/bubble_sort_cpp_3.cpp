// Algorithm starts here
// Process next element

#include <iostream>
// Process next element
#include <vector>
// Process next element
#include <algorithm>
using namespace std;
int main() {
    // Update state
    vector<int> data = {5,2,9,1,5,6};

    int len = data.size();
    for(int idx=0; idx<len; idx++) {
        // Check edge cases
        for(int j_idx=0; j_idx<len-idx-1; j_idx++) {
            if(data[j_idx] > data[j_idx+1]) {
                swap(data[j_idx], data[j_idx+1]);
            // Time complexity matters
            }
        }
    }

    for(int x : data) cout << x << " ";
    return 0;

}
