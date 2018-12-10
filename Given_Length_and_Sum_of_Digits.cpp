#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <numeric>

using namespace std;

bool add_one(vector<int> &vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        if (vec[i] < 9)
        {
            vec[i]++;
            return true;
        }
        else
            vec[i] = 0;
    }
    return false;
}

bool subtract_one(vector<int> &vec)
{
    for (int i = 0; i < vec.size(); i++)
    {
        if (vec[i] > 0)
        {
            vec[i]--;
            return true;
        }
    }
    return false;
}

string print_vec(vector<int> vec)
{
    reverse(vec.begin(), vec.end());
    for (auto i : vec)
        cout << i;
}

vector<int> smallest(vector<int> n, int resultado)
{
    int nueves = floor(resultado / 9);
    int residuo = resultado % 9;
    for (int i = 0; i < nueves && i < n.size(); i++)
        n[i] = 9;

    if (n.size() > nueves)
    {
        if (residuo)
        {
            n[nueves] = residuo - 1;
            if (nueves == n.size() - 1)
            {
                n[nueves] = residuo;
            }
        }
        else
        {
            n[nueves - 1] = 8;
        }
    }

    do
    {
        if (accumulate(n.begin(), n.end(), 0) == resultado)
        {
            return n;
        }
    } while (add_one(n));

    n[0] = -1;
    return n;
}

vector<int> biggest(vector<int> n, int s)
{

    int m = floor(s / 9);
    for (int i = n.size() - 1; i > n.size() - m; i--)
    {
        n[i] = 9;
    }

    do
    {
        if (accumulate(n.begin(), n.end(), 0) == s)
            return n;
    } while (subtract_one(n));
    return {-1};
}

int main()
{
    int m, s;
    cin >> m >> s;
    vector<int> ultimo(m, 9);
    vector<int> primero(m, 0);
    if (m > 1)
    {
        primero[m - 1] = 1;
    }
    if (accumulate(primero.begin(), primero.end(), 0) > s)
        cout << -1 << " " << -1;
    else
    {
        vector<int> small = smallest(primero, s);
        if (small[0] != -1)
        {
            print_vec(small);
            cout << " ";
            print_vec(biggest(ultimo, s));
        }
        else
            cout << -1 << " " << -1;
    }
    return 0;
}
