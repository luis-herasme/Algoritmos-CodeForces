#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
    int maximo = 0;
    string nombre, name;
    map<string, int> playes;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> name;
        if (playes[name])
            playes[name]++;
        else
            playes[name] = 1;
        if (playes[name] > maximo)
        {
            nombre = name;
            maximo = playes[name];
        }
    }
    cout << nombre;
    return 0;
}
