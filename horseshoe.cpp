#include <iostream>
#include <map>

using namespace std;

int main()
{
    int r = 0, t;
    map<int, bool> shoes;

    for (int i = 0; i < 4; i++)
    {
        cin >> t;
        shoes[t] = true;
    }

    cout << 4 - shoes.size();
    return 0;
}
