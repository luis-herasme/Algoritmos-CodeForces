#include <iostream>
using namespace std;
int main()
{
    int n, k, past, present, m = 0, t = 0;
    cin >> n >> k;
    cin >> past;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> present;
        if (past != present)
            t++;
        else
            t = 0;
        if (m < t)
            m = t;
    }
    if (m)
        cout << m;
    else
        cout << 1;
}
