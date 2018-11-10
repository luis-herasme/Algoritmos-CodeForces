#include <iostream>
using namespace std;
int main()
{
    int entran, salen, paradas, maximo = 0, dentro = 0;
    cin >> paradas;

    for (int i = 0; i < paradas; i++)
    {
        cin >> salen;
        cin >> entran;
        dentro += entran - salen;
        if (dentro > maximo)
            maximo = dentro;
    }
    cout << maximo;
    return 0;
}
