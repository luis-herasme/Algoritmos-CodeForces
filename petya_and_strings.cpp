#include <iostream>
#include <string.h>
#include <string>
#include <math.h>

using namespace std;

int buscar(char letra, string letras)
{
    for (int i = 0; i < letras.size(); i++)
    {
        if (letras[i] == letra)
        {
            return i;
        }
    }
    return -1;
}

int getSize(string letras)
{
    string alfabeto = "abcdefghijklmnopqrstuvwxyz";
    int result = 0;
    cout << "-----------------------------------------------------" << endl;
    cout << "Palabra: " << letras << endl;
    for (int i = 0; i < letras.size(); i++)
    {
        int r = buscar(letras[i], alfabeto) + 1;
        if (r > 0)
        {
            cout << "Letra: " << letras[i] << " " << r << endl;

            result += r;
        }
        else
        {
            cout << "ERROR LETRA NO ENCONTRADA: " << letras[i] << endl;
        }
    }
    return result;
}

string lowerCase(string letras)
{
    for (int i = 0; i < letras.size(); i++)
    {
        letras[i] = tolower(letras[i]);
    }
    return letras;
}

int main()
{
    int resultado = 0;

    string entrada1;
    cin >> entrada1;

    string entrada2;
    cin >> entrada2;
    int size1 = getSize(lowerCase(entrada1));
    int size2 = getSize(lowerCase(entrada2));
    cout << size1 << endl;
    cout << size2 << endl;
    if (size1 > size2)
    {
        cout << "1";
    }
    else if (size1 == size2)
    {
        cout << "0";
    }
    else
    {
        cout << "-1";
    }

    return 0;
}

/*
asdlkjad lks = 42
asdlkjad jwi = 

*/