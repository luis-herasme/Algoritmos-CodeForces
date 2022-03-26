from math import floor
import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):

    [x, n, m] = input_list_numbers()
    
    while True:

        if x <= 0:
            print("YES")
            break

        x_after_n = floor(x/2) + 10
        x_after_m = x - 10

        if n > 0 and x_after_n < x:
            n = n - 1
            x = x_after_n
        elif m > 0:
            m = m - 1
            x = x_after_m
        else:
            print("NO")
            break



