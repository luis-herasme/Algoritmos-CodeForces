#include <iostream>
using namespace std;
int main()
{
    string digits;
    cin >> digits;
    int lucky_digits = 0;

    for (int i = 0; i < digits.size(); i++)
        if ((digits[i] == '4') || (digits[i] == '7'))
            lucky_digits++;

    if (lucky_digits)
    {
        if (!(lucky_digits % 7) || !(lucky_digits % 4) || !(lucky_digits % 47))
            cout << "YES";
        else
            cout << "NO";
    }
    else
        cout << "NO";

    return 0;
}
