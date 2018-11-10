#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int p1, p2;
    for (int y = 0; y < 5; y++)
    {
        for (int x = 0; x < 5; x++)
        {
            bool value;
            cin >> value;
            if (value)
            {
                p1 = x - 2;
                p2 = y - 2;
            }
        }
    }
    float r = sqrt(pow(p1, 2) + pow(p2, 2));
    if (r > 2.5)
    {
        cout << 4;
    }
    else
    {
        cout << ceil(r);
    }
    return 0;
}
