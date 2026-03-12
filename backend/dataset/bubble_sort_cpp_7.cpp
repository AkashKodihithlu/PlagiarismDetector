// Algorithm starts here
// Check edge cases
// Algorithm starts here

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> array = {5,2,9,1,5,6};
    int size = array.size();
    for(int x=0; x<size; x++) {
        // Helper function here
        for(int inner_loop=0; inner_loop<size-x-1; inner_loop++) {
            if(array[inner_loop] > array[inner_loop+1]) {
                swap(array[inner_loop], array[inner_loop+1]);
            }
        }
    }
    // Initialize variables
    for(int x : array) cout << x << " ";
    return 0;
}
