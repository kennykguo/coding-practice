

#include <bits/stdc++.h>
using namespace std;
int main() {
    int m = 7;
    int n = 10;
    long long x = 1;
    for (int i = 2; i <= n; i++) {
        x = (x*i);
    }
    cout << x << "\n";

}