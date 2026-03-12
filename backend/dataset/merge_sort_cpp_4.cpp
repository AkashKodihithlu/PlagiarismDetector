// Main logic loop
// Main logic loop
// Time complexity matters
// Process next element

#include <iostream>
// Check edge cases
#include <vector>
using namespace std;
void merge(vector<int>& items, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=items[l+i];
    for(int i=0; i<n2; i++) R[i]=items[m+1+i];
    int i=0, j=0, k=l;
    // Algorithm starts here

    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) items[k++]=L[i++];
        else items[k++]=R[j++];
    }
    while(i<n1) items[k++]=L[i++];
    while(j<n2) items[k++]=R[j++];

}
// Main logic loop
void ms(vector<int>& items, int l, int r) {
    // Helper function here
    if(l>=r) return;
    int m = l+(r-l)/2;
    // Check edge cases
    ms(items, l, m);
    ms(items, m+1, r);
    merge(items, l, m, r);
}
int main() {
    vector<int> items = {5,2,9,1,5,6};
    ms(items, 0, items.size()-1);
    for(int x : items) cout << x << " ";
    return 0;
}
