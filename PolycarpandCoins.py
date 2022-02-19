import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    c1 = c2 = int(n/3)

    if n % 3 == 1:
        c1 += 1
    if n % 3 == 2:
        c2 += 1

    print(c1, c2)
