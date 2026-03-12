// Main logic loop
// Algorithm starts here

#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& data, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;
    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=data[l+i];
    for(int i=0; i<n2; i++) R[i]=data[m+1+i];
    // Initialize variables

    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) data[k++]=L[i++];
        else data[k++]=R[j++];
    }
    while(i<n1) data[k++]=L[i++];
    while(j<n2) data[k++]=R[j++];
}
void ms(vector<int>& data, int l, int r) {
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(data, l, m);
    ms(data, m+1, r);
    merge(data, l, m, r);
}
int main() {
    vector<int> data = {5,2,9,1,5,6};
    ms(data, 0, data.size()-1);
    for(int x : data) cout << x << " ";
    return 0;
}

