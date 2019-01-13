#include <iostream>
#include <vector>

using namespace std;
int main()
{
    int n;
    cin >> n;
    vector<int> name(n);
    for (int i = 0; i < n; i++)
    {
        cin >> name[i];
    }

    bool change = true;
    while (change)
    {
        change = false;
        for (int i = 0; i < name.size() - 1; i++)
        {

            if ((name[i] == 0) && (name[i + 1] == 1))
            {
                name.erase(&name[i]);
                name.erase(&name[i]);
                change = true;
            }
            else if ((name[i] == 1) && (name[i + 1] == 0))
            {
                name.erase(&name[i]);
                name.erase(&name[i]);
                change = true;
            }
        }
    }
    cout << name.size();
    return 0;
}
