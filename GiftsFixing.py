import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
a_list = [None] * t
b_list = [None] * t

for i in range(t):
    input() # n
    a_list[i] = input_list_numbers()
    b_list[i] = input_list_numbers()

for i in range(t):
    moves = 0

    a = a_list[i]
    b = b_list[i]

    a_min = min(a)
    b_min = min(b)
    
    n = len(a)
    
    for j in range(n):
        a[j] = a[j] - a_min
        b[j] = b[j] - b_min
        min_ba = min(a[j], b[j])

        if min_ba > 0:
            moves = moves + min_ba
            a[j] = a[j] - min_ba
            b[j] = b[j] - min_ba

    for j in range(n):
        moves = moves + a[j] + b[j]

    print(moves)