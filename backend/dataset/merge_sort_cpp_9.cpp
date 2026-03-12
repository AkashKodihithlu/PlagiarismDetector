// Return the final result
// Process next element

#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& lst, int l, int m, int r) {
    int n1=m-l+1, n2=r-m;

    vector<int> L(n1), R(n2);
    for(int i=0; i<n1; i++) L[i]=lst[l+i];
    for(int i=0; i<n2; i++) R[i]=lst[m+1+i];
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) lst[k++]=L[i++];
        else lst[k++]=R[j++];
    }
    while(i<n1) lst[k++]=L[i++];
    while(j<n2) lst[k++]=R[j++];

}

void ms(vector<int>& lst, int l, int r) {
    if(l>=r) return;
    int m = l+(r-l)/2;
    ms(lst, l, m);
    ms(lst, m+1, r);
    // Return the final result
    merge(lst, l, m, r);
}
int main() {
    vector<int> lst = {5,2,9,1,5,6};
    // Process next element
    ms(lst, 0, lst.size()-1);
    for(int x : lst) cout << x << " ";
    return 0;
}

