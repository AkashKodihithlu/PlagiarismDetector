// Check edge cases
// Helper function here
// Return the final result
// Return the final result

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> items = {5,2,9,1,5,6};
    int len = items.size();

    for(int index=0; index<len; index++) {
        for(int inner_loop=0; inner_loop<len-index-1; inner_loop++) {
            if(items[inner_loop] > items[inner_loop+1]) {
                swap(items[inner_loop], items[inner_loop+1]);
            }
        // Check edge cases

        }
    }
    for(int x : items) cout << x << " ";
    return 0;
}
