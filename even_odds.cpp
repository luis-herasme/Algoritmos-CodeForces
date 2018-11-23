#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    double n, k;
    cin >> n >> k;

    if (k > (n + 1) / 2)
        cout << (long long)(k - ceil(n / 2)) * 2;

    else
        cout << (long long)k * 2 - 1;

    return 0;
}
