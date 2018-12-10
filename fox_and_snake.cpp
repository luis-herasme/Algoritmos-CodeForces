#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, m, end = true;
    cin >> n >> m;
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < m; x++)
        {
            if (y % 2)
            {
                if (x == m - 1 && end)
                {
                    cout << "#";
                }
                else if (x == 0 && !end)
                {
                    cout << "#";
                }
                else
                {
                    cout << ".";
                }
            }
            else
            {
                cout << "#";
            }
        }
        if (y % 2)
            end = !end;
        cout << endl;
    }
    return 0;
}
