#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 10;
    int array[] = {1,2,3,4,5,5,3,5,2,122};
    int a = 0, b = n-1;
    int x = 10;
    while (a <= b) {

        int k = (a+b)/2;

        if (array[k] == x) {
            // x found at index k
        }

        if (array[k] > x) b = k-1;

        else a = k+1;
        }
}