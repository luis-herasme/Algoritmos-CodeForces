from cmath import inf
from math import floor, log2
from copy import deepcopy
from random import random

# Loading data from text file.
f = open("min_cut.txt", "r")
content = f.read()
content = content.split('\n')
result = []
for i in range(len(content)):
    row = content[i].split('\t')
    row = row[:-1]
    for j in range(len(row)):
        row[j] = int(row[j])
    result.append(row)
graph = result

# fix the indexes
for row in range(len(graph)):
    for node in range(len(graph[row])):
        graph[row][node] = graph[row][node] - 1
GRAPH = graph.copy()


def pick_random_edge(g):
    col_idx = 0
    row_idx = 0

    while col_idx == row_idx:
        row_idx = floor(random() * len(g))
        col_row_idx = floor(random() * len(g[row_idx]))
        col_idx = g[row_idx][col_row_idx]

    return row_idx, col_idx


def merge(g, row_idx, col_idx):
    g[row_idx] = g[row_idx] + g[col_idx]

    for row in range(len(g)):
        for node in range(len(g[row])):
            if g[row][node] == col_idx:
                g[row][node] = row_idx
            if g[row][node] >= col_idx:
                g[row][node] = g[row][node] - 1

    del g[col_idx]

    if col_idx <= row_idx:
        new_row_idx = row_idx - 1
    else:
        new_row_idx = row_idx

    return new_row_idx


def remove_self_loops(g, new_row_idx):
    new_row = []
    for element in range(len(g[new_row_idx])):
        if g[new_row_idx][element] != new_row_idx:
            new_row.append(g[new_row_idx][element])
    g[new_row_idx] = new_row


def min_cut(g):
    while len(g) > 2:
        row_idx, col_idx = pick_random_edge(g)
        new_row_idx = merge(g, row_idx, col_idx)
        remove_self_loops(g, new_row_idx)
    return g


print(GRAPH)

results = []
print("int( ( len(GRAPH) ** 2) * log2(len(GRAPH))): ",
      int((len(GRAPH) ** 2) * log2(len(GRAPH))))


min_val = inf
for i in range(int((len(GRAPH) ** 2) * log2(len(GRAPH)))):
    g_ = deepcopy(GRAPH)
    g0 = min_cut(g_)
    r = min(len(g0[0]), len(g0[1]))
    results.append(r)
    if r < min_val:
        min_val = r
    print(i + 1, ") ", min(len(g0[0]), len(g0[1])))
    print("min: ", min_val)

print("min(results): ", min(results))
