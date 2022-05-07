import load_data

G = load_data.load_data()
NODES = 875715

explored = [False] * NODES
leader = [False] * NODES
finishing_times = [False] * NODES

t = 0
run_leader = None

nodes = [[] for _ in range(NODES)]
nodes_rev = [[] for _ in range(NODES)]

for edge in G:
    [i, j] = edge
    nodes[i].append(j)
    nodes_rev[j].append(i)

def DFS_Loop(order, nodes):
    global t, run_leader, explored

    for i in order:
        if not explored[i]:
            run_leader = i
            DFS_iterative(nodes, i)


def DFS_iterative(nodes, v):
    global explored, t, finishing_times, leader, run_leader
    stack = [v]

    while len(stack):
        v = stack.pop()

        if not explored[v]:
            explored[v] = True
            leader[v] = run_leader
            stack.append(v)
            for w in nodes[v]:
                if not explored[w]:
                    stack.append(w)
        else:
            if not finishing_times[v]:
                finishing_times[v] = t
                t = t + 1

DFS_Loop(range(1, len(nodes)), nodes_rev)

finishing_times[0] = NODES - 1
nodes_f = [None] * NODES

nodes_order = list(range(len(nodes)))
for i, f in enumerate(finishing_times):
    nodes_f[finishing_times[i]] = nodes_order[i]
nodes_f = list(reversed(nodes_f))

explored = [False] * NODES
leader = [False] * NODES
finishing_times = [False] * NODES

t = 0
run_leader = None
DFS_Loop(nodes_f, nodes)

leaders = {}

for i in leader:
    if leaders.get(i):
        leaders[i] = leaders[i] + 1
    else:
        if i:
            leaders[i] = 1

print(sorted(list(leaders.values()), reverse=True)[:10])
