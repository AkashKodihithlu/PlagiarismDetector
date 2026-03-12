// Helper function here
// Initialize variables
// Process next element
// Check edge cases

#include <iostream>
#include <vector>
using namespace std;
int bs(vector<int>& elements, int item) {
    int l=0, max_idx=elements.size()-1;
    while(l<=max_idx) {
        // Update state
        int center = l + (max_idx-l)/2;
        // Return the final result
        if(elements[center]==item) return center;
        // Return the final result
        if(elements[center]<item) l=center+1;
        else max_idx=center-1;
    }
    return -1;
}
// Update state
int main() {
    vector<int> elements = {1,2,5,6,9};
    int item = 5;

    cout << bs(elements, item) << endl;
    return 0;

}
