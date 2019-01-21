#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

vector<int> BFS(vector<vector<int>> grafo, int v)
{
    vector<int> d(grafo.size(), -1);
    queue<int> q;
    d[v] = 0;
    q.push(v);
    while (!q.empty())
    {
        int x = q.front();
        q.pop();
        for (int y : grafo[x])
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

int main()
{
    int n, maximo = -1;
    cin >> n;

    vector<vector<int>> grafo(n);
    vector<int> cabezas(n, 1);

    for (int i = 0; i < n; i++)
    {
        int manager;
        cin >> manager;
        if (manager != -1)
        {
            grafo[i].push_back(manager - 1);
            grafo[manager - 1].push_back(i);
        }
        else
        {
            cabezas[i] = -1;
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (cabezas[i] == -1)
        {
            vector<int> d = BFS(grafo, i);
            sort(d.begin(), d.end());
            if (d[d.size() - 1] > maximo)
            {
                maximo = d[d.size() - 1];
            }
        }
    }

    cout << maximo + 1;
    return 0;
}

/*
    // GRAFO
    for (int x = 0; x < grafo.size(); x++)
    {
        cout << x << " : ";
        for (int y = 0; y < grafo[x].size(); y++)
        {
            cout << grafo[x][y] << ", ";
        }
        cout << endl;
    }
    // CABEZAS
    for (int i = 0; i < n; i++)
    {
        if (cabezas[i] == -1)
            cout << i << endl;
    }
*/