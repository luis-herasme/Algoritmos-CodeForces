import sys
import math

def input():
    r = sys.stdin.readline()
    return r[: len(r) - 1]

l1 = input()
l2 = input()
l3 = input()

if len(l3) >= (len(l2) + len(l1)):
    l3 = sorted(l3)
    lt = l1 + l2
    lt = sorted(lt[:len(l3)])

    if lt == l3:
        print("YES")
    else:
        print("NO")

else:
    print("NO")