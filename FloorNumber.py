from math import ceil
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    [n, x] = input_list_numbers()
    if (n == 1 or n == 2):
        print("1")
    else:
        levels = ceil((n - 2) / x) + 1
        print(levels)
