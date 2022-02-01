from math import ceil, floor
import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

inp = input_list_numbers()
n = inp[0]
abc = inp[1:]
abc.sort()
answer = False

results = []

for n1 in range(ceil(n/abc[0]) + 1):
    if n1 * abc[0] > n:
        break
    for n2 in range(ceil(n/abc[1]) + 1):
        if n1 * abc[0] + n2 * abc[1] > n:
            break
        for n3 in range(ceil(n/abc[2]) + 1):
            if n1 * abc[0] + n2 * abc[1] + n3 * abc[2] > n:
                break
            if n1 * abc[0] + n2 * abc[1] + n3 * abc[2] == n:
                results.append(n1 + n2 + n3)
                
print(max(results))