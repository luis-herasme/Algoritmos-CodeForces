#include <iostream>

using namespace std;

int main()
{
    int n, h, p, c = 0;
    cin >> n >> h;
    for (int i = 0; i < n; i++)
    {
        cin >> p;
        if (p > h)
            c++;
    }
    cout << c + n;
    return 0;
}
