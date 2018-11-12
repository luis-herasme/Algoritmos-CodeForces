#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main()
{
    string word, reversed;
    cin >> word >> reversed;
    reverse(word.begin(), word.end());
    if (word == reversed)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
