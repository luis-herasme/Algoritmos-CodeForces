#include <iostream>

using namespace std;

int main()
{
    int c = 0;
    string games;
    cin >> games >> games;
    for (char i : games)
        if (i == 'A')
            c++;
        else
            c--;

    if (c < 0)
        cout << "Danik";
    else if (c > 0)
        cout << "Anton";
    else
        cout << "Friendship";

    return 0;
}
