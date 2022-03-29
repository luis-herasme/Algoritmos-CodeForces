from math import ceil
import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))

[n, t] = input_list_numbers()
x = ceil(10 ** (n - 1) / t)
ans = 0

while True:
    if t * x >= 10 ** (n - 1) and t * x < 10 ** n:
        print(t * x)
        ans = 1
        break
    elif t * x >= 10 ** n:
        break
    else:
        x0 = ceil((10 ** (n - 1) - t * x) / t)
        x = x + x0

if ans == 0:
    print(-1)
