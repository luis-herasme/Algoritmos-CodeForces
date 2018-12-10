#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, m, t, r = 0;
    cin >> n >> m;
    t = m - 1;

    for (int i = 0; i < n; i++)
    {
        if (t)
        {
            t--;
        }
        else
        {
            t = m - 1;
            i--;
        }
        r++;
    }
    cout << r;
    return 0;
}
