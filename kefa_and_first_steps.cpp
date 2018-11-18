#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int d, c = 1, r = 0;
    cin >> d;
    vector<int> f(d);

    for (int i = 0; i < d; i++)
    {
        cin >> f[i];
        if (f[i] >= f[i - 1])
            c++;
        else
            c = 1;
        if (c > r)
            r = c;
    }

    cout << r;
    return 0;
}
