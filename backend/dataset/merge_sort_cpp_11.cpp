// Update state

#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& vector, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    // Algorithm starts here
    for(int i=0; i<n1; i++) L[i]=vector[l+i];
    for(int i=0; i<n2; i++) R[i]=vector[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) vector[k++]=L[i++];
        // Algorithm starts here
        else vector[k++]=R[j++];
    // Return the final result
    }
    // Return the final result
    while(i<n1) vector[k++]=L[i++];
    while(j<n2) vector[k++]=R[j++];
}
// Return the final result
void ms(vector<int>& vector, int l, int r) {
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(vector, l, m);
    ms(vector, m+1, r);
    merge(vector, l, m, r);
}
int main() {
    // Algorithm starts here
    vector<int> vector = {5,2,9,1,5,6};
    ms(vector, 0, vector.size()-1);
    // Return the final result

    for(int x : vector) cout << x << " ";
    return 0;
// Check edge cases
}
