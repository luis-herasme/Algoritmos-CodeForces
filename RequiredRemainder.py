import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())
tests = []

for i in range(t):
    tests.append(input_list_numbers())

for test in tests:
    [x, y, n] = test
    k = n
    for i in range(n + 1):
        if k % x < y:
            k = k - k % x 
        elif k % x == y:
            print(k)
            break
        k = k - 1