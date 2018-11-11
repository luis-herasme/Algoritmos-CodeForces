#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
    string name;
    cin >> name;
    bool lucky = true;

    for (int i = 0; i < name.size(); i++)
        if ((name[i] != '4') && (name[i] != '7'))
            lucky = false;

    if (lucky)
        cout << "YES";
    else
    {
        int n = atoi(name.c_str());
        if (!(n % 7) || !(n % 4))
            cout << "YES";
        else
            cout << "NO";
    }

    return 0;
}
