import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

entradas = []

for i in range(t):
    entradas.append(input())

for entrada in entradas:
    r = entrada[:2]
    for i in range(2, len(entrada) - 1, 2):
        r = r + entrada[i + 1]
    print(r)