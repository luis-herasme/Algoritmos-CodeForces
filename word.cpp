#include <iostream>
#include <string>

using namespace std;

int main()
{
    int c = 0;
    string word;
    cin >> word;

    for (char &i : word)
        if (islower(i))
            c--;
        else
            c++;

    if (c <= 0)
        for (char &i : word)
            i = tolower(i);
    else
        for (char &i : word)
            i = toupper(i);

    for (char i : word)
        cout << i;

    return 0;
}
