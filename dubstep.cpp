#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    vector<char> real_song;
    string song;
    cin >> song;

    for (int i = 0; i < song.size();)
        if (!(song[i] == 'W' && song[i + 1] == 'U' && song[i + 2] == 'B'))
        {
            real_song.push_back(song[i]);
            i++;
        }
        else
        {
            if (real_song.size() && real_song[real_song.size() - 1] != ' ')
                real_song.push_back(' ');
            i += 3;
        }

    for (auto i : real_song)
        cout << i;

    return 0;
}
