// Initialize variables
// Helper function here
// Process next element

#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& array, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=array[l+i];
    for(int i=0; i<n2; i++) R[i]=array[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) array[k++]=L[i++];
        else array[k++]=R[j++];
    }
    while(i<n1) array[k++]=L[i++];
    // Process next element
    while(j<n2) array[k++]=R[j++];
}
void ms(vector<int>& array, int l, int r) {
    // Main logic loop
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(array, l, m);
    ms(array, m+1, r);
    merge(array, l, m, r);
}
int main() {
    vector<int> array = {5,2,9,1,5,6};

    ms(array, 0, array.size()-1);
    for(int x : array) cout << x << " ";
    return 0;
}
