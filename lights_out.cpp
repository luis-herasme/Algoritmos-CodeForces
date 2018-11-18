#include <iostream>

using namespace std;

int main()
{
    int matrix[3][3], temp[3][3];

    for (int x = 0; x < 3; x++)
        for (int y = 0; y < 3; y++)
            cin >> matrix[x][y];

    for (int x = 0; x < 3; x++)
        for (int y = 0; y < 3; y++)
        {

            if (matrix[x][y] % 2)
                matrix[x][y] = 1;
            else
                matrix[x][y] = 0;
        }

    for (int x = 0; x < 3; x++)
        for (int y = 0; y < 3; y++)
            temp[x][y] = matrix[x][y];

    for (int x = 0; x < 3; x++)
        for (int y = 0; y < 3; y++)
        {
            if (matrix[x][y])
            {
                if (x + 1 < 3)
                    temp[x + 1][y]++;
                if (x - 1 >= 0)
                    temp[x - 1][y]++;
                if (y + 1 < 3)
                    temp[x][y + 1]++;
                if (y - 1 >= 0)
                    temp[x][y - 1]++;
            }
        }

    bool k = false;
    while (!k)
    {
        k = true;
        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++)
            {
                if (!temp[x][y])
                    temp[x][y] = 1;
                else
                    temp[x][y]--;
                if (temp[x][y] > 1)
                    k = false;
            }
    }

    for (int x = 0; x < 3; x++)
    {
        for (int y = 0; y < 3; y++)
            cout << temp[x][y];
        cout << endl;
    }

    return 0;
}
