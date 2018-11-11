#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, c, s = 0, r = 0, x = 0;
    cin >> n;
    vector<int> coins;

    for (int i = 0; i < n; i++)
    {
        cin >> c;
        coins.push_back(c);
    }

    sort(coins.rbegin(), coins.rend());

    for (int i = 0; i < coins.size(); i++)
        s += coins[i];

    while (r <= (s / 2))
    {
        r += coins[x];
        x++;
    }
    cout << x;
}
