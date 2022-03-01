import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

n = int(input())

ways = 0

for l in range(1, round(n/2) + 1):
    if ( n - l ) % l == 0:
        ways += 1

print(ways)