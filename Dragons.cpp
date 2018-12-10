#include <iostream>
#include <vector>

using namespace std;

struct dragon
{
    int fuerza;
    int recompenza;
};

int main()
{
    int n, s;
    vector<dragon> dragones;
    cin >> s >> n;

    for (int i = 0; i < n; i++)
    {
        dragon d;
        cin >> d.fuerza >> d.recompenza;
        dragones.push_back(d);
    }
    while (dragones.size())
    {
        bool next = false;
        for (int i = 0; i < dragones.size(); i++)
        {
            if (s > dragones[i].fuerza)
            {
                s += dragones[i].recompenza;
                dragones.erase(dragones.begin() + i);
                next = true;
            }
        }
        if (!next)
        {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}
