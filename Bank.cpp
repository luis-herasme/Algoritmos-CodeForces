#include <iostream>
#include <string>
using namespace std;

int main()
{
    string balance;
    cin >> balance;

    if (balance[0] == '-')
    {
        if (balance.size() >= 2)
        {
            if (balance[balance.size() - 1] > balance[balance.size() - 2])
                balance.erase(balance.end() - 1, balance.end());

            else
                balance.erase(balance.end() - 2, balance.end() - 1);

            if (balance.size() == 2 && balance[1] == '0')
                cout << balance[1];

            else
                cout << balance;
        }
    }
    else
    {
        cout << balance;
    }
}
