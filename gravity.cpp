#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, index_min, min = 101, index_max, max = 0, k = 1;
    cin >> n;
    vector<int> rows(n, 0);

    for (int &i : rows)
        cin >> i;

    for (int i = 0; i < rows.size(); i++)
    {
        if (rows[i] > max)
        {
            max = rows[i];
            index_max = i;
        }

        if (rows[i] <= min)
        {
            min = rows[i];
            index_min = i;
        }
    }

    if (index_max > index_min)
        k++;

    cout << index_max + (n - index_min) - k;
    return 0;
}
