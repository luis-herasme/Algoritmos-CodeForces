import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for _ in range(t):
    input() # n
    a = input_list_numbers()
    a = list(set(a))
    a.sort()
    print(len(a))