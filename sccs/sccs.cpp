#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int f[875714] = {0};
int explored[875714] = {0};
int leader[875714] = {0};

int t = 0;
int s = 0;

int* getEdges(string text) {
    int separation = text.find(" ");
    int start = stoi(text.substr(0, separation));
    int end = stoi(text.substr(separation, text.length()));
    int *result = new int[2]{start, end};
    return result;
}

vector<vector<int>> changeOrder(vector<vector<int>> nodes, vector<int> newOrder) {
    vector<vector<int>> result;
    for (int i = 0; i < newOrder.size(); i++) {
        result.push_back(nodes[newOrder[i]]);
    }
    return result;
}

void DFS(vector<vector<int>> Graph, int i) {
    ::explored[i] = 1;
    ::leader[i] = ::s;

    for (int j: Graph[i]) {
        if (!::explored[j]) {
            DFS(Graph, j);
        }
    }

    ::t = ::t + 1;
    ::f[i] = ::t;
}

void DFS_Loop(vector<vector<int>> Graph) {
    for (int i = 0; i < Graph.size(); i++) {
        if (!::explored[i]) {
            ::s = i;
            DFS(Graph, i);
        }
    }
}

int main() {
    cout << "Hola" << endl;

    vector<vector<int>> G;
    vector<int> node0 = {0};

    G.push_back(node0);

    for (int i = 0; i < 875714; i++) {
        vector<int> node;
        G.push_back(node);
    }


    string text;
    ifstream EdgesFile("sccs.txt");

    int myArray[10] = { 0 };


    while (getline (EdgesFile, text)) {
        int *r = getEdges(text);
        G[r[0]].push_back(r[1]);
    }
    EdgesFile.close();

    for (auto i: G[1]) {
        cout << i << ' ';
    }

    DFS_Loop(G);

    vector<int> f_vec(begin(f), end(f));
    vector<vector<int>> G_ = changeOrder(G, f_vec);
    // nodes_f = [value for (value, index) in sorted(zip(nodes, f), reverse=True)]

    for (int i = 0; i < 875714; i++) {
        cout << leader[i] << endl;
    }

    // for (int i = 0; i < 875714; i++) {
    //     f[i] = 0;
    //     explored[i] = 0;
    //     leader[i] = 0;
    // }

    // DFS_Loop(G_);

    // for (int i = 0; i < 875714; i++) {
    //     cout << leader[i] << endl;
    // }

    // r = {}

    // for i in f:
    //     if r.get(i):
    //         r[i] = r[i] + 1
    //     else:
    //         r[i] = 1
    // print('hola')
    // print(sorted(list(r.values()), reverse=True))
}
