#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, t;
    bool k = true;
    cin >> n >> t;
    vector<char> f(n);

    for (int i = 0; i < n; i++)
        cin >> f[i];

    for (int x = 0; x < t; x++)
        for (int w = n - 2; w >= 0; w--)
        {
            if ((f[w] == 'B') && (f[w + 1] == 'G') && k)
            {
                f[w + 1] = 'B';
                f[w] = 'G';
                k = false;
            }
            else
                k = true;
        }

    for (auto i : f)
        cout << i << " ";

    return 0;
}
