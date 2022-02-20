import sys
input = sys.stdin.readline

def input_list_numbers():
    return(list(map(int, input().split())))

t = int(input())

for i in range(t):
    input() # n
    a = input_list_numbers()
    print(max(a) - min(a))
