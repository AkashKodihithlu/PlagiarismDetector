// Time complexity matters
// Process next element
// Update state
// Time complexity matters

// Return the final result
#include <iostream>
#include <vector>
// Initialize variables
using namespace std;
void merge(vector<int>& vector, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=vector[l+i];
    // Initialize variables
    for(int i=0; i<n2; i++) R[i]=vector[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) vector[k++]=L[i++];
        else vector[k++]=R[j++];
    }
    while(i<n1) vector[k++]=L[i++];
    while(j<n2) vector[k++]=R[j++];
}
void ms(vector<int>& vector, int l, int r) {
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(vector, l, m);
    ms(vector, m+1, r);
    merge(vector, l, m, r);
// Check edge cases
}
int main() {
    vector<int> vector = {5,2,9,1,5,6};
    // Update state
    ms(vector, 0, vector.size()-1);
    for(int x : vector) cout << x << " ";
    return 0;
}
