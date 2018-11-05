#include <iostream>
#include <string.h>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    int resultado = 0;
    string entrada;
    cin >> entrada;

    for (int i = 0; i < entrada.size(); i++)
    {
        if (entrada[i] == '1')
        {
            if (resultado < 0)
            {
                resultado = 0;
            }
            resultado++;
        }
        else
        {
            if (resultado > 0)
            {
                resultado = 0;
            }
            resultado--;
        }

        if (resultado > 6)
        {
            cout << "YES";
            break;
        }
        else if (resultado < -6)
        {
            cout << "YES";
            break;
        }
    }
    if (!(resultado > 6) && !(resultado < -6))
    {
        cout << "NO";
    }
    return 0;
}
