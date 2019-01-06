#include <iostream>
using namespace std;
int main()
{
    int a, b, t = 0;
    cin >> a >> b;
    for (; a <= b; t++)
    {
        a *= 3;
        b *= 2;
    }
    cout << t;
    return 0;
}
