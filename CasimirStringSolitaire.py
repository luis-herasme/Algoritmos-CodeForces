from re import A
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    s = input()
    A = B = C = 0
    for si in s:
        if si == "A":
            A += 1
        elif si == "B":
            B += 1
        elif si == "C":
            C += 1
    if B == (A + C):
        print("YES")
    else:
        print("NO")