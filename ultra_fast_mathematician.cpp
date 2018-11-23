#include <iostream>
#include <string>

using namespace std;

int main()
{
    string line1, line2;
    cin >> line1 >> line2;

    for (int i = 0; i < line1.size(); i++)
        if (line1[i] != line2[i])
            cout << 1;
        else
            cout << 0;

    return 0;
}
