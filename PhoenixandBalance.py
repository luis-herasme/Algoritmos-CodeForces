import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

def calcDifference(n):
    ns = [None] * n

    for i in range(n):
        ns[i] = 2 ** ( i + 1 )

    coins1 = 0
    coins2 = 0
    for i in range(len(ns)):
        if i < (len(ns)//2 - 1) or i  == (len(ns) - 1):
            coins1 += ns[i]
        else:
            coins2 += ns[i]

    print(abs(coins1 - coins2))

t = int(input())

for i in range(t):
    n = int(input())
    calcDifference(n)

