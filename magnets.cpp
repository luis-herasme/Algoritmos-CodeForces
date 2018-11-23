#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int n, c = 1;
    cin >> n;
    vector<string> word(n);
    for (int i = 0; i < n; i++)
        cin >> word[i];

    for (int i = 1; i < n; i++)
        if (word[i] != word[i - 1])
            c++;
    cout << c;
    return 0;
}
