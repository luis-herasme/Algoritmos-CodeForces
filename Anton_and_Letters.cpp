#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

int main()
{
    string conjunto_string;
    getline(cin, conjunto_string);
    map<char, bool> conjunto;
    conjunto_string = conjunto_string.substr(0, conjunto_string.size() - 1);
    conjunto_string = conjunto_string.substr(1, conjunto_string.size());
    for (int i = 0; i < conjunto_string.size(); i += 3)
    {
        if (!conjunto[conjunto_string[i]])
            conjunto[conjunto_string[i]] = true;
    }
    cout << conjunto.size();
    return 0;
}
