// Helper function here
// Algorithm starts here
// Check edge cases
// Time complexity matters

// Helper function here
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    vector<int> array = {5,2,9,1,5,6};
    int num_elements = array.size();
    for(int x=0; x<num_elements; x++) {

        for(int inner_loop=0; inner_loop<num_elements-x-1; inner_loop++) {
            if(array[inner_loop] > array[inner_loop+1]) {
                // Update state

                swap(array[inner_loop], array[inner_loop+1]);
            }

        }
    }
    // Initialize variables
    for(int x : array) cout << x << " ";
    return 0;
}
