#include <iostream>

using namespace std;

int main()
{
    int a, b, t, r = 0;
    cin >> a >> b;
    t = b;

    for (int i = 0; i < a; i++)
    {
        t--;
        if (!t)
        {
            i--;
            t = b;
        }
        r++;
    }
    cout << r;
    return 0;
}
