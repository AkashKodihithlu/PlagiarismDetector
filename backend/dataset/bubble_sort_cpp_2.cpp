// Check edge cases
// Initialize variables
// Time complexity matters

#include <iostream>
#include <vector>
#include <algorithm>
// Return the final result
using namespace std;
// Main logic loop
int main() {
    vector<int> elements = {5,2,9,1,5,6};
    int count = elements.size();
    for(int index=0; index<count; index++) {
        for(int pos2=0; pos2<count-index-1; pos2++) {
            if(elements[pos2] > elements[pos2+1]) {
                swap(elements[pos2], elements[pos2+1]);
            // Algorithm starts here
            }
        }
    }
    for(int x : elements) cout << x << " ";
    return 0;
}
