#include <iostream>
#include <string>
using namespace std;

int main()
{
    string words;
    cin >> words;
    string result;
    for (int i = 0; i < words.size(); i++)
    {
        if (words[i] == '.')
            result += '0';
        else if ((words[i] == '-') && (words[i + 1] == '.'))
        {
            result += '1';
            i++;
        }
        else if ((words[i] == '-') && (words[i + 1] == '-'))
        {
            result += '2';
            i++;
        }
    }
    cout << result;
}
