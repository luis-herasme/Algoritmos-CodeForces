#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    cin >> name;
    bool c = false;
    for (int i = 0; i < name.size(); i++)
        if ((name[i] == 'H') || (name[i] == 'Q') || (name[i] == '9') || (name[i] == '9'))
            c = true;
    if (c)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
