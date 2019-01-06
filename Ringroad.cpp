#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long long n, m, d = 0;
    cin >> n >> m;
    vector<long long> casas(m + 1);
    casas[0] = 1;

    for (long long i = 1; i < m + 1; i++)
        cin >> casas[i];

    for (long long i = 0; i < m; i++)
    {
        if (casas[i] > casas[i + 1])
            d += n - (casas[i] - casas[i + 1]);
        else
            d += casas[i + 1] - casas[i];
    }
    cout << d;
    return 0;
}
