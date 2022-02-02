import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
entradas = [0] * t

for i in range(t):
    entradas[i] = int(input())

for entrada in entradas:
    r = [0] * entrada
    for i in range(int(len(r) / 2)):
        r[i] = 2*(i + 1)
    for (idx, i) in enumerate(range(int(len(r) / 2), len(r))):
        if i != len(r) - 1:
            r[i] = 2*(idx + 1) - 1
        else:
            r[i] = sum(r[: int(len(r)/2)]) - sum(r[int(len(r)/2):])
            if r[i] % 2:
                print("YES")
                print(" ".join(map(str, r)))
                break
            print("NO")
            
    
