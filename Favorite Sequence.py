import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    input() # n
    b = input_list_numbers()
    r = [None] * len(b)

    if len(b) == 1:
        print(b[0])
    else:
        for i in range(0, len(b) // 2):
            i0 = i * 2
            r[i0] = b[i]
            r[i0 + 1] = b[-(i + 1)]

        if len(b) % 2:
            r[-1] = b[len(b) // 2]

        print(' '.join(map(str, r)))