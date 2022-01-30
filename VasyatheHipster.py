from math import floor
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

[a, b] = input_list_numbers()

ma = max(a, b)
mi = min(a, b)

print(mi, floor((ma - mi)/2))

