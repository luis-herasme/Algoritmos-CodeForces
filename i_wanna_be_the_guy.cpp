#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, p1, p2, temp, c = 0;
    cin >> n >> p1;
    vector<bool> levels(n, false);

    for (int i = 0; i < p1; i++)
    {
        cin >> temp;
        levels[temp - 1] = true;
    }

    cin >> p2;

    for (int i = 0; i < p2; i++)
    {
        cin >> temp;
        levels[temp - 1] = true;
    }

    for (bool i : levels)
        if (i)
            c++;

    if (c == n)
        cout << "I become the guy.";
    else
        cout << "Oh, my keyboard!";

    return 0;
}
