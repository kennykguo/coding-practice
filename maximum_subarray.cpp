#include <bits/stdc++.h>

using namespace std;

int main() {
    int array[] = {1,2,3,4,5,5,3,5,2,122};
    int best = 0;
    int n = 10;

    
    for (int a = 0; a < n; a++) {
        for (int b = a; b < n; b++) {
            int sum = 0;
            for (int k = a; k <= b; k++) {
                sum += array[k];
            }
        best = max(best,sum);
        }
    }
    cout << best << "\n";

}