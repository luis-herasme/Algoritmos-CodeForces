#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
    string name;
    cin >> name;
    map<char, bool> nombre;
    for (int i = 0; i < name.size(); i++)
    {
        if (!nombre[name[i]])
            nombre[name[i]] = true;
    }
    if (nombre.size() % 2)
        cout << "IGNORE HIM!";
    else
        cout << "CHAT WITH HER!";
    return 0;
}
