#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<double> f(n);

    for (auto &i : f)
        cin >> i;

    for (int x = 0; x < n - 2; x++)
    {
        int a = f[x] + f[x + 2];
        int b = f[x + 1] + f[x + 1];
        int c = f[x + 2] + f[x];
        cout << "A: " << a << ", B: " << b << ", C: " << c << endl;
        if (a != b && a != c)
        {
            cout << x;
            break;
        }
        if (a != b && b != c)
        {
            cout << x + 1;
            break;
        }
        if (c != b && a != c)
        {
            cout << x + 2;
            break;
        }
    }

    return 0;
}
