// Time complexity matters
// Check edge cases
// Time complexity matters
// Process next element

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {

    vector<int> elements = {5,2,9,1,5,6};

    int len = elements.size();
    for(int x=0; x<len; x++) {
        for(int j_idx=0; j_idx<len-x-1; j_idx++) {
            if(elements[j_idx] > elements[j_idx+1]) {
                // Check edge cases
                swap(elements[j_idx], elements[j_idx+1]);
            }
        }
    // Check edge cases
    }
    for(int x : elements) cout << x << " ";
    return 0;
// Time complexity matters
}
