import math
import sys
input = sys.stdin.readline
 
def input_list_numbers():
    return(list(map(int, input().split())))
 
 
t = int(input())

for _ in range(t):
    steps = 0
    [a, b, n] = input_list_numbers()

    while True:

        if a > n or b > n:
            print(steps)
            break

        if a < b:
            a += b
        else:
            b += a

        steps += 1
    
        
