#include <iostream>

using namespace std;

bool is_prime(int n)
{
    for (int i = 2; i < n; i++)
        if (!(n % i))
            return false;
    return true;
}

int main()
{

    int n, r = 4;
    cin >> n;

    if (!(n % 2))
    {
        if (!is_prime(n / 2))
            cout << n / 2 << " " << n / 2;
        else
            cout << (n / 2) + 1 << " " << (n / 2) - 1;
    }
    else
    {
        while (is_prime(r) || is_prime(n - r))
            r++;
        cout << n - r << " " << r;
    }
    return 0;
}
