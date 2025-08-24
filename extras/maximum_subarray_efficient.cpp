#include <bits/stdc++.h>

using namespace std;

int main() {
    int array[] = {1,2,-2,4,5,-100,3,5,2,4};
    int best = 0;
    int n = 10;

    for (int a = 0; a < n; a++) {
        int sum = 0;
        for (int b = a; b < n; b++) {
        sum += array[b];
            best = max(best,sum);
        }
    }
    cout << best << "\n";


}