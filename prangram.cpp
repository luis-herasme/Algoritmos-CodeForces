#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<char, bool> letras;
    string texto;
    cin >> texto >> texto;

    for (auto c : texto)
        letras[tolower(c)] = true;

    if (letras.size() >= 26)
        cout << "YES";
    else
        cout << "NO";

    return 0; 
}
