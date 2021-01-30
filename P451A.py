import sys
input = sys.stdin.readline

def inlt():
    return(list(map(int, input().split())))

[n, m] = inlt()
plays = min(n, m)

if plays % 2:
    print("Akshat")
else:
    print("Malvika")