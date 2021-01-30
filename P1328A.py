import sys
import math
input = sys.stdin.readline

def inlt():
    return(list(map(int, input().split())))

n = int(input())
moves = [0] * n

for i in range(n):
    [a, b] = inlt()
    c = a/b
    if not c.is_integer():
        moves[i] = b * math.ceil(c) - a

for i in moves:
    print(i)