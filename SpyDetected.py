import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
listas = [None] * t
for i in range(t):
    input() # n
    listas[i] = input_list_numbers()

for lista in listas:
    if lista[0] == lista[1] and lista[1] == lista[2]:
        for idx, elemento in enumerate(lista):
            if elemento != lista[0]:
                print(idx + 1)
    elif lista[0] == lista[1] and lista[1] != lista[2]:
        print(3)
    elif lista[0] == lista[2] and lista[1] != lista[2]:
        print(2)
    else:
        print(1)