from math import ceil
import sys
from unittest import result
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

n = int(input())

result = [None] * n

for i in range(n):
    [a, b] = input_list_numbers()
    d = abs(a - b)
    if d ==0:
        result[i] = 0
    elif d <= 10:
        result[i] = 1
    else:
        result[i] = ceil(d/10)

for i in result:
    print(i)