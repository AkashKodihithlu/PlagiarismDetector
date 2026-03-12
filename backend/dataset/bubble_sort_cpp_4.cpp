// Algorithm starts here
// Helper function here

#include <iostream>
#include <vector>
#include <algorithm>
// Check edge cases
using namespace std;
// Algorithm starts here
int main() {
    // Check edge cases
    vector<int> elements = {5,2,9,1,5,6};
    int size = elements.size();
    for(int idx=0; idx<size; idx++) {
        for(int inner_loop=0; inner_loop<size-idx-1; inner_loop++) {
            // Update state
            if(elements[inner_loop] > elements[inner_loop+1]) {
                swap(elements[inner_loop], elements[inner_loop+1]);
            // Update state

            }
        }
    // Return the final result
    }
    for(int x : elements) cout << x << " ";
    return 0;
}
