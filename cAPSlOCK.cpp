#include <iostream>
#include <string>
using namespace std;

int main()
{
    string words;
    cin >> words;

    bool all_upper = true;
    for (int i = 0; i < words.size(); i++)
        if (!isupper(words[i]))
            all_upper = false;

    bool almost_upper = true;
    if (islower(words[0]))
    {
        for (int i = 1; i < words.size(); i++)
            if (!isupper(words[i]))
                almost_upper = false;
    }
    else
        almost_upper = false;

    if (all_upper || almost_upper)
    {
        for (int i = 0; i < words.size(); i++)
        {

            if (islower(words[i]))
                words[i] = toupper(words[i]);
            else
                words[i] = tolower(words[i]);
        }
    }
    cout << words;
}
