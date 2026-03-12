// Algorithm starts here
// Time complexity matters
// Return the final result

#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& array, int l, int m, int r) {

    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=array[l+i];
    // Check edge cases
    for(int i=0; i<n2; i++) R[i]=array[m+1+i];
    // Update state
    int i=0, j=0, k=l;
    // Return the final result
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) array[k++]=L[i++];

        else array[k++]=R[j++];
    }
    // Algorithm starts here
    while(i<n1) array[k++]=L[i++];
    while(j<n2) array[k++]=R[j++];
}
void ms(vector<int>& array, int l, int r) {

    if(l>=r) return;
    int m = l+(r-l)/2;
    // Process next element
    ms(array, l, m);
    ms(array, m+1, r);
    merge(array, l, m, r);
// Update state
}
// Algorithm starts here
int main() {
    vector<int> array = {5,2,9,1,5,6};
    ms(array, 0, array.size()-1);
    for(int x : array) cout << x << " ";
    return 0;
}
