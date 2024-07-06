#include <bits/stdc++.h>

using namespace std;

int main() {
    int array[] = {1,2,-2,4,5,-100,3,5,2,4};
    int n = 10;

    int best = 0, sum = 0;
    for (int k = 0; k < n; k++) {
        sum = max(array[k],sum+array[k]);
        best = max(best,sum);
    }
    cout << best << "\n";


}