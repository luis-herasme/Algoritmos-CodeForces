import sys
import math
input = sys.stdin.readline

t = int(input())
result = [0] * t

for i in range(t):
    n = int(input())
    # a > 0, b > 0 & a can be greater than b
    if n >= 3:
        if (n % 2) == 0:
            result[i] = math.floor(n/2) - 1
        else:
            result[i] = math.floor(n/2)

for i in result:
    print(i)
