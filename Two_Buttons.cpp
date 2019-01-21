#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAXV = 1000000;
bool stop = false;
vector<vector<int>> arbol(MAXV, vector<int>(2));

vector<int> BFS(int v)
{
    vector<int> d(MAXV, -1);
    queue<int> q;
    d[v] = 0;
    q.push(v);
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        for (int y : arbol[x])
        {
            if (d[y] == -1)
            {
                d[y] = d[x] + 1;
                q.push(y);
            }
        }
    }
    return d;
}

int generate(int value, int end)
{

    if (value > 0 && value < MAXV)
    {
        if (value != end && !stop)
        {
            if (!arbol[value][0])
            {
                arbol[value][0] = value - 1;
                generate(value - 1, end);
            }
            if (!arbol[value][1])
            {
                arbol[value][1] = 2 * value;
                generate(2 * value, end);
            }
        }
        else
        {
            stop = true;
        }
    }
}

int main()
{
    int s, f;
    cin >> s >> f;
    generate(s, f);

    vector<int> d = BFS(s);

    if ((arbol[f / 2][0] || arbol[f / 2][1]) && (f % 2 == 0))
    {
        cout << d[f / 2] + 1 << endl;
    }
    else if (arbol[f + 1][0] || arbol[f + 1][1])
    {
        cout << d[f + 1] + 1 << endl;
    }
    return 0;
}
