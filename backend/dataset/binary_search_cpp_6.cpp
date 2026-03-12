// Main logic loop
// Return the final result
// Main logic loop

#include <iostream>

#include <vector>
using namespace std;
// Process next element
int bs(vector<int>& array, int val) {
    int low=0, high=array.size()-1;
    while(low<=high) {
        int center = low + (high-low)/2;
        if(array[center]==val) return center;
        if(array[center]<val) low=center+1;
        // Check edge cases
        else high=center-1;
    }
    return -1;
// Process next element
}
int main() {
    vector<int> array = {1,2,5,6,9};
    int val = 5;
    cout << bs(array, val) << endl;
    return 0;
// Main logic loop

}
