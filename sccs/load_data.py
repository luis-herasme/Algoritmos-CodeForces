
def load_data():
    G = []

    f = open("sccs.txt", "r")
    content = f.read()
    content = content.split('\n')

    for i in range(len(content)):
        [v, u] = content[i].split(' ')[:-1]
        v = int(v)
        u = int(u)
        G.append([v, u])
    return G