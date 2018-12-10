#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<string> nombres = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
    int n, who = 0, counter = 1, increment = 1;
    cin >> n;
    while (n > counter)
    {
        who++;
        counter += increment;
        if (who == 4)
            increment *= 2;
        if (who == 5)
            who = 0;
    }
    cout << nombres[who] << endl;
}
