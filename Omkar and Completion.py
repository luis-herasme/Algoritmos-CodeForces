from math import floor
import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    n = int(input())
    r = ["44"] * (n // 2)
    r = r + ["384"] * (n // 2)
    if n % 2:
        r = r + ["44"]
    print(" ".join(r))
